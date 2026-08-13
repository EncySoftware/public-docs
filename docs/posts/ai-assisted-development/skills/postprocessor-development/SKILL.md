---
name: postprocessor-development
description: Plan and coordinate safe AI-assisted development of SPPX or .NET postprocessors from real CLData through reviewed NC output.
---

# Postprocessor development

## Trigger and when to use

Use this skill when a user wants to create, adapt, debug, or review an SPPX or .NET postprocessor, or when the requested NC behavior is not yet mapped to a handler. Use it as the coordinator before invoking the more specific inspection, SPPX, .NET, or NC-verification skills.

## Prerequisites and tool discovery

- Identify the CAM release, machine/controller context, post type, source location, representative project or CLData, and expected NC change.
- Discover the tools actually available in the current client: documentation/RAG or local Markdown, CLData inspection, SPPX tools, .NET Posts, a generic C#/.NET build tool, and InPCore or another supported runner.
- Ask each tool for its advertised commands and capabilities. Do not assume a future MCP, a particular command name, or a headless feature exists.
- Prefer, in order, real project/runtime values, current official documentation and installed templates, public distributable posts, then carefully marked general knowledge.
- Request the smallest representative fixture and known-good NC sample; remove credentials, machine secrets, and unnecessary customer data.

## Safe workflow

1. State the target post type and the requested observable NC behavior.
2. Read the relevant CLData documentation and inspect the actual project before proposing code.
3. Trace the command to its existing SPPX mask/program or .NET handler; explain that path before editing.
4. Choose the smallest compatible change and define expected blocks, modal transitions, and edge cases.
5. Apply the type-specific development skill. Preserve existing formatting, registers, modal state, coordinate and compensation conventions.
6. Build or compile with installed tools, then run a reduced fixture and compare generated output with the expected and known-good output.
7. Use the verification skill for an independent NC review, including simulation where available.
8. Present changed files, tool/runtime versions, test input, output location, deviations, and unresolved risks. Keep human approval before production use.

## Prohibited and unsafe actions

- Do not invent CLData mappings, SDK properties, tool signatures, register defaults, or machine behavior.
- Do not replace a full customer project with an unreviewed fixture, silently change machine configuration, bypass safety checks, transmit NC, or approve production use.
- Do not treat compilation, a successful runner exit, or plausible-looking NC as proof of safe motion.
- Do not expose secrets or commit unrelated/generated files.

## Completion criteria

The task is complete only when the requested source change is minimal and explainable, actual CLData was inspected, the selected tool path was built/run or its limitation recorded, representative NC was reviewed, and independent human/simulation verification remains explicit.

## User-visible presentation

Report the plan, evidence from the real project, exact files changed, build/run results, first differing or relevant NC blocks, verification status, and risks. Separate verified facts from assumptions and clearly mark anything that still requires user or machine-specific review.
