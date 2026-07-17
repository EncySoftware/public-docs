# Technique of work with NC-subroutines

Existing systems CNC accept various ways of registration of subroutines in the operating program (NC), however by criterion of an order of the text of subroutines concerning lines of the basic program it is possible to allocate some typical cases:

- Subroutines are deduced in NC to a output of the basic program;
- Subroutines are deduced in NC after a output of the basic program;
- Subroutines are deduced in NC in a place of the first call;
- Subroutines are not supported, and the subroutine text is deduced by each call.

Consider how it is possible to realize each of the specified cases.

### Subroutines are deduced in NC to a output of the basic program

The given format of a output assumes, that in the operating program all available subroutines is deduced at the beginning, and the basic program containing lines of a call of subroutines is inserted after.

To carry out a output of subroutines at the beginning, it is necessary to insert a corresponding code into procedure of processing of technological command [PARTNO](../../../../cldata/commands/partno.md) which is carried out before all. The procedure kind can be following.

```
program PartNo
  ! Initialization of variables
  ! A output of the lines identifying
  ! the beginning of section of subroutines
  NCSub.Output ! A output of all available subroutines
  ! A output of the lines identifying
  ! the end of section of subroutines and
  ! the beginning of section of the basic program
  ! Initialization of variables
end
```

For the purpose of formation of lines of the operating program identifying the beginning of the NC-subroutine, the end of the NC-subroutine and a NC-subroutine call, is necessary write procedure-output agent of technological commands [PPFUN STARTSUB(50)](../../../../cldata/commands/ppfun/startsub.md), [PPFUN ENDSUB(51)](../../../../cldata/commands/ppfun/endsub.md) and [PPFUN CALLSUB(52)](../../../../cldata/commands/ppfun/callsub.md) as shown below.

```
program PPFun
  if CLD[1]=50 then begin ! Command StartSub
    ! A output of the line identifying the beginning
    ! subroutines (here "NameSubroutine")
    Output "o"+NCSub.Name(CLD[2])
    ! Assignment to an initial marker current
    ! value of the register of number of a frame
    NCSub.StartLabel(CLD[2]) = Str(BlockN)
  end
  else if CLD[1]=51 then begin ! Command EndSub
    ! A output of the line identifying the end subroutines
    ! (here "Nxx M99", where Nxx - frame number)
    FormBlock
    Output OutStr $ + "M99"
    ! Assignment to a final marker values
    ! from the register of number of a frame
    NCSub.EndLabel(CLD[2]) = Str(BlockN)
  end
  else if CLD[1]=52 then begin ! Command CallSub
    ! A output of a line of a call of the subroutine of a kind
    ! "Nxx M98 Nbb, Nee", where
    ! Nxx - flowing a frame,
    ! Nbb - a beginning frame subroutine,
    ! Nee - a frame of the end of the subroutine
    FormBlock
    Output OutStr$ + "M98" +
    NCSub.StartLabel(CLD[2]) + "," +
    NCSub.EndLabel(CLD[2])
    ! Single run of the subroutine
    NCSub.Output(CLD[2], 0)
  end
end
```

In the given example the initial and final markers current values are appropriated from the register of number of a frame, however at the included automatic numbering, similar actions are made automatically and the specified code is optional. It is shown only for an example.

In the operator of a output of NC-subroutine [NCSUB.OUTPUT](operator-of-a-output-of-nc-subroutine.md) the mode 0 is specified, however, since all subroutines are already deduced in the operating program earlier, it is possible not to determine the given parameter, that will be signify a output in a mode 1 ("only for the first time").

### Subroutines are deduced in NC after a output of the basic program

Is supposed, that the text of the basic operating program together with lines of a call of NC-subroutines is placed before a code of subroutines. In this case the operator of a output of NC-subroutines is located in procedure of processing of a technological command which is processed by last – [FINI](../../../../cldata/commands/fini.md), a appearance of this procedure is shown below:

```
program Fini
  ! A output of the lines identifying the end of section of
  ! the basic program and the beginning of section of subroutines
  ! Initialization of variables
  NCSub.Output! A output of all available subroutines
  ! A output of the lines identifying the end of section of subroutines
end
```

The example of the output procedure for technological commands of the beginning, the end and a call of subroutines ([PPFUN STARTSUB(50)](../../../../cldata/commands/ppfun/startsub.md), [PPFUN ENDSUB(51)](../../../../cldata/commands/ppfun/endsub.md) and [PPFUN CALLSUB(52)](../../../../cldata/commands/ppfun/callsub.md)) in comparison with the previous case remains invariable. However it is necessary to consider, that the values returned by functions of work with markers ([NCSUB.STARTLABEL](operator-of-definition-of-an-initial-marker-of-nc-subroutine.md) and [NCSUB.ENDLABEL](operator-of-definition-of-a-final-marker-of-nc-subroutine.md)), till the moment of the termination of translation are not those markers which are appropriated by it, and have values by default a kind **SLabelNxxx** and **ELabelNxxx**, where **xxx** – NC-subroutine number, because real values of markers at the moment of inquiry are not defined. Real values of markers are substituted only after the termination of translation of the operating program as a whole.

### Subroutines are deduced in NC in a place of the first call

In this case the subroutine is at the same time a part of the basic program, the reference to which can be made repeatedly, define for example, initial and final frames. Thus, the subroutine will be deduced by the first call as a part of the basic code, and at the subsequent – as a call of an existing code. All code which is responsible for the NC-subroutines, is located in procedure of processing of technological commands of the beginning, the end and a call of subroutines ([PPFUN STARTSUB(50)](../../../../cldata/commands/ppfun/startsub.md), [PPFUN ENDSUB(51)](../../../../cldata/commands/ppfun/endsub.md) and [PPFUN CALLSUB(52)](../../../../cldata/commands/ppfun/callsub.md)).

```
program PPFun
  if CLD[1]=50 then begin ! Command StartSub
    ! Assignment to an initial marker current value of
    ! the register of number of a frame
    NCSub.StartLabel(CLD[2]) = Str(BlockN)
  end
  else if CLD[1]=51 then begin ! Command EndSub
    ! Assignment to a final marker values from
    ! the register of number of a frame
    NCSub.EndLabel(CLD[2]) = Str(BlockN)
  end
  else if CLD[1]=52 then begin ! Command CallSub
    ! If an output of subroutine already was
    if NCSub.Output(CLD[2])=0 then begin
      ! Output of line of call of the subroutine of kind
      ! "Nxx M98 Nbb, Nee", where
      ! Nxx - flowing a frame
      ! Nbb - a beginning frame subroutine,
      ! Nee - a frame of the end of the subroutine
      FormBlock
      Output OutStr$ + "M98" +
      NCSub.StartLabel(CLD[2]) +
      ","+NCSub.EndLabel(CLD[2])
    end
  end
end
```

In the resulted example the first call of operator `[NCSUB.OUTPUT(CLD[2])](operator-of-a-output-of-nc-subroutine.md)` for each subroutine will carry out a NC-subroutine output in the operating program and will return value 1. By each subsequent call, "idle pass" will be carried out and value 0 will be returned. Then in the operating program, the line of a call of the corresponding subroutine will be added.

In the given example the initial and final markers current values are appropriated from the register of number of a frame, however at the included automatic numbering, similar actions are made automatically and the specified code is optional.

### Subroutines are not supported

When system CNC does not support use of subroutines, and the sequence of technological commands contains NC-subroutines and their call it is possible to carry out "unfolding" of NC-subroutines, i.e. in all places of a call of the subroutine it is necessary to insert the subroutine instead of a line of a call. For this purpose it is necessary to insert a code of following kind into procedure of processing of a technological command of a call of subroutine [PPFUN CALLSUB](../../../../cldata/commands/ppfun/callsub.md):

```
program PPFun
  if CLD[1]=52 then begin ! Command CallSub
    NCSub.Output(CLD[2], 2) ! A subroutine output in any case
  end ! (A mode 2)
end
```

Processing of commands of the beginning and the end of subroutines in this case is not required.

**See also**

[Operators of work with NC-subroutines](readme-operators-of-work-with-nc-subroutines.md)

[The operator of a output of NC-subroutine `NCSUB.OUTPUT`](operator-of-a-output-of-nc-subroutine.md)

[The operator of definition of a name of NC-subroutine `NCSUB.NAME`](operator-of-definition-of-a-name-of-nc-subroutine.md)

[The operator of definition of an initial marker of NC-subroutine `NCSUB.STARTLABEL`](operator-of-definition-of-an-initial-marker-of-nc-subroutine.md)

[The operator of definition of a final marker of NC-subroutine `NCSUB.ENDLABEL`](operator-of-definition-of-a-final-marker-of-nc-subroutine.md)
