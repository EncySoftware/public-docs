# Modifiers

Sometimes, it is required to output the new register value independently if it is changed or not, and conversely to change the register value and do not output it to the current line. The modifiers **On** and **Off** are intended to do it.

The modifier is written in the square brackets after the value and comma.

Modifier **On**. If the modifier is written then the register value is output to the NC code in any case.

For example, lets the current register `G_PLANE` value is equal to 17:

- Mask:

```
G_PLANE[17, On] X[XT] Y[YT]
```

- NC code:

```
G17 X100.123 Y200.456
```

It is possible to out current value of register without the new value assign. To do it it is necessary to write **On** without value. For example:

- Mask:

```
G_PLANE[On] X[CLD.X] Y[CLD.Y]
```

- NC code:

```
G17 X100.123 Y200.456
```

Modifier **Off**. If the modifier is written then the new value is assigned to the register but the register is not output to the NC code. For example:

- Mask:

```
G49G80M5M9 G_PLANE[17,Off]
```

- NC code:

```
G49G80M5M9
```

It is possible to use modifier **Off** without value. It is needed to exclude the out of the current register value to the NC code without the assigning of a new value.

**See also**

[Mask structure](readme-mask-structure.md)
