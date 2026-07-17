# FROM - Original point

## Command caption

How the command appears in the CLData command list:

```text
FROM COUNT 5, MACHINE, X 0, Y 0, Z 254, A 0, C 0, GEOM X 10, Y 0, Z 194, NX 0, NY 0, NZ 1, NW 0, MSF 0, Time 0
```

**FROM** command defines original point coordinates. Usually **FROM** command is called only once at the beginning of machining, the first transition coordinates commonly equal the **FROM** command coordinates. If is necessary to avoid output of original point into the NC-program use the **FROM** command to initialize register values without printing them out into the NC-program code. This prevents the output of movement commands if the travel coordinates equal those of the **FROM** command.

## Access from sppx

Handler: `program From`

| Parameter | CLD array | CLD name | Description |
|---|---|---|---|
| X<br>Y<br>Z | CLD[1]<br>CLD[2]<br>CLD[3] | CLD.X<br>CLD.Y<br>CLD.Z | Original tooltip point spatial coordinates, relative to the active workpiece CS |
| NX<br>NY<br>NZ<br>NW | CLD[4]<br>CLD[5]<br>CLD[6]<br>CLD[7] | CLD.NX<br>CLD.NY<br>CLD.NZ<br>CLD.NW | Original tool frame orientation, relative to the active workpiece CS. The way of orientation definition depend on setting inside Machine schema. It can be Euler angles in different conventions, Tool normal vector, quaternion or rotated vector. |
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

Parameters available through the cmd operator

| TCLDFrom: ComplexType | Original point coordinates command |
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

The list of coordinates passed through CLData of **FROM** command is defined by the CAM system machine scheme.

Use the GMA array to process the **FROM** command. The properties of the GMA array are automatically assigned precalculated values of coordinate movement parameters. The command parameters are also available through the cmd operator.

Example (from the Heidenhain (iTNC530)_Mill postprocessor):

```pascal
program From  
  !X = CLD[1]; X@ = X; XT_ = X
  !Y = CLD[2]; Y@ = Y; YT_ = Y
  !Z = CLD[3]; Z@ = Z; ZT_ = Z
  !A = 0; A@ = A; AT_ = A
  !B = 0; B@ = B; BT_ = B
  !C = 0; C@ = C; CT_ = C
End
```

## Access from .NET

Handlers:

```csharp
public override void OnBeforeMovement(ICLDMotionCommand cmd, CLDArray cld)   // group handler - before any motion command
public override void OnFrom(ICLDFromCommand cmd, CLDArray cld)
public override void OnAfterMovement(ICLDMotionCommand cmd, CLDArray cld)   // group handler - after any motion command
```

Inheritance: `ICLDFromCommand : ICLDMultiMotionCommand : ICLDMotionCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd["..."]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

| Member | Type | Description |
|---|---|---|
| `cmd.EN` | `TInpRotation` | End normal or orientation of the movement in cartesian coordinate system. It can be normal vector, euler angles, quaternion etc. depend on the current machine schema settings. |
| `cmd.MSFlags` | `BitArray` | Machine state flags or robot flips which can help to define (together with cartesian coordinates) the specific state of the mechanism in case of redundancy. Which bit is responsible for which flag depends on the type and configuration of the equipment. |
| `cmd.Time` | `double` | Duration of the movement in minutes. |
| `cmd.AxesCount` | `int` | The count of axes that the movement contains inside the Axis[] list. |
| `cmd.Axis` | `ICLDMultiMotionAxesIndexer` | The list of the movement's axes [0..(AxesCount-1)]. |
| `cmd.Axes` | `IEnumerable` | Axes' enumerator object for the movement to be possible to use covenient foreach syntax. |
| `cmd.HasAxis(...)` | `bool` | Returns "true" if the movement contains axis with the speciefed textual ID. Otherwise returns "false". |
| `cmd.EP` | `TInp3DPoint` | End point (X, Y, Z) of the movement |

Example - `OnFrom` (from the Sinumerik (840D)_Mill_DN postprocessor):

```csharp
public override void OnFrom(ICLDFromCommand cmd, CLDArray cld)
{
    nc.X.Hide(cld[1]); nc.Y.Hide(cld[2]); nc.Z.Hide(cld[3]);
    LastPnt.X = cld[1]; LastPnt.Y = cld[2]; LastPnt.Z = cld[3];
}
```

## See also
- [CLData access model](../cldata.md)
