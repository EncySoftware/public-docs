# Registers in the masks

Registers are used to define the format of the number output according to the requirements of the NC systems. The register in the postprocessor unites the next properties:

- Identifier of the register;
- Current value of the register;
- Previous value;
- Value output format;
- The name of the register.

See section [The block structure and format definition](../../common-organization-of-the-work/main-window/block-structure-and-format-definition-register-list-forming.md) for more details.

If write the register name or register identifier before the open square bracket then the number output format of this register will be used for the value output. For example:

- Mask:

```
G_INTERP[1] X[XT] Y[YT] Z[ZT] F[200]
```

- NC code:

```
G1 X100.100 Y-245.100 Z-010.560 F200
```

While the mask analysis it is presumed that the word before the open square bracket defines the register. Executable system looks for the register by name, if the register is not found then the system looks by identifier. The registers are looked in order how it has defined in the registers list. So if the list has some registers with the same identifier name then the first will be used.

If register is not found then value is output by default number format and the word that is in mask before the open square bracket is output before the number. For example:

- Mask:

```
G_INTERP[1] X[XT] YYY[YT] Z[ZT] F[200]
```

- NC code:

```
G1 X100.100 YYY-245.100034 Z-010.560 F200
```

In the sample the word **YYY** is absent in the registers list.

If the register is found then the current register value is assigned to the old register value and the new value is assigned to the current register value. After that, the executable system compares the old and the current values and if they are not equal then the register identifier and value is output to the NC-program line accordingly to the defined number format.

Example. Lets the current register **F** value is equal to 200:

- Mask:

```
G_INTERP[1] X[XT] Y[YT] Z[ZT] F[200]
```

- NC code:

```
G1 X100.100 Y-245.100 Z-010.560
```

The old and new value of the register is equal, so the register **F** value is not output to the NC code.

**See also**

[Mask structure](readme-mask-structure.md)
