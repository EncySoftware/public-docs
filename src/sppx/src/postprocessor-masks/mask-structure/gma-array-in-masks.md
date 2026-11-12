# GMA array in masks

The predefined [GMA](../../../../cldata/functions/gma.md) array is used to conveniently program the [MULTIGOTO](../../../../cldata/commands/multigoto.md) command postprocessor either as a technology command program or as a mask. The [GMA](../../../../cldata/functions/gma.md) array like the [CLD](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md) array is initialized before the command is processed. Every item of the [GMA](../../../../cldata/functions/gma.md) array corresponds to an axis in the machine scheme.

The [GMA](../../../../cldata/functions/gma.md) array usage syntax in masks is different from the postprocessor program's code: when used in a mask the "GMA" keyword and brackets are omitted. To access a [GMA](../../../../cldata/functions/gma.md) array item's property when programming a mask for the [MULTIGOTO](../../../../cldata/commands/multigoto.md) command use the quoted name of the axis and the property name without quotes separated by a point. For example to put the current value of the coordinate named **AxisXPos** into a NC-program the mask `X["AxisXPos".Vn]` should be used.

The following are examples of accessing [GMA](../../../../cldata/functions/gma.md) arrays items:

- `"<AxisName>".OutFlag` – whether the coordinate is present in current [MULTIGOTO](../../../../cldata/commands/multigoto.md) command.
- `"<AxisName>".Vn` – current value of the coordinate.
- `"<AxisName>".Vp` – previous value of the coordinate.
- `"<AxisName>".Axis` – coordinate name in the machine scheme.
- `"<AxisName>".Reg` – name of the register bound to the coordinate.
- `"<AxisName>".TurnCount` – number of full revolutions (360 degrees) of the current movement of rotatable axis.
- `"<AxisName>".Dir` – direction of rotation.

**AxisName** – name of the machine coordinate.

The following example writes the **X**, **Y** and **Z** coordinates values into the NC-program passed through the [MULTIGOTO](../../../../cldata/commands/multigoto.md) command for the axes **AxisXPos**, **AxisYPos** and **AxisZPos** respectively.

```
X["AxisXPos".Vn] Y["AxisYPos".Vn] Z["AxisZPos".Vn]
```

**See also**

[Mask structure](readme-mask-structure.md)
