# The operator of a output of NC-subroutine NCSUB.OUTPUT

The operator transfers control to a file of technological commands *.mcd, which accordance the certain NC-subroutine.

**Format**

```
NCSUB.OUTPUT {(<NC-subroutine Number> {, <the Mode>}<, File name>)}
```

The operator is function, i.e. returns result. Possible values of returned result: 0 or 1.

**Description**

As a result of performance of the operator programs of processing of technological commands of the NC-subroutine specified by the identifier `NC-subroutine Number` consistently start to be caused. NC-subroutine number is usually transferred through the predetermined file of parameters of technological commands [CLD](../../basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md) with an index 2. NC-subroutine number is optional parameter. In case of absence of number consecutive translation of all available NC-subroutines will be made.

The optional parameter **Mode** defines, in what cases the result of translation of the NC-subroutine should be deduced in the text of the operating program, and can accept three values: 0, 1 and 2. At not specified parameter **Mode** is considered, that the mode is equal 1.

In a mode 0 a translation of technological commands change of values of registers and global variables is made, however the result of translation does not output in the text of the operating program. Thus, "idle pass" is carried out, allowing to simulate a program call in that case when the text of the subroutine should appear in other place of the operating program.

In a mode 1 (by default) translation of technological commands of the NC-subroutine is made also as well as in a mode 0, however the result of translation is output to the text of the operating program if the NC-subroutine still was never deduced. By the next calls of the operator in this mode "idle pass", as well as in a mode 0 is carried out. Thus, the result of translation of the NC-subroutine is output to the operating program only once.

By a call of the operator in a mode 2 a result of translation of the NC-subroutine is deduced in the operating program always, i.e. it is so much times, the operator how many is caused. Such mode allows to "unfold" NC-subroutines, in a case if system CNC does not support performance of subroutines.

The returned result is show whether the NC-subroutine is output in the operating program (NC). The result is equal 0 if not was output (has been carried out "idle pass"). The result is equal 1 if the NC-subroutine was deduced in NC. Accordingly 0 the returned result always is equal in a mode 0, in a mode 2 – is always equal 1. One result is equal in a mode 1 only after the first call of the operator for each NC-subroutine.

Use optional string parameter **File Name** to specify the name of the file, into which the NC-code of the subprogram will be saved. If the parameter is omitted then the subprogram will be output into the main NC-program file. If the **File Name** doesn't specify any file path the file of NC-subprogram will be created in the same folder as the main program.

Examples.

For example, the basic file of technological commands contains following commands:

```
0: PARTNO "Lathe Roughing"
1: PPFUN TECHINFO(58), 250.000, 114.890, 78.750, 0.000, 140.690,
2: COMMENT "Lathe Roughing"
3: LOADTL N 0, X 0.000, Y 0.000, Z 0.000, D 0.000, M 0, K 1, L 0.000
4: SPINDL ON(71), NO 1000.000, K 0, MODE CSS(2), SPEED 600.000
5: FEDRAT M 0.050, K 3, MMPR(316)
6: GOTO.abs X 140.690, Y 104.550, Z 0.000
7: GOTO.abs X 140.690, Y 78.750, Z 0.000
8: GOTO.abs X 114.890, Y 78.750, Z 0.000
9: FEDRAT M 0.050, K 0, MMPR(316)
10: PPFUN CALLSUB(52), 1.000, 0.000, 0.000, 0.000, 0.000, 0.000
11: FEDRAT M 0.050, K 8, MMPR(316)
12: GOTO.abs X 114.890, Y 104.550, Z 0.000
13: GOTO.abs X 140.690, Y 104.550, Z 0.000
14: SPINDL OFF(72), NO 0.000, K 0
15: FINI
```

While the file of the NC-subroutine with number 1 has the following list of technological commands:

```
1: COMMENT "Geometry_1"
2: PPFUN STARTSUB(50), 1.000, 0.000, 0.000, 0.000, 0.000, 0.000
3: FEDRAT M 0.000, K 0, MMPR(316)
4: GOTO.abs X 114.890, Y 33.381, Z 0.000
5: CIRCLE XC 114.690, YC 33.380, ZC 0.000, R 0.200, XE 114.831, YE
6: GOTO.abs X 110.151, Y 38.201, Z 0.000
7: CIRCLE XC 110.010, YC 38.060, ZC 0.000, R 0.200, XE 110.010, YE
8: GOTO.abs X 62.230, Y 38.260, Z 0.000
9: GOTO.abs X 41.460, Y 38.257, Z 0.000
10: PPFUN ENDSUB(51), 1.000, 0.000, 0.000, 0.000, 0.000, 0.000
```

Let's admit, that the program of processing of the tenth command ([PPFUN CALLSUB(52)](../../../../../cldata/commands/ppfun/callsub.md)) the basic file looks so:

```
program PPFun
  if cld[1]=52 then begin! CallSub
    NCSub.Output(CLD[2])
  end
end
```

In that case serial processing of technological commands of the basic file since a line 0 till the line 9 will be made from the very beginning. Having reached a line 10, at processing of operator `NCSub.Output(CLD[2])`, management will pass to a file with the NC-subroutine number 1 since the second parameter of a technological command is equal 1.000. Thus, technological commands of the NC-subroutine since a line 1 till the line 10 will start to be processed consistently. After processing of last command ([PPFUN ENDSUB(51)](../../../../../cldata/commands/ppfun/endsub.md)) management will return to the basic file, and all remained commands (lines 11 – 15) will be processed.

Other examples of a call of the operator are resulted is shown below:

```
! Carries out translation of all available NC-subroutines
NCSub.Output
! Carries out NC-subroutine translation with number 3 in a mode 0
NCSub.Output(3, 0)
! Carries out NC-subroutine translation with number taken from the
! second parameter from a current technological command in a mode 2
NCSub.Output(CLD[2], 2)
if NCSub.Output(CLD[2]) = 0 then ! Carries out translation
begin ! NC-subroutines in a mode 1.
Output "CALL "+ ! Deduces a line "CALL ", if already
NCSub.StartLabel(CLD[2]) ! there was made a output in NC
end
! Process NC-subprogram number 7 in mode 1
! and output into Sub7.txt file
NCSub.Output(7, "Sub7.txt")
! Process NC-Subprogram number 7 in mode 2
! and output into Sub7.txt file
NCSub.Output(7, 2, "Sub7.txt")
```

**See also**

[Operators of work with NC-subroutines](readme-operators-of-work-with-nc-subroutines.md)

[`NCSUB.OUTPUTALL` operator](operator.md)

[The operator of definition of an initial marker of NC-subroutine `NCSUB.STARTLABEL`](operator-of-definition-of-an-initial-marker-of-nc-subroutine.md)
