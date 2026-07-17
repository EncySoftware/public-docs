# Browsing CLData commands

Besides the current command, a postprocessor can look at other commands of the file - read the code of the current or the following command, look ahead for a command of a given type, or walk the whole file. sppx offers a set of dedicated functions for this; .NET does the same through the navigation members of `ICLDCommand` and the [CLDFile](files.md) object. Command codes/types are the common thread: sppx identifies a command type by a numeric **code** (obtained from a name with `CodeOfCmd`), .NET by the `CLDCmdType` enumeration.

## Access from sppx

### CurCode function

**CurCode** function returns the code of the current CLData command. Each CLData command has a unique numerical identifier - code. CLData command codes are listed in the [technology commands description](../commands/commands.md). Example of a function inside the command handler CIRCLE below.

```pascal
program Circle
  Print CurCode
end
```

As a result of the program in debug window output the number 15000.

The code of a following CLData command can be obtained with [NextCode](#nextcode-function) function. For the code of arbitrary commands on its textual name should use the [CodeOfCmd](#codeofcmd-function) function.

### NextCode function

The **NextCode** function returns the code of technological command, which is located immediately after the current command. Each CLData command has a unique numerical identifier - code. CLData command codes are listed in the [technology commands description](../commands/commands.md). The code of a current CLData command can be obtained with [CurCode](#curcode-function) function. For the code of arbitrary commands on its textual name should use the [CodeOfCmd](#codeofcmd-function) function.

```pascal
if NextCode=CodeOfCmd("Fini") then
Output "M02"
```

### CodeOfCmd function

`CodeOfCmd(CommandName: String)` returns the code of CLData command, which name is passed as a parameter. Each CLData command has a unique numerical identifier - code. CLData command codes are listed in the [technology commands description](../commands/commands.md). The function has the following format.

```text
CodeOfCmd(CommandName: String): Integer
```

CommandName - text name of the command. It must be one of the command names that can be seen in the CLData list on the left side of the main window. The returned value can be used with operators like [CurCode](#curcode-function), [NextCode](#nextcode-function), [GetCLD](#getcld-function), `CLDFile[i].Cmd[j].Code` (see the [CLDFile operator](files.md)).

```pascal
if NextCode=CodeOfCmd("Fini") then
Output "M02"
```

### CLDCounter function

**CLDCounter** function returns the number of the current technology command in the technology command list file. For flexible access to arbitrary CLData command on its index in the file you can use the [CLDFile](files.md) operator.

### GetCLD function

Use the **GetCLD** operator to browse CLData commands in the order they appear in the file. Browsing is possible only in forward direction. Syntax:

```text
{CldCode =} GetCLD(i: Integer; a: Array of Real)
```

Here:

- **CldCode** - **GetCLD** optionally returns the code of retrieved CLData command.
- **i** - relative index of the queried CLData command:
  - 0 - current command,
  - 1 - next command,
  - 2 - second command from the current and so on.

- **a** - a dynamic array of real, that will receive the data of the retrieved CLData command. It must be defined before the operator call.

For example, suppose the CLDATA commands list is as the following and suppose the current command is number 9:

```text
5: CUTCOM ON(71),LENGTH(9) 2,X 0,Y 0,Z 0,N 0,K 0,M 0,LEFT(8)
6: RAPID N 10000
7: GOTO.abs X 134.533,Y 99.684,Z 80
8: RAPID N 10000
9: GOTO.abs X 134.533,Y 99.684,Z 74.400
10: FEDRAT N 50,K 4,MMPM(315)
11: GOTO.abs X 134.533,Y 99.684,Z 73.400
12: FEDRAT N 200,K 0,MMPM(315)
13: PLANE XY(33)
```

The technology command [GOTO.abs](../commands/goto.md) program is the following:

```pascal
program AbsMov
  a: Array of Real ! The array must be defined beforehand
  c: Integer ! This variable will receive the operation code
  c = GetCld(1, a) ! Retrieving the next command data
  if c = CodeOfCmd("FEDRAT") then
    ! Output the value of the first item of CLD array of
  Print "FEDRAT.CLD[1]=", Str(a[1]) ! the next command
end
```

The result of the program execution will be:

```text
FEDRAT.CLD[1]=50.
```

To get access to the parameters of arbitrary technological command can also use the [CLDFile](files.md) operator.

### GetCLDStr function

**GetCLDStr** returns a string representation of current CLData command with it's parameters similar to that displayed in the [textual representation CLData window](../../sppx/common-organization-of-the-work/main-window/work-with-the-files-of-technological-commands.md).

For example, inside the command handler AbsMov function can return a string like the following.

```text
GOTO.abs X 134.533, Y 99.684, Z 80
```

### FindCld function

Use the **FindCld** function to locate command named **CmdName** in the current CLData file. **StartIndex** parameter defines the first scanned command. **StartIndex** is relative to the first command in the current CLData file. If **StartIndex** parameter is omitted, then operator will scan commands starting with the command immediately following the current. The returned value is the index of the found command. When no command was found operator returns -1. The **Data** parameter must be a declared array of real. **Data** will receive the values from the found command's CLData array. Syntax:

```text
N = FindCld({<StartIndex>, }<CmdName>, <Data>)
```

For example, suppose the following CLDATA and suppose the current command number is 0.

```text
0: PARTNO "Bottle"
1: PPFUN …..
2: COMMENT "Roughing Waterline"
3: LOADTL N 2,X 0,Y 0,Z 0,D 8….
4: SPINDL ON(71),NO 397.887,K 0,MODE RPM(0)
5: CUTCOM ON(71),LENGTH(9) 2,X 0,Y 0,Z 0,N 0,K 0,M 0,LEFT(8)
6: RAPID N 10000
7: GOTO.abs X 134.533,Y 99.684,Z 80
8: RAPID N 10000
```

[PartNo](../commands/partno.md) program is the following:

```pascal
program PartNo
  V: Array of Real
  NCircle: Integer
  NGoto: Integer
  NCircle = FindCld("CIRCLE", V)
  NGoto = FindCld("GOTO.abs", V)
  if NGoto > NCircle then
    Print "The first movement is an arc"
  else
    Print "The first movement a cut"
End
```

In result of program execution the message "The first movement a cut" will be print out.

To get access to the parameters of arbitrary technological command can also use the [CLDFile](files.md) operator.

### GFindCld function

The **GFindCld** function is similar to the [FindCLD](#findcld-function) function, but it is looking for a command named **CmdName** in all of CLData files. **StartIndex** parameter defines the first scanned command. **StartIndex** is relative to the first command in the first CLData file. If **StartIndex** parameter is omitted, then operator will scan commands starting with the command immediately following the current. The returned value is the index of the found command. When no command is found operator returns -1. The **Data** parameter must be a declared array of real. **Data** will receive the values from the found command's CLData array. Syntax:

```text
N = GFindCld({<StartIndex>, }<CmdName>, <Data>)
```

To get access to the parameters of arbitrary technological command can also use the [CLDFile](files.md) operator.

## Access from .NET

.NET does not have the sppx browsing functions; instead each command (`ICLDCommand`) knows its neighbours and can search from itself, and the [CLDFile](files.md) object searches within a file. Command types are given by the `CLDCmdType` enumeration rather than by a numeric code obtained from a name.

| sppx | .NET | Description |
|---|---|---|
| `CurCode` | `cmd.CmdTypeCode` / `cmd.CmdType` | type code / type of the current command |
| `CLDCounter` | `cmd.Index` | index of the current command in its file |
| `CodeOfCmd("NAME")` | `CLDCmdType.Name` | a command type - a named enum value instead of a looked-up code |
| `GetCLD(0, a)` / `GetCLD(1, a)` | `cmd` / `cmd.Next` | the current / the next command (`cmd.Prev` for the previous) |
| - | `cmd.NextMotion` / `cmd.PrevMotion` | the next / previous motion command |
| `NextCode` | `cmd.Next?.CmdType` | type of the following command |
| `FindCld(name, data)` | `cmd.FindNextCommand(type[, offset[, count]])` | find the next command of a type in the same file |
| `GFindCld(name, data)` | `cmd.FindNextCommandOfProject(type[, ...])` | find the next command of a type across all files |
| `GetCLDStr` | `cmd.CLDataS` | the textual representation of the command |

`cmd.Next` / `Prev` return `null` past the ends of the file; the `FindNext...` methods return `null` when nothing is found. The `CLData` array of a found command is read through its `CLD` member (see [CLD array](cld-array.md)), so no separate output array argument is needed.

```csharp
// sppx: if NextCode = CodeOfCmd("Fini") then Output "M02"
if (cmd.Next != null && cmd.Next.CmdType == CLDCmdType.Fini)
    nc.OutWithN("M02");

// sppx: NGoto = FindCld("GOTO.abs", V)
ICLDCommand goto = cmd.FindNextCommand(CLDCmdType.Goto);
if (goto != null) {
    double firstParam = goto.CLD[1];
    // ...
}
```

To reach an arbitrary command by index, or to scan a whole file or project, use the [CLDFile / project](files.md) objects (`FindCommand`, `IndexOfCmd`).

## See also

- [Current command (Cmd operator)](current-command.md)
- [CLData files (CLDFile operator)](files.md)
- [CLData access functions and operators](functions.md)
