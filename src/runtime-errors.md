# Errors at run time

The compiler finds errors in the text of a script before it runs: unknown names, incompatible
types, wrong syntax. Other errors appear only while the script runs, for example integer division
by zero or a call of a missing library function. They are reported by the virtual machine.

## Error messages

A run-time error message contains the text of the error and, after a semicolon, details:

```text
SVMERROR: mathematics operation failed; Division by zero
```

Messages that a script most often causes:

| Message | Cause |
|---|---|
| `mathematics operation failed` | Integer division by zero with `div` or `mod` |
| `incompatible types` | A value of a type the operation does not accept, for example a string as the selector of `case` |
| `illegal string` | `integer_num` or `float_num` got a string that is not a number |
| `illegal address; null pointer access` | A field of an object variable that holds `nil` |
| `library not found` | The library of an [external routine](external-routines.md) is not found; reported when the script starts |
| `entry-point missing` | The library has no function with the name given in `external` |
| `external call failed` | A method of a system class or an external routine failed, for example reading a file that is still open for writing |

After most errors the script goes on with the next statement; the result of the failed operation is
not defined. A critical error, for example a stack error, stops the script. When the script runs in
the debugger, the error message lets you stop it.

A script should check the data that may cause an error instead of relying on the error: compare the
divisor with zero, check `file_exists` before reading a file, compare an object variable with `nil`.

## Turning off the error reports

The variable `error_level` of the [system module](system-module.md) controls the reports:

- `el_default` — errors are reported (the initial value);
- `el_no_report` — errors are not reported.

```pascal
error_level = el_no_report
count = integer_num(text)     // a wrong text gives 0 without a message
error_level = el_default
```

Turn the reports back on right after the statements whose errors you expect: other errors would
otherwise pass unnoticed.
