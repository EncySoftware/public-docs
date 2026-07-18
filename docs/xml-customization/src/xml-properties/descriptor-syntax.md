# Descriptor syntax

This is the core reference chapter. It covers the XML elements, the type system,
how inheritance and overriding work, and the catalog of attributes you can put
on a descriptor.

## 1 The document skeleton

Every descriptor file is an XML document with `<SCCollection>` as its root
element. Inside it you place namespaces, includes, type declarations and
property declarations.

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<SCCollection>
    <SCNameSpace ID="Operations">
        <SCInclude>$(SUPPLEMENT_FOLDER)\CommonTypes.xml</SCInclude>
        <SCType ID="TFoo" type="ComplexType"> ... </SCType>
    </SCNameSpace>
</SCCollection>
```

The structural elements are:

| Element | Role |
|---|---|
| `SCCollection` | Document root. Always present. |
| `SCNameSpace` | Opens a namespace (`ID="Operations"`, `"Machines"`, …). Everything inside is declared in that namespace. May be nested. |
| `SCInclude` | Pulls in another file at this point. Supports `Optional="True"` and wildcards. |
| `SCType` | Declares a **type** (a reusable descriptor) — or, when nested inside another type, declares a **member** of it. The workhorse element. |
| `SCProperty` | Declares a **named global property** — a singleton value/object at namespace scope (see [§6](#6-scproperty--global-named-properties)). |

Files outside any `<SCNameSpace>` contribute to the namespace into which they are
included — that is why [`CommonTypes.xml`](../../CommonTypes.xml) has no
namespace of its own: it is included into many.

## 2 `SCType` — the workhorse

`SCType` does double duty depending on where it appears.

**At the top level (or directly under a namespace)** it *declares a type* — a
named, reusable template:

```xml
<SCType ID="T2DPoint" Caption="Point" type="ComplexType">
    <SCType ID="X" Caption="X" type="Double" DefaultValue="0" DimensionKind="Linear"/>
    <SCType ID="Y" Caption="Y" type="Double" DefaultValue="0" DimensionKind="Linear"/>
</SCType>
```

`ID` is the type's name; `type` names its **base** (here the built‑in
`ComplexType`). The nested `<SCType>` elements declare the type's *members*.

**Nested inside another type** an `<SCType>` *declares a new member* of the
enclosing type. The member's `ID` is its name within the parent, and its `type`
is the member's value type — which may be a built‑in type or any previously
declared type:

```xml
<SCType ID="TSTFaceMillingOp" type="TSTMillOp">
    <!-- a member named MillingType, of the previously declared type TMillMode -->
    <SCType ID="MillingType" type="TMillMode" Caption="Milling type"/>
</SCType>
```

So: **`ID` + `type` = "create a thing called *ID* that is a *type*"**, whether
that "thing" is a top‑level type or a member of a complex type.

## 3 The type system

### 3.1 Built‑in (primitive) types

The `type` attribute accepts these built‑in names (case is not significant —
`Double` and `double` are the same):

| Built‑in `type` | Holds | Notes |
|---|---|---|
| `Boolean` | `True` / `False` | |
| `Integer` | whole number | |
| `Double` | real number | Use `DimensionKind` for unit handling |
| `String` | text | |
| `Enumerated` | one choice from a fixed list | Items are child `SCType`s of `type="none"` |
| `ComplexType` | a record of named members | Children are the members |
| `Array` | a list of like elements | One child defines the element template; see [§5](#5-arrays) |
| `none` (or `None`) | nothing | Used for enumeration items, separators and pure UI placeholders |

Anything that is *not* one of these names is treated as a **reference to a
previously declared type** — that is how composition and inheritance work.

### 3.2 Enumerations

An enumeration lists its options as child `SCType`s with `type="none"`. The
enumeration's `DefaultValue` is the `ID` of the default option.

```xml
<SCType ID="TXYZCoordinate" Caption="XYZ Coordinate" type="Enumerated" DefaultValue="CoordX">
    <SCType ID="CoordAuto" Caption="Auto" type="none"/>
    <SCType ID="CoordX"    Caption="X"    type="none"/>
    <SCType ID="CoordY"    Caption="Y"    type="none"/>
    <SCType ID="CoordZ"    Caption="Z"    type="none"/>
</SCType>
```
*(real example: [`CommonTypes.xml`](../../CommonTypes.xml))*

The stored value of an enum property is the **option `ID`** (e.g. `CoordX`), not
its caption. Each option may carry its own metadata (a `Caption`, an `ImageFile`,
a `Priority`, a `Visible` rule, …).

### 3.3 Complex types

A `ComplexType` is a record: its child `SCType`s are its fields. Complex types
can nest arbitrarily and can be reused as the type of other members.

```xml
<SCType ID="TColor" Caption="Color" type="ComplexType">
    <SCType ID="R" type="Double" DefaultValue="0.5"/>
    <SCType ID="G" type="Double" DefaultValue="0.5"/>
    <SCType ID="B" type="Double" DefaultValue="0.5"/>
</SCType>
```

In the inspector a `TColor` is rendered as a colour swatch with a picker dialog rather
than three numeric rows — see [§3.4](#34-types-with-special-behaviour).

### 3.4 Types with special behaviour

A handful of frequently used types are declared in
[`CommonTypes.xml`](../../CommonTypes.xml) as thin **aliases** of a base type — you
reference them by name like any declared type — but each adds extra serialization or
inspector behaviour beyond its base. Declare a member with one of these when you want
that behaviour:

| Type | Base | What it adds |
|---|---|---|
| `TranslatableString` | `String` | Its value enters the **localization** subsystem and can be translated. By default only node `Caption`s are localized; use this type when a string *value* (typically a default value) must be translatable too. |
| `CDATAString` | `String` | Serialized inside a `CDATA` section, so the value may contain characters XML would otherwise forbid — letting it keep its original formatting, such as line breaks and tabs. |
| `FileName` | `String` | Holds a **file path**. On save/load the path is automatically converted between absolute and relative form and against path variables such as `$(SUPPLEMENT_FOLDER)`. In the inspector it offers a standard **file‑open dialog**; a `Filter` attribute (form `Caption (*.ext)\|mask1;mask2`) restricts that dialog to chosen file types. |
| `DynamicArray` | `Array` | Behaves like an `Array` ([§5](#5-arrays)), but the inspector shows the **element count** in the row's own value field and lets the user change it, adding or removing child elements on the fly. |
| `TColor` | `ComplexType` | A colour value (`R`/`G`/`B`, [§3.3](#33-complex-types)) rendered in the inspector as a **colour swatch** with a colour‑picker dialog. |

*(real example: [`CommonTypes.xml`](../../CommonTypes.xml). A `FileName` dialog filter — the
machine postprocessor field — in
[`Machines/AbstractMachine.xml`](../../Machines/AbstractMachine.xml):
`Filter="Postprocessors (*.sppx, *.dll)|*.sppx;*.dll"`.)*

## 4 Inheritance and overriding

### 4.1 Deriving a type

To base a new type on an existing one, name the existing type in `type`. The new
type starts with **all** the members of the base and then adds the members you
declare:

```xml
<SCType ID="T3DPoint" Caption="Point" type="T2DPoint">
    <!-- inherits X and Y from T2DPoint, adds Z -->
    <SCType ID="Z" type="Double" DefaultValue="0" DimensionKind="Linear"/>
</SCType>
```
*(real example: [`CommonTypes.xml`](../../CommonTypes.xml))*

Inheritance chains can be long. A concrete operation, for instance, derives from
a family of abstract operations
(`TSTFaceMillingOp` → `TSTMillOp` → … → `TOperationDescriptor`).

### 4.2 Overriding an inherited member

There are two different things you can write inside a type body, and the
difference is essential:

- `<SCType ID="Name" type="...">` — **declares a *new* member** called `Name`.
- `<Name ... />` — **overrides the *inherited* member** called `Name`. The tag
  *is* the member's name; you do **not** repeat `type`, you only restate the
  attributes you want to change.

```xml
<SCType ID="ZCleanup" type="TZCleanup" Caption="Cleanup height">
    <!-- override inherited members' defaults: -->
    <Enabled DefaultValue="True"/>
    <Height  DefaultValue="2"/>
</SCType>
```
*(real example: [`Operations/MillOperations/FaceMillingOp.xml`](../../Operations/MillOperations/FaceMillingOp.xml))*

Overrides can reach down into nested members and even into enumeration options.
The pattern `<EnumItem Visible="True"/>` re‑enables an option that a base type
had hidden:

```xml
<CirclesDivision DefaultValue="Halves">
    <AbsQuadrants Visible="True"/>   <!-- show an option the base hid -->
    <AbsHalves    Visible="True"/>
</CirclesDivision>
```
*(real example: [`Machines/AbstractMachine.xml`](../../Machines/AbstractMachine.xml))*

### 4.3 Metric and inch defaults

Numeric properties can declare two defaults: `DefaultValue` for the metric unit
system and `InchDefaultValue` for the imperial one. The system picks the right
one according to the active unit system — they are *independent values*, not an
automatic unit conversion, so set each to a sensible round number.

```xml
<SCType ID="Outer" type="Double" DefaultValue="0.02" InchDefaultValue="0.001"
        DimensionKind="Linear"/>
```
*(real example: [`Operations/AbstractOP.xml`](../../Operations/AbstractOP.xml))*

## 5 Arrays

An `Array` (or the predefined `DynamicArray`) holds a variable number of elements
of one type. You declare the element template as the array's single child:

```xml
<SCType ID="TStringList" Caption="List of strings" type="Array">
    <SCType ID="L" Caption="Line" type="String" DefaultValue=""/>
</SCType>
```

For arrays whose elements need a stable identity (so the application can match
elements across edits), set `CollectionKeyField` to the name of the member that
holds the key:

```xml
<SCType ID="List" type="Array" CollectionKeyField="Name">
    <SCType ID="Script" type="TScript"/>
</SCType>
```
*(real example: [`Operations/AbstractOP.xml`](../../Operations/AbstractOP.xml))*

Inside an array element, the running index is available to expressions through
`Attribute(ItemIndex)`, which is handy for auto‑numbered captions
(see [the expression language](expression-language.md)):

```xml
<SCType ID="J23ValuePair" Caption="Point [Attribute(ItemIndex)]" type="TJ23ValuePair"/>
```

## 6 `SCProperty` — global named properties

While `SCType` declares *templates*, `SCProperty` declares a **named global
property**: a single, addressable value or object at namespace scope. These act
as shared constants/objects that expressions elsewhere can reference by name.

```xml
<SCProperty ID="MetricMeasurementsSystem" type="TMeasurementsSystem">
    <LinearUnits DefaultValue="Millimeters"/>
    <CuttingSpeedUnits DefaultValue="MetersPerMinute"/>
</SCProperty>

<!-- a computed global string that derives its value from another global -->
<SCProperty ID="LinearUnits$" type="String"
            DefaultValue="[CurrentMeasurementsSystem.LinearUnits.EnumValue.Attribute(Caption)]"/>
```
*(real example: [`CommonTypes.xml`](../../CommonTypes.xml))*

> **The `$` naming convention.** A trailing `$` in a property `ID` (e.g.
> `LinearUnits$`) is a *convention* marking a derived, display‑oriented string
> property. The `$` is simply part of the name; it has no special parser meaning.

## 7 Path variables

File references — both `<SCInclude>` targets and attributes like `ImageFile`,
`Icon`, `SPPFile` — use `$(VARIABLE)` placeholders instead of absolute paths.
They resolve at runtime relative to the installation and the user profile.

| Variable | Resolves to (typical) |
|---|---|
| `$(SUPPLEMENT_FOLDER)` | `<install root>\Supplement` |
| `$(MACHINES_FOLDER)` | per‑user `…\Machines` |
| `$(SCHEMAS_FOLDER)` | `$(MACHINES_FOLDER)\Schemas` |
| `$(OPERATIONS_FOLDER)` | per‑user `…\Operations` |
| `$(LOCAL_OPERATIONS_FOLDER)` | local user operations folder |
| `$(COMMON_CONTAINERS_FOLDER)` | shared containers/extensions folder |
| `$(PROGRAM_PERSONAL)` | per‑user program data |

Always use these variables rather than hard‑coded paths, so your files keep
working regardless of where the product is installed or which user profile is
active.

## 8 Attribute catalog

Attributes set on `SCType` / `SCProperty` fall into two groups. A small set of
**core attributes** is understood by the descriptor loader itself; everything
else is a **consumer attribute**, carried along on the descriptor and interpreted
by the UI, the engine, or a specific presenter. From an author's point of view
both are "just attributes" — the table below tells you what each one does.

Boolean attributes take the literal text `True` / `False` (case‑insensitive).

### 8.1 Identity and type

| Attribute | Value | Meaning |
|---|---|---|
| `ID` | name | The member/type name. Required on declarations. |
| `type` / `Type` | type name | Value type — a built‑in or a previously declared type. |
| `Caption` | string / expression | Human‑readable label shown in the UI. May be computed. |
| `Version` | integer | Schema version of the type; bump it when you change structure so older saved data is migrated. |
| `Obsolete` | bool | Marks a member as deprecated; kept for compatibility, generally hidden. |

### 8.2 Values and units

| Attribute | Value | Meaning |
|---|---|---|
| `DefaultValue` | literal / expression | Default value (metric). For enums, the default option's `ID`. |
| `InchDefaultValue` | literal / expression | Default value when the imperial unit system is active. |
| `DimensionKind` | see below | Physical dimension of a numeric value, so the UI shows units and converts correctly. |
| `UnitsChar` | string / expression | Explicit unit label to display (e.g. `ml/s`, or `[TimeUnits_Sec$]`). |

`DimensionKind` values: `None`, `Linear`, `InverseLinear`, `Angular`,
`Feedrate`, `CuttingSpeed`, `Revolution`. Use `None` for dimensionless numbers
and direction components; `Linear` for distances; `Angular` for angles.

### 8.3 State and behavior

| Attribute | Value | Meaning |
|---|---|---|
| `Enabled` | bool / expression | Whether the property is active/editable. `False` greys it out. |
| `Visible` | bool / expression | Whether the row is shown. Drive it from other properties for dynamic forms. |
| `ReadOnly` | bool | Value is displayed but not editable. |
| `EnabledValue` | member name | For a boolean "switch" member: names the sibling that it enables when true (used with `Compact`). |
| `IsStructural` | bool | Changing this value changes the object's structure (triggers a rebuild rather than a simple value update). |
| `IsDynamic` | bool | The member's caption/icon is computed per‑instance (e.g. array items that name themselves). |

### 8.4 Presentation and grouping

| Attribute | Value | Meaning |
|---|---|---|
| `Category` | category id | Assigns the property to an inspector category/tab (e.g. `TPropertiesCategoryList.Feeds`). |
| `Parent` | member name | Re‑parents this row under another member in the inspector tree, regardless of declaration order. |
| `Priority` / `Order` | integer | Sort order of a row within its inspector group/category (higher `Priority` floats up). For placement in the *new operation* menu, use `MultiGroup` + `OrderInGroup` instead (see [Operation descriptors](../operations/operation-xml-descriptors.md#grouping-in-the-new-operation-menu--multigroup)). |
| `Expanded` | bool | Whether a complex row starts expanded in the tree. |
| `Compact` | bool | Collapse a complex type onto a single inspector row (see [§9](#9-compact-and-radio-edit-rows)). |
| `Transparent` | bool | The container itself is not shown; only its children appear (a pure grouping wrapper). |
| `Text` | string / expression | Summary text shown for a collapsed complex row. |
| `ImageFile` | path | Icon for the row (use a `$(…)` path variable). |

### 8.5 Editors / presenters

These attributes attach a specialized editor or renderer to a property. The
value is the registered name of a presenter provided by the application; you
reference it, you don't define it.

| Attribute | Meaning |
|---|---|
| `EnumPresenter` | Custom drop‑down/selector for the row (tool selector, magazine selector, …). |
| `BtnPresenter` | Renders the row as an action button (e.g. "Click to calculate"). |
| `VisPresenter` / `CaptionPresenter` | Custom value/caption renderer. |
| `IsRadioEdit` / `RadioEditValue` | Combine an enum with sibling value members into one row (see [§9](#9-compact-and-radio-edit-rows)). |
| `Filter` / `CustomDialogID` | For file‑name properties: file dialog filter / custom dialog. |

### 8.6 Arrays and integration

| Attribute | Meaning |
|---|---|
| `CollectionKeyField` | Member that uniquely identifies an array element. |
| `CollectionValueField` | Member that holds the element's payload value. |
| `Optional` | On `<SCInclude>`: load only if the file exists. |
| `ClassName` / `ClassGUID` / `InterfaceName` / `InterfaceGUID` | Bind the property to a COM object/interface the application instantiates for it. Advanced; rarely needed in hand‑authored descriptors. |

> **Unknown attributes are preserved, not rejected.** If you put an attribute the
> loader doesn't recognize, it is kept on the descriptor and is available to
> consumers and the API. That is by design — it is how presenters receive their
> parameters (e.g. `AxisIdx`, `HolderType`). It also means a typo in a *known*
> attribute name fails silently, so double‑check spelling and casing.

## 9 Compact and radio-edit rows

Two presentation patterns appear constantly in real descriptors and are worth
understanding because they change how several members map to one inspector row.

### Compact

`Compact="True"` on a complex type collapses it onto **one** inspector row: the
first visible child is promoted next to the parent's label. The classic shape is
an `Enabled` flag plus the value it gates, with `EnabledValue` linking them:

```xml
<SCType ID="SmoothCorners" type="ComplexType" Compact="True">
    <SCType ID="Enabled" type="Boolean" DefaultValue="True" EnabledValue="Radius"/>
    <SCType ID="Radius"  type="TPercentageValue" Visible="False">
        <PercentValue DefaultValue="25"/>
    </SCType>
</SCType>
```
*(real example: [`Operations/MillOperations/FaceMillingOp.xml`](../../Operations/MillOperations/FaceMillingOp.xml))*

The user sees a single "Smooth corners" row with a checkbox and a value.

### Radio edit

`IsRadioEdit="True"` on an enumeration merges it with sibling value members into
one row, where the enum choice selects which sibling is active. Each enum option
points at its sibling via `RadioEditValue`:

```xml
<SCType ID="ReferenceType" type="Enumerated" IsRadioEdit="True">
    <SCType ID="Angle"  Caption="(degrees)"     type="none" RadioEditValue="Angle"/>
    <SCType ID="Linear" Caption="[LinearUnits$]" type="none" RadioEditValue="Linear"/>
</SCType>
<SCType ID="Angle"  type="Double" DefaultValue="5"  Visible="False" DimensionKind="Angular"/>
<SCType ID="Linear" type="Double" DefaultValue="50" Visible="False" DimensionKind="Linear"/>
```
*(real example: [`Machines/AbstractMachine.xml`](../../Machines/AbstractMachine.xml))*

---

Next: **[Expression language](expression-language.md)**
