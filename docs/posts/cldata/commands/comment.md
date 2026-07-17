# COMMENT - Commentaries

## Command caption

How the command appears in the CLData command list:

```text
COMMENT "........"
```

**COMMENT** outputs comments line into the NC-program. The comment is put into CLDATA$ variable. Comments can be transliterated.

## Access from sppx

Handler: `program Comment`

Example (from the Fanuc (30i)_Mill postprocessor):

```pascal
program Comment
  if CLDATA$<>"" then begin
    if pos("@", CLDATA$) = 1  then begin
      CLDATA$ = ""!Copy(CLDATA$, 2, Len(CLDATA$))
    end
    if CLDATA$<>"" then
      Output "( "+CLDATA$+" )"
  end
end
```

## Access from .NET

Handler:

```csharp
public override void OnComment(ICLDCommentCommand cmd, CLDArray cld)
```

Inheritance: `ICLDCommentCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd["..."]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

| Member | Type | Description |
|---|---|---|
| `cmd.Text` | `string` | Textual string of a comment. |
| `cmd.UpperCaseText` | `string` | Textual string of a comment in upper case. |
| `cmd.IsOperationName` | `bool` | Returns "true" if this command is a first COMMENT command in a file of operation, that contains the name of this operation. If it's another type of comment, this flag will contain "false". |
| `cmd.IsToolName` | `bool` | Returns "true" if this command is a special COMMENT command that contains the name of the tool. If it's another type of comment, this flag will contain "false". |

Example - `OnComment` (from the Fanuc (30i)_Mill_DN postprocessor):

```csharp
public override void OnComment(ICLDCommentCommand cmd, CLDArray cld)
{
    if (!(cmd.IsOperationName || cmd.IsToolName)) {
        nc.OutWithN("( " + Transliterate(cmd.CLDataS) + " )");
    }
}
```

## See also
- [CLData access model](../cldata.md)
