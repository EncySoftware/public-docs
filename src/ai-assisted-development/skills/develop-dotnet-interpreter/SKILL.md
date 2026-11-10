---
name: develop-dotnet-interpreter
description: Creates, structures, configures, builds and debugs an NC interpreter in C# from the templates shipped with the CAM system — the released SDK package for each product version, the project files and what goes where, the INI file for machine variations, known defects of the templates, code style and debugging with F5 in the CAM system or Tuner. This is the default way to develop an interpreter. Use for any work on a C# interpreter — creating one, adding a word or a cycle, building it for product versions, F5 debugging.
---

# Develop .NET interpreters

## When to use

This is the default implementation of an interpreter. Work on a C# interpreter: creating one, adding a word or a cycle,
making it configurable, building it for the products it must run in, debugging it. Take the census of "Inspect NC
programs" (`inspect-nc-programs`) first and follow "Verify interpretation" afterwards; "How the kernel reads a block"
(`nc-interpreter-foundations`) explains the kernel calls this skill refers to.

## Words used here

- **Product version** — the major version of the installed CAM system or Tuner, as the name of its installation folder
  shows. The CAM system and Tuner of one release may carry different numbers. Each product version has its own .NET
  version and SDK package version: read both from the installation (see "The SDK package and the product versions"
  below), never from memory.
- **The `.snci` file** — the XML file that tells the CAM system which DLL is the interpreter. The documentation calls it
  the interpreter settings file.
- **The INI file** — `InterpreterSettings.ini` next to the DLL, read by the template at start. The template calls it the
  settings file; it holds the switches a user may change without building.
- **GUID** — a unique identifier such as `{5DD76B4D-8ABE-43EE-AB0C-078F5D686C5E}`; create a new one with
  `[guid]::NewGuid().ToString('B').ToUpper()` in PowerShell. The kernel accepts a GUID only in braces.

## Workflow

1. Choose the starting point and create the project (below). Say which you chose and why.
2. Set the SDK package version and the target .NET version for every product version the interpreter must run in.
3. Fix the known defects of the template you started from.
4. Build the project unchanged; if it does not build, stop and fix that first — nothing after it can be diagnosed.
5. Run the reference NC programs through it and keep the result as the baseline ("Verify interpretation"
   (`verify-interpretation`)).
6. Make one change at a time in the file of its role; make variations a setting of the INI file.
7. Build, debug or trace on a real program, then follow "Verify interpretation".

## Choose the starting point

1. **An existing interpreter for the same or a similar control** — prefer it when its behavior has been checked on real
   programs. Copy it into a new folder and give the copy a new identity:
   - a new GUID returned by `GetIdentifier` in `Entry.cs`, written also into `LibraryID` of the `.snci` file (the two
     must be equal);
   - another new GUID in `ID` of the `.snci` file. Two interpreters with the same identifiers cannot be told apart by
     the CAM system.
2. **A template** — `Supplement\NCKernel\Templates` of the installed product contains `Mill`, `TurnMill` and the robot
   templates `ABB Robot` and `Kuka Robot`; list the folder to see which templates your installation has. Create the
   project with the interpreter creator: **Create interpreter** in the list of utilities
   (extensions) of the CAM system, or **Interpreter manager** in Tuner — both start the same program. It copies the
   template, renames the files after the new folder, fills in the SDK package prefix, the program file name in
   `.vscode\launch.json`, and one new GUID for both `GetIdentifier` and `LibraryID`. It refuses a folder that already
   exists. After it has run, check by hand what it does not do:
   - `ID` in the `.snci` file is still all zeros: write a new GUID there;
   - the SDK package version in the `.csproj` is the one the template was made with — a prerelease version (`-dev`,
     `-rc`, sometimes with `*`) or a version of an older major version — not the one of the installed product: replace
     it (see "The SDK package and the product versions" below);
   - the `.snci` lies in `bin\Debug\`, which is build output: move it to the project folder (same section);
   - the environment variable for the debugger is set only if you press the button that stores the program path in the
     creator's window, and only one of them (see "Debug" below);
   - the general fields of the `.snci` keep the template's sample values — `Description`, `CNCSystem`, `FileExtension`
     (`*.cnc` in `Mill`), `Authors`, `Company`, `Date`: fill them in for the real control;
   - `NetNamespaceClass` names the class the CAM system creates (`STNCInterpreter.Interpreter`, the class in
     `Entry.cs`): if you rename that namespace or class, change it too;
   - the template comes from one control family: remove its handlers for words that mean something else on your control
     (fixed cycles G70–G76 or G81–G89 of one control are other functions on another) instead of leaving them active.

A child interpreter adds to a parent at run time; it is not a copy of the parent's sources. When the creator makes a
child, it writes the parent's `LibraryID` into `ParentID` and leaves `ParentFileName` empty. Correct both by hand:
`ParentID` must equal the parent's `ID`, and `ParentFileName` must name the parent's `.snci` — without it the kernel
loads no parent at all. A child calls the parent's methods where it adds to them (for example the parent's `TransLine`),
by the rules in "Inheritance and protection" of "Develop native interpreters" (`develop-native-interpreter`), which come
from the documentation on interpreter inheritance and hold for .NET as well.

The creator makes the child from a full copy of the template, so it starts as a complete interpreter of its own: its
registers replace the parent's registers of the same name, and nothing in it calls the parent. The base class keeps the
parent as `ParentInterpreter`; remove what the parent must handle and call the parent's methods as the inheritance rules
say. The kernel finds the parent by the file name in `ParentFileName`: in the child's own container, then in the
container's folder, in the child's folder, in the product's interpreters folder and in its containers folder. Where a
folder does not hold the file, the kernel also follows the `.lnk` shortcuts to folders found in it and in its subfolders
(one level of shortcuts; not in the folder of a child loaded from a container). It takes the first file with that name
and stops with an error if that file's `ID` differs from `ParentID`. During F5 the child's `.snci` lies in `bin\Debug`,
so the parent must be found from there.

## The SDK package and the product versions

The interpreter references the package `<Org>.NCInterpreterSDK.Net`, where `<Org>` is the package prefix of the
product's vendor. Which version to use:

1. Read the version the installed product was built with: `Bin64\STNCInterpreterSDKProject.stbuildresult.json`,
   `build_results.versions`. It tells you the package name and the major version. A Tuner installation may not have
   this file: read it from the CAM system of the same release (it runs the same .NET version; ask the user when several
   installations qualify). Where Tuner has the file, the number is set by the build of Tuner, which does not publish the
   SDK packages, so a package with exactly that number may not exist in the feed.
2. Use the newest **released** version of the package (a version without `-dev`, `-rc` and similar suffixes) that has
   the same major version and is not newer than the version from step 1. Take it from the public package feed of the
   product's vendor: the documentation section on AI-assisted development of that product names the feed and, when the
   feed is not one the .NET SDK uses by default, the command that adds it. The feed's search may show an older newest
   version than its package list: read the list of versions of the package itself.

A nightly or test build of the product records a development version (with a suffix such as `-dev.2`): a customer cannot
download it, so never write it into a project that leaves your computer. Do not use a floating version (`<major>.0.*`)
and do not choose one from memory. A project with an unknown version or an unreplaced `$(package_namespace)` does not
build; the debugger start then fails, or the product loads an older DLL left in the output folder — check the build
result before judging the behavior.

Each product version has its own .NET version. Read it from the installation: `<TargetFramework>` in the `.csproj`
files of its templates (`Supplement\NCKernel\Templates`), or `tfm` in the `runtimeconfig.json` of its program in
`Bin64` (in Tuner, `ltuner.runtimeconfig.json`). Read the package name from the same `stbuildresult.json` as in
step 1. One project can serve several product versions: replace the template's `<TargetFramework>` with the list of the
targets of those versions and give each target its own package version, as below for two versions that run
.NET 10 and .NET 8. If both properties stay, only one target is built. The robot templates target the `-windows`
variant (`net10.0-windows`): there use the `-windows` names in the list and in the conditions.

```xml
<TargetFrameworks>net10.0;net8.0</TargetFrameworks>
<PackageReference Include="<Org>.NCInterpreterSDK.Net" Version="<version for the newer product version>"
                  Condition="'$(TargetFramework)' == 'net10.0'" />
<PackageReference Include="<Org>.NCInterpreterSDK.Net" Version="<version for the older product version>"
                  Condition="'$(TargetFramework)' == 'net8.0'" />
```

When one target needs an interface that only the newer released package has, guard that code with the target's symbol
(`#if NET10_0_OR_GREATER`) and give the older product version a fallback that the README describes.

The template's `.csproj` sets `OutDir` and `PublishDir` to `bin\Debug\`: with two targets both builds would write into
that one folder and overwrite each other. Make both depend on the target (`bin\Debug\<product version>\`). If you remove
them instead, `build` writes to `bin\Debug\net10.0` and `bin\Debug\net8.0`, but `publish` writes to
`bin\Release\<target>\publish\`, away from the folder the launch configuration uses. Keep the `.snci` and
`InterpreterSettings.ini` in the project folder, not in `bin` (build output is not kept in version control), and copy
them into every output folder:

```xml
<ItemGroup>
  <None Update="<Name>.snci" CopyToOutputDirectory="PreserveNewest" />
  <None Update="InterpreterSettings.ini" CopyToOutputDirectory="PreserveNewest" />
</ItemGroup>
```

**The folder name and the `.csproj` name must be identical.** The template's `.vscode\launch.json` passes
`Bin\Debug\${workspaceFolderBasename}.snci` to the program, and its build task builds the project of the folder. With
several targets that path no longer exists: write one launch configuration per product version with the path of that
version's output folder. The template's `publish` task runs `dotnet publish` without a target; with several targets give
it `-f net10.0` or `-f net8.0`, one task per product version. Keep the `.snci`, the DLL name and `LibraryFileName_Net`
inside the `.snci` consistent.

## What goes where

The templates split the interpreter into files by role. Keep that split; a new feature goes into the file of its role.
Not every template has every file: `Mill` has no lathe cycles and no `Interpreter.Types.cs`; the robot templates read
their programs in `Interpreter.Transline.cs` and have no `Interpreter.Registers.cs` and no `IniFile.cs`; the ABB robot
template also has `Program.cs` and `AskUserForm.cs`.

| File | Contains |
|---|---|
| `Entry.cs` | the entry point the CAM system creates the interpreter through, and its GUID |
| `Interpreter.Registers.cs` | the registers: every address and G/M function the kernel reads itself, grouped as in the control's manual |
| `Interpreter.CommandHandlers.cs` | `Cmd…` methods called when a register of the block is executed (`G1`, `X`, `M3`) |
| `Interpreter.CommandTypes.cs` | the names of the commands a block puts into its queue |
| `Interpreter.Execution.cs` | executing the queued commands: motion, spindle, tool change |
| `Interpreter.Core.cs` | the state of the interpreter and the kernel calls (`TransLine`, `DefineRegister`, `BeforeInterprete`, `AfterInterprete`) |
| `Interpreter.Initialization.cs` | analyzer setup, machine axes, reading the INI file |
| `Interpreter.DrillingCycles*.cs`, `Interpreter.LatheCycles*.cs` | cycles and their move events |
| `Interpreter.Transline.cs` (robots) | reading the robot program statements |
| `Interpreter.Types.cs` | small types the interpreter uses |
| `IniFile.cs` | reading `InterpreterSettings.ini` |

A construction the kernel cannot read as a register — a numbered axis with `=`, an expression, a call with brackets, a
string — is read in `TransLine` (see "Words the kernel cannot read" in "How the kernel reads a block"); give such
readers their own file (`Interpreter.Statements.cs`, `Interpreter.Cycles.cs`, `Interpreter.ProgramFlow.cs`) when there
are many.

## Known defects of the templates

Check each one in the template you started from and fix it in your copy:

- **The INI file is never read.** `IniFile.cs` declares the Windows functions `GetPrivateProfileString` and
  `GetPrivateProfileSectionNames` without their Unicode names. Write `EntryPoint = "GetPrivateProfileStringW"` (and
  `…SectionNamesW`, `WritePrivateProfileStringW`) in each `LibraryImport`. Without it reading fails, the error is
  caught, and the log has only an information line starting with `Error reading settings file`, so every setting looks
  ignored and a log filtered by errors shows nothing.
- **The INI file is skipped when one interface is missing.** `Interpreter.Initialization.cs` returns before reading the
  file when the origin interface (`INCT_AddOriginByShiftAndRotate`) was not found, with only an information line in the
  log. Read the file independently of that interface.
- **Long values break reading.** `ReadString` passes the buffer size in bytes (`buffer.Length`) where Windows expects
  characters, so a value longer than 1023 characters (a long list of M codes) is written past the end of the buffer and
  reading fails. `GetSections` has the same error. Pass the size in characters and read again with a doubled size while
  the result fills the buffer (`size - 1` for a value, `size - 2` for the list of sections).
- **A one-digit tool number loads no tool.** `TurnMill` splits the `T` word in halves (tool, offset), so `T1` gives an
  empty tool part: no tool is loaded and `1` becomes the offset. Check against the `T` format of the control.
- **Lathe cycle register names disagree.** In `TurnMill`, the names looked up in `Interpreter.Core.cs` (`P LCYCLE`) and
  the names declared in `Interpreter.Registers.cs` must be identical; a difference silently reads the word as another
  register (see "Choosing a register by state" in "How the kernel reads a block").
- **Lathe cycles G70 and G73.** Check the feed of the finishing cycle G70 and the side the passes of G73 run on against
  the control's manual and a real program; both were found wrong in an interpreter built from this template.

When you fix a defect of a template in your interpreter, tell the user, so that it can be fixed in the template too: a
fix in your copy does not reach the next interpreter created from the template, and a fix in the template reaches users
only with a product version that ships it.

## Make variations a setting, not a code change

Programs of one machine name the same thing differently: an axis is `B90` in one program and `B1=90` in another, the
postprocessor of one shop writes M codes another does not. Put such variations into `InterpreterSettings.ini` next to
the DLL, so a support engineer can adapt the interpreter without building it.

The templates read only one key (`[Main] AddOriginFlipMode`) and ship no `InterpreterSettings.ini`. Every key below is
therefore written once in code — the key, its check and its log line — and from then on the variation is a setting. A
good set of keys:

```ini
[Axes]
; numbered machine axes that occur in the programs (axis addresses of the machine schema)
MachineAxes = B1, Cs1
; axis names of the control that differ from the machine schema: name in the program : axis of the schema
ChannelAxisNames = C1:Cs1, B:B1
[MachineFunctions]
; M codes of the machine that do not move it (clamps, doors, measuring)
M = 10, 11, 50, 51, 120, 121
[Words]
; words, addresses with a value, and calls with brackets that do not change the simulated toolpath
Keywords =
Addresses =
Procedures =
[Trace]
; yes - write every block and the commands it produced to the debug console and the CAM log
Enabled = no
```

Every key is read once at start, every malformed value is written to the CAM log as a settings error, and the values
taken are logged in one line, so the user can see what the interpreter uses. A value of the INI file is one line: INI
files have no continuation lines. A word the interpreter already knows must not be added again from the INI file: a
setting must not be able to switch off a supported word.

An axis name mapping must apply to every spelling of the axis the census found — `B90`, `B=90`, `B1=90`, `B=DC(30)` —
not only to the form one reader handles. Test each spelling against the machine schema: the SDK's helper for axis
indexes warns about an axis name it does not know once per name and then silently skips its values.

Machine-specific numbers — a safe position, a retract height — belong in the INI file or come from the program (its
machine-coordinate blocks), not in constants in the code.

## Code style

Follow the style of the templates, so the code reads as one piece:

- names from the control's own vocabulary that a machine operator recognizes (`CmdToolCall`, `CmdDwell`,
  `WorkpieceCoordinateSystem`), not internal jargon;
- one region per group of G functions, as in the control's manual;
- the register table only binds a register to its `Cmd…` method — no logic in lambdas there; each queued command is
  executed by its own `Execute…` method; keep the names and numbers of the template's command types and add new ones
  after them;
- a register's `name` is a short identifier in the control's terms; a register that reads another word as a parameter is
  named `<address> <TAG>` (`X DWELL`, `F THREAD`); its `comment` is a short English noun phrase without G numbers;
- an English comment above each block saying what it does, and XML documentation on every method and field —
  interpreters are read by people with basic programming skills, so they carry more comments than other code. A general
  rule of the workspace that keeps comments short does not apply here: compare the comment density of your files with
  the template's files before calling the style done;
- keep the line endings and the encoding of the template's files (many are CRLF without a byte order mark). Editors and
  scripts convert them silently, and the diff then shows every line as changed: check new and changed files by their
  bytes before committing;
- keep the state of the interpreter in fields of the interpreter object, not in `static` fields: the CAM system loads
  the DLL and creates a new instance for every calculation of an operation, the parent and the contour of a cycle get
  instances of their own, each in a load context of its own, so a static value neither survives the calculation nor is
  shared with the parent; Tuner keeps one instance for each channel, from its first operation to its last, so modal
  state and any static value there carry over from one operation to the next. Reset per-operation state in
  `NextOperation`;
- read numbers in programs with `CultureInfo.InvariantCulture`, so that `.` is the decimal separator whatever the
  Windows language is.

## Unit tests

Keep the decisions that need no kernel in classes that do not reference the SDK: reading numbers and expressions,
decoding cycle parameters, the rules for axes, spindles and the plane, parsing the INI file. Cover them with a small
test project that links those source files, and run it for every target framework. Test every spelling from the census,
the limits and malformed input, and check that each test fails when the code it guards is broken — a test that still
passes after you delete the condition it is about proves nothing. Unit tests complement the runs of the real programs
("Verify interpretation"); they never replace them, because the kernel's behavior is not in them.

## Debug

You need Visual Studio Code with the C# extension of Microsoft (it contains the debugger the templates' launch
configurations use). The template's `F5` configurations build the interpreter and start the CAM system or Tuner with it;
a breakpoint in a `.cs` file stops when a program is simulated. The template's `launch.json` has three configurations:
**Launch CAM** starts `${env:NCKernelDir}/<program file>` with `/Interpreter:<project folder>\Bin\Debug\<folder
name>.snci`, **Launch Tuner** starts `${env:TunerDir}/ltuner.exe` with `/i` and the same `.snci`, and **.NET Core
Attach** attaches the debugger to a CAM system or Tuner that is already running. The program folder is taken from the
environment variables `NCKernelDir` (CAM system) and `TunerDir` (Tuner). The interpreter creator stores one of them —
the one of the product it was started from — when you press its button for the program path, and it writes the program
file name into `launch.json` in place of `${env:CAMName}`; a template copied by hand, without the creator, keeps
`${env:CAMName}`, which nothing sets, so write the file name there yourself. The creator writes the variable into the
user's environment and asks you to sign out of Windows or restart the computer; at the least, close VS Code and start it
again from the Start menu or Explorer, not from a terminal that was open before. When a variable is missing, write the
program path into `launch.json` instead — the standard installation folder of each product, one configuration per
product version, never a folder that exists only on your computer.

Turn on **Use logs** and **Use log interaction with the interpreter** before debugging (System setup → Additional →
Logs, the same in the CAM system and in Tuner; the second can be switched on only when the first is on). Without them
the log gets none of the kernel's messages about the words it reads and none of the lines the interpreter writes with
`Kernel.Log`. A message the user must see even with the log off — a word that is not simulated, an interface that is
missing — goes through `Kernel.Notify`, which shows it in the notification panel.

To simulate a program: in the CAM system create an operation that works by an NC program, paste or load the program
text, choose the interpreter in the operation's strategy, and calculate the operation.

If a breakpoint is never hit, check in this order: the build produced debug symbols (a `.pdb` next to the DLL; a project
or script that sets `DebugType` to `none` makes every breakpoint look dead); the operation really uses your interpreter
(not another one with the same `LibraryID`); the build before the start succeeded (the template's build task keeps its
terminal in the background — open the terminal panel and read the build result); the `.snci` passed to the program is
the one in the output folder of the product version you started.

When a colleague's or a customer's project fails on the first block, read first the interpreter file stored in the
strategy of the NC operation of that project and the project's log: an interpreter file that is not found, or a DLL that
cannot be loaded, means the interpreter never loaded, and every word then fails. The CAM system reports every failure to
load a .NET interpreter the same way — `External library don't support NCT interface:` and the path (in the English
interface; the text follows the interface language) — and the reason is lost: the DLL is missing beside the `.snci`, a
dependency or the `.deps.json` is missing, the DLL was built for another .NET version, or an exception was raised while
the interpreter object was being created (usually while creating the registers). When the CAM system reports this
message, check the files above, then create the interpreter class in a small console program with the same SDK package
to see the real error message.

What the interpreter did with each block is visible through a trace you add once (the `[Trace]` key above, in a file of
its own such as `Interpreter.Trace.cs`): with `Enabled = yes` the block text and the commands it produced appear in the
debug console and, with the interaction log on, in the CAM log (`%AppData%\<vendor>\<product>\Version <n>\Log`; each
process of the CAM system or Tuner writes a file of its own, named after the program and the process ID, such as
`<program>-<process ID>.log`). Write the trace from the same code that outputs the commands, not from a parallel copy
of its logic, or the trace and the simulation will disagree.

## Rules

- Do not change the product's templates, kernel or DLLs to make an interpreter work; record what the product would have
  to change instead.
- Do not use SDK members that the released package does not contain: read them from the package's declarations and
  XML documentation.
- Keep the project building after every change; make one change at a time.
- Keep the template's build and `F5` debugging: no build scripts, environment variables or extra project logic in their
  place. A colleague must be able to open the folder, press `F5` and stop at a breakpoint.
- Do not put build output, customer programs or logs into the source tree.

## Done means

The project builds unchanged, then with the change, for every product version it targets, with a released SDK package;
folder, project, `.snci` and DLL names agree and both identifiers of the `.snci` are unique; the known defects of the
template are fixed or named; variations of the programs are settings with logged values; the code follows the template's
structure, style, line endings and encoding; the logic that needs no kernel has unit tests that pass for every target;
the change was debugged or traced on a real program; and "Verify interpretation" has been followed.
