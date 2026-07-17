# PPFUN TECHINFO(58) - Technology parameters command

Technology parameters command `PPFUN TECHINFO(58)` passes additional technology information about the CAM system operation. `PPFUN TECHINFO(58)` command is generated at the beginning of technology commands list of an operation.

## Parameters

| CLD array | Parameter | Variable description | Group |
|---|---|---|---|
| 1 | SubCode | 58 (TechInfo) |   |
| 2 | 2 | CLData version |   |
| 3 | 3 | Minimum X coordinate value | Toolpath box |
| 4 | 4 | Minimum Y coordinate value |   |
| 5 | 5 | Minimum Z coordinate value |   |
| 6 | 6 | Maximum X coordinate value |   |
| 7 | 7 | Maximum Y coordinate value |   |
| 8 | 8 | Maximum Z coordinate value |   |
| 9 | 9 | Safe plane level (the level of rapid movement for the EDM operations) | Levels |
| 10 | 10 | Upper machining level |   |
| 11 | 11 | Lower machining level |   |
| 12 | 12 | Stock | Workpiece |
| 13 | 13 | Minimum X coordinate value |   |
| 14 | 14 | Minimum Y coordinate value |   |
| 15 | 15 | Minimum Z coordinate value |   |
| 16 | 16 | Maximum X coordinate value |   |
| 17 | 17 | Maximum Y coordinate value |   |
| 18 | 18 | Maximum Z coordinate value |   |
| 19 | 19 | CLData tolerance (number of decimal digits) | Tolerance |
| 20 | 20 | Measurement units: 0 – mm; 1 – inches. |   |
| 21 | 21 | Minimum arc length |   |
| 22 | 22 | Deviation off workpiece |   |
| 23 | 23 | Deviation into workpiece |   |
| 24 | 24 | Operation stock |   |
| 25 | 25 | Tool type: 0 – cylindrical 1 – ball 2 – torus 3 – Double radial 4 – Limited double radial 5 – Conical mill 6 – Limited conical mill 7 – Engraver 8 – Drill 9 – Composite tool 10 – Mill with negative radius 11 – Cutting tool 12 – Tap 13 – Center drill 14 – Countersink drill 15 – Spot facing drill 16 – Reamer 17 – Threading drill 100 – External tool 101 – Boring tool 102 – External threading tool 103 – Internal threading tool 104 – External grooving tool 105 – Internal grooving tool 106 – Face grooving tool | Tool |
| 26 | 26 | Tool number |   |
| 27 | 27 | Tool diameter (wire diameter for the EDM operations) |   |
| 28 | 28 | Work part length |   |
| 29 | 29 | Work part angle (conical angle in radians) |   |
| 30 | 30 | Round radius |   |
| 31 | 31 | Length compensation number. Set to 0 if length compensation is off |   |
| 32 | 32 | Radial compensation number. Set to 0 if radial compensation is off |   |
| 33 | 33 | Length compensation value |   |
| 34 | 34 | Radial compensation value |   |
| 35 | 35 | Axial tool tooling point: 0 – Center, 1 – Custom, 2 – End. Lathe tool tooling point: 0 – Left, 1 – Right, 2 – Top, 3 – Bottom, 4 – Top left, 5 – Top right, 6 – Bottom left, 7 – Bottom right, 8 – Center, 9 – Custom. |   |
| 36 | 36 | Spindle rotation (rev per min) | Speed |
| 37 | 37 | Rapid feedrate (mm per min or inch per min) |   |
| 38 | 38 | Work feedrate |   |
| 39 | 39 | Cut-in feedrate |   |
| 40 | 40 | Approach feedrate |   |
| 41 | 41 | Retraction feedrate |   |
| 42 | 42 | Next feedrate |   |
| 43 | 43 | Return feedrate |   |
| 44 | 44 | Toolpath length | Toolpath properties |
| 45 | 45 | Operation's machining time in minutes |   |
| 46 | 46 | Total time of the techprocess in minutes |   |
| 47 | 47 | Upper guide level of the EDM machine | Levels |
| 48 | 48 | Lower guide level of the EDM machine |   |
| 49 | 49 | Operation's working time in minutes | Toolpath properties |
| 51 | 51 | Tool Axis: 1 – X, 2 – Y, 3 – Z. (Lathe – 2, Lathe-drill – 1, Milling – 3) |   |
| 52 | 52 | X coordinate | Tool change point |
| 53 | 53 | Y coordinate |   |
| 54 | 54 | Z coordinate |   |
| 55 | 55 | X coordinate | Reference point |
| 56 | 56 | Y coordinate |   |
| 57 | 57 | Z coordinate |   |
| 58 | 58 | Active tube number: 0 – coolant off, 1 – flood, 2 – mist, 3 – tool. |   |
| 60 | 60 | Operation technology group: 0 – not set, 1 – milling, 2 – lathe, 3 – auxiliary, 4 – electric discharge. |   |
| 61 | 61 | 0 – PPFUN command is not activated 1 – PPFUN command is activated |   |
| 62 | 62 | Robot kinematics: 0 – the position of the 3rd joint doesn't depend on the position of the 2nd joint 1 – the 2nd and 3rd joints are linked with the parallelogram mechanism | Robot kinematics |
| 63 | 63 | Part number that is explicitly set by the user in the part parameters of CAM system | Part |
| 64 | 64 | Turn tool tool tip offset direction vector code (0-8): 0: X=0, Y=0; 1: X=+1, Y=+1; 2: X=-1, Y=+1; 3: X=-1, Y=-1; 4: X=+1, Y=-1; 5: X=+1, Y=0; 6: X=0, Y=+1; 7: X=-1, Y=0; 8: X=0, Y=-1; | Tool tip code |
| 65 | 65 | Workpiece coordinate system number (G54, G55, G54.2 etc) of the operation | WCS number |
| 80 | 80 | Step along tool axis for multilayer machining (For 2D Contour operation only) | Layers |
| 81 | 81 | Finish layer stock along tool axis (For 2D Contour operation only) | Layers |

Parameters available through the cmd operator

| Type | Description | Subfield description |
|---|---|---|
| TCLDPPFun: ComplexType | The command determining technological parameters of the operation |   |
| PPFun: Array, Key="RecordID" | cmd.Ptr["PPFun"] - An array of structures of different types to storage parameters of the PPFun command |   |
| TPPFunTechInfoParameters: ComplexType | cmd.Ptr["PPFun"].Item[1] or cmd.Ptr["PPFun(TechInfo)"] - Separate element of the PPFun array. Contains information on technological parameters of the operation. Access to the array elements can either index or by key field **RecordID**. For the command of determining of operation technological parameters it always has the value "TechInfo". |   |
| RecordID: String | cmd.Str["PPFun(TechInfo).RecordID"] - Postprocessor function type's identifier. In this case always has a value "TechInfo". |   |
| RecordCode: Integer | cmd.Int["PPFun(TechInfo).RecordCode"] - The code that identifies the type of postprocessor function. In this case always has a value "58". |   |
| Operation: Array | cmd.Ptr["PPFun(TechInfo).Operation"] - almost a full list of parameters of technological operation. As the child elements of the item are a variety of operation parameters: the type of operation, its name, group, tool properties, stocks, calculation tolerances, lead-in and lead-out methods, machining levels and step, etc. Specific set of parameters depends on the type of operation. Type of operation can be obtained as cmd.Ptr["PPFun(TechInfo).Operation(1)"].Name. |   |
| SetupStage: ComplexType | cmd.Ptr["PPFun(TechInfo).SetupStage"] - Information about the Setup stage in which the operation is located. |   |
|   | Index: Integer | Index of the setup stage in the list of CAM system's project setup stages |
|   | Name: String | The name of the setup stage group inside CAM system's project |
| Tool: ComplexType | cmd.Ptr["PPFun(TechInfo).Tool"] - Parameters relating to the tool used in technological operation. |   |
|   | ID: Integer | cmd.Int["PPFun(TechInfo).Tool.ID"] - tool identifier (number) |
|   | HolderID: Integer | cmd.Int["PPFun(TechInfo).Tool.HolderID"] - tool holder identifier (number) |
|   | RevolverID: String | cmd.Str["PPFun(TechInfo).Tool.RevolverID"] - String identifier of the turret head. |
| Workpiece: ComplexType | cmd.Ptr["PPFun(TechInfo).Workpiece"] - Parameters relating to the workpiece used in technological operation. |   |
|   | HolderID: String | cmd.Str["PPFun(TechInfo).Workpiece.HolderID"] - string identifier of the workpiece connector. |
| Part: ComplexType | cmd.Ptr["PPFun(TechInfo).Part"] - Information about the Part being machined by this operation |   |
|   | Index: Integer | Index of the Part in the list of CAM system's project parts list |
|   | Number: Integer | Part number that is explicitly set by the user in the part parameters of CAM system |
|   | Name: String | The Part name (group name) that is set in CAM system |

Below is an example of access to the properties of operation by the operator cmd.

```pascal
program PPFun
  if cld[1]=58 then begin ! TechInfo
    call AnalysePPFun
  end
end
sub AnalysePPFun
  OpType: String
  OpGroup: Integer
  ! String name of operation type: TSTRoughingWaterlineOp, TST2DContouringOp, TSTDrillOp, LatheRoughOp...
  OpType = cmd.Ptr["PPFun(TechInfo).Operation(1)"].Name
  ! OperationGroup:
  ! 1 - Milling
  ! 2 - Lathe
  ! 3 - Auxiliary
  ! 4 - WireEDM
  OpGroup = cmd.Int["PPFun(TechInfo).Operation(1).OperationGroup"]
  Output "; Operation type = " + OpType
  Output "; Operation comment = " + cmd.Str["PPFun(TechInfo).Operation(1).Comment"]
  if OpGroup=1 then begin ! Milling
    Output "; Tool overhang = " + Str(cmd.Flt["PPFun(TechInfo).Operation(1).ToolSection.Tools(1).AxialOverhang"])
    if OpType="TSTRoughingWaterlineOp" then begin
      Output "; Axial stock = " + Str(cmd.Flt["PPFun(TechInfo).Operation(1).Stocks.Axial"])
      Output "; Radial stock = " + Str(cmd.Flt["PPFun(TechInfo).Operation(1).Stocks.Radial"])
    end
  end else if OpGroup=2 then begin ! Lathe
    Output "; Tool X overhang = " + Str(cmd.Flt["PPFun(TechInfo).Operation(1).ToolSection.Tools(1).Overhang.Value.X"])
    Output "; Tool Y overhang = " + Str(cmd.Flt["PPFun(TechInfo).Operation(1).ToolSection.Tools(1).Overhang.Value.Y"])
    Output "; Tool Z overhang = " + Str(cmd.Flt["PPFun(TechInfo).Operation(1).ToolSection.Tools(1).Overhang.Value.Z"])
    Output "; Axial stock = " + Str(cmd.Flt["PPFun(TechInfo).Operation(1).LatheStock.AxialValue"])
    Output "; Radial stock = " + Str(cmd.Flt["PPFun(TechInfo).Operation(1).LatheStock.RadialValue"])
  end
subend
```

## Access from .NET

In addition to the base `OnPPFun`, this sub-code raises the dedicated handler `OnStartTechOperation`:

```csharp
public override void OnStartTechOperation(ICLDTechOperation op, ICLDPPFunCommand cmd, CLDArray cld)
```

The common .NET model (members, 1-based vs 0-based index) is described in [Postprocessor function (PPFUN)](ppfun.md).

## Reading the operation's XML properties by name

For `TECHINFO`/`ENDTECHINFO`, besides the fixed parameters above, the command bridges into the operation's **XML properties** by name through the `cmd` helpers:

> **Warning.** This is a **direct read of the CAM system's internal data structures**. Their layout and naming are **not guaranteed to stay the same between versions**. Use it **only as a last resort**, when the value you need is not exposed through the public CLData API above. Prefer the documented parameters and typed members whenever they cover your case.

The array element index differs between environments - **1-based in sppx**, **0-based in .NET**:

- sppx: `cmd.Ptr["PPFun(TechInfo).Operation(1)"]`
- .NET: `cmd.Ptr["PPFun(TechInfo).Operation(0)"]`

Example (from the Heidenhain (iTNC530)_Mill postprocessor - sppx, **1-based** element index):

```pascal
! a deep operation property, reached through the operation's TechInfo command
MinDepth = cmd.Flt["PPFun(TechInfo).Operation(1).ChipBreaking.DepthDegression.MinStepPercent"]
```

To find the exact name of a property: open the operation's **property inspector**, locate the property, click the **...** button at the right of its row and choose **"Copy property name to clipboard"**; or inspect the operation's XML. The naming rules and the full access model are described in [Using XML properties from code](../../../../xml-properties/using-from-code.md).

Example - `OnStartTechOperation` (from the Heidenhain_Mill_iTNC530_DN postprocessor):

```csharp
public override void OnStartTechOperation(ICLDTechOperation op, ICLDPPFunCommand cmd, CLDArray cld)
{
    nc.WriteLine();
    nc.OutText("; " + Transliterate(op.Comment));

    // 17 TOOL CALL 1 Z S159 DL+0 DR+0
    // 18 TOOL DEF 2
    // 19 L Z+0 FMAX M91            
    if (op.Tool.Command!=null && op.Tool.Command.ToolChanged) { // if the operation has a Load tool command
        double s = 0;
        if (op.SpindleCommand!=null)
            s = Abs(op.SpindleCommand.RPMValue);
        nc.OutText($"TOOL CALL {op.Tool.Number} {GetToolPlaneName(op.Tool.Command)} {nc.S.ToString(s)} DL+0 DR+0");

        int nextTool = FindNextOpToolNumber(op);
        if (nextTool>0)
            nc.OutText($"TOOL DEF {nextTool}");

        if (firstToolNumber<0)
            firstToolNumber = op.Tool.Number;
        nc.OutText("L Z+0 FMAX M91");
    }

}
```

## See also
- [Postprocessor function (PPFUN)](ppfun.md)
- [CLData access model](../../cldata.md)
- [`PPFUN ENDTECHINFO(59)`](endtechinfo.md)
- [Using XML properties from code](../../../../xml-properties/using-from-code.md)
