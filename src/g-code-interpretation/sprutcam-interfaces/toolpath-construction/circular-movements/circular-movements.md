# Circular movements

**INCT_CircularMotionFormer** - a CAM system interface that simplifies forming movements along an arc. The interface is returned by the functions **[INCT_CLData.CreateCircularMotionFormer](../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md)**, **[INCT_GeomCLData.CreateCircularMotionFormer](../../basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md)**.

**Purpose:**

Arc movements are formed from a block of the NC program as follows. The NC program text is [translated](../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md), that is, split into registers with values. The registers with values are added to the list of objects for interpretation. The objects of the list are interpreted. When the [objects are interpreted](../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md), an arc movement command (**[INCT_CLData.AddCircle](../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md)/[INCT_GeomCLData.ArcTo2d](../../basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md)**) is added to the tool path (**INCT_CLData/INCT_GeomCLData**) according to the changed values of the registers linked to the machine axes of the kinematic scheme.

In more detail, the process consists of the following actions.

Before a block is interpreted:

1. *Get the indexes of the X, Y, Z axes for the current tool or working object.*
2. *Store the axis indexes.*
3. *Get the current tool position coordinates for the stored axes, separately for the arc center point.*

When registers are interpreted:

1. Get the new values of the block registers linked to the arc center point, end point, radius or angle, and direction.
2. *Set the new values for all changed arc parameters.*

After the block is interpreted, or during the interpretation but after all registers are interpreted:

1. *Calculate the missing parameters for **[INCT_CLData.AddCircle](../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md)/[INCT_GeomCLData.ArcTo2d](../../basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md)**.*
2. *Call **[INCT_CLData.AddCircle](../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md)/[INCT_GeomCLData.ArcTo2d](../../basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md)**.*

The actions from the list above that are *in italics* are implemented in the arc movement generator (**INCT_CircularMotionFormer**). Using the generator makes writing an interpreter easier.

We recommend creating one arc movement generator for the whole cycle of interpreting the NC program. Create it when the interpreter is initialized (**[INCT_Interpreter.Initialize](../../../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md)**).

**Description of the interface methods:**

<table>
<thead>
<tr><th>Method</th><th>Method description</th><th>Description of use</th></tr>
</thead>
<tbody>
<tr><td><strong>InitBlock</strong></td><td><p>The method stores in the internal list the axis indexes and the current X, Y, Z coordinates of the current tool or working object.</p><p>No input and output parameters.</p></td><td>Must be used before interpreting the objects linked to registers. It is recommended to use it in the implementation of the <a href="../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md"><strong>INCT_Interpreter.BeforeInterprete</strong></a> method.</td></tr>
<tr><td><strong>InitCenterPoint</strong></td><td><p>The method stores the current X, Y, Z coordinates of the current tool or working object as the center point.</p><p>No input and output parameters.</p></td><td>Must be used before interpreting the objects linked to registers. It is recommended to use it in the implementation of the <strong><a href="../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md">INCT_Interpreter.BeforeInterprete</a></strong> or <strong><a href="../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md">INCT_Interpreter.Interprete</a></strong> method (if the circle center point is not set in the current block).</td></tr>
<tr><td><strong>SetConstructMode</strong></td><td><p>The method sets the arc construction mode.</p><p>Input parameter: <strong>Mode</strong> (<strong>TNCConstructArcMode</strong>) - arc construction mode:</p><p><strong>caByCircleCenter</strong> - by the direction, end point and center of the arc;<br><strong>caByRadius</strong> - by the direction, end point and radius of the arc.</p><p>No output parameters.</p></td><td rowspan="6">Must be used when interpreting registers in the implementation of the <strong><a href="../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md">INCT_Interpreter.Interprete</a></strong> method.</td></tr>
<tr><td><strong>SetMode</strong></td><td><p>The method sets the arc direction.</p><p>Input parameter: <strong>Mode</strong> (<strong>TNCCircularMode</strong>) - arc direction:</p><p><strong>cmCW</strong> - clockwise;<br><strong>cmCCW</strong> - counterclockwise.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>SetEndPoint</strong></td><td><p>The method sets the coordinate of one axis of the end point.</p><p>Input parameters: <strong>Abs</strong> (boolean) - type of the end point value, True - absolute value, False - relative value (relative to the current coordinate, see <strong>InitBlock</strong>); <strong>AxisType</strong> (<strong>TNCAxisType</strong>) - axis: <strong>axX</strong> - X axis, <strong>axY</strong> - Y axis, <strong>axZ</strong> - Z axis; <strong>Value</strong> (real number) - coordinate value.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>SetEndPointByAngle</strong></td><td><p>The method sets the arc end point by the specified angle relative to the current point.</p><p>Input parameters: <strong>Plane</strong> (<strong>TNCPlaneType</strong>) - current plane: <strong>ptXY</strong> - XY plane, <strong>ptYZ</strong> - YZ plane, <strong>ptZX</strong> - ZX plane; <strong>Angle</strong> (real number) - arc angle.</p><p>No output parameters.</p><p><strong>Important!</strong> When a full circle is constructed (the arc angle is 360 degrees), the end point of the path must be forced to equal the start (current) point. Otherwise, because of a calculation error of hundredths or thousandths in the end point coordinates, the next movement command may become incorrect.</p><p>This is especially important for commands in which the start point is used to calculate auxiliary parameters of the path (for example, when the tool moves along a circular arc set by the coordinates of its center, the end point and the movement direction).</p></td></tr>
<tr><td><strong>SetCenterPoint</strong></td><td><p>The method sets the coordinate of one axis of the arc center point.</p><p>Input parameters: <strong>Abs</strong> (boolean) - type of the center point value, True - absolute value, False - relative value (relative to the current coordinate, see <strong>InitCenterPoint</strong>); <strong>AxisType</strong> (<strong>TNCAxisType</strong>) - axis: <strong>axX</strong> - X axis, <strong>axY</strong> - Y axis, <strong>axZ</strong> - Z axis; <strong>Value</strong> (real number) - coordinate value.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>SetRadius</strong></td><td><p>The method sets the arc radius.</p><p>Input parameter: <strong>Value</strong> (real number) - radius value.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>MakeWorkpath</strong></td><td><p>The method calculates the arc end point if an angle has been set (<strong>SetEndPointByAngle</strong>). Depending on the arc construction mode (<strong>SetConstructMode</strong>), it calculates the missing parameters for <strong>AddCircle</strong>.</p><p>It adds to the tool path an arc movement command (<strong><a href="../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md">INCT_CLData.AddCircle</a>/<a href="../../basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md">INCT_GeomCLData.ArcTo2d</a></strong>) with the calculated parameters.</p><p>Input parameter: <strong>LastPlane</strong> (<strong>TNCPlaneType</strong>) - arc plane.</p><p>No output parameters.</p></td><td>To form an arc movement command. Used when interpreting in <strong><a href="../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md">INCT_Interpreter.Interprete</a></strong> after all registers are interpreted (<a href="../../basic-interfaces/list-of-objects-to-interpret/list-of-objects-to-interpret.md">add it to the end of the list of objects for interpretation</a>), or in <strong><a href="../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md">INCT_Interpreter.AfterInterprete</a></strong>.</td></tr>
</tbody>
</table>
