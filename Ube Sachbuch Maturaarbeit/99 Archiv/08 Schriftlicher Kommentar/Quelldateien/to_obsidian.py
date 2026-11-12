"""Macht aus der Kommentar-Quelle eine lesbare Obsidian-Notiz.

Aufruf: python3 to_obsidian.py <quelle> <ziel.md>
"""
import re
import sys
from pathlib import Path

src = Path(sys.argv[1]).read_text(encoding="utf8").replace("\r", "")
out_path = Path(sys.argv[2])

footnotes = []


def inline(s):
    res = []
    i = 0
    while i < len(s):
        if s.startswith("[^", i):
            d = 0
            j = i
            while j < len(s):
                if s[j] == "[":
                    d += 1
                elif s[j] == "]":
                    d -= 1
                    if d == 0:
                        break
                j += 1
            footnotes.append(ph(s[i + 2:j]))
            res.append(f"[^{len(footnotes)}]")
            i = j + 1
            continue
        res.append(s[i])
        i += 1
    return ph("".join(res))


def ph(s):
    return re.sub(r"\{\{(.*?)\}\}", lambda m: f"==[{m.group(1)}]==", s)


meta = {}
lines = src.split("\n")
body = []
i = 0
while i < len(lines):
    line = lines[i]
    if line.startswith("% "):
        k, v = line[2:].split(":", 1)
        meta[k.strip()] = v.strip()
        i += 1
        continue
    body.append(line)
    i += 1

# Überschriften für das Inhaltsverzeichnis
heads = []
for line in body:
    if line.startswith("# ") or line.startswith("## "):
        t = line.split(" ", 1)[1].strip()
        if t not in ("Abstract", "Inhaltsverzeichnis"):
            heads.append((line.startswith("## "), t))

out = []
out.append("---")
out.append("tags: [maturaarbeit, kommentar]")
out.append("---")
out.append(f"# Schriftlicher Kommentar «{meta.get('titel', 'Ube')}»")
out.append("")
out.append("> [!info] Lesekopie")
out.append("> Diese Notiz zeigt den ganzen Kommentar in Obsidian. Abgegeben und weiter bearbeitet wird die Word-Datei [[Schriftlicher_Kommentar_Ube.docx]]. Gelb markierte Stellen ==[so]== müssen wir noch ausfüllen. Übersicht und offene Punkte: [[Schriftlicher Kommentar]].")
out.append("")
out.append(f"**{meta.get('untertitel', '')}**")
out.append("")
out.append(" · ".join(ph(meta[k]) for k in ("autoren", "klassen", "schule") if k in meta))
out.append("")
out.append(" · ".join(ph(meta[k]) for k in ("betreuung", "abgabe") if k in meta))
out.append("")

i = 0
while i < len(body):
    line = body[i]
    s = line.strip()
    if s.startswith(":::table"):
        cap = s[len(":::table"):].strip()
        rows = []
        i += 1
        while i < len(body) and body[i].strip() != ":::":
            r = body[i].strip()
            if r.startswith("|"):
                rows.append([inline(c.strip()) for c in r.strip("|").split("|")])
            i += 1
        out.append(f"*{inline(cap)}*")
        out.append("")
        if rows:
            out.append("| " + " | ".join(rows[0]) + " |")
            out.append("| " + " | ".join("---" for _ in rows[0]) + " |")
            for r in rows[1:]:
                out.append("| " + " | ".join(r) + " |")
        out.append("")
        i += 1
        continue
    if s.startswith(":::refs"):
        i += 1
        while i < len(body) and body[i].strip() != ":::":
            r = body[i].strip()
            if r:
                out.append("- " + inline(r))
            i += 1
        out.append("")
        i += 1
        continue
    if s.startswith(":::figure"):
        p, cap = s[len(":::figure"):].split("|", 1)
        out.append(f"![[{Path(p.strip()).name}]]")
        out.append(f"*{inline(cap.strip())}*")
        i += 1
        continue
    if s.startswith(":::placeholder"):
        cap, box = s[len(":::placeholder"):].split("|", 1)
        out.append(f"> [!todo] {inline(box.strip())}")
        out.append("")
        out.append(f"*{inline(cap.strip())}*")
        i += 1
        continue
    if line.startswith("# Inhaltsverzeichnis"):
        out.append("## Inhaltsverzeichnis")
        out.append("")
        for sub, t in heads:
            out.append(("    - " if sub else "- ") + t)
        i += 1
        continue
    if line.startswith("## "):
        out.append("### " + line[3:])
        i += 1
        continue
    if line.startswith("# "):
        out.append("## " + line[2:])
        i += 1
        continue
    if line.startswith("~ ") or line == "~":
        # wörtlicher Prompt-Text aus den Anhängen: als Zitatblock, ohne Fussnoten-Auswertung
        out.append("> " + line[2:])
        out.append(">")
        i += 1
        continue
    if s.startswith("> "):
        out.append("> " + inline(s[2:]))
        i += 1
        continue
    out.append(inline(line))
    i += 1

text = "\n".join(out)
text = re.sub(r"\n{3,}", "\n\n", text).rstrip() + "\n"
if footnotes:
    text += "\n" + "\n".join(f"[^{n}]: {f}" for n, f in enumerate(footnotes, 1)) + "\n"
out_path.write_text(text, encoding="utf8")
print(f"{out_path}: {len(footnotes)} Fussnoten, {len(heads)} Überschriften")
