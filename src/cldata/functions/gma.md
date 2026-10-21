# GMA array

The **GMA** array is an sppx convenience for processing multi-axis [MULTIGOTO](../commands/multigoto.md) movements: it presents the machine's controlled coordinates (with their new/previous values, output flags and angle-reduction results) in a single indexed structure.

> **sppx only.** There is no direct **GMA** counterpart in .NET. In a .NET postprocessor the multi-axis move is read from the strongly-typed [MULTIGOTO](../commands/multigoto.md) command (`ICLDMultiGotoCommand`) - its `Axes` collection gives each axis and value - and the register handling that **GMA** performs in sppx is done through the .NET registers API. See the [Access from .NET](../commands/multigoto.md) section of the MULTIGOTO command.

## Access from sppx

Use the predefined **GMA** array to conveniently process multiaxis movement [MULTIGOTO](../commands/multigoto.md) command in the technology program and in the mask of the command. **GMA** array is initialized directly before the [MULTIGOTO](../commands/multigoto.md) technology command is processed.

Every item of **GMA** array corresponds to an controlled coordinate of the machine scheme. Items of the **GMA** array can be added manually using the Postprocessor generator interface or imported directly from CAM system machine scheme.

Optionally, coordinates can be added to **GMA** array during postprocessor execution using following operator syntax:

```text
GMA(<AxisName> {,<RegisterName>})
```

Here **AxisName** is a legal expression that returns a string. The new coordinate name will be set to **AxisName**, use it to access the new item. Optional parameter **RegisterName** is the name of the register associated with the new coordinate.

**Example**

```pascal
GMA("AxisXPos")
```

Use the name of a coordinate to access it's **GMA** properties:

```text
GMA[<AxisName>].<Property>
```

Or for masks:

```text
<Axisname>.<Property>
```

Here **AxisName** is a legal string expression that must be a valid coordinate name. In the following example the name of the coordinate **AxisXPos** is used to access the coordinate current value:

```pascal
GMA["AxisXPos"].Vn ! Vn - coordinate current value
```

GMA Structure

**GMA** array item has the following structure:

```text
GMA[<AxisName>].OutFlag
GMA[<AxisName>].Vn
GMA[<AxisName>].Vp
GMA[<AxisName>].Axis
GMA[<AxisName>].Reg
GMA[<AxisName>].TurnCount
GMA[<AxisName>].Dir
```

- `GMA[<AxisName>].OutFlag` is an [Integer](../../sppx/src/language-description/basic-definitions/variables.md) field that is assigned values 1 or 0. Use this flag to determine whether the coordinate named **AxisName** is listed in the given [MULTIGOTO](../commands/multigoto.md) command. `GMA[<AxisName>].OutFlag` has the value of 1 (the flag is set) if there is a coordinate named **AxisName** in the given [MULTIGOTO](../commands/multigoto.md) command, otherwise the flag is 0.
- `GMA[<AxisName>].Vn` is a [Real](../../sppx/src/language-description/basic-definitions/variables.md) field and it's value is the new value of the coordinate **AxisName** set by [MULTIGOTO](../commands/multigoto.md) command. Use the **Vn** field to read or set the new coordinate value.
- `GMA[<AxisName>].Vp` is a [Real](../../sppx/src/language-description/basic-definitions/variables.md) field that contains the value of **AxisName** coordinate assigned by the previous [MULTIGOTO](../commands/multigoto.md) command. Use the **Vp** field to read or set the previous coordinate value.
- `GMA[<AxisName>].Axis` is a [String](../../sppx/src/language-description/basic-definitions/variables.md) field that is the name of the coordinate and is equal to **AxisName**. The field is read-only.
- `GMA[<AxisName>].Reg` is a [String](../../sppx/src/language-description/basic-definitions/variables.md) field and it's value is the name of the register associated with the coordinate. The field is read-only.
- `GMA[<AxisName>].TurnCount` is an [Integer](../../sppx/src/language-description/basic-definitions/variables.md) field that is assigned the number of full turns of a rotatable axis. The field is read-only.
- `GMA[<AxisName>].Dir` is an [Integer](../../sppx/src/language-description/basic-definitions/variables.md) value that is assigned +1 if the value of the coordinate is increasing, otherwise it is set to -1. The field is read-only.

Use **TurnCount** and **Dir** fields to process the movement of rotatable axes. CAM system passes the movements of rotatable axes in absolute values, whereas some NC-systems accept only values in bound ranges like 0º to 360º or 180º to -180º for those coordinates. Use the **Machine axes parameters** dialog to define the bounds and ranges parameters of rotatable axes. If angle reduction is defined for a given coordinate then when processing [MULTIGOTO](../commands/multigoto.md) command the system will reduce the coordinate value **Vn** to specified range, assign the **TurnCount** field the number of full revolutions of the coordinate and set the sign of the **Dir** field depending on the previous (not reduced) value of the coordinate.

Here are a few examples illustrating how the system initializes the properties of **GMA** array items when processing [MULTIGOTO](../commands/multigoto.md) technology command. Suppose rotatable axis C (**AxisCPos**) is bound to values from 0º to 360º.

1. Command:

```text
MULTIGOTO COUNT 4, AxisXPos(18) 80, AxisYPos(20) 19.877,
AxisZPos(22) -200, AxisCPos(24) 0
```

**GMA** array for the [MULTIGOTO](../commands/multigoto.md) command:

| Coordinate name | OutFlag | Vn | Vp | Axis | Reg | TurnCount | Dir |
|---|---|---|---|---|---|---|---|
| AxisXPos | 1 | 80 | -//-//- | "AxisXPos" | "X" | -//-//- | -//-//- |
| AxisYPos | 1 | 19.877 | -//-//- | "AxisYPos" | "Y" | -//-//- | -//-//- |
| AxisZPos | 1 | -200 | -//-//- | "AxisZPos" | "Z" | -//-//- | -//-//- |
| AxisCPos | 1 | 0 | -//-//- | "AxisCPos" | "C" | -//-//- | -//-//- |

"-//-//-" sign indicates that the values of the properties of coordinates cannot be determined because there is no information of the previous command.

1. Command:

```text
MULTIGOTO COUNT 1, AxisCPos(24) 270
```

**GMA** array for the [MULTIGOTO](../commands/multigoto.md) command:

| Coordinate name | OutFlag | Vn | Vp | Axis | Reg | TurnCount | Dir |
|---|---|---|---|---|---|---|---|
| AxisXPos | 0 | 80 | 80 | "AxisXPos" | "X" | -//-//- | -//-//- |
| AxisYPos | 0 | 19.877 | 19.877 | "AxisYPos" | "Y" | -//-//- | -//-//- |
| AxisZPos | 0 | -200 | -200 | "AxisZPos" | "Z" | -//-//- | -//-//- |
| AxisCPos | 1 | 270 | 0 | "AxisCPos" | "C" | 0 | +1 |

1. Command:

```text
MULTIGOTO COUNT 2, AxisZPos(22) 250, AxisCPos(24) -745
```

**GMA** array for the [MULTIGOTO](../commands/multigoto.md) command:

| Coordinate name | OutFlag | Vn | Vp | Axis | Reg | TurnCount | Dir |
|---|---|---|---|---|---|---|---|
| AxisXPos | 0 | 80 | 80 | "AxisXPos" | "X" | -//-//- | -//-//- |
| AxisYPos | 0 | 19.877 | 19.877 | "AxisYPos" | "Y" | -//-//- | -//-//- |
| AxisZPos | 1 | 250 | -200 | "AxisZPos" | "Z" | -//-//- | -//-//- |
| AxisCPos | 1 | 335 | 270 | "AxisCPos" | "C" | 2 | -1 |

In the last example the system applied angle reduction for the `AxisCPos(C)` coordinate. The value passed by CAM system "-745 º" is reduced to the range from 0º to 360º by the following rules:

```text
TurnCount = |(Vn' - Vp') \ 360|
TurnCount = |(-745 -270) \ 360| = 2
Dir = Sgn(Vn'-Vp')
Dir = Sgn(-745 -270) = -1
Vn = Vn' - (Vn' \ 360)*360, if Vn' > 360
Vn = Vn' - (Vn' \ 360)*360 + 360, if Vn' < 0
Vn = -745 - (-745\360)*360 + 360 = 335
```

`Vn'` - the current not reduced value of the coordinate, `Vp'` - previous not reduced value of the coordinate.

The following is an example of a simple [MULTIGOTO](../commands/multigoto.md) command program that uses the **GMA** array:

```pascal
program MultiGoto
  ! Use the GMA fields to assign
  ! respective registers their new values
  if GMA["AxisXPos"].OutFlag>0 then
    X = GMA["AxisXPos"].Vn
  if GMA["AxisYPos"].OutFlag>0 then
    Y = GMA["AxisYPos"].Vn
  if GMA["AxisZPos"].OutFlag>0 then
    Z = GMA["AxisZPos"].Vn
  if GMA["AxisCPos"].OutFlag>0 then
    C = GMA["AxisCPos"].Vn
  ! Output the formed values into the NC-program
  OutBlock
end
```

## See also

- [Predefined functions](../../sppx/src/language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md)
- [MULTIGOTO command](../commands/multigoto.md)
- [Masks](../../sppx/src/postprocessor-masks/mask-structure/gma-array-in-masks.md)
- [CLData access functions and operators](functions.md)
