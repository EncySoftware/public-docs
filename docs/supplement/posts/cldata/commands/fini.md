# FINI - Ending record

## Command caption

How the command appears in the CLData command list:

```text
FINI
```

**FINI** command is the last command in the list of technology commands of the project. Use **FINI** to form NC-program conclusion blocks.

## Access from sppx

Handler: `program Fini`

Example (from the Fanuc (30i)_Mill postprocessor):

```pascal
program Fini
  OutBlock                        ! output
  OutPut "M30"
  OutPut "%"
  OutPut ""
  NCSub.Output
  
  s$ = "G53Z0."
  CrLf$ = Chr(13) + Chr(10)
  if (HasAxisA<>0) or (HasAxisB<>0) or (HasAxisC<>0) then begin
    s$ = s$ + CrLf$ + "G53"
    if (HasAxisA<>0) then
      s$ = s$ + "A0."
    if (HasAxisB<>0) then
      s$ = s$ + "B0."
    if (HasAxisC<>0) then
      s$ = s$ + "C0."
  end
  ReplNCStr("<StartGoHome>", s$)
end
```

## Access from .NET

Handlers:

```csharp
public override void OnFini(ICLDFiniCommand cmd, CLDArray cld)
public override void OnFinishProject(ICLDProject prj)   // project-level, raised on FINI
```

Inheritance: `ICLDFiniCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd["..."]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

Example - `OnFinishProject` (from the Fanuc (30i)_Mill_DN postprocessor):

```csharp
public override void OnFinishProject(ICLDProject prj)
{
    nc.Block.Out();
    nc.Output("M30");
}
```

## See also
- [CLData access model](../cldata.md)
