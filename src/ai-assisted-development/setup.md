# Einrichtung der Werkzeuge

Die Einrichtung übernimmt der Assistent selbst. Ihr Anteil ist klein: KI-Client installieren, das Archiv mit den Skills herunterladen und dem Assistenten die Anleitung geben. Den Rest — Skills ablegen, Werkzeuge zum Bauen und Debuggen prüfen, das installierte CAM-System finden — erledigt der Assistent selbst und berichtet über das Ergebnis. Ohne Sie geht es nur bei Erlaubnissen und Aktionen in den Programmfenstern nicht: bei der Erlaubnis, fehlende Programme zu installieren; beim Neustart des KI-Clients, falls er nötig ist; im CAM-System oder in ENCY Tuner beim Erstellen des Interpreters im Fenster **Erstellen Sie einen G-Code-Interpreter**, bei der Schaltfläche **Legen Sie den Dateipfad ENCY fest** in diesem Fenster (in ENCY Tuner steht darauf sein eigener Name), danach beim Ab- und erneuten Anmelden in Windows und beim Einschalten des Protokolls im Fenster **System Einstellungen** (in ENCY Tuner **Systemeinrichtung**). Auf jede dieser Aktionen weist der Assistent Sie selbst hin, wenn sie an der Reihe ist.

## 1. Installieren Sie einen KI-Client

Am bequemsten arbeiten Sie in Visual Studio Code: Dort wird der Interpreter auch gebaut und debuggt (siehe [Debuggen des Interpreters in Visual Studio Code](../dotnet/interpreter-debugging-in-visual-studio-code/interpreter-debugging-in-visual-studio-code.md)). Der Chat ist eine Erweiterung wie jede andere: Öffnen Sie den Bereich **Extensions** (`Ctrl+Shift+X`), suchen Sie die gewünschte nach ihrem Namen und installieren Sie sie. Geeignet ist jeder Client, dem Sie erlauben können, Dateien des Arbeitsordners zu lesen und zu ändern und darin Befehle auszuführen — zum Beispiel Kilo Code oder Claude Code; ein Client, der im Terminal arbeitet, wird auf seine eigene Weise installiert.

Sie benötigen ein Konto bei einem Anbieter von KI-Diensten — siehe [Was es kostet](index.md#was-es-kostet).

Für einen Interpreter in C# brauchen Sie außerdem [Visual Studio Code](https://code.visualstudio.com/Download) mit der Erweiterung **C#** von Microsoft und das [.NET SDK](https://dotnet.microsoft.com/download) in der .NET-Version, unter der Ihre Produktversion läuft (siehe [Produktversionen](dotnet-workflow.md#produktversionen)). Vorab installieren müssen Sie sie nicht: In Schritt 3 prüft der Assistent, was fehlt, und bietet an, es zu installieren — mit Ihrer Erlaubnis.

## 2. Laden Sie die Skills herunter

Laden Sie das [Archiv der Dokumentation](https://github.com/EncySoftware/public-docs/archive/refs/heads/Technical/Interpreters/de/v3.zip) herunter und entpacken Sie es. Der gesamte Inhalt des Archivs liegt im Stammordner `public-docs-Technical-Interpreters-de-v3`, die Skills darin im Ordner `src/ai-assisted-development/skills/`: sechs Ordner, jeder mit einer Datei `SKILL.md`.

## 3. Übergeben Sie das dem Assistenten

Öffnen Sie in Visual Studio Code den Arbeitsordner (siehe [Organisation des Arbeitsbereichs](workspace.md)), öffnen Sie den Chat, erlauben Sie ihm, Befehle im Arbeitsordner auszuführen, und stellen Sie die Aufgabe. Die Skills werden in Ihren Benutzerordner (`%USERPROFILE%`) kopiert, also außerhalb des Arbeitsordners; der Client fragt deshalb auch dafür um Erlaubnis. Passen Sie die Pfade an (`<Archiv>` ist der vollständige Pfad zum Ordner `public-docs-Technical-Interpreters-de-v3` des entpackten Archivs) und fügen Sie ein:

```text
Richte die Werkzeuge für die Interpreterentwicklung nach der Anleitung ein:
<Archiv>\src\ai-assisted-development\advanced-setup.md
(dieselbe Seite auf der Website: https://docs.encycam.com/technical/Interpreters/3/de/src/ai-assisted-development/advanced-setup.html)

Entpacktes Archiv der Dokumentation: <Archiv>
Das CAM-System oder ENCY Tuner ist installiert in: <Installationsordner>

Kopiere alle Skills aus dem Archiv in den Skills-Ordner dieses Clients
für den Benutzer, nicht für den Arbeitsordner,
prüfe das .NET SDK und Visual Studio Code mit der C#-Erweiterung;
nenne, was fehlt, und biete an, es zu installieren.
Sag mir dann, was genau du geändert hast und welche Skills du jetzt siehst.
```

Neue Skills übernehmen die Clients unterschiedlich: Claude Code sofort (wenn es den Skills-Ordner vorher nicht gab, nach dem Befehl `/reload-skills`), Kilo Code in einer neuen Sitzung oder nach dem Befehl `/reload`, andere Clients laut ihrer Dokumentation. Braucht der Client einen Neustart, sagt der Assistent Ihnen das: Für Sie übernehmen kann er ihn nicht.

## 4. Prüfen Sie, ob alles geklappt hat

Zwei Anfragen im Chat genügen. Beide sind ungefährlich: Der Assistent liest nur und ändert nichts.

**Prüfung der Skills.** Schreiben Sie:

> Welche Skills für die Interpreterentwicklung siehst du gerade, und mit welchem beginnst du die Arbeit?

Eine gute Antwort zählt sechs Skills mit den Namen ihrer Ordner auf und nennt `interpreter-development` als ersten. Wenn der Assistent über „typische“ Skills spricht oder darum bittet, ihm Dateien zu schicken, sind die Skills nicht eingebunden — kehren Sie zu Schritt 3 oder zur [erweiterten Einrichtung](advanced-setup.md) zurück.

**Prüfung des Lesens von Programmen.** Legen Sie ein oder zwei echte NC-Programme in den Ordner `programs` des Arbeitsordners und schreiben Sie:

> Lies die NC-Programme im Ordner `programs` und zähle auf, welche Wörter in welcher Schreibweise darin vorkommen. Ändere nichts.

Eine gute Antwort ist eine Liste der Wörter aus Ihren Dateien: Adressen, G- und M-Funktionen, Schreibweisen von Achsen wie `B90` und `B1=90`. Enthält die Antwort Wörter, die in den Programmen nicht vorkommen, argumentiert der Assistent aus dem Gedächtnis: Nennen Sie ihm die Dateien ausdrücklich.

## 5. Aktualisierungen

Die Skills werden zusammen mit der Dokumentation aktualisiert. Wenn eine neue Version erscheint, laden Sie das Archiv erneut herunter und bitten Sie den Assistenten, die Ordner der Skills vollständig zu ersetzen.

## Wenn etwas nicht funktioniert

Unter [Fehlerbehebung](troubleshooting.md) sind typische Symptome gesammelt. Die [erweiterte Einrichtung](advanced-setup.md) beschreibt das ganze Verfahren ausführlich — es ist genau die Seite, die Sie dem Assistenten übergeben haben, sodass Sie jeden Schritt von Hand ausführen und prüfen können, was er getan hat.
