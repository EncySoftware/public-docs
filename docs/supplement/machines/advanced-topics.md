# Advanced machine topics

This page covers the parts of machine authoring that go beyond the basic kinematic
scheme of [Machine descriptors](machine-descriptors.md): how to **position nodes with matrices**, how
to build **switchable / detachable nodes** (turret blocks, attachable heads, …), a
full **turret** walk‑through, and **control channels & sub‑machines** for
multi‑channel machines.

Most machines are produced with **MachineMaker** (see [Machine descriptors](machine-descriptors.md)); the
techniques here are for the special cases that are still authored, or fine‑tuned, by
hand. The building‑block types are in
[`Machines/MachineTypes.xml`](../../Machines/MachineTypes.xml), the turret/chuck
templates in [`Machines/TurretTypes.xml`](../../Machines/TurretTypes.xml), and a
multi‑channel example template in
[`Machines/SwissTemplate.xml`](../../Machines/SwissTemplate.xml). Complete machines
ship under `$(SCHEMAS_FOLDER)` and are the best reference.

---

## 1 Positioning nodes with matrices

Every node in the `Schema` (a `TMachineNode` and its descendants) carries a
**`Matrix`** that places it **relative to its parent node**. The whole kinematic
chain is the product of these matrices down the tree. There are two ways to fill a
`Matrix`, plus a separate matrix used only for the 3D model.

The matrix type (`TMatrix`) has a **`BaseCS`** selector — `Parent` (default) or
`World` — and is built either from a *series of transformation steps* or from an
*explicit basis* (`OrtX`/`OrtY`/`OrtZ` + `Move`).

### Way 1 — relative to the parent CS (a series of moves and turns)

The usual way. Leave the base matrix at identity and **add a series of translation
and rotation steps**, applied in declaration order. The step types are
`TTranslateX` / `TTranslateY` / `TTranslateZ` and `TRotateX` / `TRotateY` /
`TRotateZ` (degrees). Each step is a member you declare inside `Matrix`:

```xml
<SCType ID="MyNode" type="TMachineNode">
    <Matrix>
        <SCType ID="T1" type="TTranslateZ" DefaultValue="100"/>  <!-- then... -->
        <SCType ID="T2" type="TRotateX"    DefaultValue="90"/>
    </Matrix>
</SCType>
```

This is what the turret templates use, with the offsets driven by expressions
(see [§3](#3-turrets)):

```xml
<!-- TurretTypes.xml: a turret block, positioned on the head -->
<Matrix>
    <SCType ID="T1" type="TTranslateX" DefaultValue="-[TurretParameters.Radius]"/>
    <SCType ID="T2" type="TRotateZ"
            DefaultValue="-[TurretParameters.RotationDirection]*360/[TurretParameters.BlocksCount]*([Parameters.BlockNumber]-1)"/>
</Matrix>
```

`BaseCS` stays `Parent` (the default), so the steps are interpreted in the parent
node's coordinate system. Order matters — `T1` is applied, then `T2`.

### Way 2 — relative to the world CS (spatial angles)

When a node is easier to describe in the cell's **world** coordinate system, set
`BaseCS` to `World` and give a single spatial transformation
(`TComplexTransformation3d`): a translation plus three angles in a chosen
**convention** (Euler / fixed‑axis / quaternion / axis‑angle).

```xml
<Matrix>
    <BaseCS DefaultValue="World"/>
    <SCType ID="T1" type="TComplexTransformation3d">
        <Translation><X DefaultValue="0"/><Y DefaultValue="0"/><Z DefaultValue="300"/></Translation>
        <Rotation>
            <Convention DefaultValue="EulerZYX"/>  <!-- FixedXYZ, Quaternion, AxisAngleDeg, ... -->
            <R1 DefaultValue="0"/>
            <R2 DefaultValue="45"/>
            <R3 DefaultValue="0"/>
            <R4 DefaultValue="0"/>   <!-- 4th value only for quaternion / axis-angle -->
        </Rotation>
    </SCType>
</Matrix>
```

> You can also set the basis explicitly with `OrtX`/`OrtY`/`OrtZ` (the three axis
> vectors) and `Move` (the origin), but the two forms above are what you will use in
> practice.

### The 3D‑model matrix (`VisualProperties.VisMatrix`)

The node's matrix above defines its **kinematic** frame. The **3D model** attached
to the node (`ImageFile`, an `.osd` or `.stl`) is positioned by a *separate* matrix,
`VisMatrix`, inside `VisualProperties`. Use it to align an imported model with the
node frame without disturbing the kinematics:

```xml
<SCType ID="MyNode" type="TMachineNode">
    <ImageFile DefaultValue="Images\head.osd"/>
    <VisualProperties>
        <VisMatrix>
            <SCType ID="T1" type="TRotateZ" DefaultValue="180"/>
        </VisMatrix>
    </VisualProperties>
</SCType>
```

(Machine visualization is handled separately from kinematics; `VisMatrix` only
affects how the model is drawn.)

---

## 2 Switchable / detachable nodes

Real machines have interchangeable parts — turret blocks, attachable milling heads,
sub‑spindle adapters, chuck variants. Within the **machine‑scheme XML** there are
**two mechanisms** to model "a node that may or may not be present", with different
trade‑offs.

> **Scope.** This section covers only the two *XML‑scheme* mechanisms. Other kinds of
> detachable content are handled **at the project level by separate, non‑XML
> mechanisms** and are unrelated to the scheme described here — for example
> **fixtures** (workpiece tooling, stored in their own binary container together with
> 3D models) and **tool assemblies** (built in their own data structures and plugged
> into the machine's magazine connectors). Don't reach for `TCaseNode` or node hiding
> to model those.

### Mechanism A — `TCaseNode` (one branch loaded at parse time)

A node derived from `TCaseNode` holds several alternative child branches but exposes
an **`ActiveNode`** naming the one that is "in". When the machine descriptor is
parsed, **only the active branch is loaded** into the node tree; the others are
skipped entirely.

```xml
<SCType ID="HeadBlockSelector" type="TCaseNode">
    <ActiveNode DefaultValue="EmptyBlock"/>   <!-- which child branch to load -->
    <Parameters>
        <SCType ID="BlockNumber" type="Integer" DefaultValue="1"/>
    </Parameters>
    <SCType ID="EmptyBlock"  Caption="Empty"  type="TAbstractTurretHeadBlock"/>
    <SCType ID="DrillBlock"  Caption="Drill"  type="TTurretDrillToolHolder"/>
    <!-- ...more alternatives... -->
</SCType>
```

- **Pros:** inactive branches consume no memory — essential when a machine has many
  optional blocks (a turret with dozens of stations, a tool magazine, …).
- **Limit:** the active branch is chosen **once, at load/parse time**. A project owns
  a **single machine instance**, so you cannot switch the active block *during* the
  project — only initialize it at the start. This is the classic mechanism for
  **turrets** (see [§3](#3-turrets)).

`TCaseNode` carries an `ActiveNode` (the active child's ID) and an optional
`Parameters` block; both are skipped by the loader when it descends into the chosen
branch.

### Mechanism B — hiding inactive nodes (switchable at runtime)

Here **all** nodes are loaded, but a node is **shown/active only when it belongs to
the currently selected tool or workpiece connector**. Because nothing is unloaded,
the active block can change **mid‑project**. Three attributes drive it:

| Attribute | Type | A node carrying it is active only when… |
|---|---|---|
| `VisToolHolderID` | string | its value equals the **ID of the active tool connector** |
| `VisWorkpieceHolderID` | string | its value equals the **ID of the active workpiece connector** |
| `HideIfInactive` | bool | the node lies on the **branch of the active tool or workpiece** (a simpler switch than spelling out IDs) |

```xml
<!-- this adapter shows only when tool connector "Tool3" is active -->
<SCType ID="Adapter3" type="TMachineNode" VisToolHolderID="Tool3">
    ...
</SCType>

<!-- this branch shows only while it carries the active tool/workpiece -->
<SCType ID="OptionalHead" type="TMachineNode" HideIfInactive="True">
    ...
</SCType>
```

`HideIfInactive` is the easy equivalent of `VisToolHolderID` / `VisWorkpieceHolderID`
when you do not want to hard‑code connector IDs (which may change): instead of naming
IDs, you just flag the node, and it is active whenever it is an ancestor of the
current tool or workpiece connector.

### Which to use

| | `TCaseNode` (A) | Hiding (B) |
|---|---|---|
| Loaded into memory | active branch only | all branches |
| When the choice is made | once, at parse/load | any time, mid‑project |
| Memory for many options | low | higher |
| Typical use | turret blocks, large optional sets | attachable heads/adapters switched during work |

---

## 3 Turrets

A turret is the textbook use of [§1](#1-positioning-nodes-with-matrices)
(parametric matrices), [§2 Mechanism A](#mechanism-a--tcasenode-one-branch-loaded-at-parse-time)
(`TCaseNode` block selection) and **parametrization** (to keep node IDs unique across
identical blocks). The shipped templates are in
[`Machines/TurretTypes.xml`](../../Machines/TurretTypes.xml); some older machines
build a turret without the template but on the same principle (the template was added
later).

### The pieces

**1. The turret head — a rotary, indexed axis.** It holds a `TurretParameters`
block (prefix, station count, radius, the IDs of the linear axes the turret rides on,
rotation direction) and an indexed state parameter. `Scale` maps one index step to
`360 / BlocksCount` degrees:

```xml
<SCType ID="TAbstractTurretHead" Caption="Turret head" type="TMachineAxis">
    <ID            DefaultValue="[TurretParameters.Prefix]TurretHead"/>
    <ParameterName DefaultValue="[TurretParameters.Prefix]TurretAxisPos"/>
    <AxisType      DefaultValue="Rotary"/>
    <Scale         DefaultValue="360/[TurretParameters.BlocksCount]"/>
    <SCType ID="TurretParameters" Caption="Turret parameters" type="ComplexType">
        <SCType ID="Prefix"            type="String"  DefaultValue=""/>
        <SCType ID="BlocksCount"       type="Integer" DefaultValue="12"/>
        <SCType ID="Radius"            type="Double"  DefaultValue="120"/>
        <SCType ID="XAxisID"           type="String"  DefaultValue="[Prefix]AxisX"/>
        <SCType ID="ZAxisID"           type="String"  DefaultValue="[Prefix]AxisZ"/>
        <SCType ID="RotationDirection" type="Integer" DefaultValue="1"/>
    </SCType>
    <SCType ID="TurretAxisPos" type="TMachineStateParameter">
        <ID          DefaultValue="[TurretParameters.Prefix]TurretAxisPos"/>
        <Address     DefaultValue="[TurretParameters.Prefix]T"/>
        <AxisControl DefaultValue="Indexed"/>
        <Group       DefaultValue="RotaryAxis"/>
    </SCType>
</SCType>
```

**2. A block — placed on the head by a parametric matrix.** Each station is rotated
to its angular position and pushed out by the head radius
([§1, Way 1](#way-1--relative-to-the-parent-cs-a-series-of-moves-and-turns)):

```xml
<SCType ID="TAbstractTurretHeadBlock" Caption="Turret head block" type="TMachineNode">
    <Matrix>
        <SCType ID="T1" type="TTranslateX" DefaultValue="-[TurretParameters.Radius]"/>
        <SCType ID="T2" type="TRotateZ"
                DefaultValue="-[TurretParameters.RotationDirection]*360/[TurretParameters.BlocksCount]*([Parameters.BlockNumber]-1)"/>
    </Matrix>
</SCType>
```

**3. A tool holder on the block — with parametric, unique IDs.** Every block must
produce **unique** node IDs and tool numbers; parametrization off
`[Parameters.BlockNumber]` and `[TurretParameters.Prefix]` guarantees that:

```xml
<SCType ID="TTurretToolHolder" Caption="Tool holder" type="TToolHolderNode">
    <ID            DefaultValue="[TurretParameters.Prefix]Tool[Parameters.BlockNumber]"/>
    <ToolAxisID    DefaultValue="[TurretParameters.Prefix]TurretHead"/>
    <ToolAxisValue DefaultValue="[TurretParameters.RotationDirection]*([Parameters.BlockNumber]-1)"/>
    <ToolNumber    DefaultValue="[Parameters.BlockNumber]"/>
    <XAxisID       DefaultValue="[TurretParameters.XAxisID]"/>
    <ZAxisID       DefaultValue="[TurretParameters.ZAxisID]"/>
</SCType>
```

**4. The block selector — a `TCaseNode`.** Each station is a selector whose
`Parameters.BlockNumber` distinguishes it and whose `ActiveNode` picks the fitted
block type (empty, lathe cutter, driven drill, …). Only the active block per station
is loaded:

```xml
<SCType ID="TAbstractTurretHeadBlockSelector" type="TCaseNode">
    <ActiveNode DefaultValue="EmptyBlock"/>
    <Parameters>
        <SCType ID="BlockNumber" type="Integer" DefaultValue="1"/>
    </Parameters>
    <SCType ID="EmptyBlock" Caption="Empty" type="TAbstractTurretHeadBlock"/>
    <!-- concrete machine adds: lathe cutter holder, drill holder, ... as alternatives -->
</SCType>
```

### Why parametrization is essential here

A turret has many identical stations. If their nodes had fixed IDs they would
collide. By driving every `ID`, `ToolNumber`, `Address` and matrix offset from
`[Parameters.BlockNumber]` (per station) and `[TurretParameters.Prefix]` (per turret,
so two turrets on one machine don't clash), one template instantiates cleanly any
number of times. This is the same `[...]` expression language as everywhere else
(see [the expression language](../xml-properties/expression-language.md)); machine descriptors lean on it heavily.

> The chuck/jaw templates in the same file follow the identical pattern — a
> parametric `ChuckParameters` block and per‑jaw matrices driven by `[JawIndex]`.

### Putting it together — assembling a turret from the template

Now combine the template pieces into a complete, reusable turret. Everything derives
from the [`TurretTypes.xml`](../../Machines/TurretTypes.xml) types, so the head's step
angle, the block matrices and all IDs are produced automatically from the parameters.

**1. Define the machine's blocks** — each block derives from
`TAbstractTurretHeadBlock` (inheriting its radial/angular positioning matrix) and
holds the appropriate parametric holder:

```xml
<SCType ID="LatheCutterBlock" Caption="Lathe cutter holder" type="TAbstractTurretHeadBlock">
    <SCType ID="ToolHolder" type="TTurretLatheCutterHolder"/>
</SCType>
<SCType ID="DrivenDrillBlock" Caption="Driven drill holder" type="TAbstractTurretHeadBlock">
    <SCType ID="ToolHolder" type="TTurretDrillToolHolder"/>
</SCType>
```

> The holders above are the template's turret‑ready holders, also declared in
> [`TurretTypes.xml`](../../Machines/TurretTypes.xml): **`TTurretToolHolder`** (from
> the generic connector `TToolHolderNode`), **`TTurretLatheCutterHolder`** (from
> `TLatheCutterHolder`) and **`TTurretDrillToolHolder`** (from `TMillToolHolder`).
> Each one only *adds the parametric turret tool IDs* —
> `ID = [TurretParameters.Prefix]Tool[Parameters.BlockNumber]`, plus `ToolAxisID`,
> `ToolNumber` and the linked `XAxisID`/`YAxisID`/`ZAxisID` — on top of its connector
> type. That is what lets a block simply drop one in and inherit unique, prefixed
> names automatically.

**2. Define the machine's block selector** — derive it from the template selector
`TAbstractTurretHeadBlockSelector` (a `TCaseNode` that already provides `ActiveNode`,
`Parameters.BlockNumber` and an inherited `EmptyBlock` alternative) and add the blocks
this machine supports:

```xml
<SCType ID="TMyBlockSelector" Caption="Turret block selector" type="TAbstractTurretHeadBlockSelector">
    <SCType ID="LatheCutter" Caption="Lathe cutter" type="LatheCutterBlock"/>
    <SCType ID="DrivenDrill" Caption="Driven drill" type="DrivenDrillBlock"/>
    <!-- "EmptyBlock" is inherited from TAbstractTurretHeadBlockSelector -->
</SCType>
```

**3. Build the turret as a type** — derive it from `TAbstractTurretHead` (which gives
the rotary, indexed axis and computes `Scale = 360 / BlocksCount` for you), set its
`TurretParameters`, and hang the 12 station selectors. Each station's `BlockNumber`
makes its IDs unique; its `ActiveNode` says which block is fitted there:

```xml
<SCType ID="TMyTurret" Caption="Turret" type="TAbstractTurretHead">
    <TurretParameters>
        <BlocksCount DefaultValue="12"/>   <!-- head Scale becomes 360/12 = 30° -->
        <Radius      DefaultValue="120"/>
    </TurretParameters>

    <SCType ID="T1"  Caption="Position 1"  type="TMyBlockSelector">
        <ActiveNode DefaultValue="LatheCutter"/>   <!-- station 1: a lathe cutter -->
        <Parameters><BlockNumber DefaultValue="1"/></Parameters>
    </SCType>
    <SCType ID="T2"  Caption="Position 2"  type="TMyBlockSelector">
        <ActiveNode DefaultValue="DrivenDrill"/>   <!-- station 2: a driven drill -->
        <Parameters><BlockNumber DefaultValue="2"/></Parameters>
    </SCType>
    <SCType ID="T3"  Caption="Position 3"  type="TMyBlockSelector">
        <ActiveNode DefaultValue="EmptyBlock"/>    <!-- station 3: empty (inherited block) -->
        <Parameters><BlockNumber DefaultValue="3"/></Parameters>
    </SCType>

    <!-- ...stations T4 … T11, each a TMyBlockSelector with its own
         ActiveNode and BlockNumber = 4 … 11 ... -->

    <SCType ID="T12" Caption="Position 12" type="TMyBlockSelector">
        <ActiveNode DefaultValue="LatheCutter"/>
        <Parameters><BlockNumber DefaultValue="12"/></Parameters>
    </SCType>
</SCType>
```

That is the whole idea end‑to‑end:

- **One selector type** enumerates all possible blocks; **twelve instances** of it
  (`T1`…`T12`) are the physical stations on the head.
- Each station's **`ActiveNode`** picks the *one* block loaded there — the other
  alternatives cost no memory ([§2 A](#mechanism-a--tcasenode-one-branch-loaded-at-parse-time)).
- Each station's **`BlockNumber`**, together with the head's `TurretParameters`,
  parametrizes the block's matrix angle and its tool `ID`/`ToolNumber`, so the twelve
  identical stations produce twelve distinct, non‑colliding tools.
- The configuration is fixed when the machine is parsed; to re‑equip a station the
  user edits the machine, which is re‑loaded.

### Placing the turret(s) in the machine — why `Prefix` matters

`TMyTurret` is now a reusable type. Place it in the machine's `Schema` at the end of
the slide that carries it, so it moves with those axes. With a **single** turret you
can leave its `Prefix` empty:

```xml
<Schema>
    <SCType ID="AxisX" type="TToolAxisX">
        <SCType ID="AxisZ" type="TToolAxisZ">
            <SCType ID="Turret" Caption="Turret" type="TMyTurret"/>
        </SCType>
    </SCType>
</Schema>
```

But a lathe/turn‑mill may carry **two turrets** (upper/lower), and a machine is
loaded into a **single namespace**, so every node ID must be unique *within the
machine* ([how a machine is loaded](machine-descriptors.md#how-a-machine-descriptor-is-loaded)). Two copies
of `TMyTurret` would each emit `TurretHead`, `Tool1`…`Tool12`, `TurretAxisPos`, … — a
collision. This is exactly why `TAbstractTurretHead` parametrizes every generated name
with a **`Prefix`**: give each instance a different prefix and all its IDs become
unique:

```xml
<Schema>
    <!-- lower turret on the lower X/Z slide -->
    <SCType ID="LowerX" type="TMachineAxis"> <ParameterName DefaultValue="LowerAxisXPos"/>
      <SCType ID="LowerZ" type="TMachineAxis"> <ParameterName DefaultValue="LowerAxisZPos"/>
        <SCType ID="LowerTurret" Caption="Lower turret" type="TMyTurret">
            <TurretParameters>
                <Prefix  DefaultValue="Lower"/>   <!-- -> LowerTurretHead, LowerTool1, LowerTurretAxisPos -->
                <XAxisID DefaultValue="LowerX"/>
                <ZAxisID DefaultValue="LowerZ"/>
            </TurretParameters>
        </SCType>
      </SCType>
    </SCType>

    <!-- upper turret on its own slide -->
    <SCType ID="UpperX" type="TMachineAxis"> <ParameterName DefaultValue="UpperAxisXPos"/>
      <SCType ID="UpperZ" type="TMachineAxis"> <ParameterName DefaultValue="UpperAxisZPos"/>
        <SCType ID="UpperTurret" Caption="Upper turret" type="TMyTurret">
            <TurretParameters>
                <Prefix  DefaultValue="Upper"/>   <!-- -> UpperTurretHead, UpperTool1, UpperTurretAxisPos -->
                <XAxisID DefaultValue="UpperX"/>
                <ZAxisID DefaultValue="UpperZ"/>
            </TurretParameters>
        </SCType>
      </SCType>
    </SCType>
</Schema>
```

Each instance reuses the same `TMyTurret` definition (all 12 stations and their
blocks) but, thanks to its distinct `Prefix`, produces its own non‑colliding IDs —
`LowerTurretHead` / `LowerTool1…` vs `UpperTurretHead` / `UpperTool1…` — and references
its own slide axes through the parametrized `XAxisID` / `ZAxisID`. (The single‑turret
case can leave `Prefix` empty.) On multi‑channel machines the two turrets typically
also sit on different `Channel`s — see [§6](#6-control-channels-simultaneous-work).

---

## 4 Tool connectors — positioning axes and activation

A connector is where a tool or the workpiece attaches to the kinematic chain — the
*Tool connector* (`TToolHolderNode`) and *Workpiece connector* (`TWorkpieceHolderNode`)
of the UI (see [building blocks](machine-descriptors.md#the-building-blocks)). Both derive
from a common socket and so share the spindle/clamping properties in
[Spindle and clamping](#spindle-and-clamping-shared-by-both-connectors). On **machines**
(not robots) a **tool** connector additionally carries the properties that tell the
kinematics solver how its tool moves and how it is selected.

> The connectors' **complete property tables** are gathered in the
> [node reference → Tool and workpiece connectors](node-reference.md#tool-and-workpiece-connectors);
> this section explains the *behaviour* behind those properties.

### Positioning axes and the base CS — `XAxisID` / `YAxisID` / `ZAxisID`

`XAxisID`, `YAxisID`, `ZAxisID` name the machine axes that **position this tool's tip
in space**. They give the solver a usable chain *even without an explicit
sub‑machine* ([§5](#5-sub-machines-alternating-work)) — in effect each connector
already describes a small "virtual sub‑machine". They also define that chain's **base
coordinate system**.

Explicit sub‑machines later added `OriginG54BaseNode` / `OriginG54` to set this base
CS directly. When those are not given, the base CS is derived:

- its **origin** coincides with the machine bed's **world CS origin**;
- its **axis directions** come from the **travel directions** of `XAxisID` /
  `YAxisID` / `ZAxisID`.

The result **must be a right‑handed triple**, so set the axes' travel directions
carefully. The **branch** an axis sits in matters:

- an axis in the **tool‑moving** branch contributes its travel direction **directly**
  (positive);
- an axis in the **workpiece‑moving** branch contributes the **opposite** direction
  (negative) — moving the part one way is equivalent to moving the tool the other way.

A negative axis `Scale` ([node reference](node-reference.md#tmachineaxis)) flips a travel
direction too, so it also affects this base CS.

### Making a connector active — `ToolAxisID` / `ToolAxisValue`

This is the core mechanism behind **tool magazines in general and turrets in
particular**. A connector states: *to make the tool in this connector active, move the
axis `ToolAxisID` to the value `ToolAxisValue`.* It works for **rotary** magazines (a
turret indexes to a station angle) and **linear** ones (a magazine slides to a
position) alike.

```xml
<SCType ID="Tool5" type="TMillToolHolder">
    <ToolAxisID    DefaultValue="TurretHead"/>   <!-- axis that indexes the magazine -->
    <ToolAxisValue DefaultValue="4"/>            <!-- value that brings this station in -->
    <ToolNumber    DefaultValue="5"/>
</SCType>
```

In the [turret template](#3-turrets) these are parametric —
`ToolAxisID = [TurretParameters.Prefix]TurretHead` and
`ToolAxisValue = [TurretParameters.RotationDirection]*([Parameters.BlockNumber]-1)` —
so every station automatically points at the turret axis and its own index.

> **`ToolAxisID` can be omitted.** When an active sub‑machine
> ([§5](#5-sub-machines-alternating-work)) defines a tool axis, the system uses
> *that*; it falls back to the connector's own `ToolAxisID` only when the sub‑machine
> has none. So a connector may leave `ToolAxisID` empty and let the active sub‑machine
> supply it.

### Tool number and supported applications

- **`ToolNumber`** — the **magazine position** of this connector, commonly known as the
  **tool number**; it is what the postprocessor outputs in the NC program. In the
  turret template it is parametrized to the station index. If it is left at `0` (not
  set), the connector number is **not** used and the NC program instead outputs the
  number taken from the **cutting tool's own properties**.
- **`SupportedToolTypes`** (*Supported applications*) — the kinds of machining a tool
  fitted in this connector can perform: `MillTool` (milling), `LatheCutter` (lathe
  cutting), `JetCutter` (jet cutting), `Punch`, `Wire` (wire EDM), `Cutter6D` (6D
  cutting), `Welder` (welding), `AdditiveTool` (additive), `Painter` (spray painting),
  `HeatTreatment`, `Gripper` (gripping). The system uses this set to **filter the lists
  of operations and tools** offered for the connector down to those its applications
  support.
- **`Channel`** — the control channel this connector belongs to
  ([§6](#6-control-channels-simultaneous-work)).
- **`ToolChangeTimeCalcLawIndex`** — index of the tool‑change‑time law (defined in the
  machine's *Tool Change* section) that applies to this connector (`0` = the default
  law).

### Spindle and clamping (shared by both connectors)

Because tool and workpiece connectors derive from the same socket, these apply to
**both**:

- **`SpindleParamID`** — the ID of the **machine state parameter**
  ([machine state parameters](machine-descriptors.md#machine-state-parameters)) that drives the rotary
  **spindle** axis spinning the tool or the part. It is the *state‑parameter* ID, not
  the axis node's `ID`.
- **`HolderType`** — `Unknown`, `LeftLatheSpindle` or `RightLatheSpindle`; marks a lathe
  spindle socket.
- **`DefaultClampID`** — the default clamp id of this socket, referenced by
  part‑handoff / takeover operations; it defaults from `HolderType` (left spindle →
  `1`, right → `2`, otherwise `-1`).

### Workpiece connectors

A **workpiece connector** (`TWorkpieceHolderNode`) holds the **part** (on a chuck,
spindle or fixture) and carries only the shared spindle/clamping properties above — none
of the tool‑specific positioning, activation or `ToolNumber` / `SupportedToolTypes`
fields, which describe how a *tool* is positioned and selected and do not apply to a part
holder. Its full property list and the **placement caveat** (the node `Matrix` is
ignored — a workpiece connector always takes its parent node's placement) are in the
[node reference → Workpiece connector](node-reference.md#workpiece-connector-tworkpieceholdernode).

---

## 5 Sub-machines (alternating work)

> **Channels vs. sub‑machines — the key difference.** *Channels*
> ([§6](#6-control-channels-simultaneous-work)) describe parts of a machine that
> work **simultaneously**. *Sub‑machines* describe alternative kinematic chains used
> **one at a time** (alternately) — they decide *which* axes drive a tool. They occur
> even on **single‑channel** machines, so they are a separate concept.

The inverse‑kinematics (IK) solver works with a **fixed‑shape chain**: three linear
axes plus **two** rotary axes (`X Y Z` + `RotaryAxis1` + `RotaryAxis2`). When a
machine's node tree offers *more* than that — extra rotary axes, or several
tool/workpiece branches (spindles, turrets) — the chain is **redundant** and the
solver cannot choose. A **sub‑machine** removes the ambiguity by naming the **active
branch**: the tool node, the workpiece node, and exactly which linear and rotary axes
participate.

### The canonical example — a 6‑axis mill (XYZ + ABC)

A common machining centre has linear `X Y Z` plus **three** rotary axes `A`, `B`, `C`
— but the IK solver only ever drives two rotaries. Three rotaries are redundant. You
resolve it by declaring **two sub‑machines**, each pinning a usable *XYZ + two‑rotary*
chain:

- `XYZ + A + C`
- `XYZ + B + C`

The operation (or the user) then picks which sub‑machine to use for a given job. Use
the `SubMachine5x` variant, which adds the two rotary‑axis fields:

```xml
<SubMachinesList>
    <SCType ID="XYZ_AC" Caption="A + C" type="SubMachine5x">
        <ToolNode DefaultValue="Spindle"/>   <!-- node carrying the tool -->
        <WrkNode  DefaultValue="Table"/>      <!-- node carrying the part -->
        <XAxisID  DefaultValue="AxisX"/>
        <YAxisID  DefaultValue="AxisY"/>
        <ZAxisID  DefaultValue="AxisZ"/>
        <R1AxisID DefaultValue="AxisA"/>      <!-- first rotary  -->
        <R2AxisID DefaultValue="AxisC"/>      <!-- second rotary -->
    </SCType>
    <SCType ID="XYZ_BC" Caption="B + C" type="SubMachine5x">
        <ToolNode DefaultValue="Spindle"/>
        <WrkNode  DefaultValue="Table"/>
        <XAxisID  DefaultValue="AxisX"/>
        <YAxisID  DefaultValue="AxisY"/>
        <ZAxisID  DefaultValue="AxisZ"/>
        <R1AxisID DefaultValue="AxisB"/>
        <R2AxisID DefaultValue="AxisC"/>
    </SCType>
</SubMachinesList>
```

Each sub‑machine is one solvable XYZ + 2‑rotary chain; together they cover the whole
6‑axis machine without ever asking the solver to handle three rotaries at once. This
machine is **single‑channel** — sub‑machines are needed regardless of channels.

### A second example — twin‑spindle / twin‑turret mill‑turn

A very common mill‑turn centre has **two tool carriers** (an upper and a lower turret)
and **two part carriers** (a left and a right spindle). Any turret can machine the part
held by either spindle, so the usable **tool + workpiece** pairings are enumerated as
sub‑machines — plus one extra entry for spindle‑to‑spindle work:

- **SubMachine 1** — UpperTurret → LeftSpindle
- **SubMachine 2** — UpperTurret → RightSpindle
- **SubMachine 3** — LowerTurret → LeftSpindle
- **SubMachine 4** — LowerTurret → RightSpindle
- **SubMachine 5** — RightSpindle *as the tool holder* → LeftSpindle *as the workpiece
  holder* — for axial drilling or pick‑and‑place / part transfer between the two spindles.

```xml
<SubMachinesList>
    <SCType ID="UpperOnLeft" Caption="Upper turret → Left spindle" type="SubMachine">
        <ToolNode   DefaultValue="UpperTurret"/>   <!-- the turret HEAD, not a single holder -->
        <WrkNode    DefaultValue="LeftSpindle"/>    <!-- the spindle node that holds the part -->
        <XAxisID    DefaultValue="UpperX"/>
        <ZAxisID    DefaultValue="UpperZ"/>
        <ToolAxisID DefaultValue="UpperTurret"/>    <!-- the turret indexing axis -->
        <Channel    DefaultValue="0"/>
    </SCType>
    <!-- ...UpperOnRight, LowerOnLeft, LowerOnRight — the other turret×spindle pairs... -->
    <SCType ID="RightToLeft" Caption="Right spindle → Left spindle" type="SubMachine">
        <ToolNode DefaultValue="RightSpindle"/>   <!-- the right spindle acts as the tool carrier -->
        <WrkNode  DefaultValue="LeftSpindle"/>     <!-- the left spindle holds the part -->
    </SCType>
</SubMachinesList>
```

> **`ToolNode` / `WrkNode` name a *carrier* node, not a single holder.** Give the
> **nearest common parent** of the holders involved — the **turret head** (parent of
> all its tool holders) or the **spindle** node — *not* an individual
> `TToolHolderNode` / `TWorkpieceHolderNode`. That is the whole point of (real)
> sub‑machines: the branch's axes (`XAxisID` / `ZAxisID` / `ToolAxisID`) are stated
> **once, on the sub‑machine**, instead of being repeated on every tool holder as the
> older "virtual sub‑machine" (the connector `XAxisID`… of
> [§4](#4-tool-connectors--positioning-axes-and-activation)) required. See the
> shipped `Machines\LatheMilling\MultiChannel\Puma MX2100ST\DOOSAN_PUMA_MX2100ST.xml`
> for a full real list (e.g. `ToolNode=AxisT` for the turret, `WrkNode=AxisC` for the
> spindle).

So each entry names **which carrier holds the tool and which holds the part**, giving
the solver one unambiguous pair; the operator (or operation) picks the active
sub‑machine. The last entry shows that a **spindle itself can be the tool carrier** —
e.g. the counter‑spindle pushing the part onto a fixed drill, or taking the part over
from the main spindle. Where the XYZ+ABC case used sub‑machines to resolve **redundant
rotary axes**, this case uses them to choose **which of several tool/workpiece carriers**
form the active pair.

### Declaration and fields

Sub‑machines are listed in the machine's **`SubMachinesList`**; each entry is a
`SubMachine` or a variant (the older array form `SubMachines` is obsolete).

| Field | Meaning |
|---|---|
| `ToolNode` / `WrkNode` | The tool‑carrying and workpiece‑carrying **carrier** nodes (the nearest common parent of the holders — a turret head, a spindle), **not** an individual holder. |
| `XAxisID` / `YAxisID` / `ZAxisID` | The linear axes of this chain. |
| `ToolAxisID` | The tool / spindle axis. |
| `OriginG54BaseNode` | The node the sub‑machine's base coordinate system is anchored to. |
| `OriginG54` | An arbitrary **orientation** (transform) for that base CS — commonly used on **counter‑spindle** machines, where the base‑CS **Z must be inverted**. |
| `ApproachRule` / `ReturnRule` | The general approach / return rule for this branch (see below). |
| `DetailedApproachRules` / `DetailedReturnRules` | Per‑machining‑mode variants of those rules, chosen automatically by operation type (see below). |
| `Channel` | The channel this sub‑machine belongs to — relevant only on multi‑channel machines ([§6](#6-control-channels-simultaneous-work)). |

**Sub‑machine types.** Which `SubMachine` type you use depends on the **kinematics
solver** the branch needs, or on extra options specific to a kind of equipment. The
plain `SubMachine` carries the common fields above; specialized types add the fields
their solver requires. The set is **open and will grow** over time; at present two
specializations exist beyond the base:

- **`SubMachine5x`** — for **5‑axis** machines. Adds `R1AxisID` / `R2AxisID`, the two
  rotary axes the 5‑axis solver drives (used in the XYZ+ABC example above).
- **`TrevisanSubMachine`** — for machines with a **U‑axis turning** function (the
  typical representatives are Trevisan‑style machines). Adds the radial `UAxisID`.

### Approach and return rules

`ApproachRule` / `ReturnRule` (and their detailed forms) describe **how the machine
moves between the tool‑change point and the toolpath body** for this sub‑machine: the
**approach** rule from the tool‑change position to the *start* of the operation's
toolpath, and the **return** rule from its *end* back to the tool‑change position.

A rule is an ordered sequence of axis moves, written as groups separated by `;` that
execute in turn; letters grouped together move together, and `Axis(value)` moves an
axis to a given value. For example `ApproachRule = "BC; Y Z(10); X"` means: first turn
**B and C**, then move **Y** and **Z** (to 10), then move **X** in.

A step can also be a **command token** rather than an axis move. In particular **`LCS`**
switches the **local coordinate system** on or off at that point in the sequence — or,
for the relevant 5‑axis machining type, the **TCPM** mode — as seen in the `MillLCS` /
`MillTCPM` variants below (`BC;Z;X;LCS;XY;Z`).

- **`ApproachRule` / `ReturnRule`** give a **single general** rule.
- **`DetailedApproachRules` / `DetailedReturnRules`** give **per‑machining‑mode**
  variants, so the right rule is selected **automatically** from the current
  operation's type:
  - `TurnRadial` / `TurnAxial` — radial / axial **turning**;
  - `MillRadial` / `MillAxial` — radial / axial ordinary **3‑axis milling**;
  - `MillLCS` — **indexed** 5‑axis machining (local CS);
  - `MillTCPM` — **continuous** 5‑axis machining (TCPM).

```xml
<SCType ID="MainMill" type="SubMachine">
    ...
    <ApproachRule DefaultValue="BC; Y Z(10); X"/>
    <ReturnRule   DefaultValue="Z(10); X; Z"/>
    <DetailedApproachRules>
        <TurnRadial DefaultValue="BS;Z;X"/>
        <TurnAxial  DefaultValue="BS;Z(10);X;"/>
        <MillRadial DefaultValue="BC;Z;X"/>
        <MillAxial  DefaultValue="BC;Z;X"/>
        <MillLCS    DefaultValue="BC;Z;X;LCS;XY;Z"/>
        <MillTCPM   DefaultValue="BC;Z;X;LCS;XY;Z"/>
    </DetailedApproachRules>
    <DetailedReturnRules> ... </DetailedReturnRules>
</SCType>
```
*(real example: `Machines\LatheMilling\MultiChannel\Puma MX2100ST\DOOSAN_PUMA_MX2100ST.xml`)*

Pick the type that matches the branch's kinematics; a single machine can mix types
across its sub‑machines.

## 6 Control channels (simultaneous work)

A **channel** is an independent stream of motion/NC code that runs **at the same
time** as the others. On a multi‑channel machine (twin‑spindle / multi‑turret lathes,
turn‑mill centres, Swiss‑type lathes) different nodes, axes and state parameters
belong to **different channels**, and some axes are **shared**. You assign membership
with the integer **`Channel`** member on the relevant nodes/axes/state‑parameters
(and `ChannelWorkpiece` where the workpiece side differs):

```xml
<MachineStateParameters>
    <SCType ID="AxisX1Pos" type="TMachineStateParameter"><Channel DefaultValue="0"/> ... </SCType>
    <SCType ID="AxisX2Pos" type="TMachineStateParameter"><Channel DefaultValue="1"/> ... </SCType>
</MachineStateParameters>
```

`Channel="0"` and `Channel="1"` put the two cross‑slides on separate channels; an
axis left on the common channel is shared. Multi‑channel machines are **not** only
Swiss‑type — see the shipped examples under
`$(SCHEMAS_FOLDER)\LatheMilling\MultiChannel` (e.g. *IndexG160*, *Puma MX2100ST*,
*PumaTT2000SY*). [`SwissTemplate.xml`](../../Machines/SwissTemplate.xml) is one common,
ready‑made special case (a 2‑channel Swiss lathe) that also shows turret/adapter
`TCaseNode` selectors in context; shipped machines built on it — for example the
Hanwha Swiss‑type lathes under `$(SCHEMAS_FOLDER)\LatheMilling\SwissType` — are real
examples of that template in use.

> **In short:** *channels* run **simultaneously** and say *which independent stream* a
> node belongs to; *sub‑machines* are used **alternately** and say *which subset of
> nodes/axes forms one solvable tool+workpiece chain*. A single‑channel machine can
> still need sub‑machines (the XYZ+ABC mill above); a multi‑channel turn‑mill uses
> both — sub‑machines within each channel.

---

Back to **[Machine descriptors](machine-descriptors.md)** | [guide index](readme-machines.md)
