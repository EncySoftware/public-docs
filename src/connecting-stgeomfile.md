# Connecting STGeomFile.dll

`STGeomFile.dll` provides access to the `ISTGeomFiler` interface. The library ships as part of the Add-in (see [Distribution files](distribution-files.md)). You will also need two TLB files — they describe the interfaces (`ISTGeomFiler`, `ISTGeomReceiver`) and the enumerations, which gives typed access to the API:

- `STGeomApiTypes.tlb`;
- `STTypes.tlb`.

The library exports the function **`CreateGeomFiler`**, which returns a reference to the `ISTGeomFiler` interface.

**Example of loading the library.**

```csharp
[DllImport("kernel32.dll")]
public static extern IntPtr LoadLibrary(string dllToLoad);
[DllImport("kernel32.dll")]
public static extern IntPtr GetProcAddress(IntPtr hModule, string procedureName);
[DllImport("kernel32.dll")]
public static extern bool FreeLibrary(IntPtr hModule);

// Signature of the exported CreateGeomFiler function
[UnmanagedFunctionPointer(CallingConvention.StdCall)]
private delegate ISTGeomFiler TCreateGeomFiler();

private IntPtr            hDLL;
protected ISTGeomFiler    sgf;   // building the file: StartFile / CloseFile (see "Building the SGF file")
protected ISTGeomReceiver sgr;   // writing geometry: methods in the geometry sections and beyond

public bool ConnectToGeomFiler(string DLLPath)
{
    hDLL = IntPtr.Zero;
    sgf  = null;
    sgr  = null;

    // releases already acquired resources and signals failure
    bool Fail()
    {
        sgr = null;
        sgf = null;
        if (hDLL != IntPtr.Zero) { FreeLibrary(hDLL); hDLL = IntPtr.Zero; }
        return false;
    }

    try
    {
        if (!File.Exists(DLLPath))
            return Fail();

        hDLL = LoadLibrary(DLLPath);
        if (hDLL == IntPtr.Zero)
            return Fail();

        IntPtr pCreateGeomFiler = GetProcAddress(hDLL, "CreateGeomFiler");
        if (pCreateGeomFiler == IntPtr.Zero)
            return Fail();

        var CreateGeomFiler = (TCreateGeomFiler)Marshal.GetDelegateForFunctionPointer(
            pCreateGeomFiler, typeof(TCreateGeomFiler));

        sgf = CreateGeomFiler();
        if (sgf == null)
            return Fail();

        // the same object exposes the geometry-writing interface (in C#, QueryInterface is a type cast)
        sgr = sgf as ISTGeomReceiver;
        if (sgr == null)
            return Fail();

        return true;
    }
    catch
    {
        return Fail();
    }
}
```

Thus, `sgf` and `sgr` are the **same COM object** (see [Import interfaces](import-interfaces.md)).
