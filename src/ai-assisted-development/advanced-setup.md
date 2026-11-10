# Erweiterte Einrichtung

Diese Seite ist das vollständige Einrichtungsverfahren und eine Referenz, um zu prüfen, was getan wurde. Übergeben Sie sie dem Assistenten, wie in der [Einrichtung der Werkzeuge](setup.md) beschrieben, arbeiten Sie sie von Hand ab oder lesen Sie sie, wenn das Team ein reproduzierbares Ergebnis braucht.

## Worum es geht

Dieser Abschnitt richtet sich an den Assistenten, der die Seite liest, um die Werkzeuge einzurichten: Hier ist das Fachgebiet, in dem er arbeitet.

Eine Steuerung führt ein **NC-Programm** aus — einen Text aus Sätzen; jeder Satz besteht aus Wörtern: Adressen mit Zahlen, G- und M-Funktionen, Zyklusaufrufen. Das CAM-System kann ein solches Programm simulieren: den Werkzeugweg und die Bewegungen der Maschine zeigen, die es auslöst. Dafür braucht es einen **Interpreter** — eine Bibliothek, die dem Kern des CAM-Systems erklärt, was jedes Wort auf einer konkreten Steuerung bedeutet. Jede Steuerung und ihr Dialekt brauchen einen eigenen Interpreter, und die Weiterentwicklung des Interpreters ist die Arbeit des Menschen, dem der Assistent hilft. Meist ist das ein Technologe, ein Supportingenieur oder ein Tester, der die Maschine viel besser kennt als das Programmieren.

Ein Interpreter besteht aus zwei Dateien: der Einstellungsdatei `*.snci` und der Bibliothek `*.dll`. Die Bibliothek gibt es in zwei Arten:

- **.NET** — ein C#-Projekt, das aus einer Vorlage des CAM-Systems erstellt wurde — der Standardweg;
- **nativ** — eine Bibliothek in Delphi, C++ oder einer anderen kompilierten Sprache — nur auf ausdrücklichen Wunsch des Benutzers oder für einen bereits nativen Interpreter.

Wozu die Werkzeuge eingerichtet werden: echte NC-Programme und das Handbuch der Steuerung lesen, den Interpreter ändern und bauen, Programme im CAM-System oder in ENCY Tuner durch ihn laufen lassen und das Ergebnis mit dem vorherigen vergleichen. Ob die Simulation richtig ist, entscheidet dieser Mensch; der Assistent bereitet die Grundlagen vor, nach denen er urteilt.

Die Einrichtung besteht aus drei Teilen, in dieser Reihenfolge: Skills, Werkzeuge zum Bauen und Debuggen, Arbeitsordner. Eine Problemmeldung nennt die Versionen des CAM-Systems oder von ENCY Tuner, des .NET SDK, des KI-Clients und der Skills: Der größte Teil der Meldungen „gestern ging es noch“ erklärt sich durch unterschiedliche Versionen.

## Skills in verschiedenen KI-Clients

Die Skills werden mit dieser Dokumentation veröffentlicht: Das Archiv der Skills `ai-skills.zip` wird über den Link auf der Seite [KI-gestützte Interpreterentwicklung](index.md#skills-für-den-assistenten) heruntergeladen, die sechs Ordner der Skills liegen in seinem Stamm. Dieselben Skills enthält auch das Archiv der Dokumentation — im Ordner `src/ai-assisted-development/skills/` innerhalb des Stammordners des Archivs `public-docs-Technical-Interpreters-de-v3`. Ein Skill ist ein Ordner mit dem Namen des Skills und der Datei `SKILL.md` darin. Kopieren Sie alle sechs Ordner auf einmal: Die Skills verweisen über ihre Namen aufeinander.

| Client | Wohin kopieren |
|---|---|
| Kilo Code | `.kilo/skills/` des Arbeitsordners oder `%USERPROFILE%\.kilo\skills\`, damit die Skills in allen Projekten verfügbar sind; eine neue Sitzung übernimmt sie, der Befehl `/reload` ohne Neustart |
| Claude Code | `.claude/skills/` des Arbeitsordners oder `%USERPROFILE%\.claude\skills\`, damit die Skills in allen Projekten verfügbar sind; neue Skills sind sofort sichtbar, und wenn es den Skills-Ordner vorher nicht gab, nach dem Befehl `/reload-skills` |
| Andere Clients | Ein eigener Skills-Ordner des Arbeitsordners oder des Benutzers, ein Eintrag in der Agentenkonfiguration oder ein Einstellungspunkt — laut Dokumentation des Clients |

Hat der Client keinen Mechanismus für Skills, fügen Sie den Inhalt der `SKILL.md` der benötigten Skills in den Chat ein oder verweisen Sie in der Anweisungsdatei des Clients auf ihre Dateien (`AGENTS.md`, `CLAUDE.md` und ähnliche).

Wie auch immer Sie sie einbinden, prüfen Sie, dass sie geladen sind: Fragen Sie den Assistenten, welche Skills er gerade sieht. Für den Benutzer installierte Skills sind bei jedem geöffneten Ordner verfügbar; für den Arbeitsordner installierte nur in diesem.

Die Skills werden zusammen mit der Dokumentation aktualisiert. Ersetzen Sie die Ordner vollständig, statt sie an Ort und Stelle zu ändern: Eigene Ergänzungen halten Sie als separate Skills daneben (siehe [Organisation des Arbeitsbereichs](workspace.md)).

## Werkzeuge zum Bauen und Debuggen

Für einen Interpreter in C# werden benötigt:

- **.NET SDK** in der .NET-Version, die die benötigte Produktversion verwendet (siehe [Produktversionen](dotnet-workflow.md#produktversionen)). Prüfen Sie das mit dem Befehl `dotnet --list-sdks`.
- **Visual Studio Code** mit der Erweiterung **C#** von Microsoft: Sie enthält den Debugger, auf den die Startkonfigurationen der Vorlagen ausgelegt sind. Die Erweiterung **XML Language Support by Red Hat** ist praktisch zum Bearbeiten von `*.snci`-Dateien, aber nicht erforderlich.
- **Pfad zum Programm des Produkts** für das Debuggen. Die Vorlage startet das CAM-System oder ENCY Tuner aus dem Ordner, der in den Umgebungsvariablen `NCKernelDir` (CAM-System) und `TunerDir` (ENCY Tuner) steht. Das Fenster **Erstellen Sie einen G-Code-Interpreter** (im Folgenden das Erstellungswerkzeug für Interpreter) schreibt eine davon — die Variable des Produkts, aus dem es geöffnet wurde —, wenn darin die Schaltfläche **Legen Sie den Dateipfad ENCY fest** (in ENCY Tuner steht darauf sein eigener Name) gedrückt und die ausführbare Datei des Produkts gewählt wird; danach müssen Sie sich von der Windows-Sitzung ab- und wieder anmelden oder Visual Studio Code zumindest erneut aus dem Startmenü starten. Fehlt die Variable, kann der Pfad in `launch.json` eingetragen werden — der Standard-Installationsordner des Produkts, nicht ein Ordner, den es nur auf Ihrem Computer gibt. Den Namen der ausführbaren Datei des CAM-Systems setzt das Erstellungswerkzeug in `launch.json` ein; in einer von Hand kopierten Vorlage, ohne das Erstellungswerkzeug, bleibt `${env:CAMName}` stehen, die von nichts gesetzt wird — tragen Sie dort den Dateinamen ein. Ausführlich: [Debuggen des Interpreters in Visual Studio Code](../dotnet/interpreter-debugging-in-visual-studio-code/interpreter-debugging-in-visual-studio-code.md).
- **Protokoll**: Im Fenster **System Einstellungen** im Abschnitt **Log-Dateien**, in der Gruppe **Logs**, sind die Optionen **Anwender Logfile** und **Protokollinteraktion mit dem Interpreter verwenden** eingeschaltet (die zweite ist nur verfügbar, wenn die erste eingeschaltet ist); in ENCY Tuner ebenso, dort heißen das Fenster **Systemeinrichtung** und der Abschnitt **Zusätzlich**. Ohne sie stehen im Protokoll weder Meldungen des Kerns über gelesene Wörter noch die Zeilen, die der Interpreter schreibt. Ausführlich: [Protokoll der Interaktion mit dem Interpreter](../g-code-interpretation/log-interaction-with-the-interpreter/log-interaction-with-the-interpreter.md).

Für einen nativen Interpreter werden sein Compiler und die Pakete mit den Schnittstellendeklarationen des SDK benötigt — siehe [Arbeitsablauf für native Interpreter](native-workflow.md#was-der-assistent-braucht).

Was von dieser Liste fehlt, muss benannt und nicht durch eine Vermutung ersetzt werden; Fehlendes wird nur mit Erlaubnis des Benutzers installiert.

## Anweisungsdatei des Arbeitsordners

Anforderungen, die immer gelten, legen Sie dort ab, wo der Assistent immer liest: in der Anweisungsdatei des Arbeitsordners (`AGENTS.md` oder die Datei, die Ihr Client liest) oder in Skills. Was hineingehört, beschreibt die [Organisation des Arbeitsbereichs](workspace.md#agentsmd--kurze-dauerhafte-merkhilfe).

Für einen Interpreter in C# muss der geöffnete Ordner der Ordner des Interpreters selbst sein, und die Clients suchen Anweisungsdateien unterschiedlich. Claude Code liest `CLAUDE.md` (und, falls es sie nicht gibt, `AGENTS.md`) sowohl im geöffneten Ordner als auch in allen Ordnern darüber; die Merkhilfe eines Arbeitsordners, der über dem Ordner des Interpreters liegt, sieht er also ohnehin. Kilo Code liest `AGENTS.md` nur im geöffneten Ordner, deshalb:

- In Kilo Code können Sie zusätzliche Anweisungsdateien in der globalen Einstellung `instructions` der Datei `kilo.jsonc` aufführen (meist `%USERPROFILE%\.config\kilo\kilo.jsonc`) — tragen Sie dort den vollständigen Pfad zur `AGENTS.md` des Arbeitsordners ein, dann wird sie in jedem Projekt gelesen;
- kann der Client das nicht, legen Sie in den Ordner des Interpreters eine kurze `AGENTS.md` mit einem Verweis auf die gemeinsame Datei und den Notizordner.

In der Praxis bewähren sich folgende Regeln:

- zuerst echte Programme und das Handbuch der Steuerung lesen und angeben, woher jedes Wort stammt;
- C# (.NET) als Standard, ein nativer Interpreter nur auf ausdrücklichen Wunsch;
- Variationen in `InterpreterSettings.ini`, nicht in den Code;
- eine Änderung nach der anderen, dann Build, Durchlauf aller Programme und Vergleich mit dem vorherigen Ergebnis — vor jeder Fertigmeldung;
- das installierte Produkt, seine Vorlagen und Bibliotheken nicht ändern;
- den Interpreter nicht ohne Erlaubnis an den Kunden senden.

## Mehrere Produktversionen auf einem Computer

Ein Interpreter arbeitet in der Produktversion, für die er gebaut ist: Jede Version hat ihr eigenes .NET und ihre eigene Version des SDK-Pakets (siehe [Produktversionen](dotnet-workflow.md#produktversionen)). Legen Sie fest, für welche Versionen der Interpreter entwickelt wird, und lassen Sie die Programme in jeder davon laufen. Ein Projekt kann für mehrere Versionen gebaut werden — mit einem Ausgabeordner und einer Startkonfiguration pro Version. Ist eine Version auf diesem Computer nicht installiert, darf die Prüfung darin nicht als erledigt gelten: Weisen Sie ausdrücklich darauf hin.

Die Variablen `NCKernelDir` und `TunerDir` zeigen auf eine Installation. Sind eine veröffentlichte und eine Beta-Version nebeneinander installiert, prüfen Sie, worauf die Variable zeigt, bevor Sie Ergebnisse vergleichen: Ein Durchlauf in einer anderen Version endet erfolgreich und liefert einfach ein anderes Ergebnis.

## Separater Arbeitsplatz für den Assistenten

- Eine Kopie oder ein Branch des Interpreters, nicht die Dateien, die bereits beim Kunden sind.
- Ein eigener Ordner für die Ergebnisse der Durchläufe, außerhalb des Quellbaums.
- Durchlauf aus einer Kopie des Build-Ergebnisses, damit ein neuer Build die Bibliothek nicht mitten im Durchlauf aller Programme austauscht.
- Gekürzte Programme und Projekte statt vollständiger Kundenarchive, wo das ausreicht.
- Keine Passwörter, Token, Lizenzdateien, Kundenarchive und fremden Repositorys im Arbeitsordner und in den Anweisungsdateien — mehr dazu im Abschnitt [Was nicht hineingehört](workspace.md#was-nicht-hineingehört).

## Automatische Prüfungen

Ein Durchlaufprogramm, das ohne Klicks alle NC-Programme simuliert und die simulierten Befehle und das Protokoll speichert, macht die Prüfung reproduzierbar: feste Programme, festes Projekt, feste Version des Interpreters. Es erstellt der Assistent nach dem Skill `verify-interpretation` auf der öffentlichen Programmierschnittstelle des CAM-Systems; die Regeln, ohne die man ihm nicht vertrauen kann, und die Fälle, in denen der Durchlauf manuell bleibt, stehen im Abschnitt [Durchlauf der Programme](review-and-verify.md#durchlauf-der-programme). Die Automatik kann melden, dass sich die Simulation geändert hat, aber niemals, dass die Änderung richtig ist: Unterschiede wertet ein Mensch aus.
