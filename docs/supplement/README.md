# CAM System Customization Reference

This folder holds developer / integrator documentation for **customizing the CAM
system by editing its declarative XML** — adding your own operations, machines and
defaults — together with related topics. It is intended for **OEMs, integrators and
partners**, and for **advanced users** who customize the system.

Everything here is built on one foundation — the **XMLProperties** framework, which
describes the system's configurable objects declaratively. **Start with the framework**
(it also covers the shared ground rules every area relies on), then move on to the
operation‑ and machine‑specific areas.

## Documentation areas

- **[XMLProperties framework](xml-properties/readme-xml-framework.md)** — **start
  here:** the declarative property framework itself (mental model, descriptor syntax,
  expression language, using properties from code, user defaults) **and the shared
  ground rules** every area relies on — why you don't edit `Supplement`, where the
  shipped files live, and the conventions used in the examples.
- **[Operation XML descriptors](operations/readme-operations.md)** — describing and
  registering technological operations, plus the full operation inheritance tree.
- **[Machine descriptors](machines/readme-machines.md)** — describing a machine: its
  file layout, kinematic scheme, *Machine Setup* parameters, advanced topics and 3D
  models.

The `Supplement/docs` folder may also host unrelated documentation; everything about the
XMLProperties framework and its descriptors lives under the areas listed above.
