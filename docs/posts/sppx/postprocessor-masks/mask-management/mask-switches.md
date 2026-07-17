# Mask switches

Any mask is linked with the three switches:

1. **Out previous**. If the switch is checked then the NC-line is formed before the mask analyzing. All registers in which the old and current values are not equal will be out to the line.
2. **Poll all registers**. If the switch is checked then all registers in which the old and current values are not equal will be included in to the line in addition to the registers of the mask. If such registers is present (it is possible if the **Off** modifier was used in the previous mask) then this register will be located in the line according to the order in list of registers. For example:

- Registers list:

```
G_INTERP, G_PLANE, X, Y, Z
```

- [Plane](../../../cldata/commands/plane.md) mask:

```
G_PLANE[ARCPLANE,Off]
```

- [AbsMov](../../../cldata/commands/goto.md) mask:

```
G_INTERP[1] X[CLD.X] Y[CLD.Y] Z[CLD.Z]
```

- CLData commands:

```
PLANE XY(33)
GOTO.abs X100 Y100 Z100
```

- NC code:

```
G1 G17 X100.000 Y100.000 Z100.000
```

3. **Out block**. If the switch is not checked then all registers written in the mask will be modified but the NC-program line is not out.

**See also**

[Postprocessor masks](../readme-postprocessor-masks.md)
