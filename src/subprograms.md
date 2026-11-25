# Subprograms

A subprogram is a named part of a script that can be called from other places. A *procedure*
performs actions; a *function* also returns a value and can be used in expressions.

## Declaration

A subprogram consists of a heading, optional declarations of local constants, types, variables
and labels, and a body between `begin` and `end`.

```pascal
function Square(x: float): float
begin
  result = x * x
end

procedure PrintLine(text: string; count: integer)
var
  i: integer
begin
  for i = 1 to count do
    print text
end
```

The type of the function result follows the parameter list after a colon. Inside a function, the
variable `result` holds the value to return; it can be assigned several times, the last value is
returned. A function is called in an expression: `area = Square(side)`.

A subprogram can be called only after its declaration. In a [module](program-structure.md#module)
the heading declared before `implementation` makes the subprogram available in the whole module.

## Parameters

Parameters are listed in parentheses: names, a colon and the type. Groups of parameters of
different types are separated with semicolons; parameters of one type can be listed with commas.

**Value parameter.** The subprogram gets a copy of the argument; changing the parameter does not
change the argument. The argument can be any expression of a compatible type.

**Variable parameter.** The word `var` before the parameter passes the variable itself: changes of
the parameter change the argument. The argument must be a variable.

```pascal
program Parameters

procedure Swap(var a, b: integer)
var
  t: integer
begin
  t = a
  a = b
  b = t
end

var
  i, j: integer
begin
  i = 1
  j = 2
  Swap(i, j)
  print i     // 2
  print j     // 1
end
```

A function can return several values through `var` parameters.

## Recursion

A subprogram can call itself:

```pascal
function Factorial(n: integer): integer
begin
  if n <= 1 then
    result = 1
  else
    result = n * Factorial(n - 1)
end
```

There is no `forward` declaration, so in a program two subprograms cannot call each other. Such
subprograms are put in a [module](program-structure.md#module), with their headings before
`implementation`.

## Overloading

Several subprograms can have the same name if their parameter lists differ. Each of them is marked
with the word `overload` after the heading. The compiler chooses the subprogram by the types of the
arguments.

```pascal
program Overloading

function Describe(x: integer): string overload
begin
  result = 'integer ' + tostring(x)
end

function Describe(x: string): string overload
begin
  result = 'string ' + x
end

begin
  print Describe(5)        // integer 5
  print Describe('five')   // string five
end
```

## Subprograms of other kinds

- Methods, constructors and destructors belong to [classes](classes.md).
- External routines are implemented in libraries; see
  [External routines and interface classes](external-routines.md).
- The routines built into the language, for example `sqrt` and `copy`, are described in
  [Built-in routines](built-in-routines.md).
