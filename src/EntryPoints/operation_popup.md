# Entry point in adding a new item to the operation's context menu

The entry point allows for the configuration of main program, enabling you to add custom items to the context menu based on the selected operation. For each added item, you can define its own executable procedure. This way, a single extension can add an unlimited amount of functionality.

- Identifier: `operation_popup`;
- Used interfaces:
    - [IExtensionTypeInfoOperationPopup](../../api/CAMAPI.Extensions.IExtensionTypeInfoOperationPopup.yml).
    - [IExtensionOperationPopup](../../api/CAMAPI.TechnologyForm.IExtensionOperationPopup.yml).
- Configuration settings: none.

Examples in [our GitHub account](https://github.com/EncySoftware/cam-api-examples/tree/v3/main):
- C# - directory `ExtensionOperationPopupNet`;
- Delphi - directory `ExtensionOperationPopupDelphi`;
- C++ - directory `ExtensionOperationPopupCpp`.