# How AI-assisted development works

AI-assisted development combines a human developer, an editor, a model, local documentation, and the postprocessor tools. The model suggests text or code; the local tools and the developer decide whether that suggestion is correct.

## Component and role map

```text
Developer
   |
   v
AI client (for example, VS Code chat) <---- local public-docs fallback
   |
   +--> CAM Agent --------------------------> CAM host / project context
   |       |                                 (windowed or headless InP)
   |       +--> InP MCP --------------------> InP operations and inspection
   |       +--> Postprocessor Tools --------> SPPX and .NET postprocessing
   |       +--> CLData MCP -----------------> read-only CLData inspection
   |
   +--> .NET Posts / InpCore or SPPX runner -> generated NC
                                               |
                                               v
                                      simulator + human review
```

CAM Agent is the host integration. InP MCP is the tool interface for InP; it is
not the same thing as either windowed InP or headless InP. CLData MCP reads the
input model. Postprocessor Tools and the subsystem runners build or execute a
postprocessor. The developer remains responsible for approving changes.

## Current beta components

| Component | Role in this guide | Beta boundary |
| --- | --- | --- |
| CAM Agent | Connects the AI client with the CAM host and project context | Availability depends on the supported host and installation |
| Windowed InP | UI-backed project selection and visual inspection | Requires a host UI; it is not a batch runner |
| Headless InP | Repeatable file and batch operations | Has no UI context and does not provide safety approval |
| InP MCP | Exposes supported InP operations to an AI client | Use only commands advertised by the installed service |
| CLData MCP | Read-only command, structure, and parameter inspection | It does not change CLData or prove machine safety |
| Postprocessor Tools 0.9.27 | SPPX and .NET postprocessor development support | Check installed capabilities before relying on an example |
| DotNet Posts 0.2.0 | .NET postprocessor setup, navigation, and execution integration | Use the installed API and separate agent configuration |

Versions and capabilities are installation facts. Record them with test results.

## Architecture

1. You describe a small task in the editor or agent interface.
2. The assistant receives only the selected or explicitly available context.
3. The assistant uses documentation, source files, and tool output to form a draft.
4. You inspect the proposed changes and apply only the useful parts.
5. SPPX or .NET tools compile, run, or debug the postprocessor.
6. You compare output with the expected toolpath and verify the result in simulation.

The central data contract is CLData. Both postprocessing subsystems consume the same commands and parameters, although SPPX and .NET use different access syntax. The AI should therefore reason from the CLData command and parameter description, not invent a second input model.

## Hybrid workflows

Use the workflow that matches the task. Ask an assistant to explain a CLData command, use SPPX for an existing mask-based postprocessor, and use .NET for typed code, debugging, or larger integrations. A single project can use both subsystems, but their source files, APIs, and build steps must remain distinct.

Local context is preferred for customer-specific work. The public documentation in this module is a fallback reference when a connected documentation service is unavailable. It is not a live view of every installed product version.

## What the assistant can and cannot do

The assistant can summarize documentation, propose a handler or mask change, identify likely missing cases, and help write tests or review checklists. It cannot know machine behavior that is not represented in the supplied context, guarantee syntactically valid output, operate a CNC safely, or approve a postprocessor for production.
