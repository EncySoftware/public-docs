---
name: develop-native-interpreter
description: Creates, configures, builds and debugs an interpreter as a native DLL (Delphi, C++ or another native language) — the INCT ABI, registers and handlers, the `.snci` file, the Win64 build, inheritance, protection and packaging. Use only when a native interpreter is explicitly needed or an existing native interpreter is being changed; .NET is the default.
---

# Develop native interpreters

## When to use

Use this skill only when the user explicitly asks for a native interpreter or the interpreter being changed is already
native; .NET is the default ("Choose the implementation: .NET by default" in "Interpreter development"
(`interpreter-development`)). Use it for an interpreter compiled as a native DLL. It covers Delphi implementations and
the same ABI implemented in C++ or another native language. Use "Inspect NC programs" (`inspect-nc-programs`) before
changing behavior and "Verify interpretation" (`verify-interpretation`) afterwards.

## Establish the native contract

Before editing code, identify the product version, target process architecture, native compiler/project, SDK packages
and the exact `.snci` file. The interface declarations come as NuGet packages from the vendor's public package feed,
with the same prefix and major version as the SDK package the installed product was built with (see "The SDK package
and the product versions" in "Develop .NET interpreters" (`develop-dotnet-interpreter`); the same feed holds the native
packages):

- Delphi: `<Org>.NCInterpreterSDK.bpl.x64`. It pulls one package per interface (`<Org>.STNCInterpreter.bpl.x64`,
  `.STNCAnalyzer.bpl.x64`, `.STNCFormers.bpl.x64`, `.STNCConnect.bpl.x64`, `.STNCCustomInterpreter.bpl.x64`) with the
  `.bpl`, `.dcp` and the `IDL.<Name>.pas` unit.
- C++ or another native language: `<Org>.NCInterpreterSDK.tlb`. It holds no files of its own and pulls
  `<Org>.STNCInterpreter.tlb` and the other interface packages, each with `<Name>.tlb`, `<Name>.h` and `<Name>.idl`.

On restore, the package's `.targets` copies these files into the build output (`tlb\`, `idl\`, `dcu\<Name>\`); add those
folders to the compiler search path. Read the declarations from these files (`STNCInterpreter`, `STNCAnalyzer`,
`STNCFormers`, `STNCCustomInterpreter`, and `STNCConnect` when protected) instead of inventing them.

A native library must export two `stdcall` functions: `NCT_GetInterface: INCT_Interpreter` and `NCT_FreeMemory`. The
product does not load a library that lacks either of them; `NCT_FreeMemory` may be empty when the library has nothing to
release. Implement the ABI methods used by the product: `GetIdentifier`, `GetRegisters`, `SetInterface`, `Initialize`,
`NextOperation`, `TransLine`, `DefineRegister`, `BeforeInterprete`, `Interprete`, `AfterInterprete` and `EndOfProgram`
as needed by the control.

## Registers and their handlers

Keep an internal list of the registers the library declares, and bind the handler to each register when you add it — as
the Delphi interpreters do with a `procedure(const BR: INCT_BaseReg) of object` field of the register, and as the C#
base class does with the `command` parameter of `AddRegister`:

- In the constructor, add every register with its handler to the internal list. `GetRegisters` returns that list to the
  kernel as `INCT_RegisterList`.
- The kernel merges the registers of the `.snci`, of the library and of its parents into the base register list of
  `INCT_SysState`, so the position of a register there is not its position in your list. In `Initialize`, walk the base
  registers (`Get_BR_Count`, `Get_BR_ByIndex`), find your register by name and keep a map from the base register index
  (`BR.Idx`) to your register.
- In `Interprete(ExecNum)`, take the queue element with `BEA.Get(ExecNum)`. For a register element (`ExecType = exReg`),
  `ExecParam` is the base register index: take your register from the map and call its handler with the base register.
  For a command element (`exObj`), `ExecParam` is the command you added with `BEA.Add(exObj, …)`: run it in your command
  dispatcher.
- A base register the map does not contain — one that exists only in the `.snci` or in a parent — is not yours: leave it
  to the parent or ignore it.

With this, `Interprete` needs no `case` over addresses, and a new word is one line in the constructor and one handler.

## Project and platform

Keep the project and library names aligned with the `.snci`. Delphi projects normally use `.dpr` and `.dproj`; C++
projects must provide the same exports and ABI. Build Win64: current products are 64-bit and load the DLL named in
`LibraryFileName_x64`; build Win32 only for a 32-bit product of an older version. Place the matching DLLs beside the
`.snci` or in the package layout required by the product.

## The `.snci` file and identifiers

For a native library fill `LibraryFileName_x64` (and `LibraryFileName_x32` only for a 32-bit product); do not fill
`LibraryFileName_Net` or `NetNamespaceClass`. `LibraryID` in the `.snci` must equal the string returned by
`GetIdentifier`. `ID` identifies the interpreter settings file. Both IDs must be unique. A child must set `ParentID` to
the parent's `ID` and set `ParentFileName` to the parent's `.snci`; the parent's `LibraryID` is not a valid `ParentID`.

Check relative DLL paths, platform suffixes (`Win32`, `Win64`), register precedence and the parent chain before running
a program.

## Inheritance and protection

A native child receives the parent `INCT_Interpreter` through `SetInterface`. The kernel itself calls the parent's
`GetIdentifier`, `GetRegisters`, `SetInterface` and `Initialize`; the child must not call them. Call the parent's other
methods as the documentation on interpreter inheritance recommends: `TransLine` when the child read nothing of the line
(`ProcessedChars` is 0), passing on everything the parent returns; `DefineRegister` when the child did not define the
register, passing on the index and the result; `Interprete` for an element the child does not interpret itself;
`BeforeInterprete` and `AfterInterprete` always; `EndOfProgram` when the child did not detect the end of the program,
returning the parent's result; `NextOperation` always — the kernel calls it only on the child, before each operation
and each following part of a program, so without this call the parent keeps its old modal state.

If the interpreter's container holds `<library-name>.dat`, the product supplies `INCT_Connect`. An interpreter loaded
from an ordinary folder does not receive it, so test a protected interpreter from its container. Verify the secret data
through `Get_Count`, `Get_Data` or `Get_SCData` before allowing interpretation. A protected interpreter must fail closed
when the data is absent or mismatched, and say so through `Kernel.Notify` — one message that names the missing
protection data, not the secret itself. The kernel looks for the `.dat` by the name of the DLL it loads, so it is
`<library-name>_Win64.dat` for `<library-name>_Win64.dll`. An existing interpreter written to fail closed silently
produces an empty toolpath without an error: when you see one, check the `.dat` and `INCT_Connect` first.

## Memory and unload

Release interfaces and objects owned by the library. Implement `NCT_FreeMemory` and ensure parent interpreters can
unload after the child. Never keep CAM interfaces in process-global state; the product can create several interpreters
at once.

## Build, debug and verify

Build unchanged sources first. Check exports, architecture, identifiers and the `.snci`/DLL pairing before diagnosing
simulation. Run the real programs under CAM or Tuner, inspect the CAM log and use a native debugger when needed. Then
follow "Verify interpretation" for every target architecture and product version.

## Package

Deliver the `.snci`, the DLLs it names and the settings file. Keep source paths, customer programs and intermediate
build files (debug symbols, object files, logs) out of the delivered package.

## Rules

- Do not change the kernel or product DLLs to make a native interpreter work.
- Do not assume Delphi-specific behavior is part of the ABI; verify it against the type library and a working
  interpreter.
- Do not claim success from compilation alone: the native DLL must load and interpret the reference programs.
