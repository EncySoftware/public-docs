# The block forming statement FORMBLOCK

This statement forms the block of NC-program according specified format, order and registers format. The block is formed in [OutStr$](../basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md) variable without the output in the file of NC-program.

**Format**

```
FORMBLOCK
```

**Description**

The formation process is similar to the [OUTBLOCK](block-output-statement-outblock.md) statement, but the [OutStr$](../basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md) variable won't be written in the block of NC-program. It's possible, then, to work with this variable as a string variable and put it into NC-file by [OUTPUT](statement-of-direct-output-into-the-block-output.md) statement.

**See also**

[Predefined functions](../basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md)

[The block output statement **OUTBLOCK**](block-output-statement-outblock.md)

[Statement of direct output into the block **OUTPUT**](statement-of-direct-output-into-the-block-output.md)
