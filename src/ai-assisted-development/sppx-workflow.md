# SPPX workflow

An SPPX postprocessor is a set of **handlers** — one per CLData command — plus subroutines, objects and registers, written in the built-in Pascal-like language, with output formatting described by masks. The assistant works on exactly these items through the InP MCP server, and the cycle is always the same: read, change, compile, run, compare.

For the language and the mask reference, see the Postprocessors generator documentation; for the meaning of the input commands, see the [CLData reference](../cldata/cldata.md).

## The cycle

1. **Prepare.** Work from the closest postprocessor that already exists — the one in use for this machine, or a distributed one for a similar control system — rather than from an empty file. Copy it, or commit the current state, so the comparison has a baseline. Generate the NC program once before any change and keep it.
2. **Find the data.** Identify the CLData command behind the NC blocks you want to change, and read its actual parameters from the test project. The command name alone is not enough: the same command carries different values in different projects.
3. **Find the handler.** The postprocessor structure lists handlers, subroutines and objects. The handler named after the command is where processing starts, but the output may be produced further down — in a subroutine, a mask, or on the next modal state change.
4. **Read before writing.** The assistant must read the current source of the item it is about to change, and the register definitions if registers are involved. Editing what it has not read is how unrelated code disappears.
5. **Change the minimum.** Preserve register order and formatting, modal behaviour, separators, the state kept in `Common` and local variables, and the existing subprogram conventions. Adapted donor code from another postprocessor has to be checked against this project's data, not pasted.
6. **Compile.** Every reported error must be fixed before going further; there is no point in running a postprocessor that did not compile.
7. **Run.** Interpret the same test project and get the NC program. A change that was never run is not finished, whatever the code looks like.
8. **Compare.** Diff the new NC program against the baseline, then against the reference program from the machine. Trace every difference to a command and a handler — including differences you did not expect.
9. **Verify.** Continue with [Review and verify](review-and-verify.md).

## What the assistant can and cannot change

There is one handler per CLData command: handlers can be edited but not created or deleted. Subroutines and objects can be created. Deleting an item is irreversible, so the assistant asks first — read the request before you confirm.

## Watching it work

Ask for a **windowed** InP instance when you want to see the IDE: the handler it edited, the compile messages and the generated program are in front of you. A **headless** instance is for batch checks and parallel runs — nothing appears on screen. With several InP windows open, tell it which one to work in.

In VS Code you can also ask it to open the changed handler in the editor, or to prepare a **Generate NC** run so you see the panel, the parameters and the diffs yourself.

## What to check in the code

Register formatting and modal output are where AI-drafted handlers usually go wrong: a value written unconditionally instead of on change, a modal register left set, an axis word emitted with the wrong sign or in the wrong order. Review every conditional branch and every direct output statement, and test the values the fixture does not contain — omitted parameters, repeated commands, boundary and maximum values, and the transitions at program start and end.

Do not let .NET property names appear in SPPX code. The two subsystems read the same data with different syntax: the CLData pages describe the meaning, the SPPX pages describe the access form, and index bases differ between them.
