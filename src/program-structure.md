# Program structure

A script is a text file. The main file of a project is a *program* or a *library* and has the
extension `.spr`; the other files are *modules* with the extension `.s`, connected with `uses`.
A group of projects is kept in a `.sprg` file.

## Program

A program starts with the word `program` and a name. The declarations follow: constants, types,
variables, labels and subprograms. The statements to execute are placed between `begin` and `end`.

```pascal
program Area

const
  Width = 20
  Height = 15

var
  s: integer

begin
  s = Width * Height
  print s
end
```

A dot after the final `end` is allowed but not required. Everything after `end.` is ignored.

## Library

A library starts with the word `library`. Instead of `begin` it has an `initialization` section,
which runs when the library is loaded, and an optional `finalization` section, which runs when it is
unloaded. A library is not run directly: the CAM system loads it and calls its subprograms.

```pascal
library Tools

var
  Counter: integer

procedure Tick
begin
  Counter = Counter + 1
end

initialization
  Counter = 0
finalization
  print Counter
end
```

## Module

A module keeps declarations that several programs or libraries share. It starts with the word
`module` and a name; the name must match the file name. The part before `implementation` is the
interface: the types, constants, variables and subprogram headings declared there are visible to
the scripts that use the module. The bodies of the subprograms and the declarations used only
inside the module follow `implementation`. The module ends with `end`.

```pascal
module Geometry

type
  TPoint = record
    x: float
    y: float
  end

function Distance(a, b: TPoint): float

implementation

function Distance(a, b: TPoint): float
begin
  result = sqrt((a.x - b.x) ^ 2 + (a.y - b.y) ^ 2)
end

end
```

## Using modules

The `uses` section lists the modules a script needs. The path to the module file is given with
`in`; a path without a folder is looked up next to the script. Modules are separated by commas.

```pascal
program Distances
uses
  Geometry in 'geometry.s'
var
  p, q: TPoint
begin
  q.x = 3
  q.y = 4
  print Distance(p, q)
end
```

The CAM system supplies modules with the declarations of its objects, for example `STTypes`,
`STOperationTypes` and `STCurveTypes`. They are connected by name, without `in`. See
[External routines and interface classes](external-routines.md).

## Lines and separators

A statement or a declaration usually takes one line. The semicolon after a statement or a
declaration is optional; it is needed to put several statements on one line:

```pascal
if k > 5 then begin
  print 'a'; print 'b'
end
```

## Comments

The compiler skips comments:

- `//` — up to the end of the line;
- `{ ... }` — any text between the braces, including several lines.

```pascal
{ Distance between two points
  on the plane }
d = sqrt(dx * dx + dy * dy) // Pythagorean theorem
```

## Identifiers and keywords

An identifier names a constant, type, variable, subprogram, label or module. It starts with a
letter or an underscore and goes on with letters, digits and underscores. Upper and lower case
Latin letters are not distinguished in identifiers and keywords: `Count`, `count` and `COUNT` are
the same name, `print` and `PRINT` are the same keyword. For letters of other alphabets the case
matters, so names of Latin letters are recommended.

Keywords cannot be used as identifiers:

`and`, `array`, `as`, `begin`, `boolean`, `break`, `case`, `class`, `const`, `constructor`,
`continue`, `destructor`, `div`, `do`, `else`, `end`, `export`, `external`, `false`, `finalization`,
`float`, `for`, `from`, `funcptr`, `function`, `goto`, `if`, `implementation`, `import`, `in`,
`initialization`, `integer`, `is`, `label`, `library`, `mod`, `module`, `nil`, `not`, `of`,
`olebstr`, `operator`, `or`, `overload`, `packed`, `pointer`, `print`, `procedure`, `program`,
`property`, `read`, `record`, `repeat`, `string`, `then`, `to`, `true`, `type`, `until`, `uses`,
`var`, `while`, `with`, `write`.

The keywords `export`, `import`, `from`, `funcptr`, `is` and `packed` are reserved for features that
scripts cannot use in the current version.

The names of the [built-in routines](built-in-routines.md) are reserved as well: `abs`, `acos`,
`asin`, `atn`, `chr`, `copy`, `cos`, `ctan`, `exp`, `float_num`, `integer_num`, `len`, `ln`,
`locase`, `log`, `ord`, `pos`, `posex`, `pow`, `random`, `round`, `roundex`, `setlen`, `sgn`, `sin`,
`sqrt`, `tan`, `tostring`, `trunc`, `upcase`.

## Text encoding

Save script files in UTF-8 with a byte order mark (BOM) if they contain characters other than
Latin letters, for example Cyrillic text in strings or comments. A file without the mark is read in
the code page of Windows.
