# The statement of the procedure start PROC

The operator is intended to declare the start and the parameters list of the subprogram in the CLDATA command processing procedure.

**Format**

```
PROC <procedure name> {(<list of formal parameters>)}
```

**Description**

After the **PROC** keyword, the **procedure name** is declared. The **procedure name** – identifier it is not coincide with the postprocessor generator keywords and variable names. This name is for the procedure indentification for calling, so the names of all procedures must be unique. After the **procedure name** follows the optional **list of formal parameters**. It is the sequence of the numerical and string variables and arrays. If the number of parameters is more then one then comma must divide it.

As distinct from [SUB](statement-of-the-subprogram-start-sub.md) statement the variables defined in the **list of formal parameters** is not initialized i.e. it is necessary to assign some values to the variables before the including to the list.

The variables declared in the **list of formal parameters** will contain the values that are defined in the [CALL](statement-to-call-a-subprogram-call.md) statement. So these variables is defined in a program and can be used everywhere.

The **PROC** statement is looks like [SUB](statement-of-the-subprogram-start-sub.md) statement. The main difference is that the procedure has the access to all variables and arrays of program of subprogram in the body of which it is located.

It is possible to place the declared procedure in any place of a program.

**See also**

[The **RETURN** from a procedure statement](return-from-a-procedure-statement.md)
