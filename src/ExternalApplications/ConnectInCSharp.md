# Connecting to main application in a C# application
The basic package of installed program includes:
- `CAMIPC.Helper.Cam.dll`, which contains the export function `CreateHelper`. This function returns an object of the [IIpcHelper](../../api/CAMIPC.Helper.IIpcHelper.yml) interface. The methods of this interface allow you to connect to an already running instance or start a new one.
- `NativeLibUtils.dll` - to simplify the loading and unloading of native DLLs.

File .csproj should contain:
- reference with path to NativeLibUtils.dll;
- package reference to CAMIPC SDK;
```
<ItemGroup>
    <PackageReference Include="EncySoftware.CAMIPC.SDK.Net" Version="1.1.5" />
    <Reference Include="C:\Program Files\ENCY Software\ENCY\Bin64\NativeLibUtils.dll" />
</ItemGroup>
```

## Support singleton class
This class provides public method `GetApplication()`, which connects to running instance.
```
using System;
using System.IO;
using System.Runtime.InteropServices;
using CAMAPI.ResultStatus;
using CAMIPC.Application;
using CAMIPC.ExecuteContext;
using CAMIPC.Helper;
using EncySoftware.NativeLibUtils;

namespace ApplicationEmptyNet;

public static class CamHelper
{
    private static IIpcHelper? _helper;
    private static ICamIpcApplication? _application;
    private static IntPtr _helperObjectPtr;
    private static IntPtr _helperDllPtr;
    private delegate IntPtr CreateHelperDelegate();
    
    /// <summary>
    /// Connect to CAM application
    /// </summary>
    private static IIpcHelper GetHelper()
    {
        if (_helper != null)
            return _helper;

        const string camFolder = @"C:\Program Files\ENCY Software\ENCY\Bin64";
        var helperPath = Path.Combine(camFolder, "CAMIPC.Helper.Cam.dll");
        if (!File.Exists(helperPath))
            throw new Exception($"{helperPath} not found");

        _helper = NativeLibLoader.CreateComObject<IIpcHelper, CreateHelperDelegate>(
                      helperPath, "CreateHelper", out _helperObjectPtr, out _helperDllPtr)
                  ?? throw new Exception("Can't create helper");
        
        return _helper;
    }
    
    /// <summary>
    /// Get instance of running CAM application to interact with it
    /// </summary>
    public static ICamIpcApplication GetApplication()
    {
        if (_application != null)
            return _application;

        var executeContext = new TExecuteContext();
        var instances = GetHelper().GetRunningCamAppList(ref executeContext);
        if (executeContext.ResultStatus.Code == TResultStatusCode.rsError)
            throw new Exception(executeContext.ResultStatus.Description);
        if (instances.Count == 0)
            throw new Exception("ENCY running instance not found");

        _application = instances.Get(0, executeContext);
        if (executeContext.ResultStatus.Code == TResultStatusCode.rsError)
            throw new Exception(executeContext.ResultStatus.Description);
        
        return _application;
    }
    
    /// <summary>
    /// Destructor. Release COM objects
    /// </summary>
    public static void Clean()
    {
        if (_helper != null)
        {
            if (_application != null)
                Marshal.ReleaseComObject(_application);
            NativeLibLoader.FreeDll(_helper, _helperObjectPtr, _helperDllPtr);
        }
    }
}
```

## Modificating support singleton class
[IIpcHelper](../../api/CAMIPC.Helper.IIpcHelper.yml) interface provides methods to:
- Connect to the first found instance (as mentioned above);
- Connect to ENCY by specifying the process PID;
- Start new ENCY and connect to it.