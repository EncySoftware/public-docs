# Postprocessor masks

Use masks to specify the NC-block templates for the given CLData command.

Each CLData command has its own mask. Masks use a special language that makes them similar to NC-program blocks.

For example suppose the CLData is:

```
GOTO.abs X 19.599, Y -73.200, Z 28.030
```

suppose we need to form the following NC-code to process the command:

```
G1 X19.599 Y-73.200 Z28.030 F200
```

The mask that forms the desired NC-code is:

```
G[1] X[XT] Y[YT] Z[ZT] F[FT]
```

where:

- **XT**, **YT**, **ZT** – current coordinates of the cutter;
- `1` – interpolation mode (positioning G0, linear G1 or arc G2, G3 (this can be different for non G-Code NC));
- **FT** – feedrate value.

Use variables and register values, the built-in [GMA](../../../cldata/functions/gma.md) array, built-in functions and expressions that result in numerical values in the masks. Also you can use special words ([switches](mask-management/mask-switches.md) and [modifiers](mask-structure/modifiers.md)) that control the output of the code into the NC-program.

**See also**

[Mask structure](mask-structure/readme-mask-structure.md)

[Mask switches](mask-management/mask-switches.md)

[Mask modifiers](mask-structure/modifiers.md)

[The transformation of a mask to the subprogram](mask-management/transformation-of-a-mask-to-the-subprogram.md)

[The interactive to create the masks](mask-management/interactive-to-create-the-masks.md)
