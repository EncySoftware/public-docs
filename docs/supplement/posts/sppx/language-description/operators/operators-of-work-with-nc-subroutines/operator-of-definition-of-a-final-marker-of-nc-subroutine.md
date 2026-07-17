# The operator of definition of a final marker of NC-subroutine NCSUB.ENDLABEL

Returns text value of a final marker of the NC-subroutine, and also allows to appropriate to text value of a final marker of the NC-subroutine any text value.

**Format**

```
S$ = NCSUB.ENDLABEL(    
<NC-subroutine Number>    
)
```

or

```
NCSUB.ENDLABEL(<NC-subroutine Number>) = S$
```

**Description**

- `NC-subroutine Number` – the unique identifier of the NC-subroutine.
- `S$` – any text variable. In the second case the text constant or any expression which returns text size also can be set.

The operator can be used as text variable in expressions and functions processing texts.

The operator is used for definition of a final marker of the NC-subroutine for a output in the operating program of the texts identifying the end of the subroutine. As a marker it is possible to indicate frame number.

Usually at the moment of the beginning of translation of technological commands in the operating program (NC) the location of the concrete subroutine in NC is not known. During this time the final marker of the NC-subroutine is established in value by default **ELabelNxxx**, where **xxx** – NC-subroutine number. In the course of NC-subroutine realization, i.e. its output in NC, usually is possible to define a final marker. Therefore in procedure of processing of a technological command of the end of subroutine [PPFUN ENDSUB(51)](../../../../cldata/commands/ppfun/endsub.md) use the operator of definition of a final marker for installation of a final marker of the subroutine:

```
NCSub.EndLabel(CLD[2]) = S$ ! Assignment of a final marker
```

- `S$` – a text variable or any expression returning a text, corresponding to a marker or number of a frame of the subroutine.
- `CLD[2]` – NC-subroutine number transferred through the predetermined file of parameters of technological command [CLD](../../basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md).

Note: At the included automatic numbering of frames of the operating program before the beginning of performance of procedure of processing of a technological command of the end of subroutine [PPFUN ENDSUB(51)](../../../../cldata/commands/ppfun/endsub.md) final marker current value of the register of number of a frame automatically is appropriated. If it suits, it is possible not to use the operator for assignment of value of a final marker.

Before a subroutine call usually is define, where the given subroutine is located. Therefore in procedure of processing of a technological command of a call of subroutine [PPFUN CALLSUB(52)](../../../../cldata/commands/ppfun/callsub.md) use the operator of definition of a final marker of the subroutine

```
S$ = NCSub.EndLabel(CLD[2]) ! Reception of a final marker
```

Then output the marker defined thus in the text of the operating program in the format necessary.

Note: If performance of procedure of processing of a technological command of a call of subroutine [PPFUN CALLSUB(52)](../../../../cldata/commands/ppfun/callsub.md) is made earlier, than there was an assignment of value of a final marker (before the subroutine is deduced in NC) the operator of definition of a final marker will return value by default a kind **ELabelNxxx**. After the translation of the operating program terminated if the subroutine has been deduced in NC, and a marker the new value differing from value by default, will be made replacement of all values by default in text NC on again appropriated marker is made.

In this case the transformations which are carried out in line a marker of containing value (value by default a kind **ELabelNxxx**), should not break integrity of expression by default, otherwise the result of translation NC can appear incorrect. In such cases of transformation over line of a marker it is necessary to make not when get value of a marker, before assignment of value of a marker in procedure of processing of a technological command of the end of subroutine [PPFUN ENDSUB(51)](../../../../cldata/commands/ppfun/endsub.md).

**See also**

[Operators of work with NC-subroutines](readme-operators-of-work-with-nc-subroutines.md)

[The operator of definition of an initial marker of NC-subroutine `NCSUB.STARTLABEL`](operator-of-definition-of-an-initial-marker-of-nc-subroutine.md)
