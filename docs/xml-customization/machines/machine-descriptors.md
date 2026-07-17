# Machine descriptors

A machine descriptor is, like an operation, a large `ComplexType` — but its most
distinctive part is the **kinematic scheme**: a nested tree of axes and holders that
describes how the machine moves. This chapter walks through a machine descriptor from
the **outside in**: the files it is made of, a complete simple example, the idea of the
kinematic chain, and then each section in turn. For the exhaustive property list of each
node type, it points you to the **[machine node reference](node-reference.md)**.

> **Most machines are built with MachineMaker, not by hand.** A dedicated
> application, **MachineMaker**, lets you create a machine *interactively*: for the
> common kinematic‑scheme types it produces the descriptor for you, with no manual
> XML editing. Reserve hand‑written XML (and manually prepared 3D models) for
> special, complex or unusual machines that fall outside what MachineMaker covers.
> This chapter documents that manual path — but if MachineMaker can build your
> machine, prefer it.

> **Companion pages for machines** — read alongside this chapter:
> - **[Machine node reference](node-reference.md)** — the full property tables for
>   every node type (`TMachineNode`, `TMachineAxis`, connectors, state parameters,
>   `VisualProperties`) plus coordinate conventions and units.
> - **[Machine Setup parameters reference](machine-setup-parameters.md)** —
>   what every parameter on the machine's *Control Parameters* tab does (arcs,
>   singularities, rotary transformations, 5‑axis compensation, tool change,
>   simulation, …), each with the XML fragment that overrides it.
> - **[Advanced machine topics](advanced-topics.md)** — node
>   matrices, switchable/detachable nodes, turrets, tool/workpiece connectors, and
>   control channels & sub‑machines.
> - **[3D models for machines](3d-models.md)** — preparing,
>   referencing and aligning the node geometry (`.osd` / `.stl`).

## A machine is a folder of files

A machine is not a single object buried in the application — it is a small set of files
you can point at:

- **the descriptor** — one `.xml` file that *is* the machine: its identity, control
  parameters and kinematic scheme;
- **its 3D models** — the `.osd` / `.stl` geometry the descriptor references through
  `ImageFile` (per node) and the `Image` / `Icon` header members, conventionally kept in
  an `Images\` subfolder beside the descriptor (see
  [3D models for machines](3d-models.md));
- optionally **machine defaults** (`*.usrdef`) that tweak shipped machines.

The shipped files under `Machines\` are your reference. They define the machine **type
library** — the abstract machines and the building‑block types every machine is
assembled from — loaded via
[`Machines/MachinesConfig.xml`](../../Machines/MachinesConfig.xml) into the **`Machines`**
namespace. The two you will read most are
[`Machines/AbstractMachine.xml`](../../Machines/AbstractMachine.xml) (the common base
every machine derives from) and
[`Machines/MachineTypes.xml`](../../Machines/MachineTypes.xml) (the node, axis, holder and
parameter types).

A *concrete* machine, by contrast, is an **individual file** loaded on its own
([below](#how-a-machine-descriptor-is-loaded)). As with operations, you do **not** edit
`Supplement`: a custom machine is an individual file in the scanned machine folders
(`$(SCHEMAS_FOLDER)` / `$(CUSTOM_SCHEMAS_FOLDER)`), normally produced by the
machine‑building tools
(see [§7](../xml-properties/framework-overview.md#7-where-your-custom-files-go)). This
chapter explains the descriptor syntax those machines are built from.

## How a machine descriptor is loaded

Machines are loaded differently from operations, and the difference shapes how you
author them.

- **The type library loads once.** [`MachinesConfig.xml`](../../Machines/MachinesConfig.xml)
  loads the shared machine **type library** — the abstract machines, and the node,
  axis, holder and parameter building blocks ([below](#the-building-blocks)).
  This is common to every machine.
- **Each machine loads in isolation.** A concrete machine is its own XML file.
  When the system needs a particular machine, it builds a *fresh* `Machines`
  namespace on top of the shared type library, includes **that one machine file**,
  and then applies the machine defaults
  ([`Machines/MachinesDefaults.xml`](../../Machines/MachinesDefaults.xml), which
  pulls in any `*.usrdef`). Each machine gets its own private namespace.
- **Identifiers are local to one machine.** Because machines never share a
  namespace, two different machine files may safely reuse the same `SCType` `ID`s.
  You do not need globally‑unique member names — only names unique *within* your
  machine.
- **The library is lazy.** Installations can hold **thousands** of machines, so the
  machine library only *scans* the predefined machine folders for lightweight
  metadata (enough to list and search them) and fully loads a machine's descriptor
  only when that machine is actually opened. Keep this in mind: a machine file is
  parsed on demand, in isolation, not all‑at‑once at startup.

The practical consequence for authoring: your machine file is a self‑contained
`<SCCollection>` in the `Machines` namespace that derives from a library type and
overrides/extends it. It lives in a scanned machine folder, not in `Supplement`.

## The building blocks

[`MachineTypes.xml`](../../Machines/MachineTypes.xml) defines the reusable types a
machine is assembled from. There are only a handful to know; the
**[node reference](node-reference.md)** lists every property of each.

| Type | Role |
|---|---|
| `TMachineNode` | Base for anything in the scheme tree — a *rigid* part (bed, column, table). Has an `ID`, a transform `Matrix`, visual properties and an optional `ImageFile` (`.osd`/`.stl` geometry). |
| `TMachineAxis` | A node that **moves**: `AxisType` (`Linear`/`Rotary`), a `Direction` (linear axes only), `Scale`, `RapidFeed`, and a `ParameterName` linking it to a state parameter. |
| `TMachineStateParameter` | The controllable **value** an axis is driven by (a position, a spindle, …): `Address`, limits, control mode. Not a scheme node — axes link to it by name. |
| `TToolHolderNode` / `TWorkpieceHolderNode` | The sockets that carry the tool / the workpiece, with `SupportedToolTypes`. Specializations: `TMillToolHolder`, `TLatheCutterHolder`, `TJetCutterHolder`, … |

> **Naming note.** The type IDs `TToolHolderNode` and `TWorkpieceHolderNode` appear
> in the **user interface** as **"Tool connector"** and **"Workpiece connector"**.
> They are the same thing — the socket where the tool, respectively the workpiece,
> attaches to the kinematic chain.

A few predefined axis and state‑parameter types also exist (`TToolAxisX/Y/Z`,
`TLatheSpindle`, `TRotaryTable`, `TAxisXPosition`, …), but they are **legacy and
optional**: introduced early to save typing through inheritance, they save little and
force you to chase down which defaults they hide. **Prefer declaring axes and
parameters explicitly** from `TMachineAxis` / `TMachineStateParameter`, so the values
that matter are visible right in your machine file. (Template types such as the turret
ones in [§3](advanced-topics.md#3-turrets) are the exception — there
inheritance genuinely pays off.)

## A complete simple machine

Concrete machines derive from `AbstractMachine` (or a closer base like
`AbstractMillMachine`), which already provides every section a machine has:

| Section | Contents |
|---|---|
| `DescriptionPlaceHolder` | Identity & metadata: `Name`, `Comment`, `Group`, `Developer`, `NCSystem`, postprocessor file (`SPPFile`), interpreter file, measurements system. |
| `ControlData` | Control/behaviour parameters: arc support, rotary transformations, 5‑axis compensation, local CS (ORIGIN) handling, tool‑frame output format. |
| `MachineStateParameters` | The list of controllable parameters (the axes' state). |
| `Schema` | The kinematic tree itself. |
| `Coolants` | Available coolant tubes. |
| `Simulation` | Simulation method/resolution and collision settings. |
| `ToolChange` | Tool‑change position, timing and output mode. |
| `MachineDimensions` | A tidy place to collect the scheme's key **defining parameters**. |

The two sections you author for almost every machine are `MachineStateParameters` (the
values the controller drives) and `Schema` (the geometry that moves with them). Here is a
complete small 3‑axis mill in which the **table traverses in X** while the **tool head
carries Y and Z** — a common bed‑type layout, and a good illustration that *both*
branches can move:

```xml
<MachineStateParameters>
    <SCType ID="AxisXPos" Caption="X" type="TMachineStateParameter">
        <Address DefaultValue="X"/><Group DefaultValue="LinearAxis"/>
        <Min DefaultValue="-300"/><Max DefaultValue="300"/>
    </SCType>
    <SCType ID="AxisYPos" Caption="Y" type="TMachineStateParameter">
        <Address DefaultValue="Y"/><Group DefaultValue="LinearAxis"/>
        <Min DefaultValue="-200"/><Max DefaultValue="200"/>
    </SCType>
    <SCType ID="AxisZPos" Caption="Z" type="TMachineStateParameter">
        <Address DefaultValue="Z"/><Group DefaultValue="LinearAxis"/>
        <Min DefaultValue="0"/><Max DefaultValue="400"/><InitialValue DefaultValue="400"/>
    </SCType>
    <SCType ID="SpindlePos" Caption="Spindle" type="TMachineStateParameter">
        <Address DefaultValue="S"/><Group DefaultValue="RotaryAxis"/><AxisControl DefaultValue="Manual"/>
    </SCType>
</MachineStateParameters>

<Schema>
    <SCType ID="Base" Caption="Bed" type="TMachineNode" IsFloor="True">
        <ImageFile DefaultValue="Images\bed.osd"/>

        <!-- TOOL branch: Y carries Z carries the spindle carries the tool -->
        <SCType ID="AxisY" Caption="Axis Y" type="TMachineAxis">
            <ParameterName DefaultValue="AxisYPos"/>
            <AxisType DefaultValue="Linear"/>
            <Direction><X DefaultValue="0"/><Y DefaultValue="1"/><Z DefaultValue="0"/></Direction>
            <SCType ID="AxisZ" Caption="Axis Z" type="TMachineAxis">
                <ParameterName DefaultValue="AxisZPos"/>
                <AxisType DefaultValue="Linear"/>
                <Direction><X DefaultValue="0"/><Y DefaultValue="0"/><Z DefaultValue="1"/></Direction>
                <SCType ID="Spindle" Caption="Spindle" type="TMachineAxis">
                    <ParameterName DefaultValue="SpindlePos"/>
                    <AxisType DefaultValue="Rotary"/>
                    <SCType ID="Tool" Caption="Tool" type="TMillToolHolder">
                        <SpindleParamID DefaultValue="SpindlePos"/>
                    </SCType>
                </SCType>
            </SCType>
        </SCType>

        <!-- WORKPIECE branch: the table traverses in X (physically -X, see the note below) -->
        <SCType ID="AxisX" Caption="Axis X" type="TMachineAxis">
            <ParameterName DefaultValue="AxisXPos"/>
            <AxisType DefaultValue="Linear"/>
            <Direction><X DefaultValue="-1"/><Y DefaultValue="0"/><Z DefaultValue="0"/></Direction>
            <SCType ID="Table" Caption="Table" type="TMachineNode">
                <ImageFile DefaultValue="Images\table.osd"/>
                <SCType ID="Workpiece" Caption="Workpiece" type="TWorkpieceHolderNode"/>
            </SCType>
        </SCType>
    </SCType>
</Schema>
```

Reading this tree: the **bed** is the fixed base (`IsFloor="True"`, see
[the kinematic scheme](#the-kinematic-scheme)). Its **tool branch** is Y → Z → spindle →
tool holder: move Y and everything below it moves, and the leaf `TMillToolHolder` is
where the cutting tool attaches. Its **workpiece branch** is X → table → workpiece: the
X axis carries the table, and the `TWorkpieceHolderNode` on the table is where the part
is held. These two leaves are the *Tool connector* / *Workpiece connector* of the UI.
Each moving node names the state parameter that drives it through `ParameterName`, and
all four parameters are declared in `MachineStateParameters`.

> Note the X axis's `Direction` of **(−1, 0, 0)**. It sits in the **workpiece** branch,
> so its `Direction` is the *table's* physical travel — world **−X**. Moving the part in
> −X is equivalent to moving the tool in +X, so this produces the conventional machine X
> with a right‑handed axis triple. (A tool‑branch axis, by contrast, uses its travel
> direction directly.) This workpiece‑branch sign rule is detailed in
> [§4](advanced-topics.md#4-tool-connectors--positioning-axes-and-activation).

The rest of this chapter walks each section in turn.

## Identity and metadata

`AbstractMachine` carries the header members every machine needs — `GUID`, `Priority`,
`Name`, `Comment`, `Group`, `Image`, `Icon` — and the `DescriptionPlaceHolder` identity
fields (`Developer`, `NCSystem`, postprocessor `SPPFile`, interpreter file, and the
**Measurements** system that fixes the machine's units). A derived machine overrides
these the same way an operation does:

```xml
<SCType ID="AbstractMillMachine" Caption="Abstract Mill Machine" type="AbstractMachine">
    <GUID     DefaultValue="{FA164E91-DF7D-474B-B335-8EE7F2C34E41}"/>
    <Priority DefaultValue="1000"/>
    <Group    DefaultValue="Milling"/>
    ...
</SCType>
```
*(real example: [`Machines/AbstractMachine.xml`](../../Machines/AbstractMachine.xml))*

`Group` is a `TMachineGroup` enum: `Milling`, `Lathe`, `LatheMilling`,
`JetCutter`, `WireEDM`, `Robot`, `Unknown`.

The **Measurements** system (metric vs. imperial) fixes the units of every `Matrix`
translation and all referenced geometry — see
[Coordinate conventions and units](node-reference.md#coordinate-conventions-and-units).

## Control parameters

`ControlData` is a deep section of switches that tell the engine and
postprocessor what the machine can do. You typically override only the parts
relevant to your machine. **Every one of these parameters is explained in detail —
with the XML fragment that overrides it — in
[Machine Setup parameters reference](machine-setup-parameters.md);** this
section is just an overview of what lives there:

- **Arcs** — whether arc output is allowed and in which planes, min length, max
  radius, spatial arcs.
- **Rotary transformations** — polar/cylindrical interpolation availability,
  TCPM support and defaults.
- **5‑axis compensation** — tool‑tip / workpiece‑zero / coordinate‑system
  compensation for indexed and continuous modes.
- **Local CS (ORIGIN)** — how G54‑style origins behave.
- **Tool‑frame output** — the rotation/orientation format the postprocessor
  expects (normal vector, quaternion, Euler variants, …).

Many of these defaults are computed with the expression language so they stay
consistent — for instance the rotation sequence derived from the chosen
tool‑frame format via a large `SWITCH` (see
[§5](../xml-properties/expression-language.md#5-functions)).

## Machine state parameters

`MachineStateParameters` lists the quantities the controller drives. You add them
by overriding the inherited section and declaring members of `TMachineStateParameter`
(or a predefined specialization):

```xml
<MachineStateParameters>
    <SCType ID="AxisXPos" type="TAxisXPosition"/>
    <SCType ID="AxisYPos" type="TAxisYPosition"/>
    <SCType ID="AxisZPos" type="TAxisZPosition">
        <InitialValue DefaultValue="100"/>
    </SCType>
    <SCType ID="AxisSPos" Caption="Spindle Position" type="TMachineStateParameter">
        <Address  DefaultValue="S"/>
        <Group    DefaultValue="RotaryAxis"/>
        <Priority DefaultValue="1"/>
        <Order    DefaultValue="4"/>
    </SCType>
</MachineStateParameters>
```
*(real example: [`Machines/AbstractMachine.xml`](../../Machines/AbstractMachine.xml))*

The properties you set most often are `Address`, `Group`, and `Min`/`Max`/`Incr`; a few
others control simulation and tool‑change behaviour (`AxisControl`, `HasBrake`,
`SupportShortestPathRotation`, `DesignTimeValue`, `ControlWithMap`, …). The **complete
property table, with notes on each**, is in the
[node reference → `TMachineStateParameter`](node-reference.md#tmachinestateparameter).

### Two places to declare a state parameter

A `TMachineStateParameter` may be declared in **either** of two places:

- in the **global `MachineStateParameters` section** (as above), or
- **inside the description of a node or axis** in the `Schema`.

Declaring it on a node is what enables **switchable (optional) nodes**: when a node
can be present or absent, its state parameter travels with it. The contents of
`MachineStateParameters` are then composed **dynamically** — parameters appear or
disappear according to which nodes are actually loaded for the current machine
configuration. Put a parameter in the global section when it always exists; put it
on the node when it should come and go with that node.

## The kinematic scheme

`Schema` is where the machine's geometry comes alive. It is a **tree of nodes
nested by containment**: a child node sits on, and moves with, its parent. The
nesting *is* the kinematic chain. A scheme always has **two branches off the base** —
one that carries the **tool** and one that holds the **workpiece** — and both are
mandatory (see the [complete example](#a-complete-simple-machine) above).

Key points when building a scheme:

- Each moving node binds to a state parameter through `ParameterName` (the spindle is
  just a rotary axis whose state parameter is in the `RotaryAxis` group, and the tool
  holder points at it with `SpindleParamID`). All the parameters a scheme names must
  exist in `MachineStateParameters`.
- `AxisType` is `Linear` or `Rotary`. **`Direction` applies to linear axes only** —
  there it is the direction of travel. For **rotary** axes `Direction` is *not used*:
  rotation is always about the **Z axis of the axis's own local coordinate system**, so
  orient the node (via its `Matrix`) to place that Z where the rotation axis should be.
- **`Scale`** is a **dimensionless** multiplier on the axis's state‑parameter value (a
  length for a linear axis, an angle in **radians** for a rotary one); a **negative**
  `Scale` inverts the axis. See the
  [node reference](node-reference.md#tmachineaxis) for the full `TMachineAxis` property
  list, including `RapidFeed`, `Channel` and `DesignTimeAxisValue`.
- The chain **must end in a holder** so the tool (and, on the workpiece side, the
  part) has a place to sit. A tool holder's `XAxisID`/`YAxisID`/`ZAxisID` and
  `ToolAxisID`/`ToolAxisValue` carry extra meaning — see
  [§4](advanced-topics.md#4-tool-connectors--positioning-axes-and-activation) and
  the [connector reference](node-reference.md#tool-and-workpiece-connectors).
- Visual `Color`/geometry per node is set through the inherited `VisualProperties` (see
  the [node reference](node-reference.md#visualproperties) and
  [3D models for machines](3d-models.md)).

### One parameter, several nodes — the shared‑axis trick

An axis lives in **two places** that play different roles: an **axis node**
(`TMachineAxis`) in the `Schema` — the *geometry* (where it sits, its `Direction`,
`Matrix`, 3D model) — and a **state parameter** (`TMachineStateParameter`) — the single
*controllable value* (its `Address`, limits, control mode). They are linked by the node's
`ParameterName` matching the parameter's `ID`.

The powerful consequence: **several axis nodes can share one state parameter**, so one
controlled value drives several pieces of geometry at once. The classic case is a
**3‑jaw chuck** — three jaws, each its own axis node pointing radially in its own rotated
direction, all driven by a single `JawPos`:

```xml
<!-- one shared state parameter -->
<MachineStateParameters>
    <SCType ID="JawPos" Caption="Jaws" type="TMachineStateParameter">
        <AxisControl DefaultValue="Manual"/>
        <Min DefaultValue="0"/><Max DefaultValue="100"/><InitialValue DefaultValue="50"/>
    </SCType>
</MachineStateParameters>

<!-- three jaw nodes, each driven by the SAME JawPos but rotated to 0°, 120°, 240° -->
<SCType ID="Chuck" Caption="Chuck" type="TMachineNode">
    <SCType ID="Jaw1" type="TMachineAxis">
        <ParameterName DefaultValue="JawPos"/><AxisType DefaultValue="Linear"/>
        <Direction><X DefaultValue="1"/><Y DefaultValue="0"/><Z DefaultValue="0"/></Direction>
        <Matrix><SCType ID="T1" type="TRotateZ" DefaultValue="0"/></Matrix>
    </SCType>
    <SCType ID="Jaw2" type="TMachineAxis">
        <ParameterName DefaultValue="JawPos"/><AxisType DefaultValue="Linear"/>
        <Direction><X DefaultValue="1"/><Y DefaultValue="0"/><Z DefaultValue="0"/></Direction>
        <Matrix><SCType ID="T1" type="TRotateZ" DefaultValue="120"/></Matrix>
    </SCType>
    <SCType ID="Jaw3" type="TMachineAxis">
        <ParameterName DefaultValue="JawPos"/><AxisType DefaultValue="Linear"/>
        <Direction><X DefaultValue="1"/><Y DefaultValue="0"/><Z DefaultValue="0"/></Direction>
        <Matrix><SCType ID="T1" type="TRotateZ" DefaultValue="240"/></Matrix>
    </SCType>
</SCType>
```

Each jaw translates along its **own local X** (its `Direction`), but its `Matrix`
turns that local frame to 0° / 120° / 240°, so the three jaws move radially in and out
**together** whenever the single `JawPos` value changes. One parameter, three moving
nodes.

### Grounding the scheme — `IsFloor`

Mark the node that represents the **ground** (where gravity points) with the boolean
attribute **`IsFloor="True"`** (as on the `Base` node in the example above). It does
not affect the kinematics; it tells the graphics window how to build the **standard
views**, so "up" looks natural to the user even when the machine's world Z does not
point up — for instance a **ceiling‑mounted robot** whose base Z points downward.

### Common scheme errors

When a scheme is loaded the system validates it and reports problems. The messages you
are most likely to meet:

- **"Axes (X,Y,Z) must define the right coordinate system (repaired)"** — the chosen
  axis travel directions do not form a **right‑handed** triple. The system repairs it,
  but check the `Direction` vectors and the tool‑/workpiece‑branch signs
  ([§4](advanced-topics.md#4-tool-connectors--positioning-axes-and-activation)).
- **`Tool connector "…" has no correct X/Y/Z axis`** — a tool connector's
  `XAxisID` / `YAxisID` / `ZAxisID` does not name existing axes.
- **"Possibly incorrect ToolAxisID …"** — the `ToolAxisID` of a tool or sub‑machine
  does not point at a valid axis (usually it should be the spindle or turret axis).
- **"The same machine axis is specified as a X, Y or Z axis more than once in the
  submachine"** — a sub‑machine lists one axis in two of its `XAxisID`/`YAxisID`/`ZAxisID`
  slots.
- **"Incorrect redundant robot axis type"** — an unsupported value in `RedundantAxis`.

> **Advanced scheme topics** — how to position nodes with **matrices** (parent‑ vs
> world‑relative), build **switchable/detachable nodes** (turret blocks, attachable
> heads), author **turrets**, wire up **tool/workpiece connectors**, and set up
> **control channels & sub‑machines** for multi‑channel machines — are covered in
> **[Advanced machine topics](advanced-topics.md)**.

## Tooling, coolants and simulation

The remaining sections of the descriptor are smaller and mostly self‑explanatory:

- **`Coolants`** — the coolant tubes available on the machine, each with the code the
  postprocessor outputs to switch it on/off.
- **`Simulation`** — the simulation method and resolution, and the collision settings
  used when verifying a project on this machine.
- **`ToolChange`** — the tool‑change position, the timing law(s) (referenced by a
  connector's `ToolChangeTimeCalcLawIndex`) and the output mode for tool changes.

## Machine dimensions

**`MachineDimensions`** is where the scheme's important driving parameters are gathered
so the user sees them all in one compact place — for example the location of a
positioner, a cell dimension, or any value that other nodes are parametrized from. A
parameter reaches this section in one of two ways: declared **directly** as its child
(for values that belong to base nodes), or **attached** to it with the `Parent`
re‑assignment attribute (for values that live on switchable/attachable nodes but should
still appear here). See
[§8.4](../xml-properties/descriptor-syntax.md#84-presentation-and-grouping) for
`Parent`.

## Discovery

Machines are **not** registered anywhere — they are discovered by location. A
machine file is found simply by being placed in one of the scanned machine folders
(`$(SCHEMAS_FOLDER)` / `$(CUSTOM_SCHEMAS_FOLDER)`); the machine library picks it up
during its folder scan and loads it on demand
([above](#how-a-machine-descriptor-is-loaded)). There is no registration record
to write — unlike operations, machines need no registrator entry.

## Checklist for a new machine

1. Decide the closest base (`AbstractMillMachine`, an abstract robot/lathe, …) or
   `AbstractMachine` directly.
2. Generate a `GUID`; set `Group`, `Name`, `Comment`, `Image`, `Icon`,
   postprocessor `SPPFile`.
3. Define the controllable quantities in `MachineStateParameters`.
4. Build the `Schema` tree: nest axes by their real kinematic order and end each
   branch in the appropriate holder; link each axis to its state parameter via
   `ParameterName`.
5. Set the relevant `ControlData` switches (arcs, rotary transforms, 5‑axis,
   tool‑frame output).
6. Put the file in a scanned machine folder
   (`$(SCHEMAS_FOLDER)` / `$(CUSTOM_SCHEMAS_FOLDER)`), not under `Supplement` — the
   library discovers it automatically, with no registration record needed; member
   `ID`s only need to be unique within this one file
   ([above](#how-a-machine-descriptor-is-loaded)).

---

Next: **[Using XML properties from the CAM API](../xml-properties/using-from-code.md)**
