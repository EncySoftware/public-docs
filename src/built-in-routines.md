# Built-in routines

The built-in routines are available in every script without `uses`. Arguments of type `float` also
accept `integer` values.

## Mathematics

Angles are in radians.

| Routine | Result |
|---|---|
| `abs(x)` | Absolute value of `x`; the result has the type of `x` |
| `sgn(x): integer` | `-1` if `x` is negative, `0` if it is zero, `1` if it is positive |
| `sqrt(x: float): float` | Square root |
| `pow(base, exponent: float): float` | `base` raised to the power `exponent`; the same as `base ^ exponent` |
| `exp(x: float): float` | e raised to the power `x` |
| `ln(x: float): float` | Natural logarithm |
| `log(x: float): float` | Logarithm to base 10: `log(1000)` gives `3` |
| `sin(x: float): float` | Sine |
| `cos(x: float): float` | Cosine |
| `tan(x: float): float` | Tangent |
| `ctan(x: float): float` | Cotangent |
| `asin(x: float): float` | Arcsine |
| `acos(x: float): float` | Arccosine |
| `atn(x: float): float` | Arctangent |
| `round(x: float): integer` | Nearest integer. A value exactly halfway between two integers is rounded to the even one: `round(2.5)` gives `2`, `round(3.5)` gives `4` |
| `trunc(x: float): integer` | Integer part, the fraction is discarded: `trunc(-2.7)` gives `-2` |
| `roundex(x, digit: float): float` | `x` rounded to a multiple of 10 to the power `digit`, halfway values to the even multiple: `roundex(3.14159, -2)` gives `3.14`, `roundex(1250, 2)` gives `1200` |

## Strings

Characters are numbered from 1.

| Routine | Result |
|---|---|
| `len(s): integer` | Number of characters in `s` |
| `copy(s: string; index, count: integer): string` | `count` characters of `s` starting from the character `index`; fewer if the string ends earlier: `copy('Hello', 2, 3)` gives `'ell'` |
| `pos(substr, s: string): integer` | Position of the first occurrence of `substr` in `s`, `0` if there is none: `pos('lo', 'Hello')` gives `4` |
| `upcase(s: string): string` | `s` with Latin letters converted to upper case |
| `locase(s: string): string` | `s` with Latin letters converted to lower case |
| `ord(s: string): integer` | Code of the first character of `s`; `-1` for an empty string |
| `trim(s: string): string` | `s` without leading and trailing spaces |
| `isnum(s: string): boolean` | `true` if the first character of `s` is a digit or one of `.`, `,`, `+`, `-` |
| `isalpha(s: string): boolean` | `true` if the first character of `s` is a letter |

## Conversions

| Routine | Result |
|---|---|
| `tostring(x): string` | `integer` or `float` value as a string: `tostring(3.5)` gives `'3.5'` |
| `tostring(format: string; x): string` | Number formatted by the format string, see below |
| `integer_num(s: string): integer` | Integer written in `s`: `integer_num('42')` gives `42` |
| `float_num(s: string): float` | Number written in `s` with a dot as the decimal separator: `float_num('2.5e1')` gives `25` |
| `float(x: integer): float` | `x` as a `float` value |

If the string passed to `integer_num` or `float_num` does not contain a number, a
[run-time error](runtime-errors.md) is reported and the result is `0`.

### Format string

The format string of `tostring` consists of these characters:

| Character | Meaning |
|---|---|
| `0` | A digit; if the number has no digit in this place, `0` is output |
| `#` | A digit; if the number has no digit in this place, nothing is output |
| `.` | The place of the decimal separator. The output always uses a dot |
| `,` | Separate the thousands of the integer part. The separator character follows the regional settings of Windows |
| `E+`, `E-` | Exponential form. `E+` outputs the sign of the exponent always, `E-` only for a negative exponent; the zeros after it set the minimum number of exponent digits |
| `'text'`, `"text"` | Text output as it is |
| `;` | Separates the formats for positive numbers, negative numbers and zero |

| Call | Result |
|---|---|
| `tostring('0.00', 3.14159)` | `3.14` |
| `tostring('0.###', 2.5)` | `2.5` |
| `tostring('000', 7)` | `007` |
| `tostring('#,##0.0', 1234567.891)` | `1,234,567.9` with the thousands separator of English regional settings |
| `tostring('0.00E+00', 12345.678)` | `1.23E+04` |

## Arrays

| Routine | Result |
|---|---|
| `len(a): integer` | Number of elements of the array `a` |
| `setlen(a, count: integer)` | Sets the number of elements of the dynamic array `a`; a procedure |

See [Arrays](data-types.md#arrays).

## Routines that do not work

The names `chr`, `posex` and `random` are reserved for built-in routines that do not work in the
current version: `chr` returns the character with the code 0 for almost every code, `posex` reports
a run-time error and returns `0`, and the compiler hangs on a script that calls `random`.

## Routines of the system module

Files, folders, dialogs and running other programs are described in [System module](system-module.md).
