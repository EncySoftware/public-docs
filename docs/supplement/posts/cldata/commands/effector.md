# EFFECTOR - End effector activation

## Command caption

How the command appears in the CLData command list:

```text
EFFECTOR N n, Value ON(71) | OFF(72)
```

EFFECTOR CLData command should activate or deactivate the end effector of a machine or robot (laser, jet nozzle, arc welder etc.).

## Access from sppx

Handler: `program Effector`

| Parameter | CLD array | CLD name | Description |
|---|---|---|---|
| N | CLD[1] | CLD.N | Unique identifier of the end effector to be enabled or disabled |
| Value | CLD[2] | CLD.Value | Type of the command: 71 - switch ON, 72 - switch OFF. |

Example:

```pascal
program Effector
  ! cld[1] - effector id, cld[2] - 71 (ON) | 72 (OFF)
  if cld[2] = 71 then
    Output "DOUT M#(" + cld[1] + ")=ON"
  else
    Output "DOUT M#(" + cld[1] + ")=OFF"
end
```

## Access from .NET

Handler:

```csharp
public override void OnEffector(ICLDEffectorCommand cmd, CLDArray cld)
```

Inheritance: `ICLDEffectorCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd["..."]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

| Member | Type | Description |
|---|---|---|
| `cmd.IsOn` | `bool` | Returns "true" if this command is EFFECTOR switch ON command, otherwise "false". |
| `cmd.IsOff` | `bool` | Returns "true" if this command is EFFECTOR switch OFF command, otherwise "false". |
| `cmd.EffectorID` | `int` | Numerical identifier of the effector to activate-deactivate. |

Example - `OnEffector` (from the CRP_robot_DN postprocessor):

```csharp
public override void OnEffector(ICLDEffectorCommand cmd, CLDArray cld)
{
//    if (cmd.IsOn && !effectorIsOn) {
//        prg.WriteLine("DOUT M#(111)=ON");
//    } else if (cmd.IsOff  && effectorIsOn) {
//        prg.WriteLine("DOUT M#(111)=OFF");
//    }
    effectorIsOn = cmd.IsOn;
}
```

## See also
- [CLData access model](../cldata.md)
