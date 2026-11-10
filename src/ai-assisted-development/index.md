# AI-assisted interpreter development

This section explains how to develop and maintain an interpreter with the help of an AI assistant: how to set up the tools, what to ask the assistant for, what it needs from you, and how to check the result. It applies to interpreters written in C# from the templates of the CAM system, described in [Developing a custom interpreter in (.NET) C#](../dotnet/developing-a-custom-interpreter-in-net-csharp.md), and to native interpreters written in Delphi or C++ (see [Interpreter library](../interpreter-structure/interpreter-library/interpreter-library.md)).

By default the assistant develops an interpreter in C# (.NET). It creates a native library in Delphi or C++ only if you explicitly ask for one or if you are changing an existing native interpreter.

## What the work looks like

You write in the chat, in your own words:

> Programs for our machine write the rotary axis as B90, but the machine calls it B1. A program with B90 is not simulated. Fix it.

Then you watch. The assistant reads the NC programs and the machine of the project, finds where the interpreter reads axis words, decides what kind of difference it is (a setting or a change in the code), makes the change, builds the interpreter, runs the NC programs through it in the CAM system and shows you what changed in the simulation and in the log.

You read the result and answer the same way — "right, but the same machine also writes B=DC(30)" — and it goes round again.

You do not have to write the code yourself, although you can look at every change and edit it by hand whenever you prefer. What cannot be handed over is the judgment: whether the simulation matches what your machine does is decided by you. Everything this section says about checking the result exists for exactly that.

## What the assistant needs from you

- The NC programs the interpreter must read, and the CAM project with the machine they are written for.
- The programming manual of the controller for the words and cycles in question.
- The installed CAM system or ENCY Tuner the interpreter must work in.
- The expected result: what the machine does with the block that is simulated wrongly.

The more real programs you give, the better: the assistant takes the spellings of the words from them, not from memory.

## What it costs

The documentation and the skills are published free of charge, but the model that answers you is not part of them. An AI assistant is a service of whoever provides the model, paid for by the amount of text processed or by subscription. You will need an account with an AI service provider or with the developer of the AI client; the work runs on their terms and at their prices.

If your data must stay inside your network, the model can be deployed on your own hardware, with a client that supports it pointed at that model. Keep in mind that small local models handle multi-step work guided by skills noticeably worse: before relying on such a model, test it on a real task. Nothing else in this section changes — the CAM system, the interpreter and the NC programs are on your computer anyway.

## Reading order

| Page | What it covers |
|---|---|
| [How AI-assisted development works](how-it-works.md) | What parts the work consists of, what each of them does, what the assistant can and cannot do |
| [Setting up the tools](setup.md) | The short path: install an AI client, download the skills, check with two requests |
| [Organizing the workspace](workspace.md) | The working folder as the assistant's memory: NC programs, machine project, manual, notes, change history |
| [.NET workflow](dotnet-workflow.md) | The default path: a C# interpreter from a template — creation, build, debugging, changes |
| [Native interpreter workflow](native-workflow.md) | Only on explicit request or for an interpreter that is already native: Delphi, C++ |
| [Checking and confirming the result](review-and-verify.md) | Running all NC programs before and after a change, verification levels, preparing an interpreter for hand-over |
| [Troubleshooting](troubleshooting.md) | Typical symptoms, their causes and what to do |
| [Advanced setup](advanced-setup.md) | The full setup procedure: skills in different clients, build and debugging tools, the log, instruction file, several product versions, a separate workplace, automatic checks |

If you are just starting, read the pages in order up to the .NET workflow; read the page on the native interpreter only if you need one. You do not have to read [Advanced setup](advanced-setup.md) yourself: the assistant reads it when it sets up the tools.

## Skills for the assistant

A skill is an instruction in plain language: what to do, in what order, what to check, and when the work counts as finished. There is no code in it — it is a text file the assistant reads and follows, much like a briefing given to a new colleague. Anyone who can explain a way of working in words can write or correct one.

The skills are in the `skills` folder of this section: each skill is a folder with a `SKILL.md` file. All the skills download from this website as one archive: [download the skills](https://docs.encycam.com/technical/Interpreters/3/en/src/ai-assisted-development/skills/ai-skills.zip) (`ai-skills.zip`, with the six skill folders at the root of the archive). The skills are written in English. You can talk to the assistant in any language. Together they guide the whole work on an interpreter: the assistant starts with the general skill and turns to the others as the work goes on.

| Skill (folder) | What it is for | Section page |
|---|---|---|
| [`interpreter-development`](skills/interpreter-development/SKILL.md) | The general skill: what to find out first, in what order to work, and when the work is finished. By default an interpreter is developed in C# (.NET) | [How AI-assisted development works](how-it-works.md) |
| [`inspect-nc-programs`](skills/inspect-nc-programs/SKILL.md) | Collecting the NC programs and the machine data (axes, channels, M-functions), and listing every word the programs use | [Organizing the workspace](workspace.md) |
| [`develop-dotnet-interpreter`](skills/develop-dotnet-interpreter/SKILL.md) | Creating, configuring, building and debugging a C# interpreter from a template — the default path | [.NET workflow](dotnet-workflow.md) |
| [`develop-native-interpreter`](skills/develop-native-interpreter/SKILL.md) | A native interpreter library in Delphi or C++ — only when a native interpreter is really needed | [Native interpreter workflow](native-workflow.md) |
| [`nc-interpreter-foundations`](skills/nc-interpreter-foundations/SKILL.md) | How the CAM system reads a block and when the interpreter's code is called | [How AI-assisted development works](how-it-works.md) |
| [`verify-interpretation`](skills/verify-interpretation/SKILL.md) | Running all NC programs before and after a change, comparing the results, and preparing an interpreter for hand-over | [Checking and confirming the result](review-and-verify.md) |

Each skill can also be read on this site through the link in the table. If the archive is not available, download the source file `SKILL.md` from the skill page and put it in a folder named after the skill, for example `skills/interpreter-development/SKILL.md`. Copy all the skills at once: they refer to each other. How to add them to your AI client is described in [setting up the tools](setup.md), in detail — in [advanced setup](advanced-setup.md#skills-in-different-ai-clients).

You can keep your own skills alongside them. They are plain Markdown: the practices your team accumulates — the controllers you support, the variations of your customers' programs — take the same form. See [organizing the workspace](workspace.md).

## What stays with you

Treat every answer as a draft. The assistant sees only what you gave it: it does not know undocumented behavior of the controller, and a plausible-looking simulation can be wrong. Before an interpreter is given to a user, run all the NC programs you have through it, read the warnings in the [interpreter interaction log](../g-code-interpretation/log-interaction-with-the-interpreter/log-interaction-with-the-interpreter.md), and check the simulation of the blocks that were changed. Do not put passwords, customer archives or data that must not leave your company into the chat.
