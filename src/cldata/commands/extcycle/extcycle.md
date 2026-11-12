# EXTCYCLE - Extended cycle

## Command caption

How the command appears in the CLData command list:

```text
EXTCYCLE ON(71)|CALL(52)|OFF(72) DRILL(163)|FACE(81)|TAP(168)|DEEP(153)|W5DDrill(481)|
         W5DBore5(485)|LATHEROUGH(401)|LATHETHREAD(403)|... {, a} {, b} {, c} ...
```

Use the extended cycle command **EXTCYCLE** to process standard cycles. The following is the list of standard cycles supported by the **EXTCYCLE** command:

- [Lathe finish cycle G70, G73 - `LATHEFINISH(400)`](lathefinish.md)
- [Lathe roughing cycle G71, G72 - `LATHEROUGH(401)`](latherough.md)
- [Lathe grooving cycle G74,G75 - `LATHEGROOVE(402)`](lathegroove.md)
- [Lathe threading cycle G76 - `LATHETHREAD(403)`](lathethread.md)
- [Lathe threading single pass cycle G92 - `LATHETHREADG92(404)`](lathethread-g92.md)
- [Lathe drilling cycle G81 - `DRILL(163)`](lathe-drill.md)
- [Lathe drilling cycle G82 - `FACE(81)`](lathe-face.md)
- [Lathe tapping cycle G84 - `TAP(168)`](lathe-tap.md)
- [Lathe drilling with chip breaking cycle - `BRKCHP(288)`](lathe-brkchp.md)
- [Lathe drilling with chip removing cycle - `DEEP(153)`](lathe-deep.md)
- [Drilling cycle G81 - `W5DDrill(481)`](w5ddrill.md)
- [Drilling cycle G82 - `W5DFace(482)`](w5dface.md)
- [Drilling with chip removing cycle G83 - `W5DChipRemoving(483)`](w5dchipremoving.md)
- [Drilling with chip breaking cycle G73 - `W5DChipBreaking(473)`](w5dchipbreaking.md)
- [Tapping cycle G84 - `W5DTap(484)`](w5dtap.md)
- [Drilling cycle G85 - `W5DBore5(485)`](w5dbore5.md)
- [Drilling cycle G86 - `W5DBore6(486)`](w5dbore6.md)
- [Drilling cycle G87 - `W5DBore7(487)`](w5dbore7.md)
- [Drilling cycle G88 - `W5DBore8(488)`](w5dbore8.md)
- [Drilling cycle G89 - `W5DBore9(489)`](w5dbore9.md)
- [Thread milling cycle - `W5DThreadMill(490)`](w5dthreadmill.md)
- [Hole pocketing cycle - `W5DHolePocketing(491)`](w5dholepocketing.md)
- [Probing cycle - `WProbing(500)`](wprobing/wprobing.md)

## Access from sppx

Handler: `program ExtCycle`

The `cld` array is read by index or by name - in sppx by the typed short name (e.g. `cld.X`), in .NET by the same name as a string key (e.g. `cld["X"]`).

| Parameter | CLD array | CLD name | Description |
|---|---|---|---|
| ON(71)<br>CALL(52)<br>OFF(72) | CLD[1] | CLD.SubCmd | Command modifier: ON(71) – turn standard cycle ON, CALL(52) – call standard cycle, OFF(72) – turn standard cycle OFF. |
| LATHEFINISH(400)<br>LATHEROUGH(401)<br>LATHEGROOVE(402)<br>LATHETHREAD(403)<br>DRILL(163)<br>FACE(81)<br>TAP(168)<br>BRKCHP(288)<br>DEEP(153)<br>W5DDrill(481)<br>W5DFace(482)<br>W5DChipRemoving(483)<br>W5DChipBreaking(473)<br>W5DTap(484)<br>W5DBore5(485)<br>W5DBore6(486)<br>W5DBore7(487)<br>W5DBore8(488)<br>W5DBore9(489)<br>W5DThreadMill(490)<br>W5DHolePocketing(491)<br>WProbing(500) | CLD[2] | CLD.SubType | Cycle type identifier. |
| a, b, c, d … | CLD[3] – CLD[258] | CLD.CLParams(1) – CLD.CLParams(256) | Cycle parameters list. |

The first parameter is used to specify the start, call and cancellation of the standard cycle.

CAM system usually generates technology command sequence containing **EXTCYCLE** command similar to the following:

```text
EXTCYCLE ON(71) ...
FEDRAT ...
GOTO ...
GOTO ...
EXTCYCLE CALL(52) ...
FEDRAT ...
GOTO ...
GOTO ...
EXTCYCLE CALL(52) ...
FEDRAT ...
GOTO ...
GOTO ...
EXTCYCLE CALL(52) ...
EXTCYCLE OFF(72) ...
```

The list of parameters depends on the cycle type.

Example (from the Fanuc (30i)_Mill postprocessor):

```pascal
program ExtCycle
  if cld[1] = 71 then CycleOn = 1                    ! cycle On
  else if cld[1] = 72 then begin                     ! cycle Off
    if (CLD.SubType >= 473) and (CLD.SubType <= 489) then Cycle = 80
    OutBlock
  end else if cld[1] = 52 then begin                 ! cycle Call
    if cld[10] > 0 then
      if cld[9] = 0 then Fr = cld[10]*S else Fr = cld[10]   ! feed units / value
  end
```

## Access from .NET

Besides the base `OnExtCycle`, the command is dispatched (by cycle family) to one of the specialized
handlers below:

```csharp
public override void OnExtCycle(ICLDExtCycleCommand cmd, CLDArray cld)        // base
public override void OnHoleExtCycle(ICLDExtCycleCommand cmd, CLDArray cld)    // hole cycles
// also, by cycle family: OnTurnExtCycle, OnProbeExtCycle, OnWeldingExtCycle, OnPickAndPlaceExtCycle
```

Inheritance: `ICLDExtCycleCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd[...]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../../cldata.md). The raw **`cld[i]` array is available with the same indices as in sppx**, and the parameters are
also reachable **by numerical code** through `cmd.Prm`.

| Member | Type | Description |
|---|---|---|
| `cmd.IsOn`<br>`cmd.IsOff`<br>`cmd.IsCall` | bool | True if it is a cycle switch-ON / switch-OFF / CALL command. |
| `cmd.CycleType` | int | Numerical code of the cycle type (simple drilling, deep drilling, tapping, OD turning, ...). See the constants in the `CLDCycle` class. |
| `cmd.Prm` | `ICodeParametersOfCLDCommand` | The parameter list; get a value by its numerical code. |

`cmd.Prm` gives `ParamCount`, `Code(i)`, `ParamType(i)`, `IndexOfCode(code)`, and value indexers
`Prm.Flt[code]` / `Prm.Int[code]` / `Prm.Bol[code]` / `Prm.Str[code]`.

Example (from the Sinumerik 840D mill postprocessor - note the `cld[i]` access):

```csharp
public override void OnHoleExtCycle(ICLDExtCycleCommand cmd, CLDArray cld)
{
    if (cmd.IsOn)
    {
        nc.GFeed.v = cld[9] == 1 ? 94 : 95;   // work-feed units (same cld index as sppx)
        nc.Feed.v = cld[10];                  // work-feed value
        nc.Block.Out();
    }
    else if (cmd.IsOff)
        nc.G.Show(80);                        // cancel the cycle
    // else if (cmd.IsCall) dispatch by cmd.CycleType ...
}
```

## See also
- [CLData access model](../../cldata.md)
