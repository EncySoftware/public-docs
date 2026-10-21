# Extension settings

An extension integrated into main application consists not only of a DLL but also a JSON file that contains a description of the library.

## Description of the library as a container for multiple extensions

List of fields:
- name;
- description;
- module_path.
Each of these fields appears in the [IExtensionLibraryInfo](../api/CAMAPI.Extensions.IExtensionLibraryInfo.yml) interface.

## Description of each extension separately

List of extensions is a JsonArray, where each extension is described in separate JsonObject. This JsonObject contains only one key - unique identifier of [entry point](EntryPoints/Main.md). Value is a JsonObject with fields:
- id;
- name.

There may also be additional properties (configuration settings) required for a specific entry point.

The ID must be unique among all other extensions, so it is recommended to use a prefix in the name to ensure this uniqueness.

## Example
```
{
    "name": "Library for empty extension",
    "description": "Library for empty extension",
    "module_path": "${extensionJsonFolder}/ExtensionEmpty.dll",
    "extensions": [
        {
            "utility": {
                "id": "Extension.Utility.Empty",
                "name": "Empty extension"
            }
        }
    ]
}
```