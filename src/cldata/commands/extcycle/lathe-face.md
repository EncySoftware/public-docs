# EXTCYCLE FACE - Lathe drilling cycle (G82)

Lathe drilling canned cycle `FACE(81)` G82 drills axial holes with static tool inside rotated workpiece. The tool approaches the hole at the safe plane level descends at rapid feedrate to the return level, machines the hole at work feedrate, dwells at the hole bottom, and rapidly retracts to the safe plane level.

## Parameters

| CLD array | CLD name | Description |
|---|---|---|
| CLD[1] | CLD.SubCmd | Command type: ON(71) – canned cycle on, CALL(52) – canned cycle call, OFF(72) – canned cycle off. |
| CLD[2] | CLD.SubType | Canned cycle type identifier: FACE(81). |
| CLD[3] | CLD.CLParams(1) | The top level of a hole (T). |
| CLD[4] | CLD.CLParams(2) | The hole depth measured relative to the top level (D). |
| CLD[5] | CLD.CLParams(3) | The return level (R). |
| CLD[6] | CLD.CLParams(4) | The Safe level (S). |
| CLD[7] | CLD.CLParams(5) | Dwell at hole bottom level (seconds). |
| CLD[8] | CLD.CLParams(6) | The federate units: 0 – mm/rev, 1 – mm/min. |
| CLD[9] | CLD.CLParams(7) | The Work feed. |
| CLD[10] | CLD.CLParams(8) | The Retract feed. |

## Access from .NET

This cycle has no dedicated family handler - it is delivered through the base `OnExtCycle` (dispatch on `cmd.CycleType` / `cld[2]`). See [Extended cycle (EXTCYCLE)](extcycle.md).

## See also
- [Extended cycle (EXTCYCLE)](extcycle.md)
- [CLData access model](../../cldata.md)
