# CUTCOM - Tool compensation

## Command caption

How the command appears in the CLData command list:

```text
CUTCOM ON(71)|OFF(72), LENGTH(9)|R(23) lr, X x, Y y, Z z,
XY n, YZ m, XZ k, RIGHT(24)|LEFT(8)
```

Use **CUTCOM** command to switch compensation mode for length or radius of the tool.

## Access from sppx

Handler: `program CutCom`

| Parameter | CLD array | CLD name | Description |
|---|---|---|---|
| ON(71)<br>OFF(72) | CLD[1] | CLD.OnOff | Command type: 71 – Enable compensation, 72 – Disable compensation. |
| LENGTH(9)<br>R(23) | CLD[2] | CLD.Length | Compensation kind: 9 – tool length compensation, 23 – tool radius compensation. |
| LR | CLD[3] | CLD.LR | Tool length or radius compensation value. |
| x<br>y<br>z | CLD[4]<br>CLD[5]<br>CLD[6] | CLD.X<br>CLD.Y<br>CLD.Z | Compensation along axes. |
| n<br>m<br>k | CLD[7]<br>CLD[8]<br>CLD[9] | CLD.N<br>CLD.M<br>CLD.K | Plane compensation values. |
| RIGHT(24)<br>LEFT(8) | CLD[10] | CLD.RGT | Tool radius compensation direction: 24 – right compensation, 8 – left compensation. |

To create ISO postprocessor using masks use ISO.G values which correspond to **CUTCOM** parameters:

| CLD parameter | ISO value |
|---|---|
| CLD[1] = 72, CLD[2] = 9 | ISO.G = 49 |
| CLD[1] = 71, CLD[2] = 9 | ISO.G = 43 |
| CLD[1] = 72, CLD[2] = 23 | ISO.G = 40 |
| CLD[1] = 71, CLD[2] = 23, CLD[10] = 24 | ISO.G = 42 |
| CLD[1] = 71, CLD[2] = 23, CLD[10] = 8 | ISO.G = 41 |

Example (from the Fanuc (30i)_Mill postprocessor):

```pascal
program CutCom
  if cld[2]=9 then begin                       ! LENGTH
    X = MaxReal; X@ = X
    Y = MaxReal; Y@ = Y
    Z = MaxReal; Z@ = Z
    if cld[1]=71 then begin ! On
      CoordSys = WCSNumber
      OutBlock
      if (NeedKorDl=0) and (OperationIsLathe=0) and
         ((WasLoadTool>0) or (H<>cld[3]))
      then begin
        NeedKorDl = 43
        H = cld[3]; H@ = H
      end
      OutBlock
    end else begin          ! Off
      KORDL = 49; !KORDL@ = MaxReal
      H = 0; H@ = H
      OutBlock

      call SwitchOffLocalCS
    end
  end else if cld[2]=23 then begin             ! RADIUS
    if cld[1]=72 then
      KorEcv = 40
    else begin
      if GFeed<>GFeed@ then OutBlock
      if cld[10]=24 then KorEcv=42 else KorEcv=41
      D = cld[3]
      D@ = MaxReal
    end
  end else begin
  end
end
```

## Access from .NET

Handlers:

```csharp
public override void OnCutCom(ICLDCutComCommand cmd, CLDArray cld)
public override void OnLengthCompensation(ICLDCutComCommand cmd, CLDArray cld)   // LENGTH(9) compensation
public override void OnRadiusCompensation(ICLDCutComCommand cmd, CLDArray cld)   // RADIUS(23) compensation
```

Inheritance: `ICLDCutComCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd["..."]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

| Member | Type | Description |
|---|---|---|
| `cmd.IsOn` | `bool` | Returns "True" if it's a compensation switch ON command, otherwise returns "False". |
| `cmd.IsOff` | `bool` | Returns "True" if it's a compensation switch OFF command, otherwise returns "False". |
| `cmd.IsLength` | `bool` | Returns "True" if it's a LENGTH compensation switch command, otherwise returns "False". |
| `cmd.IsRadius` | `bool` | Returns "True" if it's a RADIUS compensation switch command, otherwise returns "False". |
| `cmd.IsRightDirection` | `bool` | Defines direction for the compensation. "True" means right direction, "False" means left direction. |
| `cmd.IsLeftDirection` | `bool` | Defines direction for the compensation. "True" means left direction, "False" means right direction. |
| `cmd.CorrectorNumber` | `int` | Number of tool corrector in machine's correctors table. |

Example - `OnLengthCompensation` (from the Fanuc (30i)_Mill_DN postprocessor):

```csharp
public override void OnLengthCompensation(ICLDCutComCommand cmd, CLDArray cld)
{
    if (cmd.IsOn) {
        nc.GLCompens.Reset(43);
        nc.HLCompens.Reset(cmd.CorrectorNumber);
    } else {
        nc.GLCompens.Show(49);
        nc.HLCompens.Hide(0);
        nc.Block.Out();
    }
}
```

Example - `OnRadiusCompensation` (from the Fanuc (30i)_Mill_DN postprocessor):

```csharp
public override void OnRadiusCompensation(ICLDCutComCommand cmd, CLDArray cld)
{
    if (cmd.IsOn) {
        if (cmd.IsLeftDirection)
            nc.GRCompens.Show(41);
        else
            nc.GRCompens.Show(42);
        nc.DRCompens.Show(cmd.CorrectorNumber);
    } else {
        nc.GRCompens.Show(40);
    }
}
```

## See also
- [CLData access model](../cldata.md)
