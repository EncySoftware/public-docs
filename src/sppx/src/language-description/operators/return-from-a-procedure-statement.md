# The RETURN from a procedure statement

It is used to declare the end of procedure.

**Format**

```
RETURN
```

**Description**

This statement is the last statement of a procedure. While the execution of the **RETURN** statement the back assignment of the formal parameters to the variables defined in the call statement is executed and start the execution of the next after the call statement.

**Example**

```
program TestProc
  NErr: Integer
  S: String
  proc PrintDebugInfo(NErr, S)
    case NErr of
      1: Print "Interpolation error: ", S
      2: Print "Approximation error: ", S
      else Print "Unknown error: ", S
    end
  return
  PrintDebugInfo(CLD[1], "parameter 1")
  PrintDebugInfo(CLD[2], "parameter 2")
  PrintDebugInfo(CLD[3], "parameter 3")
end
```

**See also**

[The statement of the procedure start **PROC**](statement-of-the-procedure-start-proc.md)
