# Statement to call a subprogram CALL

The operator is intended to call the subprogram from the CLData command-processing program or other subprogram.

**Format**

```
CALL <program name> {(<the list of the parameters>)}
```

**Description**

The keyword of this operator is the **CALL** word. After this word it is necessary to define the **program name** – string expression or the literal string without the double quotation marks. The expression value is the name of the subprogram.

**The list of the parameters** a comma separated list of actual parameters: variables, literal constants, expressions and arrays. Types of actual parameters must match the types of formal parameters specified in the subprogram declaration. If no parameters are passed to the procedure then there must be no parenthesis.

The **CALL** jumps the execution to the defined subprogram and after the execution makes the return to the program, the call was raised from.

**Example**

```
X = 50; C = 0
CALL ConvertXYtoXC(X, 30, C)
CALL FillCycleParameters
```

**See also**

[The statement of the subprogram start **SUB**](statement-of-the-subprogram-start-sub.md)

[The statement of the subprogram end **SUBEND**](statement-of-the-subprogram-end-subend.md)
