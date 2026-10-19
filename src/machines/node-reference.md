# Machine node reference

This page is the **property reference** for every node type used in a machine's
kinematic scheme, plus the coordinate conventions and units they are all expressed in.
It is a look‑up companion to **[Machine descriptors](machine-descriptors.md)**, which
walks through how the nodes fit together; come here when you need the full property list
of a particular node type.

The node types form a small inheritance tree:

- **`TMachineNode`** — the base of everything in the scheme. Every other node type below
  inherits its `ID`, `Matrix`, `VisualProperties` and `ImageFile`.
  - **`TMachineAxis`** — a node that *moves* (linear or rotary).
  - **`TToolHolderNode`** / **`TWorkpieceHolderNode`** — the sockets where the tool and
    the workpiece attach (the *Tool connector* / *Workpiece connector* of the UI).

A separate type, **`TMachineStateParameter`**, is not a scheme node at all — it is the
controllable *value* an axis node is driven by. Axis nodes link to it by name.

---

## Coordinate conventions and units

- **World coordinate system.** Looking at the front of an ordinary mill: **Z points
  up, X to the right, Y away from the viewer**. Build the scheme (and model the
  geometry) in this frame.
- **Units.** All `Matrix` translations — and all CAD geometry — are in the units of
  the machine's *Measurements* (see
  [Identity & metadata](machine-descriptors.md#identity-and-metadata)): **millimetres**
  for a metric machine, **inches** for an imperial one. If the running unit system
  differs, the system tries to rescale the machine **once at load**, but that can
  misbehave for heavily parametrized schemes — so **prepare the scheme directly in the
  units it will be used in**.
- **`Direction` need not be a unit vector.** For an ordinary orthogonal axis it is a
  normalized travel vector. But on machines with **non‑orthogonal** axes — e.g. a
  slanted Y support on a turn‑mill — `Direction`'s magnitude is **not** 1; its
  components follow the sines/cosines of the tilt between the axes. The shipped
  *Mori Seiki* turn‑mill
  (`Machines\LatheMilling\Turret\Mori Seiki\MoriSeiki.xml`) gives its Y axis
  `Direction = (√3, 1, 0)` — written exactly as `(1.7320508…, 1, 0)`, a 30° tilt with
  magnitude 2 — for a mathematically precise description.
- **Tool‑axis convention.** The tool's **Z** runs from the cutting tip, along the
  tool's rotation axis, to its mounting point in the spindle/holder. For external
  (OD) turning tools the same holds per **ISO 13399**: Z from the tip to the holder
  mount, with the insert's working plane in the **ZX** plane; **X** is chosen so that a
  **right‑hand** tool has most of its cutting geometry on the **−X** side (a
  **left‑hand** tool on **+X**). The CAM system computes everything assuming this
  placement; only at final CLData output may the optional `AdditionalTransform`
  ([tool‑frame output](machine-setup-parameters.md#tool-frame-output)) apply a last
  offset/rotation — normally zero for machines, and used on robots to flip Z so it
  points out of the flange (and out of the tool opposite the mount).

---

## `TMachineNode`

`TMachineNode` is the base for anything in the scheme tree. Every node type inherits
these four members:

| Property | Default | Meaning |
|---|---|---|
| `ID` | `""` | The node's identifier, unique within this machine file. |
| `Matrix` | identity | Placement of the node relative to its parent (or to the world — see [positioning nodes with matrices](advanced-topics.md#1-positioning-nodes-with-matrices)). |
| `VisualProperties` | — | How the node's 3D model is drawn (see [below](#visualproperties)). |
| `ImageFile` | `""` | The node's 3D model, an `.osd` / `.stl` file (see [3D models for machines](3d-models.md)). |

A bare `TMachineNode` is a **rigid** part of the structure (a bed, a column, a table) —
it carries geometry and positions its children, but does not move on its own.

---

## `TMachineAxis`

A `TMachineAxis` extends `TMachineNode` (so it has `ID`, `Matrix`, `VisualProperties`
and `ImageFile` like any node) and adds the axis‑specific properties below:

| Property | Default | Meaning |
|---|---|---|
| `AxisType` | `Linear` | `Linear` or `Rotary`. |
| `ParameterName` | `""` | ID of the [`TMachineStateParameter`](#tmachinestateparameter) that drives this axis. |
| `Direction` | `(0, 0, 1)` | Travel direction (**linear axes only** — see the note below). |
| `Scale` | `1` | Multiplier from the state‑parameter value to physical motion (see below); negative inverts direction. |
| `RapidFeed` | `10000` | Rapid velocity per minute (mm/min for a linear‑mm axis, deg/min for a rotary‑deg axis). |
| `Channel` | `-1` | Control channel ([§6](advanced-topics.md#6-control-channels-simultaneous-work)); `-1` = common. |
| `WorkpieceIndex` | `-1` | If ≥ 0, the axis is controlled only for that workpiece. |
| `DesignTimeAxisValue` | `0` | Axis value used at design time to compute node world matrices. |

**`Direction` — linear vs. rotary.** For a **linear** axis `Direction` is the direction
of travel. For a **rotary** axis `Direction` is *not used*: rotation is always about the
**Z axis of the axis's own local coordinate system**, so orient the node (via its
`Matrix`) to place that Z where the rotation axis should be.

**`Scale`** is a **dimensionless** multiplier applied to the axis's state‑parameter
value — the physical unit is carried by the *value*, not by `Scale`: a length for a
linear axis (mm, or inch in imperial) and an angle in **radians** for a rotary axis. Use
`Scale` to remap the value — for example an **indexed** turret stores a plain station
*index* and a `Scale` of `360 / BlocksCount` turns each index step into one station's
rotation. A **negative** `Scale` inverts the axis direction (and so also flips the base
CS it contributes to — see
[§4](advanced-topics.md#4-tool-connectors--positioning-axes-and-activation)).

---

## `VisualProperties`

Every node (`TMachineNode` and its descendants — axes, holders, schema nodes) has a
`VisualProperties` block that controls how its 3D model is drawn:

| Property | Default | Meaning |
|---|---|---|
| `Visible` | `True` | Whether the node's model is shown; when off, the node is hidden. |
| `Color` | `(0.5, 0.5, 0.5)` | Node colour as `R` / `G` / `B`, each `0…1`. |
| `Metallic` | `False` | Render with a metallic appearance. |
| `IsTransparent` | `False` | Make the node transparent (enables `Transparence`). |
| `Transparence` | `0.5` | Transparency, `0` = opaque … `1` = fully transparent. |
| `DisplayMode` | `Default` | Render mode — `Wire`, `Shade`, `EdgeShade`, or `Default`. |
| `VisMatrix` | identity | Matrix that places the node's 3D model independently of its kinematic `Matrix` (see [§1](advanced-topics.md#1-positioning-nodes-with-matrices)). |
| `Use3DModelColors` | `False` | When `True`, draw the node with the colours stored in its 3D model instead of the `Color` above. (An attribute on `VisualProperties`.) |

```xml
<VisualProperties Use3DModelColors="False">  <!-- an attribute on the element itself -->
    <Visible DefaultValue="True"/>
    <Color><R DefaultValue="0.5"/><G DefaultValue="1"/><B DefaultValue="0.5"/></Color>
    <DisplayMode DefaultValue="Shade"/>
</VisualProperties>
```

> Preparing the 3D models themselves (the `.osd` / `.stl` files, where they live, units
> and alignment) is covered in **[3D models for machines](3d-models.md)**.

---

## `TMachineStateParameter`

A `TMachineStateParameter` is a controllable quantity the controller drives — an axis
position, a spindle, a jaw travel. Axis nodes link to it through `ParameterName`. It is
declared either in the global `MachineStateParameters` section or on a node in the
`Schema` (see [machine state parameters](machine-descriptors.md#machine-state-parameters)).

| Property | Default | Meaning |
|---|---|---|
| `Enabled` | `True` | Whether the parameter is active. |
| `ID` | `""` | Its identifier; axes and holders link to it by this name (often parametrized, e.g. `[Prefix]…`). |
| `Address` | `""` | The address letter the postprocessor outputs for it (e.g. `X`, `Z`, `C`, `S`). |
| `AxisControl` | `Continues` | How it is driven — `Continues` (continuous), `Indexed`, or `Manual` (see notes). |
| `Group` | `Other` | Classification — `LinearAxis`, `RotaryAxis`, or `Other`. |
| `Incr` | `0.001` | Smallest increment / resolution. |
| `Min` / `Max` | `-1E9` / `+1E9` | Travel limits. |
| `InitialValue` | `0` | The axis value when the machine is reset to its initial state in a project, before any operation runs. |
| `DesignTimeValue` | `0` | Zero‑offset of the axis — the position at which its 3D model was drawn (see notes). |
| `HasBrake` | `False` | The axis has a brake. When set, an `AXESBRAKE On\|Off` command is emitted into CLData around every change of this axis (for the postprocessor to release/apply the brake). |
| `SupportShortestPathRotation` | *computed* | Periodic rotary axes only — affects rapid‑move simulation (see notes). |
| `Priority` | `0` | Order of the parameter in the user's lists/windows only (no effect on output). |
| `Order` | `[Priority]` | Order in which axes are written into CLData commands. |
| `ParameterType` | `Geom` | **Obsolete** — has no effect now (it once grouped the display into geometrical vs. technological). |
| `ControlWithMap` | `False` | Resolve a redundant axis with the interactive *axis map* (see notes). |
| `ClampID` | *computed* | Id of a clamping fixture; referenced by part‑handoff / takeover operations that clamp and unclamp it. |

The ones you set most often are `Address`, `Group`, and `Min`/`Max`/`Incr`.

**Notes on selected properties:**

- **`AxisControl`** — *Continuous*: several continuous axes may change within one NC
  block. *Indexed*: cannot move in sync with other axes — it is positioned and locked
  in its own NC block(s) before the main cut. *Manual*: not program‑controlled — the
  operator sets it by hand, so it may be changed only in **Setup** objects (not in the
  operations inside a setup), and a postprocessor may emit it as a comment/instruction
  for the operator.
- **`ControlWithMap`** — for **redundant** axes. It enables the interactive *axis
  map*: a graph of the redundant axis's value (vertical) against path length
  (horizontal) on which you draw how that axis should move along the toolpath, while
  watching the whole machine move and seeing node collisions as forbidden zones on the
  map. It is an interactive way to resolve inverse‑kinematics redundancy. Enable it
  **only for *extra* redundant axes that the virtual sub‑machine does not already know
  about**: the principal redundant external axes — e.g. a robot's 3 linear rail axes
  and 2 rotary positioner axes, or the C axis of a 5‑axis machine (for singularity
  avoidance) — appear in the map **automatically**, without this flag.
- **`SupportShortestPathRotation`** — for periodic rotary axes whose range exceeds
  180°. It does **not** change CLData (the target value, e.g. `A+370`, is still
  output); it only affects the **simulation of rapid moves**: when on, a rapid takes
  the shortest equivalent angle (`A+10` rather than `A+370`); when off, it makes the
  full turn. Feed moves always perform the full move.
- **`DesignTimeValue`** — use it when an axis's 3D model was drawn at a non‑zero
  position: state that drawn position here, and the axis zero shifts by the opposite
  amount so the model lines up with axis value 0.

---

## Tool and workpiece connectors

A **connector** is where a tool or the workpiece attaches to the kinematic chain — the
*Tool connector* (`TToolHolderNode`) and *Workpiece connector* (`TWorkpieceHolderNode`)
of the UI. Both derive from a common socket and share the **spindle and clamping**
properties below. On **machines** (not robots) a **tool** connector additionally carries
the properties that tell the kinematics solver how its tool is positioned and selected.

The tables here are the property look‑up; the *behaviour* behind these properties — how
the base coordinate system is derived, how a connector is made active, the workpiece
placement caveat — is explained in
[§4 Tool connectors](advanced-topics.md#4-tool-connectors--positioning-axes-and-activation).

### Tool‑specific properties (`TToolHolderNode`)

| Property | Default | Meaning |
|---|---|---|
| `XAxisID` / `YAxisID` / `ZAxisID` | `""` | Machine axes that position this tool's tip in space; they also define the connector's **base coordinate system** ([§4](advanced-topics.md#4-tool-connectors--positioning-axes-and-activation)). |
| `ToolAxisID` | `""` | The axis to move in order to make this connector active (magazine / turret indexing). May be left empty when an active sub‑machine supplies the tool axis. |
| `ToolAxisValue` | `0` | The value of `ToolAxisID` that brings this station / tool in. |
| `ToolNumber` | `0` | The magazine position (tool number) the postprocessor outputs. `0` → not used; the NC program outputs the number from the cutting tool's own properties instead. |
| `SupportedToolTypes` | — | The applications a tool in this connector can perform — `MillTool`, `LatheCutter`, `JetCutter`, `Punch`, `Wire`, `Cutter6D`, `Welder`, `AdditiveTool`, `Painter`, `HeatTreatment`, `Gripper`. Used to filter the operation/tool lists offered for the connector. |
| `Channel` | `-1` | The control channel this connector belongs to ([§6](advanced-topics.md#6-control-channels-simultaneous-work)). |
| `ToolChangeTimeCalcLawIndex` | `0` | Index of the tool‑change‑time law (defined in the machine's *Tool Change* section) that applies to this connector (`0` = the default law). |

### Spindle and clamping (shared by both connectors)

| Property | Default | Meaning |
|---|---|---|
| `SpindleParamID` | `""` | ID of the [machine state parameter](#tmachinestateparameter) driving the rotary **spindle** axis that spins the tool or the part. It is the *state‑parameter* ID, **not** the axis node's `ID`. |
| `HolderType` | `Unknown` | `Unknown`, `LeftLatheSpindle` or `RightLatheSpindle`; marks a lathe spindle socket. |
| `DefaultClampID` | *computed* | The default clamp id of this socket, referenced by part‑handoff / takeover operations; defaults from `HolderType` (left spindle → `1`, right → `2`, otherwise `-1`). |

### Workpiece connector (`TWorkpieceHolderNode`)

A workpiece connector is where the **part** is held — on a chuck, spindle or fixture. It
carries the shared *spindle and clamping* properties above (most importantly
`SpindleParamID` for a turning spindle, and `HolderType` / `DefaultClampID` for
clamping), but **none** of the tool‑specific positioning (`XAxisID`/`YAxisID`/`ZAxisID`),
activation (`ToolAxisID`/`ToolAxisValue`) or `ToolNumber` / `SupportedToolTypes` fields —
those describe how a *tool* is positioned and selected, which does not apply to a part
holder.

> **Placement caveat.** Although `TWorkpieceHolderNode` inherits the node `Matrix`,
> that matrix is **ignored** for a workpiece connector — unlike for ordinary nodes,
> axes and tool holders. A workpiece connector always takes the placement of its
> **parent node**. So to offset where the part sits, add an extra parent node and put
> the placement (its `Matrix`) on *that* node. This is deliberate: the part's position
> is meant to be defined by the **workpiece setup** in the project (inside the CAM
> system), not fixed when the machine is created.

---

Back to the walkthrough: **[Machine descriptors](machine-descriptors.md)** ·
[Machines index](readme-machines.md)
