# Surfaces

A surface is the **underlying geometry of a face**: from the full (often infinite) surface, a face carves out a bounded region using its contours (see [Face (trimmed surface)](face.md)). This chapter collects the methods for building surfaces: analytic primitives (plane, cylinder, cone, sphere, torus), NURBS surface and polygonal mesh, derived surfaces (of revolution, extrusion, fillet, offset, and others), and their parametrization.

The surface-building methods are grouped into three sections:

- **[Analytic surfaces](analytic-surfaces.md)** — plane, cylinder, cone, sphere, torus, NURBS surface, and polygonal mesh.
- **[Derived surfaces](derived-surfaces.md)** — surfaces of revolution, extrusion, transposed UV, fillet surface, and offset.
- **[Surface parametrization](surface-parametrization.md)** — changing the parametric domain of an already created surface (`SetSurfaceUVDomain`).
