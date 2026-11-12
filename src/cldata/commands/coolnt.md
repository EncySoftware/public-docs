# COOLNT - Cooling

## Command caption

How the command appears in the CLData command list:

```text
COOLNT ON(71)|OFF(72), N n
```

**COOLNT** command turns on or off the machine cooling systems. The first parameter specifies command type: activation or deactivation. The second parameter is the tube number which is affected by the **COOLNT** command.

## Access from sppx

Handler: `program Coolnt`

| Parameter | CLD array | CLD name | Description |
|---|---|---|---|
| ON(71)<br>OFF(72) | CLD[1] | CLD.OnOff | Command type: ON(71) – activate coolant, OFF(72) – deactivate coolant. |
| n | CLD[2] | CLD.N | Coolant tube number: 1 – flood, 2 – mist, 3 – tool. |

To create ISO postprocessor using masks use ISO.M values which correspond to parameters:

| CLD parameter | ISO value |
|---|---|
| CLD[1] = 71 | ISO.M = 8 |
| CLD[1] = 72 | ISO.M = 9 |

Example (from the Fanuc (30i)_Mill postprocessor):

```pascal
program CoolNt
  if cld[1] = 71 then begin
    if cld[2] = 1 then begin
      Mc = 8
    end else if cld[2] = 2 then begin
      Mc = 8
    end else if cld[2] = 3 then begin
      Mc = 8
    end else begin
      Mc = 8
    end
  end else begin
    Mc = 9     ! On/Off coolant
    OutBlock
  end
end
```

## Access from .NET

Handler:

```csharp
public override void OnCoolant(ICLDCoolantCommand cmd, CLDArray cld)
```

Inheritance: `ICLDCoolantCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd["..."]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

| Member | Type | Description |
|---|---|---|
| `cmd.IsOn` | `bool` | Returns "True" if it's a switch on command and you need to switch ON all tubes marked in the TubeIsOn[] list. |
| `cmd.IsOff` | `bool` | Returns "True" if it's a switch off command and you need to switch OFF all tubes marked in the TubeIsOn[] list. |
| `cmd.TubeCount` | `int` | Returns the count of tubes presented in the TubeIsOn[] list. |
| `cmd.TubeIsOn` | `ICLDCoolantTubeIndexer` | Allows you to determine whether or not to switch the state for the tube with a given index. The index must be between 0..31 (TubeCount-1). |
| `cmd.FirstEnabledTube` | `int` | Returns the index of the first tube to be switched, i.e. TubeIsOn[FirstEnabledTube]=true. |

Example - `OnCoolant` (from the Fanuc (30i)_Mill_DN postprocessor):

```csharp
public override void OnCoolant(ICLDCoolantCommand cmd, CLDArray cld)
{
    if (cmd.IsOn) {
        nc.MCoolant.v = 8;
    } else {
        nc.MCoolant.v = 9;
        nc.Block.Out();
    }
}
```

## See also
- [CLData access model](../cldata.md)
