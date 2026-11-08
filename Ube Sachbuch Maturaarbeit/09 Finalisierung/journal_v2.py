import re, itertools
from pathlib import Path

ROOT = Path("/home/claude/ube-sachbuch-maturaarbeit/Ube Sachbuch Maturaarbeit")
J = ROOT / "03 Arbeitsjournal"
OUT = ROOT / "09 Finalisierung" / "04_ARBEITSJOURNAL_ENTWURF.md"

files = sorted(J.glob("*/*.md"), key=lambda p: p.name)

# ---------------------------------------------------------------- gezielte Korrekturen (Fakten)
FIX = {
 "2026-09-16": [
  ("Der Stopp gilt schon seit Mitte August, die grossen Berichte sind aber erst am 13. und 14. September erschienen.",
   "Der Stopp gilt schon seit Mitte August, die Berichte darüber sind aber erst ab dem 11. September erschienen."),
  ("Die Meldungen von Context.ph, SunStar und vom Landwirtschaftsministerium kamen erst am 13. und 14. September.",
   "Die ersten Meldungen, etwa im BusinessMirror, kamen am 11. September, die von Context.ph, SunStar und vom Landwirtschaftsministerium am 13. und 14. September."),
  ("- Exportstopp gilt seit 15. August, Berichte erst ab 13. September",
   "- Exportstopp gilt seit Mitte August, Berichte erst ab 11. September"),
 ],
 "2026-10-21": [
  ("- 300 Mio. Pesos (rund 4,7 Mio. US-Dollar) und 34,1 Mio. US-Dollar aus den USA",
   "- 300 Mio. Pesos (rund 4,7 Mio. US-Dollar ==[prüfen: Mit dem Kurs vom Oktober 2026 sind es rund 5,1 Mio., so rechnet auch FreshPlaza am 6.10.]==) und 34,1 Mio. US-Dollar aus den USA"),
 ],
 "2026-11-06": [
  ("Ich habe Teil 2 und das zusammengeführte Kapitel 3 von Aezri übernommen und die Seiten mit Bildern gestaltet.",
   "Ich habe Teil 2 und das zusammengeführte Kapitel 3 von Aezri übernommen und die Seiten von Teil 2 mit Bildern gestaltet."),
  ("Für die Bilder habe ich unsere eigenen Fotos verwendet und, wo wir keine eigenen hatten, Bilder aus einer Bilddatenbank.",
   "Für die Bilder habe ich Tims Liste verwendet, die meisten stammen aus einer Bilddatenbank. ==[prüfen: Gibt es eigene Fotos im Buch? Falls nicht, so lassen.]=="),
  ("Bei Kapitel 3 habe ich die Thesen jeweils auf einer neuen Seite beginnen lassen und die Fazits farbig hervorgehoben.",
   "Bei Kapitel 3 habe ich die Thesen jeweils auf einer neuen Seite beginnen lassen. Bilder hat dieses Kapitel noch keine, und die Fazits will ich hervorheben, sobald der Text steht."),
  ("Bei Kapitel 3 war es schwieriger, weil dort viel Text steht und Bilder nicht immer passen. Die farbigen Fazits helfen, dass man beim Durchblättern sieht, wo eine These endet.",
   "Bei Kapitel 3 war es schwieriger, weil dort viel Text steht und Bilder nicht immer passen. Farbig hervorgehobene Fazits würden helfen, dass man beim Durchblättern sieht, wo eine These endet."),
  ("- Eigene Fotos und Bilddatenbank, jede Quelle notiert",
   "- Bilder aus Tims Liste, jede Quelle notiert"),
 ],
 "2026-05-27": [
  ("*(kein Eintrag)*", "*(kein Eintrag)* ==[prüfen: ergänzen oder so lassen; laut Johns Eintrag war Aezri dabei]=="),
 ],
}

# ---------------------------------------------------------------- Prüfhinweise je Eintrag (angenommene Angaben)
CHECK = {
 "2026-06-05": "Ab hier sind die Einträge aus unseren Angaben ausformuliert worden (siehe Hinweis oben). Prüfen: Hat jeder an diesem Tag wirklich an dem gearbeitet, was hier steht?",
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
 "2026-11-06": "Johns Eintrag ist an das Buch-PDF vom 8.11. angepasst (keine Bilder in Kapitel 3, Fazits noch nicht hervorgehoben). Prüfen: Wer hat die drei Kurzeinleitungen auf den Kapitelseiten geschrieben? Steht noch nirgends.",
}

# ---------------------------------------------------------------- Sprachliche Varianten je Person
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
stats = {}

def vary(text, person, filename):
    d = VAR.get(person)
    if not d:
        return text
    # längere Muster zuerst
    for pat in sorted(d, key=len, reverse=True):
        def rep(m):
            v = next(counters[person][pat])
            stats[pat] = stats.get(pat, 0) + (0 if v == pat else 1)
            if "{rest}" in v:
                # "Ich habe mich gefragt, ob X." -> "Ob X, weiss ich nicht."  (nur wenn Satz einfach endet)
                return m.group(0)  # komplexe Umstellung nicht automatisch
            return v
        text = re.sub(re.escape(pat), rep, text)
    return text

def process(path):
    key = path.name[:10]
    raw = path.read_text(encoding="utf8")
    body = raw
    # Frontmatter entfernen, Navigation entfernen
    body = re.sub(r"^---\n.*?\n---\n", "", body, flags=re.S)
    body = re.sub(r"^(\[\[20|← \(Beginn\)).*\n", "", body, flags=re.M)
    body = re.sub(r"^---\n(\[\[|← ).*\n?", "", body, flags=re.M)
    body = re.sub(r"\n---\n.*$", "\n", body, flags=re.S)
    # Bezugzeile entfernen
    body = re.sub(r"^Bezug: .*\n\n?", "", body, flags=re.M)
    original = "Eintrag aus dem bisherigen Arbeitsjournal" in body
    for old, new in FIX.get(key, []):
        if old not in body:
            print("NICHT GEFUNDEN", key, old[:50])
        body = body.replace(old, new)
    if not original:
        # Personen-Abschnitte variieren
        parts = re.split(r"(^## .*$)", body, flags=re.M)
        out = [parts[0]]
        person = None
        for i in range(1, len(parts), 2):
            head, sect = parts[i], parts[i + 1]
            name = head[3:].strip()
            person = {"Aezri": "Aezri", "Tim": "Tim", "John": "John"}.get(name)
            out.append(head)
            out.append(vary(sect, person, key) if person else sect)
        body = "".join(out)
    # Überschrift auf Ebene 2 absenken, Personen auf Ebene 3, Unterteile auf 4
    body = re.sub(r"^### ", "#### ", body, flags=re.M)
    body = re.sub(r"^## ", "### ", body, flags=re.M)
    body = re.sub(r"^# Arbeitsjournal – ", "## ", body, flags=re.M)
    if key in CHECK:
        body = re.sub(r"(^## .*\n)", r"\1\n> [!warning] Prüfen\n> " + CHECK[key] + "\n", body, count=1, flags=re.M)
    return body.strip() + "\n"

header = """---
tags: [finalisierung, arbeitsjournal, entwurf]
stand: 2026-11-09
---
# 04 Arbeitsjournal, überarbeitete Fassung (Entwurf)

> [!info] Was diese Datei ist
> Alle 45 Einträge vom 22.04. bis 06.11.2026 in einer Datei, mit gezielten Korrekturen und Prüfhinweisen. Die einzelnen Einträge in `03 Arbeitsjournal` und die Word-Datei [[Arbeitsjournal_Maturaarbeit_Ube.docx]] sind unverändert. Wenn ihr diese Fassung übernehmen wollt, kopiert ihr die geänderten Stellen in die Word-Datei. Was geändert wurde und warum, steht im Abschnitt «Regeln und Änderungen» direkt unten; am Schluss stehen Vorschläge für die fehlenden Einträge nach dem 6.11.

## Regeln und Änderungen

1. **Nichts erfunden.** Kein Treffen, kein Gespräch, kein Arbeitsschritt, kein Datum ist neu dazugekommen. Wo das Journal etwas annimmt, das nur ihr bestätigen könnt, steht am Anfang des Eintrags ein Kasten «Prüfen» (aus [[Offene Punkte bis zur Abgabe]]).
2. **Fakten angepasst**, wo das Journal dem Buch-PDF vom 8.11. oder den geprüften Quellen widerspricht: 16.09. (erste Berichte zum Exportstopp ab 11.09., nicht erst 13./14.09.), 21.10. (Umrechnung der 300 Mio. Pesos), 06.11. John (Kapitel 3 hat im PDF keine Bilder, die Fazits sind noch nicht hervorgehoben, eigene Fotos sind fraglich).
3. **Sprache leicht entzerrt.** Die ausformulierten Einträge ab 05.06. benutzten in fast jeder Reflexion dieselben Wendungen («Ich habe mich gefragt, ob …» 46-mal, «… ist mir aufgefallen, dass …» 30-mal). Etwa die Hälfte davon ist jetzt je Person anders formuliert, ohne dass sich der Inhalt ändert: Aezri eher «Ich war nicht sicher, ob», Tim eher «Unklar war für mich, ob» und «beispielsweise» (so schreibt er in seinen eigenen Einträgen vom April und Mai), John eher «Ich war unsicher, ob». Mehr haben wir bewusst nicht geändert: Echt wird das Journal nur, wenn ihr eure eigenen Einträge selbst nochmals lest und in eure Worte bringt. Die sieben Einträge vom 22.04. bis 03.06. sind unverändert eure Originale.
4. **Pronomen:** Aezri wird in den Einträgen von Tim und John mit «sie» und «ihr» bezeichnet. ==[prüfen, ob das stimmt]==
5. **Transparenz:** In der Übersicht des Journals (und im Kommentar, Kapitel 10.6) sollte stehen, dass die Einträge ab 05.06. aus euren Angaben mit Claude ausformuliert und von euch geprüft wurden. Vorschlag für den Satz in [[Arbeitsjournal – Übersicht]]: «Die Einträge vom 22.04. bis 03.06.2026 stammen unverändert aus unserem bisherigen Arbeitsjournal. Die Einträge ab 05.06.2026 haben wir aus unseren Notizen zu Datum, Ort, Tätigkeit und Ergebnis mit Hilfe von Claude ausformuliert und danach selbst geprüft und korrigiert (siehe KI-Nachweis im Kommentar).»
6. **Fehlende Einträge:** Nach dem 06.11. gibt es keinen Eintrag, obwohl in diesen Tagen der Kommentar entstanden ist, das Buch fertig gesetzt und gedruckt wird. Vorschläge mit Platzhaltern stehen am Ende dieser Datei. Füllt sie nur mit dem, was wirklich passiert ist.

"""

sections = []
phase = None
PHASES = {
 "1 Kochbuch": "## Kochbuch «Salu-Salo» (April bis Juli)",
 "2 Sommerferien": "## Sommerferien: Befragung auf den Philippinen",
 "3 Wechsel": "## Vom Kochbuch zum Sachbuch über Ube (August)",
 "4 Sachbuch": "## Sachbuch über Ube (August bis November)",
}
for f in files:
    folder = f.parent.name
    ph = next(v for k, v in PHASES.items() if folder.startswith(k))
    if ph != phase:
        sections.append("\n" + ph.replace("## ", "# ", 1) + "\n")
        phase = ph
    sections.append(process(f))

footer = """
# Vorschläge für die Einträge nach dem 6. November

> [!warning] Nur Vorschläge
> Diese Einträge sind nicht geschrieben, sondern vorbereitet. Alles in ==[Klammern]== müsst ihr aus eurer Erinnerung füllen oder streichen. Was nicht passiert ist, kommt nicht hinein.

## Sonntag, 08.11.2026

### Aezri

**Wo:** ==[Ort]==

#### Was

Heute habe ich mit Claude den ersten Entwurf des schriftlichen Kommentars erstellt. Ich habe Claude unsere Unterlagen gegeben (Buchtext, Projektplan, Arbeitsjournal, Beurteilung, Quellen, den Kommentar «Game Pressure» als Beispiel und die Zitierregeln) und den Auftrag, einen Entwurf mit Gliederung und Fussnoten zu schreiben. Danach habe ich den Entwurf ==[ganz / zum Teil]== gelesen und Claude gebeten, ihn sprachlich näher an unsere Texte zu bringen und die Grafiken zu erweitern. Ausserdem habe ich das Buch-PDF von John bekommen und im Vault abgelegt.

#### Vorgehen und Methode

Die Prompts stehen wörtlich im KI-Nachweis des Kommentars (Kapitel 10.6). Ich habe die Rückfragen von Claude beantwortet (Umfang, Titel, Theorieteil, wer welchen Abschnitt geschrieben hat) und die Angaben zum Ablauf mit unserem Journal verglichen. ==[Was habt ihr am Entwurf am 8.11. selbst geändert?]==

#### Reflexion

==[Eigene Einschätzung: Was hat der Entwurf gebracht, was hat gestört, was war an ihm nicht «wir»?]==

#### Wichtige Erkenntnisse

- Erster Entwurf des Kommentars liegt vor
- Alle Prompts dokumentieren, mit Datum und dem, was wir übernommen haben
- ==[…]==

### Tim

==[Eintrag nur, wenn Tim am 8.11. am Projekt gearbeitet hat, zum Beispiel Korrektur im Layout.]==

### John

**Wo:** ==[Ort]==

#### Was

Heute habe ich das Buch in InDesign weiter gesetzt und den Stand als PDF exportiert (52 Seiten): Vorwort, Inhaltsverzeichnis, Kapitel 1 mit Bildern und Karte, Kapitel 2 mit den Farbflächen, Kapitel 3 als Text in zwei Spalten. ==[prüfen]== Noch offen sind das Verzeichnis zur Karte, das Schlusswort, das Quellenverzeichnis, der Bildnachweis, der Anhang mit dem Interview, das Cover und die Bilder oder Kästen in Kapitel 3.

#### Vorgehen und Methode

==[Wie bist du vorgegangen? Was hast du zuerst gesetzt, wo gab es Probleme (Bildauflösung, Anführungszeichen, Spaltenumbruch)?]==

#### Reflexion

==[…]==

#### Wichtige Erkenntnisse

- Erstes PDF des Buches mit 52 Seiten
- Kapitel 3 ist noch ohne Bilder und ohne hervorgehobene Fazits
- ==[…]==

## Montag, 09.11.2026

### Aezri

**Wo:** ==[Ort]==

#### Was

Heute haben wir die Finalisierung gemacht. Ich habe Claude den Auftrag gegeben, den ganzen Vault zu prüfen, den Kommentar zu überarbeiten und Widersprüche zwischen Buch, Kommentar und Journal zu finden (Prompt im Anhang B des Kommentars). Danach haben wir zu dritt ==[den Kommentar gelesen und in eigene Worte gebracht / die gelben Stellen ausgefüllt / den Buchtitel und die Kapitelnamen entschieden / das Transkript eingefügt / …]==.

#### Vorgehen und Methode

==[Wer hat was geprüft? Welche Korrekturen sind ins Buch und in den Kommentar eingeflossen (Einleitung Kapitel 3 im Layout, Beleg These 1, 5,1 statt 4,7 Mio. US-Dollar, Erntezeit, Schreibweisen)?]==

#### Reflexion

==[…]==

#### Wichtige Erkenntnisse

- ==[…]==

### Tim

==[Korrekturlesen im Layout? Bildnachweis? Quellenverzeichnis ergänzt?]==

### John

==[Kapitel 3 fertig gesetzt? Cover? PDF für die Druckerei? Druck im Copyshop wann?]==

## Dienstag, 10.11.2026 (Abgabe)

==[Kurzer Abschlusseintrag: Druck, Bindung, Abgabe von Buch, Kommentar und Journal. Nur, was wirklich war.]==
"""

text = header + "\n".join(sections) + footer
text = re.sub(r"\n{3,}", "\n\n", text)
OUT.write_text(text, encoding="utf8")
print("geschrieben:", OUT, len(text.split()), "Wörter")
print("Ersetzungen:", stats)
