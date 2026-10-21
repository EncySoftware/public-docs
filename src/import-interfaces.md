# Import interfaces

Geometry import relies on two interfaces of the same COM object of the STGeomFile.dll library (for how to obtain it, see [Connecting STGeomFile.dll](connecting-stgeomfile.md)): `ISTGeomFiler` (`sgf`) manages the file itself, while `ISTGeomReceiver` (`sgr`) writes geometry into it.

## ISTGeomFiler

A pointer to the `ISTGeomFiler` interface is returned by the exported `CreateGeomFiler` function (see [Connecting STGeomFile.dll](connecting-stgeomfile.md)); this interface manages the file:

| Method | Description |
|-------|----------|
| `StartFile(FileName: string)` | Begin building the SGF file (open it for writing). A nested `StartFile` call while a file is already open is not allowed. |
| `CloseFile()` | Close the SGF file. It is at this call that the file is physically built (written to disk). |
| `OpenFile(FileName: string; Receiver: ISTGeomReceiver)` | Open the SGF file for reading; commands are replayed into the specified `ISTGeomReceiver`. This method is used by the CAM system. |

The workflow for working with the file is described in the chapter [Building the SGF file](building-sgf.md).

## ISTGeomReceiver

The main import interface: it receives geometry as a sequence of commands. All methods return a `boolean` — the success status (omitted in the signatures below). Objects are created under a unique string identifier `ID` — subsequent calls reference them by it. The parameter types (`STFloat`, `TST3DPoint`, `TST2DPoint`, and others) are described in [Data structures](data-structures.md).

An object's local coordinate system is usually defined by a triple of points: `vT` — the position (origin), `vZ` — the Z axis, `vX` — the X axis. If the Y axis is **not passed** among the parameters, it is computed internally as the cross product `vZ × vX`, which automatically yields a right-handed coordinate system. In this case `vZ` and `vX` must be mutually perpendicular, otherwise the axis orientation is ambiguous.

Some methods come in pairs: a method with the `Start…` prefix opens a compound object, within which nested methods are called (for example, adding points, edges, or knots), and at the end the object **must** be closed with the matching `Close…`-prefixed method. For example: `StartNurbsCurve` → `SetNurbsCurveControlPoint` / `SetNurbsCurveKnot` / … → `CloseNurbsCurve`; `StartFace` → `StartFaceLoop` → `AddFaceEdge2d` → `CloseFaceLoop` → `CloseFace`. Such pairs may be nested. If an opened `Start…` is not closed with the matching `Close…`, at best the object will be built incorrectly, and at worst the SGF file structure will be corrupted and reading impossible.

> **The referenced object comes before the dependent one.** Regardless of the order of presentation, when writing to SGF each object must be created before the one that references it: a curve before an edge, a surface before a face, faces before a body. In the examples this is ensured by recursion: the top-level method (`SaveClosedShell`, `SaveTrimmedFace`, …) first saves the child objects and then assembles the compound object on top of them.
