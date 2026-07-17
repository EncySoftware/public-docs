# Statement CONTINUE

**Syntax**

```
CONTINUE
```

**Description**

The **CONTINUE** statement interrupts the execution of the current iteration of a loop. In the case of a precondition loop ([FOR](readme-cycle-statement-for.md) or [WHILE](../cycle-statement-while.md)), control is transferred to the beginning of the loop, where the condition is checked (for the [FOR](readme-cycle-statement-for.md) loop, the new value of the loop variable is calculated before that). If the condition is true, the loop continues. In the case of a postcondition loop ([REPEAT](../cycle-statement-repeat.md)), control is transferred to the end of the loop, where the condition is checked. If the condition is false, the loop continues.

The use of the **CONTINUE** statement is only allowed within the body of a loop; in all other cases, an error message is issued.

**See also**

[The cycle statement **FOR**](readme-cycle-statement-for.md)

[The cycle statement **REPEAT**](../cycle-statement-repeat.md)

[The cycle statement **WHILE**](../cycle-statement-while.md)

[Statement **BREAK**](statement-break.md)
