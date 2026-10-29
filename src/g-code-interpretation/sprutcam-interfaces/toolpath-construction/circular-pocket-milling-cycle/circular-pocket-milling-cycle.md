# Circular pocket milling cycle

**INCT_PocketCycleFormer** - a CAM system interface that simplifies forming the movements of a circular pocket milling cycle. The object implementing this interface is returned by the method **INCT_CLData_PocketCycleFormer.CreatePocketCycleFormer**.

<img src="../../../../../images/146900417/1.PNG" alt="1" height="250"><img src="../../../../../images/146900417/2.PNG" alt="2" height="250"><img src="../../../../../images/146900417/3.PNG" alt="3" height="250"><img src="../../../../../images/146900417/4.PNG" alt="4" height="250"><img src="../../../../../images/146900417/5.PNG" alt="5" height="250"><img src="../../../../../images/146900417/6.PNG" alt="6" height="250">

**Purpose:**

The movements in the various types of circular pocket milling cycles generally follow the same tool path on different controllers:

1. Approach to the pocket center at the initial level.
2. Approach to the safe distance.
3. Approach to the base point.
4. Plunging (helical or linear) to the specified depth of cut or to the full depth.
5. Retraction to the safe distance and repetition down to the pocket depth; in finishing, the tool goes directly to the pocket depth.
6. Return to the pocket center at the level where the machining started, here at the initial level.

Example of such a cycle: Sinumerik: POCKET4.

The generator forms the tool path from the specified parameters. It also allows adding to any section of the tool path the features required by a particular cycle, changing the feed type or value, or skipping a tool movement prepared by the generator.

**Using the generator:**

We recommend creating a new generator for each new cycle in a block of the NC program. Therefore, the interface of the old generator must be released when a new one is created or when the interpreter finishes its work.

1. Get the generator interface (**INCT_CLData_PocketCycleFormer.CreatePocketCycleFormer**).
2. Set the indexes of the axes along which the movements are made (**Set_AxisIndexes**).
3. Set the current plane (**Set_Plane**).
4. Set the pocket center (**Set_HoleCenter**).
5. Set the safe distance (**Set_SafeLevel**).
6. Set the pocket start (**Set_BaseLevel**).
7. Set the pocket bottom level (**Set_BottomLevel**).
8. Set the pocket diameter (**Set_Diameter**).
9. Set the flat spiral step (**Set_FlatSpiralStep**).
10. Set the flat spiral step type (**Set_FlatSpiralStepType**).
11. Set the flat spiral direction (**Set_FlatSpiralDirection**).
12. Set the helix direction (**Set_SpiralDirection**).
13. Set the helix pitch (**Set_SpiralStep**).
14. Set the machining type (**Set_TypeOfHoleProcessing**).
15. Set the depth of cut per pass (**Set_Degression**).
16. Set the plunge radius (**Set_PlungeRadius**).
17. Set the allowance at the pocket edge (**Set_EdgeStock**).
18. Set the allowance at the pocket bottom (**Set_BottomStock**).
19. Assign a cycle event handler (**Set_Events**) if the cycle path needs to be changed.
20. Form the tool movement commands along the cycle path (**MakeWorkpath**).

**Description of the interface methods:**

| Method | Method description |
| --- | --- |
| **Set_AxisIndexes** | The method sets the indexes of the X, Y, Z axes along which the movements are made when the cycle path is formed.<br>Input parameters: **Value** (**TNCDCAxisIndexes**) - **X** (integer) - index of the X axis, **Y** (integer) - index of the Y axis, **Z** (integer) - index of the Z axis.<br>No output parameters. |
| **Get_AxisIndexes** | The function returns the indexes of the X, Y, Z axes along which the movements are made when the cycle path is formed (**TNCDCAxisIndexes**).<br>No input parameters. |
| **Set_Plane** | The method sets the current plane.<br>Input parameter: **Value** (**TNCPlaneType**) - current plane.<br>**ptXY** - XY plane, the pocket is machined along the Z axis;<br>**ptYZ** - YZ plane, the pocket is machined along the X axis;<br>**ptZX** - ZX plane, the pocket is machined along the Y axis.<br>No output parameters. |
| **Get_Plane** | The function returns the current plane (**TNCPlaneType**).<br>No input parameters. |
| **Set_HoleCenter** | The method sets the pocket center point.<br>Input parameter: **Value** (**TNC3DPoint**) - pocket center point.<br>No output parameters. |
| **Get_HoleCenter** | The function returns the pocket center point (**TNC3DPoint**).<br>No input parameters. |
| **Set_SafeLevel** | The method sets the safe distance.<br>Input parameter: **Value** (real number) - safe distance.<br>No output parameters. |
| **Get_SafeLevel** | The function returns the safe distance (real number).<br>No input parameters. |
| **Set_BaseLevel** | The method sets the pocket start.<br>Input parameter: **Value** (real number) - pocket start.<br>No output parameters. |
| **Get_BaseLevel** | The function returns the pocket start (real number).<br>No input parameters. |
| **Set_Diameter** | The method sets the pocket diameter.<br>Input parameter: **Value** (real number) - pocket diameter.<br>No output parameters. |
| **Get_Diameter** | The function returns the pocket diameter (real number).<br>No input parameters. |
| **Set_FlatSpiralStep** | The method sets the flat spiral step.<br>Input parameter: **Value** (real number) - flat spiral step.<br>No output parameters. |
| **Get_FlatSpiralStep** | The function returns the flat spiral step (real number).<br>No input parameters. |
| **Set_BottomLevel** | The method sets the pocket bottom level.<br>Input parameter: **Value** (real number) - pocket bottom level.<br>No output parameters. |
| **Get_BottomLevel** | The function returns the pocket bottom level (real number).<br>No input parameters. |
| **Set_FlatSpiralStepType** | The method sets the flat spiral step type.<br>Input parameter: **Value** (**TNCFlatSpiralStepType**) - flat spiral step type.<br>**fsByMillimeters** - the spiral step is calculated in millimeters;<br>**fsByPersentOfToolDiameter** - the spiral step is calculated as a percentage of the tool diameter.<br>No output parameters. |
| **Get_FlatSpiralStepType** | The function returns the flat spiral step type (**TNCFlatSpiralStepType**).<br>No input parameters. |
| **Set_FlatSpiralDirection** | The method sets the flat spiral direction.<br>Input parameter: **Value** (**TNCSpiralDirection**) - flat spiral direction.<br>**sdCW** - clockwise;<br>**sdCCW** - counterclockwise.<br>No output parameters. |
| **Get_FlatSpiralDirection** | The function returns the flat spiral direction (**TNCSpiralDirection**).<br>No input parameters. |
| **Set_SpiralDirection** | The method sets the helix direction.<br>Input parameter: **Value** (**TNCSpiralDirection**) - helix direction.<br>**sdCW** - clockwise;<br>**sdCCW** - counterclockwise.<br>No output parameters. |
| **Get_SpiralDirection** | The function returns the helix direction (**TNCSpiralDirection**).<br>No input parameters. |
| **Set_TypeOfHoleProcessing** | The method sets the pocket machining type.<br>Input parameter: **Value** (**TNCTypeOfProcessing**) - pocket machining type.<br>**tpHelicalPlungeRoughing** - roughing, helical plunge, machining with a flat spiral;<br>**tpLinearPlungeRoughing** - roughing, linear plunge, machining with a flat spiral;<br>**tpOnlyHelicalRoughing** - roughing, fully helical machining;<br>**tpOnlyHelicalFinishing** - finishing, helical machining along the edge;<br>**tpOnlyCircularFinishing** - finishing, machining along the edge with circles;<br>**tpOnlyHelicalFinishingAndBottom** - finishing, helical machining along the edge, machining of the bottom with a flat spiral.<br>No output parameters. |
| **Get_TypeOfHoleProcessing** | The function returns the pocket machining type (**TNCTypeOfProcessing**).<br>No input parameters. |
| **Set_SpiralStep** | The method sets the helix pitch.<br>Input parameter: **Value** (real number) - helix pitch.<br>No output parameters. |
| **Get_SpiralStep** | The function returns the helix pitch (real number).<br>No input parameters. |
| **Set_Degression** | The method sets the depth of cut per pass.<br>Input parameter: **Value** (real number) - depth of cut per pass.<br>No output parameters. |
| **Get_Degression** | The function returns the depth of cut per pass (real number).<br>No input parameters. |
| **Set_DepthOfCut** | The method stores a depth of cut value. The generator does not use it when forming the tool path; the depth of cut per pass is set by **Set_Degression**.<br>Input parameter: **Value** (real number) - depth of cut.<br>No output parameters. |
| **Get_DepthOfCut** | The function returns the value stored by **Set_DepthOfCut** (real number).<br>No input parameters. |
| **Set_PlungeRadius** | The method sets the plunge radius: the lateral offset from the pocket center before helical plunging (machining type **tpHelicalPlungeRoughing**).<br>Input parameter: **Value** (real number) - plunge radius.<br>No output parameters. |
| **Get_PlungeRadius** | The function returns the plunge radius (real number).<br>No input parameters. |
| **Set_EdgeStock** | The method sets the allowance at the pocket edge for roughing.<br>Input parameter: **Value** (real number) - allowance at the pocket edge.<br>No output parameters. |
| **Get_EdgeStock** | The function returns the allowance at the pocket edge for roughing (real number).<br>No input parameters. |
| **Set_BottomStock** | The method sets the allowance at the pocket bottom for roughing.<br>Input parameter: **Value** (real number) - allowance at the pocket bottom.<br>No output parameters. |
| **Get_BottomStock** | The function returns the allowance at the pocket bottom for roughing (real number).<br>No input parameters. |
| **Set_Events** | The method assigns events that control the cycle behavior. Events allow adding to any section of the tool path the features required by a particular cycle, changing the feed type or value, or skipping a tool movement prepared by the generator.<br>Input parameter: **Value** (**INCT_PocketCycleEvents**) - object implementing the events. See the detailed description below.<br>No output parameters. |
| **Get_Events** | The function returns the object implementing the events that is linked to the generator (**INCT_PocketCycleEvents**).<br>No input parameters. |
| **MakeWorkpath** | The method forms the cycle path from the specified parameters. |

**INCT_PocketCycleEvents** - an interface implemented in the interpreter that allows controlling the behavior of the circular pocket milling cycle. The interface is a set of event methods executed during the tool movements inside the generator. With these methods, the features required by a particular cycle (dwell, oriented spindle stop, etc.) can be added to any section of the tool path, the feed type can be changed, or a tool movement prepared by the generator can be skipped.

If events are assigned to the generator, every tool movement inside the generator consists of 3 stages:

1. The **INCT_PocketCycleEvents.BeforeMove** method is executed. It receives the values set by the cycle: movement type, coordinates of the movement point, feed type.
2. The **INCT_PocketCycleEvents.OnMove** method is executed. It receives: movement type, coordinates of the movement point, feed type and the flag of whether the movement has been made. All parameters except the movement type can be changed in the implementation. Depending on the flag set in **OnMove**, the tool moves to the specified point with the specified feed, or the movement is not made.
3. The **INCT_PocketCycleEvents.AfterMove** method is executed. It receives the values returned by **OnMove**: movement type, coordinates of the movement point, feed type.

**Description of the interface methods:**

| Method | Method description | Description of use |
| --- | --- | --- |
| **BeforeMove** | The method is executed before each tool movement when the cycle path is formed.<br>Input parameters: **MoveType** (**TNCPocketCycleMoveType**) - movement type, see the description below; **Point** (**TNC3DPoint**) - coordinates of the movement point; **Feed** (**TNCFeedType**) - feed type.<br>**pcmMoveToHoleCenter** - movement to the pocket center;<br>**pcmMoveToSafeLevel** - movement to the safe distance;<br>**pcmMoveToCutOfDepthByLine** - linear movement to the depth of cut;<br>**pcmMoveToCutOfDepthByHelic** - helical movement to the depth of cut;<br>**pcmMoveToAside** - movement from the center toward the pocket edge;<br>**pcmMoveToHoleEdge** - movement along the flat spiral to the pocket edge;<br>**pcmMoveOnHoleEdge** - movement along the pocket edge;<br>**pcmMoveToTopLevel** - movement to the start point;<br>**pcmMoveFromHoleEdgeToCenter** - movement from the edge to the pocket center.<br>No output parameters. | If some commands must be added before a movement, add them to the method implementation.<br>For example, to turn on the machine coolant before milling the pocket, call **INCT_CLData.AddCoolant** with the appropriate parameters in the **BeforeMove** implementation under the condition **MoveType** = **pcmMoveToSafeLevel**. |
| **OnMove** | The method is executed immediately before each tool movement when the cycle path is formed.<br>Input parameters: **MoveType** (**TNCPocketCycleMoveType**) - movement type, see the description above;<br>Input and output parameters: **Point** (**TNC3DPoint**) - coordinates of the movement point; **Feed** (**TNCFeedType**) - feed type; **Handled** (boolean) - flag of whether the movement has been made inside the implementation (True - the movement has been made, False - it has not).<br>If **Handled** is True after the **OnMove** call, the movement has been made inside the **OnMove** implementation, and the generator does not add a movement command to the tool path.<br>If **Handled** is False after the **OnMove** call, the generator considers that the movement has not been made and adds to the tool path a command to move to the point **Point** with the feed type **Feed**. | To override the movement point or the feed, or to skip the movement.<br>For example, to switch to rapid traverse when returning to the initial level after milling, in the **OnMove** implementation set the returned **Feed** parameter to **ffRapid** under the condition **MoveType** = **pcmMoveToTopLevel** (for the feed type, see **[OutStandardFeed](../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md)**).<br>To move the tool to a point other than the one calculated by the cycle, change the **Point** parameter returned by **OnMove**.<br>If the movement to the calculated point is not needed, set the **Handled** parameter to True inside the **OnMove** implementation. |
| **AfterMove** | The method is executed after each tool movement when the cycle path is formed, even if the movement has been canceled in **OnMove**.<br>Input parameters: **MoveType** (**TNCPocketCycleMoveType**) - movement type, see the description above; **Point** (**TNC3DPoint**) - coordinates of the movement point; **Feed** (**TNCFeedType**) - feed type.<br>No output parameters. | If some commands must be added after a movement, add them to the method implementation. |
