# Drilling cycle

**INCT_DrillingCycleFormer** - a CAM system interface that simplifies forming the movements of drilling cycles. The object implementing this interface is returned by the function **[INCT_CLData.CreateDrillingCycleFormer](../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md), [INCT_GeomCLData.CreateDrillingCycleFormer](../../basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md)** when it is called with any of the parameters **dctSimple**, **dctWithShift**, **dctPeck**.

<img src="../../../../../images/129931515/DrillingCycleFormer.png" alt="DrillingCycleFormer" width="400">

**Purpose:**

The movements in the various drilling cycles generally follow the same tool path on different controllers (Fanuc: G74, G81, G82, G84, G85, G86, G88, G89; Sinumerik: CYCLE81, CYCLE82, CYCLE85, CYCLE87, CYCLE88, CYCLE89; Heidenhain: CYCL DEF 201, CYCL DEF 206, CYCL DEF 207, etc.):

1. Positioning the tool above the center of the hole or of the next hole at rapid traverse.
2. Moving the tool to the rapid level at rapid traverse.
3. Moving the tool to the hole bottom level at working feed.
4. Returning to the rapid level at rapid traverse.
5. Returning to the retract level at rapid traverse.
6. If the number of repetitions is not reached, returning to step 1.

The generator forms the tool path from the specified parameters: initial position, rapid level, hole bottom level, number of repetitions, etc. It also allows adding to any section of the tool path the features required by a particular cycle (dwell, oriented spindle stop, tapping, etc.), changing the feed type or value, or skipping a tool movement prepared by the generator.

**Using the generator:**

We recommend creating a new drilling cycle generator for each new cycle in a block of the NC program, except when the cycle is repeated in a new block (like CYCL CALL for Heidenhain). Therefore, the interface of the old generator must be released when a new one is created or when the interpreter finishes its work.

To form the tool movement commands along the cycle path, do the following:

1. Get the generator interface (**[INCT_CLData.CreateDrillingCycleFormer](../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md), [INCT_GeomCLData.CreateDrillingCycleFormer](../../basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md)**).
2. Set the indexes of the X, Y, Z axes along which the movements are made (**Set_AxisIndexes**).
3. Set the current plane (**Set_Plane**).
4. Set the hole center point (**Set_HoleCenter**).
5. Set the center point mode (**Set_HoleCenterMode**).
6. Set the rapid level (**Set_RapidLevel**).
7. Set the hole bottom level (**Set_BottomLevel**).
8. Set the retract level (**Set_TopLevel**).
9. Set the feed (**Set_Feedrate**) and the feed units (**Set_MPM**).
10. Set the number of cycle repetitions (**Set_Count**).
11. Assign a cycle event handler (**Set_Events**) if the cycle path needs to be changed.
12. Form the tool movement commands along the cycle path (**MakeWorkpath**).

**Description of the interface methods:**

<table>
<thead>
<tr><th>Method</th><th>Method description</th></tr>
</thead>
<tbody>
<tr><td><strong>Set_AxisIndexes</strong></td><td><p>The method sets the indexes of the X, Y, Z axes along which the movements are made when the cycle path is formed.</p><p>Input parameters: <strong>Value</strong> (<strong>TNCDCAxisIndexes</strong>) - <strong>X</strong> (integer) - index of the X axis, <strong>Y</strong> (integer) - index of the Y axis, <strong>Z</strong> (integer) - index of the Z axis.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_AxisIndexes</strong></td><td><p>The function returns the indexes of the X, Y, Z axes along which the movements are made when the cycle path is formed (<strong>TNCDCAxisIndexes</strong>).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_HoleCenter</strong></td><td><p>The method sets the coordinates of the hole center point.</p><p>Input parameters: <strong>Value</strong> (<strong>TNC3DPoint</strong>), X, Y, Z - coordinate values for the corresponding axes.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_HoleCenter</strong></td><td><p>The function returns the coordinates of the hole center point (<strong>TNC3DPoint</strong>).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_HoleCenterMode</strong></td><td><p>The method sets the center point mode.</p><p>Input parameter: <strong>Value</strong> (boolean) - center point mode. True - the coordinates of the hole center point (<strong>Set_HoleCenter</strong>) are absolute. False - the coordinates of the hole center point are relative to the current tool position.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_HoleCenterMode</strong></td><td><p>The function returns the center point mode (boolean).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_Plane</strong></td><td><p>The method sets the current plane.</p><p>Input parameter: <strong>Value</strong> (<strong>TNCPlaneType</strong>) - current plane.</p><p><strong>ptXY</strong> - XY plane, the hole is drilled along the Z axis.<br><strong>ptYZ</strong> - YZ plane, the hole is drilled along the X axis.<br><strong>ptZX</strong> - ZX plane, the hole is drilled along the Y axis.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_Plane</strong></td><td><p>The function returns the current plane (<strong>TNCPlaneType</strong>).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_RapidLevel</strong></td><td><p>The method sets the rapid level along the drilling axis.</p><p>Input parameter: <strong>Value</strong> (real number) - rapid level.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_RapidLevel</strong></td><td><p>The function returns the rapid level along the drilling axis (real number).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_BottomLevel</strong></td><td><p>The method sets the hole bottom level along the drilling axis.</p><p>Input parameter: <strong>Value</strong> (real number) - hole bottom level.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_BottomLevel</strong></td><td><p>The function returns the hole bottom level along the drilling axis (real number).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_TopLevel</strong></td><td><p>The method sets the retract level along the drilling axis.</p><p>Input parameter: <strong>Value</strong> (real number) - retract level.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_TopLevel</strong></td><td><p>The function returns the retract level along the drilling axis (real number).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_Feedrate</strong></td><td><p>The method sets the working feed.</p><p>Input parameter: <strong>Value</strong> (real number) - feed value.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_Feedrate</strong></td><td><p>The function returns the working feed (real number).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_MPM</strong></td><td><p>The method sets the feed units flag.</p><p>Input parameter: <strong>Value</strong> (boolean) - feed units flag. True - mm/min. False - mm/rev.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_MPM</strong></td><td><p>The function returns the feed units flag (boolean).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_Count</strong></td><td><p>The method sets the number of cycle repetitions.</p><p>Input parameter: <strong>Value</strong> (integer) - number of cycle repetitions.</p><p>No output parameters.</p><p>The cycle works differently depending on the hole center point mode (<strong>Set_HoleCenterMode</strong>):</p><ul><li>if the number of repetitions = 0, only the tool positioning above the hole center is made;</li><li>if the number of repetitions = 1, one iteration of the cycle is made;</li><li>if the number of repetitions &gt; 1, the cycle is repeated the specified number of times: at the same place if the coordinates of the hole center point are absolute; if they are relative, each iteration is shifted by the value set in <strong>Set_HoleCenter</strong> from the point where the previous iteration ended.</li></ul></td></tr>
<tr><td><strong>Get_Count</strong></td><td><p>The function returns the number of cycle repetitions (integer).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_Events</strong></td><td><p>The method assigns events that control the cycle behavior. Events allow adding to any section of the tool path the features required by a particular cycle (dwell, oriented spindle stop, tapping, etc.), changing the feed type or value, or skipping a tool movement prepared by the generator.</p><p>Input parameter: <strong>Value</strong> (<strong>INCT_DrillingCycleEvents</strong>) - object implementing the events. See the detailed description below.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_Events</strong></td><td><p>The function returns the object implementing the events that is linked to the cycle generator (<strong>INCT_DrillingCycleEvents</strong>).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>MakeWorkpath</strong></td><td>The method forms the cycle path from the specified parameters.</td></tr>
<tr><td><strong>Get_NextHole</strong></td><td>The function returns the coordinates of the current hole point calculated for the current iteration (<strong>TNC3DPoint</strong>). The value can be used only inside the events (<strong>Set_Events</strong>).</td></tr>
<tr><td><strong>Get_RapidPoint</strong></td><td>The function returns the coordinates of the rapid level point calculated for the current iteration (<strong>TNC3DPoint</strong>). The value can be used only inside the events (<strong>Set_Events</strong>).</td></tr>
<tr><td><strong>Get_TopPoint</strong></td><td>The function returns the coordinates of the retract level point calculated for the current iteration (<strong>TNC3DPoint</strong>). The value can be used only inside the events (<strong>Set_Events</strong>).</td></tr>
<tr><td><strong>Get_BottomPoint</strong></td><td>The function returns the coordinates of the hole bottom point calculated for the current iteration (<strong>TNC3DPoint</strong>). The value can be used only inside the events (<strong>Set_Events</strong>).</td></tr>
</tbody>
</table>

**INCT_DrillingCycleEvents** - an interface implemented in the interpreter that allows controlling the behavior of a drilling cycle. The interface is a set of event methods executed during the tool movements inside the cycle path generator. With these methods, the features required by a particular cycle (dwell, oriented spindle stop, tapping, etc.) can be added to any section of the tool path, the feed type or value can be changed, or a tool movement prepared by the generator can be skipped.

If events are assigned to the cycle path generator, every tool movement inside the generator consists of 3 stages:

1. The **INCT_DrillingCycleEvents.BeforeMove** method is executed. It receives the values set by the cycle: movement type, coordinates of the movement point, feed type.
2. The **INCT_DrillingCycleEvents.OnMove** method is executed. It receives: movement type, coordinates of the movement point, feed type and the flag of whether the movement has been made. All parameters except the movement type can be changed in the method implementation. Depending on the flag set in **OnMove**, the tool moves to the specified point with the specified feed, or the movement is not made.
3. The **INCT_DrillingCycleEvents.AfterMove** method is executed. It receives the values returned by **OnMove**: movement type, coordinates of the movement point, feed type.

**Description of the interface methods:**

| Method | Method description | Description of use |
| --- | --- | --- |
| **BeforeMove** | The method is executed before each tool movement when the cycle path is formed.<br>Input parameters: **MoveType** (**TNCDrillingCycleMoveType**) - movement type, see the description below; **Point** (**TNC3DPoint**) - coordinates of the movement point; **Feed** (**TNCFeedType**) - feed type.<br>**mtMoveToNextHole** - movement to the first or the next hole;<br>**mtMoveToRapidLevel** - movement to the rapid level;<br>**mtMoveToBottomLevel** - movement to the hole bottom;<br>**mtReturnToRapidLevel** - return to the rapid level;<br>**mtReturnToTopLevel** - return to the retract level;<br>**mtPeck**\* - used when a cycle with [chip breaking](../drilling-cycle-with-chip-breaking/drilling-cycle-with-chip-breaking.md) is formed.<br>No output parameters. | If some commands must be added before a movement, add them to the method implementation.<br>For example, to set clockwise spindle rotation before drilling the hole, call **INCT_CLData.AddSpindleSpeedOnRPM** with the appropriate parameters in the **BeforeMove** implementation under the condition **MoveType** = **mtMoveToBottomLevel**. |
| **OnMove** | The method is executed before each tool movement when the cycle path is formed.<br>Input parameters: **MoveType** (**TNCDrillingCycleMoveType**) - movement type, see the description above;<br>Input and output parameters: **Point** (**TNC3DPoint**) - coordinates of the movement point; **Feed** (**TNCFeedType**) - feed type; **Handled** (boolean) - flag of whether the movement has been made inside the implementation (True - the movement has been made, False - it has not).<br>If **Handled** is True after the **OnMove** call, the movement has been made inside the **OnMove** implementation, and the cycle generator does not add a movement command to the tool path.<br>If **Handled** is False after the **OnMove** call, the generator considers that the movement has not been made inside the **OnMove** implementation and adds to the tool path a command to move to the point **Point** with the feed type **Feed**. | To override the movement point or the feed, or to skip the movement.<br>For example, to change the feed type from rapid to working when returning after drilling, in the **OnMove** implementation set the returned **Feed** parameter to **ffWorking** under the condition **MoveType** = **mtReturnToRapidLevel** (for the feed type, see **[OutStandardFeed](../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md)**).<br>To move the tool to a point other than the one calculated by the cycle, change the **Point** parameter returned by **OnMove**.<br>If the movement to the point calculated by the cycle is not needed, set the **Handled** parameter to True inside the **OnMove** implementation. |
| **AfterMove** | The method is executed after each tool movement when the cycle path is formed, even if the movement has been canceled in **OnMove**.<br>Input parameters: **MoveType** (**TNCDrillingCycleMoveType**) - movement type, see the description above; **Point** (**TNC3DPoint**) - coordinates of the movement point; **Feed** (**TNCFeedType**) - feed type.<br>No output parameters. | If some commands must be added after a movement, add them to the method implementation.<br>For example, to add a dwell after drilling the hole, call **INCT_CLData.AddDelay** with the appropriate parameters in the **AfterMove** implementation under the condition **MoveType** = **mtMoveToBottomLevel**. |
