# Connecting the SDK to a C++ project using the build system

## Objectives
- Create the simplest and functional extension on C++;
- Connecting the SDK to a C++ project using the build system.

## Practical part
Order of actions:
- Open the repository in [our GitHub account](https://github.com/EncySoftware/cam-api-examples/tree/v3/main) and clone it.
- Find the directory ExtensionEmptyCpp - this is what you will base your new extension on.
- Pay attention to:
  - `ExtensionEmptyCpp/.stbuild/build/stbuild.csproj` - the version of the build system is specified in this file. Over time, you might need to update it to access new features of [the build system](https://docs.encycam.com/BuildSystem/1/en/).
  - `ExtensionEmptyCpp/.stbuild/build/build.cs`:
    - properties of `RestorerNugetProps`, where version of `EncySoftware.CAMAPI.SDK.tlb` is specified;
    - properties of `BuilderMsCppProps`, where path to `MSBuild.exe` is specified (the version from Microsoft Visual Studio is used);
  - `ExtensionEmptyCpp\project\main\ExtensionEmptyCpp.settings.json` - you can adjust the settings of the displayed menu item - caption, hint and path to icon (relative to dll file);
- Modify main.cpp (optional). You can write your own code using the [API](../../api/CAMAPI.Application.ICamApiApplication.yml) - there are no restrictions. The example is kept as simple as possible to demonstrate the overall process of creating an extension.
- To execute your code, the project must contain the exported function [CreateInstanceOfExtension](../SupportedLanguages/CPlusPlus.md). It expects the id value from ExtensionEmptyCpp.settings.json as input and returns a reference to the created object.
- Compile to check functionality.
- Run special utility to create injectable file: `ExtensionEmptyCpp/commands/pack.cmd`;
- If successful, you should have a file named `ExtensionEmptyCpp/project/main/x64/Release/ExtensionEmptyCpp.dext`. This file can be injected into ENCY both on this computer and on any other computer with the current version of ENCY.
- Double click on it in order to inject.
- Run ENCY, open utilities menu and press "Empty extension on C++" (name should accord with "caption" value in JSON).
- Make sure that Notepad with the project information is open.