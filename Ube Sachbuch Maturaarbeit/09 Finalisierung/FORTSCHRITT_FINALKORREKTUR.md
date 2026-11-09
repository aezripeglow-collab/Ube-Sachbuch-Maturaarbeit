---
tags: [finalisierung, status, kommentar, arbeitsjournal]
stand: 2026-11-09 12:30
---
# FORTSCHRITT_FINALKORREKTUR

Fortschrittsdatei für die Schlusskorrektur. Vierte Runde: Prompt vom 9.11.2026, 10:36 («Ultimativer Master-Prompt», mit der Familienchronik als Stilvorlage). Dritte Runde: Prompt vom 9.11., 08:39 (mit dem Transkript). Für eine Fortsetzung: zuerst diese Datei lesen, dann [[OFFENE_PUNKTE_FINAL]], dann `kommentar_quelle_final.txt` (Arbeitsgrundlage des Kommentars) und `journal_final.py` (Arbeitsgrundlage des Journals). Zusammenhang aller Dateien: [[FORTSCHRITT_KOMMENTAR]].

## Vierte Runde: zwölf Durchgänge

- [x] Durchgang 1 Bestandsaufnahme: Kommentar FINAL (Stand 10:00), Arbeitsjournal (45 Einträge), OFFENE_PUNKTE_FINAL zuerst; dann alle Notizen im Vault, die vier Prompts, die Familienchronik, das Buch-PDF.
- [x] Durchgang 2 Persönlicher Stil: Stilprofil aus nicht KI-bearbeiteten Texten → [[Schreibstimme Aezri]] (in `Persönliches/`, in [[CLAUDE]] und [[00 Start]] eingetragen).
- [x] Durchgang 3 Inhaltliche Kontrolle: Rechnungen, Tita-Zitate, Daten; Befund «Name selbst gewählt» behoben.
- [x] Durchgang 4 Quellenprüfung: nur formal; keine erneute Webprüfung (Stand: [[AENDERUNGSPROTOKOLL_FINAL]] B5).
- [x] Durchgang 5 Sprachliche Korrektur: mechanische Prüfung, ein Befund (Fussnote 1.3).
- [x] Durchgang 6 Vergleich mit dem Buch: PDF vom 8.11. (Format, Schrift, Belegformen, Tita-Stellen, Trennungen) → [[BUCH_KORREKTURLISTE_FINAL]].
- [x] Durchgang 7 Arbeitsjournal: alle 45 Einträge geprüft; `journal_final.py` → `ARBEITSJOURNAL_FINAL.md`, `Arbeitsjournal_Ube_FINAL.docx` (40 Seiten, 27 gelbe Stellen); Protokoll in [[AENDERUNGSPROTOKOLL_FINAL]] A3.
- [x] Durchgang 8 KI-Dokumentation: Eingabe 9 in 10.6, [[KI_DOKUMENTATION_FINAL]] mit allen vier Prompts im Wortlaut.
- [x] Durchgang 9 Formale Kontrolle: Kommentar neu gebaut (63 Seiten, 71 Fussnoten, 55 gelbe Stellen).
- [x] Durchgang 10 Unabhängige Schlusskontrolle: gebaute Fassung vollständig als Text gelesen (Befunde in [[AENDERUNGSPROTOKOLL_FINAL]] A2).
- [x] Durchgang 11 Schreibstimmenkontrolle: alle Kapitel gegen das Stilprofil, 33 Stellen (Wort-für-Wort-Vergleich dokumentiert).
- [x] Durchgang 12 Technische Endprüfung: beide Word-Dateien als PDF gerendert und angesehen, mit python-docx geöffnet; Sicherung in `Versionen/`.
- [x] Lieferungen: A `Schriftlicher_Kommentar_Ube_FINAL.docx`, B `Arbeitsjournal_Ube_FINAL.docx` (+ `ARBEITSJOURNAL_FINAL.md`), C [[OFFENE_PUNKTE_FINAL]], D [[AENDERUNGSPROTOKOLL_FINAL]], E diese Datei, F [[BUCH_KORREKTURLISTE_FINAL]], G [[KI_DOKUMENTATION_FINAL]], H [[QUALITAETSBEWERTUNG_FINAL]].

## Dritte Runde: sieben Durchgänge (abgeschlossen 10:00)

- [x] 1 Bestandsaufnahme (Kommentar v3, Transkript gegen Buch/Kommentar/Journal, Buch-PDF)
- [x] 2 Inhaltliche und wissenschaftliche Korrektur (14 Korrekturen, Leitthese entschieden)
- [x] 3 Sprachliche Korrektur
- [x] 4 Formale Vervollständigung (17 Platzhalter aufgelöst, Anhang A gebaut)
- [x] 5 Abgleich mit den Projektmaterialien
- [x] 6 Abschliessende Kontrolle
- [x] 7 Persönliche Stilkontrolle (noch mit dem alten, strengeren Stilprofil)

## Welche Dateien geprüft wurden

Vollständig gelesen: `kommentar_quelle_final.txt` (alle Kapitel, Fussnoten, Tabellen, Verzeichnisse, Anhänge; in der dritten Runde ganz, in der vierten Runde alle Kapitel nochmals für den Stil und die gebaute Fassung am Schluss), `ARBEITSJOURNAL_FINAL.md` (alle 48 Einträge inklusive Vorlagen), die vier Prompts, die Familienchronik, `OFFENE_PUNKTE_FINAL.md`, `06_OFFENE_AUFGABEN.md`, `04_ARBEITSJOURNAL_ENTWURF.md` (Nachtrag), `Interview mit Tita.md`, `Schreibstimme Aezri.md`. Buch-PDF: Text vollständig extrahiert und an den geprüften Stellen gelesen, Seiten 4, 8, 9, 13, 50 bis 52 angesehen (dritte Runde), Schrift und Format gemessen.

Nicht geprüft oder nicht verfügbar: Chatverläufe der Eingaben 1 bis 5, Zitierregeln der KSB, Beurteilung vom 19.06., InDesign-Dateien, gedrucktes Buch, Sprachnachrichten, CPBRD-Brief und USDA-PDF (gesperrt), SCMP-Volltext. Webquellen in der vierten Runde nicht erneut geprüft.

## Stand der Arbeit

Alle zwölf Durchgänge sind abgeschlossen (9.11., 12:30). Nichts ist abgabefertig, solange Priorität 1 in [[OFFENE_PUNKTE_FINAL]] offen ist (euer Anteil im KI-Nachweis, Journaleinträge 8. bis 10.11., KI-Satz in der Journal-Übersicht, Eingabe 4, Herkunft der Bewertung und Werkzeug der Prompts, weitere KI-Nutzung, Anhang B, Interviewangaben, Buchtitel und Klassen, Rechnung 850'000, Leitthese).

Für eine Fortsetzung: Kommentar in `kommentar_quelle_final.txt` ändern und `python3 build_final.py` ausführen (schreibt auch die Lesekopie [[03_KOMMENTAR_ENTWURF]]); Journal in `journal_final.py` (FIX/CHECK/TEMPLATES) ändern und `python3 journal_final.py` ausführen. Oder direkt in den Word-Dateien weiterarbeiten; dann ist Word die Wahrheit, und die Quelltexte sind veraltet. Nach jeder weiteren Sitzung mit Claude eine Eingabe in 10.6 ergänzen.
