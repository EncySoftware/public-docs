---
name: postprocessor-development
description: Coordinate AI-assisted development of an SPPX or .NET postprocessor — from the real CLData through a reviewed NC program. Use this first, then the type-specific skill.
---

# Postprocessor development

## When to use

The user wants to create, adapt, debug or review a postprocessor, or asks why an NC program looks the way it does. Start here, then hand over to `inspect-cldata`, `develop-sppx-postprocessor`, `develop-dotnet-postprocessor` and `verify-nc-program`.

## Establish the facts first

Before planning anything, know these five things. Ask for what is missing instead of assuming it.

1. **Postprocessor type** — SPPX (`*.sppx`, `*.spp`, `*.inp`) or .NET (a C# project or a compiled assembly). The tools and the whole workflow differ.
2. **The postprocessor** — the file or project path, and whether it is a copy you may change.
3. **A test project** — a CAM project (`*.stcp`, `*.stc`) or a `*.inpcld` file with a short, representative toolpath.
4. **The requested change**, expressed in NC output: which block is wrong, what it should be, on which machine and control system.
5. **A reference** — the current NC program, and a known-good program if one exists.

Then check which tools you actually have: CLData tools (`cld_*`), InP tools (`pp_*`), CAM tools if the CAM server is connected, the VS Code extension commands, a `dotnet` build tool, documentation as local Markdown or through a retrieval service. Report what is missing rather than substituting a guess for it.

CAM tools are secondary here, but they answer what CLData cannot: the machine configuration, an operation's parameters, the tool that is mounted. They can also build the input — recalculate the toolpaths, export CLData, create a test project — when the fixture you need does not exist yet.

## Trust order for facts

1. Values read from the actual project and results of actual runs.
2. The official documentation for the installed release, and the templates shipped with it — authoritative for what the product does.
3. The user's own written practices and decisions in the workspace — authoritative for the conventions of their machines and their team, which no published documentation covers. Where the two seem to disagree, the documentation describes the product and the notes describe this shop; say which one you followed.
4. Distributed postprocessors supplied with the product.
5. Patterns seen repeatedly across an internal postprocessor corpus — evidence, not specification.
6. General knowledge, only when marked as an assumption.

The published documentation, whether searched through the knowledge server or read from a local checkout, is a snapshot: it does not know this shop. The workspace notes are the living part, and keeping them current is part of your work — see the `prepare-workspace` skill.

A CLData command name never determines its parameter values. Read the project.

## Workflow

1. Restate the task as an observable difference in the NC program, and name the acceptance check.
2. Run `inspect-cldata` to find the command and its real parameters in the test project.
3. Locate the code that processes it — an SPPX handler or a typed .NET handler — and explain the current path to the output before changing anything.
4. Plan the smallest change that produces the expected output. State the expected blocks, the modal transitions and the edge cases.
5. Apply the type-specific skill to make the change, compile it and run it.
6. Run `verify-nc-program` on the result.
7. Report: files changed, evidence from the project, build and run results, the NC differences with their causes, verification state, and what remains for the user to check.

## Rules

- Do not invent CLData mappings, parameter names, SDK properties, tool signatures or register defaults.
- Do not edit an item without reading its current content first.
- Do not change machine configuration, delete items to make something pass, or transmit an NC program anywhere.
- Do not call the task done without a run: compilation and a zero exit code are not results.
- Do not use a full customer project where a reduced fixture works, and keep credentials and customer data out of the conversation.

## Done means

The change is minimal and explainable, it is based on data actually read from the project, the postprocessor compiled and ran, the generated NC program was compared with the baseline and reviewed, the verification state is stated explicitly, and the remaining human checks are named.
