# Expressions

It is possible to write the expressions to the masks. The expression is the mathematical formula. The result of expression is a number.

Syntactically, the math expression is the combination of the numbers, numerical variables and numerical functions, separated by the signs of the math operations and the parentheses. The simplest examples of math expressions are the number and the numerical variable

Following math operations are allowed in the language:

- `+` – the addition;
- `-` – the subtraction;
- `*` – the multiplication;
- `/` – the division;
- `^` – the exponentiation.

It is necessary to remember, that two operational sign can't follow one-after-another.

Following math functions are allowed:

- `SIN(x)` – sine of angle x (in degrees);
- `COS(x)` – cosine of angle x (in degrees);
- `TAN(x)` – tangent of angle x (in degrees);
- `ATN(x)` – arctangent of angle x (in degrees);
- `ASIN(x)` – arcsine of angle x (in degrees);
- `ACOS(x)` – arccosine of angle x (in degrees);
- `SQR(x)` – square root of x;
- `ABS(x)` – absolute value of x;
- `SGN(x)` – sign for x;
- `ROUND(x, y)` – rounding of x to y decimals after point;
- `LOG(x)` – decimal logarithm of x;
- `LN(x)` – natural logarithm of x.

Predefined variables and functions, all parameters of current CLDATA command transmitted via the [CLD](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md) array are available in the expression. For example:

- Mask:

```
X[2+5/2+2*(sin(45))] Y[CLD.Y*2] F[FEED]
```

- NC code:

```
X005914 Y001234 F200
```

In this sample the expression of the first element: 2+5/2+2*(sin(45)) is equal to 5.91421356237697. When out to the NC code, the **X** register was found in the registers list and the number output format was taken from the register. The expression of the second element has the parameter transmitted via the [CLD](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md) array – `CLD.Y` (equal 0.617) multiplied on 2. The third element uses the predefined variable [FEED](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md). This variable contains the current feedrate value.

**See also**

[Mask structure](readme-mask-structure.md)
