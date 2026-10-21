# Debugging a C++ extension using Visual Studio
For debugging the extension in Visual Studio you should:
- In the project properties - `Options` -> `Debugger`:
  - Set `Command`: `C:/Program Files/ENCY Software/ENCY/Bin64/ency.exe`;
  - Set `Parameters`: `/EXTENSION_DEBUG_FOLDER=\"${workspaceFolder}/project/main/bin/Debug`. Instead of `${workspaceFolder}` specify the full path to the directory with an example.
- Copy the `settings.json` file to the `bin\debug` directory.

This means that selecting `Start debugging (F5)`:
- Visual Studio your project, placing the DLL in the path specified in the project settings;
- C:/Program Files/ENCY Software/ENCY/Bin64/ency.exe is launched with the parameter `/EXTENSION_DEBUG_FOLDER="${workspaceFolder}/project/main/bin/Debug"`;
- ENCY, in addition to the extensions already registered, analyzes the directory `${workspaceFolder}/project/main/bin/Debug`, loading just compiled `dll` file according to the `settings.json` file;
- Your breakpoints in Visual Studio will be hit as your extension is used in the ENCY application.