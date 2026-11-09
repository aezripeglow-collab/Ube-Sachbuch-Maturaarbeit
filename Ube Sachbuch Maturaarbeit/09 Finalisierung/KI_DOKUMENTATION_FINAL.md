---
tags: [finalisierung, ki-nachweis, dokumentation]
stand: 2026-11-09 12:00
---
# KI_DOKUMENTATION_FINAL

Vollständige Dokumentation der KI-Nutzung für den schriftlichen Kommentar und das Arbeitsjournal, Stand 9.11.2026. Sie ergänzt den KI-Nachweis in Kapitel 10.6 des Kommentars (Kurzfassung) und enthält den **Wortlaut aller vier Master-Prompts** sowie die kurzen Nachrichten, die Claude erhalten hat. Zusammengestellt von Claude (Fable 5.1) am 9.11.2026 auf Grund der Dateien im Chat; alles, was nur die Gruppe weiss, ist als offen markiert und nicht erfunden.

> [!important] Was diese Datei kann und was nicht
> Sie dokumentiert, **was Claude bekommen und was Claude erstellt oder verändert hat.** Sie kann nicht dokumentieren, was ihr selbst gelesen, geprüft, übernommen, abgelehnt oder neu geschrieben habt. Diese Angaben («Von uns») fehlen bei allen neun Eingaben und sind der wichtigste offene Punkt vor der Abgabe (siehe [[OFFENE_PUNKTE_FINAL]], Priorität 1). Ohne sie würde der Kommentar als weitgehend KI-geschrieben gelten.

## 1. Was die Zitierregeln verlangen und was wir empfehlen

Laut Kommentar 10.6 darf KI nach den Zitierregeln der Kantonsschule Baden als Hilfe für Fragestellung, Struktur und Sprache genutzt werden, ihre Ergebnisse dürfen aber nicht wörtlich übernommen werden, und ihr Anteil muss nachvollziehbar sein (Seitenangabe im Kommentar mit Prüfvermerk, bitte an den Zitierregeln selbst prüfen; Claude hatte die Zitierregeln nicht vorliegen).

Für die Abgabe empfehlen wir:

1. **Im Kommentar bleibt der KI-Nachweis in 10.6** mit allen neun Eingaben in Kurzform (Prompt-Anfang, Mitgegeben, Erstellt, Verändert, Geprüft, Von uns). Dort müsst ihr die Felder «Von uns» ausfüllen.
2. **Die langen Prompts gehören nicht in den Kommentar.** Die vier Master-Prompts umfassen zusammen rund 15'500 Wörter; der erste allein füllt als Anhang B 19 Seiten. Gebt stattdessen diese Datei (als PDF oder ausgedruckt) zusammen mit den exportierten Chatverläufen als **separate KI-Dokumentation** ab oder legt sie auf Anfrage vor, und verweist in 10.6 darauf. Falls ihr Anhang B doch behalten wollt, müssen die Prompts 2 bis 4 als Anhang C bis E dazu, sonst ist der Nachweis unvollständig.
3. **Chatverläufe exportieren** (alle Chats vom 8. und 9. November) und aufbewahren. Nur dort stehen die Eingaben 1 bis 5 vollständig, der fehlende Prompt von Eingabe 4 und die Modellangaben.
4. **Buchtext:** Falls ihr den Buchtext mit KI sprachlich korrigiert oder Bilder mit KI erstellt habt, gehört das ebenfalls hierher und in 10.6 und 8.3. Claude weiss das nicht.
5. **Werkzeug für die Prompts:** Der Text, der den vierten Master-Prompt umgibt («Die persönliche Schreibstimme wird im neuen Prompt die höchste Priorität haben … Ich habe mir auch eure hochgeladene Word-Datei angesehen … Ein letzter Hinweis: Ein langer Prompt allein garantiert nicht …»), stammt offenbar nicht von euch, sondern von einem weiteren KI-Werkzeug, mit dem die Prompts formuliert wurden. Falls das so ist, gehört auch dieses Werkzeug mit Name und Datum in den Nachweis, und die Bewertung der zweiten Fassung (Eingabe 7) stammt dann vermutlich ebenfalls von dort. Bitte angeben.

## 2. Werkzeug und Modelle

- **Werkzeug:** Claude (Anthropic) in der Claude-App, mit Zugriff auf den Obsidian-Vault über das GitHub-Repository `aezripeglow-collab/Ube-Sachbuch-Maturaarbeit` (Branch master). Claude hat Dateien gelesen und geschrieben, Word-Dateien gebaut (docx-Bibliothek, LibreOffice für die Seitenzahlen), Rechnungen in Python nachgerechnet und für die Faktenprüfung Websuche und Webabruf benutzt. Keine Bildgenerierung; die Abbildungen 1 bis 4 und 6 sind mit Python (matplotlib) beziehungsweise aus dem Buch-PDF erstellt.
- **Modell:** Für die Eingaben 6 bis 9 ist die Sitzung auf das Modell `claude-fable-5-1` («Fable 5.1») eingestellt; das hat Aezri am 8.11. mit dem Befehl `/model claude-fable-5-1` umgestellt. Für die Eingaben 1 bis 5 stand im früheren KI-Nachweis «Opus 5.5». Claude kann das nicht nachprüfen; bitte im Chatverlauf nachsehen, welches Modell dort angezeigt wird, und die Angabe in 10.6 bestätigen oder korrigieren. Falls ihr es nicht mehr feststellen könnt, schreibt «Claude (Modell nicht mehr feststellbar)».
- **Sprache der Ausgaben:** Deutsch mit Schweizer Rechtschreibung, wie von euch verlangt.

## 3. Übersicht aller Eingaben

| Nr. | Datum | Modell | Was Claude bekommen hat | Was Claude erstellt oder verändert hat | Von uns |
| --- | --- | --- | --- | --- | --- |
| 1 | 08.11. | Opus 5.5 (prüfen) | Vault (Buchtext, Projektplan, Arbeitsjournal, Beurteilung 19.06., Quellenverzeichnis), Kommentar «Game Pressure» als Beispiel, Zitierregeln, Fotos eines weiteren Kommentars; Auftrag, den Kommentar zu schreiben | erster Entwurf des ganzen Kommentars mit Gliederung, Fussnoten, Verzeichnissen, Abbildungen 1 bis 4, Quellen für Kapitel 3 | offen |
| 2 | 08.11. | Opus 5.5 (prüfen) | Auftrag, den Entwurf Wort für Wort menschlicher zu schreiben und die genannten Fehler zu korrigieren | ganzer Entwurf sprachlich überarbeitet; falscher Beleg in These 1 gefunden und im Buchtext korrigiert | offen |
| 3 | 08.11. | Opus 5.5 (prüfen) | Auftrag, die Grafiken präziser und chronologisch tiefer zu machen | Abb. 1 bis 4 erweitert, Kapitel 2 ausführlicher | «Daten mit dem Journal verglichen» (bestätigen) |
| 4 | 08.11.? | Opus 5.5 (prüfen) | **Prompt und Datum fehlen** (aus dem Chatverlauf nachtragen) | Journaleinträge ab 05.06. in ganzen Sätzen aus euren Angaben | «gelesen und korrigiert» (welche Einträge?) |
| 5 | 08.11. | Opus 5.5 (prüfen) | erste Seiten des Buches als PDF; Auftrag, die fehlenden Journaleinträge zu ergänzen; Rückfragen beantwortet (Mittwocheinträge, Karte, Bilder, Korrekturlesen) | Journaleinträge 28.10. und 04.11. um die Arbeit am Buch ergänzt | offen |
| 6 | 08.11. abends | Fable 5.1 | **Master-Prompt 1** (Abschnitt 4.1), Buch-PDF vom 8.11. | Materialanalyse, Faktenprüfung mit Websuche, Bewertung, neue Gliederung, zweite Fassung (v2) mit Kapitel 7, 5.2, 5.5 neu, Korrekturliste Buch, Journalvorschläge | offen |
| 7 | 09.11. 00:53 | Fable 5.1 | **Master-Prompt 2** (Abschnitt 4.2) mit einer Bewertung der zweiten Fassung (fünf Kritikpunkte; Herkunft angeben) | dritte Fassung (v3): Abstract, 5.4, 5.5, 7.1 bis 7.4, 6.2, 8.3, KI-Nachweis; Websuche zu Marktdefinition, Asian Journal, Mendoza, FreshPlaza; Änderungsprotokoll | offen |
| 8 | 09.11. 08:39 | Fable 5.1 | **Master-Prompt 3** (Abschnitt 4.3) und das englische Transkript des Interviews (im selben Chat-Beitrag eingefügt; Wortlaut in Anhang A des Kommentars) | FINAL-Fassung des Kommentars: 5.5 und 7.1 nach dem Transkript berichtigt, Leitthese in 7.4 festgelegt, Anhang A, Platzhalter aufgelöst; `OFFENE_PUNKTE_FINAL`, `AENDERUNGSPROTOKOLL_FINAL`, `FORTSCHRITT_FINALKORREKTUR` | offen |
| 9 | 09.11. 10:36 | Fable 5.1 | **Master-Prompt 4** (Abschnitt 4.4), Aezris Familienchronik (Word) als Stilvorlage, Nachricht von Aezri (Abschnitt 4.4) | Stilprofil [[Schreibstimme Aezri]]; Kommentar im Stil-Durchgang angenähert (keine neuen Fakten); 5.5/Anhang A (Name «Tita»), 8.3, 10.6; `Arbeitsjournal_Ube_FINAL.docx` und `ARBEITSJOURNAL_FINAL.md`; `BUCH_KORREKTURLISTE_FINAL`, diese Datei, `QUALITAETSBEWERTUNG_FINAL`; Aktualisierung der Listen | offen |

Die Eingaben 1 bis 5 sind hier nur so genau wiedergegeben, wie sie im früheren KI-Nachweis standen (Claude in dieser Sitzung hat diese Chats nicht gesehen). Der genaue Wortlaut der Eingaben 1, 2, 3 und 5 steht in Kapitel 10.6 des Kommentars.

## 4. Wortlaut der Master-Prompts und Nachrichten

Die Prompts sind unverändert aus den Dateien übernommen, die Aezri in den Chat gestellt hat (Tippfehler eingeschlossen). Die Zeilen mit `{{…}}` und die Nummerierung stammen aus den Prompts selbst.


### 4.1 Master-Prompt 1 (Eingabe 6, 8.11.2026, abends)

Datei im Chat: `68025062-attachment.txt`, 3881 Wörter. Mitgegeben zusammen mit dem Buch-PDF vom 8.11. Im selben Chat-Beitrag hat Aezri mit `/model claude-fable-5-1` das Modell gewechselt; später im selben Chat, als Claude Schreibzugriff auf das Repository bekam, schrieb sie: «Github du kannst jetzt hineinschreiben».

> MASTER-PROMPT: Vollständige Finalisierung meiner Maturaarbeit über Ube
>
> 1. Deine Rolle und dein Auftrag
>
> Du agierst gleichzeitig als:
>
> * wissenschaftlicher Autor und kritischer wissenschaftlicher Lektor
> * Experte für Schweizer Maturaarbeiten und deren Bewertung auf Maturaniveau
> * sorgfältiger Quellenanalyst und Faktenprüfer
> * erfahrener Redaktor für Sachbücher und wissenschaftliche Kommentare
> * kritischer Betreuer, der Argumentationsschwächen erkennt und konsequent verbessert
>
> Deine Aufgabe ist es, meine gesamte Maturaarbeit auf ein möglichst hohes Qualitätsniveau zu bringen.
>
> Das Hauptziel ist ein inhaltlich überzeugender, wissenschaftlich fundierter, sprachlich natürlicher und eigenständiger schriftlicher Kommentar. Anschliessend soll mein gesamtes Arbeitsjournal überarbeitet werden, sodass es den tatsächlichen Entstehungsprozess korrekt dokumentiert und mit dem fertigen Sachbuch sowie dem wissenschaftlichen Kommentar übereinstimmt.
>
> Behandle das Projekt als zusammenhängende Maturaarbeit. Die drei Bestandteile müssen inhaltlich, methodisch und formal miteinander harmonieren:
>
> 1. Das Sachbuch beziehungsweise das eigentliche Produkt
> 2. Der wissenschaftliche Kommentar
> 3. Das Arbeitsjournal
>
> Alle drei Bestandteile sind wichtig. Vernachlässige keinen davon.
>
> Arbeite gründlich und mit hoher Eigenständigkeit. Warte nicht bei jedem kleinen Problem auf meine Rückmeldung. Triff sinnvolle redaktionelle Entscheidungen selbstständig, solange sie durch das vorhandene Material begründet sind. Bei wichtigen Unklarheiten, die du nicht zuverlässig lösen kannst, dokumentiere diese ausdrücklich, statt etwas zu erfinden.
>
> ⸻
>
> 2. Vollständige Analyse meines Obsidian-Vaults
>
> Du hast Zugriff auf meinen Obsidian-Vault. Nutze diesen Zugriff konsequent.
>
> Bevor du mit dem eigentlichen Schreiben beginnst, verschaffe dir einen möglichst vollständigen Überblick über sämtliche für die Maturaarbeit relevanten Dateien.
>
> Dazu gehören insbesondere:
>
> * das vollständige Sachbuch beziehungsweise der Produkttext
> * das Quellenverzeichnis und sämtliche verfügbaren Quellen
> * wissenschaftliche Studien und Statistiken
> * Zeitungsartikel und weitere journalistische Quellen
> * offizielle Dokumente und Daten von Behörden und Organisationen
> * mein bisheriger Entwurf des wissenschaftlichen Kommentars
> * mein vollständiges Arbeitsjournal
> * das Interview mit Tita
> * sämtliche Rechercheunterlagen, Notizen und ergänzenden Dokumente
> * schulische Vorgaben, Bewertungsraster und formale Anforderungen, sofern vorhanden
>
> Beschränke dich nicht auf die offensichtlich wichtigsten Dateien. Suche auch nach verstreuten Informationen, die für einzelne Argumente, die Methodik oder die Entstehungsgeschichte relevant sein könnten.
>
> Erstelle zuerst eine Übersicht darüber:
>
> 1. Welche relevanten Dateien vorhanden sind.
> 2. Welche Informationen sie enthalten.
> 3. Welche Quellen für welche Aussagen verwendet werden.
> 4. Welche Informationen sich mehrfach finden.
> 5. Wo Widersprüche, Lücken oder Unklarheiten bestehen.
> 6. Welche schulischen und formalen Anforderungen gelten.
>
> Gehe nicht davon aus, dass die Dateinamen den tatsächlichen Inhalt vollständig wiedergeben. Lies die relevanten Dokumente.
>
> Wichtig: Wenn du auf bestimmte Dateien nicht zugreifen kannst, erwähne das ausdrücklich. Behaupte niemals, den gesamten Vault analysiert zu haben, wenn du tatsächlich nur einen Teil davon sehen konntest.
>
> ⸻
>
> 3. Inhaltlicher Hintergrund der Maturaarbeit
>
> Das zentrale Thema meiner Arbeit lautet:
>
> «Wem gehört der Ube-Boom?»
>
> Die zentrale Leitthese lautet:
>
> «Die Philippinen verlieren beim Ube-Boom nicht ihre Kultur, sondern die Kontrolle über sie.»
>
> Die Arbeit beschäftigt sich mit dem weltweiten Aufstieg von Ube, einer violetten Yamswurzel, die insbesondere auf den Philippinen eine lange kulinarische und kulturelle Bedeutung hat.
>
> Ausgangspunkt ist die Beobachtung, dass Ube international zunehmend als Trendprodukt verwendet und vermarktet wird. Dabei stellt sich die Frage, welche Rolle die Philippinen in dieser Entwicklung spielen und wer tatsächlich von der steigenden internationalen Nachfrage profitiert.
>
> Der Begriff Kontrolle muss in zwei Dimensionen untersucht werden:
>
> A. Wirtschaftliche Kontrolle
>
> Hier geht es insbesondere um:
>
> * Wer verdient am internationalen Ube-Boom?
> * Wer kontrolliert Verarbeitung, Handel und Vermarktung?
> * Welche Rolle spielen Zwischenhändler und internationale Unternehmen?
> * In welchem Umfang profitieren philippinische Produzenten?
> * Welche wirtschaftlichen Möglichkeiten verliert oder gewinnt das Herkunftsland?
> * Welche Bedeutung haben lokale Verarbeitung, Exportstrategien und geschützte Herkunftsbezeichnungen?
> * Wie verändert die internationale Nachfrage die Situation auf dem philippinischen Binnenmarkt?
>
> B. Kulturelle Kontrolle
>
> Hier geht es insbesondere um:
>
> * Wer bestimmt, wie Ube international dargestellt wird?
> * Wird Ube als philippinisches Kulturgut wahrgenommen oder hauptsächlich als attraktive violette Zutat?
> * Was geht verloren, wenn ein traditionelles Lebensmittel zu einem globalen Lifestyle- und Trendprodukt wird?
> * Welche Bedeutung hat Ube für die Menschen auf den Philippinen?
> * Wie unterscheiden sich die Wahrnehmung und Verwendung von Ube auf den Philippinen und im Ausland?
>
> Diese beiden Dimensionen bilden den analytischen Rahmen. Sie sollen nicht einfach nebeneinanderstehen, sondern miteinander verknüpft werden.
>
> Wichtig: Verwende diese Beschreibung als Orientierung und nicht als Ersatz für die tatsächlichen Rechercheergebnisse. Überprüfe jede konkrete Behauptung anhand der vorhandenen Dokumente und Quellen.
>
> ⸻
>
> 4. Grundsätze für die wissenschaftliche Arbeit
>
> Die Qualität der Arbeit hängt nicht davon ab, möglichst viele Informationen unterzubringen, sondern davon, die relevanten Informationen richtig einzuordnen und daraus eine überzeugende Argumentation zu entwickeln.
>
> Halte dich deshalb an folgende Grundsätze:
>
> Quellen und Fakten
>
> * Verwende grundsätzlich die Informationen und Quellen aus meinem Obsidian-Vault.
> * Überprüfe Zahlen, Statistiken, Zeitangaben und konkrete Behauptungen anhand der Originalquellen, sofern diese verfügbar sind.
> * Übernimm keine Zahlen ungeprüft aus meinem bisherigen Kommentarentwurf.
> * Unterscheide klar zwischen gesicherten Fakten, Schätzungen, Prognosen, Interpretationen und persönlichen Aussagen.
> * Stelle Prognosen niemals als bereits eingetretene Tatsachen dar.
> * Achte auf unterschiedliche Bezugsjahre und Definitionen bei Statistiken.
> * Vergleiche Zahlen nur dann direkt, wenn ihre Grundlagen tatsächlich vergleichbar sind.
> * Verwende Quellen nicht als blossen Beleg für Aussagen, die sie inhaltlich gar nicht stützen.
> * Erfinde niemals Quellen, Seitenzahlen, Zitate, Statistiken oder Studienergebnisse.
> * Wenn eine Quelle nur eingeschränkt aussagekräftig ist, erkläre ihre Grenzen.
>
> Wissenschaftliche Argumentation
>
> * Entwickle eine klare Argumentationslinie.
> * Verknüpfe die einzelnen Erkenntnisse miteinander.
> * Erkläre, weshalb eine Information für die Leitthese relevant ist.
> * Berücksichtige Gegenargumente und alternative Erklärungen.
> * Vermeide einseitige oder voreilige Schlussfolgerungen.
> * Unterscheide zwischen Korrelation und Kausalität.
> * Mache deutlich, wo die vorhandenen Daten keine eindeutige Aussage erlauben.
> * Hinterfrage auch meine eigene Leitthese kritisch.
>
> Du sollst die Leitthese weder künstlich bestätigen noch zwanghaft widerlegen. Das Ergebnis muss sich aus dem Material ergeben.
>
> Umgang mit Unsicherheiten
>
> Wenn eine Information nicht ausreichend belegt ist:
>
> 1. Versuche, sie anhand anderer vorhandener Quellen zu überprüfen.
> 2. Prüfe, ob sie vorsichtiger formuliert werden kann.
> 3. Falls sie nicht zuverlässig verwendbar ist, kennzeichne sie als Unsicherheit.
> 4. Entferne sie gegebenenfalls aus der Argumentation.
>
> Erfinde keine Ergänzungen, nur damit der Text vollständig wirkt.
>
> ⸻
>
> 5. Analyse des bisherigen Kommentarentwurfs
>
> Mein bisheriger wissenschaftlicher Kommentar ist ein Ausgangspunkt, aber nicht die endgültige Grundlage.
>
> Analysiere ihn kritisch und prüfe insbesondere:
>
> * Ist die Leitfrage klar beantwortet?
> * Ist die zentrale These überzeugend entwickelt?
> * Gibt es eine nachvollziehbare Argumentationsstruktur?
> * Sind die einzelnen Kapitel sinnvoll miteinander verbunden?
> * Werden Quellen richtig interpretiert?
> * Gibt es unbelegte Behauptungen?
> * Werden wichtige Aspekte nur oberflächlich behandelt?
> * Gibt es Wiederholungen?
> * Gibt es unnötige Beschreibungen, die keinen analytischen Mehrwert bieten?
> * Werden Gegenargumente ausreichend berücksichtigt?
> * Ist die eigene methodische Vorgehensweise kritisch reflektiert?
> * Ist der Text tatsächlich ein wissenschaftlicher Kommentar oder eher eine Zusammenfassung des Sachbuchs?
>
> Behalte gute Gedanken und brauchbare Formulierungen bei. Überarbeite aber alles, was inhaltlich, argumentativ oder sprachlich verbessert werden kann.
>
> Scheue dich nicht, ganze Abschnitte neu aufzubauen oder zu ersetzen, wenn dadurch eine deutlich bessere Arbeit entsteht.
>
> ⸻
>
> 6. Das Sachbuch als Grundlage des Kommentars
>
> Lies das vollständige Sachbuch sorgfältig.
>
> Der wissenschaftliche Kommentar soll das Sachbuch nicht einfach wiederholen. Er soll dessen Inhalt wissenschaftlich einordnen, die Recherche dahinter offenlegen und die daraus gewonnenen Erkenntnisse kritisch untersuchen.
>
> Achte insbesondere auf folgende Fragen:
>
> * Welche Aussagen und Erkenntnisse des Sachbuchs sind besonders relevant?
> * Welche Quellen und Rechercheergebnisse bilden die Grundlage?
> * Welche Aspekte werden im Sachbuch bewusst vereinfacht oder ausgelassen?
> * Welche Aussagen benötigen eine genauere wissenschaftliche Einordnung?
> * Welche Erkenntnisse sind besonders überraschend oder widersprüchlich?
> * Wo zeigt sich die wirtschaftliche Kontrolle über Ube?
> * Wo zeigt sich die kulturelle Kontrolle über Ube?
> * Welche Rolle spielt das Interview mit Tita?
> * Welche Grenzen hat die eigene Recherche?
>
> Der Kommentar muss eigenständig funktionieren. Eine Person, die nur den Kommentar liest, soll die Forschungsfrage, die Argumentation, die wichtigsten Erkenntnisse und die Grenzen der Untersuchung verstehen können.
>
> Vermeide es, Kapitel des Sachbuchs einfach nacheinander zusammenzufassen.
>
> ⸻
>
> 7. Umgang mit dem Interview
>
> Das Interview mit Tita ist ein wichtiger Bestandteil meiner eigenen Recherche.
>
> Berücksichtige es sorgfältig und prüfe:
>
> * Welche Aussagen macht Tita über den Ube-Anbau und den Verkauf?
> * Welche Bedeutung hat Ube für ihre persönliche und wirtschaftliche Situation?
> * Welche Veränderungen bei Nachfrage, Verfügbarkeit und Preisen beschreibt sie?
> * Welche Aussagen lassen sich mit statistischen Daten oder anderen Quellen vergleichen?
> * Wo ergänzt ihre persönliche Erfahrung die übergeordneten Daten?
> * Wo darf ihre individuelle Erfahrung nicht verallgemeinert werden?
>
> Das Interview soll nicht bloss dekorativ eingebaut werden. Es soll dort verwendet werden, wo es tatsächlich einen Erkenntnisgewinn liefert.
>
> Unterscheide konsequent zwischen:
>
> * Titas persönlichen Erfahrungen
> * ihren Einschätzungen
> * objektiv überprüfbaren Angaben
> * meinen eigenen Interpretationen
>
> Erfinde keine Aussagen und verändere nicht den Sinn ihrer Antworten.
>
> Falls Informationen zur Kontaktaufnahme, zur Identität, zur Zustimmung zur Veröffentlichung oder zur Durchführung des Interviews fehlen, kennzeichne diese Punkte als offen. Erfinde keine Angaben dazu.
>
> ⸻
>
> 8. Entwicklung einer überzeugenden Struktur
>
> Entwickle zunächst eine optimale Gliederung für den wissenschaftlichen Kommentar.
>
> Die Gliederung soll eine klare innere Logik haben und die Forschungsfrage schrittweise beantworten.
>
> Überlege dabei:
>
> * Welche Aspekte müssen unbedingt behandelt werden?
> * Welche Argumente bauen aufeinander auf?
> * Welche Informationen gehören zusammen?
> * Wo sind Übergänge notwendig?
> * Welche Aspekte sind für die Leitthese zentral?
> * Welche Aspekte sind interessant, aber für den Kommentar weniger relevant?
>
> Vermeide eine Struktur, die lediglich die Reihenfolge des Sachbuchs übernimmt.
>
> Die Argumentation soll einen erkennbaren gedanklichen Fortschritt aufweisen.
>
> Erstelle vor dem vollständigen Schreiben eine detaillierte Argumentationsstruktur mit:
>
> 1. Kapitel und Unterkapiteln
> 2. Kernaussage jedes Abschnitts
> 3. verwendeten Quellen
> 4. relevanten Fakten und Beispielen
> 5. Verbindung zur Leitthese
> 6. möglichen Gegenargumenten
> 7. Übergang zum nächsten Abschnitt
>
> Erst wenn diese Struktur schlüssig ist, beginnst du mit dem vollständigen Kommentar.
>
> ⸻
>
> 9. Meine persönliche Schreibstimme und mein Sprachstil
>
> Dieser Punkt ist besonders wichtig und muss während der gesamten Arbeit berücksichtigt werden.
>
> Deine Aufgabe ist nicht, meinen Text durch deinen eigenen bevorzugten Schreibstil zu ersetzen. Deine Aufgabe ist es, meine Gedanken auf das bestmögliche sprachliche und wissenschaftliche Niveau zu bringen, ohne dass sie dabei ihre persönliche Stimme verlieren.
>
> Analysiere vor dem Schreiben möglichst genau meine bisherigen Texte. Verwende dafür insbesondere:
>
> * meinen bisherigen Kommentarentwurf
> * mein Sachbuch
> * mein Arbeitsjournal
> * weitere eigene schriftliche Arbeiten im Vault, sofern vorhanden
>
> Analysiere dabei:
>
> * meine typische Wortwahl und meinen Wortschatz
> * meine Satzlängen und meinen Satzbau
> * meine Art, Argumente aufzubauen und Gedanken miteinander zu verbinden
> * meine bevorzugten Formulierungen und sprachlichen Eigenheiten
> * mein Verhältnis zwischen sachlicher und persönlicher Sprache
> * meinen Umgang mit komplexen Themen und wissenschaftlichen Begriffen
> * meine Art, eigene Gedanken und Schlussfolgerungen auszudrücken
> * meinen natürlichen Schreibfluss und meine Übergänge zwischen Abschnitten
>
> Erstelle auf dieser Grundlage ein internes Stilprofil, das du während der gesamten Ausarbeitung als verbindliche Orientierung verwendest. Speichere die wichtigsten Erkenntnisse zusätzlich in der Materialanalyse, damit sie bei einer späteren Fortsetzung erhalten bleiben.
>
> Meine persönliche Schreibstimme hat Priorität
>
> Verwende meine bisherigen Texte als stilistische Grundlage. Übernimm nicht einfach einzelne Formulierungen, sondern erkenne die charakteristischen Merkmale meiner Schreibweise.
>
> Wenn du zwischen einer stilistisch perfekten, aber unpersönlichen Formulierung und einer ebenso korrekten Formulierung wählen musst, die besser zu meiner eigenen Schreibweise passt, bevorzuge grundsätzlich die zweite.
>
> Verbessere meine Ausdrucksweise, aber ersetze nicht meine Persönlichkeit durch einen generischen akademischen Stil.
>
> Der fertige Text soll so wirken, als hätte ich ihn selbst geschrieben, nachdem ich meine Gedanken sorgfältig überarbeitet, meine Recherche vertieft und meine Argumentation verbessert hätte.
>
> Der Kommentar soll nicht wie ein Text wirken, den eine fremde Person über mein Thema geschrieben hat. Er soll wie meine eigene, bestmöglich überarbeitete Arbeit klingen.
>
> Sprachliche Anforderungen
>
> * Schreibe auf Deutsch.
> * Verwende Schweizer Rechtschreibung, insbesondere «ss» statt «ß».
> * Formuliere präzise und verständlich.
> * Verwende eine natürliche, sachliche und differenzierte Sprache.
> * Baue komplexe Gedanken verständlich auf.
> * Verwende Fachbegriffe dort, wo sie sinnvoll sind, erkläre sie aber bei Bedarf.
> * Vermeide unnötig komplizierte Satzkonstruktionen.
> * Vermeide übertriebene akademische Formulierungen.
> * Vermeide künstlich aufgeblähte Absätze.
> * Vermeide typische KI-Formulierungen und leere Überleitungen.
> * Vermeide unnötige Wiederholungen.
> * Schreibe nicht ständig nach demselben Satzmuster.
> * Verwende keine übertriebenen Einleitungen wie «In der heutigen globalisierten Welt».
> * Vermeide pathetische oder journalistisch übertriebene Formulierungen.
> * Vermeide unbegründete Werturteile.
> * Verwende Gedankenstriche nicht als Ersatz für saubere Satzkonstruktionen.
>
> Der Text darf anspruchsvoll sein, muss aber glaubwürdig und natürlich bleiben.
>
> Schreibe nicht absichtlich schlechter oder baue künstliche Fehler ein, um menschlich zu wirken. Das Ziel ist eine sehr gute Arbeit, die trotzdem meine persönliche Schreibstimme bewahrt.
>
> ⸻
>
> 10. Vollständige Ausarbeitung des wissenschaftlichen Kommentars
>
> Schreibe nach Abschluss der Analyse und Strukturierung den vollständigen wissenschaftlichen Kommentar.
>
> Dabei gelten folgende Anforderungen:
>
> * Halte dich an die tatsächlichen schulischen Vorgaben, sofern diese im Vault vorhanden sind.
> * Berücksichtige die verlangte Länge und die formalen Anforderungen.
> * Verwende eine klare Einleitung, einen logisch aufgebauten Hauptteil und einen überzeugenden Schluss.
> * Beantworte die Forschungsfrage ausdrücklich.
> * Verknüpfe wirtschaftliche und kulturelle Kontrolle miteinander.
> * Beziehe das Sachbuch, die Quellen und das Interview sinnvoll ein.
> * Reflektiere die eigene Vorgehensweise und die Grenzen der Recherche.
> * Unterscheide zwischen den Erkenntnissen der Recherche und den daraus gezogenen Schlussfolgerungen.
> * Verwende korrekte Quellenangaben entsprechend den vorhandenen schulischen Vorgaben.
> * Achte darauf, dass jede wesentliche Behauptung nachvollziehbar belegt ist.
>
> Der Schluss soll nicht bloss die vorherigen Kapitel wiederholen. Er soll die gewonnenen Erkenntnisse zusammenführen und eine differenzierte Antwort auf die Forschungsfrage geben.
>
> Der Kommentar soll eine eigenständige wissenschaftliche Leistung darstellen.
>
> ⸻
>
> 11. Überarbeitung des gesamten Arbeitsjournals
>
> Das Arbeitsjournal ist ein gleichwertiger Bestandteil des Projekts und darf nicht vernachlässigt werden.
>
> Die endgültige Überarbeitung des Arbeitsjournals erfolgt erst, nachdem der wissenschaftliche Kommentar vollständig ausgearbeitet wurde.
>
> Beginne aber bereits während der Analyse damit, das vorhandene Arbeitsjournal genau zu untersuchen und relevante Informationen für die spätere Überarbeitung zu sammeln.
>
> Ziel ist ein vollständiges, glaubwürdiges und gut strukturiertes Arbeitsjournal, das den tatsächlichen Entstehungsprozess der Maturaarbeit dokumentiert.
>
> Inhaltliche Anforderungen
>
> Das Arbeitsjournal muss mit dem fertigen Sachbuch und dem wissenschaftlichen Kommentar übereinstimmen.
>
> Überprüfe deshalb:
>
> * Sind alle wichtigen Arbeitsschritte dokumentiert?
> * Ist die zeitliche Reihenfolge nachvollziehbar?
> * Stimmen die beschriebenen Entscheidungen mit dem tatsächlichen Projektverlauf überein?
> * Werden wichtige Recherchephasen erwähnt?
> * Sind Änderungen der Fragestellung oder des Konzepts nachvollziehbar?
> * Werden Schwierigkeiten und Probleme realistisch dargestellt?
> * Sind die beschriebenen Fortschritte mit den tatsächlichen Ergebnissen vereinbar?
> * Stimmen die im Journal erwähnten Kapitel und Inhalte mit dem fertigen Sachbuch überein?
> * Werden die Entscheidungen, die im wissenschaftlichen Kommentar reflektiert werden, auch im Arbeitsprozess nachvollziehbar?
>
> Besonders wichtige Regel: Keine erfundenen Arbeitsschritte
>
> Du darfst das Arbeitsjournal sprachlich verbessern, strukturieren, präzisieren und verständlicher machen.
>
> Du darfst jedoch niemals nachträglich Ereignisse erfinden.
>
> Erfinde insbesondere keine:
>
> * Treffen
> * Gespräche
> * Interviews
> * Recherchearbeiten
> * Arbeitsschritte
> * Entscheidungen
> * Probleme
> * Fortschritte
> * Rückmeldungen von Lehrpersonen
> * Daten oder Zeitangaben
>
> Stelle keine später gewonnenen Erkenntnisse so dar, als wären sie bereits zu einem früheren Zeitpunkt bekannt gewesen.
>
> Das Journal soll den tatsächlichen Verlauf dokumentieren und nicht rückwirkend eine künstlich perfekte Projektgeschichte konstruieren.
>
> Wenn Angaben fehlen oder widersprüchlich sind, markiere diese in einer separaten Liste als offene Punkte.
>
> Sprachliche Überarbeitung
>
> Das Arbeitsjournal soll ebenfalls natürlich und glaubwürdig klingen.
>
> Es darf etwas persönlicher und weniger formal sein als der wissenschaftliche Kommentar.
>
> Behalte den Charakter eines echten Arbeitsjournals bei. Es soll nicht wie ein zweiter wissenschaftlicher Kommentar wirken.
>
> Verbessere die Sprache, ohne die persönliche Perspektive und den tatsächlichen Charakter des Journals zu verlieren.
>
> Vollständigkeitsprüfung
>
> Vergleiche das gesamte Journal systematisch mit dem fertigen Sachbuch und dem Kommentar.
>
> Achte besonders darauf, dass:
>
> * wichtige Entwicklungen nicht fehlen
> * keine falschen zeitlichen Zusammenhänge entstehen
> * keine späteren Erkenntnisse rückwirkend als frühere Gedanken erscheinen
> * keine Widersprüche zwischen den drei Bestandteilen bestehen
> * die Entwicklung des Projekts nachvollziehbar bleibt
>
> ⸻
>
> 12. Einheitlichkeit der gesamten Maturaarbeit
>
> Nachdem Kommentar und Arbeitsjournal fertiggestellt wurden, führst du eine umfassende Konsistenzprüfung durch.
>
> Vergleiche:
>
> 1. Sachbuch
> 2. Wissenschaftlichen Kommentar
> 3. Arbeitsjournal
> 4. Quellenverzeichnis
> 5. Interview und ergänzende Rechercheunterlagen
>
> Prüfe insbesondere:
>
> * Stimmen alle Zahlen und Daten überein?
> * Werden Begriffe einheitlich verwendet?
> * Sind die zentralen Aussagen konsistent?
> * Stimmen die Quellenangaben?
> * Gibt es widersprüchliche Aussagen?
> * Wird die Leitthese in allen Teilen gleich verstanden?
> * Sind die wirtschaftliche und kulturelle Dimension klar voneinander abgegrenzt und gleichzeitig miteinander verbunden?
> * Entspricht das Arbeitsjournal dem tatsächlichen Projektverlauf?
> * Gibt es Aussagen im Kommentar, die im Sachbuch oder in den Quellen keine Grundlage haben?
> * Gibt es wichtige Erkenntnisse im Sachbuch, die im Kommentar überhaupt nicht berücksichtigt werden?
>
> Achte darauf, dass die drei Bestandteile zusammen eine überzeugende Gesamtarbeit ergeben.
>
> ⸻
>
> 13. Qualitätskontrolle auf höchstem Niveau
>
> Bewerte den fertigen wissenschaftlichen Kommentar kritisch, als würdest du ihn als anspruchsvoller Schweizer Maturitätsexperte beurteilen.
>
> Prüfe ihn anhand folgender Kriterien:
>
> Inhalt
>
> * Wird die Forschungsfrage vollständig beantwortet?
> * Ist die Argumentation tiefgründig?
> * Werden relevante Zusammenhänge erkannt?
> * Werden unterschiedliche Perspektiven berücksichtigt?
> * Sind die Schlussfolgerungen nachvollziehbar?
>
> Wissenschaftlichkeit
>
> * Sind die Quellen zuverlässig und korrekt verwendet?
> * Ist die Methodik transparent?
> * Werden die Grenzen der eigenen Untersuchung reflektiert?
> * Werden Fakten und Interpretationen sauber getrennt?
> * Sind die Aussagen angemessen differenziert?
>
> Aufbau
>
> * Ist der Aufbau logisch?
> * Gibt es einen klaren roten Faden?
> * Sind die Kapitel sinnvoll miteinander verbunden?
> * Gibt es unnötige Wiederholungen oder Abschweifungen?
>
> Sprache
>
> * Ist der Text präzise und verständlich?
> * Klingt er natürlich?
> * Entspricht er einem sehr guten Maturaniveau?
> * Gibt es unnötig komplizierte Formulierungen?
> * Wirkt der Text stellenweise künstlich oder generisch?
> * Ist meine persönliche Schreibstimme erkennbar?
>
> Eigenständigkeit
>
> * Wird eine eigene Argumentation entwickelt?
> * Geht der Kommentar über eine reine Zusammenfassung hinaus?
> * Werden eigene Erkenntnisse und Überlegungen sichtbar?
> * Wird die Leitthese kritisch geprüft?
>
> Überarbeite erkannte Schwächen direkt im Text.
>
> Gib dich nicht mit einer bloss akzeptablen Version zufrieden. Ziel ist eine möglichst überzeugende und sorgfältig ausgearbeitete Maturaarbeit.
>
> Erfinde aber keine zusätzliche Komplexität, nur um den Text wissenschaftlicher erscheinen zu lassen.
>
> ⸻
>
> 14. Projektmanagement und Sicherung des Arbeitsfortschritts
>
> Ein besonders wichtiger Teil dieses Auftrags ist die zuverlässige Sicherung der Arbeit.
>
> Du musst davon ausgehen, dass deine verfügbare Nutzungszeit beziehungsweise dein Kontingent während der Bearbeitung enden kann.
>
> Versuche deshalb niemals, die gesamte Arbeit in einer einzigen Sitzung ohne Zwischenspeicherung fertigzustellen.
>
> Qualität ist wichtiger als Geschwindigkeit. Gleichzeitig muss jeder bereits erreichte Fortschritt zuverlässig gesichert werden.
>
> Lege im Obsidian-Vault folgenden Ordner an:
>
> Maturaarbeit/Finalisierung/
>
> Erstelle darin folgende Arbeitsdateien:
>
> * 00_PROJEKTSTATUS.md
> * 01_MATERIALANALYSE.md
> * 02_ARGUMENTATIONSSTRUKTUR.md
> * 03_KOMMENTAR_ENTWURF.md
> * 04_ARBEITSJOURNAL_ENTWURF.md
> * 05_KONSISTENZPRUEFUNG.md
> * 06_OFFENE_AUFGABEN.md
>
> Wenn bereits ein entsprechender Ordner oder gleichwertige Dateien existieren, prüfe zuerst, ob du sie sinnvoll weiterverwenden kannst.
>
> Überschreibe niemals meine ursprünglichen Dokumente. Arbeite mit neuen Dateien beziehungsweise Arbeitskopien. Die Originale müssen erhalten bleiben.
>
> Inhalt der Statusdatei
>
> Die Datei 00_PROJEKTSTATUS.md muss jederzeit den aktuellen Stand der Arbeit wiedergeben.
>
> Sie soll mindestens folgende Informationen enthalten:
>
> 1. Projektziel und zentrale Forschungsfrage
> 2. Übersicht der vorhandenen Materialien
> 3. Bereits vollständig abgeschlossene Arbeitsschritte
> 4. Bereits getroffene inhaltliche und strukturelle Entscheidungen
> 5. Aktuelle Gliederung des Kommentars
> 6. Bereits fertiggestellte Textabschnitte
> 7. Noch ausstehende Arbeitsschritte
> 8. Offene inhaltliche und methodische Fragen
> 9. Quellen oder Fakten, die noch überprüft werden müssen
> 10. Exakter nächster Arbeitsschritt
> 11. Hinweise für die Fortsetzung in einer neuen Sitzung
> 12. Das erstellte Stilprofil meiner persönlichen Schreibstimme
>
> Regelmässige Zwischenspeicherung
>
> Speichere nach jedem grösseren Arbeitsschritt.
>
> Dazu gehören insbesondere:
>
> * nach der Materialanalyse
> * nach der Quellenprüfung
> * nach der Analyse des Kommentarentwurfs
> * nach der Erstellung der Argumentationsstruktur
> * nach jedem fertiggestellten grösseren Kommentarabschnitt
> * nach Fertigstellung des Kommentars
> * nach der Überarbeitung des Arbeitsjournals
> * nach der abschliessenden Konsistenzprüfung
>
> Aktualisiere nach jedem dieser Schritte auch die Statusdatei.
>
> Verlasse dich niemals darauf, dass du dich in einer späteren Sitzung an deine bisherigen Überlegungen erinnern kannst.
>
> Die Dateien im Obsidian-Vault sind die verbindliche Grundlage für die Fortsetzung.
>
> Wenn das Kontingent knapp wird
>
> Falls du erkennst, dass deine verfügbare Nutzungszeit oder dein Kontingent bald erschöpft sein könnte, unterbrich die inhaltliche Arbeit und sichere zuerst den aktuellen Stand.
>
> Priorität:
>
> 1. Aktuellen Arbeitsstand speichern.
> 2. Alle bereits erarbeiteten Inhalte sichern.
> 3. Statusdatei vollständig aktualisieren.
> 4. Offene Aufgaben dokumentieren.
> 5. Den nächsten Arbeitsschritt so genau beschreiben, dass eine neue Sitzung unmittelbar weiterarbeiten kann.
>
> Beginne keine neuen umfangreichen Analysen, wenn du nicht mehr genügend Kapazität hast, um die bisherigen Ergebnisse zuverlässig zu sichern.
>
> Behaupte niemals, eine Datei gespeichert zu haben, wenn dies nicht tatsächlich geschehen ist.
>
> Fortsetzung am nächsten Tag
>
> Wenn das Kontingent aufgebraucht ist und die Arbeit erst nach der Rücksetzung fortgesetzt werden kann, muss eine neue Sitzung ohne unnötige Wiederholung weiterarbeiten können.
>
> Dafür soll 00_PROJEKTSTATUS.md eine eindeutige Fortsetzungsanweisung enthalten.
>
> Bei einer neuen Sitzung gilt:
>
> 1. Lies zuerst 00_PROJEKTSTATUS.md.
> 2. Prüfe die darin genannten Arbeitsdateien.
> 3. Überprüfe, welche Arbeitsschritte tatsächlich abgeschlossen sind.
> 4. Lies die ursprünglichen Materialien nur dort erneut, wo es für die Fortsetzung notwendig ist.
> 5. Setze exakt beim dokumentierten nächsten Arbeitsschritt an.
> 6. Wiederhole keine bereits abgeschlossenen Arbeiten ohne konkreten Grund.
> 7. Aktualisiere nach der Fortsetzung erneut die Statusdatei.
> 8. Verwende weiterhin das gespeicherte Stilprofil meiner persönlichen Schreibstimme.
>
> Die Fortsetzung muss auch dann funktionieren, wenn der gesamte bisherige Chatverlauf nicht mehr verfügbar ist.
>
> ⸻
>
> 15. Reihenfolge der gesamten Bearbeitung
>
> Arbeite in folgender Reihenfolge:
>
> Phase 1: Vollständige Bestandsaufnahme
>
> Analysiere den Vault, identifiziere alle relevanten Dokumente und erstelle die Materialübersicht.
>
> Analysiere dabei auch meine persönliche Schreibstimme und erstelle ein Stilprofil.
>
> Speichere die Ergebnisse in 01_MATERIALANALYSE.md.
>
> Phase 2: Quellen- und Faktenprüfung
>
> Überprüfe die wesentlichen Fakten, Zahlen, Quellen und Aussagen. Dokumentiere Unsicherheiten und Widersprüche.
>
> Ergänze die Materialanalyse und die offene Aufgabenliste.
>
> Phase 3: Analyse des bisherigen Kommentarentwurfs
>
> Bewerte den bisherigen Kommentar kritisch und identifiziere konkrete Verbesserungsmöglichkeiten.
>
> Phase 4: Entwicklung der Argumentation
>
> Erstelle eine überzeugende Gliederung und eine detaillierte Argumentationsstruktur.
>
> Speichere diese in 02_ARGUMENTATIONSSTRUKTUR.md.
>
> Phase 5: Vollständige Ausarbeitung des wissenschaftlichen Kommentars
>
> Schreibe den Kommentar vollständig und überarbeite ihn anschliessend kritisch.
>
> Bewahre dabei konsequent meine persönliche Schreibstimme.
>
> Speichere den Text in 03_KOMMENTAR_ENTWURF.md.
>
> Phase 6: Überarbeitung des Arbeitsjournals
>
> Erst nachdem der Kommentar fertiggestellt wurde, überarbeite das gesamte Arbeitsjournal.
>
> Speichere die überarbeitete Version in 04_ARBEITSJOURNAL_ENTWURF.md.
>
> Phase 7: Konsistenzprüfung
>
> Vergleiche alle drei Bestandteile und prüfe die Übereinstimmung mit den Quellen.
>
> Dokumentiere die Ergebnisse in 05_KONSISTENZPRUEFUNG.md.
>
> Phase 8: Abschliessende Qualitätskontrolle
>
> Führe eine letzte sprachliche, inhaltliche, wissenschaftliche und formale Prüfung durch.
>
> Korrigiere alle eindeutig erkennbaren Schwächen.
>
> Phase 9: Offene Punkte
>
> Erstelle eine übersichtliche Liste aller Punkte, die noch meine Entscheidung, zusätzliche Informationen oder eine manuelle Überprüfung benötigen.
>
> Speichere diese in 06_OFFENE_AUFGABEN.md.
>
> ⸻
>
> 16. Abschliessende Ergebnisse
>
> Am Ende sollen folgende Ergebnisse vorliegen:
>
> 1. Finaler wissenschaftlicher Kommentar
>
> Ein vollständig ausgearbeiteter, wissenschaftlich fundierter und sprachlich überzeugender Kommentar, der meine persönliche Schreibstimme bewahrt.
>
> 2. Finales Arbeitsjournal
>
> Ein vollständig überarbeitetes, chronologisch nachvollziehbares und authentisches Arbeitsjournal.
>
> 3. Konsistenz- und Qualitätsbericht
>
> Eine kritische Bewertung der gesamten Maturaarbeit mit den wichtigsten vorgenommenen Verbesserungen und allfälligen verbleibenden Schwächen.
>
> 4. Liste offener Punkte
>
> Eine klare Liste aller Angaben, die nicht zuverlässig überprüft oder ohne meine Mitwirkung ergänzt werden können.
>
> 5. Aktualisierte Projektstatusdatei
>
> Eine vollständige Dokumentation des Projektstands, damit die Arbeit jederzeit fortgesetzt werden kann.
>
> ⸻
>
> 17. Abschliessende Anweisungen
>
> Nimm dir für die Arbeit so viel Zeit und Kapazität, wie innerhalb deiner tatsächlichen technischen und kontingentbedingten Grenzen verfügbar ist.
>
> Es gibt keinen künstlichen Zeitdruck. Eine gründliche und qualitativ hochwertige Arbeit ist wichtiger als eine schnelle Fertigstellung.
>
> Arbeite selbstständig und kritisch. Schreibe nicht einfach möglichst viel Text, sondern konzentriere dich auf die Qualität der Argumentation.
>
> Vermeide unnötige Rückfragen, wenn du eine Entscheidung anhand des vorhandenen Materials selbst treffen kannst. Wenn eine wichtige Information fehlt, dokumentiere sie und arbeite mit den übrigen verfügbaren Informationen weiter.
>
> Verändere keine Originaldateien.
>
> Erfinde keine Fakten, Quellen, Zitate, Erfahrungen oder Arbeitsschritte.
>
> Achte während der gesamten Arbeit darauf, dass der wissenschaftliche Kommentar und das Arbeitsjournal meine eigene Schreibstimme bewahren. Der Text soll sprachlich verbessert sein, aber weiterhin eindeutig wie meine eigene Arbeit wirken.
>
> Stelle sicher, dass jeder grössere Fortschritt gespeichert wird.
>
> Beginne jetzt mit Phase 1: der vollständigen Bestandsaufnahme und Analyse meines Obsidian-Vaults. Schreibe noch nicht sofort den fertigen Kommentar. Arbeite zuerst das Material gründlich durch und halte alle Ergebnisse in den vorgesehenen Dateien fest.

### 4.2 Master-Prompt 2 (Eingabe 7, 9.11.2026, 00:53)

Datei im Chat: `3b5897bc-attachment.txt`, 3846 Wörter. Der Prompt enthält die Bewertung der zweiten Fassung mit den fünf Kritikpunkten; von wem diese Bewertung stammt, ist offen (siehe Abschnitt 1, Punkt 5).

> MASTER-PROMPT: Abschliessende wissenschaftliche Überarbeitung und Fertigstellung des Maturaarbeits-Kommentars
>
> 1. Deine Rolle und dein Auftrag
>
> Du übernimmst die Rolle eines erfahrenen wissenschaftlichen Lektors, kritischen akademischen Gutachters und sorgfältigen Redakteurs für eine Schweizer Maturaarbeit.
>
> Dein Auftrag ist es, meinen bereits vollständig verfassten wissenschaftlichen Kommentar zu unserer Maturaarbeit über den internationalen Ube-Boom anhand des nachfolgenden Feedbacks systematisch zu überprüfen, wissenschaftlich zu verbessern und vollständig abgabefertig zu machen.
>
> Du sollst nicht einfach einen neuen Kommentar schreiben.
>
> Du sollst unseren bestehenden Kommentar verbessern, seine wissenschaftlichen Schwächen beheben, offene Stellen vervollständigen, Aussagen überprüfen und seine Qualität auf ein sehr hohes Maturaniveau bringen.
>
> Dabei gelten drei gleich wichtige Ziele:
>
> 1. Wissenschaftliche Korrektheit: Jede Aussage muss nachvollziehbar, methodisch sauber und durch die vorhandenen Quellen gedeckt sein.
> 2. Inhaltliche Qualität: Die Argumentation soll differenziert, logisch und überzeugend sein. Widersprüche und Schwächen müssen erkannt und tatsächlich behoben werden.
> 3. Authentische Schreibstimme: Der Kommentar muss weiterhin wie von uns selbst geschrieben klingen. Er darf nicht wie ein künstlich perfektionierter KI-Text wirken.
>
> Das Endprodukt soll ein vollständig überarbeiteter, konsistenter und formal möglichst abgabefertiger wissenschaftlicher Kommentar sein.
>
> ⸻
>
> 2. Zuerst: Alle verfügbaren Materialien vollständig prüfen
>
> Du hast Zugriff auf unseren Obsidian-Vault und die dort vorhandenen Projektmaterialien.
>
> Nutze diesen Zugriff aktiv und vollständig.
>
> Berücksichtige insbesondere:
>
> * Den aktuellen vollständigen Kommentarentwurf.
> * Das fertige beziehungsweise aktuelle Sachbuch.
> * Das vollständige Quellenverzeichnis.
> * Die verwendeten Originalquellen und wissenschaftlichen Studien.
> * Das Arbeitsjournal.
> * Das Interview mit Tita.
> * Die Interviewfragen und das englische Originaltranskript.
> * Vorhandene Berechnungen, Tabellen und Abbildungen.
> * Frühere Entwürfe und relevante Projektdokumente.
> * Bereits vorhandene KI-Dokumentationen und Prompts.
>
> Öffne nicht nur den Kommentar und beginne sofort mit dem Umschreiben.
>
> Verschaffe dir zunächst einen Überblick über die vorhandenen Materialien und ihre Zusammenhänge.
>
> Verbindliche Quellenhierarchie
>
> Verwende Informationen in folgender Reihenfolge:
>
> 1. Originalquellen und wissenschaftliche Studien.
> 2. Offizielle Statistiken und Behördenpublikationen.
> 3. Das Interview mit Tita als eigene empirische Quelle.
> 4. Unser fertiges Sachbuch und unsere eigenen Projektdokumente.
> 5. Sekundärliteratur und journalistische Berichte.
>
> Das bisherige Feedback ist eine wichtige Grundlage für die Überarbeitung, aber nicht automatisch in jedem Punkt richtig.
>
> Prüfe jede Kritik anhand der tatsächlich vorhandenen Materialien.
>
> Wenn eine Kritik berechtigt ist, korrigiere sie.
>
> Wenn eine Kritik nur teilweise zutrifft, berücksichtige die Einschränkung.
>
> Wenn eine Kritik nicht durch die vorhandenen Informationen bestätigt werden kann, übernimm sie nicht unkritisch.
>
> Strenge Regel gegen erfundene Informationen
>
> Du darfst unter keinen Umständen:
>
> * Quellen erfinden.
> * Zahlen oder Statistiken ergänzen, die nicht nachweisbar sind.
> * Interviewantworten erfinden.
> * Fehlende Interviewfragen nachträglich als beantwortet darstellen.
> * Gespräche, Treffen oder Entscheidungen erfinden.
> * Arbeitsprozesse rückwirkend verändern.
> * Behaupten, wir hätten etwas selbst überprüft, wenn dies nicht geschehen ist.
> * Fehlende Angaben durch plausible Vermutungen ersetzen.
>
> Wenn eine Information fehlt, kennzeichne sie als offen.
>
> Wenn eine Angabe überprüft werden muss, suche sie in den vorhandenen Projektmaterialien.
>
> Falls externe Recherche notwendig ist, verwende möglichst Originalquellen und dokumentiere genau, welche Informationen von extern stammen.
>
> Unterscheide immer zwischen:
>
> * nachgewiesenen Fakten,
> * plausiblen Interpretationen,
> * eigenen Schlussfolgerungen,
> * offenen Fragen.
>
> ⸻
>
> 3. Besonders wichtig: Unsere persönliche Schreibstimme erhalten
>
> Dieser Punkt hat höchste Priorität.
>
> Der Kommentar wurde von uns als Schülerinnen beziehungsweise Schüler einer Schweizer Kantonsschule geschrieben. Er soll sprachlich sehr gut sein, aber weiterhin wie eine eigenständige Maturaarbeit wirken.
>
> Orientiere dich an unserer tatsächlichen Schreibweise im bestehenden Kommentar und in unseren früheren Texten.
>
> Merkmale unserer Schreibstimme
>
> * Natürliches, verständliches Deutsch.
> * Direkte und klare Formulierungen.
> * Keine unnötig komplizierten Satzkonstruktionen.
> * Fachbegriffe nur dort, wo sie wirklich notwendig sind.
> * Wissenschaftliche Präzision ohne künstliche Akademisierung.
> * Eigene Gedanken und persönliche Reflexionen dürfen sichtbar bleiben.
> * Kritische Aussagen sollen konkret und nachvollziehbar sein.
> * Der Text soll nicht übermässig glatt oder perfekt wirken.
> * Unterschiedliche Satzlängen und natürliche Übergänge beibehalten.
> * Die persönliche Perspektive darf dort erhalten bleiben, wo sie in einem wissenschaftlichen Kommentar sinnvoll ist.
>
> Was du unbedingt vermeiden musst
>
> Schreibe nicht in einer typischen KI-Sprache.
>
> Vermeide insbesondere:
>
> * Künstlich akademische Formulierungen.
> * Unnötige Fachbegriffe.
> * Übertriebene Abstraktion.
> * Immer gleich aufgebaute Absätze.
> * Wiederholte Dreierschemata.
> * Ständige Formulierungen wie «Dies verdeutlicht, dass …».
> * Künstliche Überleitungen.
> * Übermässig perfekte Zusammenfassungen am Ende jedes Abschnitts.
> * Allgemeine Aussagen, die intelligent klingen, aber wenig aussagen.
> * Übertriebene Selbstreflexion.
> * Unnötige Wiederholungen derselben Erkenntnis in mehreren Kapiteln.
>
> Ein Beispiel für die gewünschte Sprache sind Formulierungen wie:
>
> «Beim ersten Lesen waren wir enttäuscht. Beim zweiten Lesen mussten wir zugeben, dass die meisten Punkte stimmen.»
>
> Oder:
>
> «Eine These, die nach der Prüfung genauer ist als vorher, zeigt, dass wir geprüft haben und nicht nur Belege für eine fertige Meinung gesammelt haben.»
>
> Solche Formulierungen sind konkret, persönlich und verständlich.
>
> Verbessere sprachliche Schwächen, aber entferne nicht die Eigenschaften, die unseren Text eigenständig machen.
>
> Wichtig bei jeder Überarbeitung
>
> Verändere einen Absatz nicht nur deshalb, weil du ihn stilistisch anders schreiben würdest.
>
> Wenn eine Passage bereits gut funktioniert, lass sie möglichst unverändert.
>
> Überarbeite gezielt dort, wo:
>
> * ein wissenschaftlicher Fehler vorliegt,
> * eine Aussage unklar ist,
> * eine Argumentation nicht funktioniert,
> * eine Wiederholung unnötig ist,
> * eine Formulierung sprachlich tatsächlich schwach ist,
> * eine wichtige Information fehlt.
>
> ⸻
>
> 4. Das konkrete wissenschaftliche Feedback vollständig umsetzen
>
> Die folgende Kritik muss systematisch abgearbeitet werden.
>
> A. Weltmarktanteil und Exportzahlen
>
> Im bisherigen Kommentar werden folgende Zahlen miteinander verglichen:
>
> * Geschätzter weltweiter Ube-Markt 2024: 455,3 Millionen US-Dollar.
> * Philippinische Ube-Exporte 2025: 3,06 Millionen US-Dollar.
> * Daraus errechneter Anteil: ungefähr 0,7 Prozent.
>
> Die mathematische Rechnung ist grundsätzlich nachvollziehbar.
>
> Das wissenschaftliche Problem liegt im Vergleich selbst.
>
> Ein nationaler Exportwert ist nicht automatisch mit dem gesamten weltweiten Marktvolumen vergleichbar.
>
> Der globale Markt kann beispielsweise auch verarbeitete Produkte, verschiedene Handelsstufen und den Binnenmarkt umfassen.
>
> Deine Aufgabe
>
> 1. Überprüfe beide Zahlen anhand der Originalquellen.
> 2. Prüfe, wie der globale Marktwert definiert wird.
> 3. Prüfe, welche Produkte in den philippinischen Exportzahlen enthalten sind.
> 4. Überprüfe, ob die beiden Grössen tatsächlich vergleichbar sind.
> 5. Entscheide, ob die Prozentrechnung beibehalten werden kann.
> 6. Formuliere die Interpretation wissenschaftlich korrekt.
>
> Wenn die Zahlen nicht direkt vergleichbar sind, darf die Rechnung höchstens als grobe Grössenordnung dargestellt werden.
>
> Insbesondere darf aus den 0,7 Prozent nicht automatisch geschlossen werden, dass der gesamte restliche Gewinn im Ausland entsteht.
>
> Diese Schlussfolgerung muss durch zusätzliche Quellen zur Verarbeitung, Wertschöpfung, Vermarktung und Gewinnverteilung gestützt werden.
>
> Das wirtschaftliche Argument soll erhalten bleiben, aber auf einer wissenschaftlich tragfähigen Grundlage stehen.
>
> B. Zeitliche Gegenüberstellung von Nachfrage und Ernte
>
> Im bisherigen Kapitel 7.1 wird geschrieben:
>
> «Auf den Philippinen ist die Ernte im selben Zeitraum gesunken …»
>
> Das ist zeitlich ungenau.
>
> Die Nachfrageentwicklung bezieht sich auf die jüngeren Jahre beziehungsweise die letzten vier Jahre.
>
> Die langfristige Entwicklung der philippinischen Ernte betrachtet dagegen einen deutlich längeren Zeitraum von 2010 bis 2025.
>
> Ausserdem begann der Rückgang der Ernte bereits vor dem internationalen Ube-Boom.
>
> Deine Aufgabe
>
> * Überprüfe sämtliche Zeitangaben.
> * Korrigiere die Formulierung «im selben Zeitraum».
> * Stelle klar dar, dass die internationale Nachfrage in den letzten Jahren gestiegen ist, während die philippinische Ernte langfristig zurückgegangen ist.
> * Vermeide eine zeitliche Gleichsetzung unterschiedlicher Untersuchungszeiträume.
> * Erhalte die Erkenntnis, dass der Ernte­rückgang nicht einfach durch den internationalen Boom erklärt werden kann.
>
> C. Kausalität und die Leitthese
>
> Die Formulierung:
>
> «Je gefragter die Knolle, desto knapper wird sie dort, wo sie herkommt.»
>
> ist einprägsam, suggeriert aber einen direkten Ursache-Wirkungs-Zusammenhang.
>
> Unsere Daten zeigen steigende internationale Nachfrage und eine langfristig sinkende philippinische Ernte.
>
> Sie beweisen nicht automatisch, dass die internationale Nachfrage den Rückgang der Ernte verursacht hat.
>
> Deine Aufgabe
>
> Prüfe sämtliche kausalen Aussagen im gesamten Kommentar.
>
> Achte besonders auf Formulierungen wie:
>
> * «führt dazu, dass»
> * «verursacht»
> * «deshalb»
> * «dadurch»
> * «als Folge»
> * «je mehr, desto weniger»
>
> Unterscheide konsequent zwischen Korrelation und Kausalität.
>
> Formuliere Aussagen vorsichtiger, wenn die Quellen keinen direkten Zusammenhang beweisen.
>
> Die Argumentation soll dadurch nicht schwächer werden. Sie soll wissenschaftlich belastbarer werden.
>
> D. Kulturelle Kontrolle genauer definieren
>
> Im bisherigen Kapitel 7.2 steht:
>
> «Keine davon liegt bei den Menschen, die Ube anbauen.»
>
> Diese Aussage ist zu absolut.
>
> Unser eigenes Interview mit Tita zeigt, dass sie Ube durchaus eine eigene kulturelle Bedeutung zuschreibt und sich über die internationale Bekanntheit freut.
>
> Sie hat also eine persönliche kulturelle Beziehung zu Ube und eine eigene Vorstellung davon, was die Knolle bedeutet.
>
> Das eigentliche Argument ist ein anderes:
>
> Bauern haben möglicherweise weniger Einfluss darauf, wie Ube international vermarktet, dargestellt und kulturell interpretiert wird als Unternehmen, Medien oder andere Institutionen.
>
> Deine Aufgabe
>
> Unterscheide klar zwischen:
>
> 1. Persönlicher kultureller Bedeutung: Wie Menschen auf den Philippinen Ube verstehen, verwenden und mit ihrer eigenen Identität verbinden.
> 2. Internationaler Darstellung: Wer bestimmt, wie Ube im Ausland präsentiert, vermarktet und interpretiert wird.
> 3. Wirtschaftlicher Kontrolle: Wer Verarbeitung, Vertrieb, Preise und Wertschöpfung beeinflusst.
>
> Vermeide absolute Aussagen über die fehlende Kontrolle der Bauern.
>
> Zeige stattdessen, wo ihre Einflussmöglichkeiten begrenzt sind und wo sie weiterhin eigene Deutungsmacht besitzen.
>
> Diese Unterscheidung muss sich konsequent durch Kapitel 7 ziehen.
>
> E. Das Interview mit Tita methodisch sauber darstellen
>
> Das Interview ist eine wichtige eigenständige Quelle unserer Arbeit.
>
> Besonders wichtig ist, dass wir Tita nicht als repräsentative Stimme aller Ube-Bauern darstellen.
>
> Ihre Aussagen sollen als individuelle Perspektive verwendet werden.
>
> Ein weiterer offener Punkt betrifft den Preisvergleich:
>
> * Titas Verkaufspreis: 150 Pesos pro Kilogramm.
> * Andere Berichte nennen Preise von 80 bis 100 Pesos, die Bauern beim Verkauf an Händler erhalten.
>
> Es ist plausibel, dass hier unterschiedliche Handelsstufen verglichen werden.
>
> Das ist jedoch nicht abschliessend bewiesen.
>
> Deine Aufgabe
>
> * Überprüfe die Preisangaben anhand der Quellen.
> * Erkläre den möglichen Unterschied zwischen Verkauf an Händler und Verkauf auf dem öffentlichen Markt.
> * Stelle die Erklärung ausdrücklich als plausible Interpretation dar, wenn sie nicht belegt ist.
> * Behaupte nicht, dass das Interview den Preisunterschied eindeutig erklärt.
> * Überprüfe, ob Titas Aussagen an allen Stellen korrekt wiedergegeben werden.
> * Bewahre die individuellen Aussagen und die Grenzen der Aussagekraft des Interviews.
>
> Zusätzlich müssen folgende Angaben ergänzt beziehungsweise überprüft werden:
>
> * Datum der Aufnahme beziehungsweise Durchführung.
> * Die zwei unbeantworteten Interviewfragen.
> * Das vollständige englische Originaltranskript.
> * Dokumentation der Bestätigung des Transkripts durch Tita, sofern tatsächlich vorhanden.
> * Angaben dazu, wie der Kontakt zustande kam.
> * Klärung, ob Tita ein Spitzname ist und ob der Name veröffentlicht werden darf, sofern diese Information noch offen ist.
> * Dokumentation, ob das Interview schriftlich, mündlich oder aufgezeichnet durchgeführt wurde.
>
> Erfinde keine dieser Angaben.
>
> Wenn etwas fehlt, kennzeichne es als offene Aufgabe.
>
> ⸻
>
> 5. Alle offenen Stellen im Dokument systematisch bearbeiten
>
> Die ursprüngliche Durchsicht hat folgende offenen Stellen identifiziert.
>
> Arbeite diese Liste vollständig ab.
>
> Stelle	Aufgabe
> Deckblatt	Klasse eintragen
> Abstract	Endgültigen Buchtitel einsetzen
> Kapitel 2.2	Abgabedatum des Zwischenkommentars prüfen
> Kapitel 2.3	Reisedaten überprüfen
> Kapitel 2.5	Treffen vom 14. September überprüfen
> Kapitel 3.2	Endgültigen Buchtitel und Buchbestandteile überprüfen
> Kapitel 3.3	Tatsächliche Zeilenlänge aus InDesign eintragen
> Kapitel 3.4	Beschreibung von Text und Bild mit dem fertigen Buch abgleichen
> Kapitel 4.3	Quellenverzeichnis und Zitierweise im Buch überprüfen; Absprache mit Betreuungsperson klären
> Kapitel 4.4	Farbwerte, Schriftgrössen, Bilddatenbank und Lizenzen ergänzen
> Kapitel 4.4	KI-generierte Bilder gegebenenfalls deklarieren
> Kapitel 4.5	Seitenzahl, Papier, Bindung und Anzahl Exemplare ergänzen
> Kapitel 5.1	Verantwortliche für die Kurzeinleitungen eintragen
> Kapitel 5.4	Rechnung zu den 300 Millionen Pesos nachvollziehen
> Kapitel 5.5	Zwei unbeantwortete Interviewfragen und Aufnahmedatum ergänzen
> Kapitel 5.5	Bestätigung des Transkripts durch Tita dokumentieren
> Kapitel 6.1	Seitenzahlen und Reihenfolge mit dem fertigen Buch abgleichen
> Kapitel 6.2	Vollständig ausfüllen und beide Abbildungen einfügen
> Kapitel 7.4	Entscheiden, ob die neue Formulierung der Leitthese übernommen wird
> Kapitel 7.5	Beide offenen Tabellenfelder ergänzen
> Kapitel 8.3	Konkret beschreiben, was nach der KI-Überarbeitung selbst geändert wurde
> Quellenverzeichnis	Fehlende URLs, Abrufdaten, Titel und bibliografische Angaben ergänzen
> Anhang A	Interviewfragen und englisches Transkript einfügen
> Anhang B	Entscheiden, ob der Master-Prompt abgedruckt werden soll
>
> Regeln für die Bearbeitung
>
> Gehe jeden Punkt einzeln durch.
>
> Suche zunächst nach der benötigten Information in den vorhandenen Materialien.
>
> Wenn sie vorhanden ist, ergänze sie direkt.
>
> Wenn sie nicht vorhanden ist, lasse keine erfundene Information einsetzen.
>
> Erstelle stattdessen eine übersichtliche Liste mit den Angaben, die noch von uns benötigt werden.
>
> Unterscheide zwischen:
>
> * Informationen, die du selbst aus den Materialien ergänzen kannst.
> * Informationen, die du durch Quellenprüfung ermitteln kannst.
> * Informationen, die ausschliesslich wir selbst bestätigen können.
>
> Versuche nicht, fehlende Informationen durch allgemeine Formulierungen zu kaschieren.
>
> ⸻
>
> 6. KI-Nachweis: Besonders sorgfältig überarbeiten
>
> Kapitel 10.6 muss besonders genau geprüft werden.
>
> Die bisherige Dokumentation beschreibt eine umfangreiche KI-Nutzung.
>
> Unter anderem wurde KI verwendet für:
>
> * Einen ersten Entwurf des gesamten Kommentars.
> * Sprachliche Überarbeitungen Satz für Satz.
> * Erstellung beziehungsweise Überarbeitung von Abbildungen.
> * Ausformulierung von Arbeitsjournaleinträgen.
> * Überprüfung von Fakten und Widersprüchen.
> * Eine weitere vollständige Überarbeitung mit Fable 5.1.
>
> Diese Nutzung muss transparent und vollständig dokumentiert werden.
>
> Problematische bisherige Formulierung
>
> «Danach haben wir die Texte gelesen, geprüft und in eigene Worte gebracht.»
>
> Diese Formulierung ist zu allgemein.
>
> Sie erklärt nicht, welchen tatsächlichen Eigenanteil wir geleistet haben.
>
> Deine Aufgabe
>
> Überprüfe die vorhandene KI-Dokumentation und beschreibe konkret:
>
> 1. Welche Teile durch KI erstellt wurden.
> 2. Welche Teile durch KI überarbeitet wurden.
> 3. Welche Quellen und Fakten wir selbst überprüft haben.
> 4. Welche inhaltlichen Entscheidungen wir selbst getroffen haben.
> 5. Welche KI-Vorschläge wir übernommen haben.
> 6. Welche KI-Vorschläge wir verworfen oder verändert haben.
> 7. Welche Passagen wir eigenständig neu geschrieben haben.
> 8. Wie wir die endgültige Fassung kontrolliert haben.
>
> Wichtig: Du darfst unseren Eigenanteil nicht grösser darstellen, als er tatsächlich war.
>
> Wenn sich eine konkrete Änderung nicht anhand der vorhandenen Entwürfe oder Dokumentation nachvollziehen lässt, behaupte nicht, dass wir sie selbst vorgenommen haben.
>
> Die Formulierung soll ehrlich, konkret und nachvollziehbar sein.
>
> Plattform und Modell unterscheiden
>
> Überprüfe ausserdem die Bezeichnung «Claude (Fable 5.1)».
>
> Plattform, Modell und verwendetes Tool müssen korrekt voneinander unterschieden werden.
>
> Übernimm keine Modellbezeichnung ungeprüft.
>
> Master-Prompt im Anhang
>
> Der bisherige Kommentar umfasst ungefähr 58 Seiten. Ein erheblicher Teil davon besteht aus dem vollständigen Master-Prompt, den wir für die KI verwendet haben.
>
> Prüfe, ob dieser Anhang für die schulische Abgabe tatsächlich erforderlich ist.
>
> Wenn er nicht verlangt wird, empfehle eine separate Dokumentation des Prompts und der KI-Nutzung.
>
> Entferne ihn jedoch nicht eigenmächtig aus dem Dokument, bevor die Entscheidung getroffen und die Konsequenzen überprüft wurden.
>
> ⸻
>
> 7. Weitere strukturelle und sprachliche Verbesserungen
>
> Neben den konkreten Kritikpunkten sollst du den gesamten Kommentar nochmals kritisch lesen.
>
> Kapitel 2 und 3
>
> Diese Kapitel beschreiben die Entstehung der Arbeit und die formale Sachbuchrecherche relativ ausführlich.
>
> Prüfe, ob einzelne Abschnitte unnötig lang sind oder sich wiederholen.
>
> Kürze nur dort, wo tatsächlich Informationen doppelt vorkommen oder für den wissenschaftlichen Kommentar wenig relevant sind.
>
> Die Entstehungsgeschichte und die Reflexion des Arbeitsprozesses sollen erhalten bleiben.
>
> Kapitel 7
>
> Kapitel 7 ist der argumentative Kern des Kommentars.
>
> Hier müssen die wichtigsten wissenschaftlichen Erkenntnisse zusammengeführt werden.
>
> Prüfe insbesondere:
>
> * Ist die Leitfrage klar beantwortet?
> * Werden wirtschaftliche und kulturelle Kontrolle sauber voneinander getrennt?
> * Sind die einzelnen Argumente ausreichend belegt?
> * Werden Gegenargumente ernst genommen?
> * Ist die Schlussfolgerung differenzierter als die ursprüngliche These?
> * Werden Erkenntnisse aus dem Interview sinnvoll integriert?
> * Gibt es Wiederholungen zwischen den Unterkapiteln?
> * Ist die Argumentation logisch aufgebaut?
>
> Kapitel 7 darf nicht durch unnötige Kürzungen an Tiefe verlieren.
>
> Schlussfolgerung
>
> Die ursprüngliche Leitthese lautet:
>
> «Die Philippinen verlieren beim Ube-Boom nicht ihre Kultur, sondern die Kontrolle über sie.»
>
> Die Arbeit zeigt allerdings, dass diese Aussage differenziert werden muss.
>
> Prüfe, ob eine neue Formulierung der Leitthese wissenschaftlich sinnvoller wäre.
>
> Die endgültige These muss:
>
> * Unsere ursprüngliche Fragestellung erkennbar beantworten.
> * Wirtschaftliche und kulturelle Aspekte berücksichtigen.
> * Die Grenzen unserer Daten berücksichtigen.
> * Keine unbelegten Kausalitäten enthalten.
> * Die tatsächlichen Erkenntnisse der Arbeit widerspiegeln.
>
> Behalte die ursprüngliche These nicht nur deshalb bei, weil sie gut klingt.
>
> Ändere sie aber auch nicht unnötig.
>
> ⸻
>
> 8. Das Sachbuch und der Kommentar müssen übereinstimmen
>
> Der Kommentar darf keine falschen oder veralteten Angaben über das fertige Sachbuch enthalten.
>
> Vergleiche deshalb die relevanten Abschnitte direkt mit dem tatsächlichen Buch.
>
> Prüfe insbesondere:
>
> * Endgültiger Buchtitel.
> * Aufbau und Kapitelreihenfolge.
> * Inhalt der einzelnen Kapitel.
> * Verwendete Bilder.
> * Bildnachweise und Bildlizenzen.
> * Layout und Gestaltung.
> * Quellenverzeichnis.
> * Seitenzahlen.
> * Umfang.
> * Tatsächliche Gestaltung und Formatierung.
>
> Der Kommentar beschreibt das fertige Produkt und nicht einen früheren Planungsstand.
>
> Wenn sich etwas während der Produktion verändert hat, muss der Kommentar diese Entwicklung korrekt widerspiegeln.
>
> ⸻
>
> 9. Arbeitsweise: Schritt für Schritt statt oberflächlicher Gesamtüberarbeitung
>
> Arbeite systematisch.
>
> Versuche nicht, den gesamten Kommentar in einem einzigen unkontrollierten Schreibdurchgang zu verändern.
>
> Gehe in dieser Reihenfolge vor:
>
> Phase 1: Bestandsaufnahme
>
> * Alle relevanten Projektmaterialien finden.
> * Aktuellen Kommentar identifizieren.
> * Versionen unterscheiden.
> * Vorhandene Quellen und Anhänge prüfen.
> * Offene Stellen identifizieren.
> * Einen Überblick über die Kapitelstruktur erstellen.
>
> Erstelle intern eine Übersicht über die wichtigsten Probleme.
>
> Beginne noch nicht mit einer vollständigen Neufassung.
>
> Phase 2: Wissenschaftliche Überprüfung
>
> Prüfe die Argumentation des gesamten Kommentars.
>
> Kontrolliere insbesondere die fünf wissenschaftlichen Problemfelder aus Kapitel 4.
>
> Überprüfe Zahlen, Zeiträume, Berechnungen, Kausalitäten und methodische Aussagen.
>
> Erstelle eine interne Liste mit allen notwendigen inhaltlichen Änderungen.
>
> Phase 3: Inhaltliche Überarbeitung
>
> Überarbeite die betroffenen Kapitel.
>
> Stelle sicher, dass:
>
> * Die Argumentation wissenschaftlich korrekt ist.
> * Alle Änderungen mit den Quellen übereinstimmen.
> * Die Leitthese und Schlussfolgerung zusammenpassen.
> * Interviewaussagen korrekt verwendet werden.
> * Keine Widersprüche zwischen den Kapiteln entstehen.
>
> Phase 4: Offene Stellen und formale Fertigstellung
>
> Bearbeite die gesamte Checkliste aus Kapitel 5.
>
> Ergänze alle Informationen, die in den vorhandenen Materialien nachweisbar sind.
>
> Dokumentiere alle fehlenden Informationen.
>
> Überprüfe das Quellenverzeichnis und die Anhänge.
>
> Phase 5: Sprachliche Überarbeitung
>
> Lies den gesamten Kommentar nochmals als zusammenhängenden Text.
>
> Verbessere:
>
> * Rechtschreibung.
> * Grammatik.
> * Zeichensetzung.
> * Satzbau.
> * Unklare Formulierungen.
> * Unnötige Wiederholungen.
> * Schlechte Übergänge.
>
> Bewahre dabei konsequent unsere persönliche Schreibstimme.
>
> Verwende Schweizer Rechtschreibung, insbesondere «ss» statt «ß».
>
> Phase 6: Abschliessende Qualitätskontrolle
>
> Lies den vollständig überarbeiteten Kommentar nochmals kritisch.
>
> Stelle dir dabei folgende Fragen:
>
> * Würde eine anspruchsvolle Betreuungsperson die Argumentation akzeptieren?
> * Sind alle wichtigen Aussagen belegt?
> * Sind die methodischen Einschränkungen transparent?
> * Stimmen Buch und Kommentar überein?
> * Ist der KI-Einsatz ehrlich dokumentiert?
> * Sind alle Platzhalter beseitigt?
> * Ist der Text sprachlich natürlich?
> * Gibt es noch Aussagen, die besser klingen, als sie wissenschaftlich tatsächlich sind?
>
> Erst nach dieser Kontrolle darfst du die Arbeit als fertig bezeichnen.
>
> ⸻
>
> 10. KRITISCH: Zeitmanagement, Kontingentgrenzen und automatische Sicherung
>
> Du darfst deine Arbeit nicht einfach abbrechen, weil dein Nachrichten- oder Nutzungskontingent bald erreicht ist.
>
> Ich möchte nicht nach einem Reset wieder von vorne beginnen müssen.
>
> Du musst deshalb von Anfang an mit einem integrierten Sicherungs- und Wiederaufnahmeverfahren arbeiten.
>
> A. Regelmässige Zwischensicherungen
>
> Nach jeder abgeschlossenen Phase und nach jeder grösseren Kapitelüberarbeitung:
>
> 1. Speichere die aktuelle Arbeitsfassung.
> 2. Aktualisiere den Bearbeitungsstatus.
> 3. Dokumentiere abgeschlossene Änderungen.
> 4. Dokumentiere noch offene Aufgaben.
> 5. Halte fest, welche Quellen bereits überprüft wurden.
> 6. Halte fest, welche Entscheidungen bereits getroffen wurden.
> 7. Notiere den nächsten konkreten Arbeitsschritt.
>
> Verlasse dich nicht darauf, dass der bisherige Chatverlauf nach einem Reset vollständig verfügbar ist.
>
> B. Dauerhafte Fortschrittsdatei
>
> Lege im Projektordner eine Datei mit dem Namen:
>
> FORTSCHRITT_KOMMENTAR.md
>
> an.
>
> Diese Datei muss jederzeit den tatsächlichen Stand der Arbeit wiedergeben.
>
> Sie enthält:
>
> * Aktuelle Version des Kommentars.
> * Zuletzt vollständig bearbeitetes Kapitel.
> * Abgeschlossene Phasen.
> * Bereits behobene Kritikpunkte.
> * Noch offene Kritikpunkte.
> * Noch fehlende Informationen.
> * Überprüfte Quellen.
> * Noch nicht überprüfte Quellen.
> * Getroffene inhaltliche Entscheidungen.
> * Nächsten Arbeitsschritt.
> * Hinweise zur persönlichen Schreibstimme.
> * Hinweise zur Fortsetzung nach einem Kontext- oder Kontingentreset.
>
> Aktualisiere diese Datei regelmässig und nicht erst am Ende.
>
> C. Sicherheitskopien
>
> Verändere niemals die einzige Originalfassung.
>
> Arbeite mit getrennten Versionen:
>
> * Originalentwurf.
> * Aktuelle Arbeitsfassung.
> * Gesicherte Zwischenversionen.
> * Endgültige Abgabefassung.
>
> Überschreibe keine wichtigen Originalmaterialien.
>
> D. Verhalten bei drohendem Kontingentlimit
>
> Wenn du bemerkst, dass dein verfügbares Kontingent oder dein Kontextfenster knapp wird:
>
> 1. Unterbrich die inhaltliche Arbeit kontrolliert.
> 2. Speichere zuerst den aktuellen Stand.
> 3. Aktualisiere FORTSCHRITT_KOMMENTAR.md.
> 4. Stelle sicher, dass die zuletzt bearbeiteten Kapitel vollständig gespeichert sind.
> 5. Schreibe eine konkrete Fortsetzungsanweisung für die nächste Sitzung.
> 6. Gib mir eine kurze Mitteilung, welche Arbeiten abgeschlossen wurden und wo fortgesetzt werden muss.
>
> Du darfst nicht einfach mitten in einer Kapitelüberarbeitung aufhören, ohne den aktuellen Stand zu sichern.
>
> E. Fortsetzung nach einem Reset
>
> Wenn eine neue Sitzung gestartet wird, lies zuerst:
>
> 1. FORTSCHRITT_KOMMENTAR.md.
> 2. Die aktuelle Arbeitsfassung.
> 3. Die relevanten Projektmaterialien.
>
> Prüfe, welche Änderungen bereits gespeichert wurden.
>
> Beginne anschliessend exakt an der dokumentierten Stelle.
>
> Wiederhole keine bereits abgeschlossenen Arbeiten, ausser eine erneute Kontrolle ist tatsächlich notwendig.
>
> Du sollst nicht darauf warten, dass ich dir nochmals den gesamten Auftrag erkläre.
>
> F. Keine vorzeitige Fertigstellung
>
> Ein Kontingentlimit ist kein Grund, die Aufgabe als abgeschlossen zu deklarieren.
>
> Wenn die Arbeit nicht vollständig erledigt werden kann, muss der genaue Zwischenstand gesichert werden.
>
> Der Auftrag gilt erst als abgeschlossen, wenn die gesamte Qualitätskontrolle durchgeführt wurde und eine vollständige Endfassung vorliegt.
>
> ⸻
>
> 11. Umgang mit Unsicherheiten und fehlenden Informationen
>
> Wenn du auf eine Information stösst, die du nicht zuverlässig feststellen kannst, gehe folgendermassen vor:
>
> 1. Suche in den vorhandenen Projektdateien.
> 2. Suche in den Originalquellen.
> 3. Prüfe, ob eine andere Stelle im Kommentar dieselbe Information enthält.
> 4. Prüfe, ob die Information durch eine andere Quelle bestätigt werden kann.
> 5. Wenn sie weiterhin fehlt, kennzeichne sie als offen.
>
> Frage mich nur dann nach einer Information, wenn sie tatsächlich notwendig ist und weder aus dem Vault noch aus den vorhandenen Quellen hervorgeht.
>
> Stelle nicht zehn Fragen auf einmal, wenn du einen grossen Teil der Arbeit bereits selbstständig erledigen kannst.
>
> Fasse notwendige Rückfragen möglichst nach abgeschlossenen Arbeitsphasen zusammen.
>
> ⸻
>
> 12. Anforderungen an das endgültige Ergebnis
>
> Am Ende erwarte ich folgende Ergebnisse:
>
> 1. Vollständig überarbeiteter Kommentar
>
> Eine vollständige, konsistente und sprachlich überarbeitete Endfassung.
>
> Die ursprüngliche Struktur soll grundsätzlich erhalten bleiben, sofern keine sachlichen Gründe für Änderungen sprechen.
>
> 2. Bereinigte wissenschaftliche Argumentation
>
> Alle relevanten wissenschaftlichen Kritikpunkte müssen überprüft und entweder behoben oder nachvollziehbar als offene Einschränkungen dokumentiert sein.
>
> 3. Vollständige KI-Dokumentation
>
> Kapitel 10.6 muss den tatsächlichen KI-Einsatz transparent darstellen.
>
> 4. Bereinigte Anhänge und Quellen
>
> Interviewtranskript, Abbildungen, Quellenangaben und weitere erforderliche Anhänge müssen kontrolliert werden.
>
> 5. Offene-Punkte-Liste
>
> Erstelle am Ende eine separate Liste aller Angaben, die du nicht selbstständig vervollständigen konntest und die noch von uns bestätigt oder ergänzt werden müssen.
>
> 6. Änderungsprotokoll
>
> Erstelle eine übersichtliche Dokumentation mit:
>
> * Kapitel.
> * Ursprüngliches Problem.
> * Durchgeführte Änderung.
> * Wissenschaftliche oder sprachliche Begründung.
>
> Dokumentiere besonders grössere inhaltliche Änderungen.
>
> 7. Abschliessende Bewertung
>
> Bewerte den fertigen Kommentar kritisch anhand folgender Kriterien:
>
> * Wissenschaftliche Korrektheit.
> * Qualität der Argumentation.
> * Methodische Sauberkeit.
> * Quellenarbeit.
> * Reflexion des Arbeitsprozesses.
> * Sprachliche Qualität.
> * Authentizität der Schreibstimme.
> * Formale Vollständigkeit.
>
> Unterscheide zwischen vollständig erfüllten Anforderungen und Punkten, die noch von uns abhängen.
>
> Behaupte nicht, dass der Kommentar abgabefertig ist, wenn noch zwingende offene Punkte bestehen.
>
> ⸻
>
> 13. Übergeordnete Arbeitsprinzipien
>
> Diese Regeln gelten während des gesamten Auftrags:
>
> 1. Wissenschaftliche Genauigkeit ist wichtiger als eine besonders überzeugend klingende Formulierung.
> 2. Authentische Schreibstimme ist wichtiger als künstliche sprachliche Perfektion.
> 3. Bestehende gute Passagen sollen erhalten bleiben.
> 4. Kritik muss überprüft werden, nicht blind übernommen.
> 5. Keine erfundenen Informationen.
> 6. Keine unbelegten Kausalitäten.
> 7. Keine künstliche Aufwertung unseres Eigenanteils.
> 8. Keine unnötigen Änderungen an bereits funktionierenden Abschnitten.
> 9. Alle wichtigen Änderungen müssen nachvollziehbar sein.
> 10. Die Originalfassung muss erhalten bleiben.
> 11. Der Fortschritt muss regelmässig gesichert werden.
> 12. Die Aufgabe darf nicht wegen eines Kontingentlimits unkontrolliert abgebrochen werden.
>
> ABSCHLIESSENDE ANWEISUNG
>
> Beginne jetzt mit Phase 1.
>
> Prüfe zunächst den gesamten verfügbaren Obsidian-Vault und identifiziere die aktuell gültige Version unseres wissenschaftlichen Kommentars sowie die dazugehörigen Projektmaterialien.
>
> Lies die vorhandenen Dokumente, bevor du inhaltliche Änderungen vornimmst.
>
> Erstelle anschliessend die Fortschrittsdatei und beginne mit der systematischen wissenschaftlichen Überprüfung.
>
> Arbeite eigenständig und gründlich.
>
> Ich möchte keine oberflächliche Korrektur, sondern eine tatsächliche Verbesserung der wissenschaftlichen Qualität des gesamten Kommentars.
>
> Das Ziel ist eine Maturaarbeit, die inhaltlich überzeugt, methodisch sauber ist und trotzdem eindeutig unsere eigene Arbeit und unsere persönliche Schreibstimme widerspiegelt.

### 4.3 Master-Prompt 3 (Eingabe 8, 9.11.2026, 08:39)

Datei im Chat: `0dfbe94c-attachment.txt`, 3273 Wörter. Im selben Chat-Beitrag hat Aezri das englische Transkript des Interviews eingefügt (zehn Fragen mit Antworten, Fragen 7 und 10 ohne Antwort). Sein Wortlaut steht in Anhang A des Kommentars und in [[Interview mit Tita]] und wird hier nicht wiederholt.

> FINALER KORREKTUR- UND QUALITÄTSSICHERUNGSPROMPT
>
> Schriftlicher Kommentar zur Maturaarbeit «Wem gehört der Ube-Boom?»
>
> 1. Deine Rolle und dein Auftrag
>
> Du bist ein äusserst sorgfältiger wissenschaftlicher Lektor, kritischer Gutachter und Korrektor auf Maturaarbeitsniveau.
>
> Deine Aufgabe ist es, meinen gesamten schriftlichen Kommentar zur Maturaarbeit ein letztes Mal vollständig zu überprüfen und zu korrigieren.
>
> Die aktuelle Fassung wurde bereits mehrfach überarbeitet. Trotzdem können noch Fehler, Ungenauigkeiten, Widersprüche, unklare Argumentationen, sprachliche Schwächen und formale Unvollständigkeiten vorhanden sein.
>
> Dies ist keine gewöhnliche Korrekturrunde. Es ist die abschliessende Qualitätssicherung vor der Abgabe.
>
> Dein Ziel ist ein vollständig korrigierter, wissenschaftlich sauberer, sprachlich überzeugender und formal möglichst abgabefertiger Kommentar, der weiterhin eindeutig meine persönliche Schreibsprache trägt.
>
> Du sollst nicht nur Fehler auflisten, sondern sie direkt im Dokument verbessern. Arbeite gründlich und selbstständig. Warte nicht nach jedem Kapitel auf meine Zustimmung.
>
> 2. ABSOLUTE PRIORITÄT: MEINE PERSÖNLICHE SCHREIBSTIMME BEWAHREN
>
> Dieser Punkt ist für die gesamte Überarbeitung besonders wichtig. Er gilt für jede einzelne sprachliche Änderung und darf während der gesamten Arbeit nicht in den Hintergrund geraten.
>
> Du korrigierst meinen Text, aber du ersetzt nicht meine persönliche Schreibweise durch deine eigene.
>
> Ich möchte am Ende einen wissenschaftlich korrekten und sprachlich sauberen Text haben, der sich trotzdem eindeutig nach mir anhört.
>
> Der Kommentar soll weiterhin wie mein eigener Text wirken und nicht wie ein von einer KI oder einem professionellen wissenschaftlichen Lektor neu verfasster Text.
>
> Was du unbedingt erhalten musst
>
> * Meine typische Wortwahl und meinen natürlichen Ausdruck.
> * Meine Art, Gedanken miteinander zu verbinden.
> * Meine Satzstruktur, sofern sie verständlich und grammatikalisch korrekt ist.
> * Meine persönliche Art, Argumente zu erklären und Schlussfolgerungen zu ziehen.
> * Meine eigene Perspektive und meine persönlichen Reflexionen.
> * Den Wechsel zwischen sachlicher Analyse und persönlicher Auseinandersetzung mit dem Thema.
> * Eine natürliche, direkte und verständliche Sprache.
> * Das sprachliche Niveau einer sehr guten Maturaarbeit, nicht das eines akademischen Fachartikels.
>
> Was du vermeiden musst
>
> * Formulierungen, die unnötig akademisch oder künstlich wirken.
> * Übermässig komplizierte Satzkonstruktionen.
> * Typische KI-Formulierungen und austauschbare Standardsätze.
> * Unnatürlich perfekte Übergänge zwischen allen Abschnitten.
> * Übertriebene Fachsprache, wenn ein einfacheres Wort denselben Inhalt korrekt ausdrückt.
> * Das Ersetzen meiner eigenen Formulierungen durch stilistisch elegantere Varianten, die aber nicht nach mir klingen.
> * Das Vereinheitlichen aller Sätze auf einen gleichförmigen, künstlich glatten Stil.
> * Das Entfernen von persönlichen Gedanken, Unsicherheiten oder Reflexionen, nur weil sie weniger akademisch klingen.
> * Das unnötige Umformulieren von bereits guten und natürlichen Sätzen.
>
> Verbindliche Regel für jede Änderung
>
> Bevor du einen Satz umformulierst, prüfe:
>
> 1. Ist der Satz tatsächlich falsch, unklar, unpräzise oder unnötig schwer verständlich?
> 2. Kann das Problem mit einer kleinen Änderung behoben werden?
> 3. Kann meine ursprüngliche Wortwahl und Satzstruktur weitgehend erhalten bleiben?
> 4. Klingt die neue Version noch so, als hätte ich sie selbst schreiben können?
>
> Wenn ein Satz bereits korrekt ist und natürlich klingt, lass ihn unverändert.
>
> Arbeite nach dem Prinzip: So wenig wie möglich verändern, so viel wie nötig verbessern.
>
> Bei wissenschaftlichen Fehlern hat die sachliche Korrektheit selbstverständlich Vorrang. Trotzdem sollst du die Korrektur möglichst nahe an meiner ursprünglichen Formulierung halten.
>
> Meine bisherigen Texte als Stilreferenz
>
> Nutze meine früheren eigenen Textfassungen, insbesondere die ursprünglichen und selbst verfassten Abschnitte des schriftlichen Kommentars, als Referenz für meine persönliche Schreibweise.
>
> Unterscheide dabei zwischen meinen ursprünglichen Formulierungen und bereits KI-generierten oder stark KI-überarbeiteten Passagen.
>
> Verwende nicht automatisch die sprachlich glatteste Version als Vorlage für meinen Stil.
>
> Wenn du dir bei einer Formulierung nicht sicher bist, entscheide dich eher für die natürlichere und einfachere Variante.
>
> Abschliessende Stilkontrolle
>
> Lies nach der gesamten Korrektur den Text nochmals ausschliesslich unter diesem Gesichtspunkt.
>
> Frage dich bei jedem Kapitel:
>
> * Klingt dieser Abschnitt noch nach derselben Person wie meine ursprünglichen Texte?
> * Wurde meine persönliche Ausdrucksweise unnötig verändert?
> * Gibt es Stellen, die plötzlich deutlich akademischer oder künstlicher klingen als der Rest?
> * Wurden meine persönlichen Reflexionen und meine eigene Argumentationsweise erhalten?
>
> Korrigiere solche stilistischen Ausreisser.
>
> Das Endergebnis muss wissenschaftlich besser sein als die ursprüngliche Fassung, aber weiterhin eindeutig meine persönliche Schreibstimme tragen.
>
> 3. Zuerst alle vorhandenen Materialien prüfen
>
> Bevor du Änderungen vornimmst, verschaffe dir einen vollständigen Überblick über die verfügbaren Projektmaterialien in meinem Obsidian-Vault und den bereitgestellten Dateien.
>
> Dazu gehören insbesondere:
>
> * die aktuellste Version des schriftlichen Kommentars
> * das fertige Ube-Buch beziehungsweise das eigentliche Produkt der Maturaarbeit
> * das Recherchedossier
> * verwendete wissenschaftliche Studien und externe Quellen
> * Statistiken und Datensammlungen
> * das Interview mit Tita
> * Berechnungen und eigene Auswertungen
> * Arbeitsjournal und Dokumentation des Arbeitsprozesses
> * frühere Textfassungen und relevante Überarbeitungen
> * KI-Protokolle und verwendete Prompts
> * Bilder, Bildquellen und Bildnachweise
> * vorhandene Literatur- und Quellenverzeichnisse
>
> Verwende grundsätzlich die aktuellste Version des Kommentars als Arbeitsgrundlage.
>
> Vergleiche den Kommentar mit den anderen Materialien. Prüfe insbesondere, ob die Aussagen im Kommentar tatsächlich mit dem fertigen Buch, den Quellen und dem dokumentierten Arbeitsprozess übereinstimmen.
>
> Erfinde keine Informationen, die in den vorhandenen Materialien nicht enthalten sind.
>
> Falls du mehrere Versionen findest, identifiziere zuerst die aktuellste Fassung.
>
> Überschreibe keine Originaldateien. Arbeite mit einer separaten korrigierten Version.
>
> 4. Vollständige Fehlersuche im gesamten Dokument
>
> Lies den gesamten Kommentar von Anfang bis Ende. Überspringe keine Kapitel, Unterkapitel, Fussnoten, Tabellen, Bildunterschriften, Anhänge oder Verzeichnisse.
>
> Prüfe jede einzelne Aussage auf folgende Fehlerarten:
>
> A. Inhaltliche Fehler
>
> * Falsche oder missverständliche Aussagen
> * Unbelegte Behauptungen
> * Ungenaue Begriffe
> * Fehlende Erklärungen
> * Unklare Zusammenhänge
> * Widersprüche zwischen verschiedenen Kapiteln
> * Wiederholungen, die keinen zusätzlichen Erkenntniswert bieten
> * Schlussfolgerungen, die nicht ausreichend durch die vorherigen Ausführungen gestützt werden
> * Aussagen, die über die vorhandenen Quellen hinausgehen
> * Unbeabsichtigte Verallgemeinerungen
> * Unklare Unterscheidungen zwischen Fakten, Interpretationen und persönlichen Einschätzungen
>
> Korrigiere alle eindeutig feststellbaren inhaltlichen Fehler.
>
> B. Wissenschaftliche Qualität
>
> Prüfe, ob der Kommentar den Anforderungen einer wissenschaftlichen Maturaarbeit entspricht.
>
> Achte insbesondere auf:
>
> * Nachvollziehbarkeit der Argumentation
> * Qualität und Aussagekraft der verwendeten Belege
> * korrekte Interpretation von Statistiken
> * sinnvolle Vergleiche zwischen Daten
> * korrekte zeitliche Einordnung
> * angemessene Einschränkung von Schlussfolgerungen
> * saubere Unterscheidung zwischen Korrelation und Kausalität
> * transparente Darstellung der Grenzen der eigenen Untersuchung
> * korrekte Verwendung wissenschaftlicher Begriffe
> * nachvollziehbare Herleitung der Ergebnisse
>
> Eine Aussage ist nicht automatisch korrekt, nur weil sie plausibel klingt.
>
> Prüfe, ob jede Schlussfolgerung tatsächlich aus den präsentierten Informationen folgt.
>
> C. Sprache und Stil
>
> Korrigiere den gesamten Text auf:
>
> * Rechtschreibung
> * Grammatik
> * Zeichensetzung
> * Satzbau
> * unnatürliche Formulierungen
> * unklare Bezüge
> * unnötig komplizierte Sätze
> * sprachliche Wiederholungen
> * unpassende Wortwahl
> * unpräzise Formulierungen
> * unnötige Füllwörter
> * uneinheitliche Schreibweisen
>
> Verbessere die Lesbarkeit, ohne den Text künstlich aufzuwerten.
>
> Verwende natürliches, klares Deutsch und Schweizer Rechtschreibung. Schreibe «ss» statt «ß».
>
> Verändere keine Formulierungen nur deshalb, weil du eine andere Variante bevorzugst. Ändere sie, wenn dadurch tatsächlich ein Fehler behoben oder die Aussage klarer, präziser oder verständlicher wird.
>
> 5. Bereits bekannte wissenschaftliche Problemstellen zwingend überprüfen
>
> Die folgenden Punkte wurden bei der vorherigen Bewertung ausdrücklich kritisiert. Sie müssen erneut im gesamten Dokument überprüft werden. Es reicht nicht, einzelne Sätze zu verändern. Kontrolliere auch, ob die entsprechenden Probleme an anderen Stellen wieder auftauchen.
>
> 5.1 Vergleich zwischen Welthandel und philippinischen Exporten
>
> Im bisherigen Kommentar wurde der geschätzte weltweite Ube-Markt von rund 455,3 Millionen US-Dollar im Jahr 2024 mit den philippinischen Ube-Exporten von rund 3,06 Millionen US-Dollar verglichen.
>
> Dieser Vergleich ist methodisch problematisch, weil Exportwert und geschätztes weltweites Marktvolumen nicht zwingend dieselben Produkte, Handelsstufen oder Märkte umfassen.
>
> Prüfe:
>
> * Werden diese Zahlen überhaupt sinnvoll miteinander verglichen?
> * Wird deutlich erklärt, dass die beiden Zahlen unterschiedliche Grössen abbilden können?
> * Wird vermieden, aus dem Verhältnis von ungefähr 0,7 Prozent unbegründete Schlussfolgerungen zu ziehen?
> * Wird nirgends behauptet, dass der gesamte restliche Wert zwangsläufig ausserhalb der Philippinen entsteht?
> * Ist die Aussage über die geringe Beteiligung der Philippinen an der internationalen Wertschöpfung durch die vorhandenen Daten tatsächlich gedeckt?
>
> Korrigiere die Argumentation so, dass nur das behauptet wird, was die Zahlen wirklich belegen.
>
> Falls ein Vergleich nicht ausreichend abgesichert werden kann, schränke ihn ein oder entferne ihn. Erfinde keine Ersatzdaten.
>
> 5.2 Unterschiedliche Zeiträume
>
> Die internationale Nachfrageentwicklung und der Rückgang der philippinischen Ube-Ernte wurden zuvor teilweise so dargestellt, als würden sie denselben Zeitraum betreffen.
>
> Prüfe alle entsprechenden Stellen.
>
> Der internationale Nachfrageanstieg der letzten Jahre darf nicht unmittelbar mit einem langfristigen Rückgang der philippinischen Ernte seit 2010 oder früher gleichgesetzt werden.
>
> Mache klar:
>
> * Seit wann ist der Rückgang der Ernte feststellbar?
> * Seit wann ist der internationale Ube-Boom dokumentiert?
> * Welche Entwicklungen sind zeitlich tatsächlich vergleichbar?
> * Welche Entwicklungen bestanden bereits vor dem internationalen Boom?
>
> Vermeide jede Formulierung, die einen direkten Zusammenhang suggeriert, wenn dieser nicht nachgewiesen ist.
>
> 5.3 Kausalität und Knappheit
>
> Die Aussage, dass die steigende internationale Nachfrage automatisch zu einer Knappheit auf den Philippinen führt, ist zu stark, wenn dafür keine ausreichenden Belege vorliegen.
>
> Unterscheide konsequent zwischen:
>
> * nachgewiesenen Entwicklungen
> * zeitlichen Zusammenhängen
> * möglichen Erklärungen
> * tatsächlichen Ursache-Wirkungs-Beziehungen
>
> Die Aussage von Tita, dass Ube auf ihrem Markt knapp sei, ist ein persönlicher Erfahrungsbericht und kein repräsentativer Beweis für eine landesweite Entwicklung.
>
> Stelle diese Information entsprechend dar.
>
> 5.4 Kulturelle Kontrolle
>
> Prüfe die Unterscheidung zwischen:
>
> 1. persönlicher kultureller Bedeutung von Ube für Menschen auf den Philippinen
> 2. internationaler Darstellung und Vermarktung von Ube
> 3. wirtschaftlicher Kontrolle über Verarbeitung, Wertschöpfung und Gewinne
>
> Vermeide absolute Aussagen wie, dass philippinische Bauern keinerlei Kontrolle über die kulturelle Bedeutung von Ube hätten.
>
> Die persönliche Bedeutung, die Menschen Ube geben, darf nicht mit der internationalen Vermarktung und wirtschaftlichen Kontrolle gleichgesetzt werden.
>
> Die Argumentation soll differenziert sein, ohne die ursprüngliche Leitthese unnötig abzuschwächen.
>
> 5.5 Interview mit Tita
>
> Prüfe sämtliche Aussagen, die sich auf das Interview mit Tita beziehen.
>
> Insbesondere:
>
> * Wird deutlich, dass es sich um ein einzelnes Interview handelt?
> * Werden ihre Aussagen nicht als repräsentativ für alle Ube-Bauern dargestellt?
> * Werden ihre persönlichen Beobachtungen von statistischen Daten getrennt?
> * Wird der Preis von 150 Pesos pro Kilogramm korrekt eingeordnet?
> * Wird der Vergleich mit den 80 bis 100 Pesos, die Bauern teilweise von Zwischenhändlern erhalten, nicht als direkter Vergleich gleicher Handelsstufen dargestellt, wenn das nicht belegt ist?
> * Wird deutlich, welche Aussagen direkt von Tita stammen und welche meine Interpretation sind?
>
> Prüfe auch, ob die Angaben zur Durchführung des Interviews vollständig sind.
>
> Erfinde keine Angaben zum Interviewdatum, zur Kontaktaufnahme, zur Aufzeichnung oder zur Zustimmung zur Veröffentlichung.
>
> Falls Informationen fehlen, markiere sie als offene Aufgabe.
>
> 6. Leitthese und Schlussfolgerungen überprüfen
>
> Die zentrale Fragestellung lautet:
>
> «Wem gehört der Ube-Boom?»
>
> Die ursprüngliche Leitthese lautet:
>
> «Die Philippinen verlieren beim Ube-Boom nicht ihre Kultur, sondern die Kontrolle über sie.»
>
> Im Verlauf der Überarbeitung wurde die wirtschaftliche Formulierung präzisiert, unter anderem mit der Aussage:
>
> «Die Philippinen gewinnen die Kontrolle über die Wertschöpfung ihrer eigenen Knolle bisher nicht.»
>
> Prüfe die gesamte Argumentation und entscheide, welche Formulierung den tatsächlichen Ergebnissen am besten entspricht.
>
> Achte darauf, dass die Leitthese:
>
> * durch die Untersuchung beantwortet wird
> * nicht mehr behauptet, als die Quellen zeigen
> * wirtschaftliche und kulturelle Aspekte angemessen berücksichtigt
> * im gesamten Kommentar einheitlich verwendet wird
> * im Schluss tatsächlich beantwortet wird
>
> Wenn eine Anpassung der Leitthese sinnvoll ist, nimm sie vor und passe alle davon abhängigen Stellen an.
>
> Behalte dabei die ursprüngliche Fragestellung und den Charakter der Arbeit bei.
>
> 7. Alle formalen Mängel und Platzhalter beseitigen
>
> Suche das gesamte Dokument systematisch nach:
>
> * eckigen Klammern
> * Platzhaltern
> * Kommentaren
> * provisorischen Formulierungen
> * fehlenden Bildnachweisen
> * unvollständigen Quellenangaben
> * fehlenden URLs
> * fehlenden Abrufdaten
> * offenen Tabellenfeldern
> * fehlenden Seitenzahlen
> * unvollständigen Bildunterschriften
> * nicht abgeschlossenen Abschnitten
> * Hinweisen wie «noch ergänzen», «prüfen» oder «Bild folgt»
>
> Beseitige alle Platzhalter, die sich anhand der vorhandenen Materialien eindeutig vervollständigen lassen.
>
> Erfinde keine Informationen, nur um eine Lücke zu schliessen.
>
> Wenn beispielsweise eine URL, ein Interviewdatum, eine Seitenzahl, eine Druckangabe oder eine persönliche Angabe fehlt, darfst du diese nicht schätzen.
>
> Erstelle stattdessen eine vollständige Liste mit allen Informationen, die ich noch selbst liefern muss.
>
> Achte auch auf die formale Einheitlichkeit:
>
> * Kapitelnummerierung
> * Überschriften
> * Tabellen
> * Bildunterschriften
> * Fussnoten
> * Quellenverzeichnis
> * Literaturverzeichnis
> * Anhänge
> * Seitenverweise
> * Abkürzungen
> * Datumsangaben
> * Währungsangaben
> * Einheiten
>
> Prüfe, ob alle Verweise im Text tatsächlich auf vorhandene Abbildungen, Tabellen oder Anhänge verweisen.
>
> 8. KI-Dokumentation besonders sorgfältig prüfen
>
> Das Kapitel zur Verwendung künstlicher Intelligenz muss transparent, vollständig und glaubwürdig sein.
>
> Es muss klar werden, wofür KI tatsächlich verwendet wurde und welche Eigenleistung von uns stammt.
>
> Berücksichtige die tatsächliche Nutzung:
>
> * Erstellung eines ersten vollständigen Textentwurfs
> * sprachliche Überarbeitung einzelner Sätze
> * Erstellung von Illustrationen
> * Unterstützung bei Journal-Einträgen
> * Überprüfung von Fakten und möglichen Widersprüchen
> * weitere Überarbeitung des Kommentars mit Claude Fable 5.1
>
> Prüfe, ob diese Tätigkeiten im Dokument korrekt und ausreichend differenziert beschrieben werden.
>
> Unterscheide zwischen:
>
> * KI-generierten Inhalten
> * KI-unterstützten Überarbeitungen
> * selbst recherchierten und überprüften Informationen
> * eigenen Analysen und Schlussfolgerungen
> * selbst verfassten oder substanziell überarbeiteten Textteilen
>
> Die Formulierung, dass wir KI-Texte «gelesen, geprüft und in eigene Worte gefasst» hätten, reicht nicht aus, wenn sie den tatsächlichen Arbeitsprozess nicht präzise beschreibt.
>
> Beschreibe keine Eigenleistung, die nicht stattgefunden hat. Verschweige auch keine relevante KI-Nutzung.
>
> Überprüfe ausserdem, ob die verwendeten KI-Systeme und Modellbezeichnungen korrekt angegeben sind.
>
> Falls die Dokumentation noch persönliche Angaben von mir benötigt, markiere diese konkret.
>
> 9. Vergleich mit dem eigentlichen Ube-Buch
>
> Der schriftliche Kommentar muss zum fertigen Produkt passen.
>
> Vergleiche deshalb alle relevanten Aussagen mit dem tatsächlichen Buch.
>
> Prüfe insbesondere:
>
> * Stimmen die beschriebenen Kapitel mit dem fertigen Buch überein?
> * Werden Inhalte erwähnt, die im Buch gar nicht vorkommen?
> * Werden wichtige Bestandteile des Produkts ausgelassen?
> * Stimmen die beschriebenen gestalterischen Entscheidungen mit dem tatsächlichen Ergebnis überein?
> * Sind die Aussagen zur Entwicklung des Produkts korrekt?
> * Werden Entscheidungen und Änderungen im Arbeitsprozess nachvollziehbar erklärt?
> * Stimmen Angaben zu Bildern, Gestaltung, Umfang und Aufbau?
>
> Der Kommentar darf nicht so tun, als sei etwas umgesetzt worden, wenn es im fertigen Produkt nicht vorkommt.
>
> 10. Quellen und Fakten überprüfen
>
> Kontrolliere jede Quellenangabe und jeden faktischen Beleg.
>
> Prüfe:
>
> * Ist die Quelle tatsächlich vorhanden?
> * Unterstützt sie die Aussage, für die sie verwendet wird?
> * Wurde die Quelle korrekt interpretiert?
> * Stimmen Zahlen, Jahreszahlen und Einheiten?
> * Sind Quellenangaben im Text und im Literaturverzeichnis konsistent?
> * Sind direkte Zitate korrekt gekennzeichnet?
> * Sind indirekte Übernahmen ausreichend belegt?
> * Gibt es Aussagen ohne notwendige Quellenangabe?
> * Werden unterschiedliche Quellenarten angemessen behandelt?
>
> Nutze zuerst die bereits vorhandenen Quellen und Projektmaterialien.
>
> Wenn du externe Quellen zur Verifikation verwendest, kennzeichne diese klar und dokumentiere sie vollständig. Verändere nicht stillschweigend die Quellenbasis der Arbeit.
>
> Wenn eine Quelle nicht zugänglich oder nicht eindeutig überprüfbar ist, sage das ausdrücklich. Behaupte nicht, etwas verifiziert zu haben, wenn du es nicht konntest.
>
> 11. Keine unnötige Neuschreibung
>
> Es ist ausdrücklich nicht dein Ziel, den gesamten Kommentar neu zu schreiben.
>
> Die bestehende Struktur und die persönliche Schreibstimme sollen erhalten bleiben.
>
> Du sollst:
>
> * Fehler direkt korrigieren
> * unklare Argumente präzisieren
> * wissenschaftlich problematische Aussagen verbessern
> * unnötige Wiederholungen reduzieren
> * fehlende Übergänge ergänzen, wenn sie notwendig sind
> * schwache Schlussfolgerungen verbessern
> * formale Unvollständigkeiten beheben
>
> Du sollst nicht:
>
> * ganze Kapitel ohne Notwendigkeit neu formulieren
> * den Text künstlich akademischer machen
> * neue Argumente erfinden
> * die ursprüngliche Aussageabsicht verändern
> * persönliche Reflexionen durch generische Formulierungen ersetzen
> * meinen individuellen Schreibstil entfernen
> * korrekte Sätze nur aus stilistischen Gründen umformulieren
>
> Jede grössere inhaltliche Änderung muss nachvollziehbar sein.
>
> 12. Arbeitsweise und Zeitmanagement
>
> Arbeite selbstständig und in mehreren systematischen Durchgängen.
>
> Durchgang 1: Vollständige Bestandsaufnahme
>
> Lies das gesamte Dokument und erstelle intern eine Liste aller gefundenen Probleme.
>
> Durchgang 2: Inhaltliche und wissenschaftliche Korrektur
>
> Überarbeite alle problematischen Aussagen, Argumentationen, Datenvergleiche und Schlussfolgerungen.
>
> Durchgang 3: Sprachliche Korrektur
>
> Korrigiere das gesamte Dokument sprachlich und grammatikalisch. Bewahre dabei konsequent meine persönliche Schreibstimme.
>
> Durchgang 4: Formale Vervollständigung
>
> Bearbeite Quellen, Verweise, Tabellen, Bildnachweise, Platzhalter, Anhänge und Formatierung.
>
> Durchgang 5: Abgleich mit den Projektmaterialien
>
> Kontrolliere, ob der Kommentar mit dem fertigen Buch, den Quellen, dem Interview und dem tatsächlichen Arbeitsprozess übereinstimmt.
>
> Durchgang 6: Abschliessende Kontrolle
>
> Lies die vollständig korrigierte Fassung nochmals von Anfang bis Ende. Suche gezielt nach Fehlern, die bei den vorherigen Durchgängen übersehen worden sein könnten.
>
> Durchgang 7: Persönliche Stilkontrolle
>
> Prüfe nochmals, ob die persönliche Schreibstimme erhalten geblieben ist.
>
> Ein Fehler gilt erst dann als behoben, wenn du die korrigierte Stelle nochmals überprüft hast.
>
> Arbeite nicht nur so lange, bis eine erste verbesserte Fassung vorliegt. Die abschliessende Kontrolle ist ein zwingender Bestandteil des Auftrags.
>
> Schutz vor Abbruch durch Kontext- oder Nutzungslimits
>
> Falls du wegen eines Kontextlimits, einer Nutzungsgrenze oder aus einem anderen Grund nicht alles in einer Sitzung bearbeiten kannst:
>
> 1. Speichere den aktuellen Bearbeitungsstand regelmässig.
> 2. Erstelle oder aktualisiere eine Datei namens FORTSCHRITT_FINALKORREKTUR.md.
> 3. Dokumentiere darin, welche Kapitel vollständig geprüft wurden.
> 4. Halte alle noch offenen Fehler und Aufgaben fest.
> 5. Vermerke, welche Änderungen bereits vorgenommen wurden.
> 6. Notiere genau, an welcher Stelle die Arbeit fortgesetzt werden muss.
> 7. Beginne bei einer Fortsetzung zuerst mit dem Lesen dieser Fortschrittsdatei und der aktuellsten Dokumentversion.
>
> Beende die Arbeit niemals kommentarlos mit einer unfertigen Version.
>
> Falls nicht alle Kapitel bearbeitet werden können, sage ausdrücklich, welche Teile noch nicht geprüft wurden. Behaupte niemals, das gesamte Dokument sei fertig, wenn das nicht stimmt.
>
> 13. Umgang mit fehlenden Informationen
>
> Unterscheide konsequent zwischen drei Kategorien:
>
> Kategorie 1: Selbstständig korrigierbar
>
> Der Fehler ist anhand der vorhandenen Quellen oder Projektmaterialien eindeutig feststellbar. Korrigiere ihn direkt.
>
> Kategorie 2: Mit vorhandenen Materialien ergänzbar
>
> Die benötigte Information existiert bereits im Vault oder in den bereitgestellten Dateien. Suche sie und ergänze sie korrekt.
>
> Kategorie 3: Persönliche Information fehlt
>
> Die benötigte Information kann nur von mir kommen. Erfinde nichts. Markiere die Stelle und schreibe konkret auf, welche Information benötigt wird.
>
> Stelle nur dann Rückfragen, wenn sie tatsächlich notwendig sind. Bearbeite währenddessen alle anderen Teile weiter.
>
> 14. Endergebnis
>
> Am Ende erwarte ich folgende Ergebnisse:
>
> 1. Vollständig korrigierter Kommentar
>
> Speichere eine neue, vollständige und sauber formatierte Word-Datei mit dem Namen:
>
> Schriftlicher_Kommentar_Ube_FINAL.docx
>
> Die Datei soll alle vorgenommenen Korrekturen enthalten und als finale Arbeitsfassung dienen.
>
> Achte darauf, dass die Formatierung der ursprünglichen Datei möglichst erhalten bleibt. Dazu gehören insbesondere Überschriften, Seitenumbrüche, Tabellen, Bilder, Bildunterschriften, Fussnoten und Verzeichnisse.
>
> 2. Liste aller noch offenen persönlichen Aufgaben
>
> Erstelle eine separate Datei:
>
> OFFENE_PUNKTE_FINAL.md
>
> Darin stehen ausschliesslich Dinge, die du trotz vollständiger Prüfung nicht selbstständig erledigen konntest, weil persönliche Informationen, Entscheidungen oder fehlende Materialien von mir benötigt werden.
>
> Ordne die Punkte nach Priorität.
>
> 3. Änderungsprotokoll
>
> Erstelle eine Datei:
>
> AENDERUNGSPROTOKOLL_FINAL.md
>
> Darin dokumentierst du die wichtigsten inhaltlichen, wissenschaftlichen, sprachlichen und formalen Änderungen.
>
> Nenne jeweils das betroffene Kapitel und erkläre kurz, welches Problem behoben wurde.
>
> Dokumentiere auch grössere Umformulierungen, damit nachvollziehbar bleibt, wo und weshalb du eingegriffen hast.
>
> 4. Abschliessende Qualitätsbewertung
>
> Bewerte den korrigierten Kommentar kritisch anhand folgender Kriterien:
>
> * Inhaltliche Richtigkeit
> * Wissenschaftliche Qualität
> * Argumentationslogik
> * Quellenarbeit
> * Methodische Reflexion
> * Sprachliche Qualität
> * Erhalt der persönlichen Schreibstimme
> * KI-Dokumentation
> * Formale Vollständigkeit
> * Übereinstimmung mit dem fertigen Buch
>
> Sei ehrlich und kritisch. Gib keine künstlich gute Bewertung, nur weil du den Text selbst überarbeitet hast.
>
> 15. Verbindliche Abschlussregeln
>
> Bevor du die Arbeit als abgeschlossen bezeichnest, musst du folgende Bedingungen erfüllen:
>
> * Jedes Kapitel wurde vollständig gelesen.
> * Alle eindeutig feststellbaren inhaltlichen Fehler wurden korrigiert.
> * Alle wissenschaftlich problematischen Aussagen wurden überprüft.
> * Alle bekannten Kritikpunkte aus der vorherigen Bewertung wurden bearbeitet.
> * Zusätzliche Fehler wurden eigenständig gesucht und korrigiert.
> * Der gesamte Text wurde sprachlich geprüft.
> * Meine persönliche Schreibstimme wurde konsequent erhalten.
> * Alle auffindbaren Platzhalter wurden bearbeitet.
> * Quellen und Literaturangaben wurden überprüft.
> * Die KI-Dokumentation wurde auf Vollständigkeit und Ehrlichkeit geprüft.
> * Der Kommentar wurde mit dem fertigen Buch abgeglichen.
> * Die finale Fassung wurde nochmals vollständig gelesen.
> * Alle nicht selbstständig lösbaren Punkte wurden in der offenen Aufgabenliste dokumentiert.
>
> Wichtig: Eine gute Überarbeitung bedeutet nicht, dass der Text möglichst schön klingt. Sie bedeutet, dass er sachlich richtig, wissenschaftlich nachvollziehbar, vollständig, präzise und authentisch ist.
>
> Deine wichtigste Aufgabe ist es, die Qualität des Kommentars zu verbessern, ohne meine persönliche Stimme zu verlieren.
>
> Sei kompromisslos bei Fehlern, aber verändere nichts ohne sachlichen Grund.
>
> Das Endergebnis soll der bestmögliche Kommentar sein, den ich selbst hätte schreiben können, wenn ich alle Fehler erkannt und korrigiert hätte.
>
> Beginne jetzt mit der vollständigen Prüfung und arbeite bis zu den oben definierten Ergebnissen.

### 4.4 Master-Prompt 4 (Eingabe 9, 9.11.2026, 10:36)

Datei im Chat: `e527e169-attachment.txt`, 4732 Wörter, davon rund 4'550 im eigentlichen Prompt. Der Text vor der Überschrift «ULTIMATIVER MASTER-PROMPT» und der «letzte Hinweis» am Schluss gehören zur Datei, sind aber offensichtlich an euch gerichtet und nicht an Claude (siehe Abschnitt 1, Punkt 5). Dazu hat Aezri im Chat geschrieben:

> Ich habe dir noch ein dokument eingefügt der meine persönliche stimme enthaltet und du sollst diesen auch als vorlage nehmen für mein persönliche stimme und speicheres auf vaul Obsidian
>
> Nutze mein komplettes kontigent für diese arbeit für Fable nutze alle meine datei von obsidian vault

Mitgegeben wurde ausserdem die Word-Datei «Die Familienchronik über Aezri Peglow» (jetzt in `Persönliches/`).

> Die persönliche Schreibstimme wird im neuen Prompt die höchste Priorität haben, direkt nach der sachlichen Richtigkeit. Fable soll euren Kommentar nicht möglichst akademisch oder perfekt klingen lassen, sondern so verbessern, dass er weiterhin eindeutig nach euch klingt.
>
> Ich habe mir auch eure hochgeladene Word-Datei angesehen. Darin sind noch konkrete offene Stellen, beispielsweise beim endgültigen Buchtitel, den Bildquellen, den Druckangaben, der KI-Dokumentation und der tatsächlichen Eigenleistung. Zudem müssen der Kommentar und das Arbeitsjournal besonders sorgfältig miteinander abgeglichen werden.
>
> Deshalb habe ich den Prompt so aufgebaut, dass Fable nicht einfach alles umschreibt, sondern als wissenschaftlicher Gutachter, vorsichtiger Lektor und kritischer Faktenprüfer arbeitet. Das verfügbare Nutzungskontingent soll vor allem in gründliche Prüfungen, Quellenvergleiche und wiederholte Qualitätskontrollen fliessen.
>
> ## Master-Prompt für Fable
>
> Kopiere den folgenden Prompt vollständig in deine bestehende Fable-Unterhaltung, damit die bisherigen Dateien, Arbeitsstände und Entscheidungen berücksichtigt werden können.
>
> # ULTIMATIVER MASTER-PROMPT – FINALE MATURAARBEIT 2026
>
> ## Wissenschaftliche Endkontrolle, sprachliche Perfektionierung und authentische Überarbeitung von schriftlichem Kommentar und Arbeitsjournal
>
> **Projekt:** Maturaarbeit «Ube – Zwischen Tradition und Trend» / «Wem gehört der Ube-Boom?»
>
> **Schule:** Kantonsschule Baden
>
> **Verfasser:** Aezri Peglow, Tim Rosal und John Meuwly
>
> **Abgabetermin:** 10. November 2026
>
> **Arbeitsmodus:** Maximale Sorgfalt, vollständige Quellenkontrolle, selbstständige Bearbeitung, mehrfache Qualitätsprüfung und konsequenter Erhalt unserer persönlichen Schreibstimme.
>
> ---
>
> # 1. DEIN AUFTRAG – DIE ABSCHLIESSENDE QUALITÄTSSICHERUNG
>
> Du übernimmst jetzt die letzte und gründlichste Qualitätskontrolle unserer gesamten schriftlichen Dokumentation zur Maturaarbeit über Ube.
>
> Du arbeitest gleichzeitig als:
>
> - wissenschaftlicher Gutachter auf Maturaarbeitsniveau
> - kritischer Faktenprüfer und Quellenanalyst
> - äusserst sorgfältiger Deutschlektor mit Schweizer Rechtschreibung
> - Prüfer für wissenschaftliche Argumentationen und Methoden
> - Spezialist für Word-Dokumente, Fussnoten und Formatierung
> - kritischer Prüfer unseres Arbeitsjournals
> - Prüfer für die transparente Dokumentation von KI-Nutzung
> - Bewahrer unserer persönlichen Schreibstimme
>
> **Dein Ziel ist nicht eine möglichst schöne Neufassung, sondern die wissenschaftlich und sprachlich bestmögliche Version unseres tatsächlich selbst erarbeiteten Projekts.**
>
> Du sollst den bestehenden Kommentar und das Arbeitsjournal vollständig überprüfen, Fehler direkt beheben und danach nochmals kritisch kontrollieren.
>
> Arbeite selbstständig. Frage nicht nach jeder Änderung nach einer Bestätigung. Alle Probleme, die sich mit vorhandenen Materialien lösen lassen, sollst du selbstständig lösen.
>
> Wichtig: Du hast bereits in vorherigen Durchgängen an diesen Dokumenten gearbeitet. Vertraue deinen bisherigen Änderungen nicht blind. Prüfe auch deine eigenen früheren Ausgaben so kritisch wie einen fremden Text.
>
> Du darfst deine bisherigen Formulierungen jederzeit korrigieren, wenn sie falsch, ungenau, künstlich oder nicht durch unsere Materialien gedeckt sind.
>
> ---
>
> # 2. ABSOLUTE PRIORITÄT: UNSERE PERSÖNLICHE SCHREIBSTIMME
>
> ## DIES IST DIE WICHTIGSTE REDAKTIONELLE ANWEISUNG DES GESAMTEN AUFTRAGS.
>
> Ich möchte ausdrücklich **keinen vollständig neu geschriebenen Kommentar**, der sich nach einer KI, einem Universitätsprofessor oder einem professionellen wissenschaftlichen Autor anhört.
>
> Ich möchte einen Kommentar, der wissenschaftlich sehr gut ist, aber weiterhin wie von uns als Maturandinnen und Maturanden geschrieben klingt.
>
> **Bewahre unsere Schreibstimme, nicht die Schreibstimme deiner früheren Überarbeitungen.**
>
> ### 2.1 Das wichtigste Prinzip
>
> **So wenig wie möglich verändern. So viel wie nötig korrigieren.**
>
> Jeder Satz wird zuerst auf seine tatsächlichen Fehler geprüft.
>
> Wenn ein Satz grammatikalisch richtig, wissenschaftlich angemessen, verständlich und natürlich formuliert ist, bleibt er unverändert.
>
> Auch wenn du eine stilistisch elegantere Formulierung kennst, ist das allein kein Grund, etwas zu ändern.
>
> Eine einfache, natürliche und persönliche Formulierung ist einer künstlich akademischen Formulierung vorzuziehen, solange sie sachlich korrekt ist.
>
> ### 2.2 Was unbedingt erhalten bleiben muss
>
> Erhalte unsere typische Wortwahl, den natürlichen Satzbau, unseren direkten Ausdruck und unsere persönliche Art, etwas zu erklären.
>
> Insbesondere:
>
> - unsere verständliche und unkomplizierte Sprache
> - unsere charakteristischen Satzverbindungen
> - unseren Wechsel zwischen kürzeren und längeren Sätzen
> - unsere persönlichen Beobachtungen und Reflexionen
> - unsere eigenen Einschätzungen
> - unsere natürliche Art, Unsicherheiten zu formulieren
> - unsere Argumentationsweise
> - unsere ursprüngliche Aussageabsicht
> - die Wir-Perspektive unserer Gruppenarbeit
> - den Unterschied zwischen erzählenden, reflektierenden und wissenschaftlichen Kapiteln
>
> Verändere nicht jede Wiederholung. Gewisse Wiederholungen gehören zu einer natürlichen Schreibweise. Entferne sie nur dann, wenn sie den Text unnötig verlängern oder den Gedankengang beeinträchtigen.
>
> Erhalte auch persönliche Formulierungen wie «Wir haben gemerkt», «Für uns war» oder «Beim Recherchieren ist uns aufgefallen», sofern sie tatsächlich passen.
>
> Solche Sätze sind gerade bei einer Reflexion wertvoll.
>
> ### 2.3 Was du unbedingt vermeiden musst
>
> Vermeide künstlich akademische Ausdrücke, übermässig abstrakte Aussagen und unnötige Fachbegriffe.
>
> Vermeide typische KI-Muster wie:
>
> - ständig ähnliche Satzanfänge
> - immer gleich lange Absätze
> - übertrieben perfekte Übergänge
> - allgemeine und austauschbare Schlussfolgerungen
> - unnötig komplizierte Satzkonstruktionen
> - wiederholte Formeln wie «Dies verdeutlicht, dass ...»
> - künstliche Gegenüberstellungen
> - übermässige Verwendung von Doppelpunkten und Gedankenstrichen
> - unnötige rhetorische Fragen
> - Formulierungen, die mehr behaupten, als tatsächlich gezeigt wurde
>
> Du sollst den Text nicht absichtlich vereinfachen oder Fehler stehen lassen. Ziel ist ein sehr gutes sprachliches Niveau, aber ohne künstliche Perfektion.
>
> ### 2.4 Erstelle zuerst ein authentisches Stilprofil
>
> Bevor du mit den Korrekturen beginnst, suche im Obsidian-Vault nach unseren ursprünglichen, möglichst wenig mit KI überarbeiteten Texten.
>
> Untersuche insbesondere:
>
> 1. Frühere Fassungen des schriftlichen Kommentars.
> 2. Ursprüngliche Texte aus unserem Ube-Buch.
> 3. Selbst geschriebene Reflexionen und Arbeitsjournaleinträge.
> 4. Den ursprünglichen Begleitkommentar des Kochbuchprojekts.
> 5. Unsere eigenen Formulierungen aus der Konzeptphase.
>
> Unterscheide ausdrücklich zwischen tatsächlich selbst geschriebenen Texten und Texten, die bereits von Claude erstellt oder stark überarbeitet wurden.
>
> Nimm nicht automatisch die aktuellste oder sprachlich glatteste Version als Stilvorlage.
>
> Erstelle daraus intern ein kurzes Stilprofil mit Beispielen für unsere Wortwahl, Satzstruktur, Erklärweise und Reflexion.
>
> Achte bei den einzelnen Kapiteln darauf, ob sie von Aezri, Tim, John oder gemeinsam verfasst wurden. Übertrage nicht automatisch die individuelle Schreibweise einer Person auf sämtliche Kapitel.
>
> ### 2.5 Verbindliche Prüfung vor jeder Änderung
>
> Stelle dir vor jeder Umformulierung diese Fragen:
>
> 1. Ist die ursprüngliche Aussage tatsächlich falsch, unklar oder sprachlich problematisch?
> 2. Kann ich das Problem mit einem einzigen Wort oder einer kleinen Anpassung lösen?
> 3. Kann ich die ursprüngliche Satzstruktur behalten?
> 4. Wird die Aussage wissenschaftlich genauer?
> 5. Würden die Verfasser diesen Satz selbst so schreiben?
> 6. Klingt die neue Formulierung plötzlich künstlich oder deutlich akademischer als der restliche Text?
>
> Wenn die Änderung keinen klaren Vorteil bringt, verwende den ursprünglichen Satz.
>
> **Bei sachlichen Fehlern hat die wissenschaftliche Korrektheit Vorrang. Bei gleichwertigen richtigen Formulierungen hat unsere ursprüngliche Sprache Vorrang.**
>
> ### 2.6 Abschliessende Schreibstimmenkontrolle
>
> Führe am Ende einen eigenständigen Prüfdurchgang durch, bei dem du ausschliesslich die persönliche Schreibstimme beurteilst.
>
> Vergleiche jedes Kapitel mit dem Stilprofil.
>
> Suche gezielt nach Formulierungen, die während deiner eigenen Überarbeitung künstlich geworden sind.
>
> Mache diese Stellen wieder natürlicher, ohne wissenschaftliche Genauigkeit zu verlieren.
>
> **Das Endergebnis soll so klingen, wie wir selbst geschrieben hätten, wenn wir alle sprachlichen und wissenschaftlichen Fehler bereits erkannt hätten.**
>
> Die KI-Nutzung muss trotzdem vollständig und ehrlich dokumentiert bleiben. Die Bewahrung unserer Stimme darf niemals dazu dienen, tatsächliche KI-Beiträge zu verschweigen.
>
> ---
>
> # 3. NUTZE DAS VERFÜGBARE NUTZUNGSKONTINGENT INTENSIV UND SINNVOLL
>
> Mein Fable-Nutzungskontingent wird heute um 13:00 Uhr zurückgesetzt.
>
> Ich möchte deshalb, dass du das aktuell verfügbare Kontingent möglichst umfassend für diese abschliessende Qualitätskontrolle einsetzt.
>
> Nutze zusätzliche Rechenleistung und Werkzeugaufrufe für echte Qualitätsverbesserungen:
>
> - wiederholte Prüfung schwieriger Argumentationen
> - sorgfältige Vergleiche verschiedener Dateiversionen
> - systematische Quellenkontrollen
> - unabhängiges Nachrechnen von Statistiken
> - Vergleich des Kommentars mit dem fertigen Buch
> - Prüfung der Arbeitsjournaleinträge
> - vollständige Kontrolle der Fussnoten
> - Erkennung von Widersprüchen
> - erneute Prüfung deiner bereits vorgenommenen Änderungen
> - abschliessende sprachliche und formale Qualitätskontrollen
>
> **Wichtig:** Verbrauche keine Ressourcen absichtlich für sinnlose Wiederholungen oder unnötig lange Antworten.
>
> Setze die verfügbare Leistung dort ein, wo sie die wissenschaftliche Qualität unserer Arbeit tatsächlich verbessert.
>
> Eine Aussage soll nicht bloss deshalb als geprüft gelten, weil du sie bereits einmal gelesen hast.
>
> Führe bei wissenschaftlich kritischen Stellen eine zweite, unabhängige Prüfung anhand der Originalquellen durch.
>
> Wenn du aufgrund eines Limits nicht weiterarbeiten kannst, speichere einen nachvollziehbaren Zwischenstand.
>
> Behaupte nicht, länger gearbeitet oder mehr kontrolliert zu haben, als tatsächlich geschehen ist.
>
> ---
>
> # 4. VOLLSTÄNDIGE BESTANDSAUFNAHME ALLER MATERIALIEN
>
> Beginne nicht sofort mit der sprachlichen Überarbeitung.
>
> Verschaffe dir zuerst einen vollständigen Überblick über alle zugänglichen Projektmaterialien im Obsidian-Vault, über GitHub und in den bereitgestellten Dateien.
>
> Suche insbesondere nach:
>
> - der neuesten Fassung des schriftlichen Kommentars
> - unserem fertigen Ube-Buch als PDF oder InDesign-Export
> - allen Fassungen des Arbeitsjournals
> - dem Recherchedossier
> - dem Projektplan und Arbeitsvertrag
> - dem Begleitkommentar zur Zwischenpräsentation
> - der schriftlichen Bewertung von Frau Büschlen und Herrn Franceschi
> - allen verwendeten Quellen und wissenschaftlichen Studien
> - den Originalstatistiken
> - unseren eigenen Berechnungen
> - dem Interview mit Tita
> - den ursprünglichen Interviewfragen und Antworten
> - den Bildquellen und Lizenzen
> - den vorhandenen KI-Protokollen
> - unseren bisherigen Prompts und Chatverläufen
> - früheren Kommentarfassungen
> - bisherigen Korrekturlisten und Änderungsprotokollen
>
> Beziehe auch die aktuell bereitgestellte Word-Datei «Schriftlicher_Kommentar_Ube_FINAL.docx» ein.
>
> Der Dateiname FINAL bedeutet nicht automatisch, dass die Datei fehlerfrei oder die neueste Version ist.
>
> Bestimme anhand von Änderungsdatum, Inhalt und Versionsgeschichte, welche Fassung tatsächlich aktuell ist.
>
> ### Verbindliche Regeln
>
> Verwende die neueste vollständige Kommentarfassung als Arbeitsgrundlage.
>
> Vergleiche sie mit früheren Versionen, um unsere ursprünglichen Formulierungen wiederzufinden und unbeabsichtigte Änderungen zu erkennen.
>
> Behandle das tatsächlich fertige Buch als massgebliche Grundlage für Aussagen über Aufbau, Bilder und Gestaltung.
>
> Für die Entstehungsgeschichte sind das Arbeitsjournal und überprüfbare Projektdokumente entscheidend.
>
> Für wissenschaftliche Aussagen sind die Originalquellen massgeblich.
>
> Für unseren Schreibstil sind möglichst authentische Eigenformulierungen massgeblich.
>
> Erfinde keine fehlenden Dateien oder Inhalte.
>
> Überschreibe unter keinen Umständen die ursprünglichen Dokumente.
>
> ---
>
> # 5. WISSENSCHAFTLICHE UND INHALTLICHE VOLLKONTROLLE
>
> Lies den gesamten Kommentar vollständig.
>
> Nicht nur die Hauptkapitel, sondern auch Abstract, Fussnoten, Tabellen, Abbildungen, Verzeichnisse und Anhänge.
>
> Prüfe jeden inhaltlichen Abschnitt auf wissenschaftliche und argumentative Schwächen.
>
> Achte besonders auf:
>
> - unbelegte Behauptungen
> - falsche Zahlen
> - ungenaue Begriffe
> - methodisch unzulässige Vergleiche
> - unbegründete Kausalzusammenhänge
> - falsche zeitliche Einordnungen
> - unzulässige Verallgemeinerungen
> - Widersprüche zwischen Kapiteln
> - unklare Schlussfolgerungen
> - schwache oder unpassende Quellen
> - Aussagen, die über die Quellen hinausgehen
> - Vermischungen von Fakten und Interpretationen
> - Wiederholungen ohne zusätzlichen Erkenntniswert
> - unklare Einschränkungen
> - unzureichende Reflexion der eigenen Methode
>
> Prüfe nicht nur, ob ein Satz plausibel klingt.
>
> Prüfe, ob er tatsächlich durch die angegebenen Quellen oder unsere eigene Untersuchung gedeckt ist.
>
> ### Evidenzklassen
>
> Ordne kritische Aussagen gedanklich einer der folgenden Kategorien zu:
>
> **A – Direkt belegt:** Die Quelle stützt die Aussage eindeutig.
>
> **B – Indirekt gestützt:** Die Aussage ist eine nachvollziehbare Interpretation mehrerer Informationen.
>
> **C – Plausible Vermutung:** Die Erklärung ist möglich, aber nicht ausreichend belegt.
>
> **D – Ungeklärt oder problematisch:** Der Beleg fehlt, widerspricht der Aussage oder kann nicht überprüft werden.
>
> Behandle diese Kategorien sprachlich unterschiedlich.
>
> Eine Vermutung darf nicht als Tatsache erscheinen.
>
> Eine einzelne Beobachtung darf nicht zu einer landesweiten Entwicklung verallgemeinert werden.
>
> Wenn ein starker Befund nicht belegbar ist, schwäche die Aussage angemessen ab oder entferne sie.
>
> ---
>
> # 6. BESONDERS KRITISCHE STELLEN UNSERES KOMMENTARS
>
> Diese Punkte wurden bereits bei früheren Überarbeitungen problematisiert. Prüfe sie erneut, auch wenn sie inzwischen korrigiert wirken.
>
> ## 6.1 Weltmarkt und philippinische Exporte
>
> Prüfe die Gegenüberstellung zwischen dem geschätzten weltweiten Ube-Markt von rund 455,3 Millionen US-Dollar im Jahr 2024 und den philippinischen Ube-Exporten von rund 3,06 Millionen US-Dollar im Jahr 2025.
>
> Untersuche, ob beide Werte überhaupt dieselben Produktgruppen, Handelsstufen und Marktdefinitionen abbilden.
>
> Ein Verhältnis von rund 0,7 Prozent darf nicht ohne entsprechende Grundlage als philippinischer Marktanteil oder Anteil an der weltweiten Wertschöpfung ausgegeben werden.
>
> Prüfe auch, ob die philippinischen Exportkategorien korrekt beschrieben werden. Unterscheide Rohware, haltbar gemachte Ware und verarbeitete Produkte, soweit die Quellen das ermöglichen.
>
> Formuliere ausschliesslich Schlussfolgerungen, die wissenschaftlich tragfähig sind.
>
> ## 6.2 Zeitliche Entwicklung von Nachfrage und Produktion
>
> Prüfe den Rückgang der philippinischen Ube-Ernte seit 2006 beziehungsweise 2010.
>
> Stelle ihn der internationalen Nachfrageentwicklung gegenüber, ohne fälschlicherweise gleiche Zeiträume oder direkte Ursachen anzunehmen.
>
> Prüfe insbesondere die Angaben von 21'906 Tonnen im Jahr 2010 und 12'483 Tonnen im Jahr 2025.
>
> Unterscheide langfristige Strukturprobleme des Anbaus von Entwicklungen während des internationalen Ube-Booms.
>
> ## 6.3 Kausalität und Knappheit
>
> Die steigende Nachfrage allein beweist nicht, dass auf den Philippinen eine landesweite Knappheit entstanden ist.
>
> Trenne nachgewiesene Veränderungen, mögliche Ursachen und persönliche Beobachtungen.
>
> Titas Aussagen über die Verfügbarkeit auf ihrem Markt sind Erfahrungen einer einzelnen Bäuerin und Verkäuferin.
>
> Verwende sie nicht als repräsentative statistische Grundlage.
>
> ## 6.4 Kulturelle und wirtschaftliche Kontrolle
>
> Prüfe die Argumentation zu unserer Leitthese:
>
> «Die Philippinen verlieren beim Ube-Boom nicht ihre Kultur, sondern die Kontrolle über sie.»
>
> Unterscheide ausdrücklich:
>
> 1. die persönliche kulturelle Bedeutung von Ube
> 2. die internationale Darstellung und Vermarktung
> 3. die wirtschaftliche Kontrolle über Verarbeitung, Preise und Wertschöpfung
>
> Vermeide absolute Aussagen darüber, dass Filipinos oder philippinische Bauern ihre kulturelle Kontrolle vollständig verlieren.
>
> Prüfe auch, wie viel die Quellen tatsächlich über die wirtschaftliche Beteiligung der Philippinen aussagen.
>
> ## 6.5 Interview mit Tita
>
> Vergleiche sämtliche Aussagen mit den ursprünglichen Fragen und dem vollständigen Transkript.
>
> Prüfe:
>
> - die tatsächliche Zahl der gestellten und beantworteten Fragen
> - die Herkunft der Aussagen
> - den Marktpreis von 150 Pesos pro Kilogramm
> - den Vergleich mit den Preisen von 80 bis 100 Pesos
> - die unterschiedlichen Handelsstufen
> - die regionale und zeitliche Vergleichbarkeit
> - die Aussage über jüngere Menschen im Ube-Anbau
> - die Einordnung des Interviews als Einzelfall
> - Übersetzungen und sinngemässe Wiedergaben
>
> Erfinde keine persönlichen Angaben zur Durchführung des Interviews.
>
> Falls Informationen fehlen, markiere sie als offene persönliche Aufgabe.
>
> ## 6.6 Wissenschaftliche Rechnungen
>
> Rechne sämtliche Zahlen unabhängig nach.
>
> Kontrolliere insbesondere:
>
> - Prozentrechnungen
> - Veränderungen der Anbaufläche
> - Veränderungen der Erntemenge
> - Ertrag pro Hektare
> - hypothetische Produktionserträge
> - Exportanteile
> - Preisvergleiche
> - Währungsumrechnungen
> - Hochrechnungen
> - Angaben über Pflanzmaterial
> - Vergleiche mit Quinoa und Matcha
> - Zahlen in Abbildungen und Tabellen
>
> Prüfe bei jeder Rechnung auch die Voraussetzungen.
>
> Eine mathematisch richtige Rechnung kann wissenschaftlich trotzdem ungeeignet sein, wenn die verglichenen Grössen nicht zusammenpassen.
>
> ---
>
> # 7. LEITFRAGE, LEITTHESE UND SCHLUSSFOLGERUNGEN
>
> Unsere zentrale Leitfrage lautet:
>
> **«Inwiefern verändert der internationale Ube-Trend die traditionelle Bedeutung, Verwendung und Produktion von Ube auf den Philippinen?»**
>
> Die zugespitzte übergeordnete Frage lautet:
>
> **«Wem gehört der Ube-Boom?»**
>
> Prüfe, ob diese Fragen im Buch und im Kommentar tatsächlich beantwortet werden.
>
> Untersuche insbesondere die ursprüngliche Leitthese und ihre spätere Präzisierung zur wirtschaftlichen Wertschöpfung.
>
> Entscheide anhand der Belege, welche Formulierung am überzeugendsten ist.
>
> Prüfe dabei:
>
> - die vier einzelnen Thesen
> - ihre Behauptungen und Einwände
> - ihre jeweiligen Fazits
> - die Zusammenführung im Buch
> - die Einordnung in Kapitel 7 des Kommentars
> - das Abstract
> - die Reflexion
> - das Schlusswort
>
> Die Argumentation darf sich nicht zwischen den Kapiteln widersprechen.
>
> Ein wissenschaftlich begründeter Unterschied zwischen der ursprünglichen Leitthese und ihrer späteren Bewertung ist dagegen ausdrücklich erwünscht, sofern er nachvollziehbar erklärt wird.
>
> Bewahre unsere ursprüngliche Idee.
>
> Mache aus einer spannenden Leitthese keine inhaltsleere, übervorsichtige Formulierung.
>
> Aber behaupte auch nicht mehr, als wir nachweisen können.
>
> ---
>
> # 8. VOLLSTÄNDIGER ABGLEICH MIT DEM FERTIGEN UBE-BUCH
>
> Vergleiche den Kommentar systematisch mit dem neuesten tatsächlich fertiggestellten Buch.
>
> Kontrolliere:
>
> - endgültigen Buchtitel
> - Untertitel
> - Kapitelüberschriften
> - Kapitelreihenfolge
> - Seitenzahlen
> - Umfang
> - Vorwort und Schlusswort
> - wissenschaftliche Thesen
> - verwendete Bilder
> - Bildunterschriften und Bildnachweise
> - Schriftarten
> - Schriftgrössen
> - Farbgestaltung
> - Seitenlayout
> - Spalten und Satzspiegel
> - Quellenverzeichnis
> - Interviewanhang
> - tatsächlich umgesetzte Gestaltungselemente
>
> Im bisherigen Kommentar wird unter anderem ein Stand vom 8. November mit 52 Seiten beschrieben.
>
> Prüfe, ob dies noch dem endgültigen Buch entspricht.
>
> Unterscheide konsequent zwischen:
>
> **geplant – begonnen – umgesetzt – nicht umgesetzt.**
>
> Eine Gestaltungsidee darf nicht als fertig umgesetzt beschrieben werden, wenn sie nur geplant war.
>
> Prüfe auch bereits bekannte Differenzen, etwa bei Datierungen, Quellenbelegen und unterschiedlichen Angaben zum Anbau.
>
> Erstelle zusätzlich eine separate, präzise Korrekturliste für das Ube-Buch, falls du darin Fehler findest.
>
> Verändere das Buch selbst nur dann, wenn die Originaldateien bearbeitbar sind und dadurch keine unbeabsichtigten Layoutprobleme entstehen.
>
> ---
>
> # 9. ARBEITSJOURNAL – EIGENSTÄNDIGE VOLLSTÄNDIGE ÜBERPRÜFUNG
>
> Dieser Punkt ist genauso wichtig wie die Überarbeitung des Kommentars.
>
> Ich möchte, dass unser gesamtes Arbeitsjournal auf ein sehr hohes Qualitätsniveau gebracht wird.
>
> Das Journal soll klar, nachvollziehbar, zeitlich korrekt, vollständig und authentisch sein.
>
> **Es soll nicht nach einem nachträglich von KI erfundenen perfekten Arbeitsprozess aussehen.**
>
> ### 9.1 Chronologische Kontrolle
>
> Prüfe jeden Eintrag vom Projektbeginn bis zur Abgabe.
>
> Vergleiche Daten, Treffen, Tätigkeiten, Ergebnisse und Entscheidungen mit:
>
> - früheren Journalfassungen
> - dem Projektplan
> - dem schriftlichen Kommentar
> - dem Ube-Buch
> - vorhandenen Dateiversionen
> - den dokumentierten Rückmeldungen
> - unseren bisherigen Angaben und Chatverläufen
>
> Achte auf Widersprüche, unlogische Abläufe, doppelte Ereignisse und fehlende Erklärungen.
>
> Eine Tätigkeit darf nicht auf ein Datum gesetzt werden, an dem sie nachweislich noch gar nicht stattgefunden haben konnte.
>
> ### 9.2 Schreibstil im Arbeitsjournal
>
> Bewahre unseren persönlichen und natürlichen Stil.
>
> Schreibe verständlich und schülerisch, aber grammatikalisch korrekt.
>
> Die Einträge sollen wie echte Arbeitsberichte wirken, nicht wie wissenschaftliche Fachartikel.
>
> Vermeide künstliche Formulierungen und unnötig komplizierte Reflexionen.
>
> Erhalte auch Schwierigkeiten und Fehler im Arbeitsprozess.
>
> Wir müssen nicht so wirken, als hätten wir von Anfang an alles richtig gemacht.
>
> Gerade ein ehrliches Journal zeigt, wie wir uns weiterentwickelt haben.
>
> ### 9.3 Besondere Kontrolle der KI-unterstützten Einträge
>
> Ein Teil der späteren Journaleinträge wurde mithilfe von Claude aus unseren Angaben ausformuliert.
>
> Prüfe diese Einträge deshalb besonders kritisch.
>
> Unterscheide zwischen einem tatsächlich dokumentierten Ereignis und einer sprachlichen Ergänzung durch KI.
>
> Wenn du nicht nachweisen kannst, dass eine Tätigkeit stattgefunden hat, darfst du sie nicht als historische Tatsache ergänzen.
>
> Fehlende Einträge dürfen nur anhand überprüfbarer Informationen rekonstruiert werden.
>
> Kennzeichne solche Rekonstruktionen transparent.
>
> Falls Informationen fehlen, erstelle eine gezielte offene Frage, statt eine passende Geschichte zu erfinden.
>
> ### 9.4 Qualität der einzelnen Einträge
>
> Kontrolliere, ob aus den Einträgen hervorgeht:
>
> - wann gearbeitet wurde
> - wer beteiligt war
> - woran gearbeitet wurde
> - was dabei herauskam
> - welche Probleme auftraten
> - welche Entscheidungen getroffen wurden
> - wie es danach weiterging
>
> Nicht jeder Eintrag muss alle diese Punkte enthalten. Ergänze nur das, was tatsächlich bekannt und für die Nachvollziehbarkeit sinnvoll ist.
>
> Erhalte die ursprüngliche Struktur und Formatierung des Journals.
>
> ### 9.5 Abgleich zwischen Journal und Kommentar
>
> Prüfe alle wichtigen Daten aus Kapitel 2, Kapitel 5 und Kapitel 8 gegen das Arbeitsjournal.
>
> Achte besonders auf die Entstehung des Kochbuchprojekts, die Zwischenpräsentation, den Themenwechsel im August, die Aufteilung der Aufgaben, das Interview und die Endphase im November.
>
> Überprüfe auch die Daten in den Zeitstrahlen und Ablaufgrafiken.
>
> Wenn Kommentar und Journal voneinander abweichen, ermittle nach Möglichkeit anhand unabhängiger Projektunterlagen, welche Information stimmt.
>
> Ändere nicht einfach beide Texte so, dass sie übereinstimmen, ohne den tatsächlichen Ablauf zu prüfen.
>
> ---
>
> # 10. QUELLEN, FUSSNOTEN UND LITERATURVERZEICHNIS
>
> Kontrolliere sämtliche Quellen.
>
> Prüfe bei jeder wichtigen Quellenangabe:
>
> 1. Existiert die Quelle?
> 2. Ist der Autor oder Herausgeber korrekt?
> 3. Stimmen Titel, Datum und Jahr?
> 4. Ist die angegebene Seite richtig?
> 5. Unterstützt die Quelle tatsächlich die Behauptung?
> 6. Wurde die Quelle korrekt interpretiert?
> 7. Ist die URL vorhanden und richtig?
> 8. Ist ein Abrufdatum dokumentiert?
> 9. Stimmen Kurzbelege und Verzeichnis überein?
> 10. Wurde die Quelle direkt oder nur über eine Sekundärquelle benutzt?
>
> Nutze vorrangig unser vorhandenes Recherchedossier.
>
> Prüfe, ob du auf das Original zugreifen kannst.
>
> Wenn du einen wissenschaftlichen Artikel nicht vollständig lesen kannst, behaupte nicht, ihn vollständig geprüft zu haben.
>
> Kontrolliere insbesondere Quellen des CPBRD, der philippinischen Statistikbehörde, des Landwirtschaftsministeriums, des USDA sowie verwendete Marktstudien.
>
> Prüfe die Zitierweise anhand der tatsächlich geltenden Regeln der Kantonsschule Baden.
>
> Ergänze fehlende bibliografische Informationen, wenn sie zuverlässig ermittelt werden können.
>
> Erfinde keine Seitenzahlen, Daten oder Abrufdaten.
>
> Neue externe Quellen dürfen zur Überprüfung benutzt werden. Wenn du sie in die Arbeit aufnimmst, muss das transparent geschehen.
>
> ---
>
> # 11. KI-DOKUMENTATION – VOLLSTÄNDIG UND EHRLICH
>
> Das Kapitel zur KI-Nutzung gehört zu den besonders wichtigen Teilen der finalen Überarbeitung.
>
> Es muss den tatsächlichen Arbeitsprozess korrekt widerspiegeln.
>
> Berücksichtige insbesondere:
>
> - KI-generierte erste Entwürfe
> - die sprachliche Überarbeitung des Kommentars
> - die wissenschaftliche Prüfung durch Claude
> - die Überarbeitung von Argumentationen
> - die Erstellung oder Bearbeitung von Grafiken
> - die Erstellung von Illustrationen
> - die Unterstützung beim Arbeitsjournal
> - die Überprüfung von Quellen und Berechnungen
> - die abschliessenden Korrekturdurchgänge
>
> Prüfe die tatsächlichen Modellbezeichnungen und Eingabedaten anhand der verfügbaren Chatverläufe.
>
> Übernimm nicht ungeprüft frühere Bezeichnungen wie «Opus 5.5» oder «Fable 5.1», wenn sie nicht eindeutig dokumentiert sind.
>
> ### Der Unterschied zwischen KI und Eigenleistung
>
> Beschreibe präzise, welche Texte von KI erstellt wurden, welche nur überarbeitet wurden und welche von uns selbst stammen.
>
> Unterscheide ausserdem zwischen selbst recherchierten Informationen, selbst durchgeführten Berechnungen, eigenen Interpretationen und KI-unterstützten Formulierungen.
>
> Die Aussage «Wir haben die Texte geprüft und in eigene Worte gefasst» ist nicht ausreichend, wenn sie keine genaue Beschreibung unseres tatsächlichen Vorgehens enthält.
>
> Nenne keine Überprüfung als eigene Leistung, wenn sie nicht stattgefunden hat.
>
> Verschweige keine umfangreiche KI-Unterstützung.
>
> ### Prüfe auch diesen aktuellen Auftrag
>
> Die Überarbeitung, die du gerade durchführst, ist selbst eine weitere KI-Nutzung.
>
> Dokumentiere sie deshalb ebenfalls sachlich und nachvollziehbar.
>
> Erhalte nach Möglichkeit den genauen Wortlaut der entscheidenden Prompts und die entsprechenden Eingabedaten in einer separaten KI-Dokumentation.
>
> Prüfe, ob lange Prompt-Anhänge tatsächlich im Kommentar stehen müssen oder besser separat abgegeben werden können.
>
> Entscheide dies anhand der Schulvorgaben und nicht nur aus gestalterischen Gründen.
>
> Wenn persönliche Bestätigungen fehlen, lasse sie als offene Aufgaben stehen.
>
> ---
>
> # 12. FORMALE ENDKONTROLLE ALLER DOKUMENTE
>
> Suche systematisch nach sämtlichen Unvollständigkeiten.
>
> Prüfe insbesondere:
>
> - eckige Klammern und Platzhalter
> - fehlende Klassennamen
> - uneinheitliche Buchtitel
> - fehlende Autorenzuordnungen
> - fehlende Bildnachweise
> - unklare Bildlizenzen
> - fehlende Druckangaben
> - unvollständige Quellen
> - fehlende URLs
> - nicht überprüfte Fussnotenseiten
> - fehlerhafte Seitenverweise
> - unvollständige Tabellen
> - fehlende Abbildungsbeschriftungen
> - nicht aktualisierte Inhaltsverzeichnisse
> - nicht aktualisierte Abbildungs- und Tabellenverzeichnisse
> - unklare Angaben zum Interview
> - offene Felder im KI-Nachweis
> - widersprüchliche Schreibweisen
> - Kommentare und Bearbeitungsnotizen
>
> Aus der vorliegenden Fassung sind insbesondere Stellen zum endgültigen Buchtitel, zur Klassenzuordnung, zu Bildquellen, Papier und Bindung, zur Absprache über die Zitierweise, zum Interview und zu einigen KI-Eingaben bekannt.
>
> Prüfe, welche davon mit unseren vorhandenen Materialien inzwischen gelöst werden können.
>
> Lasse keine versteckten Bearbeitungsnotizen unbeachtet.
>
> Wenn eine Information fehlt, die nur wir selbst bestätigen können, erfinde sie nicht.
>
> Markiere sie eindeutig und übertrage sie in die offene Aufgabenliste.
>
> Verwende überall Schweizer Rechtschreibung mit «ss» statt «ß».
>
> Erhalte die ursprüngliche Word-Formatierung möglichst vollständig, einschliesslich Tabellen, Grafiken, Bildpositionen, Fussnoten und Seitenumbrüchen.
>
> ---
>
> # 13. DEINE ARBEITSWEISE – MEHRERE VERBINDLICHE DURCHGÄNGE
>
> Arbeite in dieser Reihenfolge:
>
> ## Durchgang 1 – Bestandsaufnahme
>
> Ermittle alle relevanten Dateien und Versionen.
>
> Identifiziere die aktuelle Arbeitsgrundlage.
>
> Erstelle intern eine Liste mit Fehlern, offenen Punkten und Widersprüchen.
>
> ## Durchgang 2 – Persönlicher Stil
>
> Erstelle das authentische Stilprofil anhand möglichst ursprünglicher Texte.
>
> Unterscheide unsere Schreibstimme von früheren KI-Formulierungen.
>
> ## Durchgang 3 – Inhaltliche Kontrolle
>
> Prüfe jedes Kapitel auf sachliche und wissenschaftliche Fehler.
>
> Korrigiere unhaltbare Aussagen und ungeeignete Vergleiche.
>
> ## Durchgang 4 – Quellenprüfung
>
> Kontrolliere Belege, Statistiken, Zitate, Zahlen und Fussnoten.
>
> Rechne alle wesentlichen Zahlen unabhängig nach.
>
> ## Durchgang 5 – Sprachliche Korrektur
>
> Korrigiere Grammatik, Rechtschreibung, Satzbau und Zeichensetzung.
>
> Verändere keine korrekten, natürlichen Sätze ohne konkreten Grund.
>
> ## Durchgang 6 – Vergleich mit dem Buch
>
> Prüfe alle Angaben zum fertigen Produkt.
>
> Erfasse Fehler, die im Buch selbst noch korrigiert werden müssen.
>
> ## Durchgang 7 – Arbeitsjournal
>
> Überprüfe sämtliche Einträge chronologisch, sprachlich und inhaltlich.
>
> Vergleiche die Angaben mit dem tatsächlichen Arbeitsprozess.
>
> ## Durchgang 8 – KI-Dokumentation
>
> Prüfe die Transparenz und Vollständigkeit der KI-Angaben.
>
> Ergänze nur nachweisbare Informationen.
>
> ## Durchgang 9 – Formale Kontrolle
>
> Prüfe das vollständige Word-Dokument einschliesslich aller Anhänge und Verzeichnisse.
>
> ## Durchgang 10 – Unabhängige Schlusskontrolle
>
> Lies die korrigierte Fassung erneut von Anfang bis Ende.
>
> Gehe dabei nicht davon aus, dass deine vorherigen Änderungen richtig waren.
>
> Suche bewusst nach neuen Fehlern, die du selbst eingeführt haben könntest.
>
> ## Durchgang 11 – Schreibstimmenkontrolle
>
> Vergleiche die fertige Fassung erneut mit unseren ursprünglichen Texten.
>
> Entferne unnötige sprachliche Glättungen.
>
> Stelle sicher, dass der Kommentar weiterhin natürlich, persönlich und auf Maturaarbeitsniveau klingt.
>
> ## Durchgang 12 – Technische Endprüfung
>
> Öffne die fertigen Dateien erneut.
>
> Prüfe Dokumentstruktur, Tabellen, Bilder, Fussnoten, Verzeichnisse und Dateiintegrität.
>
> Kontrolliere die Seiten visuell, soweit die verfügbaren Werkzeuge dies ermöglichen.
>
> Eine Datei gilt erst als fertig, wenn sie nach dem Speichern nochmals geprüft wurde.
>
> ---
>
> # 14. DOKUMENTATION UND SICHERUNG DES FORTSCHRITTS
>
> Erstelle zu Beginn einen separaten Arbeitsordner für die finale Qualitätskontrolle.
>
> Arbeite mit Kopien. Überschreibe niemals die ursprünglichen Dateien.
>
> Lege die Datei **FORTSCHRITT_FINALKORREKTUR.md** an.
>
> Halte darin fest:
>
> - welche Dateien untersucht wurden
> - welche Kapitel vollständig geprüft wurden
> - welche Quellen noch ungeprüft sind
> - welche Korrekturen erfolgt sind
> - welche Arbeiten noch fehlen
> - welche Entscheidungen von uns benötigt werden
> - welche Ausgabedateien bereits gespeichert wurden
>
> Aktualisiere diese Datei nach jedem abgeschlossenen grösseren Arbeitsschritt.
>
> Falls ein Kontextlimit, Nutzungslimit oder technisches Problem auftritt, muss anhand dieser Datei klar sein, wie die Überarbeitung fortgesetzt werden kann.
>
> Falls du nicht alles abschliessen kannst, priorisiere die inhaltliche Richtigkeit, die wissenschaftliche Qualität, den Erhalt der persönlichen Stimme und die tatsächliche Sicherung aller bereits vorgenommenen Änderungen.
>
> Behaupte niemals, ein Kapitel sei fertig geprüft, wenn du nur Teile davon gelesen hast.
>
> ---
>
> # 15. VERBINDLICHE ENDERGEBNISSE
>
> Erstelle nach der Überarbeitung folgende Dateien:
>
> ### A. Schriftlicher_Kommentar_Ube_FINAL.docx
>
> Die vollständig korrigierte Fassung unseres schriftlichen Kommentars.
>
> Erhalte das ursprüngliche Layout möglichst genau.
>
> Lasse keine erfundenen Informationen, unbelegten Behauptungen oder unbemerkten Platzhalter zurück.
>
> ### B. Arbeitsjournal_Ube_FINAL
>
> Das vollständige, korrigierte Arbeitsjournal im ursprünglichen Dateiformat.
>
> Erhalte die Chronologie und die tatsächlich dokumentierten Ereignisse.
>
> ### C. OFFENE_PUNKTE_FINAL.md
>
> Eine vollständige Liste mit allen noch offenen persönlichen Aufgaben.
>
> Ordne sie nach Priorität.
>
> Nenne für jede Aufgabe die konkrete Textstelle, die fehlende Information und den Grund, weshalb du sie nicht selbstständig lösen konntest.
>
> Trenne unbedingt abgabekritische Probleme von kleineren Verbesserungsmöglichkeiten.
>
> ### D. AENDERUNGSPROTOKOLL_FINAL.md
>
> Dokumentiere die wesentlichen Änderungen.
>
> Nenne das betroffene Kapitel, die Art des Fehlers und die vorgenommene Korrektur.
>
> Bei grösseren Änderungen soll erkennbar sein, warum du eingegriffen hast.
>
> ### E. FORTSCHRITT_FINALKORREKTUR.md
>
> Der tatsächliche Bearbeitungsstand und das Ergebnis aller Prüfdurchgänge.
>
> ### F. BUCH_KORREKTURLISTE_FINAL.md
>
> Alle noch vorhandenen Fehler im eigentlichen Ube-Buch, die nicht bereits direkt korrigiert werden konnten.
>
> ### G. KI_DOKUMENTATION_FINAL.md
>
> Ein vollständiger, transparenter Überblick über die nachweisbare KI-Nutzung, einschliesslich dieser finalen Überarbeitung.
>
> Die Dokumentation soll zu den Anforderungen unserer Schule passen.
>
> ### H. QUALITAETSBEWERTUNG_FINAL.md
>
> Eine kritische abschliessende Bewertung des Kommentars und Arbeitsjournals.
>
> Bewerte:
>
> - Inhaltliche Richtigkeit
> - Wissenschaftliche Qualität
> - Argumentationslogik
> - Qualität der Quellen
> - Methoden und Eigenleistung
> - Sprachliche Qualität
> - Erhalt unserer persönlichen Schreibstimme
> - Nachvollziehbarkeit des Arbeitsprozesses
> - Vollständigkeit des Arbeitsjournals
> - Transparenz der KI-Dokumentation
> - Formale Qualität
> - Übereinstimmung mit dem fertigen Buch
>
> Sei kritisch und ehrlich.
>
> Verteile keine künstlich hohen Noten.
>
> Wenn eine Quellenprüfung oder eine andere Kontrolle nicht möglich war, muss sich das in der Bewertung widerspiegeln.
>
> ---
>
> # 16. ENDGÜLTIGE ABNAHMEKRITERIEN
>
> Bevor du die Arbeit als abgeschlossen bezeichnest, kontrolliere folgende Bedingungen:
>
> - Der gesamte Kommentar wurde vollständig gelesen.
> - Das gesamte Arbeitsjournal wurde vollständig geprüft.
> - Alle wichtigen Berechnungen wurden nachgerechnet.
> - Die wissenschaftlichen Problemstellen wurden kontrolliert.
> - Alle Kapitel wurden auf Widersprüche überprüft.
> - Die Quellenarbeit wurde kontrolliert.
> - Der Kommentar wurde mit dem fertigen Ube-Buch verglichen.
> - Die Argumentation zur Leitthese ist wissenschaftlich nachvollziehbar.
> - Die Aussagen über das Interview sind korrekt eingeordnet.
> - Die KI-Dokumentation ist transparent.
> - Sämtliche auffindbaren Platzhalter wurden bearbeitet.
> - Alle offenen persönlichen Angaben wurden dokumentiert.
> - Die ursprüngliche Formatierung wurde möglichst erhalten.
> - Die fertigen Dateien wurden nochmals geöffnet und kontrolliert.
> - Die persönliche Schreibstimme wurde in einem eigenen Schlussdurchgang geprüft.
>
> Falls einzelne Bedingungen nicht erfüllt werden konnten, benenne dies ausdrücklich.
>
> Eine unvollständig geprüfte Datei darf nicht als abgabefertig bezeichnet werden.
>
> ---
>
> # 17. DIE ENTSCHEIDENDE LETZTE ANWEISUNG
>
> Ich möchte, dass du unsere Arbeit mit aussergewöhnlicher Sorgfalt überprüfst.
>
> Aber ich möchte nicht, dass du unsere Arbeit in deine eigene verwandelst.
>
> Unsere Maturaarbeit soll unsere Geschichte erzählen: von einem philippinischen Kochbuch über den Themenwechsel zu Ube bis zur wissenschaftlichen Auseinandersetzung mit dem internationalen Boom.
>
> Dazu gehören unsere eigenen Gedanken, unsere Entscheidungen, unsere Unsicherheiten und die Schwierigkeiten, die während des Projekts aufgetreten sind.
>
> Diese Dinge sollen nicht durch perfekt klingende, allgemeine akademische Sätze ersetzt werden.
>
> **Deine Aufgabe ist es, die beste Version unserer eigenen Arbeit herauszuarbeiten, nicht eine neue Arbeit zu verfassen.**
>
> Ein guter Satz, der nach uns klingt, ist wertvoller als ein stilistisch eleganterer Satz, der nicht mehr unsere Sprache trägt.
>
> Ein wissenschaftlich vorsichtiger Satz ist wertvoller als eine beeindruckende Behauptung ohne ausreichenden Beleg.
>
> Ein ehrliches Arbeitsjournal ist wertvoller als eine nachträglich perfektionierte Projektgeschichte.
>
> Eine transparente KI-Dokumentation ist wertvoller als der Versuch, unsere tatsächliche Arbeitsweise schöner darzustellen.
>
> Nutze deine verfügbaren Fähigkeiten und das verbleibende Kontingent so gründlich wie möglich für echte Qualitätskontrolle.
>
> Suche nicht nur nach Fehlern, die ich bereits genannt habe.
>
> Finde auch Fehler, die uns beiden bisher entgangen sind.
>
> Prüfe deine eigenen Änderungen erneut und hinterfrage deine bisherigen Entscheidungen.
>
> **Sei kompromisslos bei sachlichen Fehlern und ausgesprochen zurückhaltend bei unnötigen stilistischen Änderungen.**
>
> Beginne jetzt selbstständig mit der Bestandsaufnahme und arbeite die Prüfphasen nacheinander ab.
>
> Stelle nur dann Rückfragen, wenn ohne eine persönliche Information keine sachlich richtige Entscheidung möglich ist. Erledige alle anderen Arbeiten unabhängig davon.
>
> Speichere regelmässig und dokumentiere den tatsächlichen Fortschritt.
>
> **Die wichtigste Regel bleibt während der gesamten Überarbeitung bestehen: Wissenschaftlich präziser werden, ohne unsere persönliche Schreibstimme zu verlieren.**
>
> Das Ziel ist eine überzeugende, ehrliche, wissenschaftlich saubere und authentische Maturaarbeit, die weiterhin eindeutig von Aezri, Tim und John stammt.
>
> Ein letzter Hinweis: Ein langer Prompt allein garantiert nicht, dass Fable das gesamte Kontingent verbraucht oder tatsächlich alle Dateien vollständig prüft. Entscheidend sind die gespeicherten Ergebnisse und nachweisbaren Kontrollen. Gerade weil eure Abgabe am 10. November 2026 ist, würde ich die drei Dateien `Schriftlicher_Kommentar_Ube_FINAL.docx`, `Arbeitsjournal_Ube_FINAL` und `OFFENE_PUNKTE_FINAL.md` zuerst kontrollieren.

## 5. Was Claude in der vierten Runde (Eingabe 9) konkret gemacht hat

Damit ihr den Anteil beurteilen könnt, hier ohne Beschönigung:

- **Stilprofil:** aus der Familienchronik, euren unveränderten Journaleinträgen bis 03.06. und Aezris eigenen Nachrichten; gespeichert als [[Schreibstimme Aezri]]. Nicht als Vorlage verwendet: Buchtext, Journaleinträge ab 05.06., alle Kommentarfassungen seit dem 8.11., weil dort der KI-Anteil unklar oder sicher ist.
- **Kommentar:** ein eigener Durchgang über alle Kapitel, in dem Sätze wieder verbunden, Pointen und Doppelpunkt-Schlüsse gestrichen und Wörter wie «leider», «eigentlich», «ehrlich gesagt», «zum Glück» zugelassen wurden. Betroffen: Abstract, 1.1, 2.1 bis 2.5, 4.1, 4.4, 5.2, 5.4, 5.5, 7.1 bis 7.4, 7.6, 8.2, 8.3 (33 Stellen, Wortlaut im [[AENDERUNGSPROTOKOLL_FINAL]] Tabelle A2). Keine neue Zahl, keine neue Quelle, keine neue Behauptung. Inhaltlich geändert wurde nur eine Stelle: In 5.5 und Anhang A stand, Tita habe ihren Namen selbst gewählt; das ist nirgends belegt (Journal 28.10.: «deshalb nennen wir sie Tita»; Transkript: «Her name is Tita») und steht jetzt als offene Frage. Dazu Eingabe 9 in 10.6, die Anpassung in 8.3 («vier weitere Durchgänge», Journalprüfung) und die Umstellung des Anhang-B-Absatzes auf vier Prompts.
- **Arbeitsjournal:** Endfassung aus den 45 Einträgen im Vault, als Word-Tabelle im Format der Original-Datei (A4 quer, sechs Spalten, Arial 8,5) und als Lesekopie. Berichtigt wurden nur Stellen, die dem Transkript, dem Buch-PDF oder einer geprüften Quelle widersprechen (Daten zum Exportstopp 16.09.; Umrechnung 21.10.; Kostenfrage 23.10., 28.10., 04.11.; Frage zu jungen Leuten 23.10., 28.10.; «Sorten» 28.10.; Markierungen im Transkript 04.11.; «Händler» 04.11.; Bilder und Fazits in Kapitel 3 06.11.). Jede Berichtigung ist gelb markiert und sagt, was vorher dort stand. Angenommene Treffen, Calls und Reisedaten tragen einen gelben Prüfvermerk. Die Einträge bis 03.06. sind unverändert, in den KI-ausformulierten Einträgen ab 05.06. wurden nur wiederkehrende Formeln («Ich habe mich gefragt, ob») je Person variiert. Für den 8., 9. und 10. November stehen leere Vorlagen mit dem, was aus dem KI-Nachweis belegt ist. Kein Eintrag wurde erfunden, keine Tätigkeit verschoben.
- **Geprüft:** alle 45 Journaleinträge gegen Kommentar, Transkript und Buch-PDF (Reihenfolge, Daten, Rechnungen 4,62 und 5,27 t/ha, rund 25'000 t, 43 Prozent); Schrift (Minion Pro) und Format (A4) im PDF; die Belegformen «zit. nach» und «übers. d. Verf.» im Buch; die Stellen, an denen das Buch Tita zitiert; Trennungen im PDF; mechanische Sprachprüfung des Kommentars (ß, Semikolons, Gedankenstriche, gerade Anführungszeichen, numerische Daten, Doppelwörter).
- **Nachgeholt um 13:00 (auf Aezris Nachfrage):** Websuche zu rund zwanzig Angaben des Buches, die vorher nie geprüft waren (Ergebnis in [[BUCH_KORREKTURLISTE_FINAL]] Abschnitt 7), Skript-Gegenproben (jedes Datum im Kommentar gegen das Journal, jede Quelle im Journal gegen das Buch, Abbildungen 1 und 2 gegen das Journal). Dabei eine falsche Korrektur von Claude aus Runde 2 zurückgenommen: «Berichte zum Exportstopp ab 11. September» (BusinessMirror) liess sich nicht belegen; euer Journal (13./14. September) hatte recht. Kommentar 5.2, Journal 16.09. und dieser Nachweis sind angepasst.
- **Nicht geprüft:** die Chatverläufe der Eingaben 1 bis 5, die Zitierregeln und die Beurteilung vom 19.06. (nicht im Vault), InDesign-Dateien, CPBRD- und USDA-Original, und alles, was nur ihr bestätigen könnt.

## 6. Dateien, die Claude geschrieben hat (Stand 9.11.)

In `09 Finalisierung/`: `kommentar_quelle_v2.txt`, `kommentar_quelle_v3.txt`, `kommentar_quelle_final.txt` (Quelltexte), `Schriftlicher_Kommentar_Ube_v2.docx`, `_v3.docx`, `_FINAL.docx`, `build_v2.py`, `build_v3.py`, `build_final.py`, `make_figures_v2.py`, `Abbildungen/`, `journal_v2.py`, `journal_final.py`, `ARBEITSJOURNAL_FINAL.md`, `Arbeitsjournal_Ube_FINAL.docx`, die Notizen 00 bis 07, `OFFENE_PUNKTE_FINAL.md`, `AENDERUNGSPROTOKOLL_FINAL.md`, `FORTSCHRITT_FINALKORREKTUR.md`, `FORTSCHRITT_KOMMENTAR.md`, `BUCH_KORREKTURLISTE_FINAL.md`, `QUALITAETSBEWERTUNG_FINAL.md`, diese Datei; Sicherungen in `Versionen/`. In `Persönliches/`: die Familienchronik als Markdown-Kopie und das Stilprofil. In `08 Schriftlicher Kommentar/`: die Lesekopie `03_KOMMENTAR_ENTWURF.md` wird bei jedem Bau neu geschrieben. Eure Originaldateien (`07 Originaldateien/`, `03 Arbeitsjournal/Arbeitsjournal_Maturaarbeit_Ube.docx`) wurden nicht verändert.
