# Working with an assembly

An assembly (`CADAssembly`) is a node of the model tree with a **placement matrix** (`CADMatrix`). The `IsDetail` flag defines the node's contents: when `IsDetail = true`, it holds a part (`CADPart`) with geometry; when `IsDetail = false`, it holds nested assemblies. **Only `CADAssembly` has a matrix**, so any placed component — even a single part (a screw, a washer) — is wrapped in its own `CADAssembly` (which carries its position), and the geometry is stored inside, in a `CADPart`. The same `CADPart` can be reused by many assemblies (patterns, repeated fasteners). Importing an assembly is a recursive top-down traversal of the tree that accumulates the transform.

For example, this is how the "Roller in bracket" node looks in the CAD system's model tree:

```text
Roller in bracket — CADAssembly
├─ Bracket — CADAssembly → CADPart
├─ Axle — CADAssembly → CADPart
├─ Roller — CADAssembly
│  ├─ Bushing — CADAssembly → CADPart
│  └─ Cage — CADAssembly → CADPart
├─ Screw M6 (1) — CADAssembly → CADPart
├─ Screw M6 (2) — CADAssembly → CADPart
├─ Screw M6 (3) — CADAssembly → CADPart
├─ Screw M6 (4) — CADAssembly → CADPart
├─ Washer 6 (1) — CADAssembly → CADPart
├─ Washer 6 (2) — CADAssembly → CADPart
├─ Washer 6 (3) — CADAssembly → CADPart
└─ Washer 6 (4) — CADAssembly → CADPart
```

Each tree node is a `CADAssembly` with its own matrix; the actual geometry appears only in the leaf `CADPart` nodes inside them. The "Roller" is a nested subassembly (`IsDetail = false`). "Screw M6" and "Washer 6" are present in four instances — these are four separate `CADAssembly` nodes (four matrices) that reference the same `CADPart` geometry.

> In the examples below, an assembly node (`CADAssembly`) has the following fields: `Name` — the name (a folder in the tree), `Transform` — the placement matrix (`CADMatrix`), `IsDetail` — the contents flag, and the contents themselves: when `IsDetail = true` — the part `Part` (`CADPart`), when `IsDetail = false` — the list of child nodes `Children`. In Variant 2, leaf nodes also use `ComponentId` — the identifier of the source component, shared by all identical parts (it is used to detect repeats). The exact set of fields depends on your CAD system.

**What needs to be reproduced in SGF.** Importing an assembly solves three tasks: reproduce the tree structure (folders), place each component using its matrix, and write the geometry of the parts (`ComboModel` / `ComboSolid`, see [Working with a part](part.md)). The tree structure is built by **groups**, and repeated components can be reused through **blocks**. Below are both approaches; they are equivalent and are usually combined.

**Group.** Each assembly node is shown in the CAM system's model tree as a folder. The pair of methods `StartGroupEntity` / `CloseGroupEntity` opens and closes such a folder: all objects written between the calls belong to it. The calls are nested — exactly the way the nodes of the CAD assembly tree are nested.

| Method | Description |
|-------|----------|
| `StartGroupEntity(EntityName: string)` | Begin a group — a folder in the model tree with the name `EntityName`. All objects built before the paired `CloseGroupEntity` go into this folder. The calls can be nested: nested folders are created inside a folder. It cannot be called inside `StartComboModel`, because that builds a separate closed stitched shell. |
| `CloseGroupEntity()` | Close the current group (folder). |

**Transformation matrix**. A component's position is set before its geometry is saved. The matrix is set with the `SetCurrentTransform2` method, and all subsequent surfaces — until the next matrix change — are multiplied by it. During assembly traversal, the node's **accumulated world transform** (the product of the matrices from the root) is passed into the matrix, so each solid is given its final position.

The matrix is called **before** opening a solid — before `StartGroupEntity` or `StartComboModel`. It cannot be changed inside `StartComboModel`: the body is stitched in its own coordinates and placed as a whole according to the matrix set before it was opened (see [Working with a part](part.md)).

| Method | Description |
|-------|----------|
| `SetCurrentTransform2(vT, vX, vY, vZ: TST3DPoint)` | Switches the transformation matrix for all subsequent objects; it is defined by a position (`vT` — the origin) and explicitly specified axes `vX`, `vY`, `vZ`. It must be called before saving a solid (before `StartGroupEntity` or `StartComboModel`) — all of its surfaces will be multiplied by this matrix. When saving assemblies, the final matrix is set for each solid. It cannot be called inside `StartComboModel`. |
| `SetCurrentTransform(vT, vZ, vX: TST3DPoint)` | **Deprecated** (but still used in some cases). The same as `SetCurrentTransform2`, but the coordinate system is defined by a position (`vT`), the Z axis (`vZ`), and the X axis (`vX`); the Y axis is computed as the cross product `vZ × vX` — which is ambiguous if `vZ` and `vX` are not strictly perpendicular. Where possible, use `SetCurrentTransform2`. |

**Variant 1 — standard traversal (groups).** The simplest approach: each assembly node is wrapped in `StartGroupEntity` / `CloseGroupEntity`, and the part's geometry is written inside. The placement matrix is accumulated along the path from the root: each node's world transform = the parent's transform × the node's local matrix.

```csharp
// Recursive traversal of the assembly. parentTransform is the parent's accumulated transform.
void SaveAssembly(CADAssembly asm, TST3DMatrix parentTransform)
{
    // node's world transform = parent's transform × the assembly's local matrix
    TST3DMatrix world = Multiply(parentTransform, ToMatrix(asm.Transform));

    sgr.StartGroupEntity(asm.Name);
    try
    {
        if (asm.IsDetail)
            SavePart(asm.Part, world);                 // leaf: a part with geometry
        else
            foreach (CADAssembly child in asm.Children)
                SaveAssembly(child, world);            // subassembly: descend into child nodes
    }
    finally
    {
        sgr.CloseGroupEntity();
    }
}
```

This variant is suitable for most cases. Downside: if the same component appears in the assembly many times (for example, four identical bolts), its geometry is written to the file four times. Variant 2 is intended for such cases.

**Variant 2 — blocks (Blocks).** A block is a single model with topology (`ComboModel`) or without, written to SGF **once** under a unique name and inserted into the tree any number of times through `InsertBlock`. The geometry is stored once; each instance only specifies a placement matrix. For components that appear more than once, this reduces the file size and speeds up loading.

* **subassembly** (`IsDetail = false`) — an ordinary `StartGroupEntity` / `CloseGroupEntity` folder (as in Variant 1) with recursive traversal of the child nodes;
* **part** (`IsDetail = true`) — saved as a block: at the **first** occurrence of the component its geometry is written into a block (`StartBlock` / `CloseBlock`) and immediately placed with `InsertBlock`; at **subsequent** occurrences only `InsertBlock` is called. Already written blocks are tracked by the `savedBlocks` set (in the STEP importer — the `fShellSaved` flag); pre-counting the repeats is not needed.

`InsertBlock` itself creates a node in the model tree (its `NewBlockName` argument is the name of that node), so there is no need to wrap the node in an additional `StartGroupEntity`.

**Block methods.**

| Method | Description |
|-------|----------|
| `StartBlock(BlockName: string)` | Begin a block — register, under the name `BlockName`, a single model with topology (`ComboModel`) or without, for later reuse. The geometry inside the block is written by the same methods as for a single part (see [Working with a part](part.md)). The block is placed in a buffer. |
| `CloseBlock()` | Finish building the block (it remains in the buffer). |
| `InsertBlock(BlockID, NewBlockName: string)` | Copy a block from the buffer into the model tree. `BlockID` is the block name from `StartBlock`; `NewBlockName` is the name of the node (group) being created in the tree. The placement matrix is set by a preceding call to `SetCurrentTransform2`. |

```csharp
// savedBlocks — the ComponentIds of blocks already written (an importer field; analogous to fShellSaved in STEP).
readonly HashSet<string> savedBlocks = new HashSet<string>();

void SaveAssemblyWithBlocks(CADAssembly asm, TST3DMatrix parentTransform)
{
    TST3DMatrix world = Multiply(parentTransform, ToMatrix(asm.Transform));

    if (!asm.IsDetail)
    {
        sgr.StartGroupEntity(asm.Name);
        try
        {
            foreach (CADAssembly child in asm.Children)
                SaveAssemblyWithBlocks(child, world);
        }
        finally 
        { 
            sgr.CloseGroupEntity(); 
        }
        return;
    }

    // leaf (part): at the first occurrence of the component create a block, afterwards just insert it
    if (savedBlocks.Add(asm.ComponentId))   
    {
        sgr.StartBlock(asm.ComponentId);
        try 
        { 
            SavePart(asm.Part, UnitMatrix3D); 
        }   // geometry in the part's local coordinates
        finally 
        { 
            sgr.CloseBlock(); 
        }
    }
    // place the instance by its matrix (including at the first occurrence)
    sgr.SetCurrentTransform2(world.vT, world.vX, world.vY, world.vZ);
    sgr.InsertBlock(asm.ComponentId, asm.Name);    // InsertBlock itself creates the tree node
}
```

> **Both variants are equivalent** and can be combined in a single importer. Variant 1 is simpler to implement and debug; Variant 2 gives a smaller SGF file for assemblies with repeated parts and loads faster. In the example above, parts are formed as blocks (repeated geometry is written once and reused), while subassemblies and assembly nodes remain group folders.
