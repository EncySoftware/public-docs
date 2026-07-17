# The operator of definition of an initial marker of NC-subroutine NCSUB.STARTLABEL

The operator returns a text value of an initial marker of the NC-subroutine, and also allows to define text value of an initial marker of the NC-subroutine any text value.

**Format**

```
S$ = NCSUB.STARTLABEL(<NC-subroutine Number>)
```

or

```
NCSUB.STARTLABEL(<NC-subroutine Number>) = S$
```

**Description**

- `NC-subroutine Number` – the unique identifier of the NC-subroutine.
- `S$` – any text variable. In the second case also can be set the text constant or any expression which is returning a text. The operator can be used by a similarly as text variable in expressions and functions processing strings.

The operator it is possible to use for definition of an initial markers of the NC-subroutine for a output in the operating program of the lines identifying the beginning of the subroutine. As a marker it is possible to set and a frame number.

Usually at the moment of the beginning of translation of technological commands in the operating program (NC) the location of the concrete subroutine in NC is not known. During this time the initial marker of the NC-subroutine is established in value by default **SLabelNxxx**, where **xxx** – NC-subroutine number. In the processing of NC-subroutine realization, i.e. its output in NC, usually is possible define an initial marker. Therefore in procedure of processing of a technological command of the beginning of subroutine [PPFUN STARTSUB(50)](../../../../cldata/commands/ppfun/startsub.md) use the operator of definition of an initial marker for installation of an initial marker of the subroutine:

```
NCSub.StartLabel(CLD[2]) = S$ ! Assignment of an initial marker
```

- `S$` – a text variable or any expression returning a text, corresponding to a marker or number of a frame of the subroutine.
- `CLD[2]` – NC-subroutine number transferred through the predetermined file of parameters of technological command [CLD](../../basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md).

Note: At the included automatic numbering of frames of the operating program before the beginning of performance of procedure of processing of a technological command of the beginning of subroutine [PPFUN STARTSUB(50)](../../../../cldata/commands/ppfun/startsub.md) initial marker current value of the register of number of a frame automatically is appropriated. If it suits, it is possible not to use the operator for assignment of value of an initial marker.

Before a subroutine call usually is required to define, where the given subroutine is located. Therefore in procedure of processing of a technological command of a call of subroutine [PPFUN CALLSUB(52)](../../../../cldata/commands/ppfun/callsub.md) use the operator of definition of an initial marker of the subroutine

```
S$ = NCSub.StartLabel(CLD[2])! Reception of an initial marker
```

And then deduce the marker defined thus in the text of the operating program in the format necessary.

Note: If performance of procedure of processing of a technological command of a call of subroutine [PPFUN CALLSUB(52)](../../../../cldata/commands/ppfun/callsub.md) is made earlier, than there was an assignment of value of an initial marker (before the subroutine is deduced in NC) the operator of definition of an initial marker will return value by default a kind **SLabelNxxx**. After the termination of translation of the operating program if the subroutine has been deduced in CNC, and to a marker the new value differing from value by default has been appropriated, replacement of all values by default in text NC on again appropriated marker is made.

In this case the transformations which are carried out over line, a marker containing value (value by default a kind **SLabelNxxx**), should not break integrity of expression by default, differently the result of translation NC can appear incorrect. In such cases of transformation over line of a marker it is necessary to make not at reception of value of a marker, and before assignment of value of a marker in procedure of processing of a technological command of the beginning of subroutine [PPFUN STARTSUB(50)](../../../../cldata/commands/ppfun/startsub.md).

**See also**

[Operators of work with NC-subroutines](readme-operators-of-work-with-nc-subroutines.md)

[The operator of definition of a final marker of NC-subroutine `NCSUB.ENDLABEL`](operator-of-definition-of-a-final-marker-of-nc-subroutine.md)
