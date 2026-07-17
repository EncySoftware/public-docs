# MULTIARC - Multi-axis circle movement

## Command caption

How the command appears in the CLData command list:

```text
MULTIARC EPX ep.X, EPY ep.Y, EPZ ep.Z, EPRX ep.Rx, EPRY ep.Ry, EPRZ ep.Rz, EPRW ep.Rw,
         MPX mp.X, MPY mp.Y, MPZ mp.Z, MPRX mp.Rx, MPRY mp.Ry, MPRZ mp.Rz, MPRW mp.Rw
```

**MULTIARC** movement command defines a circular arc passing through three points with a predetermined orientation of the tool in space for each of these points. The figure below SP - starting position in which the tool was before running the command, MP - an intermediate position of the tool at the arc, EP - end position of the tool.

## Access from sppx

Handler: `program MultiArc`

The `cld` array is read by index or by name - in sppx by the typed short name (e.g. `cld.X`), in .NET by the same name as a string key (e.g. `cld["X"]`).

| Parameter | CLD array | CLD name | Description |
|---|---|---|---|
| ep.X<br>ep.Y<br>ep.Z | CLD[1]<br>CLD[2]<br>CLD[3] | CLD.EPX<br>CLD.EPY<br>CLD.EPZ | Cartesian coordinates X, Y and Z of the arc end point |
| ep.Rx<br>ep.Ry<br>ep.Rz<br>ep.Rw | CLD[4]<br>CLD[5]<br>CLD[6]<br>CLD[7] | CLD.EPNX<br>CLD.EPNY<br>CLD.EPNZ<br>CLD.EPNW | The parameters defining the orientation of the tool at the end point of the arc relative to the current coordinate system (fields RX, RY, RZ and RW). Depending on the configuration of the system (defined in the scheme of machine), the tool orientation can be specified by: Normal vector n = (RX, RY, RZ), Spatial angles of rotation around the coordinate axes - the Euler angles (notation of Euler angles, ie the sequence of rotations is also specified in the settings) A = RX, B = RY, C = RZ. Quaternion q = (RX, RY, RZ, RW). |
| mp.X<br>mp.Y<br>mp.Z | CLD[8]<br>CLD[9]<br>CLD[10] | CLD.MPX<br>CLD.MPY<br>CLD.MPZ | Cartesian coordinates X, Y and Z of the arc intermediate point |
| mp.Rx<br>mp.Ry<br>mp.Rz<br>mp.Rw | CLD[11]<br>CLD[12]<br>CLD[13]<br>CLD[14] | CLD.MPNX<br>CLD.MPNY<br>CLD.MPNZ<br>CLD.MPNW | The parameters defining the orientation of the tool at the intermediate point of the arc relative to the current coordinate system (fields RX, RY, RZ and RW). Depending on the configuration of the system (defined in the scheme of machine), the tool orientation can be specified by: Normal vector n = (RX, RY, RZ), Spatial angles of rotation around the coordinate axes - the Euler angles (notation of Euler angles, ie the sequence of rotations is also specified in the settings) A = RX, B = RY, C = RZ. Quaternion q = (RX, RY, RZ, RW). |

### Access by parameter name (helpers)

Parameters available through the `cmd` operator (the same in sppx and .NET):

| TCLDMultiArc: ComplexType | Moving in a circular arc command defined by three points in space. |
|---|---|
| EndPos: ComplexType | cmd.Ptr["EndPos"] - structure whose fields identify the location of tool at the end point of the circle. |
| Axes: Array, Key="AxisID" | cmd.Ptr["EndPos.Axes"] - An array of structures such as Axis. One command may include movement along several axes, the position of each is stored in this array. |
| Axis: ComplexType | cmd.Ptr["EndPos.Axes"].Item[Index] or cmd.Ptr["EndPos.Axes(**AxisName**)"] - Separate element of the Axes array. Contains information about moving on one machine axis. Access to the array elements can either by index or by key field. Here **AxisName** - the key field value, which must match the AxisID field value. |
| AxisID: String | cmd.Str["EndPos.Axes(**AxisName**).AxisID"] - The identifier of the machine axis, for which the specified new position. Determined by the machine schema. |
| Value: Double | cmd.Flt["EndPos.Axes(**AxisName**).Value"] - The new position of the machine axis, in which it moves. |
| Pos5D: ComplexType | cmd.Ptr["EndPos.Pos5D"] - structure containing the coordinates that define the final position of the tool in space. Determines not only the position of the tuning point of the tool (the fields X, Y and Z - cartesian coordinates), but also the orientation of the tool relative to the current coordinate system (fields NX, NY, NZ and NW). Depending on the configuration of the system (defined in the scheme of machine), the tool orientation can be specified by: Normal vector n = (NX, NY, NZ), Spatial angles of rotation around the coordinate axes - the Euler angles (notation of Euler angles, ie the sequence of rotations is also specified in the settings) A = NX, B = NY, C = NZ. Quaternion q = (NX, NY, NZ, NW). |
| X: Double | cmd.Flt["EndPos.Pos5D.X"] - X cartesian coordinate of the tool tip position. |
| Y: Double | cmd.Flt["EndPos.Pos5D.Y"] - Y cartesian coordinate of the tool tip position. |
| Z: Double | cmd.Flt["EndPos.Pos5D.Z"] - Z cartesian coordinate of the tool tip position. |
| NX: Double | cmd.Flt["EndPos.Pos5D.NX"] - depending on the system configuration may be the NX component of the tool normal vector, the rotation angle around one of the coordinate axis, or the coefficient of the quaternion. |
| NY: Double | cmd.Flt["EndPos.Pos5D.NY"] - depending on the system configuration may be the NY component of the tool normal vector, the rotation angle around one of the coordinate axis, or the coefficient of the quaternion. |
| NZ: Double | cmd.Flt["EndPos.Pos5D.NZ"] - depending on the system configuration may be the NZ component of the tool normal vector, the rotation angle around one of the coordinate axis, or the coefficient of the quaternion. |
| NW: Double | cmd.Flt["EndPos.Pos5D.NW"] - if you have chosen a method of orientation tool in the form of a quaternion is a fourth coefficient of quaternion. |
| MachineStateFlags: Integer | cmd.Ptr["EndPos.MachineStateFlags"].Bit[i], i=(0..31). Integer number which is a bit field of 32 bits from 0 to 31. If there are several variants for the location of the machine axes, providing a specified position of the tool in space, every bit of this field determines the selection of one of the possible solutions. For example, a five-axis machine with A and C axes for most of the positions of the tool has two possible solutions - with a positive A-axis and with negative value of the A axis. Zero bit of this field will choose one of these solutions. For a standard six-axis articulated robot many of the tool positions in space can be provided with different combinations of three of its key joints positions (the base, elbow and wrist joints) giving a total of 8 possible solutions. In this case, the zero bit in this field will determine the position of the base, the first bit - the position of the elbow, and the third bit will be set the position of the robot's wrist. Thus, the meaning of each of this bits is determined entirely by the used machine schema. When using machines that do not need to use these flags, it is possible to disable the output of this parameter to CLData in the machine scheme. |
| MidPos: ComplexType | cmd.Ptr["MidPos"] - structure whose fields identify the location of tool at the intermediate point of the circle. |
| Axes: Array, Key="AxisID" | cmd.Ptr["MidPos.Axes"] - An array of structures such as Axis. One command may include movement along several axes, the position of each is stored in this array. |
| Axis: ComplexType | cmd.Ptr["MidPos.Axes"].Item[Index] or cmd.Ptr["MidPos.Axes(**AxisName**)"] - Separate element of the Axes array. Contains information about moving on one machine axis. Access to the array elements can either by index or by key field. Here **AxisName** - the key field value, which must match the AxisID field value. |
| AxisID: String | cmd.Str["MidPos.Axes(**AxisName**).AxisID"] - The identifier of the machine axis, for which the specified new position. Determined by the machine schema. |
| Value: Double | cmd.Flt["MidPos.Axes(**AxisName**).Value"] - The new position of the machine axis, in which it moves. |
| Pos5D: ComplexType | cmd.Ptr["MidPos.Pos5D"] - structure containing the coordinates that define the final position of the tool in space. Determines not only the position of the tuning point of the tool (the fields X, Y and Z - cartesian coordinates), but also the orientation of the tool relative to the current coordinate system (fields NX, NY, NZ and NW). Depending on the configuration of the system (defined in the scheme of machine), the tool orientation can be specified by: Normal vector n = (NX, NY, NZ), Spatial angles of rotation around the coordinate axes - the Euler angles (notation of Euler angles, ie the sequence of rotations is also specified in the settings) A = NX, B = NY, C = NZ. Quaternion q = (NX, NY, NZ, NW). |
| X: Double | cmd.Flt["MidPos.Pos5D.X"] - X cartesian coordinate of the tool tip position. |
| Y: Double | cmd.Flt["MidPos.Pos5D.Y"] - Y cartesian coordinate of the tool tip position. |
| Z: Double | cmd.Flt["MidPos.Pos5D.Z"] - Z cartesian coordinate of the tool tip position. |
| NX: Double | cmd.Flt["MidPos.Pos5D.NX"] - depending on the system configuration may be the NX component of the tool normal vector, the rotation angle around one of the coordinate axis, or the coefficient of the quaternion. |
| NY: Double | cmd.Flt["MidPos.Pos5D.NY"] - depending on the system configuration may be the NY component of the tool normal vector, the rotation angle around one of the coordinate axis, or the coefficient of the quaternion. |
| NZ: Double | cmd.Flt["MidPos.Pos5D.NZ"] - depending on the system configuration may be the NZ component of the tool normal vector, the rotation angle around one of the coordinate axis, or the coefficient of the quaternion. |
| NW: Double | cmd.Flt["MidPos.Pos5D.NW"] - if you have chosen a method of orientation tool in the form of a quaternion is a fourth coefficient of quaternion. |
| MachineStateFlags: Integer | cmd.Ptr["MidPos.MachineStateFlags"].Bit[i], i=(0..31). Integer number which is a bit field of 32 bits from 0 to 31. If there are several variants for the location of the machine axes, providing a specified position of the tool in space, every bit of this field determines the selection of one of the possible solutions. For example, a five-axis machine with A and C axes for most of the positions of the tool has two possible solutions - with a positive A-axis and with negative value of the A axis. Zero bit of this field will choose one of these solutions. For a standard six-axis articulated robot many of the tool positions in space can be provided with different combinations of three of its key joints positions (the base, elbow and wrist joints) giving a total of 8 possible solutions. In this case, the zero bit in this field will determine the position of the base, the first bit - the position of the elbow, and the third bit will be set the position of the robot's wrist. Thus, the meaning of each of this bits is determined entirely by the used machine schema. When using machines that do not need to use these flags, it is possible to disable the output of this parameter to CLData in the machine scheme. |
| Time: Double | The time of the movement in minutes. |

The list of coordinates passed through CLData is defined by the CAM system machine scheme.

Example (from the Newker robot postprocessor):

```pascal
program MultiArc

 !========================== MidPoint ==============================================================
  I = CLD.MPX;  J = CLD.MPY;  K = CLD.MPZ
  I@ = MaxReal; J@ = MaxReal; K@ = MaxReal

!========================== EndPoint ==============================================================
  X = CLD.EPX;  Y = CLD.EPY;  Z = CLD.EPZ
  A = CLD.EPNX; B = CLD.EPNY; C = CLD.EPNZ;
  X@=MaxReal; Y@=MaxReal; Z@=MaxReal
  A@=MaxReal; B@=MaxReal; C@=MaxReal;
!=====================================================================================
  call A1_A6(19, CLD.EndAxesCount)
  A1@=maxreal; A2@=maxreal; A3@=maxreal; A4@=maxreal; A5@=maxreal; A6@=maxreal;

  Formblock
  output "{"+outstr$+"}"

  Speed@=Maxreal
  Formblock

  LineN = LineN + 1; LineN@ = LineN
  output "N"+str(LineN)+" MOVC " + outstr$ + " PL=1.0" + ";Arc"

end
```

## Access from .NET

Handlers:

```csharp
public override void OnBeforeMovement(ICLDMotionCommand cmd, CLDArray cld)   // group handler - before any motion command
public override void OnMultiArc(ICLDMultiArcCommand cmd, CLDArray cld)
public override void OnAfterMovement(ICLDMotionCommand cmd, CLDArray cld)    // group handler - after any motion command
```

Inheritance: `ICLDMultiArcCommand : ICLDMotionCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd["..."]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

| Property | Type | Description |
|---|---|---|
| `cmd.EndP` | `ICLDMultiArcPoint` | Finish point of the arc. |
| `cmd.MidP` | `ICLDMultiArcPoint` | Intermediate point of the arc. |
| `cmd.Time` | double | Duration of the movement in minutes. |
| `cmd.Center` | `TInp5DPoint` | Center point and orientation (Euler angles or quaternion) of the arc. |
| `cmd.R` | double | Arc radius; the sign defines the direction (CW or CCW relative to the arc-plane normal). |
| `cmd.Ang` | double | Arc angle (always positive). |
| `cmd.EP` | `TInp3DPoint` | End point (X, Y, Z). *(inherited from `ICLDMotionCommand`)* |

An arc point (`ICLDMultiArcPoint`) has `P` (cartesian X, Y, Z), `N` (tool orientation: normal vector,
Euler angles or quaternion per the machine scheme), `MSFlags` (machine-state flags), `AxesCount`, `Axis`
(the list of physical machine-axis values at the point), `Axes` (enumerator), and `HasAxis(string ID)`.

Example (from the Fanuc robot postprocessor - all movement commands share the `Motion` method):

```csharp
public override void OnMultiArc(ICLDMultiArcCommand cmd, CLDArray cld)
{
    Motion(cmd);
}

/// <summary>All movement commands call this method (MultiGOTO, PhysicGoto, MultiArc, From)</summary>
void Motion(ICLDMotionCommand movement) 
{
    state.prevPos = state.Pos;
    if (movement.CmdType==CLDCmdType.MultiArc) {
        ICLDMultiArcCommand cmd = movement as ICLDMultiArcCommand;
        state.Pos = new TInpLocation(cmd.MidP.P, cmd.MidP.N);
        state.J.FillJoints(cmd.MidP.Axes);
        state.Flips.Fill(cmd.Int["MidPos.MachineStateFlags"], state.J);
        int midPointIndex = ls.AddPoint(false, state);
        state.middlePos = state.Pos;

        state.Pos = new TInpLocation(cmd.EndP.P, cmd.EndP.N);
        state.J.FillJoints(cmd.EndP.Axes);
        state.Flips.Fill(cmd.Int["EndPos.MachineStateFlags"], state.J);
        int endPointIndex = ls.AddPoint(false, state);

        CalculateCNT(movement);
        AddMotionLine("C P[" + midPointIndex + "] P[" + endPointIndex + "] " + Round(state.velocity/60) + 
            " mm/sec " + FineOrCnt(state.cntValue) + " ACC" + state.accValue + " ;", false);
    } else {
        ICLDMultiMotionCommand cmd = movement as ICLDMultiMotionCommand;
        state.Pos = new TInpLocation(cmd.EP, cmd.EN);
        state.J.FillJoints(cmd.Axes);
        state.Flips.Fill(cmd.Int["MachineStateFlags"], state.J);
        if (movement.CmdType==CLDCmdType.From) {
            // Output nothing, just remember
            return;
        } else if (movement.CmdType==CLDCmdType.MultiGoto) {
            // Lines
            CalculateCNT(movement);
            int pointIndex = ls.AddPoint(false, state);
            AddMotionLine("L P[" + pointIndex + "] " + Round(state.velocity/60) + " mm/sec " + FineOrCnt(state.cntValue) + " ACC" + state.accValue + " ;");
        } else { //PhysicGoto or GoHome
            // Joints
            state.cntValue = smooth.cntValueRapid;
            int pointIndex = ls.AddPoint(true, state);
            if (!state.J.ThereAreE || (state.J.ExtAxesGroup==2)) {
                AddMotionLine("J P[" + pointIndex + "] 10% " + FineOrCnt(state.cntValue) + " ;");
            } else {
                AddMotionLine("J P[" + pointIndex + "] 10% " + FineOrCnt(state.cntValue) + " ACC30;");
            }
        }
    }
}
```

## See also
- [CLData access model](../cldata.md)
