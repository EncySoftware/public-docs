# Connecting the SDK to a Delphi project using the build system

## Objectives
- Create the simplest and functional extension on Delphi;
- Connecting the SDK to a Delphi project using the build system.

## Practical part
Order of actions:
- Open the repository in [our GitHub account](https://github.com/EncySoftware/cam-api-examples/tree/v3/main) and clone it.
- Find the directory ExtensionEmptyDelphi - this is what you will base your new extension on.
- Pay attention to:
    - `ExtensionEmptyDelphi/.stbuild/build/stbuild.csproj` - the version of the build system is specified in this file. Over time, you might need to update it to access new features of [the build system](https://docs.encycam.com/BuildSystem/1/en/).
    - `ExtensionEmptyDelphi/.stbuild/build/build.cs`:
        - properties of `RestorerNugetProps`, where version of `EncySoftware.CAMAPI.SDK.bpl.x64` is specified;
        - properties of `BuilderMsDelphiProps`, where path to `MSBuild.exe` is specified (the version from Microsoft Framework is used, not the SDK);
- Modify src/Extension.pas (optional). You can write your own code using the [API](../../api/CAMAPI.Application.ICamApiApplication.yml) - there are no restrictions. The example is kept as simple as possible to demonstrate the overall process of creating an extension. Pay attention to:
    - Option `unit scope names`, because there should be mandatory `IDL` item;
- To execute your code, the project must contain the exported function [CreateInstanceOfExtension](../SupportedLanguages/Delphi.md). It expects the id value from ExtensionEmptyDelphi.settings.json as input and returns a reference to the created object.
- Compile to check functionality.
- Run special utility to create injectable file: `ExtensionEmptyDelphi/commands/pack.cmd`;
- If successful, you should have a file named `ExtensionEmptyDelphi/project/main/Win64/Release/ExtensionEmptyDelphi.dext`. This file can be injected into ENCY both on this computer and on any other computer with the current version of ENCY.
- Double click on it in order to inject.
- Run ENCY, open utilities menu and press "Empty extension on Delphi" (name should accord with "caption" value in JSON).
- Make sure that Notepad with the project information is open.