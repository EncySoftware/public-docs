# AI-assisted postprocessor development

This beta guide explains how to use AI assistance when developing and maintaining CAM postprocessors. It covers both the SPPX postprocessor workflow and the .NET postprocessor workflow. AI can help you understand CLData, draft code, and review changes, but it does not replace simulation, machine documentation, or human approval.

## Start here

- [How the system works](how-it-works.md) — the architecture, boundaries, and request flow.
- [CAM Agent](cam-agent.md) — the CAM Agent Extension Store installation and operating modes.
- [Visual Studio Code workflow](vscode.md) — the common editor workflow.
- [SPPX workflow](sppx-workflow.md) — assisted work with masks and SPPX source.
- [.NET workflow](dotnet-workflow.md) — assisted work with C# postprocessors.
- [Review and verify](review-and-verify.md) — checks required before using generated NC code.
- [Troubleshooting](troubleshooting.md) — common setup and response problems.
- [Advanced setup](advanced-setup.md) — controlled local context and team setup.

## Available skills

These reusable skills are shipped with this documentation module. Open the
resource-relative `SKILL.md` page for the skill instructions:

- [Postprocessor development](skills/postprocessor-development/SKILL.md)
- [Inspect CLData](skills/inspect-cldata/SKILL.md)
- [Develop SPPX postprocessors](skills/develop-sppx-postprocessor/SKILL.md)
- [Develop .NET postprocessors](skills/develop-dotnet-postprocessor/SKILL.md)
- [Verify NC programs](skills/verify-nc-program/SKILL.md)

Skill installation depends on the AI client and CAM Agent. If the client can
load skills, install or enable these paths through its documented mechanism.
Otherwise use the pages manually as checklists and prompts. Do not assume that
linking to a skill installs it.

## Beta status

This module documents the currently supported workflow. It does not promise an automatic code-writing service, a hosted knowledge base, or a production RAG MCP. A future RAG MCP may provide indexed documentation and project context, but that capability is not assumed here.

## Safety rule

Treat every AI response as an untrusted draft. Do not expose credentials, customer data, machine secrets, or proprietary files unnecessarily. Review the diff, compile or run the relevant tools, inspect the generated NC program, and verify it in simulation before production use.
