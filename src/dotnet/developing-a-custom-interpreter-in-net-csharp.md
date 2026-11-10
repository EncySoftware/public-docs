# Entwicklung eines eigenen Interpreters in (.NET) C#

Zur Erstellung eigener G-Code-Interpreter auf Basis von .NET (C#) empfiehlt sich ein spezielles Werkzeug. Es ist der Eintrag **Interpreter erstellen** in der Liste **Zubehör**.

<img src="../../images/129932095/CreateInterpreter_En.png" alt="CreateInterpreter_En" height="400">

Nach Auswahl des Eintrags **Interpreter erstellen** erscheint das zugehörige Fenster:

<img src="../../images/129932095/image2025-6-11_11-39-26.png" alt="image2025-6-11_11-39-26" width="555">

Darin sind nur wenige Parameter auszufüllen, aus denen die Vorlage für Ihren Interpreter vorbereitet wird:

- **Vorlage** - Vorlage des Interpreters;
- **Name** - Name des zu entwickelnden Interpreters;

> [!WARNING]
> *Aus diesem Namen wird ein gleichnamiger Ordner erstellt, in dem alle Quelldateien des neuen Interpreters liegen.*

- **Ordner** - Verzeichnis, in dem der Ordner Ihres Interpreters angelegt wird (der Wert kann von Hand eingegeben oder über den Dialog zur Ordnerauswahl mit der Schaltfläche <img src="../../images/129932095/FileDialogBtn.png" alt="FileDialogBtn" height="22"> gewählt werden).
- **Datei** - vollständiger Pfad zur Einstellungsdatei des Eltern-Interpreters (\*.snci), von dem Sie erben möchten (**optionales Feld**).
- **Starten Sie in Visual Studio Code** - Schalter: Ist er eingeschaltet, wird der Ordner des Interpreters gleich nach dem Erstellen in Visual Studio Code geöffnet.

Nach dem Ausfüllen aller nötigen Parameter klicken Sie auf &lt;**OK**&gt;. Daraufhin wird im angegebenen Verzeichnis ein Ordner mit dem Namen des Interpreters erstellt und sofort in Visual Studio Code geöffnet (sofern der Schalter **Starten Sie in Visual Studio Code** zu diesem Zeitpunkt eingeschaltet war).

> [!NOTE]
> [Visual Studio Code](https://code.visualstudio.com/Download) muss vorher auf dem Computer installiert sein.

## Was nach dem Erstellen zu korrigieren ist

Der Eintrag **Interpreter erstellen** kopiert die Vorlage und füllt möglicherweise nicht alles aus. Bevor Sie den Interpreter bauen und das Debuggen starten (`F5`), prüfen Sie die folgenden Felder und korrigieren Sie diejenigen, die falsch ausgefüllt sind. Sind alle Felder bereits korrekt, überspringen Sie diesen Schritt.

- Die Version des Pakets `EncySoftware.NCInterpreterSDK.Net` in der Datei `*.csproj`: Steht dort eine Vorabversion (mit einer Endung wie `-dev` oder `-rc`) oder eine Version einer älteren Hauptversion, ersetzen Sie sie durch die veröffentlichte Version für Ihre Produktversion, wie im Abschnitt [Produktversionen](../ai-assisted-development/dotnet-workflow.md#produktversionen) beschrieben; sonst lässt sich das Projekt möglicherweise nicht bauen.
- Das Feld `ID` in der Datei `*.snci`: Ist es mit Nullen gefüllt, tragen Sie eine neue GUID ein.
- Bei einem abgeleiteten Interpreter der Verweis auf den Eltern-Interpreter: In `ParentID` muss die `ID` des Eltern-Interpreters stehen und in `ParentFileName` der Name seiner Datei `*.snci`; ohne ihn wird der Eltern-Interpreter nicht geladen. Steht in `ParentID` die `LibraryID` des Eltern-Interpreters oder ist `ParentFileName` leer, korrigieren Sie beide Felder.

Einzelheiten im Abschnitt [Womit beginnen](../ai-assisted-development/dotnet-workflow.md#womit-beginnen) des .NET-Arbeitsablaufs.
