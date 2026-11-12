# SYNCAXES - Axes movement synchronization

The purpose of this command is to enable or disable the synchronization of simultaneous motion of two machine axes (for example left and right spindle rotation axes on a double spindles lathe machine).

Command: SYNCAXES ON(71) | OFF(72), FirstAxisID(Axis1), SecondAxisID(Axis2)

## Access from sppx

Handler: `program SyncAxes`

| Parameter | CLD array | Description |
|---|---|---|
| IsOn | CLD[1] | New state of the synchronization: 71 - Axes synchronization is active. 72 - Axes motion synchronization is disabled. |

Parameters available through the cmd operator

| Parameter | Type | Description |
|---|---|---|
| Action | Integer | Toggle control that modifies the synchronization state (enabled/disabled): 1 - Set synchronization state to enabled. 0 - Set synchronization state to disabled. |
| Axis1 | String | String identifier for the first of the two axes to be synchronized. |
| Axis2 | String | String identifier for the second of the two axes to be synchronized. |

Here is a simple example of program handler for this command:

```pascal
program SyncAxes
  Outblock
  a1: String;
  a1 = cmd.Str["Axis1"];
  a2: String;
  a2 = cmd.Str["Axis2"];
  if (a1="AxisCPos") or (a2="AxisCPos") or (a1="AxisC1Pos") or (a2="AxisC1Pos") then begin
    if CLD.IsOn=71 then begin
      GSyncSpeeds = 288; GSyncSpeeds@ = Maxreal;
      Formblock;
      Output Outstr$ + " (Sync spindles rotation)";
      Phase = C2-C; Phase@=MaxReal;
      GSyncPhase = 289; GSyncPhase@=0;
      FormBlock;
      output OutStr$ + " (Sync phase)";
    end else begin
      GsyncSpeeds = 290; GsyncSpeeds@ = Maxreal;
      Formblock;
      Output Outstr$ + " (Cancel spindles sync)";
    end;
  end;
end
```

## Access from .NET

Handler:

```csharp
public override void OnSyncAxes(ICLDSyncAxesCommand cmd, CLDArray cld)
```

Inheritance: `ICLDSyncAxesCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd["..."]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

| Member | Type | Description |
|---|---|---|
| `cmd.IsOn` | `bool` | Contains "true" if the command enables a mode of synchronous movement, otherwise it is "false". |
| `cmd.IsOff` | `bool` | Contains "true" if the command disables a mode of synchronous movement, otherwise it is "false". |
| `cmd.FirstAxisID` | `string` | Textual axis identifier for the first of the machine axes between which synchronization is performed. |
| `cmd.SecondAxisID` | `string` | Textual axis identifier for the second of the machine axes between which synchronization is performed. |

Example - `OnSyncAxes` (from the Goodway SW postprocessor):

```csharp
public override void OnSyncAxes(ICLDSyncAxesCommand cmd, CLDArray cld)
{
    if (SameText(CurrentOperation.TypeName, "TSTTakeoverMTM")) return;

    base.OnSyncAxes(cmd, cld);
    if (cmd.FirstAxisID.Contains("AxisC1") || cmd.FirstAxisID.Contains("AxisC2")){
        SyncSpindles(cmd.IsOn,false);
    }else
    if (cmd.FirstAxisID.Contains("AxisZ1") || cmd.FirstAxisID.Contains("AxisZ2")){
        SyncZ(cmd.IsOn, false);
    }else{
        Log.Error("Axes can not be syncronized: ("+cmd.FirstAxisID+","+cmd.SecondAxisID+")");      
    }
}
```

## See also
- [CLData access model](../cldata.md)
