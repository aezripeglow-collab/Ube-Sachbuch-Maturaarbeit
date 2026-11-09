---
tags: [finalisierung, status, kommentar]
stand: 2026-11-09 10:00
---
# FORTSCHRITT_FINALKORREKTUR

Fortschrittsdatei für die Schlusskorrektur (dritter Prompt vom 9.11.2026, 08:39, mit dem Transkript des Interviews). Für eine Fortsetzung: zuerst diese Datei lesen, dann `kommentar_quelle_final.txt` (Arbeitsgrundlage). Vorgängerfassungen: v3 gesichert in `Versionen/` (Stand 03:30), v2 ebenfalls dort. Zusammenhang der Dateien: [[FORTSCHRITT_KOMMENTAR]].

## Durchgänge

- [x] Durchgang 1 Bestandsaufnahme: ganzer Kommentar v3 gelesen (alle Kapitel, Fussnoten, Tabellen, Verzeichnisse, Anhänge); Transkript mit Buch, Kommentar und Journal verglichen; Buch-PDF nachgeprüft (Seitenzahlen, Bilder, Zwischentitel); Journal zu 17.06., 14.09., Sommerferien, 06.11. nachgelesen. Problemliste unten.
- [x] Durchgang 2 Inhaltliche und wissenschaftliche Korrektur (Protokoll in [[AENDERUNGSPROTOKOLL_FINAL]] Abschnitt 2, Leitthese Abschnitt 4)
- [x] Durchgang 3 Sprachliche Korrektur (mechanische Prüfung und Leseprüfung, kein deutsches Rechtschreibprogramm verfügbar)
- [x] Durchgang 4 Formale Vervollständigung (17 Platzhalter aufgelöst, Anhang A gebaut, Abrufdaten, Verweise geprüft)
- [x] Durchgang 5 Abgleich mit den Projektmaterialien (PDF, Transkript, Journal, Rechnungen)
- [x] Durchgang 6 Abschliessende Kontrolle (gebaute Fassung vollständig gelesen, fünf Stellen korrigiert, neu gebaut)
- [x] Durchgang 7 Persönliche Stilkontrolle (neue Sätze gegen das Stilprofil, drei Stellen vereinfacht)
- [x] Abgabe: `Schriftlicher_Kommentar_Ube_FINAL.docx` (63 Seiten, Haupttext S. 4 bis 34), [[OFFENE_PUNKTE_FINAL]], [[AENDERUNGSPROTOKOLL_FINAL]], Lesekopie [[03_KOMMENTAR_ENTWURF]]

## Problemliste aus Durchgang 1 (intern)

Transkript (neu, Kategorie 1 und 2):
1. 5.5 nennt Fragen «zu ihren Sorten, zu den Kosten», die es nicht gab; Kosten wurden nicht gefragt (auch 5.5 Grenzen).
2. Die zwei unbeantworteten Fragen sind jetzt bekannt (Wirtschaft von Bohol, Zukunft in zehn Jahren).
3. «Stellen markiert, die sie nicht sicher verstanden hat» ist im Transkript nicht sichtbar; streichen.
4. «Bauern und Händler profitieren» → Tita sagt «farmers and vendors», also Verkäufer (auch Buch-Korrektur).
5. Titas eigene Erklärung «lack of supply due to increasing demands» fehlt im Kommentar; als persönliche Einschätzung einordnen (Prompt 5.3).
6. Fragen zum Teil auf Bohol zugeschnitten, Markt in Talisay City (Cebu); erste Antwort in der dritten Person → Grenze und offener Punkt.
7. 7.1: Preis 100 → 150 und «Bauern und Verkäufer profitieren» ergänzen (stützt Einwand 2 zu These 1).
8. 7.2: Platzhalter auflösbar (Exportstopp/Herkunftsschutz kamen nicht vor).
9. Anhang A aus dem Transkript bauen; Aufnahmedatum und Bestätigung bleiben offen.

Wissenschaft:
10. 7.1 «Der grösste Teil dieses Rückgangs liegt vor dem Boom» ist mit drei Datenpunkten nicht belegbar (2006 bis 2010 über 8'000 t, 2010 bis 2025 9'423 t) → «ein grosser Teil», mit Zahlen.
11. 7.4 Leitthese: Formulierung entscheiden (Kontrolle statt «verdienen wenig», weil Tita und FreshPlaza höhere Erlöse belegen) und Abstract, 1.2, 7.1 angleichen.
12. 7.1 Schluss «eine Chance, die bisher andere nutzen» → «die es bisher kaum nutzt».
13. 5.2: «Im Buch haben wir beide Stellen angeglichen» und «Den Beleg haben wir im Buch ausgetauscht» stimmen für das PDF vom 8.11. nicht (Korrekturliste) → umformulieren.
14. 4.4: Interview-Zitate sind im PDF nicht hervorgehoben → Text an den Stand anpassen.

Formales:
15. Platzhalter, die sich aus dem Material klären lassen: 2.2 Abgabe 17.06. (Journal), 2.3 Sommerferien (Journal 15.07.), 2.5 Treffen 14.09. (Journal 16.09.), 3.3/4.4 Messwerte (PDF), 3.4 Kapitel 3 ohne Bilder (PDF), 4.2 Kapitelnamen (PDF), 4.5/6.2 Seitenzahl 52 (PDF), 6.1 Seitenzahlen (PDF), 7.5 Tabelle (PDF), Mendoza-Abrufdatum, IPOPHL-Abrufdatum.
16. Nur die Gruppe: Klassen, Buchtitel, Wortlaut der Beurteilung, Seitenzahlen der Zitierregeln, Absprache Zitierweise, Bilddatenbank/Lizenz/Bildquellen, Papier/Bindung/Auflage, Kurzeinleitungen, Aufnahmedatum, Bestätigung durch Tita, Herkunft der Bewertung (Eingabe 7), eigener Anteil im KI-Nachweis, Eingabe 4 (Prompt, Datum), KI im Buchtext, Anhang B/C, CPBRD-URL, DA-23.06.-URL, USDA-Abrufdatum, letztes Journaldatum, Abgleich mit dem gedruckten Buch.

## Stand der Arbeit

Alle sieben Durchgänge abgeschlossen (9.11., 10:00). Alle Kapitel wurden vollständig geprüft, kein Teil ist ausgelassen. Offen bleibt nur, was in [[OFFENE_PUNKTE_FINAL]] steht (52 gelbe Stellen, davon Priorität 1: KI-Nachweis «Von uns», Eingabe 4, Herkunft der Bewertung, weitere KI-Nutzung, Anhang B, Interview-Angaben, Buchtitel, Klassen, Rechnung 850'000).

Für eine Fortsetzung: Text in `kommentar_quelle_final.txt` ändern und `python3 build_final.py` ausführen, oder direkt in `Schriftlicher_Kommentar_Ube_FINAL.docx` weiterarbeiten (dann ist Word die Wahrheit). Nach jeder weiteren Sitzung eine Eingabe in 10.6 ergänzen.
