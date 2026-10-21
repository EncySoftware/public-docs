# Working with the tool library

Machining tool libraries are created in .db files, where each library is an independent repository of a specific set of tools. By default, the standard machining tool libraries are located in the "C:\ProgramData\[CAM_Path]\Version 17\Libraries\Tools" directory. Custom tool libraries can be created in any location. To create a new tool library or open an existing one, use the functions of the IMTI_MachiningToolsImportLibrary instance (importer):
```
//C#
//create a new tool storage
var tNewStorage = importer.CreateNewToolsStorage(@"D:\teststorage.db");
//open an existing tool storage
var tExstStorage = importer.OpenExistingToolsStorage(@"D:\teststorage.db");
```

To add a new machining tool item to the tool library, use the following function:
```
//C#
//the tool must be created and formed before adding it to the tool library
bool result = storage.AddToolItem(tool);
```

## Helpful links:
- [How to manage tool libraries in the CAM interface](https://docs.encycam.com/ENCY/3/en/615.html)
- [Preparing the machining tools import api environment](PrepEnvPage.md)
- [GitHub: Machining tool import API examples](https://github.com/EncySoftware/cam-api-examples/tree/v3/main/MachiningTools);

## Continue to read:
- [Working with cutting tools](WorkingWithTools.md)

