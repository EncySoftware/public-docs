# Miscellaneous functions and variables

Postprocessor language provides various miscellaneous functions and variables which are used to simplify the postprocessor developing.

- [CLData functions and operators](../../../../cldata/functions/functions.md).
- [Registers](../../../common-organization-of-the-work/main-window/block-structure-and-format-definition-register-list-forming.md). There is a variable for every register in the postprocessor, which name matches the register name. This variable holds the current value of the register. Register variables are of [Real](../variables.md) type.
- **Previous register values**. A variable which name matches the name of register with the `@` symbol at the end is used to hold the previous value of the register. For example, **X@** – previous value of the **X** register. This variable is initialized then the NC-block is output into the NC-program.
- [RGS](../../../common-organization-of-the-work/main-window/block-structure-and-format-definition-register-list-forming.md) array. The **RGS** array allows you to get access to the registers by their index in the list. It can be useful in some cases (for example inside multichannel postprocessors where you can have separate set of the registers for each channel and you need to switch quickly between them) instead of using name of the register.
- [CLD array](../../../../cldata/functions/cld-array.md). The array **CLD** is an array of real numbers, it is initialized by the system with the current CLData command parameters.

- **RecNum** returns the number of parameters of the current technology command which are filled in the [CLD](../../../../cldata/functions/cld-array.md) array. The index of the top element of the **CLD** array is equal to **RecNum**.

- [GMA array](../../../../cldata/functions/gma.md). Use it to process the parameters of the [MULTIGOTO](../../../../cldata/commands/multigoto.md) technology command.

- **CLData$** variable. This variable is initialized by the system with a textual data of the technology command if the command parameter is a string of text. **CLData$** holds the passed value until it is reset by other text technology command. The type of the **CLData$** is [String](../variables.md).

- **OutStr$** variable. This variable is assigned the current NC-code line after the execution of [FORMBLOCK](../../operators/block-forming-statement-formblock.md) or [OUTBLOCK](../../operators/block-output-statement-outblock.md) command. **OutStr$** is [String](../variables.md).
- **BlockStep** variable is assigned the value of increment when the automatic NC-code line numeration is used. Automatic NC-block numeration is enabled in the [Machine information](../../../common-organization-of-the-work/main-window/machine-parameters/defining-the-data-about-the-nc-machine-and-cnc-system.md) dialog. If the auto numeration is enabled then when each new NC-block is formed it's number is increased by the **BlockStep**. If you set **BlockStep** to 0 then the automatic NC-block numeration will be disabled.
- String variable **NCName$** is assigned the name of the file of the NC-program (no file path and no file extension).
- String variable **NCPath$** is assigned the full NC-program file name including file path and file extension.
- String variable **SPPName$** holds the name of the postprocessor file without path and extension.
- String variable **SPPPath$** holds the full file path of the postprocessor file including file extension.

- **CurDate** – function returns the string representing the current date.
- **CurTime** – function returns the string representing the current time.
- **CurISODate** – function returns the string representing the current date and time in ISO 8601 format.

- **Error** variable – integer variable which value is set to the last error code if an error occurs during program execution.
- **Xt**, **Yt**, **Zt** real variables – current tool position coordinates. These variables are initialized by the system directly before the commands [CIRCLE](../../../../cldata/commands/circle.md), [FROM](../../../../cldata/commands/from.md), [ABSMOV](../../../../cldata/commands/goto.md), [GOHOME](../../../../cldata/commands/gohome.md) are processed.
- **Xp**, **Yp**, **Zp** real variables – previous tool position coordinates. These variables are initialized by the system directly before the commands [CIRCLE](../../../../cldata/commands/circle.md), [FROM](../../../../cldata/commands/from.md), [ABSMOV](../../../../cldata/commands/goto.md), [GOHOME](../../../../cldata/commands/gohome.md) are processed.
- **Xc**, **Yc**, **Zc** variables – circle center coordinates (initialized by the system prior to the [CIRCLE](../../../../cldata/commands/circle.md) program call).
- **Interp** – current interpolation mode (the value of this variable is assigned automatically before the [CIRCLE](../../../../cldata/commands/circle.md), [FEDRAT](../../../../cldata/commands/fedrat.md), [ABSMOV](../../../../cldata/commands/goto.md), [RAPID](../../../../cldata/commands/rapid.md), [GOHOME](../../../../cldata/commands/gohome.md) programs are executed). The set of values for the **Interp** variable:
  - 0 – rapid feedrate,
  - 1 – linear interpolation,
  - 2 – clockwise circle interpolation,
  - 3 – counter clockwise circle interpolation.

- **ToolRad** – tool radius (initialized by the system prior to the [LOADTL](../../../../cldata/commands/loadtl.md) execution).
- **ArcPlane** – current plane of circle interpolation (the variable is assigned it's value directly before the call of the [PLANE](../../../../cldata/commands/plane.md) program), the value of this variable can be one of the following:
  - 33 – XY,
  - 37 – YZ,
  - 41 – XZ,
  - 133 – YX,
  - 137 – ZY,
  - 141 – ZX.

- **Feed** – current feedrate value (the variable is set prior to [FEDRAT](../../../../cldata/commands/fedrat.md) call).
- **TlComp**, **TrComp** variables – length and radius compensation values respectively (set before the [CUTCOM](../../../../cldata/commands/cutcom.md) and [LOADTL](../../../../cldata/commands/loadtl.md) commands execution).
- **FromX**, **FromY**, **FromZ** variables – coordinates of start point (set before the [FROM](../../../../cldata/commands/from.md) command).

- **FlagIn** returns:
  - 1 – if the next intersection is passed from the inside;
  - 0 – if the next intersection is passed from the outside;
  - -1 – if the intersection kind cannot be determined (for example, two adjacent NC-blocks form a colinear cuts for linear interpolation).

- **Cross** – function returns 0, if the current toolpath element conjugates with the next element, 1 is returned if the elements intersect. Generally two cuts always intersect, cut and arc can conjugate or intersect. This function can be used to implement compensation.
- **NextToolNum{(Mode)}** – returns the number of the next tool. Optional parameter Mode defines behavior for the last tool change. If mode is 0 (default value when no parameters defined) then it returns -1 after last tool change command. If mode is 1 then it returns the number of the first tool in the project.
- **ToolChange** – returns the indication of tool change (whether there will be [LOADTL](../../../../cldata/commands/loadtl.md) command in the CLData commands list):
  - 1 – there were no tool change but there will be tool change in the following commands or tool change command is being currently processed;
  - 0 – there were a tool change or it is being processed in the current command;
  - -1 – the current tool change is the last one in the CLData commands list.

The table below illustrates the way **ToolChange** function works.

| List of CLData commands | **ToolChange** function return value |
|---|---|
| PARTNO | 1 |
| ... | 1 |
| ... | 1 |
| ... | 1 |
| LOADTL | 1 |
| ... | 0 |
| ... | 0 |
| ... | 0 |
| LOADTL | 0 |
| ... | 0 |
| ... | 0 |
| ... | 0 |
| LOADTL | -1 |
| ... | -1 |
| ... | -1 |
| ... | -1 |
| FINI | -1 |

- **WorkingMode** – returns the working mode of PostProcessor Generator:
  - 1 – the PostProcessor Generator is started by CAM system during the operation, while the "G-code based simulation" mode is on. If all operations are executed at once in CAM system, [PARTNO](../../../../cldata/commands/partno.md) and [FINI](../../../../cldata/commands/fini.md) are the first and last technological commands, respectively. If the operations are performed by ones, the [PARTNO](../../../../cldata/commands/partno.md) and [FINI](../../../../cldata/commands/fini.md) commands do not generate;
  - 0 – PostProcessor Generator is run as a separate application or on the generating of the NC program from CAM system on the **Machining** tab.

**See also**

[Predefined variables and functions](readme-predefined-variables-and-functions.md)

[**GMA** array](../../../../cldata/functions/gma.md)
