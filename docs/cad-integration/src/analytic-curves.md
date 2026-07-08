# Point and analytic curves

Curves are built in a local XY plane: `vT` is the center, `vZ` is the normal (the axis out of the plane), `vX` is the X axis of the local coordinate system, and the Y axis is computed as the cross product of Z and X (so it does not need to be passed). Building a curve starts from the `vX` direction (this is the start point of its parameterization) and proceeds counterclockwise around `vZ`; angles are measured in the same direction. The created objects can either be added to the geometry tree via `AddEntity` or used as building blocks for other objects — for example, as loop curves for trimming surfaces.

Point and analytic curve primitives:

- **[3D point](point-3d.md)** — `CreatePoint`.
- **[Coordinate system](coordinate-system.md)** — `CreateCoordinateSystem`.
- **[Line segment](line-segment.md)** — `CreateLineSeg`.
- **[Circle](circle.md)** — `CreateCircle`.
- **[Circular arc](arc.md)** — `CreateArc`.
- **[Ellipse](ellipse.md)** — `CreateEllipse`.
- **[Elliptical arc](ellipse-arc.md)** — `CreateEllipseArc`.
- **[Conical spiral](conical-spiral.md)** — `CreateConicalSpiral`.
- **[NURBS curve](nurbs-curve.md)** — `StartNurbsCurve` … `CloseNurbsCurve`.
- **[Composite curve](composite-curve.md)** — planar (2D) and spatial (3D).

## Example of saving an analytic curve

`SaveCurve` is a dispatcher: it receives a CAD system curve and, depending on its type, calls the appropriate handler (`SaveLine`, `SaveCircle`, …). Each handler writes the geometry to the SGF with the appropriate call from [Curves and points](curves-and-points.md) and returns a success flag. Below are the dispatcher itself and one of the handlers (`SaveLine`); the rest are structured the same way.

```csharp
// Saves a curve of any type; returns a success flag (Id is already set in CADCurve)
bool SaveCurve(CADCurve curve)
{
    switch (curve.Type)
    {
        case "Line":    return SaveLine(curve.Id, curve.Param);
        case "Circle":  return SaveCircle(curve.Id, curve.Param);      // handlers for the other
        case "Arc":     return SaveArc(curve.Id, curve.Param);         // types are structured the same way
        case "Ellipse": return SaveEllipse(curve.Id, curve.Param);
        case "Nurbs":   return SaveNurbsCurve(curve.Id, curve.Param);
        // … other curve types (see "Curves and points")
        default:        return false;                  // type not supported
    }
}

// One of the handlers — saving a line segment
bool SaveLine(string id, CADLineParam param)
{
    // convert the CAD point coordinates to TST3DPoint
    return sgr.CreateLineSeg(id, ToPoint(param.Start), ToPoint(param.End));
}
```
