# CLD predefined array

The **CLD** array holds the numerical parameters of the currently executing CLData command. Before a command handler is called, the command's parameters are placed into this array; inside the handler the parameters are analyzed by reading individual array elements, and on the basis of that analysis blocks of the NC-program are generated.

Command parameters are accessed either by indexing the appropriate item in the array or by a unique parameter name.

## Access from sppx

The array **CLD** is an array of real numbers. It is designed to store numerical parameters of currently executing technological CLData command. Before calling the handler of the current command its parameters are filled in this array. Inside the handler command parameters can be analyzed by accessing individual array elements and on the basis of analysis can be generated blocks of the NC-program.

Command parameters are accessed either by indexing the appropriate item in the **CLD** array or by unique parameter name.

To access by index use the common array syntax: `CLD[i]` - i-th array item - real number, **i** - item index - positive integer. Index of array element can be a variable or an expression of integer type. For example: `CLD[3]`, `CLD[n]`, `CLD[2*n+1]` etc. The total number of elements in the array **CLD** contained in the predefined variable **RecNum**.

To access parameters by name use the following syntax: `CLD.Parameter name`, where **Parameter name** - unique identifier of the parameter. For example, `CLD.X`, `CLD.Mode` and so on. Parameter names are specific for each command. The detailed description of CLData technology commands and their parameters is found in the [technology commands description](../commands/commands.md). Also you can see the list of parameters at the **Current parameters** panel of the **Mask** page of the [main window](../../sppx/src/common-organization-of-the-work/main-window/readme-main-window.md) and on the **CLData** tab at the bottom of the main window.

Example of using **CLD** array:

```pascal
program Circle
  if CLD.R > 0 then INTERP_ = 3
  else INTERP_ = 2 ! G3/G2
  X = cld[5]
  Y = cld[6]
  Z = cld[7]
  I = CLD.Xc
  J = CLD.Yc
  R = abs(cld.R)
  OutBlock
end
```

The above CIRCLE command handler outputs into NC-code blocks of moving in a circle G2 or G3 (clockwise or counterclockwise) with the endpoint (X, Y, Z), center (I, J) and radius (R).

Access to the parameters of CLData command, including and not numeric, can also be obtained by the operator [Cmd](current-command.md).

## Access from .NET

A command handler receives the same numeric parameter array as its second argument - an instance of the `CLDArray` class (conventionally named `cld`). Its members mirror the sppx **CLD** array:

| sppx | .NET | Description |
|---|---|---|
| `CLD[i]` | `cld[i]` | the i-th parameter, a real number; the index is **1-based** ([1..Count]), the same as in sppx |
| `CLD.Name` | `cld["Name"]` | the parameter addressed by its unique textual name (case-insensitive) |
| `RecNum` | `cld.Count` | the number of parameters in the array |

The same CIRCLE handler in .NET:

```csharp
public override void OnCircle(ICLDCircleCommand cmd, CLDArray cld)
{
    int interp = cld["R"] > 0 ? 3 : 2;   // G3 / G2
    double x = cld[5];
    double y = cld[6];
    double z = cld[7];
    double i = cld["Xc"];
    double j = cld["Yc"];
    double r = Math.Abs(cld["R"]);
    // ... output the block
}
```

In .NET the parameters are usually read from the strongly-typed `cmd` object instead (`cmd.EP.X`, `cmd.R`, ...) - see [Current command](current-command.md); the raw `cld` array is available for the cases the typed members do not cover.

## See also

- [Current command (Cmd operator)](current-command.md)
- [Named CLData parameters](named-parameters.md)
- [CLData access functions and operators](functions.md)
