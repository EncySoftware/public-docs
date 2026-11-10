# Native interpreter workflow

A native interpreter is a `*.dll` library built in Delphi, C++ or another language that compiles to machine code. The assistant takes on a native interpreter only if you explicitly asked for it or are changing an existing native interpreter; a new interpreter is created in C# by default — see [.NET workflow](dotnet-workflow.md).

Reference information on the library is in [Interpreter library](../interpreter-structure/interpreter-library/interpreter-library.md), [Interpreter settings file](../interpreter-structure/interpreter-settings-file/interpreter-settings-file.md) and [Interpreter interface](../g-code-interpretation/interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md). Details for the assistant are in the `develop-native-interpreter` skill.

## What the assistant needs

- The interpreter sources and the project it is built with — or an explicit request to create a new one.
- A compiler: RAD Studio for Delphi, a C++ compiler or another one.
- The SDK interface declarations. They come as NuGet packages from the same source as the SDK package for C# (see [Product versions](dotnet-workflow.md#product-versions)), with the same version: for Delphi — `EncySoftware.NCInterpreterSDK.bpl.x64` (`IDL.<Name>.pas` units and `*.bpl`, `*.dcp` packages), for C++ and other languages — `EncySoftware.NCInterpreterSDK.tlb` (`*.tlb` type libraries, `*.h` headers and `*.idl` descriptions). Both packages pull in one package per interface, each with its own version number: `STNCInterpreter`, `STNCAnalyzer`, `STNCFormers`, `STNCCustomInterpreter` and `STNCConnect` (the protection interface used by protected interpreters). The assistant takes the declarations from them instead of inventing them. If the package of the required version is not available in the source, contact support.
- The `*.snci` file the interpreter is loaded with.

## What the library must have

- The library exports two functions: `NCT_GetInterface` and `NCT_FreeMemory`. If either of them is missing, the product will not load the library.
- The string returned by `GetIdentifier` equals `LibraryID` in the `*.snci` file. Both identifiers, `LibraryID` and `ID`, are unique.
- For current products a 64-bit library is built; its name is given in `LibraryFileName_x64`. A 32-bit one, named in `LibraryFileName_x32`, is needed only for an old 32-bit product version.
- A descendant interpreter receives its parent through `SetInterface` and calls it according to the rules of [interpreter inheritance](../g-code-interpretation/interpreter-inheritance/interpreter-inheritance.md).

Registers can be defined either in the `*.snci` file or in the library itself. It is more convenient to declare them in the library together with their handlers: then a new word is one line in the register list and one handler.

## The cycle

1. Build the sources without changes and check that the library loads and simulates your NC programs. Save the result as the baseline.
2. Before looking for an error in the simulation, check the function exports, the bitness, the identifiers and the pair of `*.snci` and `*.dll`: most "it does not work" cases start here.
3. Make one small change, build, run all NC programs and compare with the previous result — see [Checking and confirming the result](review-and-verify.md).
4. Debug under your compiler's debugger by attaching to the CAM system or ENCY Tuner, and read the [interpreter interaction log](../g-code-interpretation/log-interaction-with-the-interpreter/log-interaction-with-the-interpreter.md).

## Protected interpreter

An interpreter that checks its data through the protection interface is described in [Protected interpreters](../interpreter-structure/protected-interpreters/protected-interpreters.md). Check it from the container in which it will be delivered: from an ordinary folder it receives no protection data. Without its data, a protected interpreter must refuse to simulate. How it reports this is up to its author: the assistant makes the interpreter show a clear message, but an existing one may silently produce an empty tool path — in that case, check the protection data first.

## What not to do

- The kernel and the product libraries are not changed to make the interpreter work.
- Delphi implementation details are not part of the binary interface: in C++ and other languages the interface is checked against the type library and a working interpreter.
- Compilation is not the end of the work: the library must load and simulate your programs.
