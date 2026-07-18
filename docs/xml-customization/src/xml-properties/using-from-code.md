# Using XML properties from code

The properties you declare in XML are the same properties you read and write from
code. They are reachable from several environments — the **CAM API** (.NET, C++, …),
**native Delphi / C++** packages, **.NET postprocessors**, and **`.sppx`
postprocessors** — and, crucially, **the access pattern is identical in all of them**.
This chapter describes that common pattern once, then shows the small per‑environment
specifics.

## 1 One model, one access pattern, many hosts

Recall the [types‑vs‑instances](framework-overview.md#2-types-vs-instances)
distinction. From any host you work with **instances**: the live property tree of a
concrete object, where each node is a **property pointer**. From a pointer you read or
write its value, step into children, search, and inspect its **descriptor** for type
metadata.

A pointer always offers the **same named accessors**, whatever the host:

| Accessor | What it does |
|---|---|
| `Str[name]` / `Int[name]` / `Flt[name]` / `Bol[name]` | read **and write** a child's value as string / integer / double / boolean |
| `Ptr[name]` | get a child pointer (to step into a `ComplexType`) |
| `Arr[name]` | get a child array |
| `ValueAsString` / `ValueAsInteger` / `ValueAsDouble` / `ValueAsBoolean` | the pointer's *own* value |
| `FindChild` / `FindProperty` | locate a child by name |

**Names can be compound, and the case does not matter.** Rather than stepping with
`Ptr`, pass the **dotted path** straight to the accessor, and address **array elements
by key or index** with `(…)`:

```text
Flt["RoughPasses.StepValue"]          # nested value, dotted
Int["controldata.usearc"]             # case-insensitive
Flt["Axes(AxisXPos).Value"]           # array element by key, then a child
Str["Project.Operations(0).Name"]     # array element by index
```

The same accessor names, the same dotted/case‑insensitive lookups and the same `(key)`
array syntax appear in **every** host; only the language wrapping differs:

| Host | Pointer type | COM wrapping? |
|---|---|---|
| CAM API (.NET / C++ / …) | `IST_XMLPropPointer` | yes |
| Native Delphi / C++ packages | `IST_XMLPropPointer` | no |
| .NET postprocessors | `INamedProperty` | no |
| `.sppx` postprocessors (Pascal‑like language) | built‑in | no |

So **§2–9 below are the .NET CAM API flavour**: the `ComWrapper`, `Invoke` /
`InvokeAndWrap` and `using` you will see there are **.NET‑COM wrapping**, *not* part of
the property model. The native and postprocessor hosts (§10–12) use the very same
accessor names without that ceremony.

### Finding a property's full name

To use the accessors you need a property's **full, dotted name**. The quickest way to
get it is from the running program:

1. Open the operation's **property inspector** and find the property.
2. At the **right edge** of its row click the **⋯ (three‑dots)** button to open the row
   menu, and choose **"Copy property name to clipboard."**

The same menu has **"Customize…"**, which opens a window showing not only the
property's **computed value** but its **source expression** — handy when the value is
parametrized from other properties (see [the expression language](expression-language.md)). *(This
window exists only in recent versions.)*

> **Older versions — a workaround.** If there is no *Customize…* window, use the
> operation's context menu → **"Save as user operation."** In the window that opens,
> find the property in the inspector, right‑click it, and use **"Copy property name to
> clipboard"** there. Then **strip the leading `RefOperations(0).`** from the copied
> name — it appears only because that window shows a *copy* of the properties inside a
> separate *UserOperation* entity, not the live operation. What remains is the name you
> pass to the accessors.

## 2 Getting the property tree of an object

Domain objects expose their property tree through an `XMLProp` member. For a
technological operation:

```csharp
using var xmlPropsCom = operationCom.InvokeAndWrap(operation => operation.XMLProp);
```

> **`XMLProp` is the object's unified property tree.** For properties kept **only** in
> `XMLProp` (the modern case) it is authoritative — reading/writing it needs no commit
> step. But some **operations** still mirror certain values in their own object fields
> (legacy code); there `XMLProp` and the object can diverge and must be synchronized
> with `SaveToXMLProp` / `LoadFromXMLProp` — see
> [§7](#7-operations-syncing-object-fields-with-xmlprop).

The same `XMLProp` pattern applies to machines, tools and other objects.

## 3 Reading and writing values by name

Each node exposes typed indexers keyed by child name: `Str`, `Flt`, `Int`, `Bol`.
This is the idiom used throughout the examples — set a value by assigning to the
indexer:

```csharp
// from FullWorkflow3DProject/TechnologyHelper.cs
using var xmlPropsCom = operationCom.InvokeAndWrap(operation => operation.XMLProp);
xmlPropsCom.Invoke(xmlProps =>
{
    xmlProps.Str["DrillingType"] = "HolePocketing";   // write a string / enum option id
});
```

Reading is symmetric:

```csharp
xmlPropsCom.Invoke(xmlProps =>
{
    double step  = xmlProps.Flt["StepValue"];
    int    count = xmlProps.Int["StepCount"];
    bool   on    = xmlProps.Bol["Enabled"];
    string mode  = xmlProps.Str["DrillingType"];
});
```

As in every host ([§1](#1-one-model-one-access-pattern-many-hosts)), the name can be
a **dotted path** and is **case‑insensitive**, so you can reach a nested value in one
call instead of stepping with `Ptr` (§4):

```csharp
double step = xmlProps.Flt["RoughPasses.StepValue"];
bool   on   = xmlProps.Bol["roughpasses.enabled"];   // case ignored
```

### Check existence first

A property may not exist on a given object (e.g. an optional or custom
parameter). Guard reads with `PropExists`:

```csharp
var value = xmlProps.PropExists["DrillingType"]
    ? xmlProps.Str["DrillingType"]
    : "";
```

> **Enums — by ID or by index.** An enumeration's value is its *option `ID`*, so
> `Str["DrillingType"] = "ChipRemoving"` sets it by ID (the option's `ID`, not its
> caption — see [§3.2](descriptor-syntax.md#32-enumerations)). You can **also**
> read or write it **by zero‑based option index** with `Int`:
> `Int["DrillingType"] = 2` selects the *third* option, and reading
> `Int["DrillingType"]` returns the current option's index. (This works in every host.)

### The convenience helper layer (.NET)

The .NET helper package wraps those indexers as extension methods on
`ComWrapper<IST_XMLPropPointer>`, so you can avoid the explicit `Invoke`:

```csharp
double step = xmlPropsCom.Flt("StepValue");      // getter
xmlPropsCom.SetFlt("StepValue", 2.5);            // setter
xmlPropsCom.SetStr("DrillingType", "ChipRemoving");
string calc = xmlPropsCom.CStr("SomeComputed");  // evaluated value of a computed property
```

Helpers exist for each type (`Str`/`Flt`/`Int`/`Bol` and their `Set…` forms),
plus `Ptr`, `Arr`, `FindProperty`, `FindPropertyInWholeScope`, and more. Use
whichever style fits your code; they call the same underlying interface.

## 4 Navigating the tree

### Step into complex types

`Ptr[name]` (or the `Ptr(name)` helper) descends into a `ComplexType` child;
continue with the typed indexers. This mirrors the dotted paths from your XML
(`RoughPasses.StepValue`):

```csharp
xmlPropsCom.Invoke(xmlProps =>
{
    var rough = xmlProps.Ptr["RoughPasses"];
    rough.Bol["Enabled"]   = true;
    rough.Flt["StepValue"] = 1.0;
});
```

### Search by name

When you don't want to spell out the full path, search the subtree:

```csharp
using var dt = xmlPropsCom.FindPropertyInWholeScope("DrillingType");
string current = dt.ValueAsString();
dt.SetNodeValue("ChipRemoving");
```

`FindPropertyInWholeScope` returns the first match at any depth — prefer `Ptr`
chains (or the scoped `FindProperty`) when a name might not be unique.

## 5 Arrays

An array child is an `IST_XMLPropArray`, obtained with `Arr[name]`. It supports
element creation and addition on top of the normal pointer operations. This is
the real pattern used to add a custom array element:

```csharp
// from ExtensionOperationParamsNet/OperationCustomPropsHelper.cs
const string arrayId = "CustomOperationPropertiesArray";
using var paramArrayCom = ComWrapper.Create(operation.XMLProp.Arr[arrayId]);

if (!operation.XMLProp.PropExists[fullId])
{
    var newItem = paramArrayCom.Invoke(a => a.CreateNewItem("CustomOperationProperty"));
    newItem.Str["Name"] = paramId;
    paramArrayCom.Invoke(a => a.AddItem(newItem));
}
```

### Addressing an array element by key

When an array element has a `Name`/key member, you can address it directly with
the `ArrayName(key)` path syntax in the indexer — no manual iteration:

```csharp
var fullId = $"{arrayId}({paramId})";          // e.g. CustomOperationPropertiesArray(MyParam)
operation.XMLProp.Str[fullId] = "true";        // read/write the element's value
bool exists = operation.XMLProp.PropExists[fullId];
```

## 6 A pointer's own value

The accessors in §3 read a **child** by name (`Str["StepValue"]`). When you already
hold the pointer to the property *itself* (rather than its parent), read or write **its
own value**. This is **typed** too — `ValueAsString`, `ValueAsDouble`, `ValueAsInteger`,
`ValueAsBoolean` (see the accessor list in
[§1](#1-one-model-one-access-pattern-many-hosts)). `ValueAsString` applies to **any**
property type and returns its string representation:

```csharp
double v   = somePropCom.ValueAsDouble();   // typed own value
string raw = somePropCom.ValueAsString();   // any type → its text form
somePropCom.SetNodeValue("75");             // set the pointer's own value
```

## 7 Operations: syncing object fields with `XMLProp`

*(Operations only.)* For an operation, `XMLProp` is its **unified property tree** with
two jobs: a single runtime tree (so common code can show every operation in the
inspector, and values can be copied between operations) and the form in which the
operation's properties are serialized to/from XML when the project is saved or loaded.

Historically, operations held their values in plain **object fields**, and `XMLProp`
was added later on top. So **legacy** properties live in *both* places — the object's
fields **and** `XMLProp` — and the two copies must be kept in step:

- **`SaveToXMLProp`** — push the operation's current **field values into `XMLProp`**.
  Call it before reading `XMLProp` (e.g. before the inspector is populated from the
  tree) so the tree reflects the live object state.
- **`LoadFromXMLProp`** — read values **from `XMLProp` back into the object's fields**.
  Call it after `XMLProp` was edited (e.g. after the user changed a value in the
  inspector) so the object model picks the change up.

**Modern** properties live only in `XMLProp` — no duplicate field, so no synchronization
is needed; reading/writing `XMLProp` is enough. The sync calls matter mainly for the
older classes, of which there are still many.

`LoadFromXMLProp` also accepts a *different* operation's `XMLProp`, which is how an
operation's settings are copied from another:

```csharp
operationCom.LoadFromXmlProp(otherXmlPropsCom);   // apply another property tree to this operation
```

`SaveToXmlProp()` returns the operation's properties as a tree (with the object fields
flushed into it) — handy to snapshot, diff or transfer.

## 8 Inspecting descriptors and defaults

Every property pointer links to its **descriptor** (`IST_XMLPropDescriptor`),
which carries the metadata you declared in XML — name, caption, simple type,
default value, custom attributes, inheritance. Use it when you need to reason
about the *schema* rather than the value (for example, enumerating an object's
parameters generically, or reading a custom attribute you set on the descriptor).

Defaults are reachable through `IST_PropDefaultsEditor` (queried from the
descriptor): it distinguishes the **system default** (declared in the descriptor
XML) from any **user default** override, for both metric and inch unit systems,
and lets you read, set or clear the user default.

## 9 Practical notes

- **Dispose COM wrappers.** Property pointers and arrays are COM objects; wrap
  them in `using` so they are released promptly. In the examples, work is done
  inside `Invoke` / `InvokeAndWrap` lambdas which manage lifetime for you.
- **Use the exact `ID`** from the descriptor — names must match what the XML
  declares.
- **Set enums and booleans with their canonical text** — option `ID` for enums;
  for booleans the examples use the strings `"true"`/`"false"` via `Str[...]`, or
  the typed `Bol[...]` indexer.
- **Don't fight computed values.** A property whose value is driven by a
  `DefaultValue`/`Visible` expression will recompute; read its evaluated result
  with `CStr` (or `ValueAsCalculatedString`), and make it a real editable field if
  you need to store a fixed value.
- **Where to look next.** The `cam-api-examples` repository
  (`Operation/ExtensionOperationParamsNet`, `FullWorkflow`, `ProjectMachine`)
  contain complete, compilable usages of everything above.

## 10 Native use (Delphi / C++)

The native packages expose the same property pointer through the public
`IST_XMLPropPointer`. There is **no COM wrapper, no `Invoke`, no `using`**: you hold an
ordinary interface reference and call the same accessors directly. A domain object's
`LoadFromXMLProp` / `SaveToXMLProp` (and `LoadConditionsFromXMLProp`) methods receive
such a pointer:

```pascal
procedure LoadFromXMLProp(XMLProp: IST_XMLPropPointer);
var p: IST_XMLPropPointer;
begin
  if XMLProp <> nil then with XMLProp do begin
    p := FindProp('SafeLevel');
    if p <> nil then with p do begin
      fZRetract.IsAbs  := Int['ReferenceType'] = 0;   // the same Int[…]/Flt[…] accessors
      fZRetract.IncVal := Flt['RelValue'];
      fZRetract.AbsVal := Flt['AbsValue'];
    end;
  end;
end;
```

It is the same `Int[…]` / `Flt[…]` / `Str[…]` / `Bol[…]` / `FindProp` as from .NET —
just without the COM ceremony.

## 11 In .NET postprocessors (`INamedProperty`)

A .NET postprocessor reads the named properties of the command/project it is given and
emits NC code. It uses a **pure‑.NET layer with no COM — `INamedProperty`** — but the
access is the same: `Str` / `Int` / `Flt` / `Bol` / `Ptr` / `Arr` indexers plus
`ValueAsString` / `ValueAsInteger` / `ValueAsDouble` / `ValueAsBoolean`, with the
familiar **dotted, case‑insensitive** names and `(key)` / `(index)` array addressing:

```csharp
double x      = cmd.Flt["Axes(AxisXPos).Value"];
int    origin = cmd.Int["OriginType"];
double ox     = cmd.Flt["WCS.OriginPoint.X"];
```

A worked postprocessor is in the `postprocessors-examples` repository under
`Features/NamedParameters/DemoOfWritePPFun` (see `WritePPFun.cs`). That example is a
slightly unusual context — it *writes* the parameters to a file — but the access to the
properties is exactly as above.

## 12 In `.sppx` postprocessors (Pascal‑like language)

`.sppx` postprocessors are written in a dedicated, Pascal‑like language. The set of
available types differs, but the **method names and the way you access properties are
identical**. In the snippets below `Cmd` is one such property‑bearing object — the
current **CLData command** — and the **same accessors apply to any property object**:
`.Int["…"]` / `.Flt["…"]` / `.Str["…"]` / `.Bol["…"]` for values and `.Ptr["…"]` for a
child property pointer, all with the familiar dotted / `(key)` names:

```pascal
if Cmd.Ptr["Axes(AxisXPos)"] <> 0 then          // child property pointer (here: does the axis exist?)
  X = Cmd.Flt["Axes(AxisXPos).Value"]
if Cmd.Int["Axes(AxisAPos).BrakeState"] > 0 then ...
CurG68_2_X = Round(Cmd.Flt["WCS.OriginPoint.X"], 4)
```
*(real example: `MyDocuments\Postprocessors\Mill\Fanuc (30i)_Mill.sppx`)*

---

Next: **[User defaults](user-defaults.md)** · Back to the
**[guide index](readme-xml-framework.md)**.
