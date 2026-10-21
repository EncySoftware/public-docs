# PPFUN - Postprocessor function

## Command caption

How the command appears in the CLData command list:

```text
PPFUN PPFUN(500)|STARTSUB(50)|ENDSUB(51)|CALLSUB(52)|REPSTART(53)|REPEND(54)|JUMP(55)|
      TECHINFO(58)|ENDTECHINFO(59)|WEDMConditions(56)|WEDMPassItem(57) {, a} {, b} ...
```

Postprocessor function **PPFUN** is a multiple purpose postprocessors generator command. **PPFUN** command can be used to present different kinds of data and machining parameters. The actual type of **PPFUN** command is defined by the first parameter of the CLData array – `CLD[1]` (`CLD.SubCode`). Other CLD array parameters (`CLD[2]` through `CLD[257]`) can have various meaning dependinig on the type of the **PPFUN** command.

## Access from sppx

Handler: `program PPFun`

The `cld` array is read by index or by name - in sppx by the typed short name (e.g. `cld.X`), in .NET by the same name as a string key (e.g. `cld["X"]`).

| Parameter | CLD array | CLD name | Description |
|---|---|---|---|
| PPFUN(500)<br>STARTSUB(50)<br>ENDSUB(51)<br>CALLSUB(52)<br>REPSTART(53)<br>REPEND(54)<br>JUMP(55)<br>TECHINFO(58)<br>WEDMConditions(56)<br>WEDMPassItem(57) | CLD[1] | CLD.SubCode | Postprocessor function type |
| a, b, c, d... | CLD[2] – CLD[257] |  | List of optional parameters. The structure of the parameters list is defined by the actual postprocessor function |

The list of postprocessor functions types includes:

- [`PPFUN PPFUN(500)` - tool durability control command](tool-durability.md)
- [`PPFUN STARTSUB(50)` - NC-subprogram start command](startsub.md)
- [`PPFUN ENDSUB(51)` - NC-subprogram end command](endsub.md)
- [`PPFUN CALLSUB(52)` - NC-subprogram call command](callsub.md)
- [`PPFUN TECHINFO(58)` - command specifies technology parameters of the operation](techinfo.md)
- [`PPFUN ENDTECHINFO(59)` - end of operation's technological information](endtechinfo.md)
- [`PPFUN WEDMConditions(56)` - command specifies ED machining conditions](wedm-conditions.md)
- [Wire EDM pass properties PPFun WEDMPassItem(57)](wedm-passitem.md)

Example (from the Fanuc (30i)_Mill postprocessor):

```pascal
program PPFun
  case CLD.SubCode of
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
    51: begin ! EndSub
      OutBlock
      MSub = 99; MSub@ = MaxReal
      OutBlock
      Output "%"
    end
    52: begin ! CallSub
      OutBlock
      MSub = 98; MSub@ = MaxReal
      P = MainProgramID + CLD[2]; P@ = MaxReal
      OutBlock
    end
    58: begin ! TechInfo
      case cld[60] of
        1: OperationIsLathe = 0 !– mill,
        2: OperationIsLathe = 1 !– lathe,
        else OperationIsLathe = 3 ! other
      end
      CSOnCount = 0
      NeedKorDl = 0
      WasLoadTool = 0
      KorDl = 0; KorDl@ = KorDl
      H = cld[31]; H@ = H
      Zcycle = 0; Zcycle@ = Zcycle
      ZClear = 0; ZClear@ = ZClear
      QStep = 0; QStep@ = QStep
      !MC = 9; MC@ = Mc;
      Interp_ = MaxReal; Interp_@ = Interp_
      FEED_ = MaxReal; FEED_@ = FEED_
    end;
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

Besides the base `OnPPFun`, the framework raises sub-code-specific handlers:

```csharp
public override void OnPPFun(ICLDPPFunCommand cmd, CLDArray cld)                                    // base
public override void OnStartTechOperation(ICLDTechOperation op, ICLDPPFunCommand cmd, CLDArray cld) // TECHINFO(58)
public override void OnFinishTechOperation(ICLDTechOperation op, ICLDPPFunCommand cmd, CLDArray cld)// ENDTECHINFO(59)
public override void OnStartNCSub(ICLDSub sub, ICLDPPFunCommand cmd, CLDArray cld)                  // STARTSUB(50)
public override void OnFinishNCSub(ICLDSub sub, ICLDPPFunCommand cmd, CLDArray cld)                 // ENDSUB(51)
public override void OnCallNCSub(ICLDSub sub, ICLDPPFunCommand cmd, CLDArray cld)                   // CALLSUB(52)
```

Inheritance: `ICLDPPFunCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd["..."]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../../cldata.md).

| Property | Type | Description |
|---|---|---|
| `cmd.SubCode` | int | Numerical code of the PPFUN subtype. Standard subtypes are listed above, but the code can have any arbitrary value defined by the postprocessor developer. |
| `cmd.TechInfo` | `IPPFunTechInfo` | For `TECHINFO(58)`/`ENDTECHINFO(59)` - additional information about the operation. |

`IPPFunTechInfo` exposes `Enabled` (true if the operation uses a tool different from the previous one), `SetupStage` (`Index`, `Name`), `Tool` (`Number`, `ConnectorIndex`, `RevolverID`), `Workpiece` (`ConnectorID`) and `Part` (`Index`, `Number`, `Name`).

Example - `OnPPFun` (from the AgieCharmilles_WireEDM_DN postprocessor):

```csharp
public override void OnPPFun(ICLDPPFunCommand cmd, CLDArray cld)
{
    switch (cmd.SubCode)
    {
        case 58: // TechInfo
            nc.WriteLine("(Rapid level       = " + Str((double)cld[9]) + ")");
            nc.WriteLine("(Upper guide level = " + Str((double)cld[47]) + ")");
            nc.WriteLine("(Upper work level  = " + Str((double)cld[10]) + ")");
            nc.WriteLine("(Lower work level  = " + Str((double)cld[11]) + ")");
            nc.WriteLine("(Lower guide level = " + Str((double)cld[48]) + ")");
            nc.WriteLine("(Wire diameter     = " + Str((double)cld[27]) + ")");
            break;

        case 56: // WEDMConditions
            nc.H.Show(cld[4]); // Offset code
            nc.HValue.Show(cld[5]); // Offset value
            nc.Block.Out();
            break;

        case 50: // STARTSUB
            nc.BlockN.Show(nc.ProgN + cld[2]);
            nc.Block.Out();
            break;

        case 51: // ENDSUB
            if (wireInserted)
            {
                BreakWire();
            }
            nc.MSub.Show(99);
            nc.Block.Out();
            nc.WriteLine();
            break;

        case 52: // CALLSUB
            nc.MSub.Show(98);
            nc.SubN.Show(nc.ProgN + cld[2]);
            nc.Block.Out();
            // Idle sub call
            // TODO: NCSub.Output(cld[2], 0)
            break;
    }
}
```

## See also
- [CLData access model](../../cldata.md)
