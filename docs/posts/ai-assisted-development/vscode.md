# Develop in Visual Studio Code

In VS Code you stay in control of the code: you see every diff, run the generator yourself when you want to, and keep the postprocessor in version control as usual. The assistant is a chat extension of your choice; the results are shown by the three extensions from the bundle.

Install everything first — see [Set up the tools](setup.md).

## Which chat extension to use

Any assistant that meets three conditions will do, and the choice is yours:

- it connects to MCP servers, which is how it reads CLData and drives the postprocessor;
- it may run commands in your workspace, which is how it builds, installs and opens things for you;
- it has a place for standing instructions, so the rules of your project apply to every request.

**The recommended starting point is Kilo Code.** Three of its properties matter for this work:

- **Skills are a first-class mechanism.** A skill is a folder with a `SKILL.md` file, and Kilo Code picks it up from `.kilo/skills/` in the project or `~/.kilo/skills/` for all projects — which is exactly the shape of the skills published with this guide, so they drop in unchanged. New skills are discovered when a session starts, or on `/reload` in an open session.
- **It is not tied to one model provider.** Requests go through a gateway that reaches models from every major provider through one endpoint, and you can bring your own API keys, so the choice of provider stays yours.
- **It is open source** (MIT-licensed), and its sessions can be monitored and steered remotely, including from a phone.

Others that work with this toolset:

| Chat extension | Standing instructions | Notes |
|---|---|---|
| Kilo Code | `AGENTS.md` in the project root; project instructions in `kilo.jsonc` | Loads the published skills as they are |
| Cline, Roo Code | The client's rules file | Same origin, so the panels look familiar |
| Claude Code | `CLAUDE.md`; loads the published skills as they are | Runs commands after you approve them |
| GitHub Copilot Chat | `.github/copilot-instructions.md` | MCP and command execution require its agent mode |
| Codex CLI | `AGENTS.md` | Works from the terminal, alongside VS Code |

Whichever you choose, prefer a client that loads skills directly — you then get the way of working as well, not just the tools. With a client that has no skill mechanism, name the relevant `SKILL.md` in the standing instructions or paste it into the chat; the content is plain Markdown and works either way.

Where each client keeps its MCP configuration is listed in [Advanced setup](advanced-setup.md#connect-the-mcp-servers).

## The working cycle

1. Work on a copy or a branch of the postprocessor, never on the production file.
2. Open only the folders that matter: the postprocessor, and the documentation checkout if you use one.
3. Open a small test project. Ask the assistant to inspect it — the CLData Inspector then shows you the same commands it read.
4. State one bounded task, with the expected NC output. Ask for a plan and the evidence behind it before any file is written.
5. Review the diff as soon as it appears. Reject reformatting and rewrites you did not ask for.
6. Let it compile and run, or run **Generate NC** yourself. Compare the generated program with the previous run and with the reference program.
7. Verify the result — see [Review and verify](review-and-verify.md).

For the details of each postprocessor type, continue with the [SPPX workflow](sppx-workflow.md) or the [.NET workflow](dotnet-workflow.md).

## Ask it to show you things

The assistant can open exactly what it is talking about, which is faster to read than a quoted fragment and always shows the current state:

- a command in the CLData Inspector — the exact file, command and parameter;
- a handler at the relevant line, with a range highlighted and a short note attached;
- the **Generate NC** panel with a configuration prepared, and the run started if you asked for it.

Just ask: "show me that command in the inspector", "open the handler where you changed the offset".

Note that the assistant's own run is silent — it runs the postprocessor through the server and reads the output itself, which is how it checks its own work. The **Generate NC** panel is for you: the configuration, the post input parameters, the progress, the errors in **Problems** with links into the handler code, and the diffs against the previous run and the reference program.

## Let the assistant keep its own run configuration

The **Generate NC** panel stores named configurations: which project to process, where to write the NC file, which post input parameters to use. Ask the assistant to create its own — for example `Agent check` — instead of reusing yours. Your settings then stay untouched, and the two runs can be compared.

## Context and safety

Give the assistant a small set of authoritative sources: the handler in question, the relevant page of the CLData reference, a reduced test project, and a known-good NC program. A whole customer project rarely improves the answer.

Use the workspace instruction file (`CLAUDE.md`, `AGENTS.md`, `.clinerules`, depending on the client) to state the conventions that always apply: naming, output format, the machines involved, the requirement to run the postprocessor before reporting success. Do not put credentials, tokens or customer archives there, and keep generated NC output out of the source folders.

Ask for a plan before a multi-file change, keep every change in version control, and never let an assistant transmit a program to a machine.
