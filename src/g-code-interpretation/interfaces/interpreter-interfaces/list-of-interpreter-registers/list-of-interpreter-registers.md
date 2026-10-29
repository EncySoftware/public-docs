# List of interpreter registers

**INCT_RegisterList** - the interface returned by the interpreter function **[INCT_Interpreter](../interpreter-interface/interpreter-interface.md).GetRegisters**. The interface provides work with the list of interpreter registers.

**Description of the interface methods:**

<table>
<thead>
<tr><th>Method</th><th>Method description</th><th>Description of use</th></tr>
</thead>
<tbody>
<tr><td><strong>Get_Count<br></strong></td><td><p>The function must return the number of interpreter registers to the CAM system.</p><p>No input parameters.</p></td><td rowspan="2">When forming the common list of registers, the CAM system calls the <strong>Get_Count</strong> function, gets the number of registers, and then calls the <strong>Get_Item</strong> function for each register in turn.</td></tr>
<tr><td><strong>Get_Item<br></strong></td><td><p>The function must return the <strong>INCT_Register</strong> interface (see below) to the CAM system by the register number.</p><p>Input parameter: <strong>Index</strong> (integer) - register number. Numbering starts from 0.</p></td></tr>
</tbody>
</table>

**INCT_Register** - the interface returned by the interpreter function **INCT_RegisterList.Get_Item**. The interface provides work with the parameters of the selected interpreter register.

**Description of the interface methods:**

| Method | Method description | Description of use |
| --- | --- | --- |
| **Get_Addr** | The function must return the register address (string) to the CAM system.<br>No input parameters. | The CAM system uses the register address to find the register in the list of registers. |
| **Get_Id** | The function must return the register identifier in the machine kinematic scheme (string) to the CAM system.<br>No input parameters. | The register identifier in the machine kinematic scheme, if applicable. Otherwise, the string is empty. |
| **Get_Name** | The function must return the register name (string) to the CAM system.<br>No input parameters. | The unique register name. It is used to identify the register in the list unambiguously. |
| **Get_Comment** | The function must return the register comment (string) to the CAM system.<br>No input parameters. | The function is called, but in the current version the value it returns is not used. |
| **Get_Sign** | The function must return the register sign type (the **TNCSign** enumerated type) to the CAM system.<br>**sgnNoSign** - no sign;<br>**sgnMinus** - minus only;<br>**sgnPlusAndMinus** - plus and minus.<br>No input parameters. | The function is called, but in the current version the value it returns is not used. |
| **Get_Point** | The function must return the register point type (the **TNCPoint** enumerated type) to the CAM system.<br>**pntNoPoint** - no point;<br>**pntPoint** - the point may or may not be present;<br>**pntAlwaysPoint** - the point is always present.<br>No input parameters. | The function is called, but in the current version the value it returns is not used. |
| **Get_BeforePoint** | The function must return the number of register digits before the point (integer) to the CAM system.<br>No input parameters. | The function is called, but in the current version the value it returns is not used. |
| **Get_AfterPoint** | The function must return the number of register digits after the point (integer) to the CAM system.<br>No input parameters. | The function is used to check the correctness of arcs, so it is important to set the number of digits after the point correctly. The tool path generator uses this function inside the kernel. |
| **Get_LeadingZeros** | The function must return the flag of leading zeros in the register (boolean) to the CAM system.<br>No input parameters. | The function is called, but in the current version the value it returns is not used. |
| **Get_TrailingZeroes** | The function must return the flag of trailing (non-significant) zeros in the register (boolean) to the CAM system.<br>No input parameters. | The function is called, but in the current version the value it returns is not used. |
| **Get_ValueAvail** | The function must return the register type (the **TNCValueAvailType** enumerated type) to the CAM system.<br>**vatValue** - the register consists of an address and a value;<br>**vatOnlyAddr** - the register consists of an address only;<br>**vatBoth** - the register can consist either of an address only, or of an address and a value.<br>No input parameters. | It is used when [determining the register and its value](../../../translation-and-interpretation/algorithm-for-determining-register-and-values-in-g-code-block/algorithm-for-determining-register-and-values-in-g-code-block.md). |
| **Get_Values** | The function must return the list of register values (the **INCT_RegisterValues** interface) to the CAM system.<br>No input parameters. | **INCT_RegisterValues.Get_Count** - the number of values<br>**INCT_RegisterValues.Get_Value** - the value by index (**Index -** integer)<br>The list of register values is used when [determining the register and its value](../../../translation-and-interpretation/algorithm-for-determining-register-and-values-in-g-code-block/algorithm-for-determining-register-and-values-in-g-code-block.md). |
| **Get_Modal** | The function must return the register modality flag (boolean) to the CAM system.<br>No input parameters. | It is used when copying register values after the current block is interpreted. Modal registers get into **INCT_BlockExecArray** only if the register value has changed in the current block. Non-modal registers always get there if they are present in the current block. |
