---
tags: [ueberarbeitung, status]
stand: 2026-11-10
---
# Status der Überarbeitung (Masterprompt vom 9.11.2026, 23:51)

Arbeitsordner für die abschliessende Überarbeitung von Kommentar und Arbeitsjournal. Die Dateien in `09 Finalisierung` bleiben als Stand vom 9.11. abends liegen und sind überholt. Was hier liegt, gilt.

## Erledigt
- [x] Material geprüft (Vault, Zitierregeln 2025, Buch-PDF vom 8.11., Transkript, Johns Liste der Bildquellen)
- [x] Kommentar überarbeitet: `kommentar_quelle.txt` → [[Schriftlicher_Kommentar_Ube_UEBERARBEITET.docx]], Lesekopie [[Kommentar (überarbeitet)]]
- [x] Abbildungen 1 und 2 mit der berichtigten Interview-Chronologie neu gezeichnet, Abbildung 5 neu (Buchseiten 4 und 9)
- [x] Arbeitsjournal als fünfzehn Rückblicke über je zwei Wochen: [[Arbeitsjournal (überarbeitet)]] → [[Arbeitsjournal_Ube_UEBERARBEITET.docx]]
- [x] [[PRUEFBERICHT]] mit Änderungen, geprüften und ungeprüften Quellen, offenen Angaben, fehlenden Teilen des KI-Nachweises und Errataliste zum gedruckten Buch
- [x] Schlusskontrolle (Verweise, Verzeichnisse, gerenderte Seiten)
- [x] Notizen im Vault nachgeführt ([[Interview mit Tita]], [[Bildquellen (Liste von John)]], [[Aufteilung der Gruppe]], [[Claude-Notizen Maturaarbeit]])

## Offen (nur wir selbst)
Siehe [[PRUEFBERICHT]], Abschnitt 2: eigener Anteil am Text, Prüfung am gedruckten Buch, Seitenzahlen bei CPBRD und USDA FAS, fehlende Angaben im KI-Nachweis, «Salo-Salo» und Pronomen für Aezri bestätigen, Reflexion gegenlesen, Anhänge und Errataliste mit Frau Büschlen klären.

## Wenn noch etwas geändert werden soll
- Kommentar: `kommentar_quelle.txt` bearbeiten, dann `python3 Werkzeuge/build.py`. Oder direkt in Word ändern und am Schluss das Inhaltsverzeichnis aktualisieren.
- Journal: [[Arbeitsjournal (überarbeitet)]] bearbeiten, dann `python3 Werkzeuge/journal_docx.py`. Oder direkt in Word ändern.
- Abbildungen 1 und 2: Daten in `Werkzeuge/abbildungen.py` ändern und das Skript laufen lassen.

## Was Claude nicht vorlag
- Druck-PDF des Buches vom 9.11. (im Vault liegt nur der Satzstand vom 8.11., 52 Seiten)
- Zwischenbeurteilung vom 19.6. im Original, Wegleitung und Bewertungsraster
- Berichte von CPBRD und USDA FAS als PDF (Seitenzahlen in den Fussnoten fehlen deshalb)
- Aufnahme des Interviews, Druckbestellung, Chatverlauf zur Karte von Bohol
