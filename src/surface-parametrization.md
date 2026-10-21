# Surface parametrization

`SetSurfaceUVDomain(ID: string; SrcUmin, SrcUmax, SrcVmin, SrcVmax, PrxUmin, PrxUmax, PrxVmin, PrxVmax: STFloat; TransposeUV: boolean)` — change the parametrization of an already created surface by its identifier. No new object is created: the surface is wrapped in a **proxy** that defines a **linear remapping** between two U/V parameter ranges.

- `ID` — surface identifier;
- `SrcUmin`, `SrcUmax` / `SrcVmin`, `SrcVmax` — the **Src** range: the parametric space in which the surface is "seen" from the outside — the one in which the loop coordinates of the face referencing this surface are given;
- `PrxUmin`, `PrxUmax` / `PrxVmin`, `PrxVmax` — the **Prx** range: the space into which the external parameter is remapped for evaluating the surface itself (for NURBS — the knot range, *knot-span*);
- `TransposeUV` — when `true`, the U and V axes are swapped (for example, when the U/V order in the CAD system does not match the one used in SGF — as happens for a torus).

**Why this is needed.** Some CAD systems store the loop of a face in one parametric space, while defining the underlying surface in another. If they are not reconciled, the CAM system will project the loop to the wrong place, and the face will be built incorrectly. `SetSurfaceUVDomain` defines the linear correspondence Src↔Prx, and the loop is projected correctly.

A special case is **surface extension**: when the parametric domain of the face is **wider** than the natural domain of the surface. This is what import from KOMPAS does for NURBS faces: the actual range of the face (`MathSurface.ParamU/V`) extends beyond the NURBS knot range. The proxy "stretches" the surface over the entire domain of the face, and the face loop is projected onto the NURBS correctly. But if the face domain lies entirely within the knot range (ordinary "trimming inside a NURBS", a typical fillet) — reparametrization is not needed, otherwise it would only distort the geometry.

**Example: aligning the parametrization of a surface.**

```csharp
// Align the parametrization of a face and its underlying NURBS surface (following the KOMPAS import pattern).
void AlignSurfaceUVDomain(string surfaceId, CADFace face)
{
    CADSurface surf = face.Surface;

    // Src — the UV space in which the face loops are given
    double srcUmin = face.ParamUMin, srcUmax = face.ParamUMax;
    double srcVmin = face.ParamVMin, srcVmax = face.ParamVMax;

    // Prx — the natural domain of the surface (for NURBS — the knot range)
    double prxUmin = surf.KnotUMin, prxUmax = surf.KnotUMax;
    double prxVmin = surf.KnotVMin, prxVmax = surf.KnotVMax;

    // If the face domain lies entirely within the surface domain, this is ordinary
    // "trimming inside a NURBS", and reparametrization would only distort the geometry.
    const double eps = 1e-9;
    bool insideU = srcUmin >= prxUmin - eps && srcUmax <= prxUmax + eps;
    bool insideV = srcVmin >= prxVmin - eps && srcVmax <= prxVmax + eps;
    if (insideU && insideV)
        return;

    // Otherwise the face domain is wider — the proxy extends the surface over its entire range
    // (TransposeUV = false: the U/V axes are not swapped).
    sgr.SetSurfaceUVDomain(surfaceId,
                           srcUmin, srcUmax, srcVmin, srcVmax,
                           prxUmin, prxUmax, prxVmin, prxVmax,
                           false);
}
```
