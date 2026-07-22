# PPFUN STARTSUB(50) - NC-subprogram start command

NC-subprogram start command `PPFUN STARTSUB(50)` together with the NC-subprogram end command [`PPFUN ENDSUB(51)`](endsub.md) is used to mark out the technology commands of the subprogram. All technology commands between `PPFUN STARTSUB(50)` and [PPFUN ENDSUB(51)](endsub.md), are considered to be NC-subprogram commands. Main program commands are processed consecutively, whereas the NC-subprogram commands are skipped. The NC-subprogram commands are translated only when NC-subprogram output operators are called from one of the main program commands.

`CLD[2]` parameter holds the unique identifier of the NC-subprogram.

## Access from sppx

**PPFUN** has no sub-code-specific handler in sppx. All PPFUN sub-codes are processed in the single `program PPFun` handler, dispatching on `cld[1]` (`CLD.SubCode`); handle `STARTSUB` by adding a branch there. See [Postprocessor function (PPFUN)](ppfun.md) for the full handler.

Example (from the Fanuc (30i)_Mill postprocessor):

```pascal
program PPFun
  case cld[1] of
      50: begin ! StartSub
        OutBlock;
        Output ""
        Output "%"
        ProgNum = MainProgramID + CLD[2]; ProgNum@ = MaxReal
        if CLData$<>"" then
          Output OutStr$ + " (" + UPCASE(CLData$) + ")"
        OutBlock
        Interp_ = MaxReal; Interp_@ = Interp_
        Feed_ = MaxReal; Feed_@ = Feed_
      end
  end
end
```

## Access from .NET

In addition to the base `OnPPFun`, this sub-code raises the dedicated handler `OnStartNCSub`:

```csharp
public override void OnStartNCSub(ICLDSub sub, ICLDPPFunCommand cmd, CLDArray cld)
```

The common .NET model (members, 1-based vs 0-based index) is described in [Postprocessor function (PPFUN)](ppfun.md).

Example - `OnStartNCSub` (from the Heidenhain_Mill_iTNC530_DN postprocessor):

```csharp
public override void OnStartNCSub(ICLDSub cldSub, ICLDPPFunCommand cmd, CLDArray cld)
{
    //433 LBL101
    cldSub.Tag = 100 + cldSub.SubCode;
    nc.WriteLine();
    nc.OutText($"LBL{cldSub.Tag}");
}
```

## See also
- [Postprocessor function (PPFUN)](ppfun.md)
- [CLData access model](../../cldata.md)
- [`PPFUN ENDSUB(51)`](endsub.md)
