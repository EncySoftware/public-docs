# Variables assignment from the mask

It is possible if necessary to assign any predefined variables or [COMMON](../../language-description/basic-definitions/technology-command-programs-comments.md) variables from the mask. Values can be assigned fro the number and string variables. The constants only can be assigned to the string variable. Any expression including functions and other variables can be assigned to the number variable.

The variable values can be assigned in any line of the mask. NC program line is not generated for this mask line. The `;` sign is the delimiter between the variables. For example:

- Mask:

```
INTERP=0;XP=XT;YP=YT-Y1+2;CLDATA$="text"
G_INTERP[INTERP] X[XT] Y[YT] Z[ZT] ([CLDATA$])
```

- NC code:

```
G0 X100.122 Y231.567 Z010.546 (text)
```

**See also**

[Mask structure](readme-mask-structure.md)
