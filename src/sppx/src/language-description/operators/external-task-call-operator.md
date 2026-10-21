# External task call operator



Use **ShellExec** operator to execute a shell command or to call an external task.

**Syntax**

```
ShellExec CommandLine$
```

**Description**

`CommandLine$` – string expression.

Then executing this operator Postprocessor will run the operating system shell command interpreter (CMD.EXE) and pass it the `CommandLine$` as command (this operator is effectively executing "cmd /c CommandLine$"). Note that the console window is not displayed.

**Example**

```
! OS command execution
ShellExec "erase temp\*.*" ! Clear the temp folder
```
