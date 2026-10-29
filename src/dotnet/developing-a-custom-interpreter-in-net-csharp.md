# Entwicklung eines eigenen Interpreters in (.NET) C#

Zur Erstellung eigener G-Code-Interpreter auf Basis von .NET (C#) empfiehlt sich ein spezielles Werkzeug. Es befindet sich im Menü der Dienstprogramme und wird angezeigt, wenn in den Systemeinstellungen die Option **Show expert tools** eingeschaltet ist.

<img src="../../images/129932095/ShowExpertTools_En.png" alt="ShowExpertTools_En" height="400"><img src="../../images/129932095/CreateInterpreter_En.png" alt="CreateInterpreter_En" height="400">

Nach Auswahl des Menüpunkts **Create Interpreter** erscheint das zugehörige Fenster:

<img src="../../images/129932095/image2025-6-11_11-39-26.png" alt="image2025-6-11_11-39-26" width="555">

Darin sind nur wenige Parameter auszufüllen, aus denen die Vorlage für Ihren Interpreter vorbereitet wird:

- **Template** - Vorlage des Interpreters;
- **Name** - Name des zu entwickelnden Interpreters;

> [!WARNING]
> *Aus diesem Namen wird ein gleichnamiger Ordner erstellt, in dem alle Quelldateien des neuen Interpreters liegen.*

- **Folder** - Verzeichnis, in dem der Ordner Ihres Interpreters angelegt wird (der Wert kann von Hand eingegeben oder über den Dialog zur Ordnerauswahl mit der Schaltfläche <img src="../../images/129932095/FileDialogBtn.png" alt="FileDialogBtn" height="22"> gewählt werden).
- **File** - vollständiger Pfad zur Einstellungsdatei des übergeordneten Interpreters (\*.snci), von dem Sie erben möchten (**optionales Feld**).

Nach dem Ausfüllen aller nötigen Parameter klicken Sie auf &lt;**Ok**>. Daraufhin wird im angegebenen Verzeichnis ein Ordner mit dem Namen des Interpreters erstellt und sofort in Visual Studio Code geöffnet (sofern der entsprechende Schalter zu diesem Zeitpunkt eingeschaltet war).

> [!NOTE]
> [Visual Studio Code](https://code.visualstudio.com/Download) muss vorher auf dem Computer installiert sein.
