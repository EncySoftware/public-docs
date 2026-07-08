# Toolbar

The Toolbar is a button in the CAD system that, when activated, transfers geometry to the CAM system.
Depending on the structure of the CAD system, the Toolbar can have a different appearance and a different location — in a menu, in a shared panel, in a separate panel, and so on.

All the data required for the Toolbar to work is located in two files:

- **`CAMInfo.ini`** (see [The CAMInfo.ini file](caminfo-ini.md)) — data for filling in names, tooltips, as well as the path to the CAM system and the settings files;
- **The add-in XML file** (see [The add-in XML file](xml-descriptor.md)) — the value of the `HostApplication` tag, by which the CAM system links the transferred geometry to the correct importer.

Since in some cases the Toolbar application may reside in a different directory, when installing you must provide access to the folder with these files.

Additionally, you can use the CheckLockToolbar utility (see [The CheckLockToolbar utility](checklocktoolbar.md)).

**Algorithm on button press.**

1. **Save the model file** in the CAD system's native format (hereinafter — the CAD system project file).
   - If the model file did not exist (this is a new project), you need to show a "Save As…" dialog. In most cases this happens automatically when the corresponding API method is called; if not, you must implement this part yourself.
   - If the user declines to save, you must abort execution.
2. **Convert the file** into one of the CAM system's internal formats. If possible, it is preferable to use STEP or Parasolid; otherwise, build SGF (see [Geometry import into the CAM system](geometry-import.md)).
3. **Launch the CAM system** with command-line parameters (see the example call below).

**Example of a CAM system call.**

```csharp
void LaunchCAM(string fileName, string originalFileName)
{
    if (File.Exists(fCAMPath))
    {
        string par =
            " -EXTIMPORT -HOST \"" + fHost + "\"" +
            " -ORIGINALFILEPATH \"" + originalFileName + "\"" +
            " -DELETEIMPORTFILE \"" + fileName + "\"";

        RunAs(fCAMPath, par, false, SW_SHOW, false);
    }
}
```

This example uses the following variables:

| Variable | Description |
|------------|----------|
| `fCAMPath` | The full path to the CAM system executable. Read from the `CAMInfo.ini` file (the `CAMPath` parameter). |
| `fHost` | The value of the `HostApplication` tag from the add-in XML file. This value is unlikely to change, so it can be hard-coded in the source — but you need to keep that in mind. |
| `originalFileName` | The CAD system project file. |
| `fileName` | The converted file. |

The `RunAs` function is from the `LockProcManager` unit (see [The CheckLockToolbar utility](checklocktoolbar.md)).
