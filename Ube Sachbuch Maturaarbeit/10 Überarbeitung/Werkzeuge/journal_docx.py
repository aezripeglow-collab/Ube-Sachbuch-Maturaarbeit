"""Baut das überarbeitete Arbeitsjournal als Word-Datei.

Quelle: «Arbeitsjournal (überarbeitet).md» in diesem Ordner (Rückblicke über je zwei Wochen).
Ergebnis: Arbeitsjournal_Ube_UEBERARBEITET.docx
Aufruf: python3 Werkzeuge/journal_docx.py
Text ändern: die Markdown-Datei bearbeiten und das Skript neu laufen lassen, oder direkt in Word weiterarbeiten.
"""
import re
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

import sys

HERE = Path(__file__).resolve().parent.parent
# Ohne Argumente: Fassung «UEBERARBEITET». Für die Schlussredaktion:
#   python3 Werkzeuge/journal_docx.py "Arbeitsjournal (Schlussredaktion).md" Arbeitsjournal_Ube_SCHLUSSREDAKTION.docx
SRC = HERE / (sys.argv[1] if len(sys.argv) > 1 else "Arbeitsjournal (überarbeitet).md")
OUT = HERE / (sys.argv[2] if len(sys.argv) > 2 else "Arbeitsjournal_Ube_UEBERARBEITET.docx")

VIOLET = RGBColor(0x5B, 0x2A, 0x86)
INK2 = RGBColor(0x52, 0x51, 0x4E)
BODY, HEAD = "Cambria", "Calibri"

text = SRC.read_text(encoding="utf8")
text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)  # Frontmatter weg
lines = [l.rstrip() for l in text.split("\n")]

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
sec.left_margin = sec.right_margin = Cm(2.3)
sec.top_margin, sec.bottom_margin = Cm(2.2), Cm(2.2)

st = doc.styles["Normal"]
st.font.name, st.font.size = BODY, Pt(10.5)
st.element.rPr.rFonts.set(qn("w:eastAsia"), BODY)
lang = OxmlElement("w:lang")
lang.set(qn("w:val"), "de-CH")
st.element.rPr.append(lang)
st.paragraph_format.space_after = Pt(6)
st.paragraph_format.line_spacing = 1.25


def run(par, txt, font=BODY, size=10.5, bold=False, color=None, italic=False):
    r = par.add_run(txt)
    r.font.name, r.font.size, r.font.bold, r.font.italic = font, Pt(size), bold, italic
    r._element.rPr.rFonts.set(qn("w:eastAsia"), font)
    if color is not None:
        r.font.color.rgb = color
    return r


def shade(cell, hexcolor):
    tcPr = cell._element.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hexcolor)
    tcPr.append(shd)


def cell_margins(table, top=70, bottom=70, left=110, right=110):
    tblPr = table._element.tblPr
    m = OxmlElement("w:tblCellMar")
    for k, v in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        e = OxmlElement(f"w:{k}")
        e.set(qn("w:w"), str(v))
        e.set(qn("w:type"), "dxa")
        m.append(e)
    tblPr.append(m)


def borders(table, color="D9D4E3"):
    tblPr = table._element.tblPr
    b = OxmlElement("w:tblBorders")
    for k in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement(f"w:{k}")
        e.set(qn("w:val"), "single")
        e.set(qn("w:sz"), "4")
        e.set(qn("w:space"), "0")
        e.set(qn("w:color"), color)
        b.append(e)
    tblPr.append(b)


def fixed_widths(table):
    """Feste Spaltenbreiten, damit Word und LibreOffice die Tabelle über die ganze Textbreite setzen."""
    tblPr = table._element.tblPr
    for tag in ("w:tblW", "w:tblLayout"):
        for old in tblPr.findall(qn(tag)):
            tblPr.remove(old)
    w = OxmlElement("w:tblW")
    w.set(qn("w:w"), str(int((W_LABEL + W_TEXT) / 635)))
    w.set(qn("w:type"), "dxa")
    tblPr.append(w)
    lay = OxmlElement("w:tblLayout")
    lay.set(qn("w:type"), "fixed")
    tblPr.append(lay)
    grid = table._element.find(qn("w:tblGrid"))
    for gc, width in zip(grid.findall(qn("w:gridCol")), (W_LABEL, W_TEXT)):
        gc.set(qn("w:w"), str(int(width / 635)))


def keep_next(par):
    par.paragraph_format.keep_with_next = True


def page_field(par):
    r = par.add_run()
    for kind, txt in (("begin", None), (None, "PAGE"), ("end", None)):
        if kind:
            f = OxmlElement("w:fldChar")
            f.set(qn("w:fldCharType"), kind)
            r._element.append(f)
        else:
            it = OxmlElement("w:instrText")
            it.set(qn("xml:space"), "preserve")
            it.text = txt
            r._element.append(it)
    r.font.name, r.font.size = HEAD, Pt(9)


# Fusszeile
fp = sec.footer.paragraphs[0]
run(fp, "Arbeitsjournal «Ube – Zwischen Tradition und Trend» · Seite ", HEAD, 8.5, color=INK2)
page_field(fp)

W_LABEL, W_TEXT = Cm(3.5), Cm(12.9)
rows, n_rueck = [], 0


def flush_rows():
    global rows
    if not rows:
        return
    t = doc.add_table(rows=0, cols=2)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    fixed_widths(t)
    borders(t)
    cell_margins(t)
    for label, content in rows:
        c = t.add_row().cells
        c[0].width, c[1].width = W_LABEL, W_TEXT
        shade(c[0], "F3EEF9" if label != "Aus heutiger Sicht" else "ECEBE6")
        p0 = c[0].paragraphs[0]
        p0.paragraph_format.space_after = Pt(0)
        run(p0, label, HEAD, 9.5, bold=True)
        p1 = c[1].paragraphs[0]
        p1.paragraph_format.space_after = Pt(0)
        p1.paragraph_format.line_spacing = 1.22
        run(p1, content, BODY, 10, italic=(label == "Aus heutiger Sicht"))
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    rows = []


for L in lines:
    if not L.strip():
        continue
    if L.startswith("# "):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(4)
        run(p, L[2:], HEAD, 19, bold=True, color=VIOLET)
        continue
    if L.startswith("## "):
        flush_rows()
        title = L[3:]
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(5)
        keep_next(p)
        run(p, title, HEAD, 12.5, bold=True, color=VIOLET)
        if title.startswith("Rückblick"):
            n_rueck += 1
        continue
    m = re.match(r"\*\*(.+?):\*\*\s*(.*)$", L)
    if m:
        rows.append((m.group(1), m.group(2)))
        continue
    flush_rows()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY if len(L) > 160 else WD_ALIGN_PARAGRAPH.LEFT
    if L.startswith("Tim Rosal und Aezri Peglow"):
        run(p, L, HEAD, 10, color=INK2)
    else:
        run(p, L, BODY, 10.5)
flush_rows()

doc.core_properties.author = "Tim Rosal, Aezri Peglow, John Meuwly"
doc.core_properties.title = "Arbeitsjournal zur Maturaarbeit «Ube – Zwischen Tradition und Trend»"
doc.save(OUT)
print("ok", OUT.name, "Rückblicke:", n_rueck)
