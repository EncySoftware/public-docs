# Troubleshooting

## The assistant does not see the skills

Ask which skills it has now. If the six interpreter skills are not among them, check that the skill folders are in the folder your client actually reads, that each of them contains a `SKILL.md` file, and that the client has picked them up: Claude Code sees new skills at once, or after the `/reload-skills` command if there was no skills folder before copying; Kilo Code — in a new session or after the `/reload` command; other clients — according to their documentation, often only after a restart. Where each client looks for skills — see [advanced setup](advanced-setup.md#skills-in-different-ai-clients).

## The assistant answers from memory instead of the programs

This happens when the request names no files or when the answer is not required to refer to the data. Name the programs and the manual explicitly, ask which file and which block it took the word from, and ask it to follow the skills — they require reading the programs first.

## The assistant reports success without running anything

A build is not a result. Ask which programs were run, where the log of that run is, and how the result differs from the previous one. If there is none of this, the state is **Not verified**, see [Checking and confirming the result](review-and-verify.md).

## The interpreter does not load

First read which **Interpreter file** is selected on the **Strategy** tab of the operation parameters, and the CAM system log. If the interpreter is not loaded, every word of the program will be an error.

The CAM system describes any failure to load a C# interpreter the same way — with the message "External library don't support NCT interface:" followed by the path to the library; a native library without the required exports gets the same message. The real cause does not get into the message. Most often it is one of these:

- the library named in the `*.snci` file, or its dependencies, is not next to that file;
- the library is built for a different .NET version than this product version needs;
- an exception occurred when the interpreter object was created — usually when the registers were created.

Ask the assistant to check the files and to create the interpreter object in a small console program with the same SDK package — this shows the real error message.

For a native interpreter, check the bitness of the library, the export of `NCT_GetInterface` and `NCT_FreeMemory`, and that `GetIdentifier` matches `LibraryID` — see [Native interpreter workflow](native-workflow.md).

## Two interpreters get mixed up

The CAM system tells interpreters apart by the identifiers in the `*.snci` file. A copied interpreter with the same `LibraryID` and `ID` is indistinguishable from the original: sometimes one simulates, sometimes the other. Give the copy new identifiers.

## A breakpoint is not hit

Check in order: there is a `*.pdb` file next to the library (a build without debug information makes any breakpoint "dead"); the operation uses your interpreter; the build before the launch succeeded — open the terminal panel and read its result; the CAM system was given the `*.snci` file from the folder of the version you started.

## Settings from InterpreterSettings.ini have no effect

The templates have known errors in reading `InterpreterSettings.ini`: the file may not be read at all, and the log contains only an information line starting with `Error reading settings file`. A log filtered by errors will not show it. Ask the assistant to check the template the interpreter was created from — the `develop-dotnet-interpreter` skill lists these errors and their fixes.

## An axis is simulated in the wrong place or not at all

The SDK package helper that the .NET templates use to find the machine axes warns about an unknown axis name once and then silently skips its values. Check that the axis name in the program matches the axis address in the machine schema, and that the name mapping works for all spellings from the word list: `B90`, `B=90`, `B1=90`.

## The second channel moves the axes of the first or is not simulated

The interpreter must move the axes the CAM system gives it for the channel of its program: for the second channel, for example, `X2`, `Y2`, `Z2`. If the second channel moves the axes of the first, or its tool path shrinks to a point, compare these axes with the axes the interpreter passes to its motion commands. A mismatch is a defect of the interpreter or of its `*.snci` file, not of the CAM system.

Check the synchronization of channels in the CAM system: depending on its version and license, ENCY Tuner may simulate the channels one after another instead of at the same time, and then the wait points hold nothing back.

## Empty tool path without an error

Common causes:

- the program lacks the header the postprocessor outputs it with: a test program made only of the blocks being checked may produce no movement at all — build it from the header of a real program of the same operation;
- the parent interpreter is intended only for importing a tool path (in the [list of interpreters](../appendix/list-of-interpreters/list-of-interpreters.md) such interpreters are marked "Tool path import only");
- the axis name in the program does not match the axis address in the machine schema (see the section above);
- a protected interpreter did not receive its protection data — for example, it was started from an ordinary folder instead of the container — and is written so that it then silently simulates nothing. See [Protected interpreters](../interpreter-structure/protected-interpreters/protected-interpreters.md).

## The result differs from what another product version gives

Each version of the CAM system and ENCY Tuner has its own .NET version and its own version of the SDK package (see [Product versions](dotnet-workflow.md#product-versions)). Check which product version the run was in and which one the library was built for — see [Several product versions on one computer](advanced-setup.md#several-product-versions-on-one-computer).

## The documentation the assistant reads is out of date

A local copy is a snapshot: download the archive again when a new version is released, and record which version a decision is based on. Version-dependent details — the SDK package version, interface names — check against the installed product, not against the copy.
