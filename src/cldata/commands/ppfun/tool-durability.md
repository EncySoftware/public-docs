# PPFUN PPFUN(500) - Tool durability control command

`PPFUN(500)` command is generated then is is required to change the tool because of it's wear. In that case the `CLD[2]` parameter's value is the tool durability represented in minutes.

## Access from sppx

**PPFUN** has no sub-code-specific handler in sppx. All PPFUN sub-codes are processed in the single `program PPFun` handler, dispatching on `cld[1]` (`CLD.SubCode`); handle `PPFUN` by adding a branch there. See [Postprocessor function (PPFUN)](ppfun.md) for the full handler.

Example:

```pascal
program PPFun
  case cld[1] of
    500: begin        ! PPFUN
      ! cld[2] holds the tool durability in minutes
    end
  end
end
```

## Access from .NET

This sub-code has no dedicated handler - it is delivered through the base `OnPPFun` (dispatch on `cmd.SubCode`). See [Postprocessor function (PPFUN)](ppfun.md).

## See also
- [Postprocessor function (PPFUN)](ppfun.md)
- [CLData access model](../../cldata.md)
