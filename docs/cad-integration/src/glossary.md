# Glossary

| Term | Meaning |
|--------|----------|
| **CAD system** | The application into which the Toolbar is embedded. At a minimum it must allow third-party plugins to be registered, give them access to the currently open model, and provide a way to export geometry (through its own API or built-in export to STEP/Parasolid). |
| **CAM system** | The consumer of geometry. Loads the converted geometry from the CAD system. |
| **Add-in** | A complete package for integrating a CAD system with a CAM system. Consists of a Translator and a Toolbar. |
| **Translator** (`Translator`) | The EXE part of the Add-in. Performs installation/removal of the Add-in, and on request from the CAM system imports a CAD file into the CAM system's internal format. |
| **Toolbar** (`Toolbar`) | The part of the Add-in (usually a library) embedded in the CAD system as a button or a panel of buttons. When clicked, it converts and passes the current geometry to the CAM system. |
| **Add-in Wizard** (`AddinManager.dll`) | A CAM system UI tool for installing/removing Add-ins. It sends control commands to the Translator. |
| **`HostApplication`** | The string identifier of the CAD system (a tag of the same name in the Add-in XML file). The CAM system uses it to find the appropriate Add-in when geometry is passed from the Toolbar. |
| **Add-in XML file** (`<Translator>.xml`) | An XML file that describes the Add-in's metadata, supported formats, and commands. |
| **`CAMInfo.ini`** | A configuration file with certain CAM system parameters; it is created automatically by the Add-in Wizard. |
| **CheckLockToolbar** (`CheckLockToolbar.exe`) | A helper utility: checks whether a CAD system process is blocking installation/removal. |
| **STGeomFile.dll** | A library that provides access to the `ISTGeomFiler` interface — it contains methods for converting geometry into the CAM system's internal format (SGF). |
| **SGF** | Structured Geometry File. The CAM system's internal geometry format. |
| **`ISTGeomFiler`** (`sgf`) | The interface for managing an SGF file: open for writing (`StartFile`), close (`CloseFile`). Returned by the `CreateGeomFiler` function from STGeomFile.dll. |
| **`ISTGeomReceiver`** (`sgr`) | The main import interface: it receives geometry through a sequence of commands (surfaces, curves, faces, bodies, PMI). The same COM object as `ISTGeomFiler`. |
| **ComboModel / ComboSolid** | A pair of SGF objects for writing a closed body with stitching: the faces, edges, and vertices of a shell are assembled into a single solid (B-rep) without losing connectivity. |
| **PMI** | Product Manufacturing Information — manufacturing information annotations: dimensions, tolerances, threads, and so on. |
