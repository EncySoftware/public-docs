# INSERT - Insertion

## Command caption

How the command appears in the CLData command list:

```text
INSERT "..."
```

**INSERT** command is used to pass textual information directly into NC-program. The text is put into CLDATA$ variable.

## Access from sppx

Handler: `program Insert`

Example (from the Fanuc (30i)_Mill postprocessor):

```pascal
program Insert
  OutBlock
  FormBlock
  Output OutStr$ + CLData$
end
```

## Access from .NET

Handler:

```csharp
public override void OnInsert(ICLDInsertCommand cmd, CLDArray cld)
```

Inheritance: `ICLDInsertCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd["..."]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

| Member | Type | Description |
|---|---|---|
| `cmd.Text` | `string` | The text to output to the file. |

Example - `OnInsert` (from the Heidenhain_Mill_iTNC530_DN postprocessor):

```csharp
public override void OnInsert(ICLDInsertCommand cmd, CLDArray cld)
{
    nc.WriteLine(cmd.Text);
}
```

## See also
- [CLData access model](../cldata.md)
