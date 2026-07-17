# CYCLE - Hole machining cycles

> **Kept for compatibility.** **CYCLE** is retained only for compatibility with older postprocessors. Current versions of the CAM system generate the [extended cycle command **EXTCYCLE**](../extcycle/extcycle.md) instead: it offers more capabilities and lets the CAM system fully simulate all of the cycle's nested motions, which **CYCLE** does not. Output of **CYCLE** can still be turned on in the CAM system settings, but this is not recommended.

## Command caption

How the command appears in the CLData command list:

```text
CYCLE ON(71) | OFF(72) | DRILL(163) | FACE(81) | DEEP(153) |
BRKCHP(288) | TAP(168) | BORE5(209) | BORE6(210) | BORE7(211) |
BORE8(212) | BORE9(213)
```

**CYCLE** command is used to pass standard drilling cycles G81-G89. Use **CYCLE** command to determine cycle type and process the cycle accordingly. Cycle type is specified by the first parameter, other parameters types and their number depends on the cycle type.

## Access from sppx

Handler: `program Cycle`

The `cld` array is read by index or by name - in sppx by the typed short name (e.g. `cld.Type`), in .NET by the same name as a string key (e.g. `cld["Type"]`).

| Parameter | CLD array | CLD name | Description |
|---|---|---|---|
| Type | CLD[1] | CLD.Type | Cycle type: 71(ON) – turn cycle on, 72(OFF) – turn cycle off, [163(DRILL) - G81 drilling cycle](g81.md), [81(FACE) - G82 drilling cycle](g82.md), [153(DEEP) - Deep drilling cycle](deep-chip-removing.md), [288(BRKCHP) - Drilling with chip breaking](deep-chip-breaking.md), [168(TAP) - G84 Tapping cycle](g84.md), [209(BORE5) - G85 drilling cycle](g85.md), [210(BORE6) - G86 drilling cycle](g86.md), [211(BORE7) - G87 drilling cycle](g87.md), [212(BORE8) - G88 drilling cycle](g88.md), [213(BORE9) - G89 drilling cycle](g89.md). |

Usually CAM system generates drilling technology similar to the following:

```text
...
GOTO.abs X, Y, Z ! Position the tool at the first hole.
CYCLE DRILL(163) ! Perform the drilling calling cycle of appropriate type.
GOTO.abs X, Y, Z ! Move the tool to the next hole.
CYCLE DRILL(163) ! Perform the drilling calling cycle of appropriate type.
...
GOTO.abs X, Y, Z ! Move the tool to the last hole.
CYCLE DRILL(163) ! Perform drilling by calling cycle of appropriate type.
CYCLE OFF(72) ! Turn cycle off.
...
```

The first drilling cycle command should form the NC-block containing a cycle definition (like G81) and cycle parameters. For example:

```text
G81 X_Y_Z_R_F_
```

Following commands processing should form block containing only the changed registers. For example:

```text
X_Y_Z_
X_Y_Z_
...
X_Y_Z_
```

The `CYCLE OFF(72)` command should form the code of cancelling cycle. For example:

```text
G80
```

When developing ISO postprocessors using masks ISO.G operator can be used. The value of ISO.G is set automatically according to the following table:

| CLD parameter value | ISO.G value |
|---|---|
| CLD[1] = 163 | ISO.G = 81 |
| CLD[1] = 81 | ISO.G = 82 |
| CLD[1] = 168 | ISO.G = 84 |
| CLD[1] = 209 | ISO.G = 85 |
| CLD[1] = 210 | ISO.G = 86 |
| CLD[1] = 211 | ISO.G = 87 |
| CLD[1] = 212 | ISO.G = 88 |
| CLD[1] = 213 | ISO.G = 89 |
| CLD[1] = 153 | ISO.G = 83 |
| CLD[1] = 288 | ISO.G = 73 |
| CLD[1] = 72 | ISO.G = 80 |

Example (from the Fanuc (30i)_Mill postprocessor):

```pascal
program Cycle
  if cld[1]=71 then CycleOn = 1 else ! cycle On
  if cld[1]=72 then CycleOn = 0 else ! cycle Off
  begin
    CycleOn = 1                      ! cycle On
    KodCycle = cld[1]
    Za = cld[2]                      ! work depth
    if cld[4] > 0 then begin         ! creating FEED_ value
      if cld[3]=316 then Fr=cld[4]*S else Fr=cld[4]
    end
    Zf = cld[5]                      ! safe level
    ZP_ = cld[6]                      ! reverse move level
    Dwell = cld[10]*1000              ! dwell time
    Zl = cld[6]                      ! depth of one drilling step
    Zi = cld[8]                    ! transitional value

  end

  if CycleOn=1 then begin
    !X@=maxreal; Y@ = maxreal;
    !Feed_@=Maxreal;
    Zcycle=Zf-Za
    ZClear=Zf
    p=0;  P@=0
    If KodCycle=153 or KodCycle=288 or KodCycle=211 then Q=Zl else Q=0
    If KodCycle=81 or KodCycle=213 then P=Dwell else P=0
    if KodCycle=163 then Cycle = 81   ! DRILL
    if KodCycle=81  then Cycle = 82   ! FACE
    if KodCycle=168 then begin
      Fr = S * cld[12]
      ! Klient: Pered cziklom narezaniya
      ! rezby dolzhna stoyat strochka M84S2000 (zhyostkoj)
      if (Cycle<>84) and (Cycle<>74) then begin
        if cld[14]=1 then  ! esli zhyostkij tip derzhatelya
          output "M84 S" + Str(S);
      end
      if Msp=4 then ! SHpindel nazad krutitsya, levaya relba
        Cycle = 74
      else          ! SHpindel vperyod krutitsya, obychnaya relba
        Cycle = 84;
    end;
    if KodCycle=209 then Cycle = 85   ! BORE5
    if KodCycle=210 then begin ! BORE6
      if cld[14]>0 then begin
        Cycle = 76;
        QStep = sqr(cld[6]^2+cld[7]^2);
!        DrillPause = cld[15]*1000;
!        if DrillPause=0 then
!          DrillPause@ = 0
      end else begin
        Cycle = 86;
      end
    end
    if KodCycle=211 then begin ! BORE7
      if cld[14]>0 then begin
        call Swap(ZCycle, ZClear)
        Cycle = 87;
        QStep = sqr(cld[6]^2+cld[7]^2);
!        DrillPause = cld[15]*1000;
!        if DrillPause=0 then
!          DrillPause@ = 0
      end else begin
        Cycle = 88;
      end
    end
    if KodCycle=212 then Cycle = 88   ! BORE8
    if KodCycle=213 then Cycle = 89   ! BORE9
    if KodCycle=153 then Cycle = 83   ! DEEP
    if KodCycle=288 then Cycle = 73   ! BRKCHP
    FEED_ = Fr
    OutBlock
  end else
    begin
      Cycle = 80;
      OutBlock;
    end
end
```

## Access from .NET

```csharp
public override void OnCycle(ICLDCycleCommand cmd, CLDArray cld)
```

Inheritance: `ICLDCycleCommand : ICLDCommand`. Read from the strongly-typed `cmd`, the raw `cld[i]` array (same indices as in sppx), or the named `cmd["..."]` helpers; the common `ICLDCommand` members are described in the [CLData access model](../../cldata.md).

Example:

```csharp
public override void OnCycle(ICLDCycleCommand cmd, CLDArray cld)
{
    // cld[1] - cycle type: 71 = ON, 72 = OFF, otherwise a specific cycle (DRILL 163, TAP 168, ...)
    if ((int)cld[1] == 72) {
        nc.G.Show(80);                 // cancel the canned cycle
        nc.Block.Out();
    } else if ((int)cld[1] != 71) {
        nc.G.Show((int)cld["ISO.G"]);  // ISO.G is the mapped G-code (G81..G89)
        nc.Z.Show(cld["H"]);           // hole bottom level
        nc.R.Show(cld["Top"]);         // retract level
        nc.F.Show(cld["F"]);           // feed
        nc.Block.Out();
    }
}
```

## See also
- [G81 drilling cycle `CYCLE DRILL(163)`](g81.md)
- [G82 drilling cycle `CYCLE FACE(81)`](g82.md)
- [G84 drilling cycle `CYCLE TAP(168)`](g84.md)
- [G85 drilling cycle `CYCLE BORE5(209)`](g85.md)
- [G86 drilling cycle `CYCLE BORE6(210)`](g86.md)
- [G87 drilling cycle `CYCLE BORE7(211)`](g87.md)
- [G88 drilling cycle `CYCLE BORE8(212)`](g88.md)
- [G89 drilling cycle `CYCLE BORE9(213)`](g89.md)
- [Deep drilling with chip removing `CYCLE DEEP(153)`](deep-chip-removing.md)
- [Deep drilling with chip breaking `CYCLE BRKCHP(288)`](deep-chip-breaking.md)
- [CLData access model](../../cldata.md)
