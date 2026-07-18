# EXTCYCLE W5DTap - Tapping cycle (G84)

Tapping cycle `W5DTap(484)` (G84) performs rapid approach to the **Z return** level, thread tapping with subsequent retraction at work feedrate with reverse spindle rotation.

![G84](../../../sppx/src/images/download/attachments/142669177/G84.PNG)

G84 tapping cycle includes:

- Rapid approach to the hole center at the **Z return** level.
- Rapid travel to the **Z safe level**.
- Work feedrate motion the **Z min** level.
- Spindle reverse rotation and work feedrate trave to **Z safe** level.
- Rapid retract to the **Z return** level.
- Restore spindle rotation direction and speed.

If the appropriate setting is enabled, then tap retracts to break / remove chip during the cycle execution. Way to break chips is determined by CLD [20] parameter.

CNC-systems often have different tapping canned cycles for fixed and floating socket types. Socket type is specified by the `CLD[19]` (CLD.CLParams(17)) parameter.

## Parameters

| CLD array | CLD name | Description |
|---|---|---|
| CLD[1] | CLD.SubCmd | Command type: ON(71) – canned cycle on, CALL(52) – canned cycle call, OFF(72) – canned cycle off. |
| CLD[2] | CLD.SubType | Canned cycle type identifier: W5DTap(484). |
| CLD[3] | CLD.CLParams(1) | Nx, X coordinate of the tool normal vector |
| CLD[4] | CLD.CLParams(2) | Ny, Y coordinate of the tool normal vector |
| CLD[5] | CLD.CLParams(3) | Nz, Z coordinate of the tool normal vector |
| CLD[6] | CLD.CLParams(4) | Sf, Normal distance from current tool position to the safe plane level |
| CLD[7] | CLD.CLParams(5) | Tp, Normal distance from current tool position to the hole top level |
| CLD[8] | CLD.CLParams(6) | Bt, Normal distance from current tool position to the hole bottom level |
| CLD[9] | CLD.CLParams(7) | Work feed measurements: 0 – mm/rev, 1 – mm/min |
| CLD[10] | CLD.CLParams(8) | Work feed value |
| CLD[11] | CLD.CLParams(9) | Approach feed measurements: 0 – mm/rev, 1 – mm/min |
| CLD[12] | CLD.CLParams(10) | Approach feed value |
| CLD[13] | CLD.CLParams(11) | Return feed measurements: 0 – mm/rev, 1 – mm/min |
| CLD[14] | CLD.CLParams(12) | Return feed value |
| CLD[15] | CLD.CLParams(13) | Delay at the bottom level in seconds |
| CLD[16] | CLD.CLParams(14) | Delay at the top level in seconds |
| CLD[17] | CLD.CLParams(15) | Thread step |
| CLD[18] | CLD.CLParams(16) | Initial spindle angle in degrees (for multistart threads) |
| CLD[19] | CLD.CLParams(17) | Tap socket type: 0 – floating (compensative), 1 – fixed (uncompensative) |
| CLD[20] | CLD.CLParams(18) | The way to break chip: 0 – without chip breaking, 1 – chip removing, 2 – chip breaking |
| CLD[21] | CLD.CLParams(19) | St, chip breaking step value |
| CLD[22] | CLD.CLParams(20) | Dg, each iteration chip breaking step degression |
| CLD[23] | CLD.CLParams(21) | Dc, before drilling deceleration value for each step |
| CLD[24] | CLD.CLParams(22) | Ld, each step lead out value for cutting process breaking |
| CLD[50] | CLD.CLParams(48) | What spindle is used to machining: 1 - driven tool, 2 - workpiece spindle (lathe). |

![W5DSchema](../../../sppx/src/images/download/attachments/142669177/W5DSchema.png)

## Access from .NET

In addition to the base `OnExtCycle`, this cycle is delivered through the hole-family handler `OnHoleExtCycle`:

```csharp
public override void OnHoleExtCycle(ICLDExtCycleCommand cmd, CLDArray cld)
```

See [Extended cycle (EXTCYCLE)](extcycle.md) for the common .NET model.

## See also
- [Extended cycle (EXTCYCLE)](extcycle.md)
- [CLData access model](../../cldata.md)
