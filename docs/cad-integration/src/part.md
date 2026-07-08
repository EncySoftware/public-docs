# Working with a part

A part (`CADPart`) consists of **bodies** (`CADBody`) and may also contain individual curves, points, and PMI. A body is a shell of faces. A **closed** body (a solid) is saved separately via `ComboSolid`, which provides **stitching**: the faces, vertices, and edges of the shell are written inside the `ComboModel` → `ComboSolid` pair, and on load the CAM system assembles them into a single solid. Open shells, as well as individual curves and points, do not go into `ComboSolid` — they are added to the model tree directly via `AddEntity` (see below).

**Why stitch the model.** The full topology of the body comes from the CAD model — surfaces, edges, and vertices together with the relationships between them. `ComboSolid` transfers these relationships to the SGF **without loss**: the CAM receives the same connected topology (B-rep) with well-defined "inside/outside" and face adjacency that existed in the CAD, and it does not need to find and guess the joints again.

Faces are added to the body after they have been created via `StartFace` ([Face (trimmed surface)](face.md)); the relationships along shared edges and vertices define the stitching.

| Method | Description |
|-------|----------|
| `StartComboModel(GeomFile: string)` | Begin a model with topology (it will be "stitched"). `GeomFile` is the unique model name. |
| `StartComboSolid(ID: string)` | Begin a body inside the `ComboModel`. |
| `AddComboSolidVertex(p: TST3DPoint; VertexID: string)` | Add a body vertex `p` under the identifier `VertexID` (edges refer to it). |
| `AddComboSolidEdge(EdgeID, CurveID, StartVertexID, EndVertexID, LeftFaceID, RightFaceID: string)` | A body edge between vertices `StartVertexID`…`EndVertexID`, separating the left (`LeftFaceID`) and right (`RightFaceID`) faces — it is exactly this relationship that defines the stitching. `CurveID` **is usually better passed empty**: a topological edge does not really need its own geometry — it is already localized by the joint of the left and right surfaces. If `CurveID` is passed, during stitching the engine will try to insert the geometry of the specified curve, and that curve does not always account for the fact that the edge may be split into several during stitching. |
| `AddComboSolidFace(FaceID, FaceName: string)` | Add a previously created (via `StartFace`) face. |
| `CloseComboSolid()` | Close the body. |
| `CloseComboModel()` | Close the model. |

**Unique identifiers and associativity.** For topological elements — faces, edges, and vertices — it is critical to assign **unique identifiers**. Elements refer to each other by them (an edge refers to its two faces and two vertices, and so on), and this provides **associativity**: after stitching and subsequent recomputations, the CAM can unambiguously match an operation to a specific face rather than "losing" it. Therefore, the identifiers must be unique and stable.

The unique identifiers themselves are provided by the CAD system: every topological element in its model has its own persistent identifier that is preserved between rebuilds. The Translator does not need to generate identifiers itself — it is enough to take the element's native identifier from the CAD system's API and pass it into the SGF. This guarantees both uniqueness and stability: on re-importing a modified model, the unchanged elements will keep the same identifiers, and the operation bindings will not break.

**Example: saving a part.** The `SavePart` method, called while traversing the assembly ([Working with an assembly](assembly.md)), receives the part and its world matrix, sets the current transform, and saves its contents — bodies, individual curves, points, and PMI. It is convenient to wrap the part itself in a model tree folder (`StartGroupEntity`, [Working with an assembly](assembly.md)) — here this is an **organizational folder**, not stitching.

```csharp
void SavePart(CADPart part, TST3DMatrix transform)
{
    sgr.SetCurrentTransform2(transform.vT, transform.vX, transform.vY, transform.vZ);

    sgr.StartGroupEntity(part.Name);
    try
    {
        SaveBodies(part.Bodies);   // closed bodies — via ComboSolid, open ones — via AddEntity
        SaveCurves(part.Curves);   // curves, see "Curves and points"
        SavePoints(part.Points);   // points, see "Curves and points"
        SavePMI(part.PMIs);        // PMI (threads, etc.), see "PMI"
    }
    finally 
    { 
        sgr.CloseGroupEntity(); 
    }
}

void SaveBodies(CADBody[] bodies)
{
    foreach (CADBody body in bodies)
    {
        if (body.IsClosed)
            SaveClosedShell(body);   // closed body → ComboSolid (stitching)
        else
            SaveOpenShell(body);     // open shell → AddEntity
    }
}

// An open shell is not a body: faces are added to the tree directly via AddEntity, outside of ComboModel.
void SaveOpenShell(CADBody body)
{
    sgr.StartGroupEntity(body.Name);   // shell folder in the model tree
    try
    {
        foreach (CADFace face in body.Faces)
            if (SaveTrimmedFace(face))      // creates a face under face.Id (see "Face")
                sgr.AddEntity(face.Id, face.Name);
    }
    finally 
    { 
        sgr.CloseGroupEntity(); 
    }
}

// A closed shell → one ComboSolid inside a ComboModel; the ComboSolid itself provides the stitching.
void SaveClosedShell(CADBody body)
{
    sgr.StartComboModel(body.Id);
    try
    {
        sgr.StartComboSolid(body.Id);
        try
        {
            // 1) shell faces: save each one and add it to the body
            foreach (CADFace face in body.Faces)
                if (SaveTrimmedFace(face))
                    sgr.AddComboSolidFace(face.Id, face.Name);

            // 2) body vertices (edges refer to them by Id); convert coordinates to TST3DPoint
            foreach (CADVertex vertex in body.Vertices)
                sgr.AddComboSolidVertex(ToPoint(vertex.Point), vertex.Id);

            // 3) body edges: which faces (left/right) meet at a shared edge — that is the stitching
            foreach (CADEdge edge in body.Edges)
                sgr.AddComboSolidEdge(edge.Id, "",
                                      edge.Start.Id, edge.End.Id,
                                      edge.LeftFaceId, edge.RightFaceId);
        }
        finally 
        { 
            sgr.CloseComboSolid(); 
        }
    }
    finally 
    { 
        sgr.CloseComboModel(); 
    }
}
```

> `body.Vertices` and `body.Edges` are the body's topology: vertices with coordinates (`Point`) and identifiers (`Id`); each edge (`CADEdge`) stores its end vertices (`Start`, `End`) and the identifiers of the adjacent faces (`LeftFaceId`, `RightFaceId`). Vertices are added before edges — an edge refers to them by `Id`. An empty string is passed for `CurveID`: as in the STEP importer, the edge geometry is carried by the faces.

**Open shells, curves, and points.** Not everything in a part is a closed body. An open shell (`body.IsClosed == false`), individual 3D curves, and points do not go into `ComboSolid`: putting an open shell into a `ComboSolid` is pointless — there is nothing to stitch, no closed body will result — and it does not work with curves and points at all. Such objects are created **outside** `StartComboModel` and added to the model tree directly with a call to `AddEntity(ID, EntityName)` ([Working with an assembly](assembly.md)) — under the same `ID` the object was created with (see `SaveOpenShell` / `SaveCurves` / `SavePoints` in the example above). Placement, if needed, is defined by the `SetCurrentTransform2` matrix before `AddEntity`.

| Method | Description |
|-------|----------|
| `AddEntity(ID: string; EntityName: string)` | Add a previously created entity to the model tree by its `ID` (a face, curve, or point) under the name `EntityName`. Its local coordinates are multiplied by the matrix set via `SetCurrentTransform2`. The method can also be called inside a `ComboModel` — the entity will go into the tree as a standalone object, outside the stitching (faces are added into the body's stitching by `AddComboSolidFace`). |
