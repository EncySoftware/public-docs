# The statement of the subprogram start SUB

It is used for the declaration of the subprogram and the parameters list that is passed to the program then call.

**Format**

```
SUB <subprogram name> {(<the list of the parameters>)}
```

**Description**

The keyword of this operator is the **SUB**. Then follows the sub-program name – literal string without the double quotation marks and after that the optional parameters list in the parentheses.

**The list of the parameters** is the sequence of the numerical and string variables or arrays. If the parameters number is more the one then it is divided by commas.

The variables defined if the list will contain the values defined in the call statement when call. Therefore, these variables are declared in subprogram and can be used everywhere.

**Example**

```
sub GetProgramID(PrgID: Integer)
  ! Extracting numeric identifier from the string NC-program name
  i: Integer
  j: Integer
  k: Integer
  s$: String
  i = 1
  j = 0
  k = 0
  while i<=Len(NCName$) do begin
    s$ = Copy(NCName$, i, 1)
    case Ord(s$) of
      48, 49, 50, 51, 52, 53, 54, 55, 56, 57: begin
        if j<1 then j = i
        if (k<1) or (k=(i-1)) then
          k = i
      end
    end
    i = i + 1
  end
  if (j>0) and (k>0) then begin
    s$ = Copy(NCName$, j, k-j+1)
    PrgID = Num(s$)
  end
subend
```

**See also**

[Statement to call a subprogram `CALL`](statement-to-call-a-subprogram-call.md)

[The statement of the subprogram end `SUBEND`](statement-of-the-subprogram-end-subend.md)
