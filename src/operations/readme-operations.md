# Operation XML descriptors

This area covers **the XML descriptors of technological operations** — how to describe
and register an operation, and how the shipped operations are organized. It is not a
full manual of what each operation *does*; it is about authoring and understanding
their XML descriptors. It builds on the
[XMLProperties framework](../xml-properties/readme-xml-framework.md) (read the
[descriptor syntax](../xml-properties/descriptor-syntax.md) and
[expression language](../xml-properties/expression-language.md) first).

- **[Operation XML descriptors](operation-xml-descriptors.md)** — the anatomy of an
  operation descriptor: the registration record, choosing a base type, the header,
  parameters, `ContainerID` / `SolverID`, `MultiGroup`, and where your file goes.
- **[Operation hierarchy reference](operation-hierarchy.md)** — the full inheritance
  tree of every shipped operation (ID, caption, parent, container/solver, source
  file), to help you pick a base type. *Generated — do not hand‑edit.*

See the [XMLProperties framework](../xml-properties/readme-xml-framework.md) for the
shared ground rules (don't edit `Supplement`, where the shipped files live, example
conventions), and the [documentation root](../index.md) for the intended audience.
