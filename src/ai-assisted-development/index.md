# AI-assisted postprocessor development

This guide explains how to develop and maintain postprocessors with the help of artificial intelligence (AI): how to get the tools running, what to ask the assistant for, and how to check the result. It applies to both postprocessing subsystems — SPPX postprocessors and .NET postprocessors — because both read the same input data, [CLData](../cldata/cldata.md).

The toolset is in beta: command names and panels may still change.

## What the work looks like

You write in the chat, in your own words:

> On this machine the coolant does not come on after a tool change. Find out why and fix it.

Then you watch. The assistant opens the test project, finds the command that should have produced that block, finds the handler that processes it, reads the code, makes a small change, compiles the postprocessor, runs it on the same project, and shows you the NC program it got and how it differs from the previous one.

You read the result and answer the same way — "right, but M08 has to come before the spindle starts" — and it goes round again.

That is the whole loop. Nothing to memorise, no commands to type, and you do not have to write the code yourself, although you can look at every change and edit it by hand whenever you prefer. What cannot be handed over is the judgement: whether the program is correct for your machine and safe on it is decided by you. Everything in this guide about checking the result exists for that reason.

## What it costs

The tools and the knowledge are part of the product: the servers, the extensions, this documentation and the skills. The model that answers you is not — an AI assistant is a service of whoever provides the model, and it is paid for by the volume of text it processes.

In CAM Agent you can start straight away: it comes with an introductory allowance, enough to get a feel for what this can do. Its size and conditions may change over time. When it is used up, connect your own account with any of the publicly available AI providers; from then on the work goes on that provider's terms and at its prices, while the CAM system keeps supplying the tools and the knowledge.

Through a chat extension in Visual Studio Code, your provider account is what makes it work from the very first request. There is no introductory allowance in this case — the model is billed by the provider you connected, on the terms you agreed with it.

If the work must stay inside your own network, the model can live there too. Current tooling makes it practical to run one on your own hardware, and any client that can be pointed at a local model will use it. Nothing else in this guide changes: the servers, the extensions and the postprocessor itself are local anyway, so no project data has to leave the network. What you give up is the online half of the knowledge server — searching the published documentation goes through an online service, and in an isolated network it is not available, although skills stay searchable once their cache has been refreshed. The documentation in your workspace works regardless, as do your own notes; that is one more reason to keep a local copy even when everything else is connected.

## Two ways to work

| | CAM Agent | Visual Studio Code |
|---|---|---|
| Where you work | The agent chat inside the CAM system | VS Code with an AI chat extension |
| What you see | The task, the plan, the result; optionally the postprocessor IDE | The code, the diffs, the CLData, the generated NC program |
| Best for | Getting a result without opening the code | Developing, debugging and version-controlling a postprocessor |
| SPPX | Full cycle: read, edit, compile, run | Full cycle, with the code visible in the editor |
| .NET | Task-oriented use; the agent works with the project and the runner | The natural choice: C# language service, build, debugging |

The two are not exclusive. Asking the agent in the CAM system to investigate the data and then finishing the code in VS Code is a normal way to work.

## Read in this order

1. [How the system works](how-it-works.md) — the parts you will be dealing with, and which one does what.
2. [Set up the tools](setup.md) — download the bundle and let the assistant do the setup.
3. [Organize your workspace](workspace.md) — the folder that gives the assistant a memory.
4. [Develop with CAM Agent](cam-agent.md) or [Develop in Visual Studio Code](vscode.md) — pick your entry point.
5. [What the extensions give you](extensions.md) — the panels and commands you will be using, and where they are.
6. [SPPX workflow](sppx-workflow.md) or [.NET workflow](dotnet-workflow.md) — the development cycle for your postprocessor type.
7. [Review and verify](review-and-verify.md) — what to check before the NC program is used.
8. [Troubleshooting](troubleshooting.md) and [Advanced setup](advanced-setup.md) — when something does not work, and the full setup procedure.

## Skills for the assistant

A skill is a short instruction in plain language: what to do, in what order, what to check, and when the work counts as finished. There is no code in it — it is a text file the assistant reads and follows, much like a sensible briefing given to a new colleague. Anyone who can explain a way of working in words can write or correct one.

The skills that come with this guide cover setting up the workspace, inspecting the input data, the SPPX and .NET development cycles, and verifying a generated NC program.

They are published with this guide, in the `skills` folder of this documentation module — one folder each, with a `SKILL.md` file inside. The set grows as the toolset does; take all of it and let the assistant pick what fits the task. Loading them is part of the setup — see [Advanced setup](advanced-setup.md#documentation-and-skills-for-the-assistant).

You can add your own alongside them: they are plain Markdown, and the practices your team accumulates belong in the same form — see [Organize your workspace](workspace.md).

## What stays with you

Treat every answer as a draft. The assistant sees only what you give it: it cannot know undocumented machine behaviour, and a plausible-looking NC program can still be wrong. Review the diff, compile, run the postprocessor, read the generated NC program, and verify it in simulation before it goes to a machine. Do not put credentials, customer archives or machine secrets into the chat.
