# AI-assisted postprocessor development

This guide explains how to develop and maintain postprocessors with an AI assistant: how to get the tools running, what to ask for, and how to check the result. It applies to both postprocessing subsystems — SPPX postprocessors and .NET postprocessors — because both read the same input data, [CLData](../cldata/cldata.md).

The assistant reads the actual project data, changes the postprocessor code, compiles it and generates a test NC program. It does not decide whether the NC program is correct for your machine. That decision stays with you.

The toolset is in beta: command names and panels may still change.

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

Skills are ready-made procedures for the assistant: which tool to call, in which order, what to check, and when the work is finished. They cover setting up the workspace, inspecting the input data, the SPPX and .NET development cycles, and verifying a generated NC program.

They are published with this guide, in the `skills` folder of this documentation module — one folder each, with a `SKILL.md` file inside. The set grows as the toolset does; take all of it and let the assistant pick what fits the task. Loading them is part of the setup — see [Advanced setup](advanced-setup.md#documentation-and-skills-for-the-assistant).

You can add your own alongside them: they are plain Markdown, and the practices your team accumulates belong in the same form — see [Organize your workspace](workspace.md).

## What stays with you

Treat every answer as a draft. The assistant sees only what you give it: it cannot know undocumented machine behaviour, and a plausible-looking NC program can still be wrong. Review the diff, compile, run the postprocessor, read the generated NC program, and verify it in simulation before it goes to a machine. Do not put credentials, customer archives or machine secrets into the chat.
