# EXTCYCLE LATHETHREADG92(404) - Lathe threading single pass cycle (G92)

Lathe threading single pass cycle G92 `LATHETHREADG92(404)` (in different controls may be termed G92, G78, G21, etc.) generates a closed sequence of moves for a single pass threading. Illustration of execution is shown below. Before calling the cycle tool is located at the Start point. The cycle is called one frame of the NC program, which specifies the endpoint, thread pitch, taper and chamfer size, etc. As a result of this frame tool from the Start point will fall to the TSP point, make threading to the TEP point and come to the Start point. Because thread cutting is usually performed in several passes, the NC program often consists of multiple calls to the cycle with different values of the diameter of the thread:

```text
...
X60.0 Z20.0 M08
G01 Z10.0 F1.0 (Approach to the Start point)
G92 X29.4 Z-52.0 F2.0 (Cycle call)
X28.9 (Modal call G92 cycle with a different value of diameter)
X28.5 (Modal call G92 cycle with a different value of diameter)
X28.1 (Modal call G92 cycle with a different value of diameter)
X27.8 (Modal call G92 cycle with a different value of diameter)
X27.56 (Modal call G92 cycle with a different value of diameter)
X27.36 (Modal call G92 cycle with a different value of diameter)
X27.26 (Modal call G92 cycle with a different value of diameter)
G00 X200.0Z150.0M09 (Return of the tool)
...
```

## Parameters

| CLD array | CLD name | Description |
|---|---|---|
| CLD[1] | CLD.SubCmd | Command type: ON(71) – canned cycle on, CALL(52) – canned cycle call, OFF(72) – canned cycle off. |
| CLD[2] | CLD.SubType | Canned cycle type identifier: LATHETHREADG92(404). |
| CLD[4] | CLD.CLParams(2) | The thread orientation: 0 – outer diameter, 1 – inner diameter, 2 – face. |
| CLD[5] | CLD.CLParams(3) | The cone angle in degrees (for a taper thread) (A). |
| CLD[6] | CLD.CLParams(4) | The Z coordinate of the thread start point (SP.Z). |
| CLD[7] | CLD.CLParams(5) | The X coordinate of the thread start point (SP.X). |
| CLD[8] | CLD.CLParams(6) | The Z coordinate of the thread end point (EP.Z). |
| CLD[9] | CLD.CLParams(7) | The X coordinate of the thread end point (EP.X). |
| CLD[10] | CLD.CLParams(8) | The Z coordinate of the taper thread start point (TSP.Z). |
| CLD[11] | CLD.CLParams(9) | The X coordinate of the taper thread start point (TSP.X). |
| CLD[12] | CLD.CLParams(10) | The Z coordinate of the taper thread end point (TEP.Z). |
| CLD[13] | CLD.CLParams(11) | The X coordinate of the taper thread end point (TEP.X). |
| CLD[14] | CLD.CLParams(12) | The pulloff length at the thread termination (L). |
| CLD[21] | CLD.CLParams(19) | The number of the thread starts. |
| CLD[22] | CLD.CLParams(20) | The thread step definition mode: 0 – by distance, 1 – by number of the threads per unit. |
| CLD[23] | CLD.CLParams(21) | The thread step amount. |
| CLD[32] | CLD.CLParams(30) | The pulloff angle at the thread termination in degrees (CA). |
| CLD[33] | CLD.CLParams(31) | The spindle start angle in degrees (for multistart threads). |

## Access from .NET

In addition to the base `OnExtCycle`, this cycle is delivered through the turning-family handler `OnTurnExtCycle`:

```csharp
public override void OnTurnExtCycle(ICLDExtCycleCommand cmd, CLDArray cld)
```

See [Extended cycle (EXTCYCLE)](extcycle.md) for the common .NET model.

## See also
- [Extended cycle (EXTCYCLE)](extcycle.md)
- [CLData access model](../../cldata.md)
