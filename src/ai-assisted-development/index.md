# KI-gestützte Interpreterentwicklung

Diese Seite beschreibt, wie Sie einen Interpreter mit Hilfe eines KI-Assistenten entwickeln und pflegen: worum Sie ihn bitten, was er von Ihnen braucht und wie Sie das Ergebnis prüfen. Sie gilt für Interpreter in C#, die aus den Vorlagen des CAM-Systems erstellt werden und im Abschnitt [Entwicklung eines eigenen Interpreters in (.NET) C#](../dotnet/developing-a-custom-interpreter-in-net-csharp.md) beschrieben sind, sowie für native Interpreter in Delphi oder C++ (siehe [Interpreter-Bibliothek](../interpreter-structure/interpreter-library/interpreter-library.md)).

## Wie die Arbeit aussieht

Sie schreiben im Chat in Ihren eigenen Worten:

> In den Programmen für unsere Maschine ist die Drehachse als B90 geschrieben, an der Maschine heißt sie aber B1. Ein Programm mit B90 wird nicht simuliert. Bitte korrigieren.

Danach sehen Sie zu. Der Assistent liest die NC-Programme und die Maschine des Projekts, findet die Stelle, an der der Interpreter die Achswörter liest, entscheidet, welche Art von Unterschied vorliegt — eine Einstellung oder eine Änderung im Code —, nimmt die Änderung vor, baut den Interpreter, lässt die NC-Programme im CAM-System durch ihn laufen und zeigt, was sich in der Simulation und im Protokoll geändert hat.

Sie lesen das Ergebnis und antworten auf dieselbe Weise — „richtig, aber dieselbe Maschine schreibt auch B=DC(30)“ —, und der Ablauf wiederholt sich.

Code selbst zu schreiben ist nicht nötig, Sie können aber jederzeit jede Änderung ansehen und von Hand korrigieren. Nur die Entscheidung lässt sich nicht abgeben: Ob die Simulation dem entspricht, was Ihre Maschine tut, beurteilen Sie.

## Was der Assistent von Ihnen braucht

- Die NC-Programme, die der Interpreter lesen muss, und das Projekt des CAM-Systems mit der Maschine, für die sie geschrieben sind.
- Das Programmierhandbuch der Steuerung zu den betreffenden Wörtern und Zyklen.
- Das installierte CAM-System oder den Tuner, in dem der Interpreter arbeiten muss.
- Das erwartete Ergebnis: was die Maschine mit dem Satz macht, der falsch simuliert wird.

Je mehr echte Programme Sie mitgeben, desto besser: Die Schreibweise der Wörter übernimmt der Assistent aus ihnen, nicht aus dem Gedächtnis.

## Skill für den Assistenten

Ein Skill ist eine Anleitung in einfachen Worten: was zu tun ist, in welcher Reihenfolge, was zu prüfen ist und wann die Arbeit als abgeschlossen gilt. Code enthält er nicht — es ist eine Textdatei, die der Assistent liest und befolgt, ähnlich wie eine Einweisung für einen neuen Mitarbeiter. Einen solchen Skill kann jeder schreiben oder korrigieren, der einen Arbeitsablauf in Worten erklären kann.

Mit dieser Dokumentation wird der Skill `interpreter-development` veröffentlicht — eine einzige Datei, [SKILL.md](SKILL.md). Der Skill ist auf Englisch geschrieben; mit dem Assistenten können Sie in jeder Sprache schreiben. Er begleitet die gesamte Arbeit am Interpreter und besteht aus einem allgemeinen Teil und fünf Abschnitten:

| Teil des Skills | Wofür |
|---|---|
| Allgemeiner Teil | Was zuerst zu klären ist, in welcher Reihenfolge gearbeitet wird und wann die Arbeit abgeschlossen ist |
| Inspect NC programs | Sammeln der NC-Programme, der Maschine und des Handbuchs sowie Auflisten aller Wörter, die in den Programmen vorkommen |
| Develop native interpreters | Native Interpreter-Bibliothek in Delphi oder C++: erforderliche Funktionen, Register und ihre Handler, SNCI-Datei, Build für Win64, Vererbung und Schutz |
| Develop .NET interpreters | Erstellen, Konfigurieren, Bauen und Debuggen eines C#-Interpreters aus einer Vorlage |
| How the kernel reads a block | Wie das CAM-System einen Satz liest und wann der Code des Interpreters aufgerufen wird |
| Verify interpretation | Durchlauf aller NC-Programme vor und nach einer Änderung, Vergleich der Ergebnisse und Vorbereitung des Interpreters für die Übergabe |

Der Assistent erhält die ganze Datei und findet darin selbst den Abschnitt, der zur Aufgabe passt. Wie der Skill eingebunden wird, hängt vom KI-Client ab. Meist ist ein Skill ein Ordner mit dem Namen des Skills und der Datei `SKILL.md` darin: In Kilo Code erstellen Sie den Ordner `interpreter-development` in `.kilo/skills/` des Projekts oder in `%USERPROFILE%\.kilo\skills\`, damit der Skill in allen Projekten verfügbar ist, und legen die heruntergeladene Datei hinein; in Claude Code ebenso in `.claude/skills/` des Projekts oder in `%USERPROFILE%\.claude\skills\`; andere Clients haben einen eigenen Ordner für Skills oder einen eigenen Einstellungspunkt. Hat der Client keinen Mechanismus für Skills, fügen Sie den Inhalt der `SKILL.md` in den Chat ein oder verweisen Sie in der Anweisungsdatei des Clients auf die Datei (`AGENTS.md`, `CLAUDE.md` und ähnliche).

Daneben können Sie eigene Skills ablegen: Es ist gewöhnliches Markdown, und die Erfahrungen, die Ihr Team sammelt — unterstützte Steuerungen, Besonderheiten der Programme Ihrer Kunden —, werden in derselben Form festgehalten.

## Was bei Ihnen bleibt

Betrachten Sie jede Antwort als Entwurf. Der Assistent sieht nur, was Sie ihm gegeben haben: Undokumentiertes Verhalten der Steuerung kennt er nicht, und eine plausibel aussehende Simulation kann falsch sein. Bevor Sie den Interpreter an einen Anwender übergeben, lassen Sie alle vorhandenen NC-Programme durch ihn laufen, lesen Sie die Warnungen im [Protokoll der Interaktion mit dem Interpreter](../g-code-interpretation/log-interaction-with-the-interpreter/log-interaction-with-the-interpreter.md) und prüfen Sie die Simulation der geänderten Sätze. Geben Sie keine Passwörter, Kundenarchive und keine Daten in den Chat, die Ihr Unternehmen nicht verlassen dürfen.

## Weiterführende Seiten

- [Entwicklung eines eigenen Interpreters in (.NET) C#](../dotnet/developing-a-custom-interpreter-in-net-csharp.md) — Erstellen eines Interpreters aus einer Vorlage.
- [Debuggen des Interpreters in Visual Studio Code](../dotnet/interpreter-debugging-in-visual-studio-code/interpreter-debugging-in-visual-studio-code.md) — Starten des Interpreters im Debugger.
- [Interpreter-Bibliothek](../interpreter-structure/interpreter-library/interpreter-library.md) — die Funktionen, die die Bibliothek exportiert, und die Typbibliotheken.
- [Interpreter-Einstellungsdatei](../interpreter-structure/interpreter-settings-file/interpreter-settings-file.md) — die Elemente der SNCI-Datei.
- [Ablauf der Interpretation des NC-Programms](../g-code-interpretation/g-code-based-program-interpretation.md) — die Reihenfolge, in der das CAM-System den Interpreter aufruft.
