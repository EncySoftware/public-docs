# AI-assisted postprocessor development

This guide explains how to develop and maintain postprocessors with an AI assistant: how to set the tools up, what the assistant can do on its own, and how to check the result. It applies to both postprocessing subsystems — SPPX postprocessors and .NET postprocessors — because both read the same input data, [CLData](../cldata/cldata.md).

The assistant reads the actual project data, changes the postprocessor code, compiles it and generates a test NC program. It does not decide whether the NC program is correct for your machine. That decision stays with you.

This is a beta guide for a beta toolset. Command names and panels may change between releases; the reference for what is installed on your computer is always the release notes of your CAM system and of the tools bundle.

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

1. [How the system works](how-it-works.md) — the components, what each one does, and where the boundaries are.
2. [Set up the tools](setup.md) — install the extensions, connect the MCP servers, give the assistant the documentation.
3. [Develop with CAM Agent](cam-agent.md) or [Develop in Visual Studio Code](vscode.md) — pick your entry point.
4. [SPPX workflow](sppx-workflow.md) or [.NET workflow](dotnet-workflow.md) — the development cycle for your postprocessor type.
5. [Review and verify](review-and-verify.md) — what to check before the NC program is used.
6. [Troubleshooting](troubleshooting.md) and [Advanced setup](advanced-setup.md) — when something does not work, and how to set this up for a team.

## Skills for the assistant

A skill is a Markdown file with a procedure the assistant follows: which tool to call, in which order, what to check, and when the work is finished. Five skills are published with this guide, in the `skills` folder of this documentation module:

| Skill | Folder | What it does |
|---|---|---|
| Postprocessor development | `skills/postprocessor-development` | Chooses the postprocessor type and the tools, then runs the whole cycle |
| Inspect CLData | `skills/inspect-cldata` | Reads the real project data instead of guessing from documentation |
| Develop SPPX postprocessors | `skills/develop-sppx-postprocessor` | Read, edit, compile, run and compare an SPPX postprocessor |
| Develop .NET postprocessors | `skills/develop-dotnet-postprocessor` | Template, build, run and inspect a C# postprocessor |
| Verify NC programs | `skills/verify-nc-program` | Reviews the generated NC program before it is accepted |

How to install them depends on the client — see [Advanced setup](advanced-setup.md#documentation-and-skills-for-the-assistant). If your client has no skill mechanism, open the `SKILL.md` file and paste it into the chat as instructions: the content is plain Markdown and works either way.

## What stays with you

Treat every answer as a draft. The assistant sees only what you give it: it cannot know undocumented machine behaviour, and a plausible-looking NC program can still be wrong. Review the diff, compile, run the postprocessor, read the generated NC program, and verify it in simulation before it goes to a machine. Do not put credentials, customer archives or machine secrets into the chat.
