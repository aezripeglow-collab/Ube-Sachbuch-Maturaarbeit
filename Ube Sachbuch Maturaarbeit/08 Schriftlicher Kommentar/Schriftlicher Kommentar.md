---
tags: [maturaarbeit, kommentar]
---
# Schriftlicher Kommentar

Der Kommentar begleitet unser Sachbuch «Ube» und wird am **10.11.2026** zusammen mit dem Buch abgegeben.

- **Word-Datei zum Bearbeiten und Abgeben:** [[Schriftlicher_Kommentar_Ube.docx]]
- **Ganzer Text in Obsidian (Lesekopie):** [[Kommentar Volltext]]
- **Was noch fehlt:** Abschnitt «Schriftlicher Kommentar» in [[Offene Punkte bis zur Abgabe]]

## Stand
- Erster vollständiger Entwurf vom 8. November 2026, mit Claude geschrieben. Ihr müsst ihn noch gemeinsam lesen und in eigenen Worten überarbeiten (Zitierregeln, Punkt 1.7).
- 21 Seiten Haupttext von der Einleitung bis zum Schlusswort, dazu Titelblatt, Abstract, Inhaltsverzeichnis, Quellenverzeichnis mit KI-Nachweis, Abbildungs- und Tabellenverzeichnis und Anhang.
- Fussnoten nach den Zitierregeln der Kantonsschule Baden (deutsche Variante). Im Buch selbst stehen Kurzbelege in Klammern.
- Drei eigene Abbildungen (Zeitstrahl, Aufbau von Kapitel 3, Fläche und Ernte 2010 und 2025) und drei Tabellen.
- Gelb markierte Stellen in der Word-Datei sind Platzhalter für Angaben, die nur ihr kennt, etwa aus dem InDesign-Dokument.
- Ändern sich Seiten, in Word das Inhaltsverzeichnis aktualisieren: Rechtsklick darauf, dann «Feld aktualisieren».

## Aufbau
1. Einleitung
2. Entstehung des Projekts (Kochbuch «Salu-Salo», Zwischenpräsentation, Befragung, Wechsel zu Ube)
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
