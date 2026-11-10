# Advanced setup

This page is the full setup procedure and a reference for checking what has been done. Give it to the assistant as described in [setting up the tools](setup.md), follow it by hand, or read it when your team needs a reproducible result.

## What this is about

This section is addressed to the assistant reading this page in order to set up the tools: here is the domain it is working in.

A controller executes an **NC program** — a text of blocks; each block consists of words: addresses with numbers, G- and M-functions, cycle calls. The CAM system can simulate such a program: show the tool path and the machine movements it will cause. For this it needs an **interpreter** — a library that explains to the CAM system kernel what each word means on a particular controller. Each controller and its dialect needs its own interpreter, and refining the interpreter is the work of the person the assistant is helping. Usually this is a process engineer, a support engineer or a tester who knows the machine much better than programming.

An interpreter consists of two files: the `*.snci` settings file and the `*.dll` library. The library comes in two kinds:

- **.NET** — a C# project created from a template of the CAM system — the default path;
- **native** — a library in Delphi, C++ or another compiled language — only on the user's explicit request or for an interpreter that is already native.

What the tools are set up for: reading real NC programs and the controller manual, editing and building the interpreter, running programs through it in the CAM system or ENCY Tuner, and comparing the result with the previous one. Whether the simulation is correct is decided by that person; the assistant prepares the grounds on which they judge.

The setup consists of three parts, in this order: skills, build and debugging tools, working folder. A problem report states the versions of the CAM system or ENCY Tuner, the .NET SDK, the AI client and the skills: most "it worked yesterday" reports are explained by a difference in versions.

## Skills in different AI clients

The skills are published with this documentation: the skills archive `ai-skills.zip` is downloaded from the link on the [AI-assisted interpreter development](index.md#skills-for-the-assistant) page, and the six skill folders are at its root. The documentation archive contains the same skills, in its `src/ai-assisted-development/skills/` folder inside the archive's root folder `public-docs-Technical-Interpreters-en-v3`. A skill is a folder named after the skill with a `SKILL.md` file inside. Copy all six folders at once: the skills refer to each other by name.

| Client | Where to copy |
|---|---|
| Kilo Code | `.kilo/skills/` of the working folder, or `%USERPROFILE%\.kilo\skills\` to have the skills in every project; a new session picks them up, the `/reload` command does it without a restart |
| Claude Code | `.claude/skills/` of the working folder, or `%USERPROFILE%\.claude\skills\` to have the skills in every project; new skills are visible at once, and if there was no skills folder before — after the `/reload-skills` command |
| Other clients | Their own skills folder of the working folder or of the user, an entry in the agent configuration, or a settings item — according to the client's documentation |

If the client has no skill mechanism, paste the content of the `SKILL.md` files you need into the chat or reference their files from the client's instruction file (`AGENTS.md`, `CLAUDE.md` and similar).

However you connected them, check that they are loaded: ask the assistant which skills it sees now. Skills installed for the user are available with any folder open; skills installed for the working folder — only in it.

The skills are updated together with the documentation. Replace the folders completely instead of editing them in place: keep your own additions as separate skills next to them (see [organizing the workspace](workspace.md)).

## Build and debugging tools

A C# interpreter needs:

- **.NET SDK** of the .NET version used by the required product version (see [Product versions](dotnet-workflow.md#product-versions)). Check with the `dotnet --list-sdks` command.
- **Visual Studio Code** with the **C#** extension from Microsoft: it contains the debugger the launch configurations of the templates are designed for. The **XML Language Support by Red Hat** extension is convenient for editing `*.snci` files but not required.
- **The path to the product program** for debugging. The template starts the CAM system or ENCY Tuner from the folder stored in the environment variables `NCKernelDir` (CAM system) and `TunerDir` (ENCY Tuner). The **Create G-code interpreter** window (the interpreter creator below) writes one of them — the variable of the product it was opened from — when the **Set ENCY file path** button (in ENCY Tuner the button shows its own name) is clicked in it and the product's executable file is selected; after that you need to sign out of Windows and sign in again, or at least start Visual Studio Code again from the Start menu. If there is no variable, the path can be written into `launch.json` — the standard product installation folder, not a folder that exists only on your computer. The name of the CAM system's executable file is put into `launch.json` by the interpreter creator; a template copied by hand, without the creator, keeps `${env:CAMName}`, which nothing sets — write the file name there instead. In detail — [Interpreter debugging in Visual Studio Code](../dotnet/interpreter-debugging-in-visual-studio-code/interpreter-debugging-in-visual-studio-code.md).
- **Log**: in the **System setup** window, on the **Additional** page, in the **Logs** group, the **Use logs** and **Use log interaction with the interpreter** options are turned on (the second one is available only when the first one is on); the same in ENCY Tuner. Without them the log contains neither the kernel's messages about the words read nor the lines the interpreter writes. In detail — see [Interpreter interaction log](../g-code-interpretation/log-interaction-with-the-interpreter/log-interaction-with-the-interpreter.md).

A native interpreter needs its compiler and the packages with the SDK interface declarations — see [Native interpreter workflow](native-workflow.md#what-the-assistant-needs).

Whatever is missing from this list must be named, not replaced with a guess; missing programs are installed only with the user's permission.

## Working folder instruction file

Put requirements that always apply where the assistant always reads: into the instruction file of the working folder (`AGENTS.md` or the file your client reads) or into skills. What to keep in it is described in [organizing the workspace](workspace.md#agentsmd--a-short-permanent-memo).

For a C# interpreter the open folder must be the folder of the interpreter itself, and clients look for instruction files in different ways. Claude Code reads `CLAUDE.md` (or `AGENTS.md` if there is none) both in the open folder and in all folders above it, so the memo of a working folder that lies above the interpreter folder is visible to it anyway. Kilo Code reads `AGENTS.md` only in the open folder, therefore:

- in Kilo Code you can list additional instruction files in the global `instructions` setting of the `kilo.jsonc` file (usually `%USERPROFILE%\.config\kilo\kilo.jsonc`) — put the full path to the `AGENTS.md` of the working folder there, and it will be read in any project;
- if the client cannot do this, put a short `AGENTS.md` into the interpreter folder with a reference to the shared file and the notes folder.

In practice, the following rules pay off:

- first read the real programs and the controller manual, and name where each word was taken from;
- C# (.NET) by default, a native interpreter — only on explicit request;
- variations — into `InterpreterSettings.ini`, not into the code;
- one change at a time, then a build, a run of all programs and a comparison with the previous result — before any report that the work is done;
- do not change the installed product, its templates and libraries;
- do not send the interpreter to the customer without permission.

## Several product versions on one computer

An interpreter works in the product version it is built for: each version has its own .NET and its own version of the SDK package (see [Product versions](dotnet-workflow.md#product-versions)). Decide which versions the interpreter is developed for, and run the programs in each of them. One project can be built for several versions — one output folder and one launch configuration for each. If a version is not installed on this computer, the check in it cannot be considered done: say so.

The `NCKernelDir` and `TunerDir` variables point to one installation. If a released version and a beta version are installed side by side, check which one the variable points to before comparing results: a run in another version finishes successfully and simply gives a different result.

## A separate workplace for the assistant

- A copy or a branch of the interpreter, not the files the customer already has.
- A separate folder for run results, outside the source tree.
- Running from a copy of the build output, so that a new build does not replace the library in the middle of a set of programs.
- Shortened programs and projects instead of full customer archives, where that is enough.
- No passwords, tokens, license files, customer archives or unrelated repositories in the working folder and in the instruction files — see [What must not be in it](workspace.md#what-must-not-be-in-it).

## Automatic checks

A run program that simulates all NC programs without clicks and saves the simulated commands and the log makes the check reproducible: fixed programs, a fixed project, a fixed interpreter version. The assistant makes it following the `verify-interpretation` skill on the public programming interface of the CAM system; the rules without which it cannot be trusted, and the cases where the run stays manual, are in [Running the programs](review-and-verify.md#running-the-programs). Automation can report that the simulation has changed, but never that the change is correct: the differences are analyzed by a person.
