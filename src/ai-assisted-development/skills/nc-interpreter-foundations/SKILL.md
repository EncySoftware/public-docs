---
name: nc-interpreter-foundations
description: How the CAM NC kernel reads and executes a block and when interpreter code runs — registers and their parameters, TransLine, DefineRegister, BeforeInterprete, the execution queue with Interprete, AfterInterprete — toolpath formers, coordinates and the first move, spindles, and the known kernel traps that surprise authors. Use when deciding where a word belongs, or when a word is read wrongly, too late, twice or not at all.
---

# How the kernel reads a block

## When to use

When you have to decide where a word belongs, when a word is read wrongly or not at all, and when the order of actions
in a block matters (a spindle before a move, a cycle after it). Read this skill once before the first change to an
interpreter; "Develop .NET interpreters" (`develop-dotnet-interpreter`) refers to it.

## Workflow

1. Find the word in the census of the programs ("Inspect NC programs" (`inspect-nc-programs`)) and in the control's
   manual.
2. Decide which call reads it (the table below): the kernel itself through a register, `DefineRegister`, or `TransLine`.
3. Decide where its effect happens: in the handler of the register, in a queued command, or after the block.
4. Write a short test program with every spelling of the word and check the order of effects in the trace.

## Reading and executing a block

The kernel owns the program; the interpreter is called at fixed points. A block is handled in two passes. First the
kernel **reads** the whole block: every word it recognizes is put into the block's execution queue, nothing is executed
yet. Then it **executes** the queue in order. In a C# interpreter derived from the template the calls are overridden
methods:

| Pass | When | Method | What it is for |
|---|---|---|---|
| start | once, from the constructor of the base class | `CreateRegisters` | declare every address and G/M function the kernel reads itself; field initializers have run, the body of your own constructor has not |
| start | for each interface the kernel hands over | `SetInterface` | keep the interfaces the interpreter needs (see "Interfaces" below) |
| start | once, after all interfaces | `Initialize` | set up the analyzer, the machine axes, read the INI file |
| read | before each word of a line | `TransLine` | read a construction the kernel cannot read as a register; it receives the rest of the current line |
| read | when the kernel meets an address | `DefineRegister` | choose which register an address means in the current state |
| execute | once, after the block is read | `BeforeInterprete` | decisions that need the whole block, before anything in it is executed |
| execute | for each element of the queue, in order | `Interprete` | a register element calls the register's handler (`Cmd…`); a command element calls `ExecuteParameterCommand` |
| execute | after the queue is done; skipped when `EndOfProgram` returns true before an element of the queue | `AfterInterprete` | what must happen after the block: a modal cycle call, resetting one-block states |
| start | before each following part of the same program | `NextOperation` | reset what the next part must not inherit; the templates leave it empty |

Consequences that explain most surprises:

- The handler of a register (`CmdX`, `CmdG`) runs in the execution pass, after `BeforeInterprete` and in the order the
  words stand in the queue — not while the block is read.
- A handler usually does not move the machine itself: it stores the value and adds a command to the queue
  (`Commands.Add`). A command added during execution goes to the end of the queue, after all register elements of the
  block, so the motion of the block is executed once every word of it has been seen. A command added in `TransLine`,
  while the line is read, stands in reading order among the words.
- The kernel skips queue elements that were already executed and stops executing the block before the next element
  once `EndOfProgram` returns `true`; `AfterInterprete` is then not called for that block, unless the element that ended
  the program was the last one in the queue. The base class of the C# SDK sets its
  end-of-program flag back to `false` only in its constructor: reset it in `NextOperation`, because one interpreter
  instance serves every part of a program (see "Known traps").
- `TransLine` sees the rest of the current line before every word, so it is the place for anything the kernel's own
  reader cannot handle.
- How a word without a value is read depends on the register's `valueAvailability`, in every interpreter: `vatOnlyAddr`
  — the word is only an address (`STOPRE`) and the kernel does not look for a value; `vatValue` — a value is required:
  `X` alone is reported as an error ("Value or expression is expected") and never reaches the queue; `vatBoth` — the
  value may be absent: `X` alone reaches the queue with an empty value. Whether the control accepts a word without a
  value is therefore decided when the register is declared, not in its handler. In a C# interpreter the base
  `Interprete` replaces the empty value with `0` only for `vatBoth` registers whose `CanUpdateEmptyValue` you override
  to return `true`. All registers of the templates are `vatValue`.
- A block whose queue stays empty — a line with only a comment, or a line that `TransLine` read completely without
  adding anything to the queue — gets no `BeforeInterprete`, `Interprete` or `AfterInterprete` at all; whatever you
  reset after every block in `AfterInterprete` is not reset for it.

## Native ABI and lifetime

The product loads a native DLL through `NCT_GetInterface`, checks `GetIdentifier` against `LibraryID`, obtains
`GetRegisters`, passes interfaces through `SetInterface`, then calls `Initialize`. During interpretation it may call
`NextOperation`, `TransLine`, `DefineRegister`, `BeforeInterprete`, `Interprete`, `AfterInterprete` and `EndOfProgram`.
At unload it releases the interpreter and calls the library's `NCT_FreeMemory` before unloading parent libraries. A
native implementation must preserve COM reference ownership and calling conventions. A .NET interpreter is loaded
differently: the kernel loads the assembly into a load context of its own, creates the class named in
`NetNamespaceClass` and calls its `NCT_GetInterface` and, at unload, `NCT_FreeMemory` by reflection. In both cases the
parent is loaded and initialized before the child, and if the interpreter implements `INCT_InterpreterState`, its `Load`
is called between `SetInterface` and `Initialize`.

## Interfaces

The kernel hands its interfaces to `SetInterface` one by one. One object — the toolpath (CLData) object — carries many
interfaces at once, but it arrives in a single call, and the base class keeps it only as `CLD`: its other properties
(`AxesBrakes`, `Comment`, `CutTo5d`, `OriginShiftRotate`, `PocketCycleFormer`) stay empty. Take every additional
interface from that CLData object in your `SetInterface` override, as the templates do for the origin interface:

```csharp
if (interfaceObj is INCT_CLData_AutoAxesBrakes brakes)
  _axesBrakes = brakes;
```

When the `.snci` sets `UseGeomCLData`, the kernel hands over a geometric toolpath object instead of the CLData object.
The base class keeps it only as `Comment`, so both `GCLD` and `CLD` stay empty: take `INCT_GeomCLData` from it in your
`SetInterface` override too. The geometric object has no origin, brake or wait interface.

When a stock removal cycle reads its contour through the kernel's stock removal former, the kernel runs a second
instance of the interpreter over the contour blocks and hands it a cycle geometry object in place of the CLData object.
That object offers only the basic `INCT_CLData`, which the base class does not keep at all, so `CLD` is empty and the
extra interfaces are missing in that instance; with `UseGeomCLData` the instance gets the geometric object instead, as
above. The kernel ignores every error of that run: if `Initialize` throws because `CLD` is empty — the `TurnMill`
template does, when it creates its linear motion former — the contour stays empty without any message. Make `Initialize`
work without `CLD`, and test a stock removal cycle on a real program.

That second instance starts fresh: it does not know the plane, the units, absolute or incremental mode or diameter mode
of the program around the cycle. Pass them through `INCT_InterpreterState`: the kernel calls `Save(out state)` on the
running interpreter and its parents before the cycle, and `Load(state)` on the new instance between `SetInterface` and
`Initialize`. Every native turning interpreter implements it; the C# base class and the templates do not.

Because `Load` runs before `Initialize`, an `Initialize` that sets the modal state to its defaults overwrites what was
loaded: keep the loaded values and apply them at the end of `Initialize`. In a .NET interpreter pass the state as an
array of plain values (numbers, strings, booleans): the new instance lives in a load context of its own and cannot cast
a type declared in your assembly. Include everything the contour blocks depend on, such as the labels that delimit the
contour.

Check in `Initialize` that each interface you need arrived, and report it if it did not: a `Kernel.Log` line is written
only when **Use logs** and **Use log interaction with the interpreter** are on (System setup → Additional → Logs), so
use `Kernel.Notify` for what the user must see.

## What the kernel reads by itself

The analyzer settings set in `Initialize` (through `Analyzer`) decide what the kernel reads without the interpreter:
which characters open and close a comment, whether `X=10` assigns a value, block numbers, upper and lower case. The
templates differ here — one accepts `(`, `(*`, `!` and `;` comments, another only `(` — so take the comment characters
of the census from the control's manual and from these settings, not from the template you happen to start from.

Brackets set there become separate symbols only when `=` is allowed, and the kernel never reads a bracketed expression
as a value: `X=(10+5)` is reported as an error. A string after `=` keeps only its digits and points: with quotes set in
the analyzer, `T="b3"` is read as `T=3`. Read such forms in `TransLine`.

Other settings there change what a line is. `UnionLineChars` joins lines that end with a continuation character (`~` in
Heidenhain programs) into one block — use it instead of `nextLine` where the control has such a character.
`EndOfLineChars` splits a line at a separator such as the `;` of robot programs, and `ExcludeEOLChars` decides whether
the separator is passed on to the interpreter. `LineBeginWithNumber` skips a number at the start of a line, such as a
Heidenhain block number.

## Registers

`AddRegister(address, id, name, comment, sign, point, beforePoint, afterPoint, isLeadingZeros, isTrailingZeroes,
valueAvailability, values, isModal, command)` declares one register:

- `address` — the letters of the word (`G`, `X`, `TRAORI`); `id` — for an axis, its address in the machine schema, so
  the kernel can find the machine axis; `name` — a unique name, used to look the register up;
- `sign`, `point`, `beforePoint`, `afterPoint`, leading and trailing zeros — how a value of this address is written;
- `valueAvailability` — whether the word has a value (`X10`, `vatValue`), has none (`STOPRE`, `vatOnlyAddr`), or may
  have either (`vatBoth`);
- `values` and `isModal` — for a group of G or M functions, the allowed values and whether the group is modal;
- `command` — the handler called when the register's element of the queue is executed.

Group G functions as the control's manual does, one register per group: the kernel then knows that `G1` replaces `G0`.
`isModal` does not make the kernel skip a word whose value did not change: every word written in a block enters the
queue again, so the handler of a modal group runs each time the word is written.

**Keep `afterPoint` at the number of digits of the axes.** The kernel derives its axis tolerance from the register with
the most digits after the point, and checks arcs against ten times that tolerance. One register with four digits — a
thread lead, for example — makes the arc check ten times stricter for the whole program, and arcs whose center was
rounded to the thousandth by the postprocessor are replaced by straight lines with a warning. The value of a register is
not rounded by `afterPoint`; it affects only how the register is written.

## Words the kernel cannot read

The kernel reads a register value only in simple forms. Read these in `TransLine` instead, report exactly how many
characters you read (`processedChars`), and add the work to the queue:

- numbered addresses with `=`: `B1=90`, `S2=3000`, `M1=3`. The kernel can read them itself if you declare a register
  with the address `B1` and allow `=` in the analyzer, but then a plain word with the same letters and digits — `B1` for
  the B axis at 1, `M1` for the optional stop — is read as that register, not as `B` or `M` with the value `1`. Read
  such addresses in `TransLine` when the programs also contain those plain words;
- expressions and dimension functions: `X=R80`, `Cs1=DC(0)`, `Z=IC(-2)`;
- calls with brackets and strings: `CYCLE81(…)`, `MSG("…")`, `T="b3"`;
- program flow: labels, jumps, `IF … ELSE … ENDIF`.

A subprogram call is not done by reading text in `TransLine`: take the part of the program from `Kernel.ProgramManager`
— `GetPartByLabels` or `GetPartByIndex`, or `GetPartByLabelsFromCurPos` and `GetPartByRegisters` of
`INCT_ProgramManager2` — and run it with `Kernel.DoSubprogram(part, count)`, as the templates do for a subprogram call.
For a program that consists of several files, set the order of the files with `ProgramManager.AddToOrderList`.

Leave to the kernel what you did not read. Two flags change how the kernel continues after `TransLine`: `breakLine` ends
the block at this point — what was read is executed now, and the rest of the line is read as the next block; `nextLine`
asks for the next line of the program to be read into the same block without executing the current one first — use it
for a statement that continues on the next line, not to skip the rest of a block. The kernel ignores `nextLine` when
`processedChars` is 0. To skip a whole block — the lines of an `IF` branch that is not taken, the lines a jump passes
over — report the whole line as read (`processedChars` equal to its length).

A reader that fails, or recognizes only part of a construction, must report only the characters it really used: a reader
that looks for a subprogram name after `MCALL` and consumes `X10` in `MCALL X10` loses the move. Test every reader with
an axis word and a keyword after it. `TransLine` runs before every word, not only at the start of a line, so a reader of
a form that may only open a block — a skip level `/1`, a block number — must check that it is at the first word of the
block; otherwise it swallows a `/` in the middle of an expression.

## Choosing a register by state

The same address can mean different things: `F` is a feed, but a dwell time in a `G4` block and a thread lead in a `G33`
block. `DefineRegister(address, out index)` is called when the kernel meets an address; return the index of the register
the address means in the current state, or return `false` to let the kernel choose by its own rules. Only the words to
the left are known at that moment: the template decides by the commands already in the queue, so in `F2 G4` the `F` is
still read as a feed. If the control allows such an order, read the block in `TransLine` first. Check every register
name you look up there against `CreateRegisters`: a misspelled name makes the lookup fail and the kernel reads the word
as the default register of that address; only the interaction log, when it is on, shows which register was chosen
("Register is defined: … name …"). A misspelled name of the register a condition depends on does the opposite in the
templates' `DefineRegister`: the condition register stays `null`, the condition is not checked, and the alternative
register is chosen every time.

## The execution queue

A handler adds a command with `Commands.Add`; the queue keeps each command once per block. When an effect must happen
before the motion of the block — a spindle start, a tool length — use `Commands.InsertBefore(CommandType.Move,
CommandType.<effect>)`, and know its limits: it does nothing if the command is already in the queue, and it adds the
command to the end if the move command is not in the queue yet. Call it before the move command has been executed: if
the move is already done or is being executed, the inserted command is placed in front of it and never runs, and the
element being executed runs a second time. Effects of one block that the control applies in a fixed order (spindle
before motion, motion before a modal cycle) must be ordered by the interpreter, not by where the programmer happened to
write the word. Whatever you compute while adding a command is computed at that moment, not when the command is
executed.

Because the queue keeps a command once per block, two targets of the same kind in one block — two spindles in `S1=500
M1=3 S2=3000 M2=4` — need a command each (for example a base command number plus the spindle number); with one shared
command the second replaces the first and a spindle start or stop is lost. The spindle state of the C# helper is one
object for all spindles: load the speed and speed mode of the spindle you output right before each spindle command.

When you change how a command is issued — a spindle, coolant, a tool — find every place that issues it, including the
move events of cycles (a tapping cycle starts and reverses the spindle itself), and route them through the same check.

## Toolpath formers

The kernel builds the moves itself; the interpreter fills in a former and starts it. Before writing the moves of a
cycle, look for its former. The toolpath (CLData) object creates `CreateLinearMotionFormer`,
`CreateCircularMotionFormer`, `CreateDrillingCycleFormer` (simple, with shift, peck), `CreateLatheCycleFormer`
(grooving, thread cutting, stock removal) and, through `INCT_CLData2`, `CreateMillingCycleFormer` (thread milling);
`INCT_CLData_PocketCycleFormer` creates the pocket former. Adjust a former through its events, as the templates do in
their `…CyclesEvents.cs` files, rather than computing the moves yourself. The documentation describes every former and
its parameters.

Things that are easy to get wrong with formers:

- **Plane axes.** A former takes the coordinates of the working plane as (abscissa, ordinate): X/Y in G17, Z/X in G18,
  Y/Z in G19. Check that order and the former's sign convention for the arc direction with a reference G2/G3 program in
  every plane the machine uses: a swapped or mirrored arc looks right in G17 tests and wrong in G18.
- **Feed and feed mode.** Setting a former's feed resets its feed mode (per minute, per revolution): set the mode after
  the feed.
- **Events object.** A C# class passed to a former for its move events is a public class that implements the former's
  events interface, as in the templates' `…CyclesEvents.cs` files; it needs no COM attributes.
- **Tool size.** Check whether the former accounts for the tool width (a grooving tool) before you compute positions
  from the program's values, and test in an operation whose tool has real dimensions.
- **Start point of stock removal.** Whether a stock removal cycle starts from a computed point or from the current tool
  position changes the removed area and the passes: take it from the control's manual.

Before implementing a cycle, look for it in every existing interpreter of the same control, in any language: how they
fill the former is the best start. Check their geometry — a thread diameter, a groove position — against the CAM
operation that produces the cycle and against the former's parameters, not against the sample alone.

## Machine axes

X, Y and Z are the geometry axes of the operation's channel; the templates link them to the axes of the channel at
initialization, and `TurnMill` links them again after a tool change whose `T` word is non-zero and has two or more
digits (tool and offset); `Mill` does not. A machine whose tool change moves the work to another set of axes needs that
link in its own tool change. When you link the axes again, clear the former's axis list first — linking adds to it — and
do it at the start of the next block (`BeforeInterprete`), not while the tool change block is executed: a move written
in the same block as the tool change is otherwise lost. Other axes are found by their address in the machine schema. A
word whose axis the schema does not have produces a warning once and moves nothing; when the programs use another name
for an axis of the schema, map it through the INI file (see "Make variations a setting, not a code change" in "Develop
.NET interpreters") instead of renaming the axis in code.

The SDK can also switch the automatic axis brakes of the machine (`INCT_CLData_AutoAxesBrakes`, taken from the CLData
object as shown in "Interfaces" above). Decide with the user whether brake M codes must change the simulation or can be
read without effect. To show a brake code explicitly, switch the automatic brakes off and write the brake commands
through `INCT_CLData_BreakCommand` of the CLData object: `Open`, `SetBreak(axisIndex, on)` for each axis, `Close`.

## Coordinates and the first move

- **What an axis value means.** The axis values the interpreter reads back from the kernel (`GetAxisValue`) are tool-tip
  coordinates in the active coordinate system — after the work offset, frames, a machine-coordinate block and a plane
  rotation. Compute dimension functions and incremental values in that system.
- **Before the first move** the value is the start state of the operation: its starting point, otherwise the tool change
  point, otherwise the default of the axis in the machine schema. It is never where the previous operation ended: the
  interpreter cannot know that, and neither can the simulation know where the machine stood before the program. Say so
  in the README.
- **The first move.** In an operation simulated from NC text the kernel holds back the first moves until X, Y and Z are
  all known and starts the operation at the first complete point. A program that never sets one of them — Y in most
  lathe programs — can lose its first retract or show no motion at all. Do not output moves from `Initialize`: a move
  made before the program starts changes where the operation begins. Test the first blocks of every kind of program, and
  warn when a program ends without any motion or with a start point the interpreter had to assume: an empty or invented
  toolpath without a message is worse than an error.
- **Machine coordinates.** Moves in machine coordinates (`SUPA`, `G153`) mixed with tool-tip moves in a rotated or
  shifted coordinate system can shift an axis the program never set. Test such programs on a project with a rotated
  frame. A frame or plane rotation is output through the origin interface, as a shift and rotation on top of the active
  work offset.
- **Initial modal state.** Decide the plane, the units and the diameter mode the control starts in from its manual and
  the machine type — a lathe control usually starts in G18 — and test a program that never programs them.

## Spindles and tools

The kernel turns the spindle that carries the operation's tool. A spindle number in a program command does not choose
another spindle, and a tool change in the program does not change the operation's tool. On a lathe, selecting a spindle
through the toolpath object selects the workpiece holder: never use it to turn a tool spindle. A spindle command the
kernel cannot route is skipped with one warning per program, written for the machine user (see "Interpreter development"
(`interpreter-development`)).

## Channels

Each channel of a multi-channel machine is simulated as its own operation with its own program. The SDK packages of
newer product versions have a wait point, `INCT_CLData_Wait.AddWait(id)`, which the CAM system uses to synchronize
channels: a channel that reaches a wait point waits for the other channels with the same point. Check that the released
package you build against declares `INCT_CLData_Wait` before you use it. Take it from the CLData object (`if (CLD is
INCT_CLData_Wait wait) wait.AddWait(id);`). To make a control's wait word (`WAITM`, `M200`, a wait mark) synchronize
channels, translate it into `AddWait` with an identifier both programs share, and check in the simulation that the
channels wait as they do on the machine. For a product version whose released package has no `INCT_CLData_Wait` there is
no wait point: there the wait word can only be read without effect. An interpreter that only reads the wait word, so
that the programs are not rejected, must say in its README that the channels are not synchronized.

The equipment object also tells the interpreter which channel its program belongs to: take `INCT_Equipment_Channels`
from it (`if (EQ is INCT_Equipment_Channels channels)`) and read `CurrentIndex`, `Count` and `Channel[i].Name`.

Move the axes the equipment object gives for the channel: `GetXYZindex` returns the axes of the current channel (`X2`,
`Y2`, `Z2` for the second one). When the second channel moves the axes of the first, or its toolpath shrinks to a point,
compare those axes with the axes the interpreter passes to its motion commands: a mismatch is a defect of the
interpreter or of its `.snci`, not of the product.

Depending on its version and license, Tuner may simulate the channels one after another instead of together. Then the
wait points hold nothing back, and a synchronization check in Tuner proves nothing: check synchronization in the CAM
system and say where it was checked.

## Known traps

- A thousandth-rounded arc becomes a line: see `afterPoint` above.
- Besides the `.snci` with a library, the interpreter file field accepts `.sncix` (an interpreter set up in the
  interpreter configurator: it names an existing interpreter and stores values of its configurable parameters, without
  a library of its own) and a `.stfc` container that holds the interpreter files. This guidance covers the
  `.snci` with a library; do not convert one format into another unless the user asks for it.
- A misspelled register name in `DefineRegister` reads the word as another register without an error: see above.
- The kernel creates a new interpreter instance for every calculation of an operation, but the following parts of the
  same program are read by that same instance, and `NextOperation` is called before each part. Reset there every modal
  field and the state of the helper objects (spindle limits, constant cutting speed), and output the modal state again
  at the start of the part.
- A semicircle given by its radius whose chord, after the postprocessor's rounding, is slightly longer than twice the
  radius has no center and becomes a line: accept a small tolerance and limit the chord.
- Keep the state in instance fields and reset it in `NextOperation` where the next part must not inherit it. In a native
  DLL, global data is shared by every instance of the interpreter in the process. A .NET interpreter is loaded into a
  load context of its own for every instance, so its static fields are not shared — and do not carry anything to the
  parent or to the contour instance either. The CAM system creates a new instance for every calculation of an operation;
  Tuner keeps one instance for each channel, from the first operation of the channel to the last, and calls
  `NextOperation` between them: a modal word such as `G0` from the end of one operation is still in force at the start
  of the next.
- A coordinate that is absent and a coordinate that is zero are different things; keep them apart in the state (see the
  empty value above).
- A registered word without a handler, or a handler that is never called for one of its values, fails silently; keep a
  test program for each group.
- A fractional G function (`G33.1`, `G12.1`) is not an integer: list the value with its fraction in the register's
  values (`[12, 12.1, 13, 13.1]`) and compare the register's decimal value (`register.Flt is 12.1`), as the template
  does, never an integer value.
- Registers written in the `.snci` file are loaded first, and a register of `CreateRegisters` is added only if no
  register of the same name exists yet: a register someone added to the `.snci` under the same name silently replaces
  its address, format and values, while the handler of the code is still attached to it by name. Look there first when a
  word behaves differently from what the code says.
- An exception in `CreateRegisters` or the constructor is reported by the CAM system only as an unsupported library; see
  "Debug" in "Develop .NET interpreters" for how to see the real error.
- An exception that leaves the interpreter while a program is interpreted — in `Interprete`, for example — ends the
  calculation of the whole operation, and only its message is left. Catch what you can handle, and report a word you
  cannot simulate as a warning instead of throwing.
- In a C# interpreter, an `Initialize` override must call `base.Initialize()`: it links the registers to their handlers
  by name, and without it no `Cmd…` handler runs. `Commands` is still `null` inside `CreateRegisters`, and a second
  register with a name already used is ignored without an error.

## Done means

You can say for each word of the change in which call it is read, where its value is stored, which command it adds to
the queue, and where that command produces its effect — and the order of effects within the block is the control's, not
an accident of the word order.
