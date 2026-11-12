"""Baut die Word-Datei des Kommentars aus einer Quelldatei in diesem Ordner.

Fassung «UEBERARBEITET» (Masterprompt vom 9.11., 23:51):
    python3 Werkzeuge/build.py
Fassung «SCHLUSSREDAKTION» (Prompt vom 10.11., 01:42), mit PDF im Ordner:
    python3 Werkzeuge/build.py Schriftlicher_Kommentar_Ube_SCHLUSSREDAKTION.docx kommentar_quelle_schlussredaktion.txt "Kommentar (Schlussredaktion).md" OFFENE_PUNKTE_SCHLUSSREDAKTION --pdf

Argumente (alle freiwillig): Name der Word-Datei, Quelldatei, Name der Lesekopie, Notiz für den Verweis im Kopf der Lesekopie, --pdf.
Das eigentliche Word-Skript ist `08 Schriftlicher Kommentar/Quelldateien/build.js`.

Zwei Durchgänge: zuerst die Seitenzahlen für das Inhaltsverzeichnis ermitteln, dann final bauen.
Danach wird die Word-Datei in den Ordner «08 Schriftlicher Kommentar» kopiert und die Notiz
«Kommentar Volltext» neu erzeugt. Text ändern: kommentar_quelle.txt bearbeiten.
Braucht: node mit dem Paket docx, LibreOffice, pdfinfo/pdftotext, zip.
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TOOLS = HERE.parent / "08 Schriftlicher Kommentar" / "Quelldateien"
ARGS = [a for a in sys.argv[1:] if not a.startswith("--")]
WITH_PDF = "--pdf" in sys.argv
FINAL = ARGS[0] if len(ARGS) > 0 else "Schriftlicher_Kommentar_Ube_UEBERARBEITET.docx"
SRC = HERE / (ARGS[1] if len(ARGS) > 1 else "kommentar_quelle.txt")
MD_NAME = ARGS[2] if len(ARGS) > 2 else "Kommentar (überarbeitet).md"
NOTIZ = ARGS[3] if len(ARGS) > 3 else "PRUEFBERICHT"
BUILD = Path(tempfile.gettempdir()) / ("kommentar-build-" + Path(FINAL).stem.split("_")[-1].lower())


def find_soffice():
    for base in (Path.home() / ".claude" / "skills", Path("/mnt/skills")):
        if base.exists():
            hits = sorted(base.glob("**/docx/scripts/office/soffice.py"))
            if hits:
                return ["python3", str(hits[0])]
    return ["soffice"]


SOFFICE = find_soffice()


def run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        print(r.stdout, r.stderr)
        raise SystemExit(f"Fehler: {cmd}")
    return r.stdout


def build(out, pages=None):
    args = ["node", str(TOOLS / "build.js"), str(SRC), str(out)]
    if pages:
        args.append(str(pages))
    print(run(args).strip())


def to_pdf(docx):
    run(SOFFICE + ["--headless", "--convert-to", "pdf", "--outdir", str(BUILD), str(docx)], cwd=str(BUILD))
    return BUILD / (Path(docx).stem + ".pdf")


def page_texts(pdf):
    n = int(re.search(r"Pages:\s+(\d+)", run(["pdfinfo", str(pdf)])).group(1))
    out = []
    for i in range(1, n + 1):
        t = run(["pdftotext", "-f", str(i), "-l", str(i), "-layout", str(pdf), "-"])
        out.append(re.sub(r"\s+", " ", t.replace("­", "")))
    return out


def headings():
    hs = []
    for line in SRC.read_text(encoding="utf8").splitlines():
        if line.startswith("# ") or line.startswith("## "):
            title = line.split(" ", 1)[1].strip()
            if title not in ("Abstract", "Inhaltsverzeichnis"):
                hs.append(title)
    return hs


def find_pages(pdf):
    texts = page_texts(pdf)
    hs = headings()
    # Inhaltsverzeichnis endet auf der Seite, die den letzten Eintrag enthält
    norm = lambda s: re.sub(r"\s+", " ", s)
    last = norm(hs[-1])
    toc_end = next(i for i, t in enumerate(texts) if last in t)
    pages, start = {}, toc_end + 1
    for h in hs:
        key = norm(h)
        for i in range(start, len(texts)):
            if key in texts[i]:
                pages[h] = i  # PDF-Seite 1 = Titelblatt, Zählung beginnt danach bei 1
                start = i
                break
        else:
            print("nicht gefunden:", h)
    return pages, len(texts)


BUILD.mkdir(exist_ok=True)
p1 = BUILD / "pass1.docx"
build(p1)
pages, n = find_pages(to_pdf(p1))
pj = BUILD / "pages.json"
pj.write_text(json.dumps(pages, ensure_ascii=False, indent=1), encoding="utf8")
final = BUILD / FINAL
for k in range(3):
    build(final, pj)
    pages2, n2 = find_pages(to_pdf(final))
    if pages2 == pages:
        break
    pages = pages2
    pj.write_text(json.dumps(pages, ensure_ascii=False, indent=1), encoding="utf8")
print("PDF-Seiten:", n2)
print(json.dumps(pages, ensure_ascii=False, indent=0))

ziel = HERE / FINAL
shutil.copy(final, ziel)
subprocess.run(["zip", "-d", str(ziel), "*/"], capture_output=True)
if WITH_PDF:
    shutil.copy(BUILD / (Path(FINAL).stem + ".pdf"), HERE / (Path(FINAL).stem + ".pdf"))
MD = HERE / MD_NAME
run(["python3", str(TOOLS / "to_obsidian.py"), str(SRC), str(MD)])
md = MD.read_text(encoding="utf8")
md = md.replace("tags: [maturaarbeit, kommentar]", "tags: [ueberarbeitung, kommentar]\nstand: 2026-11-10")
i0 = md.index("> [!info] Lesekopie"); i1 = md.index("\n\n", i0)
md = md[:i0] + (f"> [!info] Fassung vom 10.11.2026\n> Lesekopie der Word-Datei [[{FINAL}]]. "
  f"Quelle: `{SRC.name}` in diesem Ordner (Text dort ändern und mit `Werkzeuge/build.py` neu bauen, oder direkt in Word weiterarbeiten). "
  f"Gelb markierte Stellen ==[so]== können nur wir selbst ausfüllen. Was geändert wurde und was offen ist: [[{NOTIZ}]].") + md[i1:]
MD.write_text(md, encoding="utf8")
print("fertig:", ziel)
