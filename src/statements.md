# Statements

Statements are executed one after another, in the order they are written. A statement usually
takes one line; several statements on one line are separated with semicolons.

## Assignment

An assignment stores the value of an expression in a variable, a field or an array element. The
sign of assignment is `=`.

```pascal
x = 10
p.x = p.x + 1
names[i] = 'item ' + tostring(i)
```

The type of the expression must be compatible with the type of the variable: an `integer` value can
be assigned to a `float` variable, but not the other way round (see
[Type conversions](data-types.md#type-conversions)).

## Compound statement

`begin` and `end` join several statements into one. A compound statement is used where the syntax
allows one statement, for example after `then`, `else` or `do`.

```pascal
if count > 0 then begin
  average = total / count
  print average
end
```

## if

`if` executes a statement when a condition of type `boolean` is `true`. The optional `else` branch
is executed when the condition is `false`.

```pascal
if k > 5 then
  print 'large'
else
  print 'small'
```

## case

`case` chooses a branch by the value of an integer expression. A branch is labelled with integer
constants separated with commas or with a range `first..last`. The `else` branch is executed when no
label matches. The statement ends with `end`.

```pascal
case k of
  0: print 'zero'
  1, 2, 3: print 'small'
  4..9: print 'medium'
  else print 'large'
end
```

In the current version the compiler accepts a string expression as the selector, but at run time the
error `incompatible types` is reported and the `else` branch is executed.

## while

`while` repeats a statement while a condition is `true`. The condition is checked before each
repetition, so the statement may be skipped completely.

```pascal
i = 1
while i <= 3 do begin
  print i
  i = i + 1
end
```

## repeat

`repeat` executes the statements up to `until` and repeats them until the condition becomes `true`.
The statements are executed at least once. Several statements between `repeat` and `until` do not
need `begin` and `end`.

```pascal
repeat
  i = i - 1
  print i
until i <= 0
```

## for

`for` repeats a statement for each value of an integer variable from the initial value to the final
value inclusive, increasing the variable by 1.

```pascal
for i = 1 to 3 do
  print i * 10
```

The variable must be of type `integer`. If the initial value is greater than the final value, the
statement is not executed. After the loop has finished, the variable is one more than the final
value.

## break and continue

`break` leaves the innermost loop. `continue` skips the rest of the current repetition and goes on
with the next one.

```pascal
i = 0
while i < 10 do begin
  i = i + 1
  if i = 2 then continue   // 2 is not printed
  if i > 4 then break      // the loop stops at 5
  print i
end
```

## goto

`goto` passes control to a statement marked with a label. Labels are identifiers declared in a
`label` section of the program or of the subprogram. A label is placed before a statement and
followed by a colon.

```pascal
procedure Check(x: integer)
label
  Done
begin
  if x < 0 then goto Done
  print 'positive'
Done:
end
```

There is no statement that leaves a subprogram before its end. A label before the final `end`, as in
the example above, does this.

## with

`with` makes the fields of an object available without its name. Here `point` is an object of a
[class](classes.md) with the fields `x` and `name`:

```pascal
with point do begin
  x = 5
  name = 'origin'
end
```

The same is written without `with` as `point.x = 5` and `point.name = 'origin'`. `with` can also be
used to read the fields of a record, but assignments to record fields made inside `with` are not
kept: assign them with the full name.

## print

`print` outputs the value of one expression of type `integer`, `float`, `boolean` or `string`.
A `float` value is printed with a dot as the decimal separator and without trailing zeros.

```pascal
print 'Hello'      // Hello
print 7 / 2        // 3.5
print 2.0          // 2
print 3 > 2        // true
```

To output several values, join them into one string: `print 'x = ' + tostring(x)`. Where the output
appears depends on how the script is run; see [Development environment](development-environment.md).

## Subprogram call

A procedure is called by its name and the arguments in parentheses. A procedure without parameters
is called by its name alone or with empty parentheses.

```pascal
Swap(i, j)
Refresh
Refresh()
```

See [Subprograms](subprograms.md).
