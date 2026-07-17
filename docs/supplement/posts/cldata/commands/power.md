# POWER - Power adjustment

## Command caption

How the command appears in the CLData command list:

```text
POWER N n, Value
```

POWER CLData command specifies the percent of a nominal power (defined in the operation parameters of CAM) for the exact active effector (laser, jet nozzle, arc welder etc.) that should be used for the following movements. For example, the CAM system may calculate the value passed by this command as a percentage of the nominal workpiece thickness or a percentage of the thickness of the layer being machined (the closest point in the previous pass).

## Access from sppx

Handler: `program Power`

| Parameter | CLD array | CLD name | Description |
|---|---|---|---|
| N | CLD[1] | CLD.N | Unique identifier of the device in the CAM whose power we should change |
| Value | CLD[2] | CLD.Value | The value of a power in percents of some constant value specified either in the parameters of the operation, or implicitly assumed. |

Example:

```pascal
program Power
  ! cld[1] - device id, cld[2] - power as a percentage of the nominal value
  NominalCurrent = 120                                  ! nominal current (A) of the effector, usually taken from operation params
  Output "A" + Str(NominalCurrent * cld[2] / 100)       ! actual current for the following movements
end
```

## Access from .NET

Handler:

```csharp
public override void OnPower(ICLDPowerCommand cmd, CLDArray cld)
```

Inheritance: `ICLDPowerCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd["..."]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

| Member | Type | Description |
|---|---|---|
| `cmd.ID` | `int` | Numeric identifier of the device for which the power is set. |
| `cmd.Value` | `double` | The value of a power in percents of some constant value specified either in the parameters of the operation, or implicitly assumed. |

Example:

```csharp
public override void OnPower(ICLDPowerCommand cmd, CLDArray cld)
{
    // cmd.Value is a percentage of the nominal power of the active effector
    double nominalCurrent = 120;                          // nominal current (A), usually taken from the operation parameters
    nc.Amperage.Show(nominalCurrent * cmd.Value / 100);   // actual current for the following movements
    nc.Block.Out();
}
```

## See also
- [CLData access model](../cldata.md)
