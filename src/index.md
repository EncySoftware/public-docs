# Script language

The CAM system has a built-in programming language for scripts. Its syntax is close to Pascal:
a script consists of declarations of types, constants, variables and subprograms and of statements
placed between `begin` and `end`. The CAM system compiles a script into byte code and runs it in its
built-in virtual machine.

```pascal
program Hello
begin
  print 'Hello, world!'
end
```

## Where scripts are used

- **Script units with event handlers.** The Scripts IDE window keeps script units and assigns
  subprograms to events that occur while the toolpath is calculated.
- **Scripted operations.** The subprograms of a scripted operation run when the operation is created,
  when its parameters change and when its toolpath is calculated.
- **Running the CAM system with a script.** A script given on the command line runs right after the
  CAM system starts.
- **Macros.** A recorded macro can be generated as a script and edited in the development
  environment; see [Editing the code](https://docs.encycam.com/ENCY/3/en/102462.html).
- **Utilities.** A script project (`.spr` file) can be added to the list of utilities and run from
  it; see [Utilities button of main panel](https://docs.encycam.com/ENCY/3/en/10012.html).

How to create script units, assign event handlers and make scripted operations is described in the
CAM system guide, section [Scripts](https://docs.encycam.com/ENCY/3/en/10346.html). This guide
describes the language itself.

## Contents

1. **[Program structure](program-structure.md)** — programs, libraries and modules, comments, identifiers
2. **[Data types](data-types.md)** — numbers, strings, arrays, records, type declarations
3. **[Constants and variables](constants-and-variables.md)** — declarations, scope, initial values
4. **[Expressions](expressions.md)** — operators and their priority
5. **[Statements](statements.md)** — assignment, conditions, loops, jumps, output
6. **[Subprograms](subprograms.md)** — procedures, functions, parameters, overloading
7. **[Classes](classes.md)** — fields, methods, constructors, properties, inheritance
8. **[External routines and interface classes](external-routines.md)** — routines from libraries, objects of the CAM system
9. **[Errors at run time](runtime-errors.md)** — error messages, `error_level`
10. **[Built-in routines](built-in-routines.md)** — mathematics, strings, conversions, arrays
11. **[System module](system-module.md)** — files and folders, dialogs, other programs
12. **[Development environment](development-environment.md)** — editing, compiling and debugging scripts
13. **[Known limitations](known-limitations.md)** — what does not work in the current version
