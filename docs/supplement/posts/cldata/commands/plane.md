# PLANE - Working plane

## Command caption

How the command appears in the CLData command list:

```text
PLANE XY(33) | YZ(37) | XZ(41) | YX(133) | ZY(137) | ZX(141)
```

**PLANE** command is used to define active machining plane. Commonly this command is processed into G17, G18, G19 G-codes. Active plane is used in circular interpolation (it defines plane of arcs), to implement tool radius offset, to define hole machining cycles etc.

## Access from sppx

Handler: `program Plane`

| Parameter | CLD array | CLD name | Description |
|---|---|---|---|
| XY(33)<br>YZ(37)<br>XZ(41)<br>YX(133)<br>ZY(137)<br>ZX(141) | CLD[1] | CLD.Plane | Plane code: 33 – XY, 37 – YZ, 41 – XZ, 133 – YX, 137 – ZY, 141 – ZX. |

To create ISO postprocessor use ISO.G mask, which is assigned the plane code automatically:

| CLD item value | ISO value |
|---|---|
| CLD[1] = 33 | ISO.G = 17 |
| CLD[1] = 37 | ISO.G = 19 |
| CLD[1] = 41 | ISO.G = 18 |

Example (from the Fanuc (30i)_Mill postprocessor):

```pascal
program Plane
  case cld[1] of
    33: Plane = 17;      ! XY
    37: Plane = 19;      ! YZ
    41: Plane = 18;      ! XZ
    133: Plane = -17;      ! XY
    137: Plane = -19;      ! YZ
    141: Plane = -18;      ! XZ
  end
  if (Plane<>Plane@) and (abs(Plane)=abs(Plane@)) then
    Plane@ = Plane
!  if Plane<>Plane@ then
!    OutBlock
  case abs(Plane) of
    17: begin
      regZPlane = Rgs["Z"].Num
      regZCycle = Rgs["ZCYCLE"].Num
    end
    18: begin
      regZPlane = Rgs["Y"].Num
      regZCycle = Rgs["YCYCLE"].Num
    end
    19: begin
      regZPlane = Rgs["X"].Num
      regZCycle = Rgs["XCYCLE"].Num
    end
    else begin
      regZPlane = Rgs["Z"].Num
      regZCycle = Rgs["ZCYCLE"].Num
    end
  end
end
```

## Access from .NET

Handler:

```csharp
public override void OnPlane(ICLDPlaneCommand cmd, CLDArray cld)
```

Inheritance: `ICLDPlaneCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd["..."]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

| Member | Type | Description |
|---|---|---|
| `cmd.Plane` | `CLDPlaneType` | Contains exact plane type. 6 standard values are possible: XY, YZ, ZX, InvXY, InvYZ, InvZX.<br>Possible values:<br>`XY` (17) - Standard plane XY or G17<br>`YZ` (19) - Standard plane YZ or G19<br>`ZX` (18) - Standard plane ZX or G18<br>`InvXY` (-17) - Standard plane opposite to XY plane (-17)<br>`InvYZ` (-19) - Standard plane opposite to YZ plane (-19)<br>`InvZX` (-18) - Standard plane opposite to ZX plane (-18) |
| `cmd.PlaneGCode` | `int` | Contains standard ISO G-code number for the plane type. 6 values are possible: 17, 18, 19, -17, -18, -19. |
| `cmd.PlaneSign` | `int` | Returns "+1" for the planes XY, YZ, ZX. Returns "-1" for the planes InvXY, InvYZ and InvZX. |

Example - `OnPlane` (from the Fanuc (30i)_Mill_DN postprocessor):

```csharp
public override void OnPlane(ICLDPlaneCommand cmd, CLDArray cld)
{
    nc.GPlane.v = cmd.PlaneGCode;
    planeSign = cmd.PlaneSign;
    switch (cmd.Plane) {
        case CLDPlaneType.XY: 
        case CLDPlaneType.InvXY:
            planeZIndex = 3;
            nc.PlaneZReg = nc.Z;
            break;
        case CLDPlaneType.ZX: 
        case CLDPlaneType.InvZX:
            planeZIndex = 2;
            nc.PlaneZReg = nc.Y;
            break;
        case CLDPlaneType.YZ: 
        case CLDPlaneType.InvYZ:
            planeZIndex = 1;
            nc.PlaneZReg = nc.X;
            break;
    }
}
```

## See also
- [CLData access model](../cldata.md)
