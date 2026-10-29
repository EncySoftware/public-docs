# Managing NC-program analysis

**INCT_Analyzer** - a CAM system interface that provides access to the settings of the NC program text analysis. The analyzer settings affect the [algorithm of determining registers and values in the NC program text](../../translation-and-interpretation/algorithm-for-determining-register-and-values-in-g-code-block/algorithm-for-determining-register-and-values-in-g-code-block.md).

**Description of the interface methods:**

<table>
<thead>
<tr><th>Method</th><th>Method description</th><th>Description of use</th></tr>
</thead>
<tbody>
<tr><td><strong>BeginUpdate</strong></td><td><p>Signals the start of an <strong>INCT_Analyzer</strong> update.</p><p>No input and output parameters.</p></td><td rowspan="2"><p>Call <strong>BeginUpdate</strong> to start changing the <strong>INCT_Analyzer</strong> settings. When the changes are finished, call <strong>EndUpdate</strong> to apply all of them.</p><p>Each <strong>BeginUpdate</strong> call must be followed by a corresponding <strong>EndUpdate</strong> call.</p><p>If only one <strong>INCT_Analyzer</strong> setting is changed at a time, <strong>BeginUpdate</strong> and <strong>EndUpdate</strong> are optional.</p></td></tr>
<tr><td><strong>EndUpdate</strong></td><td><p>Signals the end of the update. All changes made between the start and the end of the <strong>INCT_Analyzer</strong> update are applied.</p><p>No input and output parameters.</p></td></tr>
<tr><td><strong>Get_CanUseEqualToAssignRegister</strong></td><td><p>The function returns the value of the setting 'The = character can be used to set a register value' (boolean). True: the NC program text analyzer uses the '=' character to set a register value. False: when a register value is determined, the '=' character is considered an invalid token.</p><p>No input parameters.</p></td><td rowspan="2"><p>If the setting is on (True), the following combination of registers and values in the NC program text is considered correct:</p><p>X=10.0 Y10.0 Z-1 A=-1 B+3.5 C=-3.5</p><p>If the setting is off (False), the following way of setting register values is considered correct:</p><p>Y10.0 Z-1 B+3.5</p></td></tr>
<tr><td><strong>Set_CanUseEqualToAssignRegister</strong></td><td><p>The method sets the value of the setting 'The = character can be used to set a register value'.</p><p>Input parameter: <strong>Value</strong> (boolean), see the parameter description in <strong>Get_CanUseEqualToAssignRegister</strong>.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_RegistersContainSpaces</strong></td><td><p><strong>Deprecated</strong></p><p>The function returns the value of the setting 'A register can contain spaces' (boolean). True: when a register is determined, the NC program text analyzer takes into account that a register address can contain spaces. False: when a register is determined, a space is considered only a token separator.</p><p>No input parameters.</p></td><td rowspan="2"><p><strong>Deprecated</strong></p><p>If the setting is on (True), the following combination of registers and values in the NC program text is considered correct:</p><p>TOOL CALL 1</p><p>CYCL CALL</p><p>provided that the registers with the addresses 'TOOL CALL' and 'CYCL CALL' are defined in the list. The register with the address 'TOOL CALL' gets the value 1. The register with the address 'CYCL CALL' must be defined as a register without a value (<strong><a href="../../interfaces/interpreter-interfaces/list-of-interpreter-registers/list-of-interpreter-registers.md">vatOnlyAddr</a></strong>).</p><p>If the setting is off, the analyzer considers 'TOOL', 'CALL', 'CYCL', 'CALL' separate tokens.</p></td></tr>
<tr><td><strong>Set_RegistersContainSpaces</strong></td><td><p><strong>Deprecated</strong></p><p>The method sets the value of the setting 'A register can contain spaces'.</p><p>Input parameter: <strong>Value</strong> (boolean), see the parameter description in <strong>Get_RegistersContainSpaces</strong>.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_RegistersCanEndWithPlusOrMinus</strong></td><td><p><strong>Deprecated</strong></p><p>The function returns the value of the setting 'A register can end with a plus or minus' (boolean). True: when a register is determined, the NC program text analyzer takes into account that a register address can end with a plus or minus character. False: when a register is determined, the plus and minus characters are considered separate tokens that are not part of the register address.</p><p>No input parameters.</p></td><td rowspan="2"><p><strong>Deprecated</strong></p><p>If the setting is on (True), the following combination of registers and values in the NC program text:</p><p>DL+0 DR+0</p><p>is recognized as the register 'DL+' with the value 0 and the register 'DR+' with the value 0, provided that the registers with the addresses 'DL+', 'DR+' are defined in the list of addresses.</p><p>If the setting is off, the analyzer considers 'DL', '+0', 'DR', '+0' separate tokens.</p></td></tr>
<tr><td><strong>Set_RegistersCanEndWithPlusOrMinus</strong></td><td><p><strong>Deprecated</strong></p><p>The method sets the value of the setting 'A register can end with a plus or minus'.</p><p>Input parameter: <strong>Value</strong> (boolean), see the parameter description in <strong>Get_RegistersCanEndWithPlusOrMinus</strong>.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_RegistersCanEndWithNumber</strong></td><td><p><strong>Deprecated</strong></p><p>The function returns the value of the setting 'A register can end with a number' (boolean). True: when a register is determined, the NC program text analyzer takes into account that a register address can end with an integer. False: when a register is determined, the number characters are considered separate tokens that are not part of the register address.</p><p>No input parameters.</p></td><td rowspan="2"><p><strong>Deprecated</strong></p><p>If the setting is on (True), the following combination of registers and values in the NC program text:</p><p>DR2+0 R0</p><p>is recognized as the register 'DR2' with the value 0 and the register 'R0' without a value, provided that the registers with the addresses 'DR2', 'R0' are defined in the list of addresses. The register with the address 'R0' must be defined as a register without a value (<strong><a href="../../interfaces/interpreter-interfaces/list-of-interpreter-registers/list-of-interpreter-registers.md">vatOnlyAddr</a></strong>).</p><p>If the setting is off, the analyzer considers 'DR', '2', '+0', 'R', '0' separate tokens.</p></td></tr>
<tr><td><strong>Set_RegistersCanEndWithNumber</strong></td><td><p><strong>Deprecated</strong></p><p>The method sets the value of the setting 'A register can end with a number'.</p><p>Input parameter: <strong>Value</strong> (boolean), see the parameter description in <strong>Get_RegistersCanEndWithNumber</strong>.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_LineBeginWithNumber</strong></td><td><p>The function returns the value of the setting 'An NC program line can begin with a number' (boolean). True: when an NC program text line is analyzed, the first token, if it is a number, is ignored. False: when an NC program text line is analyzed, the first number is considered a token.</p><p>No input parameters.</p></td><td rowspan="2">If the setting is on (True), the first token of an NC program line, if it is a number, is skipped.</td></tr>
<tr><td><strong>Set_LineBeginWithNumber</strong></td><td><p>The method sets the value of the setting 'An NC program line can begin with a number'.</p><p>Input parameter: <strong>Value</strong> (boolean), see the parameter description in <strong>Get_LineBeginWithNumber</strong>.</p><p>No output parameters.</p></td></tr>
<tr><td><strong>Get_Comments</strong></td><td><p>The function returns the interface for managing the settings of determining comments in the NC program text (<strong>INCT_Comments</strong> interface).</p><p>No input parameters.</p></td><td><p>If the following combinations of opening and closing characters are added to the comment settings:</p><p>'!', ''</p><p>'(*', '*)'</p><p>then the NC program text lines</p><p>! X10 Y20 Z30.5 skip A+1</p><p>(* test G01 X100 F100 *)</p><p>are considered comments (skipped).</p></td></tr>
<tr><td><strong>Get_Brackets</strong></td><td><p>The function returns the interface for managing the settings of determining brackets in the NC program text (<strong>INCT_Brackets</strong> interface).</p><p>No input parameters.</p></td><td>Added for determining brackets in expressions. Currently the settings set through the interface are not used for the NC program text analysis.</td></tr>
<tr><td><strong>Get_Quotes</strong></td><td><p>The function returns the interface for managing the settings of determining strings in the NC program text (<strong>INCT_Quotes</strong> interface).</p><p>No input parameters.</p></td><td><p>If the character '&quot;' is added to the string settings and the setting 'The = character can be used to set a register value' is on, then the NC program text line</p><p>T=&quot;1&quot;</p><p>is recognized by the analyzer as the register T with the value 1. The string value &quot;1&quot; is converted to the number 1.</p></td></tr>
<tr><td><strong>Get_UnionLineChars</strong></td><td><p>The function returns the interface for managing the settings of joining the NC program text lines (<strong>INCT_UnionLineChars</strong> interface).</p><p>No input parameters.</p></td><td><p>If the character &quot;~&quot; is added to the line joining settings, then the lines</p><p>1 CYCL DEF 200 ~<br>Q200=+1~<br>Q201=-30.645~<br>Q206=+200~</p><p>are translated and interpreted as one line:</p><p>1 CYCL DEF 200 Q200=+1 Q201=-30.645 Q206=+200</p></td></tr>
<tr><td><strong>Get_EndOfLineChars</strong></td><td><p>The function returns the interface for managing the settings of splitting the NC program text into lines (<strong>INCT_EndOfLineChars</strong> interface).</p><p>No input parameters.</p></td><td><p>If the character &quot;;&quot; is added to the line splitting settings, then the NC program lines</p><p>MoveL [10,10,10,10];MoveL [20,20,20,20];</p><p>MoveC [10,10,10,10],</p><p>[10,10,10,10];</p><p>are passed to the interpreter for translation according to the specified separator:</p><p>MoveL [10,10,10,10];</p><p>MoveL [20,20,20,20];</p><p>MoveC [10,10,10,10], [10,10,10,10];</p></td></tr>
<tr><td><strong>Get_ExcludeEOLChars</strong></td><td><p>The function returns the value of the setting 'Exclude end-of-line characters from the NC program text' (boolean). True: when lines are split according to the settings set in <strong>INCT_EndOfLineChars</strong>, the end-of-line character is excluded from the text and is not passed to the interpreter. False: the end-of-line character is left in the text and passed to the interpreter.</p><p>No input parameters.</p></td><td rowspan="2"><p>If the setting is on (True) and the specified separator is ';' (<strong>INCT_EndOfLineChars</strong>), then the following NC program text:</p><p>MoveL [10,10,10,10];MoveL [20,20,20,20];</p><p>MoveC [10,10,10,10],</p><p>[10,10,10,10];</p><p>is passed to the interpreter as follows:</p><p>MoveL [10,10,10,10]</p><p>MoveL [20,20,20,20]</p><p>MoveC [10,10,10,10], [10,10,10,10]</p><p>that is, the line separator character is excluded. If the setting is off, the text is passed as follows:</p><p>MoveL [10,10,10,10]<strong>;</strong></p><p>MoveL [20,20,20,20]<strong>;</strong></p><p>MoveC [10,10,10,10], [10,10,10,10]<strong>;</strong></p></td></tr>
<tr><td><strong>Set_ExcludeEOLChars</strong></td><td><p>The method sets the value of the setting 'Exclude end-of-line characters from the NC program text'.</p><p>Input parameter: <strong>Value</strong> (boolean), see the parameter description in <strong>Get_ExcludeEOLChars</strong>.</p><p>No output parameters.</p></td></tr>
</tbody>
</table>

**INCT_Analyzer2** - a CAM system interface that provides access to the settings of the NC program text analysis.

**Description of the interface methods:**

<table>
<thead>
<tr><th>Method</th><th>Method description</th><th>Description of use</th></tr>
</thead>
<tbody>
<tr><td><strong>Get_RegistersCaseSensitivity</strong></td><td><p>The function returns the value of the setting &quot;Case sensitivity&quot;.</p><p>True: when the NC program text is analyzed, the register addresses are determined case-sensitively (registers with the addresses &quot;A&quot; and &quot;a&quot; are different).</p><p>False: when the NC program text is analyzed, the register addresses are determined case-insensitively (registers with the addresses &quot;A&quot; and &quot;a&quot; are the same).</p><p>No input parameters.</p></td><td rowspan="2"><p>If the &quot;Case sensitivity&quot; setting is on (True) and all registers of the interpreter are set in capital letters, the registers written in lowercase letters are skipped. For the following NC program text:</p><p>G0 X0 Y0 Z0<br>x10 y10 z10</p><p>all registers of the first line are recognized and added to the list of objects for interpretation <strong><a href="../basic-interfaces/list-of-objects-to-interpret/list-of-objects-to-interpret.md">INCT_BlockExecArray</a></strong>. All registers of the second line are skipped (not recognized).</p></td></tr>
<tr><td><strong>Set_RegistersCaseSensitivity</strong></td><td><p>The method sets the value of the setting &quot;Case sensitivity&quot;.</p><p>Input parameter: <strong>Value</strong> (boolean), see the parameter description in <strong>Get_RegistersCaseSensitivity</strong>.</p><p>No output parameters.</p></td></tr>
</tbody>
</table>

**INCT_Comments** - a CAM system interface that implements the list of settings for managing comments. The settings consist of pairs of strings: an opening character set and a closing character set. When an NC program block is analyzed, the characters between any pair of opening and closing character sets are considered a comment and skipped. The closing character set can be an empty string; in this case, the rest of the line after the opening character set is considered a comment.

**Description of the interface methods:**

| Method | Method description | Description of use |
| --- | --- | --- |
| **Add** | The function adds a pair of settings to the list and returns the index of the added pair in the list (integer).<br>Input parameters: **Open** (string) - opening comment character set; **Close** (string) - closing comment character set. | To add comment settings when setting up the analyzer. |
| **Get** | The method returns the comment settings by index.<br>Input parameter: **Idx** (integer) - index of the pair of settings.<br>Output parameters: **Open** (string) - opening comment character set; **Close** (string) - closing comment character set. | To get the settings. |
| **Delete** | The method deletes a pair of settings by the specified parameter.<br>Input parameter: **Idx** (integer) - index of the pair of settings. | To remove comment settings when reconfiguring the analyzer. |
| **Get_Count** | The function returns the number of pairs of settings (integer). | To get the number of settings. |

**INCT_Brackets** - a CAM system interface that implements the list of settings for determining brackets in the NC program text. The settings consist of pairs of characters: opening and closing. Currently the settings set through the interface are not used for the NC program text analysis; they are added for future use.

**Description of the interface methods:**

| Method | Method description | Description of use |
| --- | --- | --- |
| **Add** | The function adds a pair of settings to the list and returns the index of the added pair in the list (integer).<br>Input parameters: **Open** (character) - opening bracket character; **Close** (character) - closing bracket character. | To add bracket settings when setting up the analyzer. |
| **Get** | The method returns the bracket settings by index.<br>Input parameter: **Idx** (integer) - index of the pair of settings.<br>Output parameters: **Open** (character) - opening bracket character; **Close** (character) - closing bracket character. | To get the settings. |
| **Delete** | The method deletes a pair of settings by the specified parameter.<br>Input parameter: **Idx** (integer) - index of the pair of settings. | To remove bracket settings when reconfiguring the analyzer. |
| **Get_Count** | The function returns the number of pairs of settings (integer). | To get the number of settings. |

**INCT_Quotes** - a CAM system interface that implements the list of settings for determining strings. Each setting consists of the character with which a string value begins and ends. When an NC program block is analyzed, the characters between any pair of string characters are considered a string value.

**Description of the interface methods:**

| Method | Method description | Description of use |
| --- | --- | --- |
| **Add** | The function adds a setting to the list and returns the index of the added setting in the list (integer).<br>Input parameters: **Sym** (character) - character with which a string value begins and ends. | To add string value settings when setting up the analyzer. |
| **Get** | The method returns a setting by index.<br>Input parameter: **Idx** (integer) - setting index.<br>Output parameters: **Sym** (character) - character with which a string value begins and ends. | To get the settings. |
| **Delete** | The method deletes a setting by the specified parameter.<br>Input parameter: **Idx** (integer) - setting index. | To remove string value settings when reconfiguring the analyzer. |
| **Get_Count** | The function returns the number of settings (integer). | To get the number of settings. |

**INCT_UnionLineChars** - a CAM system interface that implements the list of settings for joining the NC program text lines. Each setting consists of a line joining character. If an NC program block ends with any character from the list, the line is joined with the next one without the joining character.

**Description of the interface methods:**

| Method | Method description | Description of use |
| --- | --- | --- |
| **Add** | The function adds a setting to the list and returns the index of the added setting in the list (integer).<br>Input parameters: **Sym** (character) - line joining character. | To add line joining character settings when setting up the analyzer. |
| **Get** | The method returns a setting by index.<br>Input parameter: **Idx** (integer) - setting index.<br>Output parameters: **Sym** (character) - line joining character. | To get the settings. |
| **Delete** | The method deletes a setting by the specified parameter.<br>Input parameter: **Idx** (integer) - setting index. | To remove line joining character settings when reconfiguring the analyzer. |
| **Get_Count** | The function returns the number of settings (integer). | To get the number of settings. |

**INCT_EndOfLineChars** - a CAM system interface that implements the list of settings for splitting the NC program text into lines. Each setting consists of a separator string. The NC program text is passed to the interpreter line by line, where each line is the content between separators.

**Description of the interface methods:**

| Method | Method description | Description of use |
| --- | --- | --- |
| **Add** | The function adds a setting to the list and returns the index of the added setting in the list (integer).<br>Input parameters: **Str** (string) - separator. | To add line separator settings when setting up the analyzer. |
| **Get** | The method returns a setting by index.<br>Input parameter: **Idx** (integer) - setting index.<br>Output parameters: **Str** (string) - separator. | To get the settings. |
| **Delete** | The method deletes a setting by the specified parameter.<br>Input parameter: **Idx** (integer) - setting index. | To remove line separator settings when reconfiguring the analyzer. |
| **Get_Count** | The function returns the number of settings (integer). | To get the number of settings. |
