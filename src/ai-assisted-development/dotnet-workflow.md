# .NET workflow

A C# interpreter is a .NET project that references the interpreter SDK package and is built into a `*.dll` library; next to it lies the `*.snci` settings file. The CAM system or ENCY Tuner loads the library and calls it when simulating NC programs. This is the default path: the assistant chooses it for every new interpreter unless you asked for something else.

How to create an interpreter from a template is described in [Developing a custom interpreter in (.NET) C#](../dotnet/developing-a-custom-interpreter-in-net-csharp.md), how to run it under the debugger — in [Interpreter debugging in Visual Studio Code](../dotnet/interpreter-debugging-in-visual-studio-code/interpreter-debugging-in-visual-studio-code.md). Details for the assistant are in the `develop-dotnet-interpreter` skill.

## Where to start

Most often not from scratch. If there is an interpreter for the same or a similar controller whose behavior has been checked on real programs, copy it and refine it. The copy needs new identifiers: the GUID returned by `GetIdentifier` (it is also `LibraryID` in the `*.snci` file) and the GUID in the `ID` field. The CAM system cannot tell apart two interpreters with the same identifiers.

If you need a new one, create it with the **Create interpreter** item in the **Utilities** list of the CAM system or with the **Interpreter manager** item in ENCY Tuner — both open the same **Create G-code interpreter** window (the interpreter creator). The template the interpreter is created from is designed for one family of controllers; the assistant checks and fixes what the interpreter creator does not do by itself: fills in `ID` in the `*.snci` file, sets the released version of the SDK package, removes handlers of words that mean something else on your controller. For a descendant interpreter it also fixes the reference to the parent: `ParentID` must match the parent's `ID`, and `ParentFileName` must name the parent's `*.snci` file.

An interpreter can inherit another one — see [Interpreter inheritance](../g-code-interpretation/interpreter-inheritance/interpreter-inheritance.md). Before taking a supplied interpreter as a parent, check its purpose in the [list of interpreters](../appendix/list-of-interpreters/list-of-interpreters.md): some of them are marked "Tool path import only" — they do not link NC program blocks to movements.

In any case, start from a known state:

1. Put the interpreter under version control before changing anything.
2. Build it without changes. If it does not build as it is, further diagnostics are pointless.
3. Run all your NC programs through it and save the result as the baseline for comparison.

## Product versions

Each product version has its own .NET version: version 3 of the CAM system and ENCY Tuner runs on .NET 10, version 2 runs on .NET 8.

The interpreter references the `EncySoftware.NCInterpreterSDK.Net` package. The assistant determines its version as follows:

1. It reads which package version the installed product was built with: the `Bin64\STNCInterpreterSDKProject.stbuildresult.json` file, the `build_results.versions` section. An ENCY Tuner installation may not have this file; then the version is taken from the CAM system of the same version (ENCY 3 for ENCY Tuner 3, ENCY 2 for ENCY Tuner 2). Where ENCY Tuner has the file, its number is set by the build of ENCY Tuner, which does not publish the SDK packages, so a package with exactly that number may not exist on the package source.
2. It sets the newest **released** version of the package (without `-dev`, `-rc` and similar suffixes) with the same major number and not newer than the version from step 1. For ENCY Tuner, this is the number from its file or, if there is no file, from the file of the CAM system of the same version. The number from the ENCY Tuner file is only an upper limit.

The released packages are published on nuget.org, which the .NET SDK uses by default. A version that a nightly or test build of the product was built with cannot be downloaded by the customer, so it does not get into a project that leaves your computer.

If the interpreter must work in several product versions, one project is built for each of them; it must be checked in each.

## The cycle

1. Formulate the task as a visible difference in the simulation: which program, which block, what should happen.
2. Ask the assistant to find the place where the interpreter reads this word and to explain what it does now.
3. Decide together with it what kind of change this is:
   - **a variation** — another axis name, a machine M-function, a word without effect on the tool path. Its place is the `InterpreterSettings.ini` file next to the library, not the code: then the next such case can be solved by a support engineer without a build. The first time, the setting key is added to the code; after that it is a setting;
   - **new behavior** — a cycle, a frame, a feed mode. This is a change in the code, in the file of the role it belongs to;
   - **a kernel or SDK limitation** — the required call does not exist. The assistant describes the workaround and its limits and writes down what would have to change in the product.
4. Make one small change and build the project. Build warnings are information about your change, not noise.
5. Run all NC programs and compare with the previous result — see [Checking and confirming the result](review-and-verify.md).

## Debugging

The `F5` key in Visual Studio Code builds the interpreter and starts the configuration selected in the **Run and Debug** panel: **Launch CAM** starts the CAM system, **Launch Tuner** starts ENCY Tuner; a breakpoint is hit when an NC program is simulated. Before debugging, turn on the log as described in [advanced setup](advanced-setup.md#build-and-debugging-tools) — otherwise the log will contain neither the kernel's messages about the words read nor the lines the interpreter writes.

To simulate a program, create a G-code based operation, paste the program text, select the interpreter in the **Interpreter file** field on the **Strategy** tab of the operation parameters and calculate the operation.

Keep building and debugging the way the template made them: a colleague must be able to open the folder, press `F5` and stop at a breakpoint. The assistant does not replace them with its own scripts and environment variables.

## What to check in the code

- The changes contain what was asked for and nothing more: no reformatting, no unrelated rewrites.
- The line endings and encoding of the template files are preserved — otherwise the history shows every line as changed.
- Numbers in the program are read regardless of the Windows language: the dot is always the decimal separator.
- The interpreter's state is stored in its object, not in static fields: the CAM system creates a new instance for each operation calculation, and separate ones for the parent and for the cycle contour, and a static field is not shared between them; ENCY Tuner, on the contrary, keeps one instance per channel — from the first operation of the channel to the last — and the modal state and a static field carry over from one operation to the next: for example, a `G0` from the end of one operation is still in force at the start of the next.
- A word the interpreter does not simulate does not disappear silently: it is either listed as read without effect on the tool path, or gives one warning per program that a machine operator can understand.

Rules that do not depend on the kernel — parsing numbers and expressions, cycle parameters, rules for axes and spindles, reading the settings file — the assistant can cover with unit tests. Tests complement running real programs but do not replace it.
