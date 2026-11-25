# Data types

Every constant, variable, parameter and function result has a type. The type defines the values it
can hold and the operations allowed on it.

## Simple types

| Type | Values | Literals |
|---|---|---|
| `integer` | Whole numbers from -2147483648 to 2147483647 | `42`, `-7`, `$FF` (hexadecimal) |
| `float` | Real numbers, about 15 significant digits | `3.14`, `1.5e3`, `1E-6` |
| `boolean` | `true` and `false` | `true`, `false` |
| `string` | Text of any length | `'Hello'`, `''` (empty string) |
| `pointer` | Address of data outside the script | `nil` |

An `integer` result that does not fit into the range wraps around without an error message:
`2147483647 + 1` gives `-2147483648`.

A `float` division by zero gives infinity, an operation without a result gives "not a number";
`print` shows them as `INF` and `NAN`. Integer division by zero is a [run-time error](runtime-errors.md).

A string literal is written in single quotes on one line. It cannot contain the single quote
character itself. The characters of a string are numbered from 1; a part of a string is taken with
`copy`. Strings are compared character by character, upper and lower case letters are different:
`'abc' = 'ABC'` is `false`.

The type `olebstr` is used only in [external routines](external-routines.md): it passes a string
to a library in the OLE Automation `BSTR` format.

## Arrays

An array keeps several values of one type, the *elements*. An element is selected by its index in
square brackets. Indexes start from 0.

**Static array.** The number of elements is given in the declaration with an integer literal or an
integer constant:

```pascal
program StaticArray
const
  N = 3
var
  a: array N of integer
  i: integer
begin
  for i = 0 to N - 1 do
    a[i] = (i + 1) * 10
  print a[0] + a[2]     // 40
  print len(a)          // 3
end
```

**Dynamic array.** The declaration has no size; the size is set with `setlen` and can be changed
later. The elements kept in the array remain; new elements get the initial value of their type.

```pascal
program DynamicArray
var
  names: array of string
  i: integer
begin
  setlen(names, 2)
  names[0] = 'first'
  names[1] = 'second'
  setlen(names, 3)
  names[2] = 'third'
  for i = 0 to len(names) - 1 do
    print names[i]
end
```

An element of an array can be an array. Each index is written in its own brackets:

```pascal
var
  m: array 3 of array 3 of float
begin
  m[1][2] = 7
```

Assigning one array to another copies the elements: changing the copy does not change the original.

The virtual machine does not report an index outside an array. Keep indexes within the range
from 0 to `len(a) - 1`.

## Records

A record joins values of different types, the *fields*, into one value. Each field is declared on
its own line. A field is selected with a dot: `p.x`.

```pascal
program Records
type
  TPoint = record
    x: float
    y: float
  end
  TSegment = record
    start: TPoint
    finish: TPoint
    name: string
  end
var
  p, q: TPoint
  s: TSegment
begin
  p.x = 1
  p.y = 2
  q = p           // q is a copy of p
  q.x = 5
  print p.x       // 1
  s.start = p
  s.finish.x = 10
  s.name = 'segment'
  print s.finish.x  // 10
end
```

Assigning a record copies all its fields.

## Type declarations

A `type` section gives names to types. A named type is declared once and used in many
declarations.

```pascal
type
  TLength = float
  TVector = array 3 of float
  TPoint = record
    x: float
    y: float
  end
  TPoints = array of TPoint
```

[Classes](classes.md) are declared in the `type` section as well.

## Type conversions

- An `integer` value can be used where a `float` value is expected: `f = 7` stores `7.0`.
- A `float` value is converted to `integer` only explicitly, with `round` or `trunc`. Assigning a
  `float` value to an `integer` variable is a compile error.
- `float(i)` converts an integer expression to `float`.
- Numbers are converted to strings with `tostring`, strings to numbers with `integer_num` and
  `float_num`. A number cannot be added to a string directly: `'n = ' + 5` is a compile error,
  `'n = ' + tostring(5)` is correct.

See [Built-in routines](built-in-routines.md).
