# Visual Studio Code workflow

Visual Studio Code is the common editing surface for AI-assisted postprocessor work. The SPPX workflow uses its source and mask files; the .NET workflow uses a copied SDK template and C# source.

## Install the working bundle

Use the automatic setup first when the CAM Agent or AI client offers it. The
intended bundle is Postprocessor Tools, the AI chat client, CLData MCP for
read-only CLData inspection, and InP MCP for supported InP operations. These
have different roles: CLData MCP reads input data, while InP MCP operates the
advertised CAM/InP context. Confirm actual capabilities after installation.

For a manual setup, install or enable each component using its own documented
instructions, then configure the AI client to use the installed services. Do
not copy configuration from another release. If the client needs the .NET
posts location, use `dotnetPosts.installationFolder` and set it to the folder
containing the installed DotNet Posts integration; verify the path locally.

## Connectivity smoke test

Use a non-production project and a small read-only request for each connected
service. CLData MCP should return a project/file or command summary. InP MCP
should return only an advertised status or read-only context result. A failed
or unavailable service is a setup issue, not a reason to substitute guessed
commands. Never include a write, source edit, NC transmission, or machine
connection in a connectivity test.

## Recommended sequence

1. Create a working copy or branch of the postprocessor.
2. Open only the relevant folders in the workspace.
3. Read the applicable documentation and existing handlers before asking for a change.
4. Give the assistant one bounded task with the expected input, output, and constraints.
5. Review the proposed diff immediately. Reject unrelated formatting or broad rewrites.
6. Run the native compiler, generator, or test command for the subsystem.
7. Inspect the NC output and verify the toolpath in simulation.

Use workspace instructions to state naming, output format, and safety requirements. Do not place passwords, tokens, machine credentials, or unnecessary customer files in prompts or repository instructions.

## Context selection

Prefer a small set of authoritative files: the relevant CLData page, the existing handler, the machine-specific conventions, and a representative test input. If a local public-docs checkout is available, use it as a fallback reference. Mark assumptions when the installed documentation or SDK differs from the checkout. A future RAG MCP may provide retrieval, but it is outside the current beta boundary and is not required for this workflow.

## Safe editing

Ask for a plan before a multi-file change. Keep generated output outside source directories when possible. Use version control to inspect every change, and never let an assistant directly send NC code to a machine.
