# System extension Extension.Util.Common.Dll

The extension is designed for loading DLL files. It can load both native DLLs (written in C++ and Delphi) and managed DLLs (written in C#).

- Entry point - [utility_runner](../EntryPoints/utility_runner.md);
- Implemented interface - [IExtensionUtilityRunner](../../api/CAMAPI.Application.IExtensionUtilityRunner.yml).

The DLL is analyzed to determine whether it is managed. If it is native, the method CreateInstanceOfExtension is called with the GUID specified in the utility settings (in the configurator), and it is expected to return an object of the IExtensionUtility interface.

If the called DLL is managed, it is analyzed to find the CAMAPI namespace. If this namespace is found, it should contain a ExtensionFactory class that implements the IExtensionFactory interface. An instance of this class will be created. Then, the IExtensionFactory.Create method will be called with the GUID, as there may be multiple utilities within a single DLL.