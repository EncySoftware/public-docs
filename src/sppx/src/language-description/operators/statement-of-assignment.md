# The statement of assignment



This statement is used to assign the value of an expression to the variable. The variables may change their values because of performing of this statement.

**Format**

```
<Numerical variable> = <Math expression>
```

or

```
<String variable> = <String expression>
```

**Description**

The keyword of this operator is the variable name. The symbol `=` follows after the name, and then follows the expression, the value of this expression will be assigned to variable. This operator defines that the expression interpretation result must be stored in the memory cell, identified by specified variable. The variable type must be coincident with the type, returned by the expression, i.e. the value of the math expression must be assigned to the numerical variable, and the value of the string expression – to the string variable.

Note: When the statement is performed, the value of right expression is evaluated first, and then, retrieved value will be assigned to the variable in the left part of statement. This rule allows using the same variable in the left and right parts of statement. In this case, the old value of variable participates in the evaluation of the right expression and, after this; the value of right expression will be assigned to the same variable.

**Examples**

```
! Usage of the statement statement
Zet = 41
Ddel = Mn / Cos(Beta) * Zet
Number = Number + 5
! The generation of string about the NC-machine
System$ = " 2C42 "
! The assignment of CNC-name to the System$
NAME$ = " TEST PROGRAM " + System$
```
