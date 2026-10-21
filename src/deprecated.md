# Deprecated and unused methods

> **Deprecated / unused.** The methods below are not in use and are kept only for reference and backward compatibility. There is no need to call them in new Add-ins.

They are grouped by area — in the same order as the current chapters: file → solid → curves → surfaces → PMI.

## Model parameter initialization

A pair of methods that used to initialize the importer parameters before reading SGF. The functionality has been moved into `StartFile`.

| Method | Description |
|-------|----------|
| `StartModel()` | Initialize the importer parameters (after `StartFile`). |
| `CloseModel()` | Reset the parameters (before `CloseFile`). |

## Solid assembly

The old way of building a solid without `ComboSolid` ([Working with a part](part.md)): the vertices and edges of the solid were declared directly, and a group of faces was marked as a closed shell for stitching by the CAM system. Replaced by `ComboSolid`.

| Method | Description |
|-------|----------|
| `CreateSolidVertex(ID: string; P: TST3DPoint)` | A solid vertex (end point of an edge). |
| `CreateSolidEdge(ID, SourceCurveID, svID, tvID: string)` | A named edge between the vertices `svID`…`tvID` based on the curve `SourceCurveID`. |
| `SetGroupEntityIsSolid(Value: boolean)` | Stitching flag: marks the surfaces inside the current folder (`StartGroupEntity`) as a closed shell. |

## Line properties

The type and width of the line for subsequent objects. Not used in SGF.

| Method | Description |
|-------|----------|
| `SetCurrentLineType(Value: TSTLineType)` | Line type (see `TSTLineType`). |
| `SetCurrentLineWidth(Value: integer)` | Line width. |

The `TSTLineType` enumeration: `ltSolid`, `ltDash`, `ltDashDot`, `ltDot`.

## Ignoring out-of-range parameters

Controlled whether the surface is evaluated beyond its domain of definition (the U/V parameter range). **No need to call:** with correct input data the point parameters do not go beyond the surface range, so the flag is not required.

| Method | Description |
|-------|----------|
| `SetIgnoreOutOfRange(Value: boolean)` | A one-shot flag: it is set before creating a surface, applies only to the single next surface, and is then reset. `true` — out-of-range is ignored (the surface is extrapolated beyond its boundaries); `false` — the range is strictly enforced. |

## PMI annotations

The old mechanism for building PMI views and annotations. The current PMI mechanism is described in [PMI (Product Manufacturing Information)](pmi.md).

| Method | Description |
|-------|----------|
| `CreateView(vT, vZ, vX: TST3DPoint; Scale: STFloat; id: string)` | Create a PMI view. |
| `AddViewEntity(ViewID, EntityPath: string)` | Attach an entity to a view. |
| `BeginPmiEntity(id: string; vT, vZ, vX: TST3DPoint; PmiType: TSTPmiType)` | Begin a PMI annotation (see `TSTPmiType`). |
| `PmiAddArrow(vT: TST3DPoint; Angle: STFloat; ArrowType: TSTPmiArrowType)` | Add an arrow (see `TSTPmiArrowType`). |
| `BeginPmiText(vT: TST3DPoint; Angle, Height, Length: STFloat; NumberLines: integer; TextType: TSTPmiTextType)` | Begin a text block (see `TSTPmiTextType`). |
| `AddPmiText(Text: string)` | Add a line of text. |
| `EndPmiText()` | Finish the text block. |
| `PmiAddCurve(CurveID: string; CurveType: TSTPmiCurveType)` | Add a curve (see `TSTPmiCurveType`). |
| `PmiAddMesh(ID: string)` | Add a mesh to the annotation. |
| `SetPmiPreferenceI(Path: string; Value: integer)` | Integer annotation parameter. |
| `SetPmiPreferenceD(Path: string; Value: STFloat)` | Double annotation parameter. |
| `SetPmiAssociativity(i: integer; ObjId: string)` | Attach the i-th anchor object to the annotation. |
| `EndPmiEntity()` | Finish the PMI annotation. |

PMI enumerations:

| Enum | Values / purpose |
|------|----------------------|
| `TSTPmiType` | Types of PMI annotations (28 values: dimensions, leaders, notes, etc.). |
| `TSTPmiCurveType` | Types of PMI curves (15 values). |
| `TSTPmiArrowType` | Types of PMI arrows (22 values). |
| `TSTPmiTextType` | Types of PMI text (14 values). |
