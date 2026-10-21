# The cycle statement REPEAT

The structure `REPEAT...UNTIL` is used for the repeating execution of the some operators named as cycle body, until some condition will be true.

**Syntax**

```
REPEAT
  <operators of the cycle body>
UNTIL <conditional expression>
```

**Description**

The structure works the following way. The operators of the cycle body is executed, after that is calculated the **conditional expression**. If the conditional expression returns false then the execution of the cycle body is repeated and after that, the conditional expression is calculated again. So the repeating is continues until the conditional expression returns true. After that, the cycle execution is finished and the next statement after structure `REPEAT...UNTIL` is executed.

Because the condition checking is performed after the execution of the cycle body then it is executed one time even if the condition is true in advance. On the other hand, the condition must return true one time else, the loop will be performed infinitely.

**See also**

[The cycle statement **FOR**](cycle-statement-for/readme-cycle-statement-for.md)

[The cycle statement **WHILE**](cycle-statement-while.md)

[Statement **BREAK**](cycle-statement-for/statement-break.md)

[Statement **CONTINUE**](cycle-statement-for/statement-continue.md)
