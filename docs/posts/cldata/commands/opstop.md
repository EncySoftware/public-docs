# OPSTOP - Auxiliary stop

## Command caption

How the command appears in the CLData command list:

```text
OPSTOP
```

**OPSTOP** command is used to form NC-commands of optional breaking of NC-program execution (commonly it's the M01 code). The CNC-system breaks execution on this command only if corresponding execution mode is set, otherwise the NC-program is not halted on this command.

## Access from sppx

Handler: `program OpStop`

Example (from the Fanuc (30i)_Mill postprocessor):

```pascal
program OpStop
  if M <> M@ then
    OutBlock
  M = 1      ! M01
  M@ = 0
end
```

## Access from .NET

Handler:

```csharp
public override void OnOpStop(ICLDOpStopCommand cmd, CLDArray cld)
```

Inheritance: `ICLDOpStopCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd["..."]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

Example - `OnOpStop` (from the Fanuc (30i)_Mill_DN postprocessor):

```csharp
public override void OnOpStop(ICLDOpStopCommand cmd, CLDArray cld)
{
    nc.Block.Out();
    nc.M.Show(1);
    nc.Block.Out();
}
```

## See also
- [CLData access model](../cldata.md)
