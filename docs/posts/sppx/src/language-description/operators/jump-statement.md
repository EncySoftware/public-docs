# JUMP statement



The operator is used to break the order of statements performing.

**Format**

```
JUMP <Label number>
...
<Label number>:
```

**Description**

After the **JUMP** keyword one of labels, which is defined in the current program, must be specified. The symbol `:` must not appear after the label number, unlike the label definition.

The operator, labeled by corresponding label, will be performed after the **JUMP** statement. it is necessary to define corresponding label, otherwise the error message will appear during compilation.

It is not recommended to usually use the **JUMP** statement in the program.

**Example**

```
AFF = 20 ! this statement is performed first
JUMP 2 ! jump to label 2
ABC = 1 ! This statement never be performed
2: ATR = 4 ! this statement is performed second
```
