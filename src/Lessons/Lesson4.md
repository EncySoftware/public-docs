# Demonstration of methods for unloading an extension during main application is running

## Objectives
- Create the simplest and functional extension on C#;
- Use various methods to unload extensions.

## Practical part
Order of actions:
- Open ENCY because we will be editing the list of utilities while the application is running.
- Open the repository in [our GitHub account](https://github.com/EncySoftware/cam-api-examples/tree/v3/main) and clone it.
- Find the directory `GCodeGeneration\ExtensionUtilityNCMakerNet` - this is what you will base your new extension on.
- The extension is already correct. In this lesson, we will not modify it but will only change the configuration file.
- Open .NET project and compile it - `bin/debug/ExtensionUtilityNcMakerNet.dll` should appear;
- Copy `ExtensionUtilityNcMakerNet.settings.json` into `bin/debug/`;
- Add extension in the first time:
  - Archive both files (`dll` and `settings.json`) into file with `*.dext` extension;
  - Execute created `*.dext` file - it will be added to ENCY. It has no `unload_mode` setting, so it will be set to default `umJustAfterExecution`;
- In ENCY open utilities menu and press `Generate G code by C#`. Then close notepad window with results.
- Don't close ENCY and add extension in the second time:
  - Modify `bin/debug/ExtensionUtilityNcMakerNet.settings.json`:
    - Add unload mode `umManuallyFromUI`;
    - Change caption;
    ```
    {
      "name": "Extension on C# to generate G code",
      "description": "Extension on C# to generate G code",
      "module_path": "${extensionJsonFolder}/ExtensionUtilityNcMakerNet.dll",
      "unload_mode": "umManuallyFromUI",
      "extensions": [
        {
          "utility": {
            "name": "Generate G code by C#",
            "caption": "Generate G code by C# (version 2)",
            "id": "Extension.Utility.NcMaker.Net"
          }
        }
      ]
    }
    ```
  - Archive json and dll files into file with `*.dext` extension;
  - Execute created `*.dext` file - it will be added to main application. Library will be overwritten, because it was unloaded. Otherwise, you will encounter an error.
  - In ENCY open utilities menu - there should be item, called `Generate G code by C# (version 2)`. This means that with the previous action, you successfully updated the extension - now it has new caption.
  - Press `Generate G code by C# (version 2)` and close notepad with opened results.
  - Now try to execute early created `*.dext` extension. You'll get an error `Access to the path 'ExtensionUtilityNcMakerNet.dll' is denied`. This means that the extension was not unloaded from memory - as it should be, since we specified the unload method as `umManuallyFromUI`.
  - But we still can unload it from UI:
    - Open `Settings` -> `Extensions`;
    - Choose `Generate G code by C#` (here is value from `name` field in `settings.json`);
    - Click `unload` - if the library unloads successfully, the `unload` button will become inactive, otherwise, you will encounter an error.
  - Now execute early created `*.dext` extension - you will succeed, because extension was manually unloaded from memory;
- Don't close ENCY and add extension in the third time:
  - Modify `bin/debug/ExtensionUtilityNcMakerNet.settings.json`:
    - Add unload mode `umBeforeProgramFinalization`;
    - Change caption;
    ```
    {
      "name": "Extension on C# to generate G code",
      "description": "Extension on C# to generate G code",
      "module_path": "${extensionJsonFolder}/ExtensionUtilityNcMakerNet.dll",
      "unload_mode": "umBeforeProgramFinalization",
      "extensions": [
        {
          "utility": {
            "name": "Generate G code by C#",
            "caption": "Generate G code by C# (version 3)",
            "id": "Extension.Utility.NcMaker.Net"
          }
        }
      ]
    }
    ```
  - Archive json and dll files into file with `*.dext` extension;
  - Execute created `*.dext` file - it will be added to main application.
  - In ENCY open utilities menu - there should be item, called `Generate G code by C# (version 3)`. This means that with the previous action, you successfully updated the extension - now it has new caption.
  - Press `Generate G code by C# (version 2)` and close notepad with opened results.
  - Try to execute early created `*.dext` extension. You'll get an error `Access to the path 'ExtensionUtilityNcMakerNet.dll' is denied`.
  - Check unloading manually from UI:
    - Open `Settings` -> `Extensions`;
    - Choose `Generate G code by C#` (here is value from `name` field in `settings.json`);
    - Ensure that the `unload` button is inactive. You can't unload it, because of `umBeforeProgramFinalization`.
- Now you can close ENCY and execute created `*.dext` - the library was unloaded from memory when ENCY closed.

