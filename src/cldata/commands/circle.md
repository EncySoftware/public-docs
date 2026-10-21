# CIRCLE - Circle movement

## Command caption

How the command appears in the CLData command list:

```text
CIRCLE XC xc, YC yc, ZC zc, R r, XE xe, YE ye, ZE ze
```

**CIRCLE** command represents movement along an arc. **CIRCLE** parameters are arc center, arc end point and arc radius. The sign of the radius defines the arc's direction. If the radius is positive then the arc has counter clockwise direction (G03 circle interpolation). If the radius is negative then the arc has clockwise direction (G02 circle interpolation). The arc's plane (G17/G18/G19) is defined by the current machining plane, set by the PLANE command.

## Access from sppx

Handler: `program Circle`

The `cld` array is read by index or by name - in sppx by the typed short name (e.g. `cld.X`), in .NET by the same name as a string key (e.g. `cld["X"]`).

| Parameter | CLD array | CLD name | Description |
|---|---|---|---|
| xc<br>yc<br>zc | CLD[1]<br>CLD[2]<br>CLD[3] | CLD.Xc<br>CLD.Yc<br>CLD.Zc | X, Y and Z coordinates of the arc center. |
| r | CLD[4] | CLD.R | Arc radius. If CLD.R > 0 then the arc is counter clockwise (G03), else if CLD.R < 0 then the arc is clockwise (G02). |
| xe<br>ye<br>ze | CLD[5]<br>CLD[6]<br>CLD[7] | CLD.Xe<br>CLD.Ye<br>CLD.Ze | X, Y and Z coordinates of the arc end point. |
| xs<br>ys<br>zs | CLD[8]<br>CLD[9]<br>CLD[10] | CLD.Xs<br>CLD.Ys<br>CLD.Zs | X, Y and Z coordinates of the arc start point |
| XcInc<br>YcInc<br>ZcInc | CLD[11]<br>CLD[12]<br>CLD[13] | CLD.XcInc<br>CLD.YcInc<br>CLD.ZcInc | X, Y and Z coordinates of the arc center point relative to the start point (I, J and K) |
| RAbs | CLD[14] | CLD.RAbs | Absolute value of the arc radius |
| RIso | CLD[15] | CLD.RIso | Arc radius in ISO variant - positive if angle less than 180 degrees and negative in other case |
| Dir | CLD[16] | CLD.Dir | Direction of the arc: 2-clockwise, 3-counterclockwise relative to the ISO plane G17-G19 |
| Plane | CLD[17] | CLD.Plane | Plane of the arc, can take 6 values: 17, 18, 19, -17, -18, -19. Corresponds to the ISO planes G17-G19. A negative value means that the normal of the arc plane is inverse relative to the standard ISO plane. |
| Length | CLD[18] | CLD.Length | Size of the arc in current linear units |
| Ang | CLD[19] | CLD.Ang | Angle of the arc in degrees (0 to 360 degrees) |
| SAng | CLD[20] | CLD.SAng | Start angle of the arc relative to the first axis of the current plane |
| EAng | CLD[21] | CLD.EAng | End angle of the arc relative to the first axis of the current plane |
| HelixAng | CLD[22] | CLD.HelixAng | Angle of the helix in degrees. zero for planar circle, positive value for rising helix, negative value for descending helix. |

Example (from the Fanuc (30i)_Mill postprocessor):

```pascal
program Circle
  RSign: Integer
  
  if cld[4] > 0 then INTERP_ = 3 else INTERP_ = 2   ! G3/G2
  X = cld[5]                                  ! X,Y,Z in absolutes
  Y = cld[6]
  Z = cld[7]
  if CirclesThroughRadius>0 then begin
    call CheckCircleAngle(RSign)
    Rc = RSign*abs(CLD.R); Rc@ = MaxReal
  end else begin
    XC_ = cld[1] - XT_                            ! I,J,K in increments always
    YC_ = cld[2] - YT_
    ZC_ = cld[3] - ZT_
    XC_@ = MaxReal; ZC_@ = MaxReal
    if OperationIsLathe<>1 then
      YC_@ = MaxReal
    case Plane of
      17: ZC_@ = ZC_;
      18: YC_@ = YC_;
      19: XC_@ = XC_;
    end
  end
  case Plane of
    17: begin
      X@ = MaxReal;
      Y@ = MaxReal
    end
    18: begin
      X@ = MaxReal;
      Z@ = MaxReal
    end
    19: begin
      Y@ = MaxReal
      Z@ = MaxReal
    end
  end
  if IsRotaryInterpolation = 2 then begin
    Y = -Y/CylR/Pi*180
  end
  OutBlock                     ! output to NC block
  XT_ = cld[5]                 ! save current coordinates
  YT_ = cld[6]
  ZT_ = cld[7]
end
```

## Access from .NET

Handlers (the specific handler plus the movement-group brackets that fire for every motion command):

```csharp
public override void OnCircle(ICLDCircleCommand cmd, CLDArray cld)
public override void OnBeforeMovement(ICLDMotionCommand cmd, CLDArray cld)   // before any movement
public override void OnAfterMovement(ICLDMotionCommand cmd, CLDArray cld)    // after any movement
```

Inheritance: `ICLDCircleCommand : ICLDMotionCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd[...]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

| Property | Type | Description |
|---|---|---|
| `cmd.EP` | `TInp3DPoint` | End point (X, Y, Z) of the movement. *(inherited from `ICLDMotionCommand`)* |
| `cmd.SP` | `TInp3DPoint` | Arc start point (X, Y, Z). |
| `cmd.Center` | `TInp3DPoint` | Arc center point (X, Y, Z), absolute. |
| `cmd.IncCenter` | `TInp3DPoint` | Arc center point (I, J, K), incremental to the start point. |
| `cmd.R` | double | Arc radius; positive for CCW (G03), negative for CW (G02). |
| `cmd.RAbs` | double | Absolute value of the arc radius. |
| `cmd.RIso` | double | ISO-standard radius: positive if the arc angle is < 180 deg, negative if > 180 deg. |
| `cmd.Dir` | int | ISO direction code: `2` = CW (G2), `3` = CCW (G3). |
| `cmd.Plane` | int | Plane of the arc: `17, 18, 19, -17, -18, -19` (ISO G17-G19; negative = inverted normal). |
| `cmd.Length` | double | Length of the arc in current linear units. |
| `cmd.Ang` | double | Angle of the arc in degrees (0 to 360). |
| `cmd.SAng`<br>`cmd.EAng` | double | Start / end angle of the arc relative to the first axis of the current plane. |
| `cmd.HelixAng` | double | Helix angle in degrees (0 planar, >0 rising, <0 descending). |

Example (from the Fanuc 30i mill postprocessor):

```csharp
public override void OnCircle(ICLDCircleCommand cmd, CLDArray cld)
{
    nc.GInterp.Show(cmd.Dir);                             // G02 / G03
    nc.X.v = cmd.EP.X;  nc.Y.v = cmd.EP.Y;  nc.Z.v = cmd.EP.Z;
    switch (Abs(cmd.Plane))                               // arc center as incremental I, J, K
    {
        case 17:
            nc.I.v = cmd.IncCenter.X;  nc.J.v = cmd.IncCenter.Y;
            nc.Block.Show(nc.X, nc.Y, nc.I, nc.J);
            break;
        case 18:
            nc.I.v = cmd.IncCenter.X;  nc.K.v = cmd.IncCenter.Z;
            nc.Block.Show(nc.X, nc.Z, nc.I, nc.K);
            break;
        case 19:
            nc.J.v = cmd.IncCenter.Y;  nc.K.v = cmd.IncCenter.Z;
            nc.Block.Show(nc.Y, nc.Z, nc.J, nc.K);
            break;
    }
}
```

## See also
- [CLData access model](../cldata.md)
