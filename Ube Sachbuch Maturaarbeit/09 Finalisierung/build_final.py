"""Baut die finale Word-Datei des Kommentars (für Claude).

Kopie von build_v3.py für die Schlusskorrektur (dritter Prompt, 9.11.2026).
Text ändern: kommentar_quelle_final.txt bearbeiten, dann `python3 build_final.py`.

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

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent / "08 Schriftlicher Kommentar" / "Quelldateien"
BUILD = Path(tempfile.gettempdir()) / "kommentar-build-final"
SRC = HERE / "kommentar_quelle_final.txt"


def find_soffice():
    for base in (Path.home() / ".claude" / "skills", Path("/mnt/skills")):
        if base.exists():
            hits = sorted(base.glob("**/docx/scripts/office/soffice.py"))
            if hits:
                return ["python3", str(hits[0])]
    return ["soffice"]


SOFFICE = find_soffice()
FINAL = sys.argv[1] if len(sys.argv) > 1 else "Schriftlicher_Kommentar_Ube_FINAL.docx"


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
run(["python3", str(TOOLS / "to_obsidian.py"), str(SRC), str(HERE / "03_KOMMENTAR_ENTWURF.md")])
md = (HERE / "03_KOMMENTAR_ENTWURF.md").read_text(encoding="utf8")
md = md.replace("tags: [maturaarbeit, kommentar]", "tags: [finalisierung, kommentar, entwurf]\nstand: 2026-11-09")
md = md.replace("> [!info] Lesekopie\n> Diese Notiz zeigt den ganzen Kommentar in Obsidian. Abgegeben und weiter bearbeitet wird die Word-Datei [[Schriftlicher_Kommentar_Ube.docx]]. Gelb markierte Stellen ==[so]== müssen wir noch ausfüllen. Übersicht und offene Punkte: [[Schriftlicher Kommentar]].",
  "> [!info] Finale Arbeitsfassung (Schlusskorrektur, 9.11.2026)\n> Lesekopie der Word-Datei [[Schriftlicher_Kommentar_Ube_FINAL.docx]]. Quelle: `kommentar_quelle_final.txt` im Ordner 09 Finalisierung (Text dort ändern, dann `python3 build_final.py`, oder direkt in Word weiterarbeiten). Gelb markierte Stellen ==[so]== könnt nur ihr ausfüllen oder entscheiden: Liste nach Priorität in [[OFFENE_PUNKTE_FINAL]]. Was sich geändert hat und wie wir den Stand bewerten: [[AENDERUNGSPROTOKOLL_FINAL]]. Ältere Fassungen (v2, v3) liegen in `Versionen/`.")
(HERE / "03_KOMMENTAR_ENTWURF.md").write_text(md, encoding="utf8")
print("fertig:", ziel)
