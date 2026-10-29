# Linear movements

**INCT_LinearMotionFormer** - a CAM system interface that simplifies forming linear movements. The interface is returned by the function **[INCT_CLData.CreateLinearMotionFormer](../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md)**.

**Purpose:**

Linear movements are formed from a block of the NC program as follows. The NC program text is [translated](../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md), that is, split into registers with values. The registers with values are added to the list of objects for interpretation. The objects of the list are interpreted. When the [objects are interpreted](../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md), a multi-axis movement command ([**INCT_CLData.OpenMultiMotion, AddMotion, CloseMultiMotion**](../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md)) is added to the tool path (**INCT_CLData**) according to the changed values of the registers linked to the machine axes of the kinematic scheme.

In more detail, the process consists of the following actions.

Before the NC program is interpreted:

1. *Get the list of registers linked to the machine axes in the kinematic scheme.*
2. *Store the list of registers with the axis indexes.*

Before a block is interpreted:

1. *Get the current tool position coordinates for all axes linked to the machine axes in the kinematic scheme.*

When registers are interpreted:

1. *Get the new values of the block registers linked to the machine axes in the kinematic scheme.*
2. *Set the new values for all changed block registers linked to the machine axes in the kinematic scheme.*

After the block is interpreted, or during the interpretation but after all registers are interpreted:

1. *Compare the new axis coordinates with the old ones to find changes.*
2. *If there was a change:*
3. *Call **OpenMultiMotion**.*
4. *Check each axis value for a change and, if the tool position along the axis has changed, call **AddMotion**.*
5. *Call **CloseMultiMotion**.*

*To execute commands that require movements in the physical machine coordinates, the movement type must also be switched to **gtmPhysic**.*

The actions from the list above that are *in italics* are implemented in the linear movement generator (**INCT_LinearMotionFormer**). Using the generator makes writing an interpreter easier.

We recommend creating one linear movement generator for the whole cycle of interpreting the NC program. Create it when the interpreter is initialized ([**INCT_Interpreter.Initialize**](../../../interpreter-loading-and-initialization/interpreter-loading-and-initialization.md)).

**Description of the interface methods:**

<table>
<thead>
<tr><th>Method</th><th>Method description</th><th>Description of use</th></tr>
</thead>
<tbody>
<tr><td><strong>SetGotoMode</strong></td><td><p>The method sets the type of the formed movements.</p><p>Input parameter: <strong>Mode</strong> (<strong>TNCGotoMode</strong>) - movement type, see the description of <strong><a href="../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md">OpenMultiMotion</a></strong>.</p><p>If the movement type is not set by the method, it is <strong>gtmTooltip</strong>.</p><p>No output parameters.</p></td><td>The method can be used when interpreting G53 in ISO code (set the movement type to <strong>gtmPhysic</strong>, then return it to <strong>gtmTooltip</strong>).</td></tr>
<tr><td><strong>Get_ClearGotoMode</strong></td><td><p>The function returns the value of the <strong>ClearGotoMode</strong> parameter (boolean).</p><p>No input parameters.</p></td><td rowspan="2"><p>The <strong>ClearGotoMode</strong> parameter controls the automatic reset of the movement type (see <strong>SetGotoMode</strong>) to <strong>gtmTooltip</strong>. The movement type is reset in <strong>InitBlock</strong>.</p><p>As a rule, the G53 command acts only in the current block, so it makes sense to set <strong>ClearGotoMode</strong> to True. Then, after a block with G53 is interpreted (where the movement type is set to <strong>gtmPhysic</strong>), the movement type returns to <strong>gtmTooltip</strong> by itself at the next <strong>InitBlock</strong> call.</p></td></tr>
<tr><td><strong>Set_ClearGotoMode</strong></td><td><p>The method sets the value of the <strong>ClearGotoMode</strong> parameter.</p><p>Input parameter: <strong>Value</strong> (boolean) - value of the <strong>ClearGotoMode</strong> parameter.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>InitAxisIndex</strong></td><td><p>The method adds an axis index to the list.</p><p>Input parameters: <strong>Index</strong> (integer) - index of the axis added to the list.</p><p>No output parameters.</p></td><td><p>Used to add the axes linked to the machine axes in the kinematic scheme. As a rule, it is called right after getting the interface (function <strong><a href="../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md">INCT_CLData.CreateLinearMotionFormer</a></strong>) in the implementation of the interpreter method <strong><a href="../../../interpreter-loading-and-initialization/interpreter-loading-and-initialization.md">INCT_Interpreter.Initialize</a></strong>.</p><p>The indexes of the registers linked to the machine axes can be obtained with the interfaces <a href="../../basic-interfaces/register-list/register-list.md"><strong>INCT_SysState</strong></a>, <a href="../../basic-interfaces/equipment-parameters/equipment-parameters.md"><strong>INCT_Equipment</strong></a>.</p></td></tr>
<tr><td><strong>ClearAxesIndexes</strong></td><td>The method clears the list of axis indexes.</td><td>Used when the tool is changed if the names of the axes controlling the tool coincide.</td></tr>
<tr><td><strong>InitBlock</strong></td><td><p>The method stores in the internal list the current tool coordinates for all axes from the list formed with <strong>InitAxisIndex</strong>. If the <strong>ClearGotoMode</strong> parameter is True, the movement type set in <strong>SetGotoMode</strong> is set to <strong>gtmTooltip</strong>.</p><p>No input and output parameters.</p></td><td>Must be used before interpreting the objects linked to registers. It is recommended to use it in the implementation of the <a href="../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md"><strong>INCT_Interpreter.BeforeInterprete</strong></a> method.</td></tr>
<tr><td><strong>SetAxisValue</strong></td><td><p>The method stores in the internal list the new tool coordinate for the specified axis.</p><p>Input parameters: <strong>Abs</strong> (boolean) - type of the new coordinate value, True - absolute value, False - relative value (relative to the current coordinate, see <strong>InitBlock</strong>); <strong>Index</strong> (integer) - axis index; <strong>Value</strong> (real number) - new value.</p><p>No output parameters.</p></td><td>Used to store the new value in the internal list to form a multi-axis movement command later. Used when interpreting in <a href="../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md"><strong>INCT_Interpreter.Interprete</strong></a>.</td></tr>
<tr><td><strong>MakeWorkpath</strong></td><td>The method compares the list of current coordinates (stored in <strong>InitBlock</strong>) with the new tool coordinates (stored in <strong>SetAxisValue</strong>). If the coordinates have changed, a multi-axis movement command along the changed axis coordinates is formed in the tool path (<a href="../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md"><strong>INCT_CLData.OpenMultiMotion, AddMotion, CloseMultiMotion</strong></a>).</td><td>To form a multi-axis movement command. Used when interpreting in <strong><a href="../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md">INCT_Interpreter.Interprete</a></strong> after all registers are interpreted (<a href="../../basic-interfaces/list-of-objects-to-interpret/list-of-objects-to-interpret.md">add it to the end of the list of objects for interpretation</a>), or in <strong><a href="../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md">INCT_Interpreter.AfterInterprete</a></strong>.</td></tr>
</tbody>
</table>

**INCT_GeomLinearMotionFormer** - a CAM system interface that simplifies forming linear movements. The interface is returned by the function **[INCT_GeomCLData.CreateLinearMotionFormer](../../basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md)**.

Its **purpose** is the same as that of the **INCT_LinearMotionFormer** interface, but for movements in geometric axes. The movements are formed by the **[CutTo3d](../../basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md)** command. Therefore, to form the first movement, the coordinates of all three axes must be set.

**Description of the interface methods:**

| Method | Method description | Description of use |
| --- | --- | --- |
| **ClearSpecifiedAxes** | The method clears the list of axes set for the first movement.<br>No input and output parameters. | Must be used at the beginning of each operation. It is recommended to use it in the implementation of the **[INCT_Interpreter.NextOperation](../../../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md)** method. |
| **InitBlock** | The method stores in the internal list the current values of the 3 tool coordinates.<br>No input and output parameters. | Must be used before interpreting the objects linked to registers. It is recommended to use it in the implementation of the [**INCT_Interpreter.BeforeInterprete**](../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md) method. |
| **SetAxisValue** | The method stores in the internal list the new tool coordinate for the specified axis.<br>Input parameters: **Abs** (boolean) - type of the new coordinate value, True - absolute value, False - relative value (relative to the current coordinate, see **InitBlock**); **Index** (integer) - axis index (1-3); **Value** (real number) - new value.<br>No output parameters. | Used to store the new value in the internal list to form a movement command later. Used when interpreting in [**INCT_Interpreter.Interprete**](../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md). |
| **MakeWorkpath** | The method compares the list of current coordinates (stored in **InitBlock**) with the new tool coordinates (stored in **SetAxisValue**). If the coordinates have changed and the coordinates of all 3 axes are set, a movement command (**[INCT_GeomCLData.CutTo3d](../../basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md)**) is formed in the tool path. | To form a movement command. Used when interpreting in **[INCT_Interpreter.Interprete](../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md)** after all registers are interpreted ([add it to the end of the list of objects for interpretation](../../basic-interfaces/list-of-objects-to-interpret/list-of-objects-to-interpret.md)), or in **[INCT_Interpreter.AfterInterprete](../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md)**. |
