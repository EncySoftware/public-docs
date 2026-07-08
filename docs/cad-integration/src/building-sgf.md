# Building the SGF file

This is the **entry point** of geometry import — the moment when control is handed to the Add-in from outside. There are two possible scenarios (see [Interaction scenarios](scenarios.md)):

- **clicking a Toolbar button** in the CAD system — the user exports the open model ([Import from a CAD system into a CAM system](import-from-cad.md));
- **a call from a translator or from the CAM system** when importing a CAD file — the Add-in is launched on an already loaded model ([Import a CAD file into a CAM system](import-cad-file.md)).

In both cases the input is the same: the **current model of the CAD system** (what to save) and the **path to the output file** (where). From there the Add-in builds the SGF file following a single scheme:

1. connect to the import library (see [Connecting STGeomFile.dll](connecting-stgeomfile.md));
2. traverse the CAD model top-down and write its geometry through `sgr` (see the sections [Curves and points](curves-and-points.md)–[PMI](pmi.md));
3. release the interfaces and unload the library (`FreeLibrary`).

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

**Example: the import entry point.**

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
