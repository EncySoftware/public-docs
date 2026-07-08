# Distribution files

All Add-ins are stored in the CAM system's standard directory. This is the only place from which Add-ins are managed and interacted with — it also holds the files required for the Toolbar to work.

**Path template.**

```
%ProgramData%\<Company_name>\<Product_name>\<Product_version>\AddIns\<CAD_system_name>\
```

For example, for the KOMPAS CAD system:

```
C:\ProgramData\<Company_name>\<Product_name>\<Product_version>\AddIns\Kompas\
```

The files of each Add-in are stored in a separate subfolder named after the CAD system. The Add-in wizard scans all `AddIns/` subfolders and offers them for installation.

**Example of an Add-in's file structure.**

```
AddIns/
  <CAD>/
    <Translator>.exe
    <Translator>.bmp
    <Translator>.xml
    STGeomFile.dll
    CAMInfo.ini
    <ToolbarFiles>
```

**Required folder contents.** Three files with the **same name** and different extensions; without them the Add-in wizard will not display this add-in:

| File | Purpose |
|------|-----------|
| `<Translator>.exe` | The Translator executable (see [Translator](translator.md)). |
| `<Translator>.bmp` | A 16×16 icon shown in the Add-in wizard UI. |
| `<Translator>.xml` | The Add-in XML file (see [Add-in XML file](xml-descriptor.md)). |

**Accompanying files.**

| File | Purpose |
|------|-----------|
| `CAMInfo.ini` | Created automatically by the Add-in wizard. Contains the current CAM system settings (see [CAMInfo.ini file](caminfo-ini.md)). |
| Toolbar file (extension depends on the CAD) | The plugin file that converts the CAD system's geometry and embeds itself into its toolbar (see [Toolbar](toolbar-plugin.md)). |
| CAD system UI resources | Button icons, fonts, panel configuration XML/CUIX files — the format depends on the CAD. Usually placed in a subfolder. |

Any other files (if present) should be placed in a separate subfolder (for example, `ToolbarFiles/`) — this makes the structure easier to read and does not interfere with the Add-in wizard finding the required files.
