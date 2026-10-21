# RAPID - Rapid feedrate

## Command caption

How the command appears in the CLData command list:

```text
RAPID N n
```

**RAPID** activates rapid travel mode (G-code G00). All further travels are done in rapid mode until feedrate modification command [FEDRAT](fedrat.md) is received.

## Access from sppx

Handler: `program Rapid`

| Parameter | CLD array | CLD name | Description |
|---|---|---|---|
| n | CLD[1] | CLD.N | Rapid feedrate value |

Example (from the Fanuc (30i)_Mill postprocessor):

```pascal
program Rapid
  if IsRotaryInterpolation>0 then begin
    INTERP_ = 1
    Feed_ = 5000
    GFeed = 94
  end else begin
    if INTERP_ > 0 then INTERP_ = 0    ! G0
  end
  RapFr=cld[1]
end
```

## Access from .NET

Handlers:

```csharp
public override void OnMoveVelocity(ICLDMoveVelocityCommand cmd, CLDArray cld)   // shared velocity handler (FEDRAT and RAPID)
public override void OnRapid(ICLDRapidCommand cmd, CLDArray cld)   // rapid feed
```

Inheritance: `ICLDRapidCommand : ICLDMoveVelocityCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd["..."]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

| Member | Type | Description |
|---|---|---|
| `cmd.IsRapid` | `bool` | Contains "true" if the command is a RAPID command, otherwise it is "false". |
| `cmd.FeedKind` | `CLDFeedKind` | The kind of a feed (working, rapid, engage, return, finish etc.).<br>Possible values:<br>`Working` (0) - The feed kind for base working movements.<br>`Rapid` (1) - The feed kind of rapid movements.<br>`First` (2) - The feed kind for the working movements on a first (roughing) pass.<br>`Engage` (4) - The feed kind for the movements entering to the first machining (cutting) point.<br>`Retract` (8) - The feed kind for the movements leaving the last machining (cutting) point.<br>`Plunge` (16) - The feed kind for the movements that plunge vertically into the machining area.<br>`Finish` (32) - The feed kind for the working movements on a last (finishing) pass.<br>`Next` (64) - The feed kind for the short link movements.<br>`Return` (128) - The feed kind for the movements which take the tool away from the machining site.<br>`Approach` (256) - The feed kind for the movements which bring the tool closer to the machining site.<br>`Rapid5D` (512) - The feed kind value reserved for an internal use.<br>`TransitionOnSafe` (1024) - The feed kind for the movements performed in a safe area.<br>`ApproachFromSafe` (2048) - The feed kind for the movements from the safe area to the machining side.<br>`ReturnToSafe` (4096) - The feed kind for the movements from the machining side to the safe area.<br>`LongNext` (8192) - The feed kind for the long link movements.<br>`ThreadPitch` (16384) - The feed kind for the threading movements.<br>`Overload` (1073741824) - The feed kind value reserved for an internal use. |
| `cmd.FeedCode` | `int` | Numerical representation of the "FeedKind" flag, that defines the kind of a feed (working, rapid, engage, return, finish etc.). For a wire EDM case it contains the numerical code of a row in a machining conditions table. |
| `cmd.FeedUnits` | `CLDFeedUnits` | Units of the feed (mm/min, mm/rev etc.)<br>Possible values:<br>`MPM` (0) - Current linear units (mm or inch) per minute.<br>`MPR` (1) - Current linear units (mm or inch) per revolution.<br>`ConditionCode` (2) - Numerical code of a row in a machining conditions table (for a wire EDM). |
| `cmd.FeedValue` | `double` | The value of the feed. |

Example - `OnMoveVelocity` (from the Fanuc (30i)_Mill_DN postprocessor):

```csharp
public override void OnMoveVelocity(ICLDMoveVelocityCommand cmd, CLDArray cld)
{
    if (cmd.IsRapid) {
        nc.GInterp.v = 0;
    } else {
        if (nc.GInterp == 0)
            nc.GInterp.v = 1;
        nc.F.v = cmd.FeedValue;
        if (cmd.FeedUnits==CLDFeedUnits.MPR) 
            nc.GFeed.v = 95;
        else 
            nc.GFeed.v = 94;
        if (IsFirstFeed) 
        {
            nc.F.Show();
            nc.GFeed.Show();
            IsFirstFeed = false;
        } 
    }
}
```

## See also
- [CLData access model](../cldata.md)
