# Operation descriptors

A technological operation is described by one big `ComplexType` derived from an
existing operation, plus a small **registration record** that announces it to the
system. This chapter shows the anatomy of an operation using two real files:
[`Operations/MillOperations/FaceMillingOp.xml`](../../Operations/MillOperations/FaceMillingOp.xml)
(a shipped operation) and the partner example
`OperationSimpleNet.xml` from the `cam-api-examples` repository (an operation whose
toolpath is computed by a C# extension).

The shipped operation files live under `Operations\` and
`Operations\MillOperations\` and are pulled in by
[`Operations.xml`](../../Operations.xml) — read them as your reference. Your own
operation does **not** go there. Register it instead by one of the two mechanisms
in [§7](../xml-properties/framework-overview.md#7-where-your-custom-files-go): drop an
`*_ExtOp.xml` file in the common containers folder (picked up automatically), or
point the **Operations Manager** wizard (Utilities → Operations Manager) at your
operation XML file. Either way the file is an `<SCCollection>` in the
**`Operations`** namespace and uses exactly the syntax shown below.

## 1 The two pieces

To add an operation you provide:

1. **A registration record** in the `OperationRegistrator` namespace, whose
   `TypeName` equals the `ID` of your operation type.
2. **The operation type** itself, derived from an existing operation base.

```xml
<SCCollection>
    <!-- 1. Register the type name -->
    <SCNameSpace ID="OperationRegistrator">
        <SCType ID="RegTSTFaceMillingOp" type="TRegisterOperationRecord" Enabled="True">
            <TypeName DefaultValue="TSTFaceMillingOp"/>
        </SCType>
    </SCNameSpace>

    <!-- 2. The operation type (its ID must match TypeName above) -->
    <SCType ID="TSTFaceMillingOp" Caption="FaceMilling" type="TSTMillOp" Enabled="True">
        ...
    </SCType>
</SCCollection>
```
*(real example: [`Operations/MillOperations/FaceMillingOp.xml`](../../Operations/MillOperations/FaceMillingOp.xml))*

### Why the registration record exists

There can be a very large number of descriptors in the system. The
`OperationRegistrator` namespace is a small, fast **lookup index**: it lists which
XML types are actually technological operations, so the system can find them directly
instead of scanning the entire body of descriptors. A record is just a
`TRegisterOperationRecord` whose `TypeName` points at your operation type's `ID`.
If you forget the record, your type exists but is not recognized as an operation.

## 2 Choosing a base type

Operations inherit a great deal of structure (tool section, feeds, leads,
simulation, machine state, …) from a chain of base operations. Pick the base
whose behavior is closest to yours and override/extend from there:

| Base type | For |
|---|---|
| `TSTMillOp` (milling family) | Milling operations — e.g. `TSTFaceMillingOp` derives from it |
| Lathe operation base | Lathe operations |
| Axial / drilling base | Drilling and axial cycles |
| `TSTMillExtensionOp` | Operations whose toolpath is computed by a **CAM API extension** (see [§3](#3-the-operation-header)) |

The simplest way to find the right base is to open the shipped operation most
like the one you want and reuse its base type. The full inheritance tree of every
shipped operation — IDs, captions, parents, implementing classes and source files —
is tabulated in the **[operation hierarchy reference](operation-hierarchy.md)**.

## 3 The operation header

Near the top of the operation type you override a set of inherited "header"
members that identify and present the operation:

```xml
<SCType ID="TSTFaceMillingOp" Caption="FaceMilling" type="TSTMillOp" Enabled="True">
    <GUID        DefaultValue="{9F01E1A0-6F3E-4C7A-9C52-9A024CED54FF}"/>
    <ContainerID DefaultValue="{F4DE00D1-7AE3-468E-BA5C-ED3C8275CBF8}"/>

    <Name    DefaultValue="FaceMilling"/>
    <Comment DefaultValue="Face Milling"/>
    <OperationGroup DefaultValue="Mill"/>

    <Image DefaultValue="Images\FaceMilling.png"/>
    <Icon  DefaultValue="Images\FaceMilling_Ico.bmp"/>
    <Video DefaultValue="Video\FaceMilling.wmv"/>
    ...
</SCType>
```
*(real example: [`Operations/MillOperations/FaceMillingOp.xml`](../../Operations/MillOperations/FaceMillingOp.xml))*

| Header member | Meaning |
|---|---|
| `GUID` | Unique, permanent identity of the operation type. Generate a fresh one; never reuse. |
| `ContainerID` | Class GUID of the Delphi **container** that represents the operation in the operation tree (see below). Usually inherited; override only when your operation needs a specific container class. |
| `SolverID` | Identifies the **solver** that computes the toolpath (see below). Usually inherited. |
| `Name` / `Comment` | Default display name and description. |
| `OperationGroup` | Broad technological group the operation belongs to (`Mill`, `Lathe`, …). |
| `Image` / `Icon` / `Video` | Illustration, list icon, and tutorial clip. |

Useful attributes on the type element itself:

- `Enabled="True"` — the operation is available. Set `False` to ship it disabled.
- `DefaultVisibility="False"` — keep a specialized operation loadable but hidden
  from the default menu.
- `Version` — schema version; bump it when you change the operation's structure
  so existing saved data migrates correctly.

### ContainerID and SolverID — container, solver and toolpath

These two identifiers describe how an operation is implemented. Understanding the
split helps you decide what to inherit and what to override.

- **`ContainerID` — the container class.** It is the class GUID of the Delphi
  class that *represents the operation* in the CAM system's operation tree. The
  system instantiates this container class; the container then builds the operation
  instance from the XML descriptor, **owns it and all its parameters**, and is the
  object the rest of the system talks to.
- **`SolverID` — the (optional) solver.** When set, the container creates a
  separate **solver** subclass identified by `SolverID`, and that solver computes
  the toolpath. When `SolverID` is *not* set, there is no separate solver and the
  **container class computes the toolpath itself**.

> **Why the split exists (history).** Originally there were neither XML descriptors
> nor separate solvers — an operation was just a container class that defined all of
> its behavior: its parameters and its toolpath computation. XML descriptors (to
> declare parameters declaratively) and solvers (to factor out toolpath computation,
> including into CAM API extensions) were layered on later. That is why an operation
> can still work with only a container and no solver.

In practice you inherit both `ContainerID` and `SolverID` from your base type.
Override `ContainerID` only when your operation needs a specific container class;
set `SolverID` to choose the engine that computes the toolpath.

`SolverID` accepts **two forms**:

1. **A GUID of an existing built‑in solver class** — reuse an engine the system
   already provides:

   ```xml
   <SolverID DefaultValue="{301F6C21-2499-4514-83D1-72A4931529BE}"/>
   ```

2. **The identifier of a CAM API extension** you wrote — specifically an
   `OperationSolver` extension. Here `SolverID` is the extension's string `id`,
   not a GUID:

   ```xml
   <!-- from OperationSimpleNet.xml -->
   <SCType ID="TSimpleNetOP" Caption="Simple .NET" type="TSTMillExtensionOp" Enabled="True">
       <GUID     DefaultValue="{BDD2CAD7-D2A9-43C4-86E3-399FCB439FC0}"/>
       <SolverID DefaultValue="Extension.Operation.Simple.Net"/>
       ...
   </SCType>
   ```

   The same `id` is declared in the extension's settings file, under the
   `OperationSolver` entry:

   ```json
   // ExtensionOperationSimpleNet.settings.json
   "extensions": [
       { "OperationSolver": { "id": "Extension.Operation.Simple.Net" } }
   ]
   ```

   Working, compilable `OperationSolver` extensions live in the `cam-api-examples`
   repository under `Operation/` (`ExtensionOperationSimpleNet`,
   `ExtensionOperationParamsNet`). Derive such an operation from
   `TSTMillExtensionOp` (or the appropriate extension base) so the standard
   machinery is wired up for you.

### Grouping in the "new operation" menu — `MultiGroup`

`MultiGroup` controls where the operation appears in the *create new operation*
tree. It lets one operation show up in **several groups at once**, and lets
different interface configurations (e.g. *Beginner* vs *Expert*) place it in
different groups. Each entry is a `TLinkToParentMultiGroup` whose `ID` is the
target group; `OrderInGroup` sets its position within that group.

```xml
<MultiGroup>
    <SCType ID="Group3DEntry" OrderInGroup="1" type="TLinkToParentMultiGroup"/>
    <SCType ID="Roughing"     OrderInGroup="1" type="TLinkToParentMultiGroup"/>
</MultiGroup>
```
*(real example: [`Operations/MillOperations/FaceMillingOp.xml`](../../Operations/MillOperations/FaceMillingOp.xml))*

Use `MultiGroup` + `OrderInGroup` for all menu placement and ordering.

## 4 Adding parameters

Parameters are just members of the operation type. Group them under inspector
placeholders with `Parent`, order them, attach an icon with `ImageFile`, and make
them dynamic with the expression language from
[the expression language](../xml-properties/expression-language.md).

```xml
<!-- an enum that drives the operation's strategy -->
<SCType ID="Strategy" Caption="Strategy" type="Enumerated" DefaultValue="Spiral"
        ImageFile="$(SUPPLEMENT_FOLDER)\operations\TypeImages\FaceMillingStrategy.bmp">
    <SCType ID="Spiral"      Caption="Spiral"           type="None"/>
    <SCType ID="OptimZigzag" Caption="Optimized zigzag" type="None"/>
    <SCType ID="Zigzag"      Caption="Zigzag"           type="None"/>
    <SCType ID="OneWay"      Caption="One way"          type="None"/>
    <SCType ID="OnePass"     Caption="One pass"         type="None"/>
</SCType>

<!-- a value placed under Strategy, shown only for some strategies -->
<SCType ID="Step" Caption="Step" type="TPercentageValue"
        Parent="Strategy" Visible="[Strategy] != 4">
    <ValueType    DefaultValue="Percent"/>
    <PercentValue DefaultValue="75"/>
</SCType>
```
*(real example: [`Operations/MillOperations/FaceMillingOp.xml`](../../Operations/MillOperations/FaceMillingOp.xml))*

### Categories and placeholders

Parameters are assigned to inspector categories and to **placeholder** containers
inherited from the base, via `Category` and `Parent`:

```xml
<SCType ID="LeadInDistance" Caption="Lead in" type="TPercentageValue"
        Category="TPropertiesCategoryList.Leads" Parent="LeadsPlaceHolder"
        ImageFile="$(SUPPLEMENT_FOLDER)\operations\TypeImages\FaceMillingLeadInDistance.bmp">
    <PercentValue DefaultValue="10"/>
</SCType>
```

`Parent="LeadsPlaceHolder"` files this row under a grouping node defined by the
base operation, so related parameters collect together regardless of where they
are declared.

### Overriding inherited parameters

Because your operation inherits a full parameter set, much of an operation file is
*overrides* of inherited members — tuning defaults, hiding what doesn't apply, or
re‑enabling options. Use the override form (`<MemberName .../>`) from
[§4.2](../xml-properties/descriptor-syntax.md#42-overriding-an-inherited-member):

```xml
<Stock Visible="False"/>                 <!-- hide an inherited parameter -->
<ConditionsSection>
    <Feeds>
        <EngageFeed  Enabled="False"/>   <!-- disable feeds that don't apply -->
        <RetractFeed Enabled="False"/>
    </Feeds>
</ConditionsSection>
```

## 5 Checklist for a new operation

1. Generate a new `GUID`.
2. Choose `SolverID`: a built‑in solver GUID, or the `id` of your `OperationSolver`
   CAM API extension (derive from `TSTMillExtensionOp` in that case).
3. Add a registration record in `OperationRegistrator` with `TypeName` = your
   type's `ID`.
4. Derive the type from the closest existing operation base.
5. Override the header members (`Name`, `Comment`, `OperationGroup`,
   `Image`, `Icon`, `Video`) and set `MultiGroup` for menu placement.
6. Declare your strategy parameters and override inherited ones as needed; assign
   `Category`/`Parent` so they land in the right inspector group.
7. Register the operation — save it as `<YourName>_ExtOp.xml` in
   `$(COMMON_CONTAINERS_FOLDER)`, or add it through the Operations Manager wizard
   (see [§7](../xml-properties/framework-overview.md#7-where-your-custom-files-go)). Do not
   edit the shipped files under `Supplement`.
8. Bump `Version` whenever you later change the structure.

---

Next: **[Machine descriptors](../machines/machine-descriptors.md)**
