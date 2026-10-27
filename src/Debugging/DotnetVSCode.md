# Debugging a .NET extension using Visual Studio Code
Debugging in Visual Studio Code is configured using `launch.json`, where the executable program and its launch parameters are specified. This `launch.json` is already present in the examples from our [GitHub](https://github.com/EncySoftware/cam-api-examples/tree/v3/main) repository:
- `program`: "C:/Program Files/ENCY Software/ENCY/Bin64/ency.exe";
- `args`: ["/EXTENSION_DEBUG_FOLDER=\"${workspaceFolder}/project/main/bin/Debug\""].

This means that selecting `Run` -> `Start Debugging` will lead to:
- Visual Studio Code executes preLaunchTask:
    - Compiles your project, placing the DLL in the path specified in the .csproj file (`<OutDir>bin\$(Configuration)\</OutDir>`);
    - Copies `settings.json` to the same folder;
- C:/Program Files/ENCY Software/ENCY/Bin64/ency.exe is launched with the parameter `/EXTENSION_DEBUG_FOLDER="${workspaceFolder}/project/main/bin/Debug"`;
- ENCY, in addition to the extensions already registered, analyzes the directory `${workspaceFolder}/project/main/bin/Debug`, loading just compiled `dll` file according to the `settings.json` file;
- Your breakpoints in Visual Studio Code will be hit as your extension is used in the ENCY application.
