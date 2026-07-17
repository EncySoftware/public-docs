# PPFUN ENDTECHINFO(59) - End of operation's technological information

This command is usually the last in the list of technological commands of the operation and serves to detect the end of the operation. The command has a set of parameters completely coincide with the parameters of [PPFUN TECHINFO(58)](techinfo.md) command. It provides technological information on the operation of CAM system.

## Access from sppx

**PPFUN** has no sub-code-specific handler in sppx. All PPFUN sub-codes are processed in the single `program PPFun` handler, dispatching on `cld[1]` (`CLD.SubCode`); handle `ENDTECHINFO` by adding a branch there. See [Postprocessor function (PPFUN)](ppfun.md) for the full handler.

Example (from the Fanuc (30i)_Mill postprocessor):

```pascal
program PPFun
  case cld[1] of
      59: begin ! EndTechInfo
        if Cmd.Int["PPFun(EndTechInfo).Enabled"]>0 then begin
          if CLDFile.CurrentFile <> CLDFile.FileCount - 1 then begin
            Output "M1"
          end
          Output " "
        end
        call CheckSwitchOffLocalCS
      end
  end
end
```

## Access from .NET

In addition to the base `OnPPFun`, this sub-code raises the dedicated handler `OnFinishTechOperation`:

```csharp
public override void OnFinishTechOperation(ICLDTechOperation op, ICLDPPFunCommand cmd, CLDArray cld)
```

The common .NET model (members, 1-based vs 0-based index) is described in [Postprocessor function (PPFUN)](ppfun.md).

Example - `OnFinishTechOperation` (from the Sinumerik (840D)_Mill_DN postprocessor):

```csharp
public override void OnFinishTechOperation(ICLDTechOperation op, ICLDPPFunCommand cmd, CLDArray cld)
{
    if (cmd.TechInfo.Enabled) {
        if (cmd.CLDFile.Index != CLDProject.CLDFiles.FileCount - 1){    
            nc.M.Show(1);
            nc.Block.Out();
        }
        nc.WriteLine();
    }
}
```

## See also
- [Postprocessor function (PPFUN)](ppfun.md)
- [CLData access model](../../cldata.md)
- [`PPFUN TECHINFO(58)`](techinfo.md)
