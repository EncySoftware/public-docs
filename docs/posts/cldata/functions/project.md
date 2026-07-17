# Project information (Project operator)

Part of CLData is project-level data - information that relates to the whole CAM project rather than to an individual operation (the machine schema, the parts and workpieces, setup stages, and so on). A postprocessor reads it with the sppx **Project** operator or the .NET `ICLDProject` object. The catalogue of the available project properties and their meaning is described in [Project information in CLData](../project-information.md).

## Access from sppx

The **Project** operator allows you to get access from the code of the postprocessor to the information about the CAM system project (information that relates to the entire project, and not to individual operations), which lies in the CLData. Operator syntax is as follows.

```text
Project.Ptr|Str|Int|Flt["ParameterName"]
```

Here, Project is the key word to access CAM system project level parameters.

Ptr or Str or Int or Flt is a keyword that defines the form in which you want to represent the value of a property - as a string, as an integer, as a floating point number, or as a pointer to a property. Read more about this in [Named CLData parameters](named-parameters.md) topic.

Further in square brackets follows the string identifier of the property whose value is to be obtained. It can be a string constant, as shown here, as well as any string expression or variable.

For a description of possible properties and their values, see the appendix in the [Project information in CLData](../project-information.md) article.

Consider an **example** of obtaining information about the workpiece using this operator.

```pascal
                    PrintAllWorkpiece
sub PrintAllWorkpiece
  i: Integer
  j: Integer
  px, py, pz, pv: Real
  for i = 1 to Project.Ptr["Parts"].ItemCount do begin
    Output "( Part" + str(i) + ".Workpiece )"
    for j = 1 to Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].ItemCount do begin
      Output "(     Primitive " + str(j) + " )"
      case Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Int["PrimitiveType"] of
        0: begin !Unknown
          Output "(         Type: Unknown )"
        end
        1: begin !Empty
          Output "(         Type: Empty workpiece )"
        end
        2: begin !Faces
          Output "(         Type: Faces )"
          px = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Box.Min.X"]
          py = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Box.Min.Y"]
          pz = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Box.Min.Z"]
          Output "(         Min point: (" + str(px) + ", " + str(py) + ", " + str(pz) + " ) )"
          px = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Box.Max.X"]
          py = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Box.Max.Y"]
          pz = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Box.Max.Z"]
          Output "(         Max point: (" + str(px) + ", " + str(py) + ", " + str(pz) + " ) )"
        end
        3: begin !Casting
          Output "(         Type: Casting )"
          pv = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Stock"]
          Output "(         Stock: " + str(pv) + " )"
          px = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Box.Min.X"]
          py = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Box.Min.Y"]
          pz = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Box.Min.Z"]
          Output "(         Min point: (" + str(px) + ", " + str(py) + ", " + str(pz) + " ) )"
          px = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Box.Max.X"]
          py = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Box.Max.Y"]
          pz = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Box.Max.Z"]
          Output "(         Max point: (" + str(px) + ", " + str(py) + ", " + str(pz) + " ) )"
        end
        4: begin !Box
          Output "(         Type: Box )"
          px = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Min.X"]
          py = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Min.Y"]
          pz = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Min.Z"]
          Output "(         Min point: (" + str(px) + ", " + str(py) + ", " + str(pz) + " ) )"
          px = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Max.X"]
          py = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Max.Y"]
          pz = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Max.Z"]
          Output "(         Max point: (" + str(px) + ", " + str(py) + ", " + str(pz) + " ) )"
        end
        5: begin !RevBody
          Output "(         Type: Turn envelope )"
          px = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Origin.X"]
          py = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Origin.Y"]
          pz = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Origin.Z"]
          Output "(         Origin: (" + str(px) + ", " + str(py) + ", " + str(pz) + " ) )"
          px = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Axis.X"]
          py = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Axis.Y"]
          pz = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Axis.Z"]
          Output "(         Axis: (" + str(px) + ", " + str(py) + ", " + str(pz) + " ) )"
        end
        6: begin !Cylinder
          Output "(         Type: Cylinder )"
          px = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Origin.X"]
          py = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Origin.Y"]
          pz = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Origin.Z"]
          Output "(         Origin: (" + str(px) + ", " + str(py) + ", " + str(pz) + " ) )"
          px = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Axis.X"]
          py = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Axis.Y"]
          pz = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Axis.Z"]
          Output "(         Axis: (" + str(px) + ", " + str(py) + ", " + str(pz) + " ) )"
          pv = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["HMin"]
          Output "(         Min level: " + str(pv) + " )"
          pv = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["HMax"]
          Output "(         Max level: " + str(pv) + " )"
          pv = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["ROut"]
          Output "(         Outer radius: " + str(pv) + " )"
        end
        7: begin !Tube
          Output "(         Type: Tube )"
          px = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Origin.X"]
          py = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Origin.Y"]
          pz = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Origin.Z"]
          Output "(         Origin: (" + str(px) + ", " + str(py) + ", " + str(pz) + " ) )"
          px = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Axis.X"]
          py = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Axis.Y"]
          pz = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Axis.Z"]
          Output "(         Axis: (" + str(px) + ", " + str(py) + ", " + str(pz) + " ) )"
          pv = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["HMin"]
          Output "(         Min level: " + str(pv) + " )"
          pv = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["HMax"]
          Output "(         Max level: " + str(pv) + " )"
          pv = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["ROut"]
          Output "(         Outer radius: " + str(pv) + " )"
          pv = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["RInn"]
          Output "(         Inner radius: " + str(pv) + " )"
        end
        8: begin !Prism
          Output "(         Type: Prism )"
          px = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Origin.X"]
          py = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Origin.Y"]
          pz = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Origin.Z"]
          Output "(         Origin: (" + str(px) + ", " + str(py) + ", " + str(pz) + " ) )"
          px = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Axis.X"]
          py = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Axis.Y"]
          pz = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Axis.Z"]
          Output "(         Axis: (" + str(px) + ", " + str(py) + ", " + str(pz) + " ) )"
          pv = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["HMin"]
          Output "(         Min level: " + str(pv) + " )"
          pv = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["HMax"]
          Output "(         Max level: " + str(pv) + " )"
        end
        9: begin !PolygonalPrism
          Output "(         Type: Polygonal prism )"
          px = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Origin.X"]
          py = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Origin.Y"]
          pz = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Origin.Z"]
          Output "(         Origin: (" + str(px) + ", " + str(py) + ", " + str(pz) + " ) )"
          px = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Axis.X"]
          py = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Axis.Y"]
          pz = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Axis.Z"]
          Output "(         Axis: (" + str(px) + ", " + str(py) + ", " + str(pz) + " ) )"
          pv = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Int["CornerCount"]
          Output "(         Corner count: " + str(pv) + " )"
          pv = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["RInn"]
          Output "(         Inscribed radius: " + str(pv) + " )"
          pv = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["Angle"]
          Output "(         Angle around axis: " + str(pv) + " )"
          pv = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["HMin"]
          Output "(         Min level: " + str(pv) + " )"
          pv = Project.Ptr["Parts"].Item[i].Ptr["Workpiece"].Item[j].Flt["HMax"]
          Output "(         Max level: " + str(pv) + " )"
        end
        else begin
          Output "(         Type: Something else )"
        end
      end
    end
  end
subend
```

The result of this subroutine may be the following text block.

```text
                    Results
( Part1.Workpiece )
(     Primitive 1 )
(         Type: Tube )
(         Origin: (0, 0, 117.5 ) )
(         Axis: (0, 0, 1 ) )
(         Min level: -149.5 )
(         Max level: 149.5 )
(         Outer radius: 66 )
(         Inner radius: 29 )
(     Primitive 2 )
(         Type: Cylinder )
(         Origin: (0, 0, 117.5 ) )
(         Axis: (0, 0, 1 ) )
(         Min level: -147.5 )
(         Max level: 147.5 )
(         Outer radius: 64 )
(     Primitive 3 )
(         Type: Turn envelope )
(         Origin: (0, 0, 117.5 ) )
(         Axis: (0, 0, 1 ) )
(     Primitive 4 )
(         Type: Box )
(         Min point: (-64, -64, -30 ) )
(         Max point: (64, 64, 265 ) )
(     Primitive 5 )
(         Type: Casting )
(         Stock: 1 )
(         Min point: (-65, -65, -31 ) )
(         Max point: (65, 65, 266 ) )
(     Primitive 6 )
(         Type: Faces )
(         Min point: (-54, -54, -30 ) )
(         Max point: (54, 54, 265 ) )
(     Primitive 7 )
(         Type: Polygonal prism )
(         Origin: (0, 0, 117.5 ) )
(         Axis: (0, 1, 0 ) )
(         Corner count: 6 )
(         Inscribed radius: 160.786 )
(         Angle around axis: 0 )
(         Min level: -64 )
(         Max level: 64 )
(     Primitive 8 )
(         Type: Empty workpiece )
```

## Access from .NET

The project is available to a handler as the `CLDProject` object (`ICLDProject`); it is also passed to `OnStartProject` / `OnFinishProject`. `ICLDProject` implements the common [named-property model](named-parameters.md), so the project properties are read exactly as with the sppx **Project** operator - `CLDProject.Ptr["Parts"]`, `CLDProject.Flt["..."]`, `CLDProject.Arr["Parts"][i]...` - with the same dotted/bracketed names. Besides the named properties it exposes:

| .NET (`ICLDProject`) | Description |
|---|---|
| `CLDProject.ProjectName` | the project name (without a file path) |
| `CLDProject.FilePath` | the full path of the project file (empty if not yet saved) |
| `CLDProject.CLDFiles` | the list of CLData files (`ICLDFileList`, see [CLData files](files.md)) |
| `CLDProject.Operations` | the list of technological operations |
| `CLDProject.CLDSub` | the list of CLD-subroutines |
| `CLDProject.Machine` | the machine info (name, type group, list of axes) |
| `CLDProject.FindCommand(type, startFile, startCommand)` | find a command of a type across the project |

The same workpiece scan in .NET walks the same named tree (note the 0-based array indices - see the index-base note in [Named CLData parameters](named-parameters.md)). The complete method, ready to paste into a postprocessor - call it, for example, from `OnStartProject`:

```csharp
// Outputs a comment for every element of every part's workpiece into the NC-program.
public void PrintAllWorkpiece()
{
    var parts = CLDProject.Arr["Parts"];
    for (int i = 0; i <= parts.TopItem; i++)
    {
        nc.OutWithN("( Part" + (i + 1) + ".Workpiece )");
        var workpiece = parts[i].Arr["Workpiece"];
        for (int j = 0; j <= workpiece.TopItem; j++)
        {
            var wp = workpiece[j];
            nc.OutWithN("(     Primitive " + (j + 1) + " )");
            switch (wp.Int["PrimitiveType"])
            {
                case 0: // Unknown
                    nc.OutWithN("(         Type: Unknown )");
                    break;
                case 1: // Empty
                    nc.OutWithN("(         Type: Empty workpiece )");
                    break;
                case 2: // Faces
                    nc.OutWithN("(         Type: Faces )");
                    OutPoint(wp, "Min point", "Box.Min");
                    OutPoint(wp, "Max point", "Box.Max");
                    break;
                case 3: // Casting
                    nc.OutWithN("(         Type: Casting )");
                    nc.OutWithN("(         Stock: " + wp.Flt["Stock"] + " )");
                    OutPoint(wp, "Min point", "Box.Min");
                    OutPoint(wp, "Max point", "Box.Max");
                    break;
                case 4: // Box
                    nc.OutWithN("(         Type: Box )");
                    OutPoint(wp, "Min point", "Min");
                    OutPoint(wp, "Max point", "Max");
                    break;
                case 5: // RevBody
                    nc.OutWithN("(         Type: Turn envelope )");
                    OutPoint(wp, "Origin", "Origin");
                    OutPoint(wp, "Axis", "Axis");
                    break;
                case 6: // Cylinder
                    nc.OutWithN("(         Type: Cylinder )");
                    OutPoint(wp, "Origin", "Origin");
                    OutPoint(wp, "Axis", "Axis");
                    nc.OutWithN("(         Min level: " + wp.Flt["HMin"] + " )");
                    nc.OutWithN("(         Max level: " + wp.Flt["HMax"] + " )");
                    nc.OutWithN("(         Outer radius: " + wp.Flt["ROut"] + " )");
                    break;
                case 7: // Tube
                    nc.OutWithN("(         Type: Tube )");
                    OutPoint(wp, "Origin", "Origin");
                    OutPoint(wp, "Axis", "Axis");
                    nc.OutWithN("(         Min level: " + wp.Flt["HMin"] + " )");
                    nc.OutWithN("(         Max level: " + wp.Flt["HMax"] + " )");
                    nc.OutWithN("(         Outer radius: " + wp.Flt["ROut"] + " )");
                    nc.OutWithN("(         Inner radius: " + wp.Flt["RInn"] + " )");
                    break;
                case 8: // Prism
                    nc.OutWithN("(         Type: Prism )");
                    OutPoint(wp, "Origin", "Origin");
                    OutPoint(wp, "Axis", "Axis");
                    nc.OutWithN("(         Min level: " + wp.Flt["HMin"] + " )");
                    nc.OutWithN("(         Max level: " + wp.Flt["HMax"] + " )");
                    break;
                case 9: // PolygonalPrism
                    nc.OutWithN("(         Type: Polygonal prism )");
                    OutPoint(wp, "Origin", "Origin");
                    OutPoint(wp, "Axis", "Axis");
                    nc.OutWithN("(         Corner count: " + wp.Int["CornerCount"] + " )");
                    nc.OutWithN("(         Inscribed radius: " + wp.Flt["RInn"] + " )");
                    nc.OutWithN("(         Angle around axis: " + wp.Flt["Angle"] + " )");
                    nc.OutWithN("(         Min level: " + wp.Flt["HMin"] + " )");
                    nc.OutWithN("(         Max level: " + wp.Flt["HMax"] + " )");
                    break;
                default:
                    nc.OutWithN("(         Type: Something else )");
                    break;
            }
        }
    }
}

// Reads the .X / .Y / .Z children of a nested point property and prints them as one comment.
private void OutPoint(INamedProperty item, string label, string basePath)
{
    double x = item.Flt[basePath + ".X"];
    double y = item.Flt[basePath + ".Y"];
    double z = item.Flt[basePath + ".Z"];
    nc.OutWithN("(         " + label + ": (" + x + ", " + y + ", " + z + " ) )");
}
```

## See also

- [Project information in CLData](../project-information.md)
- [Named CLData parameters](named-parameters.md)
- [CLData files (CLDFile operator)](files.md)
- [CLData access functions and operators](functions.md)
