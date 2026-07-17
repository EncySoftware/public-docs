# CYCLE DEEP(153) - Deep drilling with chip removing

> **Kept for compatibility.** **CYCLE** is retained only for compatibility with older postprocessors. Current versions of the CAM system generate the [extended cycle command **EXTCYCLE**](../extcycle/extcycle.md) instead: it offers more capabilities and lets the CAM system fully simulate all of the cycle's nested motions, which **CYCLE** does not. Output of **CYCLE** can still be turned on in the CAM system settings, but this is not recommended.

Deep drilling with chip removing cycle performs rapid approach to the safe level and repeated drilling according to specified cut-in depth value **ZI** and withdrawal **Zi** values.

![Img5_4_31_3](../../../sppx/images/download/attachments/142669100/Img5_4_31_3.gif)

Cycle includes:

- Rapid travel to the **Z safe** level.
- Work feedrate travel to the **Zl**.
- Rapid retract to the **Z safe** level.
- Rapid travel to the **Zl** - **Zi** level.
- Work feedrate travel to the **Zl** + **Zi** level.
- Rapid retract to the **Z safe** level.
- Rapid travel to the 2***Zl** - **Zi** level.
- Work feedrate travel to the **Zl** + **Zi** level.
- Rapid retract to the **Z safe** level.
- Repeat until the hole depth level is reached.
- Rapid retract to the **Safe plane** level.

**Command**

```text
CYCLE DEEP(153), A a, MMPM(315), N nm, F f, L l, I i, P p, T t
```

or

```text
CYCLE DEEP(153), A a, MMPR(316), M nm, F f, L l, I i, P p, T t
```

## Parameters

| Parameter | CLD array | CLD name | Description |
|---|---|---|---|
| DEEP(153) | CLD[1] | CLD.Type | Cycle type 153 (DEEP). |
| a | CLD[2] | CLD.A | Hole depth in current measure units (mm or inches). |
| MMPM(315)<br>MMPR(316) | CLD[3] | CLD.MMPM | Feedrate measure units: 315 (MMPM) – mm per minute (inches per minute), 316 (MMPR) – mm per revolution (inches per revolution). |
| nm | CLD[4] | CLD.NM | Work feedrate value. |
| f | CLD[5] | CLD.F | Safe level. |
| L | CLD[6] | CLD.L | Cut in value Zl |
| i | CLD[7] | CLD.I | Withdrawal value Zi |
| p | CLD[8] | CLD.P | Safe plane level. |
|  | CLD[9]<br>CLD[10] |  | Reserved. |
| t | CLD[11] | CLD.Top | Hole top level. |

## Access from .NET

Delivered through the `OnCycle` handler (dispatch on the cycle type in `cmd`/`cld[1]`):

```csharp
public override void OnCycle(ICLDCycleCommand cmd, CLDArray cld)
```

See [Hole machining cycles (CYCLE)](cycle.md) for the common .NET model.

## See also
- [Hole machining cycles (CYCLE)](cycle.md)
- [CLData access model](../../cldata.md)
