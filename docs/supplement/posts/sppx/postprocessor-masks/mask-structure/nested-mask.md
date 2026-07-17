# Nested mask

Sometimes it is required to out the register value if the value of other register is changed. Then the nested mask is used. For example:

- Mask:

```
Z[CLD.Z, G[43]]
```

- NC code:

```
G43 Z0.123
```

The value of the register **Z** is changed and value 43 is assigned to the register **G**.

It is possible to use the modifiers, expressions, and other nested masks in the nested masks. The registers of the nested mask will be included in to the NC-program line in the order according to the registers list. For example:

- Mask:

```
X[CLD.X] Y[CLD.Y] Z[CLD.Z, G[43]]
```

- NC code:

```
G43 X6.141 Y-4.234 Z0.123
```

The changed register **G** is located in the start of line according to the registers list.

**See also**

[Mask structure](readme-mask-structure.md)
