# STOP - Stop

## Command caption

How the command appears in the CLData command list:

```text
STOP
```

Use the **STOP** command to form frames of breaking the execution of NC-program. Commonly it's the M00 code of NC-program. When the stop frame is reached execution of the NC-program is interrupted.

## Access from sppx

Handler: `program Stop`

Example (from the Fanuc (30i)_Mill postprocessor):

```pascal
program Stop
  if M <> M@ then OutBlock           ! output to NC block
  M = 0                                ! M0
  M@ = 1
end
```

## Access from .NET

Handler:

```csharp
public override void OnStop(ICLDStopCommand cmd, CLDArray cld)
```

Inheritance: `ICLDStopCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd["..."]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

Example - `OnStop` (from the Fanuc (30i)_Mill_DN postprocessor):

```csharp
public override void OnStop(ICLDStopCommand cmd, CLDArray cld)
{
    nc.Block.Out();
    nc.M.Show(0);
    nc.Block.Out();
}
```

## See also
- [CLData access model](../cldata.md)
