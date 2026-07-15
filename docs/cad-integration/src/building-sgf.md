# Building the SGF file

This is the **entry point** of geometry import — the moment when control is handed to the Add-in from outside. There are two possible scenarios (see [Interaction scenarios](scenarios.md)):

- **clicking a Toolbar button** in the CAD system — the user exports the open model ([Import from a CAD system into a CAM system](import-from-cad.md));
- **a call from a translator or from the CAM system** when importing a CAD file — the Add-in is launched on an already loaded model ([Import a CAD file into a CAM system](import-cad-file.md)).

In both cases the input is the same: the **current model of the CAD system** (what to save) and the **path to the output file** (where). From there the Add-in builds the SGF file following a single scheme:

1. connect to the import library (see [Connecting STGeomFile.dll](connecting-stgeomfile.md));
2. traverse the CAD model top-down and write its geometry through `sgr` (see the sections [Curves and points](curves-and-points.md)–[PMI](pmi.md));
3. release the interfaces and unload the library (`FreeLibrary`).

## Global import settings

Right after `StartFile`, before geometry is written, the **global import settings** are specified. They apply to the whole file and are set once through the `ISTGeomReceiver` interface (`sgr`, see [Import interfaces](import-interfaces.md)):

| Method | Description |
|-------|----------|
| `SetModelUnits(Units: TST_LinearMeasure; MultScale: STFloat)` | Set the model units of measurement (`lm_Millimetre`, `lm_Centimetre`, `lm_Decimetre`, `lm_Metre`, `lm_Inch`, `lm_Foot`). `MultScale` is a scale factor. The defaults are `lm_Millimetre` and `MultScale = 1`. |
| `SetArcToler(Value: STFloat)` | Set the arc approximation tolerance. The default is `0.001` (in model units). |
| `SetImportOption(OptionType: TSTImportOption; OptionValue: boolean)` | Enable/disable import option `OptionType` (value `OptionValue`). The `TSTImportOption` values and their purpose are in the table below. |

The `TSTImportOption` options control the import of face loops — primarily for **inverted** (reversed-normal) and **cyclic** (parameter-periodic) surfaces. **Usually there is no need to change them:** the default values are suitable for most cases, and the options are touched only for specific problems with orientation or with reconstructing loops. Possible values:

| `TSTImportOption` | Purpose | Default |
|-------------------|------------|--------------|
| `ioCreateRectLoops` | Reconstruct the outer loop for a cyclic face if it is not given explicitly: a rectangular (outer) loop is added over the parametric region of the surface. | off |
| `ioInverse3dLoopsForInversedFaces` | Reverse the traversal direction of 3D loops (loops made of spatial edges) for faces with an inverted surface — so that the "face body on the left" rule is preserved. | on |
| `ioInverse2dLoopsForInversedFaces` | The same, but for 2D loops specified in the surface UV parameters. | off |

## SGF header metadata

The SGF file starts with a header: a signature, the format version and a JSON metadata block. The header as a whole is built by the library at `CloseFile`; the Add-in only extends the JSON block with information about the source — which file, which CAD system and which version of the Add-in produced the SGF. The CAM system shows this information to the user — for example, the name of the source model. The `originalFileName` and `hostName` keys are **mandatory**; the rest are filled in when possible.

The metadata is written through `sgr.Header.MetaWriter` (the `ISGFMetaWriter` interface) strictly between `StartFile` and `CloseFile` — outside this window `sgr.Header` returns `null`. The root JSON object is owned by the library: pairs are added right away, without opening the root, and every `BeginObject`/`BeginArray` is closed by its paired `EndObject`/`EndArray` (just like the geometric `Start…`/`Close…`). The methods return a `boolean` — the success status:

| Method | Description |
|-------|----------|
| `AddStrPair(AKey, AValue: string)` | Add a "key — string value" pair. Similarly `AddIntPair` (`integer`), `AddFltPair` (`STFloat`), `AddBolPair` (`boolean`). |
| `BeginObject(ObjectID: string)` / `EndObject()` | Open / close a nested object with the given key. |
| `BeginArray(ArrayID: string)` / `EndArray()` | Open / close a nested array with the given key. |
| `AddStrValue(AValue: string)` | Add a value to the open array. Similarly `AddIntValue`, `AddFltValue`, `AddBolValue`. |

The standard set of keys is given in the table. **The names in the table are the keys**: the CAM system reads the values exactly by these names, so write them exactly as specified, without renaming. Custom keys may be added — the format version does not change because of that, and unknown keys are ignored on reading.

| Key | Contents | Mandatory |
|------|------------|----------------|
| `originalFileName` | The full path to the CAD system project file (see [Toolbar](toolbar-plugin.md)). | **mandatory** |
| `hostName` | The value of the `HostApplication` tag — the string identifier of the CAD system by which the CAM system finds the Add-in (see [Add-in XML file](xml-descriptor.md) and [Glossary](glossary.md)). | **mandatory** |
| `sourceApp` | A nested object: `name` — the name of the CAD system executable, `processFileName` — its full path, `version` — the CAD system version. | optional |
| `toolbarLibrary` | A nested object: `name`, `path`, `version` — the name, path and version of the Add-in module. | optional |

The `_generated` key is reserved: this section (`timeUTC` — the file creation time, `library` — the import library version, `processFileName` — the path of the process that produced the file) is appended by the library itself at `CloseFile`.

A writing example (the method is called from [the import entry-point example](#example-the-import-entry-point)) and the resulting JSON block:

```csharp
// Header metadata: the source file, the CAD system, the Add-in module
void WriteHeaderMeta(CADDocument doc)
{
    var mw = sgr.Header.MetaWriter;
    mw.AddStrPair("originalFileName", doc.FileName);
    mw.AddStrPair("hostName", fHost); // the HostApplication tag from the Add-in XML file
    mw.BeginObject("sourceApp");
        mw.AddStrPair("name", "mycad.exe");
        mw.AddStrPair("processFileName", cadExePath);
        mw.AddStrPair("version", cadVersion);
    mw.EndObject();
    mw.BeginObject("toolbarLibrary");
        mw.AddStrPair("name", "MyCADToolbar.dll");
        mw.AddStrPair("path", toolbarPath);
        mw.AddStrPair("version", toolbarVersion);
    mw.EndObject();
}
```

```json
{
  "originalFileName": "C:\\Models\\part.mcad",
  "hostName": "MyCAD",
  "sourceApp":      { "name": "mycad.exe", "processFileName": "C:\\MyCAD\\mycad.exe", "version": "3.2.1" },
  "toolbarLibrary": { "name": "MyCADToolbar.dll", "path": "C:\\MyCAD\\Addins\\MyCADToolbar.dll", "version": "1.4.0.12" },
  "_generated":     { "timeUTC": "2026-07-15T10:30:00Z", "library": "STGeomFile 1.0.0.0", "processFileName": "C:\\MyCAD\\mycad.exe" }
}
```

## Example: the import entry point

```csharp
// The import entry point. Input: the current model of the CAD system and the path to the output SGF file.
bool ExportToSGF(CADDocument doc, string outFilePath)
{
    if (!ConnectToGeomFiler(GetLibraryPath()))
        return false;

    bool ok = false;
    try
    {
        sgf.StartFile(outFilePath);         
        try
        {
            // header metadata (see "SGF header metadata")
            WriteHeaderMeta(doc);

            // sgr.SetModelUnits(TST_LinearMeasure.lm_Metre, 1.0);
            // sgr.SetArcToler(0.005); 
            // sgr.SetImportOption(TSTImportOption.ioCreateRectLoops, true);            

            // UnitMatrix3D — the identity matrix (root without offset)            
            if (!doc.IsDetail)
                SaveAssembly(doc.Assembly, UnitMatrix3D);   
            else
                SavePart(doc.Part, UnitMatrix3D);          
        }
        finally
        {
            sgf.CloseFile();
        }
        ok = true;
    }
    catch
    {
        ok = false;
    }
    finally
    {
        sgr = null;
        sgf = null;
        if (hDLL != IntPtr.Zero) { FreeLibrary(hDLL); hDLL = IntPtr.Zero; }
    }
    return ok;
}
```
