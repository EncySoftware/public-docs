# .NET postprocessors

This is the open postprocessing system based on the [.NET platform](https://dotnet.microsoft.com/). It uses `C#` as a programming language and [Visual Studio Code](https://code.visualstudio.com/) as the development environment and code debugger.

The CAM system has two independent postprocessing subsystems; both are actual and can be used by your choice. This section documents only the .NET based system. The other subsystem (the Postprocessors generator) is documented under [Postprocessors generator](../../sppx/src/index.md).

## Why this system

- Based on widespread, free and open-source top-class tools: .NET, `C#` and Visual Studio Code. All modern programming technologies are available to postprocessor developers.
  - The power and at the same time the simplicity of the `C#` programming language: object-oriented style, strong and safe typing, automatic garbage collection, and features like generics, lambda expressions, LINQ and tuples.
  - Syntax highlighting and autocomplete with IntelliSense.
  - A first-class debugger with different kinds of breakpoints, call stacks, an interactive console, a local variables view and the watch list.
  - A high-end code editor with a huge number of useful extensions for all occasions.
  - An unlimited amount of documentation available on the network.
  - Postprocessor documentation available directly in the code as comments and pop-up tips.
- The familiar register-based concept of the Postprocessors generator, re-implemented from scratch on a new level with a modern object-oriented paradigm and taking into account decades of experience in postprocessor development. This provides advantages such as:
  - Easy writing of postprocessors that generate many files at the same time.
  - The ability to append to an arbitrary location in a file, not just to the end.
  - Generating output files in any encoding.
  - Multiple independent sets of registers.
  - Text registers in addition to numeric registers.
  - Developer-defined settings individual for each postprocessor.
  - An integrated library of functions for geometric calculations.
  - The ability to use third-party libraries widely available through [Nuget](https://www.nuget.org/).

## Documentation

- [Introduction](introduction.md) — what a postprocessing system is and the main program modules.
- Organization of the postprocessing system
  - [Running the postprocessing](organization/running-the-postprocessing.md)
  - [Postprocessors' development tools](organization/development-tools.md)
  - [Postprocessor's file set](organization/postprocessor-file-set.md)
- User interface
  - [CLData Viewer](user-interface/cldata-viewer.md)
  - [Postprocessor settings window](user-interface/postprocessor-settings-window.md)
  - [Registers window](user-interface/registers-windows.md)
  - [Visual Studio Code user interface](https://code.visualstudio.com/docs/getstarted/userinterface)
- How to write postprocessors
  - [How to prepare the computer to start writing the postprocessors](how-to/prepare-the-computer.md)
- [CLData documentation](../../cldata/cldata.md) — the shared input model read by both postprocessing subsystems.
- [External references and examples](references.md) — the .NET SDK API reference, external links and example postprocessors.
