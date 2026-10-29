# Interpreter-Einstellungsdatei

Die Einstellungsdatei hat die Erweiterung SNCI (**S**ystem **N**umerical **C**ontrol **I**nterpreter) und das Format XML. Ihre Elemente sind unten beschrieben. Pflichtparameter sind in der entsprechenden Spalte gekennzeichnet.

**Beschreibung der Elemente der SNCI-Datei**

<table>
<thead>
<tr><th>Name des Elements</th><th>Feldformat</th><th>Beschreibung</th><th>Pflichtfeld</th></tr>
</thead>
<tbody>
<tr><td><strong>NCInterpreter</strong></td><td>Tag</td><td>Wurzelelement</td><td>*</td></tr>
<tr><td><strong>CNCSystem</strong></td><td>Zeichenkette</td><td>Name der Steuerung bzw. der Maschine</td><td></td></tr>
<tr><td><strong>MachineType</strong></td><td>Zeichenkette</td><td><p>Maschinentyp, mögliche Werte:</p><ul><li><strong>Lathe</strong> - Drehmaschine</li><li><strong>Mill</strong> - Fräsmaschine</li><li><strong>TurnMill</strong> - Dreh-Fräsmaschine</li><li><strong>Robots</strong> - Roboter</li><li><strong>WireEDM</strong> - Drahterodiermaschine</li></ul></td><td></td></tr>
<tr><td><strong>UseGeomCLData</strong></td><td>boolesch</td><td><p>Legt fest, ob die Schnittstelle zur Bildung des Werkzeugwegs in geometrischen Achsen verwendet wird.</p><p><strong>True</strong> - zur Bildung des Werkzeugwegs übergibt das CAM-System dem Interpreter die Schnittstelle <a href="../../g-code-interpretation/sprutcam-interfaces/basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md"><strong>INCT_GeomCLData</strong></a>.</p><p><strong>False</strong> - zur Bildung des Werkzeugwegs übergibt das CAM-System dem Interpreter die Schnittstelle <a href="../../g-code-interpretation/sprutcam-interfaces/basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md"><strong>INCT_CLData</strong></a>.</p><p>Standardwert ist <strong>False</strong>.</p></td><td></td></tr>
<tr><td><strong>Date</strong></td><td>Datum</td><td>Datum des Interpreters im Format <strong>dd.mm.yyyy</strong></td><td></td></tr>
<tr><td><strong>Authors</strong></td><td>Zeichenkette</td><td>Entwickler</td><td></td></tr>
<tr><td><strong>Company</strong></td><td>Zeichenkette</td><td>Firma</td><td></td></tr>
<tr><td><strong>Description</strong></td><td>Zeichenkette</td><td>Beschreibung</td><td></td></tr>
<tr><td><strong>Version</strong></td><td>Zahl</td><td>Version</td><td>*</td></tr>
<tr><td><strong>ID</strong></td><td>GUID</td><td>Kennung des Interpreters (muss eindeutig sein)</td><td>*</td></tr>
<tr><td><strong>LibraryID</strong></td><td>GUID</td><td>Kennung der Programmbibliothek (muss eindeutig sein)</td><td>*</td></tr>
<tr><td><strong>LibraryFileName_Net</strong></td><td>Zeichenkette</td><td>Verweis auf die Programmbibliothek für die Plattform <strong>.NET</strong></td><td>**</td></tr>
<tr><td><strong>NetNamespaceClass</strong></td><td>Zeichenkette</td><td>Namensraum und Name der Klasse, die den Interpreter implementiert (wenn das Feld <strong>LibraryFileName_Net</strong> ausgefüllt ist)</td><td>***</td></tr>
<tr><td><strong>LibraryFileName_x64</strong></td><td>Zeichenkette</td><td>Verweis auf die native Programmbibliothek in der Version <strong>x64</strong> (wird verwendet, wenn das Feld <strong>LibraryFileName_Net</strong> nicht ausgefüllt ist)</td><td>**</td></tr>
<tr><td><strong>ParentID</strong></td><td>GUID</td><td>Kennung des übergeordneten Interpreters (Feld <strong>ID</strong> in dessen SNCI-Datei)</td><td>*</td></tr>
<tr><td><strong>ParentFileName</strong></td><td>Zeichenkette</td><td>Verweis auf die Einstellungsdatei des übergeordneten Interpreters (SNCI-Datei)</td><td>*</td></tr>
<tr><td><strong>FileExtension</strong></td><td>Zeichenkette</td><td>Erweiterung der Dateien mit dem NC-Programm</td><td>*</td></tr>
<tr><td><strong>Registers</strong></td><td>Tag</td><td>Liste der Register des Interpreters</td><td>*</td></tr>
</tbody>
</table>

\* - Pflichtfeld;

\*\* - entweder das Feld **LibraryFileName_Net** oder das Feld **LibraryFileName\_x64** muss ausgefüllt sein;

\*\*\* - das Feld muss ausgefüllt sein, wenn das Feld **LibraryFileName_Net** ausgefüllt ist.

**Beschreibung der Elemente der Registerliste (Registers):**

<table>
<thead>
<tr><th>Name des Elements</th><th>Feldformat</th><th>Beschreibung</th></tr>
</thead>
<tbody>
<tr><td><strong>Address</strong></td><td>Zeichenkette</td><td>Adresse des Registers</td></tr>
<tr><td><strong>Name</strong></td><td>Zeichenkette</td><td>Name des Registers</td></tr>
<tr><td><strong>Id</strong></td><td>Zeichenkette</td><td>Kennung des Registers</td></tr>
<tr><td><strong>Comment</strong></td><td>Zeichenkette</td><td>Kommentar</td></tr>
<tr><td><strong>AddrOnly</strong></td><td>Zeichenkette</td><td><p>Mögliche Werte:</p><ul><li><strong>aoValue</strong> - das Wort des NC-Programms besteht nur aus Adresse und Wert</li><li><strong>aoAddr</strong> - das Wort des NC-Programms besteht nur aus der Adresse</li><li><strong>aoBoth</strong> - das Wort des NC-Programms kann entweder nur aus der Adresse oder aus Adresse und Wert bestehen</li></ul></td></tr>
<tr><td><strong>Sign</strong></td><td>Ganzzahl</td><td><p>Vorzeichen des Werts:</p><ul><li>0 - ohne Vorzeichen</li><li>1 - nur '-'</li><li>2 - '+' und '-'</li></ul></td></tr>
<tr><td><strong>NumeralsBeforePoint.Count</strong></td><td>Ganzzahl</td><td>Stellen vor dem Punkt</td></tr>
<tr><td><strong>NumeralsBeforePoint.Zeros</strong></td><td>boolesch</td><td>Führende Nullen vorhanden</td></tr>
<tr><td><strong>DecimalPoint</strong></td><td>Ganzzahl</td><td><p>Dezimalpunkt:</p><ul><li>0 - ohne '.'</li><li>1 - '.'</li><li>2 - immer '.'</li></ul></td></tr>
<tr><td><strong>NumeralsAfterPoint.Count</strong></td><td>Ganzzahl</td><td>Stellen nach dem Punkt</td></tr>
<tr><td><strong>NumeralsAfterPoint.Zeros</strong></td><td>boolesch</td><td>Nachgestellte Nullen</td></tr>
<tr><td><strong>Scale</strong></td><td>Zahl</td><td>Maßstab</td></tr>
<tr><td><strong>Modal</strong></td><td>boolesch</td><td>Kennzeichen, ob das Register modal ist</td></tr>
<tr><td><strong>ModalGroupList</strong></td><td>Werteliste</td><td>Liste der Werte, die das Register annehmen kann</td></tr>
</tbody>
</table>

Das Feld **Version** ist für die künftige Verwendung reserviert.

Wichtige Elemente der Einstellungsdatei des Interpreters sind: seine eigene Kennung (**ID**), die Kennung (**LibraryID**) und der Verweis auf die Dateien der Programmbibliothek in der Version .NET/x64 (**LibraryFileName\_\***), die Kennung (**ParentID**) und der Verweis auf den übergeordneten Interpreter (**ParentFileName**). Die Kennungen der Einstellungsdatei und der Programmbibliothek müssen eindeutig sein (siehe den Artikel über GUID: [Globally Unique Identifier](https://wikipedia.org/wiki/GUID)).

Das Feld **LibraryFileName\_\*** muss auf die Dateien der Programmbibliothek relativ zum Verzeichnis der SNCI-Datei verweisen. Es empfiehlt sich, die Datei der Programmbibliothek im Verzeichnis der SNCI-Datei abzulegen.

Die Programmbibliothek kann auf zwei Arten an das CAM-System angebunden werden:

1. Die Programmbibliothek ist für die Plattform .NET entwickelt (zum Beispiel in C#).\
   In diesem Fall müssen die Felder **LibraryFileName_Net** und **NetNamespaceClass** ausgefüllt werden:
   - **LibraryFileName_Net** - Verweis auf die Programmbibliothek.
   - **NetNamespaceClass** - Namensraum und Klasse, die die Schnittstelle für das Zusammenwirken mit dem Interpreter implementiert. Format: Namespace.Class, zum Beispiel: Sample.Interpreter.

2. Die Programmbibliothek ist nativ (in Delphi, C\+\+ usw. geschrieben).

   In diesem Fall muss das Feld **LibraryFileName_x64** ausgefüllt werden (Verweis auf die Programmbibliothek x64). Der Name der x64-Version der Programmbibliothek muss die Endung „**64**“ tragen. Zum Beispiel: **Sample_x64.dll** oder **Sample_Win64.dll**, wobei „Sample“ der Name der Programmbibliothek ist.

Ist der Interpreter nicht von einem anderen Interpreter abgeleitet, werden die Felder des übergeordneten Interpreters mit leeren Werten gefüllt:

**&lt;ParentID>**\{00000000-0000-0000-0000-000000000000}**&lt;/ParentID>**

**&lt;ParentFileName/>**

Das Feld **FileExtension** ist für die künftige Verwendung reserviert.

Im Feld **Registers** steht die Liste der Register für das automatische Heraustrennen der Wörter aus dem NC-Programm. Wie ein Satz des NC-Programms übersetzt wird, ist im [folgenden Artikel](../../g-code-interpretation/translation-and-interpretation/translation-and-interpretation-g-code-based-program.md) beschrieben. Die Liste der Register in der Einstellungsdatei des Interpreters darf leer bleiben, sie wird dann [von der Programmbibliothek des Interpreters bezogen](../../g-code-interpretation/interpreter-loading-and-initialization/interpreter-loading-and-initialization.md); das Tag **&lt;Registers/>** muss trotzdem vorhanden sein.

Die Verwendung der Einstellungsdatei des Interpreters ist im Abschnitt [Ablauf der Interpretation des NC-Programms](../../g-code-interpretation/g-code-based-program-interpretation.md) beschrieben.

**Beispiel einer Einstellungsdatei des Interpreters für eine native Bibliothek (x64):**

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<NCInterpreter>
 <CNCSystem>Sample CNC (mill)</CNCSystem>
 <MachineType>Mill</MachineType>
 <Date>01.01.2019</Date>
 <Authors>Headquarters Team</Authors>
 <Company>Headquarters</Company>
 <Description>Interpreter for Sample CNC</Description>
 <Version>1</Version>
 <ID>{79B1410C-67D5-42B6-867B-A3BF30AB3D8A}</ID>
 <LibraryID>{80F754D9-EE7B-47CF-A802-A9424D9F6749}</LibraryID>
 <LibraryFileName_x64>Sample_x64.dll</LibraryFileName_x64>
 <ParentID>{00000000-0000-0000-0000-000000000000}</ParentID>
 <ParentFileName/>
 <FileExtension>*.cnc</FileExtension>
 <Registers/>
</NCInterpreter>
```

Beispiel [Sample.snci](../../../images/129931392/sample.snci) herunterladen.
