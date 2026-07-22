# Machine descriptors

This area covers **describing a machine** — its file layout, kinematic scheme and the
parameters that drive how its toolpath becomes NC code. It builds on the
[XMLProperties framework](../xml-properties/readme-xml-framework.md).

Most machines are built interactively with the **MachineMaker** application; the guides
here are for understanding a machine and for the special cases still authored, or
fine‑tuned, by hand.

- **[Machine descriptors](machine-descriptors.md)** — start here: a machine's file
  layout, a complete simple example, the kinematic node chain, and each section of the
  descriptor (Description, Control Parameters, Schema, state parameters, Tooling,
  Machine dimensions).
- **[Machine node reference](node-reference.md)** — the look‑up companion: the full
  property tables for every node type (`TMachineNode`, `TMachineAxis`, connectors, state
  parameters, `VisualProperties`), plus coordinate conventions and units.
- **[Machine Setup parameters reference](machine-setup-parameters.md)** — what every
  parameter on the machine's *Control Parameters* tab does, each with the XML fragment
  that overrides it.
- **[Advanced machine topics](advanced-topics.md)** — node matrices, switchable /
  detachable nodes, turrets, tool/workpiece connectors, sub‑machines and control
  channels.
- **[3D models for machines](3d-models.md)** — preparing, referencing and aligning the
  node geometry (`.osd` / `.stl`).

See the [XMLProperties framework](../xml-properties/readme-xml-framework.md) for the
shared ground rules (don't edit `Supplement`, where the shipped files live, example
conventions), and the [documentation root](../index.md) for the intended audience.
