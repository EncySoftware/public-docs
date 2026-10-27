# Delphi support in CAMAPI

## Support export function

You native DLL should have export function, which will be entry point:
```
function CreateInstanceOfExtension(PluginID: WideString): NativeUInt;
begin
    // create instance of your class
    var res: IExtension;
    if SameText(PluginID, TExtensionUtilCommonDll.GetIdent()) then
        res := TExtensionUtilCommonDll.Create() as IExtension

    else
        raise Exception.Create('Unknown ID ' + PluginID);

    // modify as pointer
    res._AddRef;
    result := NativeUInt(res);
end;
```
Its logic can be more complex, but it is important that the result of the function is a pointer with an incremented reference count.

## Connecting the SDK

The SDK is stored as package `EncySoftware.CAMAPI.SDK.bpl.x64` on nuget.org. In the BuildSystem, you can configure it to download and extract this package to a specific directory before compilation. Then, this directory needs to be connected in the Delphi project settings.

In build.cs:
- Add in list of `ManagerProps`:
```
new RestorerNugetProps
{
    Name = "RestorerNuget",
    DepsProp = new List<RestorerDepProp>
    {
        new()
        {
            PackageId = "EncySoftware.CAMAPI.SDK.bpl.x64",
            Version = "1.1.0", 
            OutDir = Path.Combine(RootDirectory.Parent, "SDK")
        }
    }
}
```
- Specify accordance:
```
settings.ManagerNames.Add("restorer", "Debug", "RestorerNuget");
settings.ManagerNames.Add("restorer", "Release", "RestorerNuget");
```
- Add restore before compile in target:
```
private Target Compile => _ => _
    .Executes(() =>
    {
        _buildSpace.Projects.Restore(Variant);
        _buildSpace.Projects.Compile(Variant, true);
    });
```

In this way, any other package can be connected - similar to PackageReference in C# projects.