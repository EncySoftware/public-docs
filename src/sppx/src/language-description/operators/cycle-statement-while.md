# The cycle statement WHILE

The structure `WHILE...DO` is used for the repeating execution of the some operators named as cycle body while some condition is true.

**Format**

```
WHILE <conditional expression> DO <statement>
```

The structure works the following way. At the first, the **conditional expression** is calculated. If the result is true then the cycle body is performed and after that the conditional expression is calculated again. So the repeating is continues until the expression returns false. After that the cycle execution is finished and the next statement after structure `WHILE...DO` is executed.

Because the condition checking is performed before the execution of the cycle body then if the conditional expression is false in advance then the cycle body is never performed. It is the main difference between the structures `WHILE...DO` and [REPEAT...UNTIL](cycle-statement-repeat.md). On the other hand the condition must return true one time else the loop will be performed infinitely.

**See also**

[The cycle statement **FOR**](cycle-statement-for/readme-cycle-statement-for.md)

[The cycle statement **REPEAT**](cycle-statement-repeat.md)

[Statement **BREAK**](cycle-statement-for/statement-break.md)

[Statement **CONTINUE**](cycle-statement-for/statement-continue.md)
