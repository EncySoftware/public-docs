---
name: develop-dotnet-postprocessor
description: Develop a compatible C# postprocessor from an installed template, build it, run it through verified DotNet Posts or InpCore, and inspect NC output.
---

# Develop .NET postprocessors

## Trigger and when to use

Use this skill for C#/.NET postprocessor handlers, SDK projects, and typed CLData behavior. Use it after CLData inspection and before NC verification.

## Prerequisites and tool discovery

- Locate the installed CAM templates, normally under `Supplement/Postprocessor/DotNet/Templates`, and choose `EmptyPost` or `SimplePost` as appropriate.
- Discover the available generic C#/.NET build tool and the current DotNet Posts integration. DotNet Posts 0.2.0 operations are ordered: discover/status, setup when needed, then inspection, build/run, and diagnostics. Its supported API may include `dotnetPosts.status`, `setup`, `run`, `cancel`, `symbols`, `goto`, `whereAmI`, `inspectCldata`, and `highlight`; query availability rather than assuming every command or argument.
- Preserve the copied template's framework, SDK/package references, generated files, configuration, and build instructions. Do not select versions from memory.

## Safe workflow

1. Copy the installed template to a new working folder and rename the folder and `.csproj` consistently. Preserve the template SDK reference.
2. Open the copy and build the unchanged template with the generic C#/.NET build tool. Record framework, SDK, warnings, and output assembly.
3. Use `status` to discover DotNet Posts availability, then `setup` only when setup is needed. Do not confuse status with opening or mutating a panel.
4. Locate the typed handler using the installed SDK reference and `symbols`/navigation if available. Use named typed properties rather than guessed raw CLD indexes.
5. Make one small change with an explicit expected NC result. Review nulls, units, culture formatting, modal state, compensation, coordinate transforms, output encoding, and exception paths.
6. Build again. If DotNet Posts `run` is available, run the reduced project/CLData fixture and capture its structured report; use `goto`, `whereAmI`, or `inspectCldata` for diagnosis.
7. Otherwise use the supported `InpCore.exe` fallback and its documented settings/project invocation. The current beta requires the `-settingsdump` procedure and JSONL output for settings discovery. Verify the installed runtime first; do not invent command-line switches or treat another output format as equivalent.
8. Compare generated NC with the baseline and pass it to NC verification. Cancel a long run through the advertised `cancel` operation when supported.

## Prohibited and unsafe actions

- Do not hard-code framework or SDK versions, replace template references with guessed packages, or assume a structured API is installed.
- Keep DotNet Posts agent configuration separate from the copied template, `.csproj`, and postprocessor source.
- Do not edit before compiling the unchanged template, use unverified SDK properties, ignore build/runtime failures, alter machine settings, transmit NC, or treat a successful exit code as safety certification.

## Completion criteria

The template copy builds unchanged, its SDK reference is preserved, the typed change builds, a supported DotNet Posts or InpCore run produces inspectable results (or the limitation is recorded), and representative NC has been reviewed.

## User-visible presentation

Report template and SDK provenance, project files changed, build command/results, discovered API capabilities, run/fallback used, output path and report, relevant NC comparison, and unresolved compatibility or safety risks.
