# AXESBRAKE - Machine axes brakes control

## Command caption

How the command appears in the CLData command list:

```text
AXESBRAKE COUNT N, Axis1Pos(n1) State1, Axis2Pos(n2) State2, ...,
AxisNPos(nN) StateN
```

Use **AXESBRAKE** command to turn on and off axes brakes if there are axes brakes on the machine. Most commonly this command is used to turn on/off spindle brake (Axis C) on the lathe-milling machines when switching from lathe to milling and vice versa. When performing lathe machining the spindle rotates at high speed, and when milling the spindle is fixed by the brake at specific angle. Using brakes helps to increase the spindle load and reduces the spindle precision positioning mechanisms wear. Also brakes are used on milling machines rotating axes to perform indexed machining.

## Access from sppx

Handler: `program AxesBrake`

| Parameter | CLD array | Description |
|---|---|---|
| N | CLD[1] | Number of axes affected by this command. |
| n1 | CLD[2] | Index of axis named Axis1Pos in the coordinates list. |
| State1 | CLD[3] | New state of Axis1Pos axis: ON(71) - brake is on, OFF(72) - brake is off. |
| n2 | CLD[4] | Index of Axis2Pos axis in the coordinates list. |
| State2 | CLD[5] | New state of Axis2Pos axis: ON(71) - brake is on, OFF(72) - brake is off. |
| … | … | … |
| nN | CLD[2*N] | Index of AxisNPos axis in the coordinates list. |
| StateN | CLD[2*N+1] | New state of AxisNPos axis: ON(71) - brake is on, OFF(72) - brake is off. |

Parameters available through the cmd operator

| TCLDAxesBrake: ComplexType | The command to switch the states of axes brake. |
|---|---|
| Axes: Array, Key="AxisID" | cmd.Ptr["Axes"] - An array of structures such as AxisBrake. Thus, one command can change the brake state for several axes. |
| AxisBrake: ComplexType | cmd.Ptr["Axes"].Item[Index] or cmd.Ptr["Axes(**AxisName**)"] - Separate element of the Axes array. Contains the state of one machine axis brake. Access to the array elements can either by index or by key field. Here **AxisName** - the key field value, which must match the AxisID field value. |
| AxisID: String | cmd.Str["Axes(**AxisName**).AxisID"] - The machine axis identifier, for which is given a new brake state. Determined by the machine schema. |
| BrakeState: Integer | cmd.Int["Axes(**AxisName**).BrakeState"] - the new state of the machine axis brake: 0 - Off, 1 - On. |

Command syntax allows changing states of multiple axes brakes at once. List of coordinates, which names appear in this command are defined by the CAM system machine scheme.

Here are two simple examples of programs handlers for this command.

```pascal
program AxesBrake
  Index: Integer ! Loop counter
  AxisNumber: Integer ! Index of an axis in the list of machine axes
  BrakeState: Integer ! New state of the axis brake
  Index = 1
  while Index<=CLD[1] do begin
    AxisNumber = CLD[2*Index]
    BrakeState = CLD[2*Index+1]
    case AxisNumber of
      4: begin ! AxisAPos(A) index in the list of machine axes
        if BrakeState=71 then Output "M680" ! Turn axis A brake on
        else Output "M690" ! Turn axis A brake off
      end
      6: begin ! AxisAPos(A) index in the list of machine axes
        if BrakeState=71 then Output "M68" ! Turn axis C brake on
        else Output "M69" ! Turn axis C brake off
      end
    end
    Index = Index + 1
  end
end
```

Another example with cmd operator using.

```pascal
program AxesBrake
  if cmd.Ptr["Axes(AxisAPos)"]<>0 then begin ! Axis A is present in this command
    if cmd.Int["Axes(AxisAPos).BrakeState"]=1 then Output "M680" ! Turn axis A brake on
    else Output "M690" ! Turn axis A brake off
  end
  if cmd.Ptr["Axes(AxisCPos)"]<>0 then begin ! Axis C is present in this command
    if cmd.Int["Axes(AxisCPos).BrakeState"]=1 then Output "M68" ! Turn axis C brake on
    else Output "M69" ! Turn axis C brake off
  end
end
```

## Access from .NET

Handler:

```csharp
public override void OnAxesBrake(ICLDAxesBrakeCommand cmd, CLDArray cld)
```

Inheritance: `ICLDAxesBrakeCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd["..."]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

| Member | Type | Description |
|---|---|---|
| `cmd.AxesCount` | `int` | The count of axes inside the "Axis" list. |
| `cmd.Axis` | `ICLDBrakeAxesIndexer` | The list of axes brake states Axis[i] or Axis["AxisCPos"]. |
| `cmd.Axes` | `IEnumerable` | Axes' enumerator object for the brakes to be possible to use covenient foreach syntax. |
| `cmd.HasAxis(...)` | `bool` | Returns "True" if the "Axis" list contains the axis with the specified textual ID. Otherwise returns "False". |

Example - `OnAxesBrake` (from the Fanuc (30i)_Mill_DN postprocessor):

```csharp
public override void OnAxesBrake(ICLDAxesBrakeCommand cmd, CLDArray cld)
{
    foreach(CLDAxisBrake ax in cmd.Axes) {
        if (ax.IsA) {
            if (ax.StateIsOn)
                nc.MABrake.v = 593;
            else
                nc.MABrake.v = 592;
        } else if (ax.IsB) {
            if (ax.StateIsOn)
                nc.MBBrake.v = 595;
            else
                nc.MBBrake.v = 594;
        } else if (ax.IsC) {
            if (ax.StateIsOn)
                nc.MCBrake.v = 597;
            else
                nc.MCBrake.v = 596;
        }
    }
    if (nc.MABrake.Changed || nc.MBBrake.Changed || nc.MCBrake.Changed)
        nc.Block.Out();
}
```

## See also
- [CLData access model](../cldata.md)
