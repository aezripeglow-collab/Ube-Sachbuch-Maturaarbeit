"""Baut das finale Arbeitsjournal (für Claude).

Quelle: die 45 Einträge in `03 Arbeitsjournal/*/*.md` (unverändert).
Ergebnis:
  - ARBEITSJOURNAL_FINAL.md  (Lesekopie in 09 Finalisierung)
  - Arbeitsjournal_Ube_FINAL.docx  (Tabelle wie die Original-Word-Datei: A4 quer, 6 Spalten, Arial 8,5 pt)

Regeln: keine neuen Ereignisse, nur belegte Korrekturen (FIX), Prüfvermerke (CHECK) als gelbe Stellen,
sprachliche Entzerrung der KI-ausformulierten Einträge (ab 05.06.) mit VARY, Originaleinträge bis 03.06. unverändert.
Aufruf: python3 journal_final.py
"""
import re, itertools, datetime
from pathlib import Path

ROOT = Path("/home/claude/ube-sachbuch-maturaarbeit/Ube Sachbuch Maturaarbeit")
J = ROOT / "03 Arbeitsjournal"
HERE = ROOT / "09 Finalisierung"
OUT_MD = HERE / "ARBEITSJOURNAL_FINAL.md"
OUT_DOCX = HERE / "Arbeitsjournal_Ube_FINAL.docx"

files = sorted(J.glob("*/*.md"), key=lambda p: p.name)

# ---------------------------------------------------------------- Korrekturen (belegt)
FIX = {
 # 16.09.: keine Korrektur mehr. Die Angabe «Berichte ab 11. September» aus der zweiten Runde liess sich am 9.11.
 # nicht bestätigen (früheste gefundene Berichte: Context.ph 13.09., DA/FreshPlaza/Tribune 14.09.); das Original (13./14.09.) bleibt.
 "2026-10-21": [
  ("- 300 Mio. Pesos (rund 4,7 Mio. US-Dollar) und 34,1 Mio. US-Dollar aus den USA",
   "- 300 Mio. Pesos (rund 5 Mio. US-Dollar) und 34,1 Mio. US-Dollar aus den USA {{Umrechnung: mit dem Kurs vom Oktober 2026 rund 5,1 Mio., so rechnet FreshPlaza am 6.10.; im Buch steht noch 4,7}}"),
 ],
 "2026-10-23": [
  ("- Interviewfrage zu Kosten und Pflanzmaterial vorgeschlagen",
   "- Interviewfrage zu Kosten und Pflanzmaterial vorgeschlagen {{prüfen: Im Transkript gibt es keine Kostenfrage. Hier ergänzen, dass der Vorschlag nicht in die zehn Fragen kam, oder den Punkt streichen.}}"),
  ("Ich hoffe, dass das Interview hier weiterhilft, und habe deshalb eine Frage zu jungen Leuten im Anbau aufgenommen.",
   "Ich hoffe, dass das Interview hier weiterhilft.{{prüfen: Im Journal vom 8.11. stand hier, John habe eine Frage zu jungen Leuten im Anbau aufgenommen. In den zehn Fragen (Anhang A des Kommentars) gibt es keine solche Frage; Tita hat die junge Generation bei Frage 9 von sich aus erwähnt. Falls John die Frage vorgeschlagen hat, hier sagen, warum sie nicht aufgenommen wurde.}}"),
 ],
 "2026-10-28": [
  ("Fragen zu Preisen, Nachfrage, Sorten und zur Zukunft des Anbaus habe ich ergänzt.",
   "Fragen zu Preisen, Nachfrage und zur Zukunft des Anbaus habe ich ergänzt."),
  ("meine Frage zu Kosten und Zukunft des Anbaus geprüft.",
   "die Frage zur Zukunft des Anbaus geprüft, die ich gebraucht habe.{{prüfen: Eine Kostenfrage steht nicht in den zehn Fragen (Anhang A des Kommentars). Falls Tim eine vorgeschlagen hat, hier sagen, warum sie nicht aufgenommen wurde.}}"),
  ("Die Frage nach den Kosten hat Aezri bewusst einfach gehalten, damit Tita sie gut beantworten kann.",
   "{{prüfen: Im Journal vom 8.11. stand hier, Aezri habe die Kostenfrage bewusst einfach gehalten. Weil es in den zehn Fragen keine Kostenfrage gibt, ist der Satz gestrichen.}}"),
  ("Bei den Interviewfragen habe ich geprüft, ob eine Frage zur Meinung über den Trend und eine zu jungen Leuten im Anbau dabei ist.",
   "Bei den Interviewfragen habe ich geprüft, ob eine Frage zur Meinung über den Trend dabei ist.{{prüfen: Im Journal vom 8.11. stand zusätzlich eine Frage zu jungen Leuten im Anbau. Die gibt es in den zehn Fragen nicht, deshalb gestrichen.}}"),
 ],
 "2026-11-04": [
  ("Stellen, die ich nicht sicher verstanden habe, habe ich markiert.",
   "{{prüfen: Im Journal vom 8.11. stand hier, Aezri habe unsichere Stellen markiert. Im Transkript (Anhang A) ist nichts markiert, deshalb ist der Satz gestrichen. Falls es Markierungen gab, hier nachtragen.}}"),
  ("Tita sagt aber ausdrücklich, dass Bauern und Händler von den höheren Preisen profitieren.",
   "Tita sagt aber ausdrücklich, dass Bauern und Verkäufer von den höheren Preisen profitieren."),
  ("Zu den Kosten hat Tita leider nichts Genaues gesagt, deshalb bleibt meine Lücke bestehen. Ich war zuerst enttäuscht, aber eigentlich zeigt das, wie schwer diese Zahlen zu bekommen sind.",
   "Nach den Kosten haben wir sie allerdings gar nicht gefragt, das ist mir erst jetzt aufgefallen, deshalb bleibt meine Lücke bestehen.{{prüfen: Satz so übernehmen oder anders erklären, warum keine Kostenfrage gestellt wurde}}"),
 ],
 "2026-11-06": [
  ("Ich habe Teil 2 und das zusammengeführte Kapitel 3 von Aezri übernommen und die Seiten mit Bildern gestaltet.",
   "Ich habe Teil 2 und das zusammengeführte Kapitel 3 von Aezri übernommen und die Seiten von Teil 2 mit Bildern gestaltet."),
  ("Für die Bilder habe ich unsere eigenen Fotos verwendet und, wo wir keine eigenen hatten, Bilder aus einer Bilddatenbank.",
   "Für die Bilder habe ich Tims Liste verwendet, die meisten stammen aus einer Bilddatenbank.{{prüfen: Gibt es eigene Fotos im Buch?}}"),
  ("Bei Kapitel 3 habe ich die Thesen jeweils auf einer neuen Seite beginnen lassen und die Fazits farbig hervorgehoben.",
   "Bei Kapitel 3 habe ich die Thesen jeweils auf einer neuen Seite beginnen lassen. Bilder hat dieses Kapitel noch keine, und die Fazits will ich hervorheben, sobald der Text steht."),
  ("Bei Kapitel 3 war es schwieriger, weil dort viel Text steht und Bilder nicht immer passen. Die farbigen Fazits helfen, dass man beim Durchblättern sieht, wo eine These endet.",
   "Bei Kapitel 3 war es schwieriger, weil dort viel Text steht und Bilder nicht immer passen. Farbig hervorgehobene Fazits würden helfen, dass man beim Durchblättern sieht, wo eine These endet."),
  ("- Eigene Fotos und Bilddatenbank, jede Quelle notiert",
   "- Bilder aus Tims Liste, jede Quelle notiert"),
 ],
}

# ---------------------------------------------------------------- Prüfvermerke (nur die Gruppe kann sie bestätigen)
CHECK = {
 "2026-05-27": "Aezri: kein Eintrag. Laut Johns Eintrag war sie dabei. Ergänzen oder so lassen.",
 "2026-06-05": "Ab hier wurden die Einträge am 8.11. mit Claude aus unseren Stichworten ausformuliert (siehe KI-Nachweis). Bei jedem Eintrag prüfen: Stimmt, was da steht, und war es wirklich an diesem Tag?",
 "2026-06-17": "Angenommen: Abgabe des Kochbuch-Kommentars am 17.06. und Treffen bei John.",
 "2026-06-26": "Angenommen: Besprechung per Teams am Abend.",
 "2026-07-03": "Angenommen: Teams-Call am Nachmittag; Tims Fragenliste auf Englisch und Tagalog.",
 "2026-07-15": "Angenommen: Reisedaten von Tim und John, Aezris Arbeit zu Hause, Nachrichten untereinander.",
 "2026-07-24": "Angenommen: Reisedaten, Nachrichten untereinander.",
 "2026-08-05": "Angenommen: Abbruch der Befragung an diesem Tag, keine Fotos.",
 "2026-08-19": "Angenommen: Teams-Call am Abend.",
 "2026-08-21": "Angenommen: Johns Skizze für das Titelblatt.",
 "2026-09-16": "Angenommen: Treffen am Montag, 14.09., nach der Schule.",
 "2026-09-25": "Angenommen: Treffen bei John in Turgi.",
 "2026-09-30": "Angenommen: Teams-Call.",
 "2026-10-23": "Angenommen: Teams-Call am Abend.",
 "2026-10-28": "Am 8.11. ergänzt: Tims Bildersuche und Johns Karte. Prüfen, ob beides an diesem Tag begonnen hat.",
 "2026-10-30": "Angenommen: gegenseitiges Lesen von These 4 Ende Oktober.",
 "2026-11-04": "Am 8.11. ergänzt: Tims Bilder und Korrekturlesen, Johns Start in InDesign. Prüfen.",
 "2026-11-06": "Johns Eintrag ist an das Buch-PDF vom 8.11. angepasst (keine Bilder in Kapitel 3, Fazits noch nicht hervorgehoben). Im PDF vom 8.11. fehlen Quellenverzeichnis, Bildnachweis und Schlusswort noch; Aezris Quellenverzeichnis aus Word liegt uns nicht vor. Wer hat die drei Kurzeinleitungen auf den Kapitelseiten geschrieben?",
}

# ---------------------------------------------------------------- Sprachliche Varianten je Person (nur KI-ausformulierte Einträge)
VAR = {
 "Aezri": {
  "Ich habe mich gefragt, ob": ["Ich war nicht sicher, ob", "Offen war für mich, ob", "Ich habe mich gefragt, ob"],
  "Ich habe mich auch gefragt, ob": ["Nicht sicher war ich auch, ob", "Ich habe mich auch gefragt, ob"],
  "Ich habe mich gefragt, wie": ["Ich wusste nicht, wie", "Ich habe mich gefragt, wie"],
  "Ich habe mich gefragt, was": ["Offen war für mich, was", "Ich habe mich gefragt, was"],
  "Ich habe mich gefragt, warum": ["Mich hat beschäftigt, warum", "Ich habe mich gefragt, warum"],
  "Dabei ist mir aufgefallen, dass": ["Dabei habe ich gemerkt, dass", "Aufgefallen ist mir, dass", "Dabei ist mir aufgefallen, dass"],
  "Mir ist aufgefallen, dass": ["Aufgefallen ist mir, dass", "Mir ist aufgefallen, dass"],
 },
 "Tim": {
  "Ich habe mich gefragt, ob": ["Unklar war für mich, ob", "Ich wusste nicht, ob", "Ich habe mich gefragt, ob"],
  "Ich habe mich auch gefragt, ob": ["Unklar war für mich auch, ob", "Ich habe mich auch gefragt, ob"],
  "Ich habe mich gefragt, wie": ["Unklar war für mich noch, wie", "Ich habe mich gefragt, wie"],
  "Ich habe mich gefragt, was": ["Ich wusste nicht, was", "Ich habe mich gefragt, was"],
  "Ich habe mich gefragt, warum": ["Ich wusste nicht, warum", "Ich habe mich gefragt, warum"],
  "Dabei ist mir aufgefallen, dass": ["Dabei habe ich festgestellt, dass", "Dabei ist mir aufgefallen, dass"],
  "Mir ist aufgefallen, dass": ["Ich habe festgestellt, dass", "Mir ist aufgefallen, dass"],
  "zum Beispiel": ["beispielsweise", "zum Beispiel"],
 },
 "John": {
  "Ich habe mich gefragt, ob": ["Ich war unsicher, ob", "Ich habe mich gefragt, ob"],
  "Ich habe mich auch gefragt, ob": ["Unsicher war ich auch, ob", "Ich habe mich auch gefragt, ob"],
  "Ich habe mich gefragt, wie": ["Ich wusste noch nicht, wie", "Ich habe mich gefragt, wie"],
  "Ich habe mich gefragt, was": ["Ich wusste nicht, was", "Ich habe mich gefragt, was"],
  "Ich habe mich gefragt, warum": ["Ich habe mich gefragt, warum"],
  "Dabei ist mir aufgefallen, dass": ["Dabei habe ich gesehen, dass", "Dabei ist mir aufgefallen, dass"],
  "Mir ist aufgefallen, dass": ["Ich habe gesehen, dass", "Mir ist aufgefallen, dass"],
 },
}
counters = {p: {k: itertools.cycle(v) for k, v in d.items()} for p, d in VAR.items()}

def vary(text, person):
    d = VAR.get(person)
    if not d:
        return text
    for pat in sorted(d, key=len, reverse=True):
        text = re.sub(re.escape(pat), lambda m: next(counters[person][pat]), text)
    return text

# ---------------------------------------------------------------- Einträge einlesen
PHASES = [
 ("1 ", "April bis Juli 2026: Kochbuch «Salu-Salo»"),
 ("2 ", "Juli und August 2026: Sommerferien und Befragung"),
 ("3 ", "August 2026: Wechsel zu Ube"),
 ("4 ", "August bis November 2026: Sachbuch über Ube"),
]
WEEKDAYS = {0:"Mo",1:"Di",2:"Mi",3:"Do",4:"Fr",5:"Sa",6:"So"}

def parse(path):
    key = path.name[:10]
    raw = path.read_text(encoding="utf8")
    body = re.sub(r"^---\n.*?\n---\n", "", raw, flags=re.S)
    body = re.sub(r"^(\[\[20|← \(Beginn\)).*\n", "", body, flags=re.M)
    body = re.sub(r"\n---\n.*$", "\n", body, flags=re.S)
    body = re.sub(r"^> \[!note\].*\n(> .*\n)*", "", body, flags=re.M)
    body = re.sub(r"^Bezug: .*\n\n?", "", body, flags=re.M)
    original = "Unverändert aus dem ursprünglichen Arbeitsjournal" in raw
    for old, new in FIX.get(key, []):
        if old not in body:
            print("NICHT GEFUNDEN", key, old[:60])
        body = body.replace(old, new)
    # Personen-Abschnitte
    persons = []
    parts = re.split(r"^## (.+?)\n", body, flags=re.M)
    for i in range(1, len(parts), 2):
        name, sect = parts[i].strip(), parts[i+1]
        if not original:
            pkey = name if name in VAR else None
            if pkey:
                sect = vary(sect, pkey)
        wo = re.search(r"\*\*Wo:\*\*\s*(.+)", sect)
        def grab(h):
            m = re.search(r"### " + h + r"\s*\n(.*?)(?=\n### |\Z)", sect, re.S)
            return m.group(1).strip() if m else ""
        persons.append({
            "name": name,
            "wo": wo.group(1).strip() if wo else "",
            "was": grab("Was"),
            "vorgehen": grab("Vorgehen und Methode"),
            "reflexion": grab("Reflexion"),
            "erkenntnisse": grab("Wichtige Erkenntnisse"),
            "leer": "(kein Eintrag)" in sect and not grab("Was"),
        })
    d = datetime.date.fromisoformat(key)
    return {"key": key, "date": d, "phase": path.parent.name[:2], "persons": persons, "original": original, "check": CHECK.get(key)}

entries = [parse(p) for p in files]

# ---------------------------------------------------------------- Vorlagen für die fehlenden Einträge (nur Fakten, die aus dem Chat/KI-Nachweis belegt sind)
TEMPLATES = [
 {"key": "2026-11-08", "persons": [
   {"name": "Aezri", "wo": "{{Ort}}", "was": "{{von euch zu schreiben. Belegt ist: Am 8.11. hat Aezri das Buch-PDF (Stand 8.11., 52 Seiten) in den Chat mit Claude gestellt und mit mehreren Eingaben den ersten Entwurf des Kommentars und die Ausformulierung des Journals erstellen lassen (KI-Nachweis, Eingaben 1 bis 6).}}", "reflexion": "{{von euch zu schreiben}}", "erkenntnisse": ""},
   {"name": "Tim", "wo": "{{Ort}}", "was": "{{von euch zu schreiben, falls Tim an diesem Tag gearbeitet hat}}", "reflexion": "", "erkenntnisse": ""},
   {"name": "John", "wo": "{{Ort}}", "was": "{{von euch zu schreiben. Belegt ist: Das Buch-PDF vom 8.11. hat 52 Seiten, Kapitel 3 ohne Bilder, Schlusswort und Verzeichnisse noch leer.}}", "reflexion": "", "erkenntnisse": ""},
 ]},
 {"key": "2026-11-09", "persons": [
   {"name": "Aezri", "wo": "{{Ort}}", "was": "{{von euch zu schreiben. Belegt ist: Am 9.11. hat Aezri drei weitere Prompts an Claude gegeben (wissenschaftliche Überarbeitung, Schlusskorrektur mit dem Transkript, Endkontrolle mit Arbeitsjournal) und die Familienchronik als Stilvorlage mitgegeben (KI-Nachweis, Eingaben 7 bis 9).}}", "reflexion": "{{von euch zu schreiben}}", "erkenntnisse": ""},
   {"name": "Tim", "wo": "{{Ort}}", "was": "{{von euch zu schreiben}}", "reflexion": "", "erkenntnisse": ""},
   {"name": "John", "wo": "{{Ort}}", "was": "{{von euch zu schreiben}}", "reflexion": "", "erkenntnisse": ""},
 ]},
 {"key": "2026-11-10", "persons": [
   {"name": "Aezri, Tim und John", "wo": "{{Ort}}", "was": "{{von euch zu schreiben: Abgabe von Buch, Kommentar und Arbeitsjournal.}}", "reflexion": "{{von euch zu schreiben}}", "erkenntnisse": ""},
 ]},
]
for t in TEMPLATES:
    d = datetime.date.fromisoformat(t["key"])
    for p in t["persons"]:
        p.setdefault("vorgehen", ""); p.setdefault("leer", False)
    entries.append({"key": t["key"], "date": d, "phase": "4 ", "persons": t["persons"], "original": False, "check": "Vorlage: Eintrag fehlt noch. Nur eintragen, was wirklich war.", "template": True})

# ---------------------------------------------------------------- Markdown-Lesekopie
def md_mark(t):
    return re.sub(r"\{\{([^}]*)\}\}", r"==[\1]==", t)

md = ["---", "tags: [finalisierung, arbeitsjournal, final]", "stand: " + datetime.date.today().isoformat(), "---",
      "# Arbeitsjournal, finale Fassung (Lesekopie)", "",
      "> [!info] Was diese Datei ist",
      "> Lesekopie der Word-Datei `Arbeitsjournal_Ube_FINAL.docx` (Tabelle wie das Original). Grundlage sind die 45 Einträge in `03 Arbeitsjournal` vom 22.04. bis 06.11.2026, dazu drei Vorlagen für 08. bis 10.11. Einträge bis 03.06. sind unverändert eure eigenen. Einträge ab 05.06. wurden am 8.11. mit Claude aus euren Stichworten ausformuliert; hier sind sie sprachlich leicht entzerrt und an belegten Stellen korrigiert (Liste in [[AENDERUNGSPROTOKOLL_FINAL]]). Gelbe Stellen ==[so]== könnt nur ihr bestätigen oder ausfüllen. Kein Ereignis wurde hinzugefügt.", ""]
cur_phase = None
for e in entries:
    if e["phase"] != cur_phase:
        cur_phase = e["phase"]
        md.append("## " + dict(PHASES)[cur_phase]); md.append("")
    wd = WEEKDAYS[e["date"].weekday()]
    md.append(f"### {wd} {e['date'].strftime('%d.%m.%Y')}")
    if e.get("check"):
        md.append(f"> [!warning] Prüfen\n> {e['check']}")
    md.append("")
    for p in e["persons"]:
        md.append(f"**{p['name']}** · Wo: {md_mark(p['wo'])}")
        if p["leer"]:
            md.append("*(kein Eintrag)*"); md.append(""); continue
        md.append(""); md.append("Was: " + md_mark(p["was"]))
        if p["vorgehen"]: md.append(""); md.append("Vorgehen und Methode: " + md_mark(p["vorgehen"]))
        if p["reflexion"]: md.append(""); md.append("Reflexion: " + md_mark(p["reflexion"]))
        if p["erkenntnisse"]: md.append(""); md.append("Wichtige Erkenntnisse:\n" + md_mark(p["erkenntnisse"]))
        md.append("")
OUT_MD.write_text("\n".join(md) + "\n", encoding="utf8")

# ---------------------------------------------------------------- Word-Tabelle wie das Original
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.section import WD_ORIENT
from docx.enum.text import WD_COLOR_INDEX
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = Document()
sec = doc.sections[0]
sec.orientation = WD_ORIENT.LANDSCAPE
sec.page_width, sec.page_height = Cm(29.7), Cm(21.0)
for side in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
    setattr(sec, side, Cm(1.27))
normal = doc.styles["Normal"]
normal.font.name = "Arial"; normal.font.size = Pt(8.5)
normal.element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
normal.paragraph_format.space_after = Pt(2)

def para(text, size, bold=False, color=None, after=4):
    p = doc.add_paragraph(); r = p.add_run(text); r.font.size = Pt(size); r.bold = bold
    if color: r.font.color.rgb = RGBColor.from_string(color)
    p.paragraph_format.space_after = Pt(after)
    return p
para("Arbeitsjournal Maturaarbeit", 16, True, "5B2A86", 2)
para("Vom Kochbuch «Salu-Salo» zum Sachbuch über Ube", 11, False, None, 2)
para("Aezri Peglow, Tim Rosal und John Meuwly · Kantonsschule Baden · April bis November 2026 · Fassung vom " + datetime.date.today().strftime("%d.%m.%Y") + " (gelbe Stellen: von uns zu prüfen oder auszufüllen)", 9, False, "555555", 8)

def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), hexcolor)
    tcPr.append(shd)

def write_cell(cell, text, bold=False):
    cell.text = ""
    first = True
    blocks = [b for b in re.split(r"\n\s*\n", text.strip()) if b.strip()] or [""]
    for block in blocks:
        lines = block.split("\n")
        for line in lines:
            p = cell.paragraphs[0] if first else cell.add_paragraph()
            first = False
            p.paragraph_format.space_after = Pt(2)
            # Aufzählungen
            if line.strip().startswith("- "):
                line = "• " + line.strip()[2:]
            # gelbe Platzhalter
            pos = 0
            for m in re.finditer(r"\{\{([^}]*)\}\}", line):
                if m.start() > pos:
                    r = p.add_run(line[pos:m.start()]); r.bold = bold
                r = p.add_run("[" + m.group(1) + "]"); r.font.highlight_color = WD_COLOR_INDEX.YELLOW; r.bold = bold
                pos = m.end()
            if pos < len(line):
                r = p.add_run(line[pos:]); r.bold = bold

cols = ["Wann", "Wer", "Was", "Wo", "Reflexion", "Wichtige Erkenntnisse"]
widths = [Cm(1.9), Cm(1.4), Cm(9.6), Cm(2.3), Cm(8.6), Cm(3.3)]
table = doc.add_table(rows=1, cols=6)
table.style = "Table Grid"
table.autofit = False
# feste Spaltenbreiten auch für LibreOffice/Pages: tblLayout fixed + gridCol-Breiten + Tabellenbreite
tblPr = table._tbl.tblPr
lay = OxmlElement("w:tblLayout"); lay.set(qn("w:type"), "fixed"); tblPr.append(lay)
tblW = tblPr.find(qn("w:tblW"))
if tblW is None:
    tblW = OxmlElement("w:tblW"); tblPr.append(tblW)
tblW.set(qn("w:type"), "dxa"); tblW.set(qn("w:w"), str(int(sum(w.twips for w in widths))))
for gc, w in zip(table._tbl.tblGrid.findall(qn("w:gridCol")), widths):
    gc.set(qn("w:w"), str(int(w.twips)))
hdr = table.rows[0].cells
for i, c in enumerate(cols):
    write_cell(hdr[i], c, bold=True); shade(hdr[i], "E6DAF0"); hdr[i].width = widths[i]
# Kopfzeile wiederholen
trPr = table.rows[0]._tr.get_or_add_trPr(); th = OxmlElement("w:tblHeader"); th.set(qn("w:val"), "true"); trPr.append(th)

cur_phase = None
for e in entries:
    if e["phase"] != cur_phase:
        cur_phase = e["phase"]
        row = table.add_row(); m = row.cells[0].merge(row.cells[5])
        write_cell(m, dict(PHASES)[cur_phase], bold=True); shade(m, "F3EEF8")
    first_row = True
    for p in e["persons"]:
        row = table.add_row(); c = row.cells
        for i, w in enumerate(widths): c[i].width = w
        wd = WEEKDAYS[e["date"].weekday()]
        wann = f"{wd} {e['date'].strftime('%d.%m.%Y')}" if first_row else ""
        if first_row and e.get("check"):
            wann += "\n\n{{" + e["check"] + "}}"
        write_cell(c[0], wann); write_cell(c[1], p["name"])
        if p["leer"]:
            write_cell(c[2], "(kein Eintrag)"); write_cell(c[3], p["wo"]); write_cell(c[4], ""); write_cell(c[5], "")
        else:
            was = p["was"] + (("\n\nVorgehen und Methode: " + p["vorgehen"]) if p["vorgehen"] else "")
            write_cell(c[2], was); write_cell(c[3], p["wo"]); write_cell(c[4], p["reflexion"]); write_cell(c[5], p["erkenntnisse"])
        first_row = False

doc.save(OUT_DOCX)
n = sum(len(e["persons"]) for e in entries)
print("fertig:", OUT_MD.name, OUT_DOCX.name, "| Einträge:", len(entries), "| Personenzeilen:", n)
