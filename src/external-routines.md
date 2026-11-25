# External routines and interface classes

A script can call functions of dynamic link libraries (DLL) and work with the objects of the CAM
system. Both are declared with the word `external`.

## External routines

An external routine is declared with a heading followed by `external`, the library file name and,
after `name`, the name of the function in the export table of the library. If `name` is omitted,
the name of the subprogram is used.

```pascal
program ExternalCall

function GetTickCount: integer external 'kernel32.dll' name 'GetTickCount'
function StrLength(s: string): integer external 'kernel32.dll' name 'lstrlenW'

begin
  print GetTickCount > 0      // true
  print StrLength('abcdef')   // 6
end
```

The library file name and the function name are string literals or string constants. A library
without a path is looked up first in the library folders set by the CAM system, then by the rules of
Windows.

External routines use the `stdcall` calling convention. Parameters and results are passed as
follows:

| Type in the script | Passed to the library |
|---|---|
| `integer` | Signed 32-bit integer |
| `float` | 64-bit floating-point number (`double`) |
| `pointer` | Pointer |
| `string` | Pointer to the first character of a UTF-16 string (`const wchar_t*`); the library must not change it |
| `olebstr` | OLE Automation string `BSTR`; a `var` parameter passes a pointer to `BSTR` |

A function result can be `integer`, `float` or `pointer`. A library returns a string through a `var`
parameter of type `olebstr`: pass a string variable as the argument, and after the call it holds the
string written by the library. A string expression can be passed where a value parameter of type
`olebstr` is expected.

```pascal
function SysReAllocString(var p: olebstr; s: string): integer external 'oleaut32.dll' name 'SysReAllocString'
...
text = 'old'
SysReAllocString(text, 'new text')
print text    // new text
```

A variable of type `olebstr` cannot be declared.

The same function of a library can be declared under several names, and several external routines
with one name can be [overloaded](subprograms.md#overloading).

## Interface classes

The objects of the CAM system are used through *interface classes*. An interface class is declared
with `class external`, the library file name and, after `name`, the name of the interface. Unlike a
script class, it can have fields without a parent class. Each method is declared with
`external` and the name of the method of the interface. A fragment of the declaration of a curve of
the CAM system:

```pascal
type
  IST_Curve = class(IST_AbstractCurve) external 'sckernel_intf.dll' name 'IST_Curve'
    function Get_QntP: Integer external 'Get_QntP'
    function Get_TMin: float external 'Get_TMin'
    function Get_TMax: float external 'Get_TMax'
    function Get_FullLen: float external 'Get_FullLen'
    function Get_IsClosed: WordBool external 'Get_IsClosed'
    ...
  end
```

A variable of an interface class gets an object from the CAM system: as a parameter of an event
handler, as a result of a method of another object, and so on. Its methods are called like the methods
of script classes: `curveLength = curve.Get_FullLen`. A reference is converted to another interface
of the same object with `as`, for example `curve5D = receiver.GetCurve(wordbool(false)) as IST_Curve5D`.

The declarations of the CAM system objects are installed with the CAM system as modules in the
folder `Supplement\script_api` of the installation folder: `STTypes`, `STCurveTypes`,
`STOperationTypes`, `STXMLPropTypes`, `STGeomLibTypes` and others. A script connects them by name:

```pascal
module MyHandlers

uses
  STTypes, STCurveTypes, STOperationTypes
```

These modules also declare the data types of the CAM system, for example the records of points and
vectors, and use additional numeric types for data exchange: `WordBool`, `Double`, `Single`,
`Int64`, `LongWord`, `SmallInt`, `ShortInt`, `Word`, `Byte`. A value is converted to such a type by
the type name used as a function, for example `wordbool(true)`.

The reference of the interfaces of the CAM system is linked from the CAM system guide, section
[Application programming interface](https://docs.encycam.com/ENCY/3/en/10349.html).
