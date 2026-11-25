# Known limitations

The current version of the language has the limitations listed below. Most of them are also
described in the section where they matter.

## Declarations and types

- An `integer` result that does not fit into the range wraps around without an error message. See
  [Simple types](data-types.md#simple-types).
- A minus before the value of a constant is lost: `Offset = -5` gives `5`. See
  [Constants](constants-and-variables.md#constants).
- A string literal cannot contain the single quote character. See
  [Simple types](data-types.md#simple-types).
- The virtual machine does not report an index outside an array. See [Arrays](data-types.md#arrays).
- A variable of type `olebstr` cannot be declared. See
  [External routines](external-routines.md#external-routines).
- The keywords `export`, `import`, `from`, `funcptr`, `is` and `packed` cannot be used. See
  [Identifiers and keywords](program-structure.md#identifiers-and-keywords).

## Expressions and statements

- `^` cannot be chained, and its exponent cannot start with a minus. See
  [Priority](expressions.md#priority).
- Only the unary minus can be defined with `operator`. See
  [Operator for a record type](expressions.md#operator-for-a-record-type).
- With a string selector `case` reports the error `incompatible types` and executes the `else`
  branch. See [case](statements.md#case).
- Assignments to the fields of a record made inside `with` are not kept. See
  [with](statements.md#with).
- There is no statement that leaves a subprogram before its end; a label before the final `end`
  does this. See [goto](statements.md#goto).
- There is no `forward` declaration: in a program two subprograms cannot call each other. See
  [Recursion](subprograms.md#recursion).

## Classes

- A class that has fields must be declared with a parent class, and its fields must precede its
  methods. See [Declaration](classes.md#declaration).
- The fields of the parent class are not available in the derived class, and the parent's methods
  that use its fields do not work for objects of the derived class. See
  [Inheritance](classes.md#inheritance).

## Routines

- `chr`, `posex` and `random` do not work. See
  [Routines that do not work](built-in-routines.md#routines-that-do-not-work).
- The parameter `title` of `show_message` is not used. See [Dialogs](system-module.md#dialogs).
- The routines `extract_file_ext` and `rename_file` of the system module work incorrectly and are
  not described in this guide: `extract_file_ext` returns the folder of the file, and
  `rename_file(old, new)` renames the file `new` to `old`.
