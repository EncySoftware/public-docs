# Register List

**INCT_SysState** - the interface of the machine-controller system state. Currently the interface provides work with the [formed list of registers](../../../interpreter-loading-and-initialization/interpreter-loading-and-initialization.md) (taking into account the settings file, the program library and the interpreter parents). To distinguish the formed list of registers from the original registers of the interpreter, the settings file and the parent interpreters, the formed list is called the **base list of registers**.

**Description of the interface methods:**

| Method | Method description | Description of use |
| --- | --- | --- |
| **FindFirstRegister** | The function returns the first base register found by the address (**INCT_BaseReg** interface).<br>Input parameter: **Addr** (string) - register address. | The function can be used to find a base register by its address when analyzing the NC program text in the implementation of **INCT_Interpreter.TransLine**. |
| **FindNextRegister** | The function returns the next base register found by the address, starting from **FromIdx** (**INCT_BaseReg** interface).<br>Input parameters: **FromIdx** (integer) - starting index; **Addr** (string) - register address. | The function can be used to find a base register by its address when analyzing the NC program text in the implementation of **INCT_Interpreter.TransLine**. |
| **Get_BR_ByIndex** | The function returns a base register by index (**INCT_BaseReg** interface).<br>Input parameter: **Index** (integer) - register index. | The function can be used to get a base register by index when iterating over the base registers (for example, to get the initial values of the tool position axes linked to the base registers). |
| **Get_BR_ByName** | The function returns a base register by name (**INCT_BaseReg** interface).<br>Input parameter: **Name** (string) - register name. | The function can be used to find a base register by name, to determine the register index in the implementation of **INCT_Interpreter.DefineRegister**. |
| **Get_BR_Count** | The function returns the number of base registers. | The function can be used to get the number of base registers for iterating over them (for example, to get the initial values of the tool position axes linked to the base registers). |

**INCT_SysState2** - the interface of the machine-controller system state.

**Description of the interface methods:**

<table>
<thead>
<tr><th>Method</th><th>Method description</th><th>Description of use</th></tr>
</thead>
<tbody>
<tr><td><strong>Get_SpindleState</strong></td><td>The function returns the spindle state (<strong>INCT_SpindleState</strong> interface).</td><td>The spindle state is used to store and exchange information between the interpreter and its parent(s).</td></tr>
<tr><td><strong>Get_Reg_ByIndex</strong></td><td><p>The function returns a register by index (<strong>INCT_Register</strong> interface).</p><p>Input parameter: <strong>Index</strong> (integer) - register index.</p></td><td rowspan="3">The functions can be used to find a register by name or by iterating over the required parameter, for example, to get the register values <strong>INCT_Register.Values</strong> (not available in <strong>INCT_BaseReg</strong>).</td></tr>
<tr><td><strong>Get_Reg_ByName</strong></td><td><p>The function returns a register by name (<strong>INCT_Register</strong> interface).</p><p>Input parameter: <strong>Name</strong> (string) - register name.</p></td></tr>
<tr><td><strong>Get_Reg_Count</strong></td><td>The function returns the number of base registers.</td></tr>
</tbody>
</table>

**INCT_SpindleState** - the spindle state interface. The spindle state is shared by the interpreter and its parents. It is intended for storing and exchanging the spindle state between the interpreter and its parent(s).

**Description of the interface methods:**

| Method | Method description |
| --- | --- |
| **Get_MaxSpeed** | The function returns the maximum spindle speed (real number). |
| **Set_MaxSpeed** | The method sets the maximum spindle speed.<br>Input parameter: **Value** (real number) - maximum spindle speed. |
| **Get_RPMSpeed** | The function returns the spindle speed (real number) when the constant cutting speed mode is off (**Get_CSS** = False). |
| **Set_RPMSpeed** | The method sets the spindle speed.<br>Input parameter: **Value** (real number) - spindle speed. |
| **Get_CSSSpeed** | The function returns the spindle speed (real number) for the constant cutting speed mode (**Get_CSS** = True). |
| **Set_CSSSpeed** | The method sets the spindle speed for the constant cutting speed mode.<br>Input parameter: **Value** (real number) - spindle speed. |
| **Get_Range** | The function returns the spindle speed range number (integer). |
| **Set_Range** | The method sets the spindle speed range number.<br>Input parameter: **Value** (integer) - spindle speed range number. |
| **Get_Direction** | The function returns the spindle rotation direction (boolean). |
| **Set_Direction** | The method sets the spindle rotation direction.<br>Input parameter: **Value** (boolean) - spindle rotation direction.<br>**True** - clockwise;<br>**False** - counterclockwise. |
| **Get_CSS** | The function returns the constant cutting speed flag of the spindle (boolean). |
| **Set_CSS** | The method sets the constant cutting speed flag of the spindle.<br>Input parameter: **Value** (boolean) - constant cutting speed flag of the spindle.<br>**True** - the constant cutting speed mode is on;<br>**False** - the constant cutting speed mode is off. |
| **Get_MaxRPM** | The function returns the maximum spindle speed for constant cutting speed (real number) (**Get_CSS** = True). |
| **Set_MaxRPM** | The method sets the maximum spindle speed for constant cutting speed.<br>Input parameter: **Value** (real number) - maximum spindle speed for constant cutting speed. |
| **Get_Angle** | The function returns the oriented spindle stop angle (real number). |
| **Set_Angle** | The method sets the oriented spindle stop angle.<br>Input parameter: **Value** (real number) - oriented spindle stop angle. |
| **Get_Command** | The function returns the spindle status (the last executed command) (**TNCSpindleCommand**). |
| **Set_Command** | The method sets the spindle status (the last executed command).<br>Input parameter: **Value** (**TNCSpindleCommand**) - spindle status.<br>**scOn** - on;<br>**scOff** - off;<br>**scOrient** - oriented stop. |
| **Get_IsChanged** | The function returns the flag of a change of any **INCT_SpindleState** parameter except the spindle number since the last spindle command was executed (boolean).<br>**True** - one of the parameters has changed;<br>**False** - the parameters have not changed. |
| **Set_IsChanged** | The method sets the flag of a change of any **INCT_SpindleState** parameter except the spindle number since the last spindle command was executed. Used for interpreter inheritance. The command to turn the spindle on, off or stop it is executed by one of the interpreters, as a rule by the last descendant.<br>Input parameter: **Value** (boolean) - parameter change flag. |
| **Get_Num** | The function returns the spindle number (integer). |
| **Set_Num** | The method sets the spindle number.<br>Input parameter: **Value** (integer) - spindle number. |
| **Get_IsChangedNum** | The function returns the flag of a change of the spindle number (boolean). |
| **Set_IsChangedNum** | The method sets the flag of a change of the spindle number.<br>Input parameter: **Value** (boolean) - spindle number change flag. |

**INCT_BaseReg** - the interface provides work with a base register.

**Description of the interface methods:**

<table>
<thead>
<tr><th>Method</th><th>Method description</th><th>Description of use</th></tr>
</thead>
<tbody>
<tr><td><strong>SetValue</strong></td><td><p>The method sets a new value of the base register. The base register has three fields for storing the value: string, real number and integer. If the new value is not empty, it is written to the string field and converted and written to the integer and real number fields.</p><p>Input parameter: <strong>Value</strong> (string) - new register value.</p></td><td>The method can be used when interpreting lexemes and semantic constructs that affect the register value (for example, functions).</td></tr>
<tr><td><strong>Get_Addr</strong></td><td><p>The function returns the address of the base register (string).</p><p>No input parameters.</p></td><td rowspan="7">The functions can be used to get the corresponding parameters of the base register when the NC program text is initialized, translated or interpreted.</td></tr>
<tr><td><strong>Get_Name</strong></td><td><p>The function returns the name of the base register (string).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Get_Id</strong></td><td><p>The function returns the identifier of the base register in the machine kinematic scheme (string).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Get_Idx</strong></td><td><p>The function returns the index of the base register in the list of registers (integer).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Get_Str</strong></td><td><p>The function returns the string value of the base register (string).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Get_Int</strong></td><td><p>The function returns the numeric value of the base register (integer).</p><p>No input parameters.</p></td></tr>
<tr><td><strong>Get_Flt</strong></td><td><p>The function returns the numeric value of the base register (real number).</p><p>No input parameters.</p></td></tr>
</tbody>
</table>
