# Constants and variables

## Constants

A `const` section gives names to values that do not change. The value of a constant is a number or
a string; an expression is not allowed.

```pascal
const
  Count = 10
  Tolerance = 0.01
  Title = 'Report'
```

The type of a constant is defined by its value: `Count` is an `integer`, `Tolerance` is a `float`,
`Title` is a `string`. An integer constant can set the size of a [static array](data-types.md#arrays).

Write the value without a sign: in the current version a minus before the value of a constant is
lost, `Offset = -5` gives `5`. Use the minus where the constant is used: `x = -Offset`.

## Variables

A `var` section declares variables: a name, a colon and a type. Several variables of one type are
listed with commas.

```pascal
var
  i, j: integer
  length: float
  name: string
  points: array of TPoint
```

The value of a variable is changed by [assignment](statements.md#assignment):

```pascal
i = 10
name = 'Contour ' + tostring(i)
```

## Initial values

Before the first assignment a variable holds the initial value of its type:

| Type | Initial value |
|---|---|
| `integer`, `float` | `0` |
| `boolean` | `false` |
| `string` | empty string |
| dynamic array | no elements |
| record, static array | the initial values of the fields and elements |
| class | `nil` |

Local variables of a subprogram get these values again at every call.

## Scope

Where a name can be used depends on where it is declared:

- **Program or library.** Constants, types and variables declared before the subprograms and
  `begin` are available in the subprograms declared after them and in the main block.
- **Module.** Declarations before `implementation` are available in the module and in the scripts
  that use it. Declarations after `implementation` are available only in the module.
- **Subprogram.** Parameters and variables declared in a subprogram exist only while it runs and
  are visible only in it.

A name must be declared before it is used. A name cannot be declared twice in one scope.
