---
tags: [ueberarbeitung, status]
stand: 2026-11-10
---
# Status der Überarbeitung

> [!warning] Kommentar abgelöst (10.11.2026, 04:15 Uhr)
> Als gültiger Kommentar gilt jetzt die Fassung der Gruppe: [[Schriftlicher_Kommentar_Ube_Sachbuch_Peglow_Rosal_Meuwly.docx]] in `08 Schriftlicher Kommentar`, siehe [[Fassung der Gruppe vom 10.11.2026]]. Die Kommentar-Dateien in diesem Ordner bleiben als ältere Fassungen liegen. Für das Arbeitsjournal gilt weiterhin [[Arbeitsjournal_Ube_SCHLUSSREDAKTION.docx]].

> [!important] Stand 10.11.2026, nach der Schlussredaktion (Prompt von 01:42 Uhr)
> Es gilt jetzt die **Arbeitsfassung «SCHLUSSREDAKTION»**: [[Schriftlicher_Kommentar_Ube_SCHLUSSREDAKTION.docx]] mit PDF, Lesekopie [[Kommentar (Schlussredaktion)]], und [[Arbeitsjournal_Ube_SCHLUSSREDAKTION.docx]], Lesekopie [[Arbeitsjournal (Schlussredaktion)]].
> Was geändert wurde: [[AENDERUNGSPROTOKOLL_SCHLUSSREDAKTION]]. Was offen ist und was vor der Abgabe geklärt werden muss: [[OFFENE_PUNKTE_SCHLUSSREDAKTION]].
> Die Fassung «UEBERARBEITET» bleibt als Ausgangsfassung unverändert liegen. Nicht abgabefertig, solange die Punkte mit Priorität 1 offen sind.

## Schlussredaktion: erledigt
- [x] Ausgangsfassung vollständig gelesen, Zugriff auf Dateien und Quellen geprüft
- [x] Absolute Aussagen berichtigt (Abstract, 7.4), Interview mit dem Transkript abgeglichen (4.5, 7.2)
- [x] Angaben aus zweiter Hand mit «zit. nach» gekennzeichnet, USDA FAS nach Context.ph vom 29.06.2026 zitiert
- [x] Kapitel 8 umgebaut: Herkunft der Aussagen, 8.2 bündelt Zeit und Ablenkung, 8.3 nur Zusammenarbeit, 8.9 gekürzt
- [x] KI-Nachweis in drei Teile getrennt, Eingabe 12 und Anhang G, offene Frage der Zulässigkeit ausdrücklich genannt
- [x] Aussagen über das gedruckte Buch auf den Satzstand vom 8.11. begrenzt, Titelblatt als Arbeitsfassung gekennzeichnet
- [x] Arbeitsjournal an neun Stellen berichtigt, neue Datei
- [x] Word-Datei gebaut und geprüft (90 Fussnoten, 107 Seiten im PDF), PDF durchgesehen

## Wenn noch etwas geändert werden soll (Schlussredaktion)
- Kommentar: `kommentar_quelle_schlussredaktion.txt` bearbeiten, dann den Aufruf oben in `Werkzeuge/build.py` verwenden. Oder direkt in Word ändern und am Schluss das Inhaltsverzeichnis aktualisieren.
- Journal: [[Arbeitsjournal (Schlussredaktion)]] bearbeiten, dann `python3 Werkzeuge/journal_docx.py "Arbeitsjournal (Schlussredaktion).md" Arbeitsjournal_Ube_SCHLUSSREDAKTION.docx`.

# Stand vor der Schlussredaktion (Masterprompt vom 9.11.2026, 23:51)

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
