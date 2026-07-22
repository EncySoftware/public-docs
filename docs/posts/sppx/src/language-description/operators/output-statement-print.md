# The output statement PRINT

This statement is designed to write the results on the display (in the debug window) during the trial NC-program generation. If the run-time postprocessor (`Inp.exe`) generates the NC-program, it ignores this operator.

**Format**

```
PRINT <Math expression> | <String expression>
{, <Math expression> | <String expression>}
{ > | >> output file name}
```

**Description**

The keyword of this statement is the **PRINT** word. The list, which contains one or more math or string expressions, follows the keyword. The number of expressions is not limited in this statement, if there are more than one expressions in the statement, they must be separated by commas.

The value of expressions will be consecutively evaluated and printed in the **Debuging information** tab.

To save the output information on disk, you must redirect the output to a file. To do this, it is enough to specify the symbol **>** or **>>** after the last of the output expressions and the name of the output file.

The use of the symbols **>** and **>>** indicates the mode for outputting information to a file:

- symbol **>** - start output from the first record, having previously cleared the output file. If a file with the same name already exists, the old contents of the file are lost;
- symbol **>>** – add output parameters to the end of the file. If there is no file with that name, it will be created and the contents of the current output statement will be the first entry in the new file.

**Examples**

```
PRINT "Runs the subprogram ABSMOVE"
PRINT CLD[1]-XT, " increase by X"
PRINT AA, " ", CLD[1]
```

```
PRINT CLD[1] > "c:\my_folder\log.txt" ! Output to file
```

**See also**

[The input statement **INPUT**](input-statement-input/readme-input-statement-input.md)
