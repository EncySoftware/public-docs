# KI-gestützte Interpreterentwicklung

Dieser Abschnitt beschreibt, wie Sie einen Interpreter mit Hilfe eines KI-Assistenten entwickeln und pflegen: wie Sie die Werkzeuge vorbereiten, worum Sie den Assistenten bitten, was er von Ihnen braucht und wie Sie das Ergebnis prüfen. Er gilt für Interpreter in C#, die aus den Vorlagen des CAM-Systems erstellt werden und im Abschnitt [Entwicklung eines eigenen Interpreters in (.NET) C#](../dotnet/developing-a-custom-interpreter-in-net-csharp.md) beschrieben sind, sowie für native Interpreter in Delphi oder C++ (siehe [Interpreter-Bibliothek](../interpreter-structure/interpreter-library/interpreter-library.md)).

Standardmäßig entwickelt der Assistent einen Interpreter in C# (.NET). Eine native Bibliothek in Delphi oder C++ erstellt er nur, wenn Sie ausdrücklich darum bitten oder einen bereits vorhandenen nativen Interpreter ändern.

## Wie die Arbeit aussieht

Sie schreiben im Chat in Ihren eigenen Worten:

> In den Programmen für unsere Maschine ist die Drehachse als B90 geschrieben, an der Maschine heißt sie aber B1. Ein Programm mit B90 wird nicht simuliert. Bitte korrigieren.

Danach sehen Sie zu. Der Assistent liest die NC-Programme und die Maschine des Projekts, findet die Stelle, an der der Interpreter die Achswörter liest, entscheidet, welche Art von Unterschied vorliegt — eine Einstellung oder eine Änderung im Code —, nimmt die Änderung vor, baut den Interpreter, lässt die NC-Programme im CAM-System durch ihn laufen und zeigt, was sich in der Simulation und im Protokoll geändert hat.

Sie lesen das Ergebnis und antworten auf dieselbe Weise — „richtig, aber dieselbe Maschine schreibt auch B=DC(30)“ —, und der Ablauf wiederholt sich.

Code selbst zu schreiben ist nicht nötig, Sie können aber jederzeit jede Änderung ansehen und von Hand korrigieren. Nur die Entscheidung lässt sich nicht abgeben: Ob die Simulation dem entspricht, was Ihre Maschine tut, beurteilen Sie. Alles, was dieser Abschnitt über die Prüfung des Ergebnisses sagt, dient genau diesem Zweck.

## Was der Assistent von Ihnen braucht

- Die NC-Programme, die der Interpreter lesen muss, und das Projekt des CAM-Systems mit der Maschine, für die sie geschrieben sind.
- Das Programmierhandbuch der Steuerung zu den betreffenden Wörtern und Zyklen.
- Das installierte CAM-System oder ENCY Tuner, in dem der Interpreter arbeiten muss.
- Das erwartete Ergebnis: was die Maschine mit dem Satz macht, der falsch simuliert wird.

Je mehr echte Programme Sie mitgeben, desto besser: Die Schreibweise der Wörter übernimmt der Assistent aus ihnen, nicht aus dem Gedächtnis.

## Was es kostet

Die Dokumentation und die Skills werden kostenlos veröffentlicht. Das Modell, das Ihnen antwortet, gehört nicht dazu: Ein KI-Assistent ist eine Dienstleistung des Anbieters des Modells und wird nach der Menge des verarbeiteten Textes oder per Abonnement abgerechnet. Sie benötigen ein Konto bei einem Anbieter von KI-Diensten oder beim Entwickler des KI-Clients; die Arbeit erfolgt zu dessen Bedingungen und Preisen.

Wenn die Daten in Ihrem Netzwerk bleiben müssen, kann das Modell auf eigener Hardware betrieben werden; richten Sie dann einen Client darauf, der das unterstützt. Beachten Sie, dass kleine lokale Modelle mehrstufige Arbeit nach Skills deutlich schlechter bewältigen: Bevor Sie sich auf ein solches Modell verlassen, testen Sie es an einer echten Aufgabe. Alles Übrige in diesem Abschnitt ändert sich nicht — CAM-System, Interpreter und NC-Programme befinden sich ohnehin auf Ihrem Computer.

## Lesereihenfolge

| Seite | Wofür sie zuständig ist |
|---|---|
| [Wie KI-gestützte Entwicklung funktioniert](how-it-works.md) | Aus welchen Teilen die Arbeit besteht, was jeder Teil tut, was der Assistent kann und was nicht |
| [Einrichtung der Werkzeuge](setup.md) | Der kurze Weg: KI-Client installieren, Skills herunterladen, mit zwei Anfragen prüfen |
| [Organisation des Arbeitsbereichs](workspace.md) | Der Arbeitsordner als Gedächtnis des Assistenten: NC-Programme, Maschinenprojekt, Handbuch, Notizen, Änderungsverlauf |
| [Arbeitsablauf .NET](dotnet-workflow.md) | Der Standardweg: Interpreter in C# aus einer Vorlage — Erstellen, Bauen, Debuggen, Änderungen |
| [Arbeitsablauf für native Interpreter](native-workflow.md) | Nur auf ausdrücklichen Wunsch oder für einen bereits nativen Interpreter: Delphi, C++ |
| [Prüfung und Bestätigung des Ergebnisses](review-and-verify.md) | Durchlauf aller NC-Programme vor und nach einer Änderung, Prüfstufen, Vorbereitung des Interpreters für die Übergabe |
| [Fehlerbehebung](troubleshooting.md) | Typische Symptome, ihre Ursachen und was zu tun ist |
| [Erweiterte Einrichtung](advanced-setup.md) | Das vollständige Einrichtungsverfahren: Skills in verschiedenen Clients, Werkzeuge zum Bauen und Debuggen, Protokoll, Anweisungsdatei, mehrere Produktversionen, separater Arbeitsplatz, automatische Prüfungen |

Wenn Sie gerade erst anfangen, lesen Sie die Seiten der Reihe nach bis zum Arbeitsablauf .NET; die Seite über native Interpreter nur, wenn Sie einen solchen brauchen. Die Seite [Erweiterte Einrichtung](advanced-setup.md) müssen Sie nicht selbst lesen: Sie ist für den Assistenten gedacht, der sie beim Einrichten der Werkzeuge liest.

## Skills für den Assistenten

Ein Skill ist eine Anleitung in einfachen Worten: was zu tun ist, in welcher Reihenfolge, was zu prüfen ist und wann die Arbeit als abgeschlossen gilt. Code enthält er nicht — es ist eine Textdatei, die der Assistent liest und befolgt, ähnlich wie eine Einweisung für einen neuen Mitarbeiter. Einen solchen Skill kann jeder schreiben oder korrigieren, der einen Arbeitsablauf in Worten erklären kann.

Die Skills liegen im Ordner `skills` dieses Abschnitts: Jeder Skill ist ein eigener Ordner mit der Datei `SKILL.md`. Alle Skills lassen sich von dieser Website als ein Archiv herunterladen: [Skills herunterladen](https://docs.encycam.com/technical/Interpreters/3/de/src/ai-assisted-development/skills/ai-skills.zip) (`ai-skills.zip`, die sechs Ordner der Skills liegen im Stamm des Archivs). Die Skills sind auf Englisch geschrieben; mit dem Assistenten können Sie in jeder Sprache schreiben. Zusammen begleiten sie die gesamte Arbeit am Interpreter: Der Assistent beginnt mit dem allgemeinen Skill und greift im Verlauf der Arbeit auf die übrigen zurück.

| Skill (Ordner) | Wofür | Seite des Abschnitts |
|---|---|---|
| [`interpreter-development`](skills/interpreter-development/SKILL.md) | Der allgemeine Skill: Was zuerst zu klären ist, in welcher Reihenfolge gearbeitet wird und wann die Arbeit abgeschlossen ist. Standardmäßig wird ein Interpreter in C# (.NET) entwickelt | [Wie KI-gestützte Entwicklung funktioniert](how-it-works.md) |
| [`inspect-nc-programs`](skills/inspect-nc-programs/SKILL.md) | Sammeln der NC-Programme und der Maschinendaten (Achsen, Kanäle, M-Funktionen) sowie Auflisten aller Wörter, die in den Programmen vorkommen | [Organisation des Arbeitsbereichs](workspace.md) |
| [`develop-dotnet-interpreter`](skills/develop-dotnet-interpreter/SKILL.md) | Erstellen, Konfigurieren, Bauen und Debuggen eines C#-Interpreters aus einer Vorlage — der Standardweg | [Arbeitsablauf .NET](dotnet-workflow.md) |
| [`develop-native-interpreter`](skills/develop-native-interpreter/SKILL.md) | Native Interpreter-Bibliothek in Delphi oder C++ — nur wenn wirklich ein nativer Interpreter benötigt wird | [Arbeitsablauf für native Interpreter](native-workflow.md) |
| [`nc-interpreter-foundations`](skills/nc-interpreter-foundations/SKILL.md) | Wie das CAM-System einen Satz liest und wann der Code des Interpreters aufgerufen wird | [Wie KI-gestützte Entwicklung funktioniert](how-it-works.md) |
| [`verify-interpretation`](skills/verify-interpretation/SKILL.md) | Durchlauf aller NC-Programme vor und nach einer Änderung, Vergleich der Ergebnisse und Vorbereitung des Interpreters für die Übergabe | [Prüfung und Bestätigung des Ergebnisses](review-and-verify.md) |

Jeder Skill lässt sich auch auf dieser Website über den Link in der Tabelle lesen. Ist das Archiv nicht verfügbar, laden Sie die Quelldatei `SKILL.md` auf der Seite des Skills herunter und legen Sie sie in einen Ordner mit dem Namen des Skills, zum Beispiel `skills/interpreter-development/SKILL.md`. Kopieren Sie alle Skills auf einmal: Sie verweisen aufeinander. Wie Sie sie in Ihren KI-Client einbinden, steht in der [Einrichtung der Werkzeuge](setup.md), ausführlich in der [erweiterten Einrichtung](advanced-setup.md#skills-in-verschiedenen-ki-clients).

Neben ihnen können Sie eigene Skills ablegen: Skills sind gewöhnliche Markdown-Dateien, und in derselben Form lassen sich die Erfahrungen festhalten, die Ihr Team sammelt — unterstützte Steuerungen, Besonderheiten der Programme Ihrer Kunden. Siehe [Organisation des Arbeitsbereichs](workspace.md).

## Was bei Ihnen bleibt

Betrachten Sie jede Antwort als Entwurf. Der Assistent sieht nur, was Sie ihm gegeben haben: Undokumentiertes Verhalten der Steuerung kennt er nicht, und eine plausibel aussehende Simulation kann falsch sein. Bevor Sie den Interpreter an einen Anwender übergeben, lassen Sie alle vorhandenen NC-Programme durch ihn laufen, lesen Sie die Warnungen im [Protokoll der Interaktion mit dem Interpreter](../g-code-interpretation/log-interaction-with-the-interpreter/log-interaction-with-the-interpreter.md) und prüfen Sie die Simulation der geänderten Sätze. Geben Sie keine Passwörter, Kundenarchive und keine Daten in den Chat, die Ihr Unternehmen nicht verlassen dürfen.
