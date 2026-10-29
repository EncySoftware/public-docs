# Equipment parameters

**INCT_Equipment** - a CAM system interface that provides access to some equipment parameters.

**Description of the interface methods:**

<table>
<thead>
<tr><th>Method</th><th>Method description</th><th>Description of use</th></tr>
</thead>
<tbody>
<tr><td><strong>GetAxisIndex</strong></td><td><p>The function returns the index of a machine axis by its address (integer).</p><p>Input parameter: <strong>Addr</strong> (string) - axis address ('X', 'Y', 'Z', etc., as specified in the machine kinematic scheme).</p></td><td>To control the tool movement (with <strong><a href="../forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md">INCT_CLData.AddMotion</a></strong> or <a href="../../toolpath-construction/linear-movements/linear-movements.md"><strong>CreateLinearMotionFormer</strong></a>), the axis indexes returned by <strong>GetAxisIndex</strong> must be specified.</td></tr>
<tr><td><strong>GetAxisIndexByNum</strong></td><td><p>The function returns the index of a main or additional robot axis by its number (integer).</p><p>Input parameters: <strong>AxisNum</strong> (integer) - robot axis number (1-6); <strong>Ext</strong> (boolean): False - robot axis, True - additional axis.</p></td><td>If a robot axis is set by a number (not by an address), <strong>GetAxisIndexByNum</strong> can be used to get the axis index. As a rule, the axes of Motoman robots are obtained this way.</td></tr>
<tr><td><strong>GetXYZindex</strong></td><td><p>The function returns the index of the axis linked to the movement along the X, Y or Z coordinate by the specified parameter (see <a href="../forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md"><strong>INCT_CLData.AddCircle</strong></a>).</p><p>Input parameter: <strong>Ort</strong> (integer):</p><p>1 - <strong>X</strong>; 2 - <strong>Y</strong>; 3 - <strong>Z</strong>.</p></td><td>To get the indexes of the axes linked to X, Y, Z of the current tool.</td></tr>
<tr><td><strong>CurrentLatheToolWidth</strong></td><td>The function returns the width of the current turning tool (real number).</td><td>Used to set the groove width step in <a href="../../toolpath-construction/turning-cycle-grooving/turning-cycle-grooving.md"><strong>INCT_LatheGroovingCycleFormer</strong></a>.</td></tr>
<tr><td><strong>GetSpindlesCount</strong></td><td>The function returns the number of spindles of the current machine (integer).</td><td rowspan="2">To execute commands that control a machine spindle by its number. For example, SPos[<strong>SpindelIndex</strong>] = Value for the Sinumerik controller.</td></tr>
<tr><td><strong>GetAxisIndexBySpindleIndex</strong></td><td><p>The function returns the spindle axis number by the spindle index (integer).</p><p>Input parameter: <strong>SpindleIndex</strong> (integer) - spindle index, possible values from <strong>0</strong> to <strong>GetSpindlesCount - 1</strong>.</p></td></tr>
<tr><td><strong>GetOperationGroup</strong></td><td><p>The function returns the type of the operation in the CAM system (<strong>TNCOperationGroup</strong>).</p><p>The <strong>TNCOperationGroup</strong> type:</p><p><strong>ogUnknown</strong> - unknown;<br><strong>ogMill</strong> - milling;<br><strong>ogLathe</strong> - turning;<br><strong>ogAuxiliary</strong> - auxiliary;<br><strong>ogWireEDM</strong> - wire EDM;<br><strong>ogWelding</strong> - various kinds of welding;<br><strong>ogAdditive</strong> - various additive operations such as cladding;<br><strong>ogWaterJet</strong> - water jet cutting;<br><strong>ogSawing</strong> - sawing.</p></td><td><p><strong>Use it in interpreters only as a last resort.</strong></p><p>The function was added to compensate the position of a turning tool in a turning operation of the CAM system where the offset value cannot be set.</p></td></tr>
</tbody>
</table>

**INCT_Equipment2** - a CAM system interface.

**Description of the interface methods:**

| Method | Method description | Description of use |
| --- | --- | --- |
| **GetCurrentToolRadius** | The function returns the radius of the current tool (real number). | Can be used to calculate the overshoots for CYCLE90 in Sinumerik. |

**INCT_Equipment_Channels** - a CAM system interface that provides access to the machine channels. The interface is requested from the **INCT_Equipment** object; check the result of the request: in earlier versions of the CAM system the object may not support it.

**Description of the interface methods:**

| Method | Method description | Description of use |
| --- | --- | --- |
| **Get_Count** | The function returns the number of machine channels (integer). | |
| **Get_CurrentIndex** | The function returns the index of the channel the current operation belongs to (integer). Numbering starts from 0. | To interpret multichannel programs: allows determining which channel's program the interpreter is interpreting. |
| **Get_Channel** | The function returns the channel interface (**INCT_Channel**) by index.<br>Input parameter: **Index** (integer) - channel index, possible values from **0** to **Get_Count - 1**. | |

**INCT_Channel** - a CAM system interface that provides access to the machine channel parameters.

**Description of the interface methods:**

| Method | Method description | Description of use |
| --- | --- | --- |
| **Get_Name** | The function returns the channel name specified in the machine kinematic scheme (string). | |
