# SELWORKPIECE - Active workpiece connector selection

## Command caption

How the command appears in the CLData command list:

```text
SELWORKPIECE WorkpieceConnectorID
```

Use the **SELWORKPIECE** command to specify active workpiece connector. The workpiece connector is a machine unit that is used to fix the workpiece. For the multi-spindle lathe machines this command specifies the active spindle. For the milling machines the workpiece connector can be the pallet for example. All machining commands will relate to the workpiece fixed in the active connector.

## Access from sppx

Handler: `program SelWorkpiece`

The **SELWORKPIECE** command's single parameter is the string identifier of the workpiece connector. This identifier is defined by the CAM system machine scheme. Parameter value is stored into the CLDATA$ predefined variable. Following is an example of a program processing this command.

```pascal
program SelWorkpiece
  if CLData$="MainSpindle" then
    Output "SETMS(1)" ! Activate the main spindle
  else
    Output "SETMS(2)" ! Activate the counter spindle
end
```

## Access from .NET

Handler:

```csharp
public override void OnSelWorkpiece(ICLDSelWorkpieceCommand cmd, CLDArray cld)
```

Inheritance: `ICLDSelWorkpieceCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd["..."]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

| Member | Type | Description |
|---|---|---|
| `cmd.ConnectorID` | `string` | Textual workpiece connector identifier (as it defined inside machine schema). |

Example:

```csharp
public override void OnSelWorkpiece(ICLDSelWorkpieceCommand cmd, CLDArray cld)
{
    activeWorkpieceConnector = cmd.ConnectorID;   // remember which workpiece connector the following commands refer to
}
```

## See also
- [CLData access model](../cldata.md)
