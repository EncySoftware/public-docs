# Protection interface

If the container with the interpreter contains the file **interpreter_library_name.dat** (hereinafter, the secret data file), the **INCT_Connect** interface is additionally passed to such an interpreter during initialization.

**INCT_Connect** - the interface that gives the interpreter access to the data from the secret data file. The data file is not extracted from the container and therefore can be read only through the interface passed to the interpreter.

The interpreter must be designed so that it works only after the check of the data received through the **INCT_Connect** interface has been passed. The places of the checks, their number and the algorithm are chosen by the developer.

**Description of the interface methods:**

<table>
<thead>
<tr><th>Method</th><th>Method description</th><th>Description of use</th></tr>
</thead>
<tbody>
<tr><td><strong>Get_Count<br></strong></td><td>The function returns the number of bytes in the secret data file (integer).</td><td rowspan="3"><p>Using these methods, check the data placed in the container by the interpreter developer against the data passed to the interpreter by the CAM system (they must match).</p><p>Suppose the developer has placed in the container the file sample.dat (the interpreter library is called sample.dll) 5 bytes in size with the following data: 12345</p><p>The <strong>Get_Count</strong> function returns 5.</p><p><strong>Get_Data</strong>(0) returns 1, <strong>Get_Data</strong>(2) returns 3, <strong>Get_Data</strong>(4) returns 5.</p><p>The <strong>Get_SCData</strong> method returns in the <strong>Data</strong> parameter a pointer to the memory containing the data 12345.</p></td></tr>
<tr><td><strong>Get_Data<br></strong></td><td><p>The function returns the byte of the secret data file with the number given in the input parameter.</p><p>Input parameter: <strong>Index</strong> (integer) - the number of the returned byte. Bytes are numbered from 0.</p><p>Output parameter: the byte of the secret data file with the number given in the <strong>Index</strong> parameter.</p></td></tr>
<tr><td><strong>Get_SCData<br></strong></td><td>The method returns the pointer to the secret data from the file. Output parameter: <strong>Data</strong> (pointer) - the pointer to the secret data.</td></tr>
</tbody>
</table>
