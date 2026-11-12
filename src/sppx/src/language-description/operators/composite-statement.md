# Composite statement BEGIN...END



It is used to unite a group of statements to a one statement. It is the analogue of the parentheses

**Format**

```
BEGIN
<statement 1>
...
<statement N>
END
```

**Description**

The composite statement provides the execution of the included statements step by step. The auxiliary words **BEGIN** and **END** are analogue of the parentheses. The multiplicity level of the composite statements is unlimited. The composite statement can be used everywhere where a simple statement can be used.

**Example**

```
! Simple example of the composite statement
IF var < 3 THEN BEGIN
  ac=12; bb=16
END ELSE BEGIN
  ac=15; bb=60
END ! word END close the statement
```
