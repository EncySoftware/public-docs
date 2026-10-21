# Derived curves

Derived curves are built on top of objects that already exist: the source curve (and, for a curve on a surface, the surface as well) is specified by its identifier, and the result receives a new `ID`. Such curves can be trimmed, inverted, reparameterized, or built on a surface. Like analytical curves, the result can be added to the tree via `AddEntity` or used as a building block (for example, a loop curve for trimming surfaces).
When creating derived objects, the source objects are not changed, but if the same `ID` is used, the new object will overwrite the old one.

Types of derived curves:

- **[Curve on surface](curve-on-surface.md)** — `CreateCurveOnSurface`.
- **[Trimmed curve](trimmed-curve.md)** — `CreateTrimmedCurve` / `CreateTrimmedCurve2`.
- **[Inverted curve](inversed-curve.md)** — `CreateInversedCurve`.
- **[Intersection curve](intersection-curve.md)** — `StartIntersectionCurve` … `CloseIntersectionCurve`.
- **[Blend boundary](blend-bound.md)** — `CreateBlendBound`.

## Example of saving a derived curve

To save a derived curve, you must first save all of its supporting objects and only then save the curve itself.

```csharp
bool SaveTrimmedEdge(string edgeId, CADEdge edge)
{
    // first save the supporting curve
    if (!SaveCurve(edge.Curve))
        return false;

    // then save the trimmed curve itself, based on the supporting curve (by two boundary points;
    // the CAD vertex coordinates are converted to TST3DPoint)
    return sgr.CreateTrimmedCurve2(edgeId, edge.Curve.Id,
                                   ToPoint(edge.Start.Point), ToPoint(edge.End.Point));
}
```
