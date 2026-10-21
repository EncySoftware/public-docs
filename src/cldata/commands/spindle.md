# SPINDL - Spindle

## Command caption

How the command appears in the CLData command list:

```text
SPINDL ON(71)|OFF(72)|ORIENT(246), NO n, K k, MODE RPM(0)|RANGE(1)|CSS(2) {, SPEED c}
```

**SPINDL** command passes spindle control parameters. **SPINDL** command is used to define spindle rotation frequency or range of frequencies, surface speed, etc.

## Access from sppx

Handler: `program Spindl`

The `cld` array is read by index or by name - in sppx by the typed short name (e.g. `cld.X`), in .NET by the same name as a string key (e.g. `cld["X"]`).

| Parameter | CLD array | CLD name | Description |
|---|---|---|---|
| ON(71)<br>OFF(72)<br>ORIENT(246) | CLD[1] | CLD.OnOff | Command type: ON(71) – spindle rotation on, OFF(72) – spindle rotation off, ORIENT(246) – oriented spindle stop. |
| n | CLD[2] | CLD.NO | Rotation frequency, spindle rotation angle or maximum spindle rotation frequency in CSS mode. |
| k | CLD[3] | CLD.K | Range of rotation frequencies. |
| RPM(0)<br>RANGE(1)<br>CSS(2) | CLD[4] | CLD.Mode | Mode of the rotation frequency definition: RPM(0) – revolutions per minute, RANGE(1) – range of spindle rotation frequencies, CSS(2) – constant surface speed mode. |
| c | CLD[5] | CLD.CSS | Constant surface speed value for the CSS mode. |

To create ISO postprocessor using masks use ISO.M values which correspond to **SPINDL** parameters.

| CLD parameter | ISO value |
|---|---|
| CLD[1] = 71 | ISO.M = 3 |
| CLD[1] = 72 | ISO.M = 5 |

Example (from the Fanuc (30i)_Mill postprocessor):

```pascal
program Spindl
  OutBlock
  case cld[1] of
    71: begin ! On
      if cld[4]=2 then begin ! CSS
        GSpindl = 96
        S = abs(cld[5])
        OutBlock
        if cld[5] > 0 then SpDir = 3
                      else SpDir = 4    ! M3/M4  CW/CCW
        SpRPM = abs(cld[2])
      end else begin ! RPM
        if cld[2] > 0 then Msp = 3
                      else Msp = 4    ! M3/M4  CW/CCW
        if ((SpDir=3) or (SpDir=4)) and (SpDir<>Msp) then ! Spindle reverse
          Output "M5"
        GSpindl = 97
        S = abs(cld[2]); S@=SpRPM
        Msp@ = SpDir
        SpDir = Msp
        SpRPM = abs(cld[2])
        OutBlock
      end
    end
    72: begin ! Off
      Msp = 5
      S=0; S@=S
      SpRPM = 0
      SpDir = 5    ! M3/M4/M5
      OutBlock  ! Msp = 5;; OutBlock; Msp=1; OutBlock
    end
    246: begin  ! M19 ORIENT
      OutBlock
      M = 19; M@ = MaxReal
      OutBlock
    end
  end
end
```

### Access by parameter name (helpers)

Parameters available through the `cmd` operator (the same in sppx and .NET):

| Name | Helper | Description |
|---|---|---|
| `Action` | `cmd.Int["Action"]` | Command kind (0 - on, 1 - off, 2 - orient). |
| `RotationDirection` | `cmd.Int["RotationDirection"]` | Rotation direction. |
| `SpeedMode` | `cmd.Int["SpeedMode"]` | 0 - RPM, 1 - RANGE, 2 - CSS. |
| `Value` | `cmd.Flt["Value"]` | Rotation frequency / orientation angle / max rpm. |
| `CSSValue` | `cmd.Flt["CSSValue"]` | Constant surface speed value. |
| `RangeValue` | `cmd.Int["RangeValue"]` | Gearbox range. |
| `SpindleID` | `cmd.Str["SpindleID"]` | Spindle identifier. |

## Access from .NET

Handler:

```csharp
public override void OnSpindle(ICLDSpindleCommand cmd, CLDArray cld)
```

Inheritance: `ICLDSpindleCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd[...]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

| Property | Type | Description |
|---|---|---|
| `cmd.SpindleID` | string | Textual identifier of the spindle for which this command sets parameters. |
| `cmd.Action` | `CLDSpindleAction` | The action for the spindle (`On`, `Off` or `Orient`). |
| `cmd.IsOn`<br>`cmd.IsOff`<br>`cmd.IsOrient` | bool | True if it is a switch-ON / switch-OFF / angular-orientation command. |
| `cmd.SpeedMode` | `CLDSpindleSpeedMode` | The spindle rotation mode (`RPM` or `CSS`). |
| `cmd.IsRPM`<br>`cmd.IsCSS` | bool | True if the mode is RPM (rev/min, G97) / CSS (constant surface speed, G96). |
| `cmd.RotationDir` | `CLDRotationDir` | Rotation direction for the spindle (CW or CCW). |
| `cmd.IsClockwiseDir` | bool | True if the rotation direction is CW (clockwise). |
| `cmd.RPMValue` | double | Revolutions per minute (maximal if the CSS mode is active). |
| `cmd.CSSValue` | double | The value of a linear (surface) speed for the spindle. |
| `cmd.GearRange` | int | Spindle's gearbox range. |

Example (from the Sinumerik 840D mill postprocessor):

```csharp
public override void OnSpindle(ICLDSpindleCommand cmd, CLDArray cld)
{
    if (cmd.IsOn)
    {
        switch (cmd.SpeedMode)
        {
            case CLDSpindleSpeedMode.RPM:
                nc.S.Show(cld[2]);
                nc.Msp.Show(cmd.IsClockwiseDir ? 3 : 4);
                break;
            case CLDSpindleSpeedMode.CSS:
                throw new Exception("CSS mode not realized");
        }
    }
    else if (cmd.IsOff)
        nc.Msp.Show(5);
}
```

## See also
- [CLData access model](../cldata.md)
