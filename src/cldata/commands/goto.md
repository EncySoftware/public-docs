# GOTO - Linear transition

## Command caption

How the command appears in the CLData command list:

```text
GOTO.abs X x, Y y, Z z
```

CAM system passes linear transition data through **ABSMOV** (`GOTO.abs`) command. The parameters of the command are the new absolute coordinates along the X, Y and Z axes.

## Access from sppx

Handler: `program AbsMov`

| Parameter | CLD array | CLD name | Description |
|---|---|---|---|
| x<br>y<br>z | CLD[1]<br>CLD[2]<br>CLD[3] | CLD.X<br>CLD.Y<br>CLD.Z | New tool coordinates (absolute) |

Example (from the Fanuc (30i)_Mill postprocessor):

```pascal
program AbsMov  
  if (INTERP_ > 1) and (INTERP_ <> 33) then
    INTERP_ = 1    ! G1
  X = cld[1]                         ! X,Y,Z in absolutes
  Y = cld[2]
  if IsRotaryInterpolation = 2 then begin
    Y = -Y/CylR/Pi*180
  end
  Z = cld[3]
  if (Z<>Z@) and (NeedKorDl<>0) then begin
    KorDl = NeedKorDl; KorDl@ = MaxReal
    H@ = MaxReal
    NeedKorDl = 0
  end
  if (CycleOn=0) and ((X<>X@) or (Y<>Y@) or (Z<>Z@)) then begin
    if KorEcv<>KorEcv@ then begin
      if Interp_<>Interp_@ then begin
        X@ = X
        Y@ = Y
        Z@ = Z
        KorEcv@ = KorEcv
        D@ = D
        OutBlock
        KorEcv@ = MaxReal
        D@ = MaxReal
      end
      X@ = MaxReal !XT_
      Y@ = MaxReal !YT_
      Z@ = MaxReal !ZT_
    end
    if IsMultiaxisInterpolation = 1 then begin
      X@ = MaxReal;
      Y@ = MaxReal;
      Z@ = MaxReal;
    end;
    OutBlock
  end
  XT_ = X;  YT_ = Y;  ZT_ = Z        ! save current coordinates
end
```

## Access from .NET

Handlers:

```csharp
public override void OnBeforeMovement(ICLDMotionCommand cmd, CLDArray cld)   // group handler - before any motion command
public override void OnGoto(ICLDGotoCommand cmd, CLDArray cld)
public override void OnAfterMovement(ICLDMotionCommand cmd, CLDArray cld)   // group handler - after any motion command
```

Inheritance: `ICLDGotoCommand : ICLDMotionCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd["..."]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

| Member | Type | Description |
|---|---|---|
| `cmd.EP` | `TInp3DPoint` | End point (X, Y, Z) of the movement |

Example - `OnGoto` (from the Fanuc (30i)_Mill_DN postprocessor):

```csharp
public override void OnGoto(ICLDGotoCommand cmd, CLDArray cld)
{
    if (nc.GInterp > 1)
        nc.GInterp.v = 1;
    nc.X.v = cmd.EP.X;
    nc.Y.v = cmd.EP.Y;
    nc.Z.v = cmd.EP.Z;

    if (!cycleIsOn) {
        if (nc.Z.Changed && nc.GLCompens.ValuesDiffer) {
            nc.Block.Hide(nc.X, nc.Y);
            nc.Block.Show(nc.GLCompens, nc.HLCompens, nc.Z);
            nc.Block.Out();
            nc.Block.UpdateState(nc.X, nc.Y);
        }            
        // Uncomment if you want mandatory XYZABC in TCPM mode
        // if (nc.GLCompens == 43.4) {
        //     nc.Block.Show(nc.X, nc.Y, nc.Z);
        //     if (CLDProject.Machine.HasAAxis)
        //         nc.A.Show();
        //     if (CLDProject.Machine.HasBAxis)
        //         nc.B.Show();
        //     if (CLDProject.Machine.HasCAxis)
        //         nc.C.Show();
        // } 
        if(nc.X.Changed || nc.Y.Changed || nc.Z.Changed )               
            nc.Block.Out();
    }
    nc.LastP = cmd.EP;
}
```

## See also
- [CLData access model](../cldata.md)
