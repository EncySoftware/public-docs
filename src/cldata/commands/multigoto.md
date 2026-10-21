# MULTIGOTO - Multi-coordinate movement

## Command caption

How the command appears in the CLData command list:

```text
MULTIGOTO COUNT 2, MACHINE, X 34.725, Y 32, GEOM X 34.725, Y 32, Z 194, NX 0, NY 0, NZ 1, NW 0, MSF 0, Time 0.003
```

**MULTIGOTO** is a universal technology command that is used to pass machine coordinate movement. **MULTIGOTO** command is used to pass a variable number of coordinates (also called "axes") to postprocessor. These coordinates can be linear movement of tool or table, table or tool rotation or movement of other machine coordinates. Also **MULTIGOTO** is used to pass miscellaneous technology commands specific for a given machine that can not be passed through more specialized commands. **MULTIGOTO** command can be used to control common axes like X, Y, Z linear movement, or A, B, C rotatable axes or to control "axes" like chuck jaws, spindle brake, lunet movement and so on. The list of the machine coordinates is defined by the kinematic scheme.

## Access from sppx

Handler: `program MultiGOTO`

The `cld` array is read by index or by name - in sppx by the typed short name (e.g. `cld.X`), in .NET by the same name as a string key (e.g. `cld["X"]`).

| Parameter | CLD array | CLD name | Description |
|---|---|---|---|
| X<br>Y<br>Z | CLD[1]<br>CLD[2]<br>CLD[3] | CLD.X<br>CLD.Y<br>CLD.Z | Tooltip spatial coordinates, relative to the active workpiece CS |
| NX<br>NY<br>NZ<br>NW | CLD[4]<br>CLD[5]<br>CLD[6]<br>CLD[7] | CLD.NX<br>CLD.NY<br>CLD.NZ<br>CLD.NW | Tool frame orientation, relative to the active workpiece CS. The way of orientation definition depend on setting inside Machine schema. It can be Euler angles in different conventions, Tool normal vector, quaternion or rotated vector. |
| MSF | CLD[8] | CLD.MSF | Machine state flags (flips). Actual for the robots and machines that can have multiple configurations of physical axes for same spatial position. See description in the next table. |
| Time | CLD[9] | CLD.Time | The time of movement. |
| AxesCount | CLD[10] | CLD.AxesCount | Number of physical machine coordinates affected in this command. |
| r1 | CLD[11] |  | Index of axis named Axis1Pos in the coordinates list. |
| Val1 | CLD[12] |  | Value of the machine coordinate Axis1Pos. |
| r2 | CLD[13] |  | Index of axis named Axis2Pos in the coordinates list. |
| Val2 | CLD[14] |  | Value of the machine coordinate Axis2Pos. |
| … | … |  | … |
| rN | CLD[2*N+9] |  | Index of axis named AxisNPos in the coordinates list. |
| ValN | CLD[2*N+10] |  | Value of the machine coordinate AxisNPos. |

### Access by parameter name (helpers)

Parameters available through the `cmd` operator (the same in sppx and .NET):

| TCLDMultiGoto: ComplexType | Multi coordinate movement command |
|---|---|
| Axes: Array, Key="AxisID" | cmd.Ptr["Axes"] - An array of structures such as Axis. One command may include movement along several axes, the position of each is stored in this array. |
| Axis: ComplexType | cmd.Ptr["Axes"].Item[Index] or cmd.Ptr["Axes(**AxisName**)"] - Separate element of the Axes array. Contains information about moving on one machine axis. Access to the array elements can either by index or by key field. Here **AxisName** - the key field value, which must match the AxisID field value. |
| AxisID: String | cmd.Str["Axes(**AxisName**).AxisID"] - The identifier of the machine axis, for which the specified new position. Determined by the machine schema. |
| Value: Double | cmd.Flt["Axes(**AxisName**).Value"] - The new position of the machine axis, in which it moves. |
| Pos5D: ComplexType | cmd.Ptr["Pos5D"] - structure containing the coordinates that define the final position of the tool in space. Determines not only the position of the tuning point of the tool (the fields X, Y and Z - cartesian coordinates), but also the orientation of the tool relative to the current coordinate system (fields NX, NY, NZ and NW). Depending on the configuration of the system (defined in the scheme of machine), the tool orientation can be specified by: Normal vector n = (NX, NY, NZ), Spatial angles of rotation around the coordinate axes - the Euler angles (notation of Euler angles, ie the sequence of rotations is also specified in the settings) A = NX, B = NY, C = NZ. Quaternion q = (NX, NY, NZ, NW). |
| X: Double | cmd.Flt["Pos5D.X"] - X cartesian coordinate of the tool tip position. |
| Y: Double | cmd.Flt["Pos5D.Y"] - Y cartesian coordinate of the tool tip position. |
| Z: Double | cmd.Flt["Pos5D.Z"] - Z cartesian coordinate of the tool tip position. |
| NX: Double | cmd.Flt["Pos5D.NX"] - depending on the system configuration may be the NX component of the tool normal vector, the rotation angle around one of the coordinate axis, or the coefficient of the quaternion. |
| NY: Double | cmd.Flt["Pos5D.NY"] - depending on the system configuration may be the NY component of the tool normal vector, the rotation angle around one of the coordinate axis, or the coefficient of the quaternion. |
| NZ: Double | cmd.Flt["Pos5D.NZ"] - depending on the system configuration may be the NZ component of the tool normal vector, the rotation angle around one of the coordinate axis, or the coefficient of the quaternion. |
| NW: Double | cmd.Flt["Pos5D.NW"] - if you have chosen a method of orientation tool in the form of a quaternion is a fourth coefficient of quaternion. |
| MachineStateFlags: Integer | cmd.Ptr["MachineStateFlags"].Bit[i], i=(0..31). Integer number which is a bit field of 32 bits from 0 to 31. If there are several variants for the location of the machine axes, providing a specified position of the tool in space, every bit of this field determines the selection of one of the possible solutions. For example, a five-axis machine with A and C axes for most of the positions of the tool has two possible solutions - with a positive A-axis and with negative value of the A axis. Zero bit of this field will choose one of these solutions. For a standard six-axis articulated robot many of the tool positions in space can be provided with different combinations of three of its key joints positions (the base, elbow and wrist joints) giving a total of 8 possible solutions. In this case, the zero bit in this field will determine the position of the base, the first bit - the position of the elbow, and the third bit will be set the position of the robot's wrist. Thus, the meaning of each of this bits is determined entirely by the used machine schema. When using machines that do not need to use these flags, it is possible to disable the output of this parameter to CLData in the machine scheme. |
| Time: Double | The time of the movement in minutes. |

The list of coordinates passed through CLData of **MULTIGOTO** command is defined by the CAM system machine scheme.

Use the GMA array to process the **MULTIGOTO** command. The properties of the GMA array are automatically assigned precalculated values of coordinate movement parameters. The command parameters are also available through the cmd operator.

A simple example of **MULTIGOTO** command handler with cmd operator using below.

```pascal
program MultiGoto
  if cmd.Ptr["Axes(AxisXPos)"]<>0 then begin
    X = cmd.Flt["Axes(AxisXPos).Value"]
  end
  if cmd.Ptr["Axes(AxisYPos)"]<>0 then begin
    Y = cmd.Flt["Axes(AxisYPos).Value"]
  end
  if cmd.Ptr["Axes(AxisZPos)"]<>0 then begin
    Z = cmd.Flt["Axes(AxisZPos).Value"]
  end
  if cmd.Ptr["Axes(AxisCPos)"]<>0 then begin
    C = cmd.Flt["Axes(AxisCPos).Value"]
  end
  OutBlock
end
```

## Access from .NET

Handlers (the specific handler plus the movement-group brackets):

```csharp
public override void OnMultiGoto(ICLDMultiGotoCommand cmd, CLDArray cld)
public override void OnBeforeMovement(ICLDMotionCommand cmd, CLDArray cld)
public override void OnAfterMovement(ICLDMotionCommand cmd, CLDArray cld)
```

Inheritance: `ICLDMultiGotoCommand : ICLDMultiMotionCommand : ICLDMotionCommand : ICLDCommand`
(`ICLDMultiGotoCommand` adds no members of its own; everything below is inherited from
`ICLDMultiMotionCommand` / `ICLDMotionCommand`).

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd[...]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

| Member | Type | Description |
|---|---|---|
| `cmd.EP` | `TInp3DPoint` | End point (X, Y, Z) of the movement. *(from `ICLDMotionCommand`)* |
| `cmd.EN` | `TInpRotation` | End normal or orientation of the movement (normal vector, Euler angles, quaternion, ... per the machine scheme). |
| `cmd.MSFlags` | `BitArray` | Machine state flags / robot flips that (together with the cartesian coordinates) define the mechanism state in case of redundancy; the meaning of each bit depends on the equipment. |
| `cmd.Time` | double | Duration of the movement in minutes. |
| `cmd.AxesCount` | int | The count of axes contained in the `Axis[]` list. |
| `cmd.Axis` | `ICLDMultiMotionAxesIndexer` | The list of the movement's axes `[0..AxesCount-1]`; indexable by position, by textual `ID`, or by name (`Axis.X/.Y/.Z/.A/.B/.C/.C1/.C2/.A1..A6/.E1..E3`, `null` if absent). |
| `cmd.Axes` | `IEnumerable` | Axes enumerator, for `foreach`. |
| `cmd.HasAxis(string ID)` | bool | True if the movement contains an axis with the specified textual ID. |

An axis element (`CLDMultiMotionAxis`) has `IntID` (numeric machine-axis id), `ID` (textual machine-axis id
as defined in the machine schema), `Value` (final axis value; units - mm/inch/deg/pulse - per the axis
definition), and `IsX/IsY/IsZ/IsA/...` tests.

Example (from the Fanuc 30i mill postprocessor):

```csharp
public override void OnMultiGoto(ICLDMultiGotoCommand cmd, CLDArray cld)
{
    foreach (CLDMultiMotionAxis ax in cmd.Axes)
    {
        if (ax.IsX) nc.X.v = ax.Value;
        else if (ax.IsY) nc.Y.v = ax.Value;
        else if (ax.IsZ) nc.Z.v = ax.Value;
        else if (ax.IsA) nc.A.v = ax.Value;
        else if (ax.IsB) nc.B.v = ax.Value;
        else if (ax.IsC) nc.C.v = ax.Value;
    }
    nc.Block.Out();
}
```

## See also
- [CLData access model](../cldata.md)
