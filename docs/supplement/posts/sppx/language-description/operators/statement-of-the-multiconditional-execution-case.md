# Statement of the multiconditional execution CASE

The **Case** statement allows checking the value of the expression and depends of the result to execute different code.

**Format**

```
CASE <expression> OF
  <values list 1> : <statement 1>
  ...
  <values list N>: <statement N>
  ELSE <statement M>
END
```

**Description**

The **expression** must be numerical in this construction. Inadmissible to use a string expressions.

The values lists can contain one or more constants, divided by commas. The `:` symbol follows the values list. After that the statement is written that is executed if the expression is equal to one of the list. After the execution of this statement the execution of the **CASE** structure is finished and next statement is executed.

If the expression result is not defined in all lists then the statement after **ELSE** keyword is executed. The **ELSE** part is an optional. If **ELSE** absent and there is no corresponding value in the lists then nothing is executed.

**Example**

```
CASE i OF
  1,2,3,4,5: Str = "Less or equal 5"
  6,7,8,9: Str = "Greater 5"
  ELSE Str = "Error value"
END
```

**See also**

[Conditional statement **IF**](conditional-statement-if.md)
