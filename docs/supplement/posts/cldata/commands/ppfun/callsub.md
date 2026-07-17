# PPFUN CALLSUB(52) - NC-subprogram call command

NC-subprogram call command `PPFUN CALLSUB(52)` is used when NC-program contains several different NC-subprograms and at some point of program execution it is necessary to pass control to other subprogram. To achieve this the postprocessor of the `PPFUN CALLSUB(52)` command should call one of the NC-subprogram output operators. When this operators are called some or all of the NC-subprogram commands are processed. Otherwise technology commands of NC-subprograms are ignored.

`CLD[2]` parameter holds the unique identifier of the NC-subprogram.

## Access from sppx

**PPFUN** has no sub-code-specific handler in sppx. All PPFUN sub-codes are processed in the single `program PPFun` handler, dispatching on `cld[1]` (`CLD.SubCode`); handle `CALLSUB` by adding a branch there. See [Postprocessor function (PPFUN)](ppfun.md) for the full handler.

Example (from the Fanuc (30i)_Mill postprocessor):

```pascal
program PPFun
  case cld[1] of
      52: begin ! CallSub
        OutBlock
        MSub = 98; MSub@ = MaxReal
        P = MainProgramID + CLD[2]; P@ = MaxReal
        OutBlock
      end
  end
end
```

## Access from .NET

In addition to the base `OnPPFun`, this sub-code raises the dedicated handler `OnCallNCSub`:

```csharp
public override void OnCallNCSub(ICLDSub sub, ICLDPPFunCommand cmd, CLDArray cld)
```

The common .NET model (members, 1-based vs 0-based index) is described in [Postprocessor function (PPFUN)](ppfun.md).

Example - `OnCallNCSub` (from the Heidenhain_Mill_iTNC530_DN postprocessor):

```csharp
public override void OnCallNCSub(ICLDSub cldSub, ICLDPPFunCommand cmd, CLDArray cld)
{
    // 25 ;Top plane
    // 26 CALL LBL101
    cldSub.Tag = 100 + cldSub.SubCode;
    nc.OutText($"CALL LBL{cldSub.Tag}");

    // Reset the state of main registers to output them at the first assign. 
    nc.Block.Reset(nc.X, nc.Y, nc.Z, nc.Feed, nc.MoveType, nc.RCompens, nc.S, nc.MCoolant, nc.MSpindle);

    // Idle run of cldSub translation (with disabled writing to the nc-file) to fill registers with an actual state.
    NCFiles.DisableOutput();
    cldSub.Translate(false);
    NCFiles.EnableOutput();
}
```

## See also
- [Postprocessor function (PPFUN)](ppfun.md)
- [CLData access model](../../cldata.md)
