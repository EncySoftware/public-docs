# Expressions

An expression computes a value from constants, variables, function calls and operators:
`(a + b) * 2`, `len(name) > 0`, `'Total: ' + tostring(sum)`.

## Operators

| Operator | Operation | Operands | Result |
|---|---|---|---|
| `+` | Addition | `integer`, `float` | `integer` if both are `integer`, otherwise `float` |
| `+` | Joining strings | `string` | `string` |
| `-` | Subtraction, change of sign | `integer`, `float` | as for `+` |
| `*` | Multiplication | `integer`, `float` | as for `+` |
| `/` | Division | `integer`, `float` | always `float`: `7 / 2` gives `3.5` |
| `div` | Integer division, the fraction is discarded | `integer` | `integer`: `7 div 2` gives `3`, `-7 div 2` gives `-3` |
| `mod` | Remainder of integer division, with the sign of the dividend | `integer` | `integer`: `7 mod 2` gives `1`, `-7 mod 2` gives `-1` |
| `^` | Raising to a power | `integer`, `float` | `float`: `2 ^ 10` gives `1024` |
| `=`, `<>` | Equal, not equal | numbers, strings, booleans, objects | `boolean` |
| `<`, `>`, `<=`, `>=` | Comparison | numbers, strings | `boolean` |
| `not` | Logical NOT | `boolean` | `boolean` |
| `and` | Logical AND | `boolean` | `boolean` |
| `or` | Logical OR | `boolean` | `boolean` |

The sign `=` means comparison inside an expression and [assignment](statements.md#assignment) at
the beginning of a statement.

## Priority

Operators of a higher priority are applied first. Operators of the same priority are applied from
left to right. Parentheses change the order.

| Priority | Operators |
|---|---|
| 1 (highest) | `^` |
| 2 | `not`, unary `-` and `+` |
| 3 | `*`, `/`, `div`, `mod`, `and` |
| 4 | `+`, `-`, `or` |
| 5 (lowest) | `=`, `<>`, `<`, `>`, `<=`, `>=` |

`1 + 2 * 3` gives `7`, `(1 + 2) * 3` gives `9`. `-2 ^ 2` gives `-4`: the power is computed before
the change of sign; `(-2) ^ 2` gives `4`.

In the current version `^` cannot be chained and its exponent cannot start with a minus: write
`(2 ^ 3) ^ 2` and `2 ^ (-1)`.

Comparisons have the lowest priority, so conditions joined with `and` and `or` must be put in
parentheses:

```pascal
if (x > 0) and (y > 0) then
  print 'first quadrant'
```

Without parentheses `x > 0 and y > 0` means `x > (0 and y) > 0`, and the compiler reports
incompatible types.

Both operands of `and` and `or` are always evaluated. In `(p <> nil) and (p.age > 0)` the second
comparison is evaluated even when `p` holds `nil`; check such conditions with nested `if`.

## Operator for a record type

A script can define the unary minus for its own record type with `operator`; other operators cannot
be defined. The definition looks like a function with one parameter; the result is returned in
`result`.

```pascal
program Negation
type
  TVector = record
    x: float
    y: float
  end

operator -(v: TVector): TVector
begin
  result.x = -v.x
  result.y = -v.y
end

var
  a, b: TVector
begin
  a.x = 1
  a.y = 2
  b = -a
  print b.y      // -2
end
```
