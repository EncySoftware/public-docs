# The cycle statement FOR

This statement repeats one or multiple operators a defined number of repetitions.

**Syntax**

```
FOR <numerical cycle control variable> = <math expression> TO <math expression> {STEP <number> | <number variable>} DO <operator>
```

**Description**

This statement provides repetitive performing of some statement and simultaneous incrementing the cycle variable, until the value is greater than specified limit.

The keyword of this operator is the **FOR** word. Then follows the construction, which is similar to assignment:

```
<Numerical cycle control variable> = <Math expression>
```

In reality, they are much similar, because this construction assigns the initial value, defined by **Math expression**, to **Numerical cycle control variable**.

After the **TO** reserved word the math expression follows, which defines the upper limit. When the **Numerical cycle control variable** achieves this limit, the cycle statement terminates, and next program statement will be performed. Any math expression can be specified as an upper limit for cycle.

Unnecessary part of this statement, containing reserved word **STEP** and following number or numerical variable, defines the incrementing step for the cycle variable. As default, the step is 1. The expression can not be the step.

The statement, which must be performed cyclically, is specified after the **DO** keyword. All other cycle parameters serve for organization of cyclical performing of this statement.

When the loop body contains several operators, they should be placed between the keywords BEGIN and END.

**Examples**

```
! Example 1.
! Simple example of usage the cycle statement.
FOR as = 3 TO 10 DO PRINT as:0," ",as^2:0
! Example 2.
! Using embedded cycle statements
FOR i = 0 TO 0.9 STEP 0.5 DO
FOR j = -1 TO 0 STEP 0.2 DO
PRINT " i = ",i:1," j = ",j:1
```

**See also**

[The cycle statement **REPEAT**](../cycle-statement-repeat.md)

[The cycle statement **WHILE**](../cycle-statement-while.md)

[Statement **BREAK**](statement-break.md)

[Statement **CONTINUE**](statement-continue.md)
