---
uid: main_page
---

# CAM API

CAM API lets you develop extensions for [ENCY](https://encycam.com) and connect external applications to the CAM system. This guide covers the SDK, extension development workflows and API reference.

## Main information

ENCY allows third-party extensions to be connected and to take control using COM technology. These extensions can be developed by external developers and [integrated into the ENCY workflow](src/EntryPoints/Main.md).

If you are interacting with the ENCY Open API for the first time, we recommend familiarizing yourself with [Lesson #1](src/Lessons/Lesson1.md) - completing it will allow you to create a test extension with minimal functionality, on which you can safely experiment.

Using CAMAPI, you can also write a [separate application](src/ExternalApplications/Main.md) that:
- interacts with ENCY;
- controls ENCY, for example, by loading a project;
- mimics the behaviour of user, for a example, by pressing some buttons.

An example of such an application can be found in [Lesson #4](src/Lessons/Lesson4.md).

## Sections
Choose a section from the navigation tree or start with one of these guides.

- [Supported programming languages](src/SupportedLanguages/Main.md) — SDK setup for C#, Delphi and C++.
- [Tutorial lessons](src/Lessons/Main.md) — examples of extensions and external applications.
- [System extensions](src/SystemExtensions/Main.md) — integration through utility DLLs and executables.
- [Debugging](src/Debugging/Main.md) — configure your development environment to debug extensions.
- [Entry points](src/EntryPoints/Main.md) — connect extensions to ENCY menus and commands.
- [Machining tools import](src/MachiningToolsImport/MTIStartPage.md) — work with tool libraries, cutting tools and holders.
- [External applications](src/ExternalApplications/Main.md) — connect to and control ENCY from a separate application.
- [Using ComWrapper](src/Helpers/ComWrapper.md) — work with COM objects through the helper library.
- [Developer guide](src/DeveloperGuide/Main.md) — concepts, macros, and C# examples for every API domain.
- [API reference](xref:CAMAPI.Application) — namespaces, interfaces and methods, including the application API.

## Helpful links:
- [GitHub: CAMAPI using examples](https://github.com/EncySoftware/cam-api-examples/tree/v3/main);
- [Postprocessing API documentation](https://docs.encycam.com/technical/Postprocessors/3/en/).

## System requirements:
- OS Windows 10 or higher;
- .NET 10.0 SDK or higher;
