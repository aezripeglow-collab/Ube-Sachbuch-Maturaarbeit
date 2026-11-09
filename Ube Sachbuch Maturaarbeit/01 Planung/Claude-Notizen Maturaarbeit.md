---
tags: [maturaarbeit, ube, claude]
---

# Claude-Notizen zur Maturaarbeit

Was Claude über eure Maturaarbeit weiss (Stand: 9. November 2026). Du kannst diese Notiz jederzeit selbst ergänzen oder korrigieren.

## Eckdaten
- **Thema:** Sachbuch über Ube (lila Yamswurzel)
- **Schule:** Kantonsschule Baden
- **Team:** Aezri, Tim, John
- **Abgabe:** Dienstag, 10. November 2026

## Aufbau der Arbeit
- Die Arbeit besteht aus zwei Teilen:
  - **Produkt:** gedrucktes Buch (der Text geht in den Druck)
  - **Schriftlicher Kommentar:** erster Entwurf am 8. November 2026 mit Claude geschrieben, siehe [[Schriftlicher Kommentar]]
- **Teil 1:** führt nicht-wissenschaftlich ins Thema ein
- **Teil 3 / Kapitel 3:** enthält die wissenschaftlichen Belege (Thesen)

## Aufteilung im Team
| Person | Teil |
|---|---|
| Aezri | Teil 1, These 1 und 2 in Kapitel 3, Interview |
| Tim | Teil 2, These 4 |
| John | These 3, Satz und Layout in InDesign |

- Tims These folgt im zusammengeführten Text auf Aezris Teil.
- Johns Teil behandelt die Leitfragen: Was denken Menschen auf den Philippinen über den Ube-Trend? Bleibt die Tradition erhalten?

## Schriftlicher Kommentar
- Titel des Buches: «Ube» (das Buch-PDF heisst «Ube – Zwischen Tradition und Trend», prüfen)
- Betreuerin: Andrea Büschlen, Zweitbewerter: Joel Franceschi
- Umfang: etwa 20 bis 25 Seiten ohne Titelblatt, Verzeichnisse und Anhang, mit kurzem Theorieteil und Quellen
- Fussnoten nach den Zitierregeln der Kantonsschule Baden (deutsche Variante), Wir-Form, keine Note erwähnen
- Vorbilder: Kommentare «Game Pressure» und Kaffeemuseum
- Produktangaben aus InDesign (Format, Schriften, Seitenzahl, Cover) fehlen noch und sind im Kommentar gelb markiert
- Offene Punkte stehen in [[Offene Punkte bis zur Abgabe]]

## Produkt (Buch)
- Buch-PDF vom 8.11.2026, etwa die Hälfte fertig, so wie es an die Druckerei gehen soll: [[Buch Ube – Zwischen Tradition und Trend (Stand 08.11.2026).pdf]]
- John setzt das Buch in Adobe InDesign: A4, Schrift Minion Pro, bisher 52 Seiten
- Kapitel im Buch: 1 «Die Geschichte von Ube» (S. 3), 2 «Der Ube-Trend» (S. 14), 3 «Einfluss von Ube auf den Philippinen» (S. 23), Schlusswort (S. 52)
- Die Karte von Bohol (S. 9) hat John gemacht. Tim hat Bilder gesucht und Korrektur gelesen.
- Was am Buch noch fehlt: [[Offene Punkte bis zur Abgabe]], Abschnitt «Buch fertigstellen»
- Arbeitsjournal: Die Arbeit am Buch steht in den Mittwochseinträgen vom 28.10. und 04.11. Wenn Aezri das fertige Buch schickt, den Rest ergänzen.

## Finalisierung (9. November 2026)
- Aezri hat Claude am 8.11. einen Master-Prompt gegeben (Wortlaut in Anhang B des Kommentars v2). Ergebnis: Ordner `09 Finalisierung` mit [[00_PROJEKTSTATUS]] (zuerst lesen), [[01_MATERIALANALYSE]] (mit Stilprofil in Abschnitt 8), [[02_ARGUMENTATIONSSTRUKTUR]], [[03_KOMMENTAR_ENTWURF]] (Kommentar v2, auch als Word `Schriftlicher_Kommentar_Ube_v2.docx`), [[04_ARBEITSJOURNAL_ENTWURF]], [[05_KONSISTENZPRUEFUNG]], [[06_OFFENE_AUFGABEN]].
- Geprüfte Korrekturen: 300 Mio. Pesos sind rund 5,1 Mio. USD (nicht 4,7); erste Berichte zum Exportstopp ab 11.9.2026; USDA-Bericht heisst «Ube – Purple Yam – A High-Value Specialty Crop …», RP2026-0019, 26.6.2026.
- Im Vault fehlen weiterhin: Transkript und Fragen des Interviews, Zitierregeln, Beurteilung vom 19.6., Wegleitung.
- Werkzeuge: `build_v2.py` baut Word und Lesekopie aus `kommentar_quelle_v2.txt`; `make_figures_v2.py` zeichnet Abb. 2; `journal_v2.py` erzeugt den Journal-Entwurf.
- Zweiter Master-Prompt (9.11., 00:53): wissenschaftliche Überarbeitung von v2 → **v3** (`kommentar_quelle_v3.txt`, `build_v3.py`, `Schriftlicher_Kommentar_Ube_v3.docx`). Fünf Kritikpunkte von Aezri geprüft und behoben; Protokoll in [[07_AENDERUNGSPROTOKOLL_UND_BEWERTUNG]], Stand in [[FORTSCHRITT_KOMMENTAR]]. Neu geprüfte Quellen: Asian Journal 20.03.2026 (Aromahersteller ohne Quelle), Mendoza 08.05.2026 (Drittel/Zwei-Drittel nur Szenario), FreshPlaza 11.06.2026 (80 Pesos ab Hof), TMR-Marktdefinition (75 % Asien-Pazifik). Offen bleibt vor allem, was die Gruppe selbst am Kommentar geprüft und geändert hat (für den KI-Nachweis), das Transkript, der Entscheid zu 7.4 und zu Anhang B.
- Modell laut Anzeige: Opus 5.5 am 8.11., Fable 5.1 ab dem späten Abend des 8.11. (im Kommentar 10.6 mit Prüfvermerk).
- Dritter Prompt (9.11., 08:39, Schlusskorrektur) mit dem **Transkript des Interviews** (zehn Fragen, acht Antworten; unbeantwortet: Wirtschaft von Bohol, Zukunft in zehn Jahren). Wichtige Fakten daraus: Tita ist Bäuerin und Verkäuferin auf dem Talisay Public Market (Talisay City, Cebu); Preis 100 → 150 Pesos/kg; «farmers and vendors also benefited»; Knappheit erklärt sie mit der Nachfrage; eine ihrer violetten Sorten stammt aus Bohol; keine Frage zu Kosten oder Sorten gestellt; erste Antwort in der dritten Person. Ergebnis: `Schriftlicher_Kommentar_Ube_FINAL.docx`, [[OFFENE_PUNKTE_FINAL]], [[AENDERUNGSPROTOKOLL_FINAL]], [[FORTSCHRITT_FINALKORREKTUR]]. Das Transkript steht auch in [[Interview mit Tita]] noch nicht; dort einfügen (nicht von Claude geändert, weil Originalnotiz).

## Quellen und Material
- 2-minütiges Interview mit einer Bäuerin von den Philippinen
- Keine Umfrage (keine Zeit mehr dafür)

## Arbeitsweise
- Geschrieben in Obsidian auf dem iPad
- Synchronisiert mit Obsidian Git über das GitHub-Repository `aezripeglow-collab/Ube-Sachbuch-Maturaarbeit`
