# TAKEOVER - Workpiece takeover

## Command caption

How the command appears in the CLData command list:

```text
TAKEOVER WorkpieceConnectorID
```

Use **TAKEOVER** command to take workpiece over from the active connector into the connector specified in the command parameter. The active workpiece connector is specified by the [SELWORKPIECE](selworkpiece.md) command. The workpiece connector is a machine unit that is used to fix the workpiece. Use this command for multi-spindle lathe or lathe-milling machines to perform workpiece takeover from one spindle into another.

## Access from sppx

Handler: `program Takeover`

The **TAKEOVER** command's single parameter is the string identifier of the workpiece connector. This identifier is defined by the CAM system machine scheme. Parameter value is stored into the CLDATA$ predefined variable.

Example:

```pascal
program Takeover
  ! CLDATA$ - target workpiece connector identifier
  Output "( TAKEOVER TO " + CLDATA$ + " )"
end
```

## Access from .NET

Handler:

```csharp
public override void OnTakeover(ICLDTakeoverCommand cmd, CLDArray cld)
```

Inheritance: `ICLDTakeoverCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd["..."]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

| Member | Type | Description |
|---|---|---|
| `cmd.TargetConnectorID` | `string` | Textual identifier of the workpiece connector. This identifier is defined by the machine schema. |

Example:

```csharp
public override void OnTakeover(ICLDTakeoverCommand cmd, CLDArray cld)
{
    nc.OutWithN("( TAKEOVER TO " + cmd.TargetConnectorID + " )");   // hand the workpiece to the target workpiece connector
}
```

## See also
- [CLData access model](../cldata.md)
