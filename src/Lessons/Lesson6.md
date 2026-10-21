# Creating a C# application to interact with geometry in main application

## Objectives
- Create a separate application in C# which works with geometry model.

## Practical part
- Open the repository in [our GitHub account](https://github.com/EncySoftware/cam-api-examples/tree/v3/main) and clone it.
- Find the directory Geometry. This folder contains two examples, one of them shows how to work with importer and the second shows how to use geometry model.
- Open project ExtensionUtilityGeometryModelNet\project\main\ExtensionUtilityGeometryModelNet.csproj.
- Build the project.
- Run ENCY separately.
- Open `Setting`, go to the tab `Extensions`.
- Press `Install`, select the file ExtensionUtilityGeometryModelNet\project\main\ExtensionUtilityGeometryModelNet.settings.json.
- Return to the main window and press `Import`, select the model Models\Milling_3D\49-1.igs from examples.
- After the model import is completed, find the utilities button in the upper left corner and run one of utilities:
  - `Export geometry node` - this utility exports current geometry model to .osd file;
  - `Transform geometry node` - this utility transforms current geometry model;
  - `Select colored geometry nodes` - this utility changes color of nodes and selects then in the main window.