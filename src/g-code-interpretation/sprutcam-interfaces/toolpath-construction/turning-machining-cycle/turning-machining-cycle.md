# Turning machining cycle

**INCT_LatheStockRemovalCycleFormer** - a CAM system interface that simplifies forming the movements of a turning cycle along a specified contour. The object implementing this interface is returned by the function **[INCT_CLData.CreateLatheCycleFormer](../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md), [INCT_GeomCLData.CreateLatheCycleFormer](../../basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md)** when it is called with the **lctStockRemoval** parameter.

The **INCT_LatheStockRemovalCycleFormer2** interface extends the capabilities of the turning cycle generator along a specified contour. Its new properties and methods are described below. The object implementing this interface is returned by the function **[CreateLatheCycleFormer](../../basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md)** (as for **INCT_LatheStockRemovalCycleFormer**).

<img src="../../../../../images/129931501/LatheStockRemovalCycle_Bars.png" alt="LatheStockRemovalCycle_Bars" width="900">

<img src="../../../../../images/129931501/LatheStockRemovalCycle_CopyContour.png" alt="LatheStockRemovalCycle_CopyContour" width="900">

<img src="../../../../../images/129931501/LatheStockRemovalCycle_Finishing.png" alt="LatheStockRemovalCycle_Finishing" width="900">

<img src="../../../../../images/129931501/LatheStockRemovalCycle_Params.png" alt="LatheStockRemovalCycle_Params" width="700">

**Purpose:**

The movements in the various types of turning cycles along a specified contour generally follow the same tool path on different controllers:

1. Approach of the tool to the start point or to the point of the next pass at rapid traverse.
2. Approach to the level of the roughing pass at rapid traverse.
3. Movement to the point of the roughing pass parallel to the longitudinal axis at working feed (roughing pass).
4. Return parallel to the contour, along the contour with the finishing allowance, to the last point of the roughing pass at working feed (end of the roughing pass).
5. Return to the retraction plane at rapid traverse.
6. Returning to step 1 if the machining depth is not reached.
7. Finishing of the contour (approach to the start point at rapid traverse, finishing along the contour at working feed, retraction at rapid traverse).

Example of such a cycle: Sinumerik: CYCLE95.

The generator forms the tool path from the specified parameters: contour path, retraction plane, machining step, machining type and direction, etc. It also allows adding to any section of the tool path the features required by a particular cycle, changing the feed type or value, or skipping a tool movement prepared by the generator.

**Using the generator:**

We recommend creating a new turning cycle generator for each new cycle in a block of the NC program, except when the cycle is repeated in a new block. Therefore, the interface of the old generator must be released when a new one is created or when the interpreter finishes its work.

To form the tool movement commands along the cycle path, do the following:

1. Get the generator interface (**[INCT_CLData.CreateLatheCycleFormer](../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md), [INCT_GeomCLData.CreateLatheCycleFormer](../../basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md)**).
2. Set the indexes of the longitudinal and transverse axes along which the movements are made (**Set_AxisIndexes**).
3. Set the cycle parameters (**Set_NCProgram**, **Set_MachiningType**, **Set_MachiningDirection**, **Set_Overlap**, etc., see the description below).
4. Assign a cycle event handler (**Set_Events**) if the cycle path needs to be changed.
5. Form the tool movement commands along the cycle path (**MakeWorkpath**).

**Description of the interface methods:**

<table>
<thead>
<tr><th>Method</th><th>Method description</th></tr>
</thead>
<tbody>
<tr><td><strong>Set_AxisIndexes</strong></td><td><p>The method sets the indexes of the longitudinal and transverse axes along which the movements are made when the cycle path is formed.</p><p>Input parameters: <strong>Value</strong> (<strong>TNCLCAxisIndexes</strong>) - <strong>Transverse</strong> (integer) - index of the transverse axis, <strong>Longitudinal</strong> (integer) - index of the longitudinal axis.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_AxisIndexes</strong></td><td><p>The function returns the indexes of the longitudinal and transverse axes along which the movements are made when the cycle path is formed (<strong>TNCLCAxisIndexes</strong>).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_Plane</strong></td><td><p>The method sets the current plane for the NC program of the contour. If the plane is not set, the current plane at the moment of getting the contour geometry is used.</p><p>Input parameters: <strong>Value</strong> (<strong>TNCPlaneType</strong>) - current plane for the NC program of the contour.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_Plane</strong></td><td><p>The function returns the current plane for the NC program of the contour.</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_NCProgram</strong></td><td><p>The method passes to the generator the interface implementing the text of the contour NC program.</p><p>Input parameter: <strong>Value</strong> (<strong>INCT_Program</strong>) - interface implementing the text of the contour NC program.</p><p>The contour text can be obtained using the <strong><a href="../../basic-interfaces/nc-program-management/nc-program-management.md">INCT_ProgramManager.GetPartByIndex, INCT_ProgramManager.GetPartByLabels</a></strong> methods.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_NCProgram</strong></td><td><p>The function returns the interface implementing the text of the contour NC program (<strong>INCT_Program</strong>).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_RecalcContourGeometry</strong></td><td><p>The method sets the flag of whether the contour NC program must be interpreted.</p><p>Input parameter: <strong>Value</strong> (boolean) - False - do not interpret the contour NC program if it has already been interpreted, True - interpret the contour NC program in any case.</p></td></tr>
<tr><td><strong>Get_RecalcContourGeometry</strong></td><td><p>The function returns the flag of whether the contour NC program must be interpreted.</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_MachiningProcessing</strong></td><td><p>The method sets the machining kind.</p><p>Input parameter: <strong>Value</strong> (<strong>TNCMachiningProcessing</strong>) - machining kind.</p><p><strong>mpRoughing</strong> - roughing (several passes are made taking into account the specified allowance, step, etc.);<br><strong>mpFinishing</strong> - finishing (only one pass along the contour without allowance is made).</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_MachiningProcessing</strong></td><td><p>The function returns the machining kind.</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_MachiningType</strong></td><td><p>The method sets the machining type.</p><p>Input parameter: <strong>Value</strong> (<strong>TNCLatheMachiningType</strong>) - machining type.</p><p><strong>mtInside</strong> - inside;<br><strong>mtOutside</strong> - outside.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_MachiningType</strong></td><td><p>The function returns the machining type (<strong>TNCLatheMachiningType</strong>).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_MachiningDirection</strong></td><td><p>The method sets the machining direction.</p><p>Input parameter: <strong>Value</strong> (<strong>TNCLatheMachiningDirection</strong>) - machining direction.</p><p><strong>mdLongitudinal</strong> - longitudinal;<br><strong>mdTransverse</strong> - transverse.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_MachiningDirection</strong></td><td><p>The function returns the machining direction (<strong>TNCLatheMachiningDirection</strong>).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_MachiningStyle</strong></td><td><p>The method sets the contour machining style for roughing.</p><p>Input parameters: <strong>Value</strong> (<strong>TNCLatheMachiningStyle</strong>) - machining style. <strong>msBars</strong> - at each iteration the machining is parallel to the axis (longitudinal or transverse depending on <strong>MachiningDirection</strong>); <strong>msCopyContour</strong> - at each iteration the machining is parallel to the contour (contour copy).</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_MachiningStyle</strong></td><td><p>The function returns the contour machining style for roughing.</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_Overlap</strong></td><td><p>The method sets the overtravel type.</p><p>Input parameter: <strong>Value</strong> (boolean) - overtravel type. True - with return along the contour, False - with direct return.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_Overlap</strong></td><td><p>The function returns the overtravel type (boolean).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_AxialStock</strong></td><td><p>The method sets the axial allowance on the contour.</p><p>Input parameter: <strong>Value</strong> (real number) - axial allowance on the contour.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_AxialStock</strong></td><td><p>The function returns the axial allowance on the contour (real number).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_RadialStock</strong></td><td><p>The method sets the radial allowance on the contour.</p><p>Input parameter: <strong>Value</strong> (real number) - radial allowance on the contour.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_RadialStock</strong></td><td><p>The function returns the radial allowance on the contour (real number).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_ProfileStock</strong></td><td><p>The method sets the equidistant allowance on the contour.</p><p>Input parameter: <strong>Value</strong> (real number) - equidistant allowance on the contour.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_ProfileStock</strong></td><td><p>The function returns the equidistant allowance on the contour (real number).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_StartPointMode</strong></td><td><p>The method sets the mode of setting the contour start point.</p><p>Input parameters: <strong>Value</strong> (<strong>TNCLatheStartPointMode</strong>) - mode of setting the contour start point. <strong>spmCalcPoint</strong> - the start point is calculated by the cycle; <strong>spmSetPoint</strong> - the start point is set (see <strong>StartPoint</strong>).</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_StartPointMode</strong></td><td><p>The function returns the mode of setting the contour start point.</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_StartPoint</strong></td><td><p>The method sets the cycle start point (for the mode <strong>StartPointMode = spmSetPoint</strong>).</p><p>Input parameters: <strong>Value</strong> (<strong>TNC2DPoint</strong>) - cycle start point.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_StartPoint</strong></td><td><p>The function returns the cycle start point.</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_EachReliefcutSeparately</strong></td><td><p>The method sets the flag of machining the relief cuts.</p><p>Input parameter: <strong>Value</strong> (boolean) - True - each relief cut is machined separately, False - all relief cuts are machined in one pass.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_EachReliefcutSeparately</strong></td><td><p>The function returns the flag of machining the relief cuts.</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_DoReliefcutsInReverseOrder</strong></td><td><p>The method sets the flag of the order of machining the relief cuts.</p><p>Input parameters: <strong>Value</strong> (boolean) - flag of the order of machining the relief cuts. <strong>True</strong> - machine the relief cuts in reverse order. <strong>False</strong> - machine the relief cuts in direct order.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_DoReliefcutsInReverseOrder</strong></td><td><p>The function returns the flag of the order of machining the relief cuts.</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_StepType</strong></td><td><p>The method sets the type of calculating the roughing step.</p><p>Input parameter: <strong>Value</strong> (<strong>TNCLatheStepType</strong>) - type of calculating the roughing step.</p><p><strong>stConst</strong> - at each pass the machining depth equals the machining step (<strong>Set_Step</strong>);<br><strong>stCalcEvenly</strong> - at each stage (relief cut) the generator calculates the number of steps from the machining step (<strong>Set_Step</strong>) and machines in equal steps (depth of cut / number of steps).</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_StepType</strong></td><td><p>The function returns the type of the roughing step (<strong>TNCLatheStepType</strong>).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_Step</strong></td><td><p>The method sets the machining step.</p><p>Input parameter: <strong>Value</strong> (real number) - machining step.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_Step</strong></td><td><p>The function returns the machining step (real number).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_SafeDist</strong></td><td><p>The method sets the retraction for the return (the side retraction before the tool exits).</p><p>Input parameter: <strong>Value</strong> (real number) - retraction value.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_SafeDist</strong></td><td><p>The function returns the retraction for the return (real number).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_LengthChipBreaking</strong></td><td><p>The method sets the travel length for chip breaking.</p><p>Input parameter: <strong>Value</strong> (real number) - travel length for chip breaking.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_LengthChipBreaking</strong></td><td><p>The function returns the travel length for chip breaking (real number).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_Feedrate</strong></td><td><p>The method sets the working feed.</p><p>Input parameter: <strong>Value</strong> (real number) - working feed.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_Feedrate</strong></td><td><p>The function returns the working feed.</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_MPM</strong></td><td><p>The method sets the working feed units.</p><p>Input parameter: <strong>Value</strong> (boolean) - working feed units. True - mm/min, False - mm/rev.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_MPM</strong></td><td><p>The function returns the working feed units.</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_UseContourFeedrate</strong></td><td><p>The method sets the flag of using the feed set in the NC program of the contour.</p><p>Input parameters: <strong>Value</strong> (boolean) - flag of using the feed. True - the feed set in the contour NC program is used when machining the same contour sections. False - the feed set in the contour is ignored.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_UseContourFeedrate</strong></td><td><p>The function returns the flag of using the feed set in the NC program of the contour.</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Set_Events</strong></td><td><p>The method assigns events that control the cycle behavior. Events allow adding to any section of the tool path the features required by a particular cycle (dwell, oriented spindle stop, etc.), changing the feed type or value, or skipping a tool movement prepared by the generator.</p><p>Input parameter: <strong>Value</strong> (interface) - object implementing the interfaces <strong>INCT_LatheCycleEvents</strong> (described in detail in the article <a href="../turning-cycle-grooving/turning-cycle-grooving.md">Turning cycle grooving</a>) and <strong>INCT_LatheCycleArcEvents</strong> (described below).</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_Events</strong></td><td><p>The function returns the object implementing the events that is linked to the cycle generator (<strong>INCT_LatheCycleEvents</strong>, <strong>INCT_LatheCycleArcEvents</strong>).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Get_SignLongitudinal</strong></td><td><p>The function returns the sign of the longitudinal machining (integer). 1 - the direction coincides with the longitudinal axis, 0 - the direction is not defined, -1 - the direction is opposite to the longitudinal axis.</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Get_SignTransverse</strong></td><td><p>The function returns the sign of the transverse machining (integer). 1 - the direction coincides with the transverse axis, 0 - the direction is not defined, -1 - the direction is opposite to the transverse axis.</p><p>No input parameters.</p></td></tr>
<tr><td><strong>MakeWorkpath</strong></td><td><p>The method forms the cycle path from the specified parameters. The tool path is formed as follows:</p><ol><li>Getting the current state of the interpreter (method <strong>INCT_InterpreterState.Save</strong>) if the interpreter supports the <strong>INCT_InterpreterState</strong> interface (described below).</li><li>Creating and initializing a new interpreter instance.</li><li>Restoring the current state for the new interpreter instance (<strong>INCT_InterpreterState.Load</strong>).</li><li>Running the new interpreter on the NC program of the cycle contour text to form the contour path.</li><li>After the new interpreter finishes, the tool path is formed from the specified parameters and the obtained contour path.</li></ol></td></tr>
</tbody>
</table>

**INCT_LatheStockRemovalCycleFormer2** extends the capabilities of the turning cycle generator along a specified contour.

| Method | Method description |
| --- | --- |
| **Set_PassReturnMethod** | The method sets the order of the return to the pass entry point.<br>Input parameter: **Value** (**TNCPassReturnMethod**) - order of the return to the pass entry point. **prmStepwise** - at each cycle iteration the return is made first normal to the feed axis and then normal to the machining axis; **prmDirect** - at each cycle iteration the return is made directly to the entry point of the next pass.<br>No output parameters. |
| **Get_PassReturnMethod** | The function returns the order of the return to the pass entry point (**TNCPassReturnMethod**).<br>No input parameters. |
| **Set_CutDepthCalcMethod** | The method sets the way the depth of cut is determined.<br>Input parameter: **Value** (**TNCCutDepthCalcMethod**) - way of determining the depth of cut. **cdcByStep** - the depth of each cut is equal to or (at the last cycle iteration) less than the specified machining step; **cdcByCount** - the depth of each cut is calculated from the specified number of cycle repetitions.<br>No output parameters. |
| **Get_CutDepthCalcMethod** | The function returns the way the depth of cut is determined (**TNCCutDepthCalcMethod**).<br>No input parameters. |
| **Set_Count** | The method sets the number of cycle repetitions (for the way of determining the depth of cut by the number of repetitions, **cdcByCount**).<br>Input parameter: **Value** (integer) - number of repetitions.<br>No output parameters. |
| **Get_Count** | The function returns the number of cycle repetitions (for the way of determining the depth of cut by the number of repetitions, **cdcByCount**).<br>No input parameters. |
| **Set_Offset** | The method sets the offset of the contour machining start point at each pass.<br>Input parameter: **Value** (real number) - offset of the contour start point.<br>No output parameters. |
| **Get_Offset** | The function returns the offset of the contour machining start point at each pass.<br>No input parameters. |
| **Get_ContourStartPoint** | The function returns the coordinates of the contour start point taking into account the allowance set in the generator (**TNC2DPoint**). |
| **Get_ContourEndPoint** | The function returns the coordinates of the contour end point taking into account the allowance set in the generator (**TNC2DPoint**). |
| **Set_AxialStockDependsOnContour** | The method sets how the axial and radial allowances (**Set_AxialStock**, **Set_RadialStock**) are taken into account.<br>Input parameter: **Value** (boolean). True (default) - the allowances are taken as absolute values, and the shift direction is determined by the contour and the machining direction; False - the allowances are treated as shifts along the axes with the specified sign.<br>No output parameters. |
| **Get_AxialStockDependsOnContour** | The function returns how the axial and radial allowances are taken into account (boolean).<br>No input parameters. |
| **Set_StartPointContainsSafeDist** | The method sets whether the retraction value (**Set_SafeDist**) is taken into account when the cycle start point is calculated (for the mode **StartPointMode = spmCalcPoint**).<br>Input parameter: **Value** (boolean). True (default) - the start point is moved away from the contour by the allowance and the retraction value; False - by the allowance only.<br>No output parameters. |
| **Get_StartPointContainsSafeDist** | The function returns whether the retraction value is taken into account when the cycle start point is calculated (boolean).<br>No input parameters. |

**INCT_LatheCycleArcEvents** - an interface implemented in the interpreter that allows controlling the behavior of a turning cycle when arcs are formed. The interface consists of one event method executed when the tool moves along an arc inside the cycle path generator. With this method, the features required by a particular cycle (dwell, oriented spindle stop, etc.) can be added to any section of the tool path, the feed type can be changed, or a tool movement prepared by the generator can be skipped.

**Description of the interface method:**

| Method | Method description | Description of use |
| --- | --- | --- |
| **OnArc** | The method is executed before each tool movement along an arc when the cycle path is formed.<br>Input parameters: **MoveType** (**TNCLatheCycleMoveType**) - movement type, see [Turning cycle grooving](../turning-cycle-grooving/turning-cycle-grooving.md);<br>Input and output parameters: **Center** (**TNC2DPoint**) - coordinates of the arc center; **Point** (**TNC2DPoint**) - coordinates of the arc end point; **Radius** (real number) - arc radius; **Feed** (**TNCFeedType**) - feed type; **Handled** (boolean) - flag of whether the movement has been made inside the implementation (True - the movement has been made, False - it has not).<br>If **Handled** is True after the **OnArc** call, the movement has been made inside the **OnArc** implementation, and the cycle generator does not add an arc movement command to the tool path.<br>If **Handled** is False after the **OnArc** call, the generator considers that the arc movement has not been made inside the **OnArc** implementation and adds to the tool path a command to move along an arc to the point **Point** with the feed type **Feed**. | To override the arc movement or the feed, or to skip the movement.<br>For example, to switch to rapid traverse when returning to the initial level after grooving, in the **OnArc** implementation set the returned **Feed** parameter to **ffRapid** under the condition **MoveType** = **lmReturnToTopLevel** (for the feed type, see **[OutStandardFeed](../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md)**).<br>To move the tool to a point other than the one calculated by the cycle, change the **Center**, **Point**, **Radius** parameters returned by **OnArc**.<br>If the movement to the point calculated by the cycle is not needed, set the **Handled** parameter to True inside the **OnArc** implementation. |

**INCT_LatheStockRemovalCycleEvents** - an interface implemented in the interpreter that allows controlling the behavior of the turning machining cycle. The interface consists of one event method executed after the contour geometry is obtained and before the cycle path is calculated. With this method and the **INCT_InterpreterState** interface, the contour parameters can be obtained from the NC program text and passed to the cycle path generator for correct forming (for example, the machining direction if it is set by a command in the contour path).

**Description of the interface methods:**

| Method | Method description | Description of use |
| --- | --- | --- |
| **OnCalcContourGeometry** | The method is executed after the contour geometry is obtained and before the generator calculates the cycle path.<br>No parameters. | With this method and the **INCT_InterpreterState** interface, the contour parameters can be obtained from the NC program text and passed to the cycle path generator for correct forming (for example, the machining direction if it is set by a command in the contour path). |

**INCT_LatheStockRemovalCycleEvents2** - an interface implemented in the interpreter that allows controlling the behavior of the turning machining cycle. It extends the **INCT_LatheStockRemovalCycleEvents** interface.

**Description of the interface methods:**

| Method | Method description | Description of use |
| --- | --- | --- |
| **OnCalcNextStep** | The method is executed when the tool path is calculated for each pass. It is intended for changing the step and the offset used to calculate the next start point of the pass along the contour and the return point after the pass along the contour for the current iteration.<br>Input parameters: **Iteration** (integer) - pass number starting from 1; **PointType** (**TNCLSRPointType**) - type of the contour point: **ptProfilePoint** - start point of the pass along the contour; **ptReturnPoint** - return point after the pass along the contour.<br>Input and output parameters: **Step** (real number) - step for calculating the current pass (infeed axis); **Offset** (real number) - offset for calculating the current pass (the axis opposite to the infeed axis). | With this method, your own algorithm of calculating the start points of the passes along the contour and the return points after them can be set for each pass by operating the step and the offset at the current iteration. |
| **OnCalcNextPoint** | The method is executed when the tool path is calculated for each pass. It is intended for changing the coordinates of the start point of the pass along the contour and of the return point after the pass, calculated for the current iteration.<br>Input parameters: **Iteration** (integer) - pass number starting from 1; **PointType** (**TNCLSRPointType**) - type of the contour point: **ptProfilePoint** - start point of the pass along the contour; **ptReturnPoint** - return point after the pass along the contour.<br>Input and output parameters: **Point** (**TNC2DPoint**) - point coordinates. | With this method, your own algorithm of calculating the start points of the passes along the contour and the return points after them can be set for each pass by operating the point coordinates at the current iteration. |

**INCT_LatheStockRemovalCycleEvents3** - an interface implemented in the interpreter that allows controlling the behavior of the turning cycle. It extends the **INCT_LatheStockRemovalCycleEvents** interface.

**Description of the interface methods:**

| Method | Method description | Description of use |
| --- | --- | --- |
| **OnCalcSafeCut** | The method is executed when the tool path is calculated. It is intended for changing the retraction values for the return calculated inside the cycle (the side retraction before the tool exits).<br>Input and output parameters: **Point** (**TNC2DPoint**) - point coordinates (relative). | With this method, your own retraction value can be set. By default the cycle calculates it from **Set_SafeDist** along both axes away from the contour. The value is used for the approach, for the return to the safe distance and for calculating the levels of the passes. |

**INCT_InterpreterState** - an interface implemented by the interpreter (by the same object that implements the **INCT_Interpreter** interface) that allows saving the current state of the interpreter and loading it into a newly created interpreter instance for correct forming of the contour path.

For example, the current plane must be known to form the contour path. For this, the interpreter must create an object, save the current plane in it (method **Save**), and, when a new interpreter instance is created, restore the current plane from the object passed to it (method **Load**).

**Description of the interface methods:**

<table>
<thead>
<tr><th>Method</th><th>Method description</th><th>Description of use</th></tr>
</thead>
<tbody>
<tr><td><strong>Save</strong></td><td><p>The method must create an object implementing its own interface, save the data of the current state in the object and pass the interface of the object in the output parameter.</p><p>No input parameters.</p><p>Output parameter: <strong>State</strong> - <strong>IUnknown</strong> interface.</p></td><td rowspan="2">To form the contour path, the current plane set in the NC program text must be known. In the implementation of the <strong>Save</strong> method, save the current plane in the object created inside the method. The CAM system kernel passes the reference to the object to the new interpreter instance by calling the <strong>Load</strong> method. In its implementation, get the current plane from the passed object.</td></tr>
<tr><td><strong>Load</strong></td><td><p>The method must get its own interface from the object passed in the input parameter and get the current state of the interpreter required to form the contour path.</p><p>Input parameter: <strong>State</strong> - <strong>IUnknown</strong> interface.</p><p>No output parameters.</p></td></tr>
</tbody>
</table>
