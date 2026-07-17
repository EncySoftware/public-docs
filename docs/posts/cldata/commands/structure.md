# STRUCTURE - Toolpath structure

## Command caption

How the command appears in the CLData command list:

```text
STRUCTURE ON(71)|OFF(72), TYPE(Level), Comment(Level: -65)
```

The **STRUCTURE** command allows us to represent a tree structure of CLData commands as a linear list of commands.

## Access from sppx

Handler: `program Structure`

In CAM system toolpath of each operation is represented as a tree, separated into groups and subgroups, within which are placed the usual commands of moving tool, turn on the spindle or feed, etc. Inside the postprocessors generator toolpath is represented as a linear list of commands that is not divided into groups. **STRUCTURE** command intended to preserve the original information as to in what group was originally located CLData command. Each group is converted into two commands: `STRUCTURE ON(71)` and `STRUCTURE OFF(72)`. The first command defines the start of the group, and the second one - the end of the group. All items that are placed inside a group will be located between these two commands. As well as groups can be nested within each other, inside a `STRUCTURE ON(71)`... `STRUCTURE OFF(72)` block can be nested several other blocks `STRUCTURE ON(71)`... `STRUCTURE OFF(72)`.

| Parameter | CLD array | Description |
|---|---|---|
| ON(71)<br>OFF(72) | CLD[1] | Sign that this command is the beginning or the end of the group: ON(71) - command defines the beginning of group, OFF(72) - command defines the end of group. |

Parameters available through the cmd operator

| TCLDStructure: ComplexType | Command that defines the structure |
|---|---|
| IsClose: Integer | cmd.Int["IsClose"] - Sign that this command is the beginning or the end of the group: 0 - command defines the beginning of group, 1 - command defines the end of group. |
| NodeType: String | cmd.Str["NodeType"] - A string that specifies the type of group. For example, Approach - a group of approach movings, Level - a layer of machining, etc. This string is not translated into local languages. |
| Comment: String | cmd.Str["Comment"] - The group name that is displayed in the CAM system's toolpath tree. Can be translated into local languages and contain arbitrary characters. |

Example (from the KUKA robot postprocessor):

```pascal
program Structure
  str1, str2: string
  str1 = Cmd.Str["NodeType"]
!  str2 = Cmd.Str["Comment"]

  if CLD.OnOff=71 and drilling = 10 then begin
    cdis = ""
  end

  if CLD.OnOff=72  and drilling = 10 then begin
    cdis = " C_DIS"
  end

!----------------------------------------------------------------------------

  if CLD.OnOff=71 and drilling=1 and pos("BodySection", str1)>0 then !only for hole machining
    drilling = 10

  if CLD.OnOff=72 and drilling=10 and pos("BodySection", str1)>0 then !only for hole machining
    drilling = 0

end
```

## Access from .NET

Handler:

```csharp
public override void OnStructure(ICLDStructureCommand cmd, CLDArray cld)
```

Inheritance: `ICLDStructureCommand : ICLDCommand`.

Read the parameters from the strongly-typed `cmd` object (**recommended**); the raw `cld[i]` array (same indices as in sppx) and the named `cmd["..."]` helpers are available too. The table lists the command's members, including those inherited from its base interfaces; the common `ICLDCommand` members (navigation, `CLD`, `CLDFile`, `TechOperation`, ...) are described in the [CLData access model](../cldata.md).

| Member | Type | Description |
|---|---|---|
| `cmd.IsOpen` | `bool` | Contains "true" if the command is the start of a new group. Otherwise it contains "false". |
| `cmd.IsClose` | `bool` | Contains "true" if the command is the end of a group. Otherwise it contains "false". |
| `cmd.NodeType` | `string` | Textual attribute that defines the type of a group. There are few standard group types like "Approach", "String", "Level" etc. But it can contain any arbitrary value also. |
| `cmd.Comment` | `string` | Some arbitrary textual commentary or name of the group. |

Example:

```csharp
public override void OnStructure(ICLDStructureCommand cmd, CLDArray cld)
{
    if (cmd.IsOpen)
        nc.OutWithN("(>>> " + cmd.NodeType + ": " + cmd.Comment + ")");   // group start
    else if (cmd.IsClose)
        nc.OutWithN("(<<< " + cmd.NodeType + ")");                        // group end
}
```

## See also
- [CLData access model](../cldata.md)
