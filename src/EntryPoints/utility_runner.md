# Entry point in executing utility

This entry point already contains a list of system extensions:
- [Loading DLL files](../SystemExtensions/ExtensionUtilCommonDll.md);
- [Loading EXE files](../SystemExtensions/ExtensionUtilCommonExe.md).

The extension expands the list of utilities that can be connected to main application. The fact is that system extensions can only run DLL and EXE files. By adding a new extension of type `utility_runner`, you can specify it in the launch parameters for extensions of type utility. Thus, ENCY calls the `utility_runner` extension, passing it information about the utility to be launched.

- Identifier: `utility_runner`;
- Used interfaces:
  - [IExtensionTypeInfoUtilityRunner](../../api/CAMAPI.Extensions.IExtensionTypeInfoUtilityRunner.yml).
  - [IExtensionUtilityRunner](../../api/CAMAPI.Application.IExtensionUtilityRunner.yml).
- Available configuration settings:
  - filter_types: filter provided to "Choose file" dialog window, when user chooses utility;
  - visible_in_editor: extension is visible in utility editor, so it can be chosen. This allows for the creation of a unique extension that is suitable for launching only a specific utility and should not be displayed elsewhere to the user.

Examples in [our GitHub account](https://github.com/EncySoftware/cam-api-examples/tree/v3/main):
- C# - directory `ExtensionUtilityRunnerNet`;
- Delphi - directory `ExtensionUtilityRunnerDelphi`;
- C++ - directory `ExtensionUtilityRunnerCpp`.