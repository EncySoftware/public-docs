# Creating a C# application to connect to ENCY for managing it

## Objectives
- Create a separate application in C# to interact with ENCY.

## Practical part
- Open the repository in [our GitHub account](https://github.com/EncySoftware/cam-api-examples/tree/v3/main) and clone it.
- Find the directory ApplicationEmptyNet - this is what you will base your new application on.
- Open project ApplicationEmptyNet/project/main/ApplicationEmptyNet.csproj.
- Pay attention to:
    - `CamHelper` singleton, which [connects](../ExternalApplications/ConnectInCSharp.md) to any found ENCY instance;
- Modify MainWindow.xaml.cs (optional). You can write your own code using the [API](../../api/CAMAPI.Application.ICamApiApplication.yml) - there are no restrictions. The example is kept as simple as possible to demonstrate the overall process of creating a separate application.
- Run example;
- Run ENCY separately;
- Press `Open project`, choose any project from examples;
- Ensure that the project you selected has opened in ENCY.