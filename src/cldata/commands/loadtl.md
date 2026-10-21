# LOADTL - Tool loading

## Command caption

How the command appears in the CLData command list:

```text
LOADTL N n, Tool changed 1, X x, Y y, Z z, D d, M m, K k, L l, P p, A a, R r, H h, RC rc,
       PLANE XY(33)|YZ(37)|XZ(41)|YX(133)|ZY(137)|ZX(141),
       DUR d2, HID hid, NX nx, NY ny, NZ nz, NW nw, RevolverID rid
```

**LOADTL** command loads tool of the specified in the first parameter number. Use **LOADTL** command to form NC-program block that move the tooling turret or select the tool from the tool magazine. Also this command is used to form NC-program frames that move the tool to the safe tool changing position.

## Access from sppx

Handler: `program Loadtl`

The `cld` array is read by index or by name - in sppx by the typed short name (e.g. `cld.X`), in .NET by the same name as a string key (e.g. `cld["X"]`).

| Parameter | CLD array | CLD name | Description |
|---|---|---|---|
| n | CLD[1] | CLD.N | Tool number |
| x<br>y<br>z | CLD[2]<br>CLD[3]<br>CLD[4] | CLD.X<br>CLD.Y<br>CLD.Z | Tool offset along axes X, Y, Z relative to tool fixing point (flange coordinate system). |
| d | CLD[5] | CLD.D | Tool diameter. |
| m | CLD[6] | CLD.M | Length corrector number. If the tooling point is the tool end then M < 0. |
| k | CLD[7] | CLD.K | Radius corrector number. If the tooling point is the tool end then K < 0. |
| L | CLD[8] | CLD.L | Tool length. |
| P | CLD[9] | CLD.P | Tool width. |
| a | CLD[10] | CLD.A | Tool approach angle (for external pocketing 180<a<0, for internal pocketing 0<a<90). |
| r | CLD[11] | CLD.R | Nose radius. |
| h | CLD[12] | CLD.H | Tool height. |
| rc | CLD[13] | CLD.Rc | Radius of cylinder part of axial tool. |
| XY(33)<br>YZ(37)<br>XZ(41)<br>YX(133)<br>ZY(137)<br>ZX(141) | CLD[14] |  | Tool plane. A plane normal to the tool axis for axial tool. Machining plane for the lathe tool. 33 – XY, 37 – YZ, 41 – XZ, 133 – YX, 137 – ZY, 141 – ZX. |
|  | CLD[15]<br>CLD[16] |  | Reserved. |
| d2 | CLD[17] | CLD.Dur | Tool durability (minutes). 0 – ignored. |
| HID | CLD[18] | CLD.HID | Tool holder block id (number) |
| nx<br>ny<br>nz<br>nw | CLD[19]<br>CLD[20]<br>CLD[21]<br>CLD[22] | CLD.NX<br>CLD.NY<br>CLD.NZ<br>CLD.NW | The values that define orientation of the tool relative to the anchor point (the flange coordinate system). Depending on the system settings (defined in the machine schema) they can be either rotation angles around the coordinate axes X, Y and Z in degrees (Euler angles A = NX, B = NY, C = NZ), either the coefficients of the quaternion q = (NX, NY, NZ, NW). |

### Access by parameter name (helpers)

Parameters available through the `cmd` operator (the same in sppx and .NET):

| TCLDLoadTool: ComplexType | Tool loading command |
|---|---|
| ToolChanged: bool (integer) | cmd.Int["ToolChanged"] - ToolChanged is a flag that determines whether a tool change is made at this location relative to the previous operation. If it has a value of 1 (true), it means that the tool in this operation is different from the tool in the previous operation. If the flag has a value of 0 (false), it means that the tools in the current and previous operations are the same and there is no tool change. "Skip LoadTL if no tool change" option in the settings window depend on this flag and postprocessor can skip LoadTL procedure calling. |
| ToolID: Integer | cmd.Int["ToolID"] - Tool identifier (number) |
| RadCorrNum: Integer | cmd.Int["RadCorrNum"] - Radius corrector number |
| LenCorrNum: Integer | cmd.Int["LenCorrNum"] - Length corrector number |
| HolderID: Integer | cmd.Int["HolderID"] - Tool holder identifier (number) |
| RevolverID: String | cmd.Str["RevolverID"] - String identifier of the turret head |

Example (from the Fanuc (30i)_Mill postprocessor):

```pascal
program LoadTl
  OutBlock

  H = abs(cld[6]); H@ = H
  
  GFunc = 53; GFunc@ = MaxReal
  Z = 0; Z@ = MaxReal
  OutBlock
  GFunc = 53; GFunc@ = MaxReal
  X = 0; X@ = MaxReal
  Y = 0; Y@ = MaxReal
  OutBlock
  
  M = 06; M@ = M-1
  Tool = cld[1]; Tool@ = MaxReal    ! filling Tool register
  FormBlock
  if NextCode=CodeOfCmd("Comment") then begin
    s$ = CLDFile[CLDFile.CurrentFile].Cmd[CLDFile.CurrentCmd+1].Data
    call TransStr(s$)
    OutStr$ = OutStr$ + " (" + s$ + ")"
  end
  Output OutStr$
  WasLoadTool = 1

  CoordSys = WCSNumber
  CoordSys@ = MaxReal
  OutBlock

  X = MaxReal; X@ = X
  Y = MaxReal; Y@ = Y
  Z = MaxReal; Z@ = Z
!  A = MaxReal; A@ = A
!  B = MaxReal; B@ = B
!  C = MaxReal; C@ = C
end
```

## Access from .NET

Handler:

```csharp
public override void OnLoadTool(ICLDLoadToolCommand cmd, CLDArray cld)
```

Inheritance: `ICLDLoadToolCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd[...]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

| Property | Type | Description |
|---|---|---|
| `cmd.ToolChanged` | bool | True if the tool changed since the previous operation; false if the operation uses the same tool. |
| `cmd.Number` | int | The tool number. |
| `cmd.LCorNum` | int | First corrector number (length corrector) of the tool. |
| `cmd.RCorNum` | int | Second corrector number (radius corrector) of the tool. |
| `cmd.ConnectorIndex` | int | Index of the tool connector inside the machine schema. |
| `cmd.RevolverID` | string | Turret-head identifier for turret machines; tool-connector identifier for other machine types. |
| `cmd.Overhang` | `TInpLocation` | Tooltip overhang (X, Y, Z + orientation angles) relative to a spindle; the orientation type depends on the machine schema (Euler angles, normal vector or quaternion). |
| `cmd.Plane` | `CLDPlaneType` | Tool orientation plane. |
| `cmd.Durability` | double | Tool durability in minutes. |
| `cmd.Geom` | `IToolGeometry` | Main geometrical parameters of the tool: `D` (cutting diameter), `R` (tip rounding radius), `Rc` (rounding radius next to the cylindrical part), `L` (length), `P` (width), `A` (angle), `H` (height of the shaped part). |

Example (from the Sinumerik 840D mill postprocessor):

```csharp
public override void OnLoadTool(ICLDLoadToolCommand cmd, CLDArray cld)
{
    nc.Tool.Show(cmd.Number);
    nc.DTool.Reset(Abs(cmd.LCorNum));
    nc.OutText("M6");
}
```

## See also
- [CLData access model](../cldata.md)
