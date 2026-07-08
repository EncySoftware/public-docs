# Analytic surfaces

Surfaces are created under a unique `ID`. For analytic primitives (plane, cylinder, cone, sphere, torus) the placement is specified in the same way by a triple: `Location` — position (`vT`), `Axis` — the Z axis (`vZ`), `RefAxis` — the X axis (`vX`); the Y axis is computed as the cross product `Axis × RefAxis`. Besides the analytic primitives, this group also includes the NURBS surface and the polygonal mesh (Mesh).

Some analytic surfaces are mathematically infinite — a plane is unbounded, and a cylinder and a cone are unbounded along their axis. For that reason they must be bounded when created: for a plane the region is given by a rectangle `xMin…xMax` × `yMin…yMax`, for a cylinder and a cone by axial bounds `Hmin…Hmax` (and, if needed, an angular sector `Amin…Amax`). If the CAD system does not provide explicit bounds, it is reasonable to bound the surface by the extents of the whole model. (A sphere and a torus are closed and do not need any additional bounding.)

Analytic surface primitives:

- **[Plane](plane.md)** — `CreatePlaneP`.
- **[Cylinder](cylinder.md)** — `CreateCylinderP`.
- **[Cone](cone.md)** — `CreateConeP`.
- **[Sphere](sphere.md)** — `CreateSphereP`.
- **[Torus](torus.md)** — `CreateTorusP`.
- **[NURBS surface](nurbs-surface.md)** — `StartNurbsSurface` … `CloseNurbsSurface`.
- **[Polygonal mesh](mesh.md)** — `StartMesh` … `CloseMesh`.

## Example of saving an analytic surface

`SaveSurface` is a dispatcher: it receives a CAD-system surface and, depending on its type, calls the corresponding handler (`SavePlane`, `SaveCylinder`, …). Each handler writes the geometry to SGF with the appropriate call from [Surfaces](surfaces.md) and returns a success flag. Below are the dispatcher itself and one of the handlers (`SavePlane`); the others are organized in the same way.

```csharp
// Saves a surface of any type; returns a success flag (Id is already set in CADSurface)
bool SaveSurface(CADSurface surf)
{
    switch (surf.Type)
    {
        case "Plane":    return SavePlane(surf.Id, surf.Param);
        case "Cylinder": return SaveCylinder(surf.Id, surf.Param);    // handlers for the other
        case "Cone":     return SaveCone(surf.Id, surf.Param);        // types are organized the same way
        case "Sphere":   return SaveSphere(surf.Id, surf.Param);
        case "Torus":    return SaveTorus(surf.Id, surf.Param);
        case "Nurbs":    return SaveNurbsSurface(surf.Id, surf.Param);
        case "Mesh":     return SaveMesh(surf.Id, surf.Param);
        // … other surface types (see "Surfaces")
        default:         return false;                  // type not supported
    }
}

// One of the handlers — saving a plane
bool SavePlane(string id, CADPlaneParam param)
{
    // convert the CAD direction points to TST3DPoint (Xmin/Ymin/Xmax/Ymax are numbers)
    return sgr.CreatePlaneP(id, ToPoint(param.Location), ToPoint(param.Axis), ToPoint(param.RefAxis),
                            param.Xmin, param.Ymin, param.Xmax, param.Ymax);
}
```
