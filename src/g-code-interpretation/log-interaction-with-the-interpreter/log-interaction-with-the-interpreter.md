# Interpreter interaction log

The process of interpreting the NC program text, including the interaction with the interpreter, is recorded to the log when a separate log option is on. The log is managed in the **System setup** window: &lt;[Additional](https://docs.encycam.com/ENCY/3/en/23.html)&gt; page, &lt;**Logs**&gt; group, &lt;**Use logs**&gt; and &lt;**Use log interaction with the interpreter**&gt; options. The second option is available only when the first one is on. In ENCY Tuner the log is turned on in the same way.

If both options are on, the interpretation of the NC program text is recorded in the log for calculations in the “[Simulation of machining by NC program](https://docs.encycam.com/ENCY/3/en/10291.html)” mode and for calculations of “[G-code based operations](https://docs.encycam.com/ENCY/3/en/10379.html)”: the kernel's messages about the words read and the lines the interpreter writes.

The log is kept in one file per running program process: all calculations made while the program runs are written to this file. File location:

- ENCY - `%APPDATA%\ENCY Software\ENCY\Version 3\Log\ency-<process ID>.log`;
- ENCY Tuner - `%APPDATA%\ENCY Software\ENCY Tuner\Version 3\Log\ltuner-<process ID>.log`.

When the log file exceeds 20 MB, its previous content is moved to the `RotatedLogs` subfolder, and writing continues to a file with the same name.

The log is intended for [creating your own interpreters](../../../index.md).
