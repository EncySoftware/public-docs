# Conditional statement IF

This statement is designed to perform one of statements, included by it, in depending of some condition.

**Format**

```
IF <Conditional expression> then <Statement 1>
{else <Statement 2>}
```

**Description**

This operator allows changing the next steps of program dependently of some conditions.

The keyword of this statement is the **IF** word. Then follows the conditional expression, when it is true, the statement, following the **THEN** keyword, is performed. If the conditional expression is false, then the statement, following the keyword **ELSE**, is performed. **ELSE** – is unnecessary part of this statement. If it is absent and the value of conditional expression is false, then the performing of **IF** statement terminates and next statement of a program will be performed.

**Conditional expression** may be a single **Simple conditional expression** or a sequence of the **Simple conditional expressions**, linked by logical **OR** and **AND** operations, i.e.:

```
<Simple conditional expression> {{AND <Simple conditional expression>} |
{OR <Simple conditional expression>}}
```

**Conditional expression** is true, if all **Simple conditional expressions**, linked by **AND** operation are true or if at least one of **Simple conditional expressions**, linked by **OR** operation is true.

The **Simple conditional expressions** – is a two math or string expressions, linked by comparison operations, i.e.:

```
<Math expression> <Comparison operator> <Math expression>
```

or

```
<String expression> <Comparison operation> <String expression>
```

The expressions around the **Comparison operation** must be same type; otherwise, you will obtain the error message "Incompatible types" during the compilation.

The **Comparison operation** is one of following operations:

- `=` – the values of left and right operations are **EQUAL**;
- `>` – the value of left expression is **GREATER** than value of right expression;
- `<` – the value of left expression is **LESS** than value of right expression;
- `#` or `<>` – the values expressions are **DIFFERENT**;
- `>=` or `=>` – the value of left expression is **EQUAL OR GREATER** than value of right expression;
- `<=` or `=<` – the value of left expression is **EQUAL OR LESS** than value of right expression.

It is necessary to pay attention to the comparison of string expressions. The comparison of two strings is performed character-by-character from left to right respecting their ASCII-codes. Keep in mind that capital letters are less than small letters.

If the lengths of the strings are different, but the longest string includes the shortest entirely, then the longest string is greater. The strings are equal, if they contain the same symbols and have the same length.

When the conditional statement is performed, the values of math and string expressions in the **Simple conditional expressions** are evaluated first, then the operations of comparison are performed, and then the **AND** and **OR** operations are performed without priority. After that, the **THEN** or **ELSE** statement will be performed, depending the result of entire **Conditional expression**.

**Examples**

```
! Sample 1.
! The example, which uses the conditional statement
IF kadr <224 THEN PRINT "This is a short program "
ELSE PRINT "You are the monster in programming"
! Sample 2.
! This example shows how to use embedded conditional statements
IF POS(" ",str$) = 2 THEN
b$ = "The first char in string is a letter"
ELSE
IF POS(" ",str$) <= 4 THEN
b$ = "First in string is a word, it is length is 4 symbols"
ELSE
b$ = "First in string is a word greater than 5 symbols length"
```

**See also**

[Statement of the multiconditional execution **CASE**](statement-of-the-multiconditional-execution-case.md)
