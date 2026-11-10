// Baut den schriftlichen Kommentar «Ube» als Word-Datei aus kommentar.md
// Aufruf: node build.js kommentar.md out.docx [pages.json]
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, Footer, PageNumber,
  FootnoteReferenceRun, TableOfContents, Bookmark, ImageRun, Table, TableRow, TableCell,
  WidthType, ShadingType, BorderStyle, TabStopType, NumberFormat, VerticalAlign, LineRuleType,
} = require("docx");

const SRC = process.argv[2];
const OUT = process.argv[3];
const PAGES = process.argv[4] && fs.existsSync(process.argv[4]) ? JSON.parse(fs.readFileSync(process.argv[4], "utf8")) : {};
const BASE = path.dirname(path.resolve(SRC));

const BODY = "Cambria";
const HEAD = "Calibri";
const VIOLET = "5B2A86";
const INK2 = "52514E";
const TEXTW = 9072; // A4 minus 2 x 2.5 cm
const SZ = 22; // 11 pt
const LINE = 336; // 1.4 Zeilenabstand
const LANG = { value: "de-CH" };

// ---------------------------------------------------------------- Parser
const raw = fs.readFileSync(SRC, "utf8").replace(/\r/g, "");
const meta = {};
const blocks = [];
{
  const lines = raw.split("\n");
  let para = [];
  const flush = () => { if (para.length) { blocks.push({ t: "p", text: para.join(" ") }); para = []; } };
  for (let i = 0; i < lines.length; i++) {
    const L = lines[i];
    if (L.startsWith("% ")) { const m = L.slice(2).match(/^(\w+):\s*(.*)$/); meta[m[1]] = m[2]; continue; }
    if (L.startsWith("# ")) { flush(); blocks.push({ t: "h1", text: L.slice(2).trim() }); continue; }
    if (L.startsWith("## ")) { flush(); blocks.push({ t: "h2", text: L.slice(3).trim() }); continue; }
    if (L.startsWith(":::figure")) { flush(); const [p, c] = L.slice(9).split("|").map(s => s.trim()); blocks.push({ t: "fig", path: p, cap: c }); continue; }
    if (L.startsWith(":::placeholder")) { flush(); const [c, b] = L.slice(14).split("|").map(s => s.trim()); blocks.push({ t: "phfig", cap: c, box: b }); continue; }
    if (L.startsWith(":::table")) {
      flush(); const cap = L.slice(8).trim(); const rows = [];
      for (i++; i < lines.length && !lines[i].startsWith(":::"); i++) {
        if (lines[i].trim().startsWith("|")) rows.push(lines[i].trim().replace(/^\||\|$/g, "").split("|").map(s => s.trim()));
      }
      blocks.push({ t: "table", cap, rows }); continue;
    }
    if (L.startsWith(":::refs")) {
      flush(); const items = [];
      for (i++; i < lines.length && !lines[i].startsWith(":::"); i++) if (lines[i].trim()) items.push(lines[i].trim());
      blocks.push({ t: "refs", items }); continue;
    }
    // "~ " = wörtlicher Text in kleiner Schrift (Prompts in den Anhängen), ohne Fussnoten- oder Platzhalter-Auswertung
    if (L.startsWith("~ ") || L === "~") { flush(); blocks.push({ t: "small", text: L.slice(2) }); continue; }
    if (L.startsWith("> ")) { flush(); blocks.push({ t: "quote", text: L.slice(2).trim() }); continue; }
    if (!L.trim()) { flush(); continue; }
    para.push(L.trim());
  }
  flush();
}

// Inline: [^Fussnote] mit Klammertiefe, {{Platzhalter}}
function parseInline(s) {
  const out = [];
  let buf = "";
  let i = 0;
  const pushText = () => { if (buf) { out.push({ k: "t", v: buf }); buf = ""; } };
  while (i < s.length) {
    if (s.startsWith("[^", i)) {
      pushText();
      let d = 0, j = i;
      for (; j < s.length; j++) { if (s[j] === "[") d++; else if (s[j] === "]") { d--; if (d === 0) break; } }
      out.push({ k: "fn", v: s.slice(i + 2, j) });
      i = j + 1; continue;
    }
    if (s.startsWith("{{", i)) {
      pushText();
      const j = s.indexOf("}}", i);
      out.push({ k: "ph", v: s.slice(i + 2, j) });
      i = j + 2; continue;
    }
    buf += s[i]; i++;
  }
  pushText();
  return out;
}

// ---------------------------------------------------------------- Fussnoten
const footnotes = {};
let fnId = 0;
function fnParagraph(text) {
  const runs = [new TextRun({ text: " ", font: BODY, size: 18 })];
  for (const r of parseInline(text)) {
    if (r.k === "ph") runs.push(new TextRun({ text: `[${r.v}]`, highlight: "yellow", font: BODY, size: 18, language: LANG }));
    else runs.push(new TextRun({ text: r.v, font: BODY, size: 18, language: LANG }));
  }
  return new Paragraph({ children: runs, spacing: { after: 40, line: 240 }, alignment: AlignmentType.LEFT });
}

function runsFor(text, opts = {}) {
  const runs = [];
  for (const r of parseInline(text)) {
    if (r.k === "t") runs.push(new TextRun({ text: r.v, font: opts.font || BODY, size: opts.size || SZ, bold: opts.bold, italics: opts.italics, color: opts.color, language: LANG }));
    else if (r.k === "ph") runs.push(new TextRun({ text: `[${r.v}]`, font: opts.font || BODY, size: opts.size || SZ, highlight: "yellow", language: LANG }));
    else if (r.k === "fn") {
      fnId++;
      footnotes[fnId] = { children: [fnParagraph(r.v)] };
      runs.push(new FootnoteReferenceRun(fnId));
    }
  }
  return runs;
}

// ---------------------------------------------------------------- Bausteine
const children = [];
const tocEntries = [];
let bm = 0;
const BREAK_BEFORE = [/^1 /, /^10 /, /^11 /, /^Anhang/];

function heading(level, text) {
  bm++;
  const id = `_Ube${bm}`;
  const pageBreakBefore = level === 1 && BREAK_BEFORE.some(r => r.test(text));
  tocEntries.push({ title: text, level, href: id, page: PAGES[text] !== undefined ? String(PAGES[text]) : "00" });
  return new Paragraph({
    heading: level === 1 ? HeadingLevel.HEADING_1 : HeadingLevel.HEADING_2,
    pageBreakBefore,
    children: [new Bookmark({ id, children: [new TextRun({ text, language: LANG })] })],
  });
}

const border = { style: BorderStyle.SINGLE, size: 4, color: "C3C2B7" };
const borders = { top: border, bottom: border, left: border, right: border };

function table(b) {
  const n = b.rows[0].length;
  const widths = n === 2 ? [Math.round(TEXTW * 0.44), TEXTW - Math.round(TEXTW * 0.44)] : Array(n).fill(Math.floor(TEXTW / n));
  const rows = b.rows.map((r, ri) => new TableRow({
    tableHeader: ri === 0,
    cantSplit: true,
    children: r.map((c, ci) => new TableCell({
      width: { size: widths[ci], type: WidthType.DXA },
      borders,
      margins: { top: 60, bottom: 60, left: 100, right: 100 },
      shading: ri === 0 ? { fill: "EFE9F7", type: ShadingType.CLEAR, color: "auto" } : undefined,
      verticalAlign: VerticalAlign.TOP,
      children: [new Paragraph({ spacing: { after: 0, line: 260 }, alignment: AlignmentType.LEFT,
        keepNext: ri === b.rows.length - 2,
        children: runsFor(c, { font: HEAD, size: 19, bold: ri === 0 }) })],
    })),
  }));
  const [lab, ...rest] = b.cap.split(":");
  children.push(new Paragraph({ keepNext: true, spacing: { before: 200, after: 80 },
    children: [new TextRun({ text: lab + ":", font: HEAD, size: 19, bold: true, color: INK2, language: LANG }),
      ...runsFor(rest.join(":"), { font: HEAD, size: 19, color: INK2 })] }));
  children.push(new Table({ width: { size: TEXTW, type: WidthType.DXA }, columnWidths: widths, rows }));
  children.push(new Paragraph({ spacing: { before: 0, after: 0, line: 160, lineRule: LineRuleType.AUTO }, children: [] }));
}

function caption(text) {
  const [lab, ...rest] = text.split(":");
  return new Paragraph({ spacing: { before: 60, after: 240, line: 260 }, alignment: AlignmentType.LEFT,
    children: [new TextRun({ text: lab + ":", font: HEAD, size: 19, bold: true, color: INK2, language: LANG }),
      ...runsFor(rest.join(":"), { font: HEAD, size: 19, color: INK2 })] });
}

function figure(b) {
  const p = path.join(BASE, b.path);
  const buf = fs.readFileSync(p);
  // PNG-Grösse lesen
  const w = buf.readUInt32BE(16), h = buf.readUInt32BE(20);
  const W = 605; // Pixel bei 96 dpi = 16 cm
  children.push(new Paragraph({ keepNext: true, alignment: AlignmentType.CENTER, spacing: { before: 160, after: 0, line: 240, lineRule: LineRuleType.AUTO },
    children: [new ImageRun({ type: "png", data: buf, transformation: { width: W, height: Math.round(W * h / w) },
      altText: { title: b.cap.split(":")[0], description: b.cap, name: b.cap.split(":")[0] } })] }));
  children.push(caption(b.cap));
}

function phFigure(b) {
  children.push(new Table({ width: { size: TEXTW, type: WidthType.DXA }, columnWidths: [TEXTW], rows: [
    new TableRow({ height: { value: 2600, rule: "atLeast" }, children: [new TableCell({
      width: { size: TEXTW, type: WidthType.DXA }, verticalAlign: VerticalAlign.CENTER,
      borders: { top: { style: BorderStyle.DASHED, size: 6, color: "A58FD6" }, bottom: { style: BorderStyle.DASHED, size: 6, color: "A58FD6" },
        left: { style: BorderStyle.DASHED, size: 6, color: "A58FD6" }, right: { style: BorderStyle.DASHED, size: 6, color: "A58FD6" } },
      shading: { fill: "F7F4FB", type: ShadingType.CLEAR, color: "auto" },
      children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: `[${b.box}]`, font: HEAD, size: 20, highlight: "yellow", language: LANG })] })],
    })] })] }));
  children.push(caption(b.cap));
}

// ---------------------------------------------------------------- Titelseite
const titleChildren = [
  new Paragraph({ spacing: { before: 1800, after: 120 }, children: [new TextRun({ text: meta.schule || "", font: HEAD, size: 22, color: INK2, language: LANG })] }),
  new Paragraph({ spacing: { before: 400, after: 120 }, children: [new TextRun({ text: meta.titel || "Ube", font: HEAD, size: 120, bold: true, color: VIOLET, language: LANG })] }),
  new Paragraph({ spacing: { after: 360, line: 320 }, border: { bottom: { style: BorderStyle.SINGLE, size: 18, color: VIOLET, space: 14 } },
    children: [new TextRun({ text: meta.untertitel || "", font: HEAD, size: 30, color: "1F1F1F", language: LANG })] }),
  new Paragraph({ spacing: { before: 600, after: 60 }, children: [new TextRun({ text: meta.autoren || "", font: HEAD, size: 26, bold: true, language: LANG })] }),
  new Paragraph({ spacing: { after: 400 }, children: runsFor(meta.klassen || "", { font: HEAD, size: 22, color: INK2 }) }),
  new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: meta.betreuung || "", font: HEAD, size: 22, color: INK2, language: LANG })] }),
  new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: meta.abgabe || "", font: HEAD, size: 22, color: INK2, language: LANG })] }),
];
// Optionale Zeile «% hinweis: …» (z. B. Kennzeichnung als Arbeitsfassung); {{…}} wird gelb markiert.
if (meta.hinweis) titleChildren.push(new Paragraph({ spacing: { before: 500, after: 60, line: 300 }, children: runsFor(meta.hinweis, { font: HEAD, size: 20, color: INK2 }) }));

// ---------------------------------------------------------------- Hauptteil
let tocIndex = -1;
for (const b of blocks) {
  if (b.t === "h1") {
    if (b.text === "Abstract") {
      children.push(new Paragraph({ style: "Unnummeriert", children: [new TextRun({ text: "Abstract", language: LANG })] }));
      continue;
    }
    if (b.text === "Inhaltsverzeichnis") {
      children.push(new Paragraph({ style: "Unnummeriert", pageBreakBefore: true, children: [new TextRun({ text: "Inhaltsverzeichnis", language: LANG })] }));
      tocIndex = children.length; children.push(null); // Platzhalter, wird unten ersetzt
      continue;
    }
    children.push(heading(1, b.text));
  } else if (b.t === "h2") children.push(heading(2, b.text));
  else if (b.t === "p") children.push(new Paragraph({ alignment: AlignmentType.JUSTIFIED, children: runsFor(b.text) }));
  else if (b.t === "quote") children.push(new Paragraph({ alignment: AlignmentType.LEFT, keepLines: true,
    indent: { left: 567, right: 340 }, spacing: { before: 120, after: 200 },
    border: { left: { style: BorderStyle.SINGLE, size: 18, color: VIOLET, space: 10 } },
    children: runsFor(b.text, { italics: true }) }));
  else if (b.t === "small") children.push(new Paragraph({ alignment: AlignmentType.LEFT,
    spacing: { after: 50, line: 228, lineRule: LineRuleType.AUTO },
    children: [new TextRun({ text: b.text, font: HEAD, size: 17, language: LANG })] }));
  else if (b.t === "table") table(b);
  else if (b.t === "fig") figure(b);
  else if (b.t === "phfig") phFigure(b);
  else if (b.t === "refs") for (const it of b.items) children.push(new Paragraph({ alignment: AlignmentType.LEFT,
    indent: { left: 425, hanging: 425 }, spacing: { after: 110, line: 270 },
    children: runsFor(it, { size: 20 }) }));
}
children[tocIndex] = new TableOfContents("Inhaltsverzeichnis", {
  hyperlink: true, headingStyleRange: "1-2", beginDirty: false, cachedEntries: tocEntries,
});

// ---------------------------------------------------------------- Dokument
const footer = new Footer({ children: [new Paragraph({
  tabStops: [{ type: TabStopType.RIGHT, position: TEXTW }],
  border: { top: { style: BorderStyle.SINGLE, size: 4, color: "E1E0D9", space: 6 } },
  children: [new TextRun({ text: "Schriftlicher Kommentar «Ube»", font: HEAD, size: 17, color: "898781", language: LANG }),
    new TextRun({ children: ["\t", PageNumber.CURRENT], font: HEAD, size: 18, color: INK2 })],
})] });

const pageProps = { page: { size: { width: 11906, height: 16838 }, margin: { top: 1417, bottom: 1417, left: 1417, right: 1417, footer: 680 } } };

const doc = new Document({
  creator: "Aezri Peglow, Tim Rosal, John Meuwly",
  title: "Ube – Schriftlicher Kommentar",
  description: "Schriftlicher Kommentar zur Maturaarbeit «Ube», Kantonsschule Baden 2026",
  features: { updateFields: false },
  hyphenation: { autoHyphenation: true, consecutiveHyphenLimit: 2, doNotHyphenateCaps: true, hyphenationZone: 357 },
  styles: {
    default: {
      document: { run: { font: BODY, size: SZ, language: LANG }, paragraph: { spacing: { after: 140, line: LINE, lineRule: LineRuleType.AUTO } } },
      heading1: { run: { font: HEAD, size: 32, bold: true, color: VIOLET }, paragraph: { spacing: { before: 420, after: 180, line: 276, lineRule: LineRuleType.AUTO }, keepNext: true, keepLines: true } },
      heading2: { run: { font: HEAD, size: 25, bold: true, color: "1F1F1F" }, paragraph: { spacing: { before: 280, after: 100, line: 276, lineRule: LineRuleType.AUTO }, keepNext: true, keepLines: true } },
    },
    paragraphStyles: [
      { id: "Unnummeriert", name: "Ueberschrift ohne Nummer", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font: HEAD, size: 32, bold: true, color: VIOLET }, paragraph: { spacing: { before: 0, after: 240, line: 276, lineRule: LineRuleType.AUTO }, keepNext: true } },
      { id: "TOC1", name: "toc 1", basedOn: "Normal", next: "Normal",
        run: { font: HEAD, size: 22, bold: true }, paragraph: { spacing: { before: 140, after: 40, line: 260 } } },
      { id: "TOC2", name: "toc 2", basedOn: "Normal", next: "Normal",
        run: { font: HEAD, size: 21 }, paragraph: { indent: { left: 420 }, spacing: { before: 0, after: 30, line: 260 } } },
    ],
    characterStyles: [
      { id: "IndexLink", name: "Index Link", run: { color: "000000" } },
    ],
  },
  footnotes,
  sections: [
    { properties: { ...pageProps, titlePage: false }, children: titleChildren },
    { properties: { ...pageProps, page: { ...pageProps.page, pageNumbers: { start: 1, formatType: NumberFormat.DECIMAL } } },
      footers: { default: footer }, children },
  ],
});

Packer.toBuffer(doc).then(buf => { fs.writeFileSync(OUT, buf); console.log(`ok ${OUT} footnotes=${fnId} toc=${tocEntries.length}`); });
