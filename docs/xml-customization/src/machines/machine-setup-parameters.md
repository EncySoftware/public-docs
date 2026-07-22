# Machine Setup parameters reference

This page explains the parameters shown on the **Machine Setup** tab of a machine —
the *Description*, *Control Parameters* and the related sections — as you see them
in the parameter inspector. For each parameter it describes **what it does and when
to change it**, and gives the **XML fragment** that overrides its default in a
machine descriptor.

These parameters are the human‑facing side of the machine descriptor's
`ControlData` and neighbouring sections (the XML structure is covered in
[Machine descriptors](machine-descriptors.md)). Machine builders normally set them with the
**MachineMaker** tool, but understanding them is essential when fine‑tuning a
machine or writing a postprocessor/interpreter, because they govern how the toolpath
is turned into NC code and how the machine is simulated.

> **Machine vs. robot.** Some parameters and whole groups differ by kinematic type —
> a 5‑axis mill exposes different options from a 6‑axis articulated robot. Where it
> matters, the differences are called out below.

> **Where values come from.** Each parameter has a machine‑level **default** set
> here; many of them simply seed the corresponding option that the operator then
> sees (and can change) inside an operation. The text notes when a Machine Setup
> value is "the default for the operation property".

## How to override a parameter in XML

Each fragment below goes **inside your machine type's body**, overriding the value
inherited from the base machine with the override form from
[§4.2](../xml-properties/descriptor-syntax.md#42-overriding-an-inherited-member) — you restate
the member (and the section path that contains it) and set a new `DefaultValue`:

```xml
<SCType ID="MyMachine" Caption="My 5-axis mill" type="AbstractMillMachine">
    <ControlData>
        <LocalCS>
            <AutoLCSRotationLaw DefaultValue="SnapToToolCS"/>
            <!-- SnapToMachineCS, SnapToWorkpieceCS, ExcludeA, ExcludeB, ExcludeC -->
        </LocalCS>
    </ControlData>
</SCType>
```

The fragments shown for each group below omit the outer `<SCType …>` for brevity —
they start at the relevant section (`<ControlData>`, `<ToolChange>`, …). **The
section nesting matters**: a member must be wrapped in the same elements that contain
it. Comments after a value list the other accepted enum options. Almost every
parameter is declared in [`MachineTypes.xml`](../../Machines/MachineTypes.xml) and
[`Machines/AbstractMachine.xml`](../../Machines/AbstractMachine.xml); complete,
ready‑made machines ship under `$(SCHEMAS_FOLDER)` and are worth studying as
examples.

---

## Description

General, mostly informational identity of the machine:

- **Name**, **Group** — display name and the machine category it belongs to.
- **Developer** — who authored the machine/scheme.
- **NC System name** — the control/CNC family, for information.
- **Postprocessor file** — the default postprocessor used to generate NC programs
  for this machine.
- **Interpreter file** — used to read an NC program back and reconstruct the
  toolpath inside the machine.
- **Measurements** — the unit system the machine was created in (mm / inch) and the
  derived units (linear, cutting speed, feedrate, feed/rev, feed/tooth, revolution).
  These are view‑only on the tab.

```xml
<!-- machine type body (direct children) -->
<Name      DefaultValue="My 5-axis mill"/>
<Group     DefaultValue="Milling"/>  <!-- Unknown, Lathe, LatheMilling, JetCutter, WireEDM, Robot -->
<Developer DefaultValue="Acme"/>
<NCSystem  DefaultValue="Heidenhain TNC640"/>
<SPPFile   DefaultValue="$(PROGRAM_PERSONAL)\Postprocessors\MyPost.sppx"/>
<Image     DefaultValue="Images\MyMachine.png"/>
<Icon      DefaultValue="Images\MyMachine_ico.bmp"/>
```

## Tooling

For turret machines, this is where the turret block layout is configured.

---

## Control Parameters

The bulk of the tab. These tell the engine and the postprocessor what the control
can do and how output should be formed. Everything in this group lives under the
`<ControlData>` element.

### Arcs

Controls how circular moves are emitted into the NC program.

- **Use arcs** — master switch. If off, every arc that would appear in the toolpath
  is replaced by line segments, computed to the tolerance set in the operation.
- **Use arcs in XY / YZ / ZX plane** — restrict arc output to the planes the control
  actually supports; arcs in a disabled plane fall back to segments.
- **Circles division** — whether full circles are broken up: *Do not break*, *Into
  quadrants* (90°), or *Into halves* (180°).
- **Minimal Arc Length** / **Maximal Arc Radius** — guard against degenerate arcs.
  An arc shorter than the minimum, or with a radius larger than the maximum (almost
  a straight line), is emitted as segments instead.
- **Spatial arcs** — arcs that do **not** lie in an orthogonal XY/YZ/ZX plane,
  usually defined by three arbitrary points. Common on industrial robots. If off,
  such arcs become segments; if on, a dedicated multi‑point arc command is produced
  for the postprocessor.
  - **Supported** — enables spatial‑arc output.
  - **Minimal distance between start and end points** — a 3‑point arc cannot be
    defined when start and end coincide (a full 360° arc). If the start/end distance
    is below this value, segments are emitted instead.
  - **Reorientation mode** — how the *tool orientation* is modelled while traversing
    a spatial arc: *Relative to base CS* (spherical interpolation of the orientation
    in the arc's base coordinate system) or *Relative to path* (the orientation is
    interpolated relative to the path tangent).
  - **Consider middle point orientation** — a 3‑point arc carries position *and*
    orientation at start, middle and end. Off: the middle orientation is ignored and
    orientation is interpolated start→end (the middle point still shapes the arc in
    space). On: orientation is interpolated start→middle, then middle→end. Set it to
    match how the real control behaves.

```xml
<ControlData>
    <UseArc          DefaultValue="true"/>
    <UseArcInXY      DefaultValue="true"/>
    <UseArcInYZ      DefaultValue="false"/>
    <UseArcInZX      DefaultValue="false"/>
    <CirclesDivision DefaultValue="DoNotBreak"/>  <!-- Quadrants, Halves -->
    <MinArcLength    DefaultValue="0.05"/>
    <MaxArcRadius    DefaultValue="10000"/>
    <SpatialArcs>
        <Supported            DefaultValue="False"/>
        <MinDistance          DefaultValue="0.2"/>
        <ReorientationMode    DefaultValue="rmBaseCS"/>  <!-- rmPath -->
        <ConsiderMiddleOrient DefaultValue="False"/>
    </SpatialArcs>
</ControlData>
```

### Singularities

A **singularity** is a pose where the joint values are mathematically undefined or
ambiguous. The contents of this group depend on the current kinematics.

- **Machine (rotary table).** With a rotary‑table scheme, when the tool axis becomes
  vertical the table rotation is undefined (infinitely many solutions). Such zones
  should be avoided.
  - **Allowed axis deviation** (e.g. *Wrist angle*) — how far the tool may be tilted
    away from the ideal orientation to skirt around a singularity zone instead of
    driving straight through it.
- **Robot.** A robot has more singularities (wrist, base/shoulder, elbow) because it
  has more joints. The per‑joint angle values define **where each singularity zone
  begins** (the angle from which a joint is considered "in" the zone), and the
  *J2–J3 free area* / maps describe forbidden regions used to route around them.

```xml
<ControlData>
    <Singularities>
        <Wrist DefaultValue="0.01"/>   <!-- allowed axis deviation, degrees -->
        <!-- robot only, additional joints: -->
        <Elbow DefaultValue="0"/>
        <Base><Angle DefaultValue="5"/></Base>
    </Singularities>
</ControlData>
```

### Flip Table / default machine configuration

When a pose can be reached in more than one way (e.g. tilt the head left or right —
same tool/part relation, opposite axis signs), a **flip** chooses which solution to
use. The Machine Setup only stores the **default** state of each flip; the operation
itself exposes the actual flip controls.

- **Machines:** a single *Flip Table* default.
- **Robots:** a default state per joint flip — *Flip base (J1)*, *Flip elbow (J3)*,
  *Flip wrist (J5)*, plus external‑axis flips/positions.

```xml
<ControlData>
    <DefaultFlips>
        <Flip5x DefaultValue="False"/>   <!-- machine: default table/wrist flip (Boolean) -->
        <!-- robot only: FlipA1, FlipA3, FlipA5, ... -->
    </DefaultFlips>
</ControlData>
```

### Origin list parameters

How work coordinate systems are numbered.

- **Origin prefix** (e.g. `G`), **Initial number** (e.g. `54`), **Increment value**
  (e.g. `1`) — produce `G54`, `G55`, `G56`, … as new origins are created. Robots use
  different conventions.
- **Create new origin for part group** — whether each part group gets its own origin.

```xml
<ControlData>
    <OriginParams>
        <Prefix                 DefaultValue="G"/>
        <InitialNum             DefaultValue="54"/>
        <IncStep                DefaultValue="1"/>
        <CreateNewOriginForPart DefaultValue="True"/>
    </OriginParams>
</ControlData>
```

### Radius Compensation Parameters

- **Sharp Corner** — the angle threshold (e.g. `135°`) that separates *sharp* from
  *obtuse* corners when building the cutter‑radius‑compensated path. At a sharp
  corner an extra chord is inserted so the tool does not swing too far from the
  corner; at an obtuse corner the path simply runs to the intersection point.

```xml
<ControlData>
    <RadiusCompensationParams>
        <SharpCorner DefaultValue="135"/>   <!-- degrees -->
    </RadiusCompensationParams>
</ControlData>
```

### Rotary Transformations

Polar and cylindrical interpolation support.

- **Polar interpolation is available** / **Cylindrical interpolation is available** —
  whether the control offers these interpolations at all.
- **CNC supports polar interpolation** / **CNC supports cylindrical interpolation** —
  if **on**, the control performs the transform itself and the CAM system works as if
  in plain Cartesian coordinates; if **off**, the CAM system *simulates* the
  interpolation and outputs the resulting rotary‑axis values for the control to
  follow.
- **Start from C=0** — legacy compatibility for old postprocessors that required the
  C axis to be reset to zero before enabling interpolation. Leave it **off** on new
  machines; the path is now tracked correctly without it.

```xml
<ControlData>
    <RotaryTrans>
        <PolarAvailable     DefaultValue="true"/>
        <CNCSupPolar        DefaultValue="true"/>
        <CylindAvailable    DefaultValue="true"/>
        <CNCSupCylind       DefaultValue="true"/>
        <OldPPCompatibility DefaultValue="false"/>  <!-- "Start from C=0"; keep false -->
    </RotaryTrans>
</ControlData>
```

### Tool frame output

How the **tool orientation** is written in each block of the NC program (mainly for
5‑axis / multi‑goto output).

- **Format** (the combo box) — the orientation format: *Normal vector (Nx, Ny, Nz)*
  (default for machines), the various *Euler angle* sequences (common on robots),
  *Quaternion*, or *Axis‑angle*. Pick what the control expects.
- **Additional transformation** — an extra rotation of the tool's own coordinate
  system, mostly for robots. By default the tool Z points from the tip up toward the
  spindle; some robots are calibrated with Z pointing the other way, or with X along
  the tool. Three angles let you match the real tool frame.
  > **Known limitation — read before using on robots.** There is currently **one
  > global** `AdditionalTransform`, and it is applied to **two different frames at
  > once**: the final *tool* coordinate system **and** the robot's *6th‑axis flange*
  > coordinate system. On real cells those two do **not** always coincide, and a cell
  > may have **several** working organs while this setting stays single and global —
  > so one transform cannot correct both independently. This is a known architectural
  > limitation (a future version is expected to split the setting between the machine
  > scheme and the cutting tool). If a robot's tool or flange orientation looks wrong
  > and one `AdditionalTransform` cannot satisfy both, this is why — do not keep
  > re‑debugging it.
- **Set machine state flags** — output the machine frame state (zero / path / robot
  base) in every block. Off for ordinary machines (not used); typically on for
  robots, where per‑point orientation is essential.
- **Swap Tool and Workpiece frames** — for robots that hold the **part** while the
  tool is stationary. Each block then expresses the part orientation relative to the
  tool (the inverse of the usual tool‑relative‑to‑part matrix). If the control itself
  performs this inversion, leave it off; otherwise the CAM system inverts the matrix
  itself before passing the orientation to the postprocessor.
- **Set tool contact surface normal vectors** — for **5‑axis tool compensation**.
  On finishing passes the contact point and its surface normal are known; outputting
  that normal lets the control shift the tool along it by the difference between the
  real and the programmed tool (so a slightly different tool does not gouge). When
  enabled, a special **`TLCONTACT`** command is written into the CL data in every
  block that has surface contact, carrying that contact normal; the postprocessor
  must handle it (see the `TLCONTACT` command in your postprocessor manual).

```xml
<ControlData>
    <ToolFrameOutput>
        <Format DefaultValue="NormalVector"/>
            <!-- EulerZYX, EulerXYZ, FixedABC, Quaternion, AxisAngleDeg, AxisAngleRad, ... -->
        <SetMachineStateFlags       DefaultValue="False"/>
        <SwapToolAndWorkpieceFrames DefaultValue="False"/>
        <SetContactNormal           DefaultValue="False"/>
        <AdditionalTransform>            <!-- extra tool-frame rotation (robots) -->
            <A DefaultValue="0"/>
            <B DefaultValue="0"/>
            <C DefaultValue="0"/>
        </AdditionalTransform>
    </ToolFrameOutput>
</ControlData>
```

### Redundant axis

Selects the rule for resolving a **redundant** axis when solving the inverse
kinematics (used only by schemes that actually have a redundant axis). Default
*None*.

```xml
<ControlData>
    <RedundantAxis DefaultValue="None"/>
        <!-- KukaLBRiiwa, NITIProgress, NITIProgress3, NonSphericalWrist, ScaraSimple -->
</ControlData>
```

### Robot joint coupling

(Robot schemes.) Flags such as **Joint 3 is linked with joint 2 (parallelogram)**
model mechanically coupled joints — on by default for parallelogram‑type robots,
off for others. When set, the coupled joint values are output as linked.

```xml
<ControlData>
    <IsParallelJoints23 DefaultValue="false"/>  <!-- joint 3 linked with joint 2 -->
    <IsConnected46Joints DefaultValue="False"/>
    <IsConnected56Joints DefaultValue="False"/>
</ControlData>
```

---

## Indexed vs. continuous 5‑axis machining

Two almost‑identical groups, **Indexed 5‑axis machining** and **Continuous 5‑axis
machining**, each containing the *same three compensation switches*. Which group an
operation uses is chosen by the operation's **Tool Center Point Management (TCPM)**
toggle: TCPM **off** → the operation uses the *indexed* group; TCPM **on** → it uses
the *continuous* group.

### The three compensation switches

They control how the tooltip and the workpiece coordinate system are recomputed as
the tool and part move during 5‑axis machining:

- **5 Axis tooling point compensation** — when **on**, the tooltip stays rigidly
  attached to the tool (the control recomputes the tip position for every rotation).
  When **off**, the programmed point stays fixed while the tool turns — used in the
  rare case where a rotary head's kinematics are *not* known to the control (e.g. a
  manual head); then the CAM system computes the path itself. Normally leave it on.
- **5 Axis workpiece zero point compensation** — whether the **origin** of the
  workpiece coordinate system moves with the part as axes rotate.
- **5 Axis coordinate system compensation** — whether the **axis orientation** of
  the workpiece coordinate system rotates with the part.

Defaults differ by group: *indexed* = tooling‑point on, workpiece compensation off;
*continuous* = all three on (in TCPM the control compensates the whole kinematics, so
the path is programmed as if the system were rigidly attached to the part).

```xml
<ControlData>
    <!-- used when the operation's TCPM is OFF (indexed): -->
    <Indexed5AxisCompensationMode>
        <IsToolTipCompensated        DefaultValue="true"/>
        <IsWorkpieceZeroCompensated  DefaultValue="false"/>
        <IsCoordinateAxesCompensated DefaultValue="false"/>
    </Indexed5AxisCompensationMode>
    <!-- used when the operation's TCPM is ON (continuous): -->
    <TCPM5AxisCompensationMode>
        <IsToolTipCompensated        DefaultValue="true"/>
        <IsWorkpieceZeroCompensated  DefaultValue="true"/>
        <IsCoordinateAxesCompensated DefaultValue="true"/>
    </TCPM5AxisCompensationMode>
</ControlData>
```

### Local coordinate system (ORIGIN) — indexed mode

Indexed machining of a tilted feature needs an explicit *rotate the work coordinate
system* command in the NC program (e.g. a plane/cycle command). These parameters
govern it:

- **Local coordinate system** availability — *Unavailable* (the control has no such
  command — the operation then offers no Local CS option at all), *Off* (available
  but default off), or *Auto*. The chosen value becomes the **default** for the
  operation's Local CS property.
- **Auto** computes the local CS so its **Z is along the tool axis** while keeping
  the origin where the work zero (e.g. `G54`) was set.
- **Auto LCS rotation law** — Z along the tool leaves the rotation *about* Z
  undefined; this law fixes it: *Snap to Tool CS*, *Snap to Machine CS*, *Snap to
  Workpiece CS*, or *Exclude A/B/C* (force one spatial angle to zero so the result is
  just two rotations). The right choice usually depends on where the rotary axes sit
  in the kinematics.
- **Local CS positioning mode** — what the machine axes do when the CS‑rotation
  command is output:
  - *Stay* — the CS rotates but **no axis moves**; the tooltip stays put, so its
    coordinates relative to the new CS change. You must add the axis‑turn commands
    yourself.
  - *Turn* — additionally turns the rotary axis so the tool re‑aligns with the new
    CS Z (e.g. on some controls a CS‑rotate command is immediately followed by an
    "align rotaries" command). **Most common** — the rotate command alone is enough.
  - *Move* — like *Turn*, and also moves the linear axes so the tooltip keeps the
    same coordinates in the rotated CS. Usually undesirable.
- **Euler angles type (rotation sequence)** — the angle convention used to output the
  CS rotation (e.g. `XYZ`, `ZXZ`). Note that the CL data carries *both* the spatial
  (Euler) angles and the physical axis values; the postprocessor decides which to
  emit. The two can differ greatly on non‑orthogonal kinematics (e.g. a 45°‑skewed
  table), so confirm with the machine integrator which the control expects.
  - **Rotations around movable axes** — primed vs. unprimed convention (rotate about
    the already‑rotated axes vs. the fixed axes).
  - **Angles in degrees** — degrees vs. radians.
- **Move auto LCS with table** — whether the **origin** of the auto CS rotates with
  the part (on) or stays at its original calibrated location (off).
- **Rotatable Workpiece CS** — whether the workpiece CS rotates with the part **at
  setup/calibration time** (when you define `G54` with an axis already rotated). Off
  for machines (the workpiece CS is always calibrated in a fixed orientation), on for
  robots (it is rigidly tied to the part).

```xml
<ControlData>
    <LocalCS>
        <DefaultState           DefaultValue="Auto"/>   <!-- Unavailable, Off, Auto -->
        <PositioningMode        DefaultValue="Stay"/>    <!-- Turn, Move -->
        <IsSpatial              DefaultValue="True"/>
        <AutoLCSRotationLaw     DefaultValue="SnapToMachineCS"/>
            <!-- SnapToToolCS, SnapToWorkpieceCS, ExcludeA, ExcludeB, ExcludeC -->
        <TurnAutoLCSRotationLaw DefaultValue="ZAlongTurn_XAlongTool"/>
            <!-- ZAlongTurn_MinusXAlongTool, ZAlongTool_XbySnapRule -->
        <MoveAutoLCSWithTable   DefaultValue="true"/>
        <RotatableWCS           DefaultValue="false"/>   <!-- robots: true -->
        <EulerAnglesType>
            <RotationsSequence          DefaultValue="XYZ"/>  <!-- ZXZ, ZYX, XZY, ... -->
            <RotationsAroundMovableAxes DefaultValue="False"/>
            <AnglesInDegrees            DefaultValue="True"/>
        </EulerAnglesType>
    </LocalCS>
</ControlData>
```

### Continuous 5‑axis machining (TCPM)

- **TCPM mode is available** — whether the control offers continuous 5‑axis / tool
  centre point management (an often separately‑licensed option). If unavailable, the
  operation shows no TCPM toggle.
- **TCPM mode default state** — the default for the operation's TCPM toggle.
- **Disable TCPM when rotate back** — for rotary axes with a limited travel range
  that must be "rewound". Rewinding with TCPM active makes every axis move to hold the
  tooltip fixed — a large, risky motion. With this on, the system drops out of TCPM,
  turns just the one rotary axis back, then re‑enables TCPM and continues.

These three live under `RotaryTrans` (the *Continuous 5‑axis machining* group is only
a UI grouping):

```xml
<ControlData>
    <RotaryTrans>
        <TCPMAvailable         DefaultValue="False"/>
        <TCPMDefault           DefaultValue="False"/>
        <DisableTCPMifOverturn DefaultValue="True"/>  <!-- "Disable TCPM when rotate back" -->
    </RotaryTrans>
</ControlData>
```

---

## Tool Change

- **Go to tool change position** — *Only if tool change is needed* (retract to the
  change position only when consecutive operations use different tools), *Always at
  the end of operation*, or *Never* (a legacy mode that simply swaps the tool with no
  retract, emulating the old "tool floating in space" behaviour from before machine
  simulation existed).
- **Output mode** — how the change‑position coordinates are written:
  - *Machine coordinates (ISO G53)* — physical‑axis moves (e.g. `G53 Z0`); safe,
    small numbers, independent of the work zero.
  - *Reference point (ISO G28)* — retract via the machine reference point; common on
    turn‑mill / lathe centres; avoids stating an explicit change‑position in the work
    CS.
  - *Tool tip coordinates* — the actual tip coordinates relative to the work CS;
    produces large numbers and requires the machine to be calibrated, or it may hit
    the limit switches.
- **Tool change position** — the position itself.
- **Heavy axes** — axes the collision‑avoidance approach/retract planner should avoid
  moving where possible (manual/indexed/awkward axes such as a column). Lists machine
  node IDs.
- **Tool change time calculation** — how change time is estimated: *Undefined* (a
  built‑in constant, for compatibility) or an explicit law stating the duration;
  several laws can be defined.

```xml
<!-- machine type body -->
<ToolChange>
    <Using      DefaultValue="Auto"/>     <!-- Anyway, DoNotUse -->
    <OutputMode DefaultValue="RefPoint"/> <!-- Tooltip, Machine -->
</ToolChange>
<ToolChangeMachineState DefaultValue=""/> <!-- tool change position -->
<Leads>
    <MotionPlannerOptions>
        <HeavyAxes DefaultValue=""/>       <!-- space-separated machine node IDs -->
    </MotionPlannerOptions>
</Leads>
```

## Coolants

Which coolant channels the machine has — *Flood*, *Mist*, *Tool* (through‑tool), and
additional numbered tubes — each with a *Supported* flag and an optional **switch
time**. Enabled channels appear on the operation's output tab.

```xml
<Coolants>
    <Coolant5>                          <!-- Coolant1..Coolant20 -->
        <Supported  DefaultValue="True"/>
        <SwitchTime DefaultValue="1"/>
    </Coolant5>
</Coolants>
```

## Simulation

Parameters for the machining/stock simulation:

- **Simulation method** — *Voxel 5d* (default; fast, less precise — a voxel is a 3D
  pixel), *Voxel 3d*, or *Solid* (surface model; more precise and independent of
  voxel size, but slower on long paths and complex shapes). Voxel modes are a poor fit
  for very thin tools (e.g. EDM wire) where the tool size approaches the voxel size.
- **Model resolution** — the voxel count the stock is divided into (high / standard /
  low).
- **Gouge detection tolerance** — how precisely gouges into the part are detected.
- **Revolution bodies simulation** — when a chuck spins fast, its jaws become a body
  of revolution; on, that body is computed from the 3D jaw model for display and
  collision (can slow simulation); off, the jaws are shown/collided as‑is.
- **Check inappropriate tool and spindle direction** — warns when the tool/spindle
  rotation is wrong (e.g. a right‑hand tool with the spindle reversed), which would
  ruin the surface or crash the tool.
- **Collisions to ignore** — node pairs whose collisions should not be checked.
  Adjacent nodes are ignored automatically; list here only non‑adjacent pairs that can
  never collide, to speed up checking.
- **Show active part only** — for multi‑channel / Swiss‑type machines that machine
  two part instances at once; hides the second part instance when it is in the way.

```xml
<Simulation>
    <Simulation_Method       DefaultValue="smVoxel5d"/>  <!-- smSolid, smVoxel -->
    <Simulation_Resolution   DefaultValue="srStandard"/> <!-- srLow, srHigh -->
    <GougeDetectionTolerance DefaultValue="0.05"/>
    <RevBodySim              DefaultValue="True"/>
    <CheckSpindleDirection   DefaultValue="true"/>
    <ShowActivePartOnly      DefaultValue="False"/>
</Simulation>
```

## System settings → Main

- **Rotation angles type (rotation sequence)** — the default Euler‑angle convention
  used wherever angles are entered (e.g. when creating a coordinate system). It is the
  default only; each case can still override it.

```xml
<SystemSettings>
    <Main>
        <RotationAnglesType>
            <RotationsSequence DefaultValue="XYZ"/>  <!-- ZXZ, ZYX, ... -->
        </RotationAnglesType>
    </Main>
</SystemSettings>
```

## Machine state parameters, Schema, Machine dimensions

The remainder of the tab is the machine's own kinematics:

- **Machine state parameters** — the controllable quantities (Axis X/Y/Z/B/C
  positions, …); see [Machine state parameters](machine-descriptors.md#machine-state-parameters).
- **Schema** — the kinematic node tree; see
  [The kinematic scheme](machine-descriptors.md#the-kinematic-scheme).
- **Machine dimensions** — cell‑calibration values established when the cell is set
  up: e.g. the position of a rotary fixture/table relative to the cell's world
  coordinate system, or a tool's mounted position. Especially important for robot
  cells.

---

Back to **[Machine descriptors](machine-descriptors.md)** | [guide index](readme-machines.md)
