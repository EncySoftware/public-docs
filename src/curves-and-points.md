# Curves and points

Methods for building curve geometry: analytic primitives (point, line segment, circle, arc, ellipse, helix, NURBS, composite curves), derived curves (on-surface, trimmed, inverted, intersection) and their parametrization.

**Color.** The current color is set with the `SetCurrentColor(Value: integer)` call. This is a **state**: the specified color applies to all objects created after it — surfaces, curves and points (added through `AddEntity` or `AddComboSolidFace`) — and persists until it is changed by the next call. Therefore `SetCurrentColor` is called **before** each object that needs its own color. If `SetCurrentColor` was not called, the color is not overridden and the object inherits the color of the parent tree node. The value format is a packed integer `Blue shl 16 or Green shl 8 or Red` (8 bits per channel).

**Example: saving curves and points.**

```csharp
void SaveCurves(CADCurve[] curves)
{
    foreach (CADCurve curve in curves)
        if (SaveCurve(curve))                
        {
            sgr.SetCurrentColor(curve.Color);  // the color affects the next AddEntity (and onward, until changed)
            sgr.AddEntity(curve.Id, curve.Name);
        }
}

void SavePoints(CADPoint[] points)
{
    foreach (CADPoint point in points)
    {
        sgr.CreatePoint(point.Id, ToPoint(point));   // convert the CAD point coordinates to TST3DPoint
        sgr.AddEntity(point.Id, point.Name);         // SetCurrentColor was not called — the point inherits the current/parent color
    }
}
```

The curve-building methods are grouped into three sections:

- **[Point and analytic curves](analytic-curves.md)** — point, coordinate system, line segment, circle, arc, ellipse, helix, NURBS curve, composite curves.
- **[Derived curves](derived-curves.md)** — on-surface curve, trimmed, inverted, intersection curve and fillet boundary.
- **[Curve parametrization](curve-parametrization.md)** — changing the range and reparametrizing an already created curve.
