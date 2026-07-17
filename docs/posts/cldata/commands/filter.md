# Filter - Output filter (global handler)

> **Not a CLData command.** `Filter` is a global handler called on **every** NC-program line, whatever CLData command (or any other code) produced it. It is listed here so that all postprocessor handlers can be found in one place and in a common style.

## Access from sppx

All postprocessors include the predefined subprogram **Filter**, which can be found in the subprograms list. **Filter** is called immediately after the NC-program block was formed and before it is added to the NC-program text. Thus, this subprogram allows the user to edit every NC-program block at the moment of its output. For example, it is possible to replace symbols or add marks at the end or at the beginning of a line.

By default the system creates the following subprogram prototype for the **Filter**:

```pascal
sub Filter(S: string)
subend
```

The formed NC-block is passed through the **S** parameter. All changes to that string will be put into the NC-program text.

Example:

```pascal
sub Filter(S: String)
  replace(S,"R1","L") ! Replace "R1" with "L"
  replace(S,"R-1","R") ! Replace "R-1" with "R"
  replace(S,"F0","FMAX") ! Replace "F0" with "FMAX"
subend
```

Executing this code for the block "17 L Z-10 R0 F0" will result with the line of NC-program "17 L Z-10 R0 FMAX".

## Access from .NET

The .NET counterpart is the `OnFilterString` handler:

```csharp
public override void OnFilterString(ref string s, TNCFile ncFile, INCLabel label)
```

The line is passed by reference in `s` - modify it in place. `ncFile` is the target NC file, `label` the current label.

Example (from the Goodway SW postprocessor):

```csharp
public override void OnFilterString(ref string s, TNCFile ncFile, INCLabel label)
{
    SynchPoints.CheckForOutput(s);
    if ((ncFile is NCFile ncx) && (ncx.NeedSlash) && (!String.IsNullOrEmpty(s)))
        s= "/"+s;
}
```

## See also
- [CLData access model](../cldata.md)
