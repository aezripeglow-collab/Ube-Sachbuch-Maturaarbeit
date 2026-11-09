---
tags: [maturaarbeit, kommentar]
---
# Schriftlicher Kommentar

Der Kommentar begleitet unser Sachbuch «Ube» und wird am **10.11.2026** zusammen mit dem Buch abgegeben.

- **Word-Datei zum Bearbeiten und Abgeben:** [[Schriftlicher_Kommentar_Ube.docx]]
- **Ganzer Text in Obsidian (Lesekopie):** [[Kommentar Volltext]]
- **Was noch fehlt:** Abschnitt «Schriftlicher Kommentar» in [[Offene Punkte bis zur Abgabe]]

## Stand
- **9. November 2026, 10:00:** **Finale Arbeitsfassung** nach der Schlusskorrektur mit dem Transkript des Interviews: `09 Finalisierung/Schriftlicher_Kommentar_Ube_FINAL.docx` und [[03_KOMMENTAR_ENTWURF]]. Anhang A enthält jetzt die zehn Fragen und das Transkript. Korrigiert nach dem Transkript: keine Kostenfrage, «Bauern und Verkäufer», offene Fragen 7 und 10, Markt in Talisay City. Leitthese in 7.4 festgelegt. Was wir noch tun müssen: [[OFFENE_PUNKTE_FINAL]] (vor allem der eigene Anteil im KI-Nachweis). Bewertung: [[AENDERUNGSPROTOKOLL_FINAL]].
- **9. November 2026, 03:30:** Arbeitsfassung **v3** nach der wissenschaftlichen Überarbeitung in [[03_KOMMENTAR_ENTWURF]] und `09 Finalisierung/Schriftlicher_Kommentar_Ube_v3.docx` (v2 gesichert in `09 Finalisierung/Versionen/`). Behoben: Weltmarktvergleich (0,7 %) nur noch als Grössenordnung, Zeiträume von Nachfrage und Ernte getrennt, Kausalaussagen den Quellen zugeordnet, kulturelle Kontrolle dreigeteilt, Interview als Einzelsicht; KI-Nachweis neu strukturiert; 6.2 mit Abb. 6. Noch nicht abgabefertig: Pflichtpunkte in [[07_AENDERUNGSPROTOKOLL_UND_BEWERTUNG]] Abschnitt 6.
- **9. November 2026, 00:15:** Entwurf v2 aus der Finalisierung. Neu: Kapitel 7 (Einordnung nach wirtschaftlicher und kultureller Kontrolle, Einwände gegen die Leitthese), 5.2 Quellenarten, 5.5 Interviewauswertung, Produktangaben aus dem Buch-PDF, vollständiger KI-Nachweis. Die Dateien in diesem Ordner sind der Stand vom 8.11. und unverändert. Was ihr noch entscheiden müsst: [[06_OFFENE_AUFGABEN]].
- Entwurf vom 8. November 2026, mit Claude geschrieben und am gleichen Tag Satz für Satz überarbeitet, damit er nach euch klingt (Vorbild: Teil 1 und These 1 und 2 im Buch). Ihr müsst ihn noch gemeinsam lesen und in eigenen Worten überarbeiten (Zitierregeln, Punkt 1.7).
- 25 Seiten Haupttext von der Einleitung bis zum Schlusswort, dazu Titelblatt, Abstract, Inhaltsverzeichnis, Quellenverzeichnis mit KI-Nachweis, Abbildungs- und Tabellenverzeichnis und Anhang. Schrift Cambria 11 Punkt.
- 52 Fussnoten nach den Zitierregeln der Kantonsschule Baden (deutsche Variante). Im Buch selbst stehen Kurzbelege in Klammern.
- Kapitel 2 erzählt den Ablauf jetzt Datum für Datum, vom 22. April bis zur Abgabe. Die Daten stammen aus dem [[Arbeitsjournal – Übersicht|Arbeitsjournal]]. Bitte prüfen, ob alles so stimmt.
- Vier eigene Abbildungen: Zeitstrahl mit allen wichtigen Daten, Arbeitsplan (wer wann woran), Aufbau von Kapitel 3 mit allen Behauptungen, Fläche und Ernte 2010 und 2025 mit eigener Rechnung. Dazu drei Tabellen und zwei Platzhalter für Cover und Doppelseite.
- Gelb markierte Stellen in der Word-Datei sind Platzhalter für Angaben, die nur ihr kennt, etwa aus dem InDesign-Dokument.
- Ändern sich Seiten, in Word das Inhaltsverzeichnis aktualisieren: Rechtsklick darauf, dann «Feld aktualisieren».

## Aufbau
1. Einleitung
2. Entstehung des Projekts (Kochbuch «Salu-Salo», Zwischenpräsentation, Befragung, Wechsel zu Ube, Ablauf bis zur Abgabe)
3. Formale Recherche: Wie ein Sachbuch funktioniert (kurzer Theorieteil mit Quellen)
4. Konzeptentwicklung
5. Inhaltliche Recherche und Methode
6. Inhalt des Endprodukts
7. Zentrale Erkenntnisse
8. Reflexion
9. Schlusswort und Dank
10. Quellenverzeichnis mit KI-Nachweis
11. Abbildungsverzeichnis
12. Tabellenverzeichnis
- Anhang: Interview mit «Tita»

## Grundlagen
- Buchtext: [[Vorwort]], [[Teil 1 – Ube auf den Philippinen]], [[Teil 2 – Der Ube-Trend]], [[3.0 Einleitung und Leitthese]] bis [[3.5 Was bleibt von unserer Leitthese]], [[Schlusswort]]
- [[Projektplan]], [[Aufteilung der Gruppe]], [[Arbeitsjournal – Übersicht]]
- [[Interview mit Tita]], [[Quellenverzeichnis Kapitel 3]]
- Beurteilung der Zwischenpräsentation vom 19.06.2026 und Zitierregeln der Kantonsschule Baden (5. Auflage, 2025)

## Für Claude
In `Quelldateien` liegt der Text in `kommentar_quelle.txt`. `python3 build_all.py` baut daraus die Word-Datei neu (mit Seitenzahlen im Inhaltsverzeichnis) und erzeugt [[Kommentar Volltext]] neu. Die Abbildungen entstehen mit `make_figures.py`. Wurde die Word-Datei inzwischen von Hand geändert, zuerst diese Änderungen in die Quelle übernehmen.
