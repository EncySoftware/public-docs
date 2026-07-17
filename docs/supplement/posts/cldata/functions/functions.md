# CLData access functions and operators

The postprocessor generator's programming language implements several functions, variables and operators that provide information about the contents of CLData. The idea is the same in sppx and in .NET, but the concrete primitives differ, so each topic below documents the sppx form and the .NET form side by side - the parameters of the current command, the other commands of the file, and the project-level data - and points out where one subsystem has no direct counterpart.

For the overall picture of how a postprocessor reaches CLData (the command model, the current command, the `cld` array) see the [CLData access model](../cldata.md).

## In this section

- [Named CLData parameters](named-parameters.md) - the common named-parameter model (`Str` / `Int` / `Flt` / `Ptr` access by a dotted/bracketed name); shared by the command, file and project accessors.
- [CLD predefined array](cld-array.md) - the numeric parameter array of the current command (`CLD[i]` / `CLD.Name` in sppx, `CLDArray` in .NET).
- [Current command (Cmd operator)](current-command.md) - reading the code, name, data and named parameters of the current command, including parameters addressed by a unique code.
- [Browsing CLData commands](browsing.md) - looking at other commands of the file (look ahead/back, find the next command of a given type, command codes).
- [CLData files (CLDFile operator)](files.md) - access to any command of any loaded CLData file.
- [Project information (Project operator)](project.md) - access to the CAM project-level data embedded in CLData.
- [GMA array](gma.md) - the sppx convenience array for processing multi-axis [MULTIGOTO](../commands/multigoto.md) movements.

## See also

- [CLData access model](../cldata.md)
- [Technology commands description](../commands/commands.md)
- [Project information in CLData](../project-information.md)
