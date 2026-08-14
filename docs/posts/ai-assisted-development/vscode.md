# Develop in Visual Studio Code

In VS Code you stay in control of the code: you see every diff, run the generator yourself when you want to, and keep the postprocessor in version control as usual. The assistant is a chat extension of your choice; the postprocessor-specific work is done through the MCP servers, and the results are shown to you by the three extensions from the tools bundle.

Install everything first — see [Set up the tools](setup.md).

## The working cycle

1. Work on a copy or a branch of the postprocessor, never on the production file.
2. Open only the folders that matter: the postprocessor, and the documentation checkout if you use one. A workspace with unrelated repositories in it wastes the assistant's attention.
3. Open a small test project. Ask the assistant to inspect it — the CLData Inspector then shows you the same commands it read.
4. State one bounded task, with the expected NC output. Ask for a plan and the evidence behind it before any file is written.
5. Review the diff as soon as it appears. Reject reformatting and rewrites you did not ask for.
6. Let it compile and run, or run **Generate NC** yourself. Compare the generated program with the previous run and with the reference program.
7. Verify the result — see [Review and verify](review-and-verify.md).

For the details of each postprocessor type, continue with the [SPPX workflow](sppx-workflow.md) or the [.NET workflow](dotnet-workflow.md).

## How the assistant shows you things

An assistant running outside VS Code does not know about your editor windows, so the extensions give it a way to point at things. In practice this means:

- When it finds a command in the data, it can open it in the CLData Inspector — the exact file, command and parameter, in the sidebar or in an editor tab.
- When it changes a handler, it can open that handler at the relevant line, and highlight a range with a short note attached. Highlights disappear as soon as the file is edited.
- When it wants to show you a run, it can open the **Generate NC** panel with a configuration prepared and, if you asked for it, start the generation.

Ask for this when a report is hard to follow: "show me that command in the inspector", "open the handler where you changed the offset". It is faster to read than a quoted fragment, and it shows the code as it actually is now.

The panel run and the assistant's own run are not the same thing. Through MCP the assistant runs the postprocessor silently and reads the output itself — that is how it checks its own work. The **Generate NC** panel is for you: the configuration, the post input parameters, the progress, the errors in **Problems** with links into the handler code, and the diffs against the previous run and against the reference program.

## Let the assistant keep its own run configuration

The **Generate NC** panel stores named configurations: which project to process, where to write the NC file, which post input parameters to use. Ask the assistant to create its own — for example `Agent check` — instead of reusing yours. It can clone the active configuration, set the project, the output path and the parameter values, and run it. Your own settings then stay untouched, and the two runs can be compared.

## Context and safety

Give the assistant a small set of authoritative sources: the handler in question, the relevant page of the CLData reference, a reduced test project, and a known-good NC program. A whole customer project rarely improves the answer.

Use the workspace instruction file (`CLAUDE.md`, `AGENTS.md`, `.clinerules`, depending on the client) to state the conventions that always apply: naming, output format, the machines involved, the requirement to run the postprocessor before reporting success. Do not put credentials, tokens or customer archives there, and keep generated NC output out of the source folders.

Ask for a plan before a multi-file change, keep every change in version control, and never let an assistant transmit a program to a machine.
