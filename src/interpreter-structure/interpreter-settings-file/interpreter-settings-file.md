# Interpreter settings file

The settings file has the SNCI extension (**S**ystem **N**umerical **C**ontrol **I**nterpreter) and the XML format. Its elements are described below. Required parameters are marked in the corresponding column.

**Description of the SNCI file elements**

<table>
<thead>
<tr><th>Element name</th><th>Field format</th><th>Description</th><th>Required</th></tr>
</thead>
<tbody>
<tr><td><strong>NCInterpreter</strong></td><td>Tag</td><td>Root element</td><td>*</td></tr>
<tr><td><strong>CNCSystem</strong></td><td>String</td><td>Controller/machine name</td><td></td></tr>
<tr><td><strong>MachineType</strong></td><td>String</td><td><p>Machine type, options:</p><ul><li><strong>Lathe</strong> — lathe</li><li><strong>Mill </strong>— milling machine</li><li><strong>TurnMill </strong>— mill-turn machine</li><li><strong>Robots </strong>— robot</li><li><strong>WireEDM </strong>— wire EDM machine</li></ul></td><td></td></tr>
<tr><td><strong>UseGeomCLData</strong></td><td>Boolean</td><td><p>Sets the flag of using the interface for constructing the tool path in geometric axes.</p><p><strong>True</strong> — the <a href="../../g-code-interpretation/sprutcam-interfaces/basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md"><strong>INCT_GeomCLData</strong></a> interface is passed from the CAM system to the interpreter to form the tool path.</p><p><strong>False</strong> — the <a href="../../g-code-interpretation/sprutcam-interfaces/basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md"><strong>INCT_CLData</strong></a> interface is passed from the CAM system to the interpreter to form the tool path.</p><p>The default value is <strong>False</strong>.</p></td><td></td></tr>
<tr><td><strong>Date</strong></td><td>Date</td><td>Interpreter date in the <strong>dd.mm.yyyy</strong> format</td><td></td></tr>
<tr><td><strong>Authors</strong></td><td>String</td><td>Developer(s)</td><td></td></tr>
<tr><td><strong>Company</strong></td><td>String</td><td>Company</td><td></td></tr>
<tr><td><strong>Description</strong></td><td>String</td><td>Description</td><td></td></tr>
<tr><td><strong>Version</strong></td><td>Number</td><td>Version</td><td>*</td></tr>
<tr><td><strong>ID</strong></td><td>GUID</td><td>Interpreter identifier (must be unique)</td><td>*</td></tr>
<tr><td><strong>LibraryID</strong></td><td>GUID</td><td>Program library identifier (must be unique)</td><td>*</td></tr>
<tr><td><strong>LibraryFileName_Net</strong></td><td>String</td><td>Link to the program library for the <strong>.NET</strong> platform</td><td>**</td></tr>
<tr><td><strong>NetNamespaceClass</strong></td><td>String</td><td>Namespace and name of the class implementing the interpreter (if the <strong>LibraryFileName_Net</strong> field is filled in)</td><td>***</td></tr>
<tr><td><strong>LibraryFileName_x64</strong></td><td>String</td><td>Link to the native <strong>x64</strong> program library (used if the <strong>LibraryFileName_Net</strong> field is not filled in)</td><td>**</td></tr>
<tr><td><strong>ParentID</strong></td><td>GUID</td><td>Parent interpreter identifier (the <strong>ID</strong> field in the parent's SNCI file)</td><td>*</td></tr>
<tr><td><strong>ParentFileName</strong></td><td>String</td><td>Link to the parent interpreter settings file (SNCI file)</td><td>*</td></tr>
<tr><td><strong>FileExtension</strong></td><td>String</td><td>Extension of the NC program files</td><td>*</td></tr>
<tr><td><strong>Registers</strong></td><td>Tag</td><td>List of interpreter registers</td><td>*</td></tr>
</tbody>
</table>

\* — required field;

\*\* — either the **LibraryFileName_Net** or the **LibraryFileName\_x64** field must be filled in;

\*\*\* — the field must be filled in if the **LibraryFileName_Net** field is filled in.

**Description of each element of the register list (Registers):**

<table>
<thead>
<tr><th>Element name</th><th>Field format</th><th>Description</th></tr>
</thead>
<tbody>
<tr><td><strong>Address</strong></td><td>String</td><td>Register address</td></tr>
<tr><td><strong>Name</strong></td><td>String</td><td>Register name</td></tr>
<tr><td><strong>Id</strong></td><td>String</td><td>Register identifier</td></tr>
<tr><td><strong>Comment</strong></td><td>String</td><td>Comment</td></tr>
<tr><td><strong>AddrOnly</strong></td><td>String</td><td><p>Possible values:</p><ul><li><strong>aoValue</strong> — the NC program word consists of an address and a value only</li><li><strong>aoAddr</strong> — the NC program word consists of an address only</li><li><strong>aoBoth</strong> — the NC program word may consist either of an address only or of an address and a value</li></ul></td></tr>
<tr><td><strong>Sign</strong></td><td>Integer</td><td><p>Value sign:</p><ul><li>0 — unsigned</li><li>1 — '-' only</li><li>2 — '+' and '-'</li></ul></td></tr>
<tr><td><strong>NumeralsBeforePoint.Count</strong></td><td>Integer</td><td>Digits before the point</td></tr>
<tr><td><strong>NumeralsBeforePoint.Zeros</strong></td><td>Boolean</td><td>Leading zeros</td></tr>
<tr><td><strong>DecimalPoint</strong></td><td>Integer</td><td><p>Decimal point:</p><ul><li>0 — no '.'</li><li>1 — '.'</li><li>2 — always '.'</li></ul></td></tr>
<tr><td><strong>NumeralsAfterPoint.Count</strong></td><td>Integer</td><td>Digits after the point</td></tr>
<tr><td><strong>NumeralsAfterPoint.Zeros</strong></td><td>Boolean</td><td>Trailing zeros</td></tr>
<tr><td><strong>Scale</strong></td><td>Number</td><td>Scale</td></tr>
<tr><td><strong>Modal</strong></td><td>Boolean</td><td>Register modality flag</td></tr>
<tr><td><strong>ModalGroupList</strong></td><td>List of values</td><td>List of values the register can take</td></tr>
</tbody>
</table>

The **Version** field is reserved for future use.

The important elements of the interpreter settings file are: its own identifier (**ID**), the identifier (**LibraryID**) and the link to the .NET/x64 program library files (**LibraryFileName\_\***), the identifier (**ParentID**) and the link to the parent interpreter (**ParentFileName**). The identifiers of the settings file and the program library must be unique (see the article on GUID: [Globally Unique Identifier](https://wikipedia.org/wiki/GUID)).

The **LibraryFileName\_\*** field must point to the program library files relative to the folder where the SNCI file is located. It is recommended to place the program library file in the folder with the SNCI file.

There are two ways to connect a program library to the CAM system:

1. The program library is developed for the .NET platform (for example, in C#).\
   In this case, fill in the **LibraryFileName_Net** and **NetNamespaceClass** fields, where:
   - **LibraryFileName_Net** — link to the program library.
   - **NetNamespaceClass** — namespace and class implementing the interface of interaction with the interpreter. Format: Namespace.Class, for example: Sample.Interpreter.

2. The program library is native (written in Delphi, C\+\+, etc.)

   In this case, the **LibraryFileName_x64** field (link to the x64 program library) must be filled in. The x64 version of the program library must be named using the "**64**" suffix. For example: **Sample_x64.dll** or **Sample_Win64.dll**, where "Sample" is the name of the program library.

If the interpreter does not inherit from another interpreter, the parent fields are filled in with empty values:

**&lt;ParentID>**\{00000000-0000-0000-0000-000000000000}**&lt;/ParentID>**

**&lt;ParentFileName/>**

The **FileExtension** field is reserved for future use.

The **Registers** field contains the list of registers for automatic extraction of words from the NC program text. The order of NC program block translation is described in the [following article.](../../g-code-interpretation/translation-and-interpretation/translation-and-interpretation-g-code-based-program.md) The register list in the interpreter settings file may be left empty: it [will be obtained from the interpreter program library](../../g-code-interpretation/interpreter-loading-and-initialization/interpreter-loading-and-initialization.md); however, the **&lt;Registers/>** tag must be present.

The use of the interpreter settings file is described in the [G-code based program interpretation](../../g-code-interpretation/g-code-based-program-interpretation.md) section.

**Example of the interpreter settings file for a native library (x64):**

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

Download the example [Sample.snci](../../../images/129931392/sample.snci).
