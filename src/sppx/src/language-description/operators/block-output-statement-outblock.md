# The block output statement OUTBLOCK

This statement forms the content of a block, corresponding to specified variable format, order, register format, and outputs the block into NC-program.

**Format**

```
OUTBLOCK {<FileName$>}
```

**Description**

The block of NC-program is formed according following algorithm:

The registers are checked from the first. If the previous and current values of register are different, then the register will be written in the block, and its current value will be assigned to its previous value; otherwise the register won't be written in the block.

When the register is written in the block, its identifier will be written first, then it's value, multiplied by the scale. The number will be written in the block corresponding to specified format. After that, the processing program will be called, if it is defined. The block is formed in the variable [OutStr$](../basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), and will be written in the program as separate string after the formation is done.

Use optional `FileName$` parameter to specify the file where the system outputs the NC-block. If the parameter is omitted then the NC-block is output into the current file. If "*" is specified as a file name then the NC-block would be output into the main file, also the current file will be changed. If `FileName$` specifies the name of a file then corresponding tab will be created and the current file would be changed accordingly.

**See also**

[Predefined functions](../basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md)

[The block forming statement **FORMBLOCK**](block-forming-statement-formblock.md)

[Statement of direct output into the block **OUTPUT**](statement-of-direct-output-into-the-block-output.md)
