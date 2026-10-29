# AI-assisted interpreter development

This page explains how to develop and maintain an interpreter with the help of an AI assistant: what to ask it for, what it needs from you, and how to check the result. It applies to interpreters written in C# from the templates of the CAM system, described in [Developing a custom interpreter in (.NET) C#](../dotnet/developing-a-custom-interpreter-in-net-csharp.md), and to native interpreters written in Delphi or C++ (see [Interpreter library](../interpreter-structure/interpreter-library/interpreter-library.md)).

## What the work looks like

You write in the chat, in your own words:

> Programs for our machine write the swivel axis as B90, but the machine calls it B1. A program with B90 is not simulated. Fix it.

Then you watch. The assistant reads the NC programs and the machine of the project, finds where the interpreter reads axis words, decides whether the difference is a setting or a change in the code, makes the change, builds the interpreter, runs the NC programs through it in the CAM system and shows you what changed in the simulation and in the log.

You read the result and answer the same way — "right, but the same machine also writes B=DC(30)" — and it goes round again.

You do not have to write the code yourself, although you can look at every change and edit it by hand whenever you prefer. What cannot be handed over is the judgement: whether the simulation matches what your machine does is decided by you.

## What the assistant needs from you

- The NC programs the interpreter must read, and the CAM project with the machine they are written for.
- The manual of the controller for the words and cycles in question.
- The installed CAM system or Tuner the interpreter must work in.
- The expected result: what the machine does with the block that is simulated wrongly.

The more real programs you give, the better: the assistant takes the spellings of the words from them, not from memory.

## Skill for the assistant

A skill is an instruction in plain language: what to do, in what order, what to check, and when the work counts as finished. There is no code in it — it is a text file the assistant reads and follows, much like a briefing given to a new colleague. Anyone who can explain a way of working in words can write or correct one.

The skill published with this guide is `interpreter-development` — a single file, [SKILL.md](SKILL.md). It guides the whole work on an interpreter and consists of a general part and five sections:

| Part of the skill | What it is for |
|---|---|
| General part | What to find out first, in what order to work, and when the work is finished |
| Inspect NC programs | Collecting the NC programs, the machine and the manual, and listing every word the programs use |
| Develop native interpreters | A native interpreter library in Delphi or C++: the required functions, registers and their handlers, the SNCI file, the Win64 build, inheritance and protection |
| Develop .NET interpreters | Creating, configuring, building and debugging a C# interpreter from a template |
| How the kernel reads a block | How the CAM system reads a block and when the interpreter's code is called |
| Verify interpretation | Running all NC programs before and after a change, comparing the results, and preparing an interpreter for hand-over |

The assistant receives the whole file and finds the section that fits the task itself. How to add the skill depends on the AI client. Usually a skill is a folder named after it with the `SKILL.md` file inside: in Kilo Code, create the folder `interpreter-development` in `.kilo/skills/` of the project or in `%USERPROFILE%\.kilo\skills\` to have the skill in every project, and put the downloaded file into it; in Claude Code, do the same in `.claude/skills/` of the project or in `%USERPROFILE%\.claude\skills\`; other clients have their own skills folder or configuration entry. If your client has no skill mechanism, paste the content of `SKILL.md` into the chat or reference the file from the client's instruction file (`AGENTS.md`, `CLAUDE.md` and similar).

You can add your own skills alongside it: they are plain Markdown, and the practices your team accumulates — the controllers you support, the variations of your customers' programs — belong in the same form.

## What stays with you

Treat every answer as a draft. The assistant sees only what you gave it: it does not know undocumented behaviour of the controller, and a plausible-looking simulation can be wrong. Before an interpreter is given to a user, run all the NC programs you have through it, read the warnings in the [log](../g-code-interpretation/log-interaction-with-the-interpreter/log-interaction-with-the-interpreter.md), and check the simulation of the blocks that were changed. Do not put passwords, customer archives or data that must not leave your company into the chat.

## Where to read further

- [Developing a custom interpreter in (.NET) C#](../dotnet/developing-a-custom-interpreter-in-net-csharp.md) — creating an interpreter from a template.
- [Interpreter debugging in Visual Studio Code](../dotnet/interpreter-debugging-in-visual-studio-code/interpreter-debugging-in-visual-studio-code.md) — running the interpreter under the debugger.
- [Interpreter library](../interpreter-structure/interpreter-library/interpreter-library.md) — the functions the library exports, and the type libraries.
- [Interpreter settings file](../interpreter-structure/interpreter-settings-file/interpreter-settings-file.md) — the elements of the SNCI file.
- [G-code based program interpretation](../g-code-interpretation/g-code-based-program-interpretation.md) — the order in which the CAM system calls the interpreter.
