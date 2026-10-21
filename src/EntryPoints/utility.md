# Entry point in adding new utility

At present, CAMAPI utilities has 2 entry points. This is sufficient to add any file to the list of utilities and configure its execution. This could be a DLL file, an executable EXE file, a script whose commands can only be processed by your other application.

The first entry point allows you to extend the list of utilities. Yes, this duplicates the functionality of manually adding utilities through the configuration window. However, extensions can be transferred from computer to computer via a dext file, so you can provide the user with just the executable file instead of writing instructions on how to configure a new utility. This becomes especially useful as the number of utilities begins to grow.

The use of this entry point can be complemented by the use of [the second entry point](utility_runner.md) – this will allow utilities of any format to be connected.

- Identifier: `utility`;
- Used interfaces:
  - [IExtensionTypeInfoUtility](../../api/CAMAPI.Extensions.IExtensionTypeInfoUtility.yml).
  - [IExtensionUtility](../../api/CAMAPI.Application.IExtensionUtility.yml).
- Available configuration settings:
  - caption: the text that will be shown to the user;
  - hint_text: the text that will be displayed as a tooltip when hovering the mouse cursor;
  - loader_extension_ident: the identifier of another extension that will invoke the current extension for execution (non-mandatory setting - in the case, where it is not set, will be used standard [Extension.Util.Common.Dll](../SystemExtensions/ExtensionUtilCommonDll.md))

Examples in [our GitHub account](https://github.com/EncySoftware/cam-api-examples/tree/v3/main):
- C# - directory `ExtensionUtilityNet`;
- Delphi - directory `ExtensionUtilityDelphi`;
- C++ - directory `ExtensionUtilityCpp`.

IMPORTANT: The code in the examples demonstrates how main application will display an error that occurs in the extension code. There is an error in the examples – ENCY must be run with administrator rights to save the exported.stcp file.