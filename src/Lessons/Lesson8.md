# Creating a C# extension to integrate with a PLM system

## Objectives
- Understand the basic structure of a PLM integration extension;
- Create an extention in C# or modify an existing example to integrate with a PLM system.

## Practical part
To create an extension, you need to:
- Install the latest version of the NuGet package that provides the base interfaces:
    - `EncySoftware.CAMAPI.SDK.Net`.
- Implement two interfaces:
    - `IExtension` – is a common interface for extensions so the CAM application can load your extension. It includes a single property `IExtensionInfo Info` which contains basic metadata;
    - `IExtensionPLM` – provides methods for integration with the PLM system (e.g., connect, send data, fetch data).
- Start with the required methods:
    - `GetParameters` – returns an IPLMParameters object. The CAM application uses it to display extension settings to the user;
    - `Connect` – receives parameter values and can establish a connection with the PLM system;
    - `Disconnect` – closes the connection and clears any internal state if needed.
- Then, implement the core item-related methods:
    - Retrieving items:
        - `GetChilds` – retrieves child items for a given parent ID. If no parent ID is provided, it returns items from the root level;
        - `FindItems` – searches items by name;
        - `GetItem` – loads a specific item by ID;
        - `GetLinkedItem` – returns a related item;
        - `GetItemData` – loads detailed data for a selected item.
    - Working with items:
        - `DownloadItems` – downloads selected items (except projects);
        - `UploadItem` – uploads regular items (except projects);
        - `DownloadProject` / `UploadProject` – for project-specific operations.
- Implement lifecycle methods:
    - `Install` and `Uninstall` – methods called when the extension is registered or removed. They can be left empty if you don’t need setup or cleanup logic.
- These boolean properties let the CAM application know which functions your extension supports: `SupportProjectLoad`, `SupportMachineLoad`, `SupportPostprocessorLoad`, `SupportPostprocessorInsideMachineLoad`, `SupportToolLoad`, `SupportToolSave`, `SupportDomainAuth`. If a property returns false, related functionality will be disabled in the app UI.

You can find the full method list and descriptions [here](../../api/CAMAPI.Extension.PLM.yml).

You can clone the example project and either use it as-is or modify it to create your own extension:
- Open the repository in [our GitHub account](https://github.com/EncySoftware/cam-api-examples/tree/v3/main) that contains the example extensions and clone it.
- Within the repository, find the folder that contains the PLM integration example - this is what you will base your new extension on.
- Open the project `PLMExtension/PLMExtensionNet/project/main/PLMExtensionNet.csproj` in your preferred IDE or code editor.
- Pay attention to:
    - `PLMExtension/PLMExtensionNet/.stbuild/build/stbuild.csproj` - the version of the build system is specified in this file. Over time, you might need to update it to access new features of [the build system](https://docs.encycam.com/BuildSystem/1/en/);
    - the version of the NuGet package `EncySoftware.CAMAPI.SDK.Net`.
- Modify the example for your PLM system. The example already includes a basic working implementation of both interfaces and uses directories to simulate operations of PLM system;

Once your extension is ready:
- Build the solution;
- Run ENCY separately;
- Setup the extension in ENCY and set configuration for PLM connection, further information is available [here](https://docs.encycam.com/ENCY/3/en/10602.html);
- Ensure that all functions of the extension operate correctly within ENCY.