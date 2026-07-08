# Derived surfaces

Derived surfaces are built on the basis of objects that have already been created — curves (generatrices, spines) and other surfaces: the source objects are specified by their identifiers, and the result receives a new `ID`.

Types of derived surfaces:

- **[Surface of revolution](revolution-surface.md)** — `CreateRevSurface120`.
- **[Extrusion surface](extrusion-surface.md)** — `CreateTabSurface122`.
- **[Transposed UV surface](transposed-uv-surface.md)** — `CreateTransposedUVSurface`.
- **[Blended surface](blended-surface.md)** — `CreateBlendedSurface`.
- **[Offset surface](offset-surface.md)** — `CreateOffsetSurf`.

## Example of saving a derived surface

To save a derived surface, you must first save all the supporting objects, and only then the surface itself.

```csharp
bool SaveOffsetSurface(string id, CADOffsetParam param)
{
    if (!SaveSurface(param.Surface))
        return false;

    return sgr.CreateOffsetSurf(id, param.Surface.Id, param.Offset);
}
```
