# Mask element

Any mask element is output to the NC-program line in the form as it looks in the mask. For example:

- Mask:

```
G0 rapid movement
```

- NC code:

```
G0 rapid movement
```

If the mask element is in a brackets "[" and "]" then it is replaced by value or variable that located in the brackets. For example:

- Mask:

```
[XT] [200]
```

- NC code:

```
100.12456 200
```

In the sample, the value of the **XT** variable is equal to 100.12456.

In the brackets, it is possible to use:

- All variables of the [COMMON](../../language-description/basic-definitions/technology-command-programs-comments.md) subprogram.
- Predefined (reserved) variables: [XT](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [YT](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [ZT](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [XC](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [YC](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [ZC](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [INTERP](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [TOOLRAD](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [CLDATA$](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [ARCPLANE](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [XP](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [YP](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [ZP](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [FEED](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [TLCOMP](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [TRCOMP](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [FROMX](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [FROMY](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [FROMZ](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [CURCODE](../../../cldata/functions/browsing.md), [NCNAME$](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [NCPATH$](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [BLOCKSTEP](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md).
- Predefined (reserved) functions: [FLAGIN](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [CROSS](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [NEXTTOOLNUM](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [CURDATE](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [CURTIME](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md).
- All parameters of the current technological command passed by the [CLD](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md) array.

Numbers have the different representation in the NC-program. The number out method is defined by the next parameters:

- **Decimal point** – this field can have following values:
  - **Is absent**,
  - **Is present if the number has the fractional part**,
  - **Is present anyway**;

- **Integer width** – the maximal digits number to represent the integer part of the number;
- **fractional width** – the digits number to represent the fractional part of the number;
- **Leading zeroes** and **Non-significant zeroes** – defines the zeroes output mode before and after the number;
- **Sign** – defines the output mode for the sign of the number. Following options are available:
  - **No**,
  - **"-" only**,
  - **"+" only**,
  - **"+" and "-" always**.

When the value is output to the NC-program block, the default number format is used:

- **Leading zeroes** and **Non-significant zeroes** – is absent;
- **Decimal point** – is present if the number has the fractional part;
- **Sign** – is present if the number is negative;
- **Integer width** and **Fractional width** – allows to out number without rounding
- Element identifier is output as text.

**See also**

[Mask structure](readme-mask-structure.md)
