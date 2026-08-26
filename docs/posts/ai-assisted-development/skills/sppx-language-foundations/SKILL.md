---
name: sppx-language-foundations
description: Practical SPPX language foundations for reading and planning postprocessor code: execution model, state, runtime data, registers, output and compact verified syntax patterns. Use with develop-sppx-postprocessor; it is not a substitute for actual CLData or versioned documentation.
---

# SPPX language foundations

## Purpose and boundary

Use this skill when reading or planning SPPX code. It supplies stable language concepts and small syntax patterns; it does **not** replace the development workflow, CLData inspection, InP MCP tools, NC verification, or the documentation MCP.

- `postprocessor-development` frames the task and source trust order.
- `inspect-cldata` reads actual command values and parameter paths.
- `develop-sppx-postprocessor` controls InP work, editing, translating, running and comparison.
- `verify-nc-program` assigns the verification state.
- This skill explains common SPPX forms so that general C# / Pascal / Delphi knowledge is not substituted for the postprocessor language.

For an unfamiliar or version-sensitive SPPX/InP semantic, read the authoritative documentation page before relying on it. Current post code, actual CLData and a baseline run remain stronger evidence for the current project than a generic pattern here.

## Execution model

An SPPX postprocessor transforms a stream of CLData commands into NC blocks:

```text
CLData command -> enabled handler -> state and registers -> OUTBLOCK / FORMBLOCK / MASK -> NC block
```

- A CLData token and a handler name are not necessarily identical. For example, the token may be `GOTO.abs` while the current post's handler is `AbsMov`. Obtain handler names from `pp_get_structure`; never construct one from an NC word or a CLData token.
- A handler can set state without printing a block. Output may occur in a called subroutine, a mask, `Filter`, or a later modal transition.
- Register assignment alone does not prove that an NC word is emitted. The output operation and modal state determine the resulting block.
- `COMMON` executes before normal command processing. `PARTNO` is commonly used for program-start initialization, but its actual role must be read in the current post.

## State: choose lifetime before code

Use the lifetime required by the behavior, not the most convenient syntax.

| Need | Common location | Verify before use |
|---|---|---|
| Temporary value used only during one handler invocation | Local variable in that handler or subroutine | The value is not needed by another handler or later command |
| State shared by handlers or preserved across commands | `Common` | Initialization and reset boundaries in the current post |
| Structured state with related data and behavior | Custom object instance | Object syntax and instance lifetime; documentation if unfamiliar |
| An NC address to be formatted/output | Register list | Existing binding, list position, format and modal behavior |

Do not put an NC register in `Common` merely because its value must persist. Do not create a register merely because a local calculation needs storage. Variables ending in `@` conventionally represent previous register state; treat their semantics as runtime behavior and do not redeclare them without documentation/current-code evidence.

### Common lifecycle questions

Before adding or resetting state, identify which transition owns it: program start, operation boundary, tool change, first motion, subprogram boundary, command repeat, or program end. Common patterns such as `PARTNO`, `PPFUN`, `LoadTl`, `Fedrat`, `AbsMov` and `Filter` are only routing clues. The real CLData and current post decide where a reset belongs.

## Small verified syntax patterns

These patterns demonstrate language form only. They do not prove that the shown storage, reset point, handler or output behavior is suitable for a particular post.

### Variables, conditions and blocks

```sppx
Count: Integer;
FeedValue: Real;

if Count > 0 then begin
  FeedValue = FeedValue + 1
end
```

- **Purpose:** declaration and a multi-statement conditional block.
- **Guaranteed:** SPPX uses typed declarations and `begin ... end` for grouped statements.
- **Not guaranteed:** the correct type, variable scope, condition or lifecycle for the current post.

### Arrays and records

```sppx
Values: array 3 of Real;
State: record
  Ready: Integer;
  LastValue: Real
end;

Values[1] = 10;
State.Ready = 1
```

- **Purpose:** basic collection and structured data form.
- **Guaranteed:** array and CLD-style indexing are 1-based in SPPX.
- **Not guaranteed:** an index exists in actual CLData, an array size is sufficient, or a record is better than `Common`/an object.

### Custom object form

```sppx
object FeedState
  LastFeed: Real;
  Initialized: Integer;

  procedure Reset
  begin
    self.LastFeed = 0;
    self.Initialized = 0
  end
end.
```

```sppx
State: FeedState;
State.Reset
```

- **Purpose:** fields, a method, `self`, object closing syntax and an instance declaration.
- **Guaranteed:** custom object form shown here is a language pattern.
- **Not guaranteed:** whether an object should be used, where its instance belongs, when `Reset` is called, or how feed/modal output works. Read documentation before first use of an unfamiliar object form or method semantic.

### Subroutine form

```sppx
sub PrepareOutput(Value: Real)
  if Value <> 0 then begin
    PRINT STR(Value)
  end
subend

call PrepareOutput(10)
```

- **Purpose:** subroutine definition and call form.
- **Guaranteed:** a `sub ... subend` body can encapsulate repeated SPPX logic.
- **Not guaranteed:** that `PRINT`, output, parameters or the chosen ownership are appropriate for a production handler.

## Runtime input data

| Runtime item | Use | Rule |
|---|---|---|
| `CLD` | Numeric parameters of the current command | Values and indices come from `inspect-cldata` and current handler/docs evidence |
| `RecNum` | Count of current numeric CLD parameters | Check before reading optional positions |
| `CLData$` | Text data for textual commands | Do not treat it as a numeric CLD value |
| `Cmd` | Named, textual, typed and complex command parameters | Prefer named access when actual command data provides it |
| `Project` | Project-level parameters | Read actual project settings; do not infer them from NC |
| `GMA` | Machine-axis data for relevant multi-axis commands | Use actual machine/schema evidence; do not invent axis names |
| `RGS` | Register access by index | Read the current register model before relying on indexed access |

Typical access forms:

```sppx
X = CLD[1];
Name$ = Cmd.Str["Comment"];
Changed = Cmd.Int["ToolChanged"];
Value = Cmd.Flt["SomeValue"];
```

`CLD[1]` in this example is only syntax. It never proves that position 1 means X, feed, a mode, or any other value for the current command. `inspect-cldata` returns SPPX-ready 1-based paths; do not convert them manually from .NET paths.

## Registers and NC output

A register combines an NC identifier, an internal name, a current value, previous state and output format. `OUTBLOCK` normally scans the register list in list order and emits changed values in that order.

```text
register list order + changed current/previous state -> NC word order in OUTBLOCK
```

Consequences:

- The order of assignments in a handler does not define NC word order.
- Different registers may share an NC identifier when the post needs separate output positions; choose by the current register list and intended sequence, not the first matching identifier.
- Before adding a register, read `pp_get_registers`, locate current bindings and verify that no existing register covers the required address and position.
- Do not reorder existing registers to solve one local block. A new register, if truly needed, must have a validated position and format.
- Formatting, scale, signs, leading/trailing zero policy and duplicated-register semantics are post/control specific. Read the current definition and documentation before changing them.
- `X@`, `F@` and similar previous-state variables are not ordinary independent registers. Do not reset or declare them based only on generic programming intuition.

### Output operations

| Operation | Practical meaning | Must verify |
|---|---|---|
| `OUTBLOCK` | Forms and emits a normal NC block from current register/output state | Which registers are eligible, list order and modal state |
| `FORMBLOCK` | Forms an output block without normal NC emission | Destination and later use of the formed string |
| `MASK(...)` | Produces output according to mask-specific syntax and rules | Mask semantics, modifiers and state effects from docs/current code |
| `OUTPUT` | Writes a direct text block | File/destination and control-specific formatting |
| `Filter` | May transform a block after formation and before final NC insertion | Current signature and existing post behavior |

Do not put mask-only modifiers into ordinary handler expressions. A mask, its register resolution and modal effects are not inferred from a similar fragment; read its documentation/current definition first.

## CLData and handler routing clues

These are navigation clues, not universal implementation recipes.

| Intent area | Often related handlers/data | Do not assume |
|---|---|---|
| Linear motion | `AbsMov`, `MultiGoto`, `PhysicGoto`, `From`, `GoHome` | Which coordinates/axes apply or where output occurs |
| Feed | `Fedrat`, then a later motion handler | Whether feed emits immediately or is modal |
| Spindle | `Spindl` | Control codes, orientation support and output placement |
| Tool change | `LoadTl`, command data such as `ToolChanged` | Reset boundaries or T/M code sequence |
| Program/operation/subprogram lifecycle | `PartNo`, `PPFUN`, `Structure`, `FINI` | Exact CLD subcodes and local conventions |
| Cycles | `Cycle`, `ExtCycle` | Field mapping and first/repeated-cycle output |
| Coordinates/interpolation | `Origin`, `Interpolation`, `Circle` | Plane, machine transform and kinematic assumptions |

For exact CLD mappings, use `inspect-cldata` first. Read detailed documentation for unfamiliar command variants, cycles and optional fields.

## Built-ins and documentation trigger

The following categories are common, but their methods and version behavior are not memorized by this skill:

- string/date helpers;
- `Point3D`, `Matrix`, `EulerConverter`, `Quaternion4d` and transformation helpers;
- `NCChannel` and multichannel state;
- `Cmd.Ptr` complex values and machine-axis structures;
- masks, formats, register modifiers and output filters.

Before first use of a built-in object, method, unfamiliar runtime object, mask form or version-sensitive feature:

```text
cam_search_docs_semantic or cam_search_docs
-> cam_read_doc
-> use the specific documented fact
```

A search snippet, a skill example or similar code from another postprocessor is not the language specification. If the page cannot be read and the semantic is necessary, leave it `blocked` rather than inventing syntax.

## Common mistakes

- Writing C# / .NET property syntax into SPPX.
- Constructing a handler name from a CLData token or NC word.
- Guessing `CLD[...]` indices, optional fields or `Cmd` parameter names.
- Treating an assignment as proof of output without tracing `OUTBLOCK`, masks and modal state.
- Reusing a donor's global state, register name, format, reset point or output fragment without checking the current post.
- Treating a successful translation as proof of correct NC behavior.
- Using a language mini-pattern as a production handler template.

## Use with the workflow

Load this skill to recognize ordinary SPPX forms while reading code. Then follow `develop-sppx-postprocessor` for the actual change. If this skill, the current post and actual CLData do not prove the semantic needed by the change, the workflow's change-critical-unknowns gate requires documentation lookup before planning or editing.
