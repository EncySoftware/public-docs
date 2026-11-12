# PPRINT - Postprocessor printing

## Command caption

How the command appears in the CLData command list:

```text
PPRINT "..."
```

**PPRINT** command passes text information from CAM system to postprocessor. The text of technology command is put into the CLDATA$ predefined variable, after that the text can be printed out into the operator window as a comment explaining postprocessor operation.

## Toolpath tags

Besides free-form text, **PPRINT** is also used to **tag key points of the toolpath**. Such a tag is a **PPRINT** whose text starts with `#`, followed by the tag type and, optionally, a value:

```text
PPRINT "#KeyPoint: StartCutting"
PPRINT "#Approach:[Rule 1]=C; Z10; X; Z"
PPRINT "#Return:[Rule 1]=Z10; X; Z; C"
```

The CAM system inserts these tags to annotate the toolpath - for example the start of cutting, and the rule that produced the approach or return move. A postprocessor can recognize a tag by the leading `#`, react to it if needed, or simply skip it so the marker does not reach the NC program. See [The structure of a CLData listing](../cldata.md) for where these tags appear inside a real operation.

## Access from sppx

Handler: `program PPrint`

Example (from the Fanuc (30i)_Mill postprocessor):

```pascal
program PPrint
  print cldata$
end
```

## Access from .NET

Handler:

```csharp
public override void OnPrint(ICLDPrintCommand cmd, CLDArray cld)
```

Inheritance: `ICLDPrintCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd["..."]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

| Member | Type | Description |
|---|---|---|
| `cmd.Text` | `string` | Arbitrary text information transmitted from CAM. |

Example:

```csharp
public override void OnPrint(ICLDPrintCommand cmd, CLDArray cld)
{
    nc.OutWithN("(" + cmd.Text + ")");   // pass the CAM text into the NC program (here - as a comment)
}
```

## See also
- [CLData access model](../cldata.md)
