# The processing program start operator PROGRAM



Each processing program of the technological commands begins by the header, which consists the **PROGRAM** keyword and the program name, and terminates by the keyword **END**.

**Format**

```
PROGRAM ProgramName
  <statement 1>
  ...
  <statement N>
END
```

**Description**

The text of a program is written on the special problem-oriented language and can contain the mathematical expressions, functions, input/output operators, conditional operators, cycles, jump statement, calls of subroutines, the statements to form the NC-program blocks and the statements to work with the file of the technological commands.

**Example**

```
PROGRAM AbsMov
  FormBlock
  X = cld[1]
  Y = cld[2]
  if X <> LastX or y <> LastY then begin
    xs$ = Str(40*x)
    ys$ = str(40*y)
    if IsRapid> 0 then fs$ = "PU"
    else fs$ = "PD"
    output fs$ + xs$+","+ys$+";"
    LastX = X
    LAstY = Y
  end;
END
```
