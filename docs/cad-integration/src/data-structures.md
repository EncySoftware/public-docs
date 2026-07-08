# SGF data structures

The base types and structures are declared in `STTypes.idl`. All the method signatures in the following sections are written in terms of them.

| Type | Definition | Purpose |
|-----|-------------|-----------|
| `STFloat` | `double` | Floating-point number: coordinates, radii, angles, parameters, weights. |
| `TST3DPoint` | `record (X, Y, Z: double)` | A point or vector in 3D. When used as a vector (`vZ`, `vX`, `Axis`, `ExtrusionVector`) it specifies a direction. |
| `TST2DPoint` | `record (X, Y: double)` | A point in 2D — in the parametric space of a surface (when building 2D loop curves). |
| `TST3DMatrix` | `record (vX, vY, vZ, vT: TST3DPoint; A, B, C, D: double)` | A transformation matrix / coordinate system: the basis vectors `vX`, `vY`, `vZ`, the origin `vT`, and the coefficients `A`–`D`. |

The signatures also use primitives: `string` — a text identifier (`ID`) or a file path, `integer` — an integer, `boolean` — a flag.

**CAD → SGF conversions in the examples.** The CAD-system types (`CADPoint`, `CADMatrix`, …) do not match the SGF types, so the examples use small conversion functions: `ToPoint` converts a CAD point to `TST3DPoint`, and `ToMatrix` converts a CAD matrix (coordinate system) to `TST3DMatrix`. This is a component-wise copy of the fields; the implementation is trivial and is not given in the examples — only the calls are shown (with explanatory comments).
