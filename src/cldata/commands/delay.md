# DELAY - Delay

## Command caption

How the command appears in the CLData command list:

```text
DELAY A a
```

**DELAY** command is used to pause program execution for the specified time. **DELAY** commonly translates to G04.

## Access from sppx

Handler: `program Delay`

| Parameter | CLD array | CLD name | Description |
|---|---|---|---|
| a | CLD[1] | CLD.A | Delay time in seconds |

Example (from the Fanuc (30i)_Mill postprocessor):

```pascal
program Delay
  OutBlock
  GFunc = 4; GFunc@ = MaxReal
  Pause = CLD[1]; Pause@ = MaxReal
  OutBlock
end
```

## Access from .NET

Handler:

```csharp
public override void OnDelay(ICLDDelayCommand cmd, CLDArray cld)
```

Inheritance: `ICLDDelayCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd["..."]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

| Member | Type | Description |
|---|---|---|
| `cmd.TimeSpan` | `double` | Delay time in seconds. |

Example - `OnDelay` (from the Fanuc (30i)_Mill_DN postprocessor):

```csharp
public override void OnDelay(ICLDDelayCommand cmd, CLDArray cld)
{
    nc.GDelay.Show(4);
    nc.XDelay.Show(cmd.TimeSpan);
    nc.Block.Out();
}
```

## See also
- [CLData access model](../cldata.md)
