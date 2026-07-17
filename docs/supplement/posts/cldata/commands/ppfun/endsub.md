# PPFUN ENDSUB(51) - NC-subprogram end command

NC-subprogram end command `PPFUN ENDSUB(51)` together with the NC-subprogram start command [`PPFUN STARTSUB(50)`](startsub.md) is used to mark out the technology commands of the subprogram. All technology commands between [PPFUN STARTSUB(50)](startsub.md) and `PPFUN ENDSUB(51)`, are considered to be NC-subprogram commands. Main program commands are processed consecutively, whereas the NC-subprogram commands are skipped. The NC-subprogram commands are translated only when NC-subprogram output operators are called from one of the main program commands.

`CLD[2]` parameter holds the unique identifier of the NC-subprogram.

## Access from sppx

**PPFUN** has no sub-code-specific handler in sppx. All PPFUN sub-codes are processed in the single `program PPFun` handler, dispatching on `cld[1]` (`CLD.SubCode`); handle `ENDSUB` by adding a branch there. See [Postprocessor function (PPFUN)](ppfun.md) for the full handler.

Example (from the Fanuc (30i)_Mill postprocessor):

```pascal
program PPFun
  case cld[1] of
      51: begin ! EndSub
        OutBlock
        MSub = 99; MSub@ = MaxReal
        OutBlock
        Output "%"
      end
  end
end
```

## Access from .NET

In addition to the base `OnPPFun`, this sub-code raises the dedicated handler `OnFinishNCSub`:

```csharp
public override void OnFinishNCSub(ICLDSub sub, ICLDPPFunCommand cmd, CLDArray cld)
```

The common .NET model (members, 1-based vs 0-based index) is described in [Postprocessor function (PPFUN)](ppfun.md).

Example - `OnFinishNCSub` (from the Heidenhain_Mill_iTNC530_DN postprocessor):

```csharp
public override void OnFinishNCSub(ICLDSub cldSub, ICLDPPFunCommand cmd, CLDArray cld)
{
    // 454 LBL0
    nc.Block.Out();
    nc.OutText("LBL0");
}
```

## See also
- [Postprocessor function (PPFUN)](ppfun.md)
- [CLData access model](../../cldata.md)
- [`PPFUN STARTSUB(50)`](startsub.md)
