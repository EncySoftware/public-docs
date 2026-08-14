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
3. [Develop with CAM Agent](cam-agent.md) or [Develop in Visual Studio Code](vscode.md) — pick your entry point.
4. [SPPX workflow](sppx-workflow.md) or [.NET workflow](dotnet-workflow.md) — the development cycle for your postprocessor type.
5. [Review and verify](review-and-verify.md) — what to check before the NC program is used.
6. [Troubleshooting](troubleshooting.md) and [Advanced setup](advanced-setup.md) — when something does not work, and the full setup procedure.

## Skills for the assistant

Skills are ready-made procedures for the assistant: which tool to call, in which order, what to check, and when the work is finished. Five are published with this guide, in the `skills` folder of this documentation module:

| Skill | Folder | What it does |
|---|---|---|
| Postprocessor development | `skills/postprocessor-development` | Chooses the postprocessor type and the tools, then runs the whole cycle |
| Inspect CLData | `skills/inspect-cldata` | Reads the real project data instead of guessing from documentation |
| Develop SPPX postprocessors | `skills/develop-sppx-postprocessor` | Read, edit, compile, run and compare an SPPX postprocessor |
| Develop .NET postprocessors | `skills/develop-dotnet-postprocessor` | Template, build, run and inspect a C# postprocessor |
| Verify NC programs | `skills/verify-nc-program` | Reviews the generated NC program before it is accepted |

Loading them is part of the setup — see [Advanced setup](advanced-setup.md#documentation-and-skills-for-the-assistant).

## What stays with you

Treat every answer as a draft. The assistant sees only what you give it: it cannot know undocumented machine behaviour, and a plausible-looking NC program can still be wrong. Review the diff, compile, run the postprocessor, read the generated NC program, and verify it in simulation before it goes to a machine. Do not put credentials, customer archives or machine secrets into the chat.
