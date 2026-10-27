# Lesson #1 - general introduction to the extension ideology

## Objectives
- Create the simplest and functional extension on C#;
- Show the process in broad strokes, which will be explained in detail in subsequent lessons.

## Practical part

Order of actions:
- Open the repository in [our GitHub account](https://github.com/EncySoftware/cam-api-examples/tree/v3/main) and clone it.
- Find the directory ExtensionEmptyNet - this is what you will base your new extension on.
- Pay attention to ExtensionEmptyNet/.stbuild/build/stbuild.csproj - the version of the build system is specified in this file. Over time, you might need to update it to access new features of [the build system](https://docs.encycam.com/BuildSystem/1/en/).
- Open project ExtensionEmptyNet/project/main/ExtensionEmptyNet.csproj. We will review the structure and features of the project in subsequent lessons. For now, our goal is to create the most basic extension.
- Pay atteniton to version of package EncySoftware.CAMAPI.SDK.Net - you might need to update it to access new features of API.
- Modify ExtensionTest.cs (optional). You can write your own code using the [API](../../api/CAMAPI.Application.ICamApiApplication.yml) - there are no restrictions. The example is kept as simple as possible to demonstrate the overall process of creating an extension.
- To execute your code, the DLL must contain the [ExtensionFactory class](../SupportedLanguages/CSharp.md). Its Create method will be called to obtain an instance of the class, and the code within that instance will then be executed.
- Modify [JSON file](../JsonSettings.md):
    - Type of extension should be identifier of [entry point](../EntryPoints/Main.md);
    - Extension id should accord with value expected in ExtensionFactory.Create method;
```
{
    "name": "Empty extension on C#",
    "description": "Empty extension on C#",
    "module_path": "${extensionJsonFolder}/ExtensionEmptyNet.dll",
    "extensions": [
        {
            "utility": {
            "name": "Empty extension on C#",
                "caption": "Empty extension on C#",
                "id": "Extension.Utility.Empty.Net"
            }
        }
    ]
}    
```
- Compile to check functionality.
- Run special utility to create injectable file: `ExtensionEmptyNet/commands/pack.cmd`;
- If successful, you should have a file named `ExtensionEmptyNet/project/main/bin/ExtensionEmptyNet.dext`. This file can be injected into ENCY both on this computer and on any other computer with the current version of ENCY.
- Double click on it in order to inject.
- Run ENCY, open utilities menu and press "Empty extension on C#" (name should accord with "caption" value in JSON).
- Make sure that Notepad with the project information is open.