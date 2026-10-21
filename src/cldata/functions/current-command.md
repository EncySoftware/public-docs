# Current command (Cmd operator)

The current command is the CLData command whose handler is being executed. Besides the numeric [CLD array](cld-array.md), a postprocessor can read the command's code, name, textual data and any of its named parameters (including nested ones). The sppx **Cmd** operator and the .NET strongly-typed `cmd` object provide this.

## Access from sppx

The **Cmd** operator provides a flexible mechanism for working with the current CLData command. It returns a reference to the current command, on which you can request a code, name and parameters of this command. Format of access to specific command data following.

`Cmd.Code` - returns a unique numeric code of the CLData command. Each command is uniquely identified by this code. List of command codes listed in the [technology commands description](../commands/commands.md).

`Cmd.Name` - returns the text name of the command or command parameter.

`Cmd.Data` - for individual CLData commands, which have a single string parameter (such as Comment, PartNo, etc.), returns string value. For the rest of the commands returns a string representation of the command, exactly what is displayed on the tab CLData of main window.

`Cmd.Data[Index]` - an alternative way to access an array of numeric parameters of command [CLD](cld-array.md). Returns the real value of the parameters array element with the index Index.

The following below are a few language structures allow access to the parameters of CLData command by parameter name. See [Named CLData parameters](named-parameters.md) topic for more information. Each CLData command can be characterized by its own set of named parameters. The names of the parameters with description for each command are listed in the [technology commands description](../commands/commands.md). The parameter names can be seen on CLData tab at the bottom of the main window.

`Cmd.Str["ParameterName"]` - returns the value of the command parameter with the name ParameterName as a text String.

`Cmd.Int["ParameterName"]` - returns the value of the command parameter with the name ParameterName as an Integer number.

`Cmd.Flt["ParameterName"]` - returns the value of the command parameter with the name ParameterName as a Real number (floating point number).

`Cmd.Ptr["ParameterName"]` - returns a reference to the command parameter with the ParameterName name.

Consider a few examples of CLData command parameters using.

**Example 1**. Inside the tool loading command handler LoadTl to NC-program output the string with address T, with number of the tool and with the name of the turret head in parentheses.

```pascal
program LoadTl
  Output "T" + Cmd.Int["ToolID"] + "(" + Cmd.Str["RevolverID"] + ")"
end
```

A possible result of the output to the NC-code: T3 (TopTurret)

**Example 2**. Example of MultiGoto command processing using various methods to access elements of array parameter Axes.

```pascal
program MultiGoto
  i: Integer
  AxisName: String
  for i = 1 to Cmd.Ptr["Axes"].ItemCount do begin
    AxisName = cmd.Ptr["Axes"].Item[i].Str["AxisID"]
    if AxisName="AxisXPos" then begin
      X = cmd.Ptr["Axes"].Item[i].Flt["Value"]
    end else
    if AxisName="AxisYPos" then begin
      Y = cmd.Ptr["Axes("+Str(i)+")"].Flt["Value"]
    end else
    if AxisName="AxisZPos" then begin
      Z = cmd.Flt["Axes("+Str(i)+").Value"]
    end else
    if cmd.Ptr["Axes(AxisCPos)"]<>0 then begin
      C = cmd.Flt["Axes(AxisCPos).Value"]
    end
  end
  OutBlock
end
```

**Example 3**. Example of coordinate system setup command processing Origin. It analyzes the **OriginType** property's value. If it is zero, output the standard workpiece coordinate system selection command G54-G59. Number of the coordinate system is taken from the parameter **CSNumber**. Otherwise the local coordinate system transfer command G92 X Y Z is formed. The values of the displacements along the axes of the coordinate system are taken in different ways from the corresponding child properties of the `MCS.OriginPoint` parameter.

```pascal
program Origin
  if Cmd.Int["OriginType"]=0 then begin !G54-G59
    Output "G" + Cmd.Str["CSNumber"]
  end else begin                        !G92 X Y Z
    X = Cmd.Flt["MCS.OriginPoint.X"]
    Y = Cmd.Ptr["MCS.OriginPoint.Y"].Flt
    Z = Cmd.Ptr["MCS.OriginPoint"].Flt["Z"]
    Output "G92 X" + Str(X) + " Y" + Str(Y) + " Z" + Str(Z)
  end
end
```

### Cmd operator (parameters with a unique code)

For probing cycles, parameters can be written to the [CLD array](cld-array.md) in a different order. Each parameter has a [unique code](../commands/extcycle/wprobing/wprobing.md) by which you can get the value of the parameter.

The syntax for accessing the parameters of the CLData command by numerical code:

- `CmdPrm.ItemCount` - number of parameters for the command;
- `CmdPrm.Flt[Code]` - return the value of the parameter by its code in the Double value;
- `CmdPrm.Int[Code]` - return the value of the parameter by its code in the Integer value;
- `CmdPrm.Str[Code]` - return the value of the parameter by its code in the String value;
- `CmdPrm.Bol[Code]` - return the value of the parameter by its code in the Boolean value;
- `CmdPrm.IndexOfCode(Code)` - find parameter index by its code;
- `CmdPrm.Item[i].ItemType` - parameter type by index (String, Integer, Double, Boolean);
- `CmdPrm.Item[i].Flt` - parameter value by index in the Double value;
- `CmdPrm.Item[i].Int` - parameter value by index in the Integer value;
- `CmdPrm.Item[i].Str` - parameter value by index in the String value;
- `CmdPrm.Item[i].Bol` - parameter value by index in the Boolean value;
- `CmdPrm.Item[i].Code` - numeric parameter code by index.

## Access from .NET

In .NET the current command is the first argument of the handler - a strongly-typed interface (`ICLDCircleCommand`, `ICLDGotoCommand`, ...) derived from `ICLDCommand`. Reading the typed properties (`cmd.EP.X`, `cmd.R`, ...) is the recommended way; the members below cover the same information as the sppx **Cmd** operator:

| sppx | .NET (`ICLDCommand`) | Description |
|---|---|---|
| `Cmd.Code` | `cmd.CmdTypeCode` | the unique numeric type code of the command |
| - | `cmd.CmdType` | the command type as the `CLDCmdType` enumeration |
| `Cmd.Name` | `cmd.Caption` | the command name as it appears in windows |
| `Cmd.Data` | `cmd.CLDataS` | the textual data of the command (or its string representation) |
| `Cmd.Data[i]` | `cmd.CLD[i]` | the i-th numeric parameter (see [CLD array](cld-array.md)) |
| - | `cmd.Index` | the index of the command in its CLData file |

The named-parameter access (`Str` / `Int` / `Flt` / `Ptr`) is identical, because `ICLDCommand` implements the common [named-property model](named-parameters.md):

```csharp
public override void OnLoadTl(ICLDLoadTlCommand cmd, CLDArray cld)
{
    nc.OutWithN("T" + cmd.Int["ToolID"] + "(" + cmd.Str["RevolverID"] + ")");
}
```

Nested and array parameters use `cmd.Ptr["Name"]`, `.Arr["Name"]`, `.Item[i]` and the compound `"Group.Sub.Param"` / `"Array(Key)"` name syntax, exactly as in sppx - see [Named CLData parameters](named-parameters.md).

**Parameters with a unique code.** In .NET postprocessors, everything is almost the same, but access is via the `cmd.Prm` keyword (`cmd.Prm.Flt[code]`, `cmd.Prm.Int[code]`, `cmd.Prm.IndexOfCode(code)`, `cmd.Prm.Item[i]...`).

## See also

- [Named CLData parameters](named-parameters.md)
- [CLD predefined array](cld-array.md)
- [Browsing CLData commands](browsing.md)
- [CLData access functions and operators](functions.md)
