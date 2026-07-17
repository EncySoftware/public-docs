# CLData

CLData is the intermediate data that the CAM system passes to a postprocessor: an ordered list of
**technology commands** (tool movements, spindle and coolant control, tool changes, canned cycles,
auxiliary functions, etc.), each carrying a set of parameters. A postprocessor reads CLData and
generates the NC program for a particular machine and control system.

Both postprocessing subsystems — the [Postprocessors generator (sppx postprocessors)](../sppx/readme-sppx.md)
and the [.NET postprocessors](../dotnet/readme-dotnet.md) — work with **the same** CLData. The module
that reads and writes CLData is shared between them; the low-level interaction with native code is
hidden, and each subsystem exposes the data through convenient wrappers. **Only the access syntax
differs between the two subsystems** — the commands and their parameters are identical.

This section documents the CLData commands once, for both subsystems. For every command the parameters
are described in a syntax-neutral way first, followed by separate paragraphs showing how to read them
from sppx and from .NET. Use the access form of your own subsystem and do not mix the two syntaxes.

## What CLData contains

CLData is organized as a small hierarchy - a project, its files, the commands inside each file, and the
parameters of each command:

- **Project** - the whole CAM project. Apart from its operations it carries project-level information -
  the machine schema, the parts and workpieces, the units, the setup stages, and so on.
- **Files** - the project's CLData is split into files. There is one file for each CAM operation, an
  optional file for each subprogram, and one project-level file that holds the project information and
  contains no commands.
- **Commands** - each file is an **ordered** sequence of technology commands: tool movements, spindle and
  coolant control, tool changes, canned cycles, section markers, auxiliary functions, and so on. The
  order is the order in which the operation is performed.
- **Parameters** - every command carries a set of parameters that describe it: the coordinates of a move,
  the spindle speed, the tool number, a cycle's depths and offsets, and so on. Each command type has its
  own set of parameters.

A postprocessor walks this hierarchy - file by file, command by command - and for each command reads the
parameters it needs to build the corresponding NC block. The next section shows a real listing of such a
project; the sections after it explain how to reach the files, commands and parameters from postprocessor
code.

## The structure of a CLData listing

A project's CLData is not one flat list of commands but a set of **files**, and inside each file the
commands are grouped into nested **sections**. Knowing this layout makes the command list readable and
lets a handler react to the toolpath structure. The example below is a real listing of a simple
mill-turn project, produced by a small postprocessor that walks every file and command (the same
file-walking pattern as the example in [CLData files](functions/files.md)).

### Files

- A project's CLData is a list of files, numbered from `0`. **File numbering is 0-based in both
  subsystems.** The numbering of commands *inside* a file, however, differs: it is **1-based in sppx**
  (`for c = 1 to CldFile[f].CmdCount`) and **0-based in .NET** (`for (int c = 0; c < file.CmdCount; c++)`).
- **File `0`** is always the project-level file (type `CAMProject`). It carries no commands - it holds
  the project information, read with the [Project operator](functions/project.md).
- Every CAM operation becomes one file of type `TechOperation`, in the order of the operations list.
- Files of type `NCSub` are optional - they exist only when the project uses subprograms or
  cycles-with-subprograms. Unlike operation files, they are **not** translated automatically; a
  postprocessor emits them by calling the NC-subroutine operators explicitly (see [Operators of work
  with NC-subroutines](../sppx/language-description/operators/operators-of-work-with-nc-subroutines/readme-operators-of-work-with-nc-subroutines.md)).

```text
File 0   CAMProject      - project-level data, no commands
File 1   NCSub           - optional: subprogram / cycle bodies
File 2   NCSub
File 3   TechOperation   - one file per CAM operation, in operations-list order
File 4   TechOperation
 ...
File 15  TechOperation
```

### Sections inside an operation

- Each operation file is wrapped by [`PPFUN TECHINFO(58)`](commands/ppfun/techinfo.md) …
  [`PPFUN ENDTECHINFO(59)`](commands/ppfun/endtechinfo.md) - the operation start / end, carrying the
  operation's technological data.
- Commands are grouped into nested sections with the [`STRUCTURE`](commands/structure.md) command
  (`ON(71)` opens a section, `OFF(72)` closes it). The three top-level sections are **Header**, **Body**
  and **Tail**; **Header** contains an **Approach** sub-section and **Tail** a **Return** sub-section.
  `STRUCTURE` is also used to group the cutting moves by region / tool pass - for a milling operation,
  for example, the **Body** is split into depth **Level** groups and each level into **Offset** passes
  (see `File 15` below). In the command list these nested sections appear as indentation.
- The **Header** carries the set-up commands, typically in this order:
  - the first [`COMMENT`](commands/comment.md) - the CAM operation name;
  - [`ORIGIN`](commands/origin.md) - the base coordinate system this operation's toolpath is output in;
  - [`LOADTL`](commands/loadtl.md) - the tool used in the operation;
  - the [`COMMENT`](commands/comment.md) right after the tool, starting with `@` - the tool name;
  - [`CUTCOM`](commands/cutcom.md) - activates the tool compensation;
  - [`PLANE`](commands/plane.md) - activates the working plane;
  - [`SPINDL`](commands/spindle.md) - starts the spindle;
  - [`FROM`](commands/from.md) - the tool's initial position; it performs no motion, it only states
    where the tool already is when the operation starts.
- The set of movement commands depends on the machine kind: [`GOTO`](commands/goto.md) /
  [`CIRCLE`](commands/circle.md) for 2D/3D mill-turn toolpaths (turning and drilling cycles additionally
  emit [`EXTCYCLE`](commands/extcycle/extcycle.md) and [`MULTIGOTO`](commands/multigoto.md) for
  positioning, as in the example below), [`MULTIGOTO`](commands/multigoto.md) /
  [`MULTIARC`](commands/multiarc.md) for 5-axis machines and robots, and
  [`EDMMOVE`](commands/edmmove.md) for wire-EDM. The rest of the structure stays largely the same.
- Key points of the toolpath are marked with **tags** - a [`PPRINT`](commands/pprint.md) whose text
  starts with `#` (for example `#KeyPoint: StartCutting`, `#Approach:…`, `#Return:…`). A postprocessor
  reacts to a tag or skips it so the marker does not reach the NC program; see
  [Toolpath tags](commands/pprint.md#toolpath-tags). These lines are marked `! toolpath tag` in the
  listing below.

The listing below walks the whole project - the project file, the subprogram files and the operation
files - with long parameter lists trimmed to `…` and the repeating passes collapsed; indentation
shows the `STRUCTURE` nesting (per-command indices are omitted):

```text
File 0 — CAMProject   (project level; carries no commands)

File 1 — NCSub   (a subprogram / cycle body; output only when the postprocessor calls it explicitly)
COMMENT    "Geometry"
PPFUN      STARTSUB(50), 1
GOTO       X 67.8, Y 0, Z 0
PPRINT     "#KeyPoint: StartCutting"                    ! toolpath tag
FEDRAT     F 0.5, MMPR(316), K 0
GOTO       X 30.703, Y 0, Z 0
GOTO       X 33.362, Y 0, Z 2.659
PPFUN      ENDSUB(51), 1

File 2 — NCSub   (another subprogram body; same shape as File 1 — omitted)

File 3 — TechOperation "Lathe facing"   (turning)
STRUCTURE  ON(71)  TYPE "HeaderSection", Comment "$Header$"
  PPFUN      TECHINFO(58), 250, 30.703, 0, 0, 979.484, …    ! the operation starts
  STRUCTURE  ON(71)  TYPE "String", Comment "Header"
    COMMENT    "Lathe facing"                               ! operation name
    ORIGIN     X 0, Y 0, Z 265, PPFUN 0, N 54, …            ! base coordinate system (G54)
    LOADTL     N 2, ToolChanged 1, X 15, Y 125, …           ! tool
    COMMENT    "@IC16 Re0.2 R OD cutting tool"              ! tool name (starts with @)
    CUTCOM     ON(71), LENGTH(9)2, …, LEFT(8)               ! tool compensation
    FROM       COUNT 10, MACHINE, X 100, Y 0, Z 500, …      ! initial tool position (no motion)
  STRUCTURE  OFF(72) TYPE "String", Comment "Header"
  STRUCTURE  ON(71)  TYPE "String", Comment "Approach"
    STRUCTURE  ON(71)  TYPE "Approach", Comment "Approach"
      PPRINT     "#Approach:[Rule 1]=C; Z10; X; Z"      ! toolpath tag
      SELWORKPIECE"Table"
      SPINDL     ON(71), NO -1000, K 0, MODE CSS(2), SPEED -150   ! spindle
      RAPID      N 10000
      MULTIGOTO  COUNT 1, MACHINE, Z 10, …
      MULTIGOTO  COUNT 1, MACHINE, X 67.8, …
      MULTIGOTO  COUNT 1, MACHINE, Z 2.659, …
    STRUCTURE  OFF(72) TYPE "Approach", Comment "Approach"
  STRUCTURE  OFF(72) TYPE "String", Comment "Approach"
STRUCTURE  OFF(72) TYPE "HeaderSection", Comment "$Header$"
STRUCTURE  ON(71)  TYPE "BodySection", Comment "$Body$"
  GOTO       X 67.8, Y 0, Z 2.659
  COOLNT     ON(71), N 1, #1
  FEDRAT     F 0.5, MMPR(316), K 0
  EXTCYCLE   ON(71)   LATHEFINISH(400), 1, 0, 3, 0, 0.3, …
  EXTCYCLE   CALL(52) LATHEFINISH(400), 1, 0, 3, 0, 0.3, …
  EXTCYCLE   OFF(72)  LATHEFINISH(400), 1, 0, 3, 0, 0.3, …
STRUCTURE  OFF(72) TYPE "BodySection", Comment "$Body$"
STRUCTURE  ON(71)  TYPE "TailSection", Comment "$Tail$"
  STRUCTURE  ON(71)  TYPE "String", Comment "Return"
    STRUCTURE  ON(71)  TYPE "Return", Comment "Return"
      PPRINT     "#Return:[Rule 1]=Z10; X; Z; C"        ! toolpath tag
      RAPID      N 10000
      MULTIGOTO  COUNT 1, MACHINE, Z 10, …
    STRUCTURE  OFF(72) TYPE "Return", Comment "Return"
  STRUCTURE  OFF(72) TYPE "String", Comment "Return"
  PPFUN      ENDTECHINFO(59), 250, 30.703, 0, 0, 979.484, … ! the operation ends
STRUCTURE  OFF(72) TYPE "TailSection", Comment "$Tail$"

…  (Files 4…14 — the other operations, each the same Header / Body / Tail shape — omitted)

File 15 — TechOperation "2D contouring"   (milling)
STRUCTURE  ON(71)  TYPE "HeaderSection", Comment "$Header$"
  PPFUN      TECHINFO(58), 250, -47.996, -289.976, -16, …  ! the operation starts
  STRUCTURE  ON(71)  TYPE "String", Comment "Header"
    COMMENT    "2D contouring"                             ! operation name
    ORIGIN     X 0, Y 0, Z 274, PPFUN 0, N 55, …           ! base coordinate system (G55)
    LOADTL     N 1, ToolChanged 1, …, D 8, L 40, …         ! tool
    COMMENT    "@Cylindrical mill L40, D8"                 ! tool name (starts with @)
    PLANE      XY                                          ! working plane
    SPINDL     ON(71), NO 10544.01, K 0, MODE RPM(0)       ! spindle
    CUTCOM     ON(71), LENGTH(9)1, …, LEFT(8)              ! tool compensation
    FROM       COUNT 10, MACHINE, X 100, Y 0, Z 500, …     ! initial tool position (no motion)
  STRUCTURE  OFF(72) TYPE "String", Comment "Header"
  STRUCTURE  ON(71)  TYPE "String", Comment "Approach"
    STRUCTURE  ON(71)  TYPE "Approach", Comment "Approach"
      PPRINT     "#Approach:[Rule 1]=C; Z10; X; Z"      ! toolpath tag
      RAPID      N 10000
      AXESBRAKE  COUNT 1, AxisCPos(3) OFF(72)
      MULTIGOTO  COUNT 1, MACHINE, C 90, …
      MULTIGOTO  COUNT 1, MACHINE, Z 10, …
      MULTIGOTO  COUNT 1, MACHINE, X -28.715, …
      MULTIGOTO  COUNT 1, MACHINE, Z 0, …
      MULTIGOTO  COUNT 1, MACHINE, Y -1.804, …
    STRUCTURE  OFF(72) TYPE "Approach", Comment "Approach"
  STRUCTURE  OFF(72) TYPE "String", Comment "Approach"
STRUCTURE  OFF(72) TYPE "HeaderSection", Comment "$Header$"
STRUCTURE  ON(71)  TYPE "BodySection", Comment "$Body$"
  STRUCTURE  ON(71)  TYPE "String", Comment "Level: -4"      ! first depth level
    STRUCTURE  ON(71)  TYPE "String", Comment "Offset 2"     ! first offset pass at this level
      RAPID      N 10000
      GOTO       X -28.715, Y -1.804, Z 0
      GOTO       X -28.715, Y -1.804, Z -3
      AXESBRAKE  COUNT 1, AxisCPos(3) ON(71)
      COOLNT     ON(71), N 1, #1
      FEDRAT     F 100, MMPM(315), K 256
      GOTO       X -28.715, Y -1.804, Z -4
      FEDRAT     F 100, MMPM(315), K 4
      GOTO       X -28.716, Y -3.004, Z -4
      GOTO       X -32.716, Y -3.001, Z -4
      FEDRAT     F 200, MMPM(315), K 0
      GOTO       X -39.887, Y -2.994, Z -4
      CIRCLE     XC -0.086, YC -0.024, ZC -4, R -39.911, XE -39.882, YE 3, ZE -4
      GOTO       X -32.725, Y 3.001, Z -4
      …
    STRUCTURE  OFF(72) TYPE "String", Comment "Offset 2"
    STRUCTURE  ON(71)  TYPE "String", Comment "Offset 1"     ! next offset pass — same shape — omitted
      …
    STRUCTURE  OFF(72) TYPE "String", Comment "Offset 1"
    STRUCTURE  ON(71)  TYPE "String", Comment "Offset 0"
      …
    STRUCTURE  OFF(72) TYPE "String", Comment "Offset 0"
  STRUCTURE  OFF(72) TYPE "String", Comment "Level: -4"
  …  (Levels -8, -12, -16 — the same offset passes at each depth; then the whole set repeats after
      each C-axis rotation MULTIGOTO C 180 / 270 / 360 — a lot of repeating passes, omitted)
STRUCTURE  OFF(72) TYPE "BodySection", Comment "$Body$"
STRUCTURE  ON(71)  TYPE "TailSection", Comment "$Tail$"
  COOLNT     OFF(72), N 1, #1
  STRUCTURE  ON(71)  TYPE "String", Comment "Return"
    STRUCTURE  ON(71)  TYPE "Return", Comment "Return"
      PPRINT     "#Return:[Rule 1]=Z10; X; Z; C"        ! toolpath tag
      RAPID      N 10000
      MULTIGOTO  COUNT 1, MACHINE, Z 10, …
      GOHOME     COUNT 1, MACHINE, X 100, …
      GOHOME     COUNT 1, MACHINE, Z 500, …
      GOHOME     COUNT 1, MACHINE, Y 0, …
    STRUCTURE  OFF(72) TYPE "Return", Comment "Return"
  STRUCTURE  OFF(72) TYPE "String", Comment "Return"
  CUTCOM     OFF(72), LENGTH(9)0, …                         ! compensation off
  SPINDL     OFF(72), NO 0, K 0                             ! spindle off
  PPFUN      ENDTECHINFO(59), 250, -47.996, -289.976, …     ! the operation ends
STRUCTURE  OFF(72) TYPE "TailSection", Comment "$Tail$"
```

## Access model

A command's parameters come in two flavours:

- **Numeric parameters** — a flat array of real numbers, addressed by position. This is the original,
  legacy form.
- **Named / structured parameters** — typed values addressed by name, possibly nested (objects, arrays).
  This is the modern form used by newer commands (and available for most parameters of the older ones).
  The naming model is the same one described in
  [XML properties — access from code](../../xml-properties/using-from-code.md).

The table summarizes the ways to read them. Details and examples are given per command in the command
reference; the access pattern is always the same.

| Access form | sppx | .NET | Notes |
|---|---|---|---|
| Numeric array, by index | `cld[i]` | `cld[i]` | Common to both. The array is filled with the current command's parameters before the command is processed. |
| Numeric element, by short name | `cld.X`, `cld.N` … | — | **sppx only.** A flat, duplicate accessor for some numeric elements. Not available in .NET. |
| Named / structured, by name | `cmd.Str["Name"]`, `cmd.Flt["Name"]`, `cmd.Int["Name"]`, `cmd.Ptr["Name"]` | `cmd.Str["Name"]`, `cmd.Flt["Name"]`, `cmd.Int["Name"]`, `cmd.Ptr["Name"]` | Same grammar in both (dotted paths, array keys `Name(Key)`, pointer chaining). See [XML properties — access from code](../../xml-properties/using-from-code.md). |
| By stable parameter code | `CmdPrm.Flt[code]` | `cmdPrm.Flt[code]` | Used by the extended / probing cycles, where parameters are addressed by a fixed code so their order can change without breaking postprocessors. |
| Strongly-typed command wrapper | — | `cmd.<Property>` (e.g. `cmd.R`, `cmd.IsCSS`) | **.NET only.** Each command handler receives a typed `cmd` object with named, documented properties. The modern .NET way; see the API reference. |

### sppx

In sppx the current command's numeric parameters are placed in the predefined `cld` array before the
command's program runs, so `cld[1]`, `cld[2]`, … address them by position; some elements also have
short member names such as `cld.X`. Structured parameters are read by name with the `cmd` operator
(`cmd.Str["…"]`, `cmd.Flt["…"]`, `cmd.Ptr["…"]`), and the extended cycles use code-based access
`CmdPrm.Flt[code]`. These accessors are described in
[CLData access functions and operators](functions/functions.md).

### .NET

In .NET a postprocessor implements a typed handler per command, for example
`OnSpindle(ICLDSpindleCommand cmd, CLDArray cld)`. Inside the handler you can:

- use the **strongly-typed** `cmd` object — named, documented properties such as `cmd.IsCSS`,
  `cmd.RPMValue`, `cmd.R`, `cmd.Center` (this is the recommended, modern form);
- read named / structured parameters with `cmd.Str["Name"]`, `cmd.Flt["Name"]`, etc.;
- read the raw numeric array `cld[i]` (the same indices as in sppx);
- use code-based access `cmdPrm.Flt[code]` for the extended cycles.

The typed command interfaces (`ICLD…Command`) and all their properties are described in the .NET SDK
**API reference** — see [.NET references](../dotnet/references.md).

## Locating commands (browsing CLData)

Besides the current command, a postprocessor can browse other commands of the file (look ahead/back,
find the next command of a given type, read project / operation context).

- **sppx:** `CurCode`, `NextCode`, `CodeOfCmd`, `GetCld`, `FindCld` / `GFindCld`, the `CLDFile`
  operator and the `Project` operator.
- **.NET:** `CurrentFile.Cmd[i]`, `CurrentFile.FindCommand(...)`, `CurrentFile.IndexOfCmd(...)`,
  `CurrentCmd.Next` / `Prev` / `NextMotion` / `PrevMotion`, `CurrentOperation.*`, `CLDProject.*`.

Both forms are documented side by side in [CLData access functions and operators](functions/functions.md).

## Command reference

Each command is documented once for both subsystems (common parameters → access from sppx → access from
.NET). The full list is in [Technology commands description](commands/commands.md).

## Project information in CLData

Static project-level data embedded in CLData (machine schema, parts, workpieces, setup stages, WCS,
units, etc.) is described in [Project information in CLData](project-information.md).

## In this section
- [CLData access functions and operators](functions/functions.md) - reading CLData from postprocessor code
- [Project information in CLData](project-information.md) - static project-level data embedded in CLData
- [Technology commands description](commands/commands.md) - the list of all CLData commands
