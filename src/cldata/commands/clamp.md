# CLAMP - Fixtures clamp

Use **CLAMP** command to control part fixture devices (such as chucks, vices, collets, etc.) in the pick-and-place, takeover operations.

Command: CLAMP ID(N), ON(71)|OFF(72) DIR(N)

## Access from sppx

Handler: `program Clamp`

| Parameter | CLD array | CLD name | Description |
|---|---|---|---|
| ID | CLD[1] | CLD.ID | Unique identifier of the clamping device you need to switch. Depend on the equipment settings inside a CAM project. |
| IsOn | CLD[2] | CLD.IsOn | New state of the clamping device: 71 - clamp is on, the workpiece is fixed in the clamping device. 72 - clamp is off. the workpiece is released. |
| Dir | CLD[3] | CLD.Dir | Clamping direction (-1; 0; +1) - direction of the clamping jaw movement (sign of jaw axis coordinate change). |

Here is a simple example of programs handlers for this command.

```pascal
program Clamp
  if CLD[2] = 72 then begin
    call OutPause(1)
    if CLD[1] = 2 then begin
      Mchuck = 111; Mchuck@ = Maxreal
      Formblock
      Outstr$ = Outstr$ + " (OTKRYT-PROTIVOSHPINDEL)"
      Output Outstr$
      Formblock
      Outstr$ = Outstr$ + " M114 (AIR ON)"
      Output Outstr$
      call OutPause(1)
      Formblock
      Outstr$ = Outstr$ + " M115 (AIR OFF)"
      Output Outstr$
    end else begin
      Mchuck = 11; Mchuck@ = Maxreal
      Formblock
      Outstr$ = Outstr$ + " (OTKRYT-GLAVNYi SHPINDEL)"
      Output Outstr$
      Formblock
      Outstr$ = Outstr$ + " M14 (AIR ON)"
      Output Outstr$
      call OutPause(1)
      Formblock
      Outstr$ = Outstr$ + " M15 (AIR OFF)"
      Output Outstr$
    end
  end else begin
    if CLD[1] = 2 then begin
      Mchuck = 110; Mchuck@ = Maxreal
      Formblock
      Outstr$ = Outstr$ + "(ZAKRIT-PROTIVOSHPINDEL)"
    end else begin
      Mchuck = 10; Mchuck@ = Maxreal
      Formblock
      Outstr$ = Outstr$ + "(ZAKRIT-GLAVNIY SHPINDEL)"
    end
    Output Outstr$
    call OutPause(1)
  end
end
```

## Access from .NET

Handler:

```csharp
public override void OnClamp(ICLDClampCommand cmd, CLDArray cld)
```

Inheritance: `ICLDClampCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd["..."]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

Example - `OnClamp` (from the Goodway SW postprocessor):

```csharp
public override void OnClamp(ICLDClampCommand cmd, CLDArray cld)
{
    base.OnClamp(cmd, cld);
    bool MainSp = cmd.ClampID==1;
    outClamp(nc, MainSp, cmd.IsOn, 0.2);
}
```

## See also
- [CLData access model](../cldata.md)
