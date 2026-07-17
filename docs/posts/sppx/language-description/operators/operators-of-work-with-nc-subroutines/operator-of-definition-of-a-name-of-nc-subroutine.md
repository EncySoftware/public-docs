# The operator of definition of a name of NC-subroutine NCSUB.NAME



Returns a text name of the NC-subroutine, and also allows to appropriate to a text name of the NC-subroutine any text value.

**Format**

```
S$ = NCSUB.NAME(<NC-subroutine Number>)
```

or

```
NCSUB.NAME(<NC-subroutine Number>) = S$
```

**Description**

- `NC-subroutine number` – the unique identifier of the NC-subroutine.
- `S$` – any text variable. In the second case also can be set the text constant or any expression which is returning a text.

The operator can be used by a similarly as text variable in expressions and functions processing strings.

For output in the operating program of the text identifier of the subroutine in the necessary format it is necessary to use the operator of definition of a name of the NC-subroutine.

Note: Before the first assignment of a name of the NC-subroutine by operator `NCSUB.NAME`, the name already matters by default which is taken from a text of the comment (technological command a [COMMENT](../../../../cldata/commands/comment.md)), located before a technological command of the beginning of NC-subroutine [PPFUN STARTSUB(50)](../../../../cldata/commands/ppfun/startsub.md) corresponding NC-subroutines.

**Example**

```
St$: text
n1: Integer
St$ = "Example"
n1 = 3
! Assignment of a name of value "Example3":
NCSub.Name(n1) = St$ + Str(n1)
! A output in the operating program of a text "oExample3":
Output "o"+NCSub.Name(n1)
```

**See also**

[Operators of work with NC-subroutines](readme-operators-of-work-with-nc-subroutines.md)
