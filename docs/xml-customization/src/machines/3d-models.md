# 3D models for machines

A machine scheme is a tree of nodes ([Machine descriptors](machine-descriptors.md)); each node can
carry a **3D model** that is drawn — and collision‑checked — at that node's position
in the kinematic chain. This page explains how those models are referenced, prepared
and aligned. The XML side is small (three things: `ImageFile`, `VisMatrix`,
`Use3DModelColors`); the rest is about preparing the geometry correctly.

## 1 Attaching a model to a node

A node's model is named by its **`ImageFile`** property (inherited from
`TMachineNode`), and positioned for display by **`VisMatrix`** inside
`VisualProperties`:

```xml
<SCType ID="Column" Caption="Column" type="TMachineNode">
    <ImageFile DefaultValue="Images\column.osd"/>
    <VisualProperties>
        <VisMatrix>                          <!-- adjusts the model only, not the kinematics -->
            <SCType ID="T1" type="TRotateZ" DefaultValue="90"/>
        </VisMatrix>
        <Color><R DefaultValue="0.4"/><G DefaultValue="0.4"/><B DefaultValue="0.45"/></Color>
    </VisualProperties>
</SCType>
```

A node is drawn using **its kinematic frame** (the product of the `Matrix` chain from
the root down to it, see [§1](advanced-topics.md#1-positioning-nodes-with-matrices)),
and then **`VisMatrix`** is applied **on top, to the model only**. So if a CAD model
was exported in an awkward orientation, correct it with `VisMatrix` without disturbing
how the node moves.

> **One node = its own geometry.** Each moving node must carry **only** the geometry
> that moves with it. A correctly prepared machine is therefore an **assembly** of
> separate models — one per node — not a single monolithic model. This is what lets
> the parts move correctly relative to one another.

## 2 Where model files live

- Model files normally sit **next to the machine's XML file**, or in an **`Images\`**
  subfolder for tidiness, and are referenced by **relative paths** (e.g.
  `Images\column.osd`). The same applies to the bitmap images shown in the machine
  library.
- A complete machine is therefore **a folder of several files** — the descriptor XML
  plus its models and images.
- **Keep the folder self‑contained and portable.** Do **not** reference files in a
  neighbouring machine's folder — that breaks when the machine is moved or shared.
  (Machine schemes are stored, as folders, inside projects precisely so projects stay
  portable.)
- These folders do **not** have to live under the standard distribution aliases such
  as `$(SCHEMAS_FOLDER)`: the machine library can be told to scan any user folders for
  machines.

## 3 Units and coordinate system

- **Units must match the machine descriptor.** Model geometry must be saved in the
  same units as the machine's *Measurements* — millimetres for a metric machine,
  inches for an imperial one — exactly like the `Matrix` translations (see
  [coordinate conventions and units](node-reference.md#coordinate-conventions-and-units)).
  If the running unit system
  differs, the system tries to scale the machine once at load, but that can misbehave
  for heavily parametrized schemes — so **prepare models in the units the machine will
  use**.
- **Coordinate system.** Geometry is shown in the global CS it was drawn in, combined
  with the node‑hierarchy matrices and then `VisMatrix`. In other words, model the part
  in the machine's world CS (Z up, X right, Y away — [coordinate conventions](node-reference.md#coordinate-conventions-and-units)),
  and use `VisMatrix` only to fix up a model that came out misaligned.
- **Often it is a zero‑position issue, not a `VisMatrix` one.** A model frequently
  looks "off" simply because the axis it sits on was modelled at a **non‑zero
  position**. Then you usually do **not** need `VisMatrix` — just set that axis's
  **`DesignTimeAxisValue`** ([node reference](node-reference.md#tmachineaxis)) to the
  position at which the model was drawn, and the node (model *and* kinematics together)
  lines up correctly at design time. Reach for `VisMatrix` only when the model itself
  is rotated/offset relative to its node frame.

## 4 The OSD and STL formats

Two formats are accepted:

- **OSD** (*OpenGL Stream Data*) — the system's own format and the one to prefer. It
  is a triangulated mesh stored as a stream of OpenGL primitives/commands, and unlike
  STL it can also carry **edges and surface normals** (for nicer rendering) and **extra
  snap/key points** (e.g. circle centres from the original CAD that are otherwise lost
  in triangulation).
- **STL** — the common interchange mesh format; also supported, but without the extra
  edge/normal/snap information.

### Producing an OSD

1. Import a CAD model (the system reads many common CAD formats) into the CAM system.
2. On the **Model** page, select the node (sub‑folder) you want.
3. Use **Save as** and choose the **OSD** format.

The same export is available through the **CAM API** and **CAM IPC** (see the
`cam-api-examples` repository), so model preparation can be scripted.

## 5 Visual vs. collision geometry — keep it light

Right now **the same model is used both for display and for collision checking**
(this may change in future). That means model detail is a trade‑off between looks and
speed — **favour speed**: do not build schemes from over‑detailed CAD. Both the CAM
system and MachineMaker provide a tool that interactively helps strip out invisible,
internal or very small surfaces to simplify a model. (There is no fixed
triangle‑count guideline; simpler is better.)

This also interacts with the *Simulation* settings — *Revolution bodies simulation*
and *Collisions to ignore* — described in
[Machine Setup → Simulation](machine-setup-parameters.md#simulation).

## 6 Colours — `Use3DModelColors`

`VisualProperties` accepts an optional boolean attribute **`Use3DModelColors`**:

- **`False`** (default) — the node is drawn with the `Color` set in its
  `VisualProperties` (the XML descriptor wins).
- **`True`** — the node is drawn with the **colours stored in the 3D model** itself.

```xml
<VisualProperties Use3DModelColors="True">
    <!-- this node keeps the colours baked into its .osd model -->
</VisualProperties>
```

## 7 Ready‑made models

**MachineMaker** has an online library of devices, robots, machines and cells. It
supplies **prepared sets** (models *plus* the extra descriptor information), not loose
model files, and inserts them into the cell description for you — they cannot be loaded
as individual files. So when you prepare a scheme **by hand**, you typically prepare
the models individually for that machine, ending up with the self‑contained, portable
folder described in [§2](#2-where-model-files-live).

---

Back to **[Machine descriptors](machine-descriptors.md)** | [guide index](readme-machines.md)
