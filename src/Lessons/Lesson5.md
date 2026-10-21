# Creating a custom operation

## Objectives
- Create a new operation type with settings.

## Practical part
Order of actions:
- Open the repository in [our GitHub account](https://github.com/EncySoftware/cam-api-examples/tree/v3/main) and clone it.
- Find the directory `Operation\ExtensionOperationSimpleNet` - this is what you will base your new extension on.
- Pay attention to:
  - XML-file `project\main\OperationSimpleNet.xml` - this file contains the operation settings:
    - Settings that allow ENCY to understand that the tool path calculation is handled by an external extension;
    - Operation settings that the user can configure in the UI;
    - `ContainerID` cannot be changed;
    - `SolverID` contains value, which will be later provided into `ExtensionFactory.Create`;
  - `ExtensionFactory.cs`:
    - Methods `OnLibraryRegistered` and `OnLibraryUnRegistered` - they edit the global `UserOperationsList.xml`, which contains custom operations.
  - The tool path calculation is performed in a subthread, and .NET only allows working with COM objects created in the same thread. Therefore, you should avoid declaring the properties of `ExtensionOperationSimpleNet` in `RunInitialize`.
- Modify main.cpp (optional). You can write your own code using the [API](../../api/CAMAPI.Application.ICamApiApplication.yml) - there are no restrictions.
- Call task 'Pack', which will create `*.dext` file - execute it. This action must be performed the first time - only then will the global `UserOperationsList.xml` be edited. It will add the path to `bin\Release\OperationSimpleNet.xml`.
- Restart ENCY to update list of available operation types;
- Click to add new operation. It should be located in the group specified in the XML file under the `MultiGroup` node. If it’s not there, check with `unavailable operations` specified.
- Click `generate toolpath` on the new operation.