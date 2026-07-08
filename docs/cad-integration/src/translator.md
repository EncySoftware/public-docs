# Translator

A single entry point for commands from the Add-in Wizard and for the import command from the CAM system. A standalone process, an executable `.exe` file. The implementation language is arbitrary; most commonly Delphi, C++, or C# (.NET Framework).

**Command-line contract.** `<Translator>.exe` accepts one of four argument formats:

| Arguments | Semantics |
|-----------|-----------|
| `IsInstalled` | Check whether installation is possible — namely, that the CAD system is present on the machine and all conditions for installation are met. On success, return 10. Otherwise the Add-in Wizard will block the ability to install. |
| `Install` | The Translator performs the operations needed to make a Toolbar with a button appear in the CAD system. On success, return 10. Otherwise the Add-in Wizard will show an error. |
| `UnInstall` | Remove the Toolbar from the CAD system. Same as the command above; as a result, the button should disappear from the CAD system. On success, return 10. |
| `$(InFile) $(OutFile)` | Import of a CAD file. The Translator launches the CAD system (or connects to an already running one), creates a new document and loads `InFile` into it, then imports all the geometry (usually by means of the Toolbar) and produces the `OutFile`. For details, see [Importing a CAD file into a CAM system](import-cad-file.md). |

The command argument names (`IsInstalled`, `Install`, `UnInstall`, and the `<In> <Out>` format) are specified in the Add-in XML file through the tags `CommandLineIsAppInst`, `CmdLnInstall`, `CmdLnUnInstall`, `CommandLine`. The names may differ in each specific Add-in — the Add-in Wizard and the CAM system read them from the XML.

**Return codes.**

| Code | Meaning |
|-----|----------|
| `0` | False — the operation was not performed (the CAM system will show an error window). |
| `10` | True — the operation completed successfully. |
