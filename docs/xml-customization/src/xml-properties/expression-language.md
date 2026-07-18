# Expression language

Many attribute values are not constants — they are **expressions** evaluated
against other properties. This is what makes descriptors dynamic: a default that
depends on another field, a row that appears only under certain conditions, a
caption that reflects the current unit system.

## 1 Where expressions are used

Any of these attributes may hold an expression instead of a literal:

- `DefaultValue`, `InchDefaultValue` — computed defaults.
- `Visible`, `Enabled`, `ReadOnly` — dynamic state (the expression must yield a
  boolean).
- `Caption`, `Text`, `UnitsChar` — computed display strings.
- a handful of others used by specific subsystems (e.g. error‑state flags).

An attribute value is treated as an expression when it contains a property
reference in `[...]` brackets or a recognized function/operator. A plain value
like `DefaultValue="1"` or `DefaultValue="Millimeters"` is taken literally.

## 2 Property references: `[...]`

A reference in square brackets resolves to the **value** of another property.

```xml
Visible="[Enabled]"
DefaultValue="[ApproachFeed.ValuePerMinut]"
```

### Name resolution

A bare name like `[Enabled]` is looked up in this order:

1. **siblings** of the current property,
2. the **parent** chain,
3. **global** properties / context objects in scope.

So `[Enabled]` next to the property usually means "the sibling `Enabled`".

### Dotted paths

Dots navigate into complex types and across the tree:

```xml
DefaultValue="[ApproachFeed.LatheFeedRelativeMeasurement]"
Visible="[TechOperation.IsPrevOpInOtherChannel]"
```

A path can also address an **enumeration option** by name — `[Group.LinearAxis]`
is the `LinearAxis` option of the `Group` enum. Comparing a property to one of
its options is the idiomatic way to test an enum:

```xml
Visible="[SimulationType] = [SimulationType.Painting]"
DefaultValue="([Group] != [Group.LinearAxis]) AND (([Max]-[Min]) GT 10000)"
```

### Context roots

Besides nearby properties, some **context objects** are available as path roots,
giving expressions access to the wider environment. The ones you'll see most:

| Root | Gives access to |
|---|---|
| `TechOperation` | The operation that owns the property (flags, neighbours, magazine info, …). |
| `CAMApplication` | Application‑level state (e.g. `[CAMApplication.PLMManager.ConnectionCount]`). |
| `CurrentMeasurementsSystem` | The active unit system and its captions. |

## 3 Accessors inside `[...]`

Within a reference you can call accessors on the resolved property:

| Accessor | Returns |
|---|---|
| `.Attribute(Name)` | The value of the descriptor attribute `Name` (e.g. `Caption`, `ItemIndex`, or any custom attribute). |
| `.EnumValue` | The currently selected option of an enum (so you can chain `.Attribute(Caption)` to get its label). |
| `.Value` | The property value explicitly (usually implicit). |
| `.Count` | Element count of an array. |

```xml
<!-- the caption of the currently chosen LinearUnits option -->
DefaultValue="[CurrentMeasurementsSystem.LinearUnits.EnumValue.Attribute(Caption)]"

<!-- this array element's running index, for a self-numbering caption -->
Caption="Point [Attribute(ItemIndex)]"
```

Inside an array element template, `$ParentNode` refers to the enclosing
collection element, e.g. `Caption="Rule [$ParentNode.Attribute(ItemIndex)]"`.

## 4 Operators

| Group | Operators |
|---|---|
| Arithmetic | `+`  `-`  `*`  `/`  `^` (power)  `DIV` (integer divide)  `MOD` |
| Comparison | `=`  `!=`  `<>`  `<`  `>`  `<=`  `>=` and the word forms `LT` `GT` `LE` `GE` |
| Logical | `AND`  `OR`  `NOT` |

Word forms exist because XML attribute values are quoted and the symbolic `<`/`>`
can be awkward to read next to markup — `GT`/`LT`/`GE`/`LE` are the common choice
in real files. Parentheses group sub‑expressions as usual.

```xml
Visible="[Enabled] and ([StepCount] GT 1)"
DefaultValue="[UpperWorkLevel] + 5"
SupportShortestPathRotation DefaultValue="([Group] != [Group.LinearAxis]) AND (([Max]-[Min]) GT 10000)"
```

## 5 Functions

### Conditionals — `CASE`, `IF`, `SWITCH`

These three cover almost all real‑world logic.

**`IF(condition, valueIfTrue, valueIfFalse)`** — the plain ternary.

```xml
DefaultValue="IF([SimulateToolChange], 'Auto', 'DoNotUse')"
```

**`CASE(...)`** — the most common conditional in descriptors. In its two‑value
form it behaves like `IF`: `CASE(condition, valueIfTrue, valueIfFalse)`. It also
chains: a series of `condition, result` pairs, evaluated in order, with an
optional final default.

```xml
<!-- if/else form -->
DefaultValue="CASE([IsSpatial], 'SnapToWorkpieceCS', 'SnapToToolCS')"

<!-- chained: first matching condition wins, last bare value is the default -->
DefaultValue="CASE(
    [HolderType]=[HolderType.LeftLatheSpindle],  '1',
    [HolderType]=[HolderType.RightLatheSpindle], '2',
    -1)"
```
*(real example: [`Machines/MachineTypes.xml`](../../Machines/MachineTypes.xml))*

**`SWITCH(value, case1, result1, case2, result2, …, default)`** — selects by
**equality** against `value`, like a classic switch statement. Useful when one
property maps to many outcomes:

```xml
RotationsSequence DefaultValue="
    SWITCH([ControlData.ToolFrameOutput.Format],
        [ControlData.ToolFrameOutput.Format.EulerXYZ], 'XYZ',
        [ControlData.ToolFrameOutput.Format.EulerXZY], 'XZY',
        'XYZ')"           <!-- final value is the default -->
```
*(real example: [`Machines/AbstractMachine.xml`](../../Machines/AbstractMachine.xml))*

### Numeric functions

| Function | Meaning |
|---|---|
| `MIN(a, b, …)` / `MAX(a, b, …)` | Minimum / maximum |
| `ABS(x)` | Absolute value |
| `ROUND(x [, digits])` / `SMARTROUND(x)` | Rounding |
| `SQRT`, `EXP`, `LN`, `SGN`/`SIGN` | Common math |
| `SIN`, `COS`, `TAN`, `ASIN`, `ACOS`, `ARCTAN`, … | Trigonometry |

### String functions

| Function | Meaning |
|---|---|
| `STR(x)` | Number → string |
| `CHR(code)` | Character from code point |
| `CONCATENATE(sep, s1, s2, …)` | Join strings with a separator |
| `ISVALUEINSET(v, a, b, …)` | True if `v` equals one of the listed values |

## 6 String literals

String literals inside expressions use single quotes: `'XYZ'`, `'Auto'`.

```xml
DefaultValue="IF([SimulateToolChange], 'Auto', 'DoNotUse')"
```

## 7 Worked examples

**A value that defaults to another property** — keep two feeds in sync unless
edited:

```xml
<ValuePerMinut DefaultValue="[ApproachFeed.ValuePerMinut]"
               InchDefaultValue="[ApproachFeed.ValuePerMinut]"/>
```

**A row that appears only when a flag is set and a count is meaningful:**

```xml
<SCType ID="StepValue" type="Double" DefaultValue="1" DimensionKind="Linear"
        Visible="[Enabled] and ([StepCount] GT 1)"/>
```

**An enum default chosen from another enum's state:**

```xml
<SCType ID="DefaultState" type="Enumerated"
        DefaultValue="if([RotaryTrans.TCPMAvailable] AND (NOT [RotaryTrans.TCPMDefault]), 'Auto', 'Off')">
    <SCType ID="Off"  type="none"/>
    <SCType ID="Auto" type="none"/>
</SCType>
```
*(real example: [`Machines/AbstractMachine.xml`](../../Machines/AbstractMachine.xml))*

> **Tips.** Keep expressions side‑effect free — they are evaluated whenever the UI
> refreshes. Test enum comparisons with the `[Enum.Option]` form rather than
> string literals, so a renamed option fails loudly instead of silently
> mismatching. When a `Visible`/`Enabled` expression references a property in
> another branch of the tree, use a full dotted path from a known root.

---

Next: **[Operation descriptors](../operations/operation-xml-descriptors.md)**
