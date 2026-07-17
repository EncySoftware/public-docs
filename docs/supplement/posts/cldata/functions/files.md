# CLData files (CLDFile operator)

A CAM project's CLData is split into files - one per technological operation, plus NC-subroutine files and the project-level file. A postprocessor can reach any command of any file (not only the current one) to look ahead, gather tool lists, and so on. sppx does this with the **CLDFile** operator; .NET with the `ICLDProject.CLDFiles` list of `ICLDFile` objects.

## Access from sppx

The **CldFile** operator is intended to obtain access to CLData files data from the postprocessor code. It provides information only for reading, ie can only be to the right of the assignment operator. Syntax:

- `CldFile.FileCount` - returns the number of CLData loaded files;
- `CldFile.CurrentFile` - index of the current CLData file (CLData files are indexes starting with number 0);
- `CldFile.FirstEnabledFile` - index of the first CLD-file (operation) that is enabled in the list on the CLData tab;
- `CldFile.LastEnabledFile` - index of the last CLD-file (operation) that is enabled in the list on the CLData tab;
- `CldFile.CurrentCmd` - index of the current CLData command in the current CLData file (1 based indices);
- `CldFile[<FileIndex>].Enabled` - returns 1 when the file number **FileIndex** is enabled, 0 - file is disabled;
- `CldFile[<FileIndex>].FileType` - returns the type of the CLData file: 0 - technological operation, 1 - NC-subroutine, 2 - CAM project settings;
- `CldFile[<FileIndex>].IsNCSub` - returns 1 when the file is a file of NC-subprogram, 0 - when file is not NC-subprogram;
- `CldFile[<FileIndex>].CmdCount` - number of commands in the CLData file number **FileIndex**;
- `CldFile[<FileIndex>].Cmd[<CmdIndex>]` - returns a reference to the CLData command numbered **CmdIndex** in a file with an index **FileIndex**. After this command through a point is acceptable to specify any of the instructions defined for the operator [Cmd](current-command.md). For example: `CldFile[<FileIndex>].Cmd[<CmdIndex>].Code` - code of the CLData command with number **CmdIndex**;
- `CldFile[<FileIndex>].Cmd[<CmdIndex>].Data` - returns a string data of the CLData command with number **CmdIndex** (for example, a comment line). If the command does not contain string data, then returns its string representation.
- `CldFile[<FileIndex>].Cmd[<CmdIndex>].Data[<CldIndex>]` - value of CLD array item with number **CldIndex**.
- `CldFile[<FileIndex>].Cmd[<CmdIndex>].Name` - the CLData command or CLData command parameter name;
- `CldFile[<FileIndex>].Cmd[<CmdIndex>].Str |.Int |.Flt |.Ptr` - value of the command parameter by its name in appropriate form; see [Named CLData parameters](named-parameters.md) topic for more information

The example below prints out numbers and comments of all tools used in the program.

```pascal
sub PrintAllTools
  i: Integer
  j: Integer
  for i = 0 to CLDFile.FileCount-1 do begin
    if (CldFile[i].Enabled>0) and (CldFile[i].IsNCSub=0) then begin
      for j = 1 to CldFile[i].CmdCount do begin
        ! If the given command is "LoadTl"
        if CldFile[i].Cmd[j].Code = CodeOfCmd("LoadTl") then begin
          ! Print the turret head identiefer
          Print "RevolverID = " + CldFile[i].Cmd[j].Str["RevolverID"]
          ! Print the tool number
          Print "Tool number = ", CldFile[i].Cmd[j].Data[1]
          ! Print the tool comment
          if CldFile[i].Cmd[j+1].Code = CodeOfCmd("Comment") then
            Print "Tool comment: " + CldFile[i].Cmd[j+1].Data
        end
      end
    end
  end
subend
```

## Access from .NET

The list of files is reached from the [project](project.md) object as `CLDProject.CLDFiles` (an `ICLDFileList`); the current file is available directly as `CurrentFile`. Each element is an `ICLDFile`. Note that the file-command index in .NET is **0-based** (`[0..CmdCount-1]`), whereas the sppx `CLDFile[f].Cmd[c]` command index is 1-based.

`ICLDFileList`:

| sppx | .NET | Description |
|---|---|---|
| `CldFile.FileCount` | `CLDProject.CLDFiles.FileCount` | number of loaded files |
| `CldFile[f]` | `CLDProject.CLDFiles[f]` | the file with index `f` |
| `CldFile.CurrentFile` | `CurrentFile` | the file being postprocessed |

`ICLDFile`:

| sppx | .NET | Description |
|---|---|---|
| `CldFile[f].CmdCount` | `file.CmdCount` | number of commands in the file |
| `CldFile[f].Cmd[c]` | `file.Cmd[c]` / `file[c]` | the command with index `c` (0-based) |
| `CldFile[f].Cmd[c].Code` | `file.GetCommandType(c)` | the type of the command with index `c` (`CLDCmdType`) |
| `CldFile[f].Enabled` | `file.Enabled` | whether the file is postprocessed |
| `CldFile[f].FileType` | `file.FileType` | the file type (`CLDFileType.TechOperation` / `NCSub` / `CAMProject`) |
| `CldFile[f].IsNCSub` | `file.FileType == CLDFileType.NCSub` | whether the file is an NC-subroutine |
| - | `file.Caption` / `file.ID` | a short description / the unique identifier of the file |
| - | `file.Index` | the file's index in the project |
| - | `file.Project` | the project the file belongs to |
| - | `file.IndexOfCmd(type, from, to)` | index of the first command of a type in a range (`-1` if none) |
| - | `file.IndexOfCmdName(name, from, to)` | the same, by the type name |
| - | `file.FindCommand(type, from[, to])` | the first command of a type in a range (`null` if none) |

The same "print all tools" scan in .NET:

```csharp
foreach... // over CLDProject.CLDFiles
for (int f = 0; f < CLDProject.CLDFiles.FileCount; f++) {
    ICLDFile file = CLDProject.CLDFiles[f];
    if (!file.Enabled || file.FileType == CLDFileType.NCSub)
        continue;
    for (int c = 0; c < file.CmdCount; c++) {
        ICLDCommand command = file.Cmd[c];
        if (command.CmdType == CLDCmdType.LoadTl) {
            nc.OutWithN("RevolverID = " + command.Str["RevolverID"]);
            nc.OutWithN("Tool number = " + command.CLD[1]);
            ICLDCommand next = file.Cmd[c + 1];
            if (next != null && next.CmdType == CLDCmdType.Comment)
                nc.OutWithN("Tool comment: " + next.CLDataS);
        }
    }
}
```

## See also

- [Named CLData parameters](named-parameters.md)
- [Current command (Cmd operator)](current-command.md)
- [Browsing CLData commands](browsing.md)
- [Project information (Project operator)](project.md)
- [CLData access functions and operators](functions.md)
