# Classes

A class joins data, the *fields*, with the subprograms that work with them, the *methods*. A
variable of a class type holds a reference to an *object*, an instance of the class.

## Declaration

A class is declared in a `type` section. The declaration lists the fields first, then the methods,
constructors, destructors and properties, and ends with `end`.

```pascal
type
  TObject = class
  end

  TCounter = class(TObject)
    count: integer
    procedure Add(step: integer)
    function Value: integer
  end
```

The class in parentheses after `class` is the parent class (see [Inheritance](#inheritance)). In the
current version of the language a class that has fields must be declared with a parent class, and
its fields must precede its methods. When no real parent is needed, use an empty class, as
`TObject` above. A class without fields can be declared without a parent.

Methods are defined after the class declaration. The name of a method is preceded by the class name
and a dot. Inside a method the fields and other methods of the object are used by their names;
the object itself is available as `self`.

```pascal
procedure TCounter.Add(step: integer)
begin
  count = count + step
end

function TCounter.Value: integer
begin
  result = self.count
end
```

## Creating objects

An object is created by a constructor called with the class name:

- `TCounter.create` — the default constructor, available in every class. It creates an object whose
  fields hold the [initial values](constants-and-variables.md#initial-values) of their types.
- A constructor declared in the class with the word `constructor` — it creates the object and runs
  its code, for example to set the fields from its parameters.

```pascal
program Objects
type
  TObject = class
  end

  TPerson = class(TObject)
    name: string
    age: integer
    constructor Make(aName: string; aAge: integer)
    destructor Done
  end

constructor TPerson.Make(aName: string; aAge: integer)
begin
  name = aName
  age = aAge
end

destructor TPerson.Done
begin
  print 'done ' + name
end

var
  p, q: TPerson
begin
  p = TPerson.Make('Ann', 30)
  q = p           // q refers to the same object
  q.age = 41
  print p.age     // 41
  p.Done          // done Ann
  p.destroy
end
```

A variable of a class type that has not been assigned an object holds `nil`. Compare it with `nil`
before use: `if p <> nil then ...`.

An object exists until it is freed with `destroy`, the destructor that every class has: `p.destroy`
frees the object and sets `p` to `nil`. Other variables that referred to the object keep the
reference to the freed object; do not use them. Free objects that are no longer needed with
`destroy`.

A destructor declared in the class with the word `destructor` runs its code, for example to release
resources that the object holds, but does not free the object: call `destroy` after it, as in the
example above.

## Properties

A property looks like a field to the code that uses the object, while reading and writing it call
methods. The declaration names the type of the property and the methods after `read` and `write`.
A property with `read` only cannot be assigned.

```pascal
type
  TPerson = class(TObject)
    fname: string
    function GetName: string
    procedure SetName(value: string)
    property Name: string read GetName write SetName
  end

function TPerson.GetName: string
begin
  result = fname
end

procedure TPerson.SetName(value: string)
begin
  fname = upcase(value)
end
```

After `p.Name = 'bob'` the expression `p.Name` gives `BOB`.

A property can have an index. Its read method takes the index, its write method takes the index and
the value:

```pascal
type
  TList = class(TObject)
    items: array of integer
    function GetItem(index: integer): integer
    procedure SetItem(index: integer; value: integer)
    property Item[index: integer]: integer read GetItem write SetItem
  end
```

`l.Item[2] = 7` calls `l.SetItem(2, 7)`, `l.Item[2]` calls `l.GetItem(2)`.

## Inheritance

A class declared as `class(TParent)` inherits the methods of the parent class: they can be called
for objects of the new class. A method with the same name declared in the new class replaces the
parent's method for objects of the new class.

The method is chosen by the declared type of the variable, not by the class of the object. If a
variable of type `TShape` refers to an object of the derived class `TRect`, calling `Area` through
this variable runs `TShape.Area`.

The fields of the parent class are not available in the derived class, and the parent's methods that
use its fields do not work for objects of the derived class. Derive classes only from classes
without fields, such as the empty `TObject` above, and declare the fields in the class whose methods
use them.

## Classes of the CAM system

The objects of the CAM system, such as curves, operations and tools, are available to scripts
through interface classes declared with `class external`. See
[External routines and interface classes](external-routines.md#interface-classes).
