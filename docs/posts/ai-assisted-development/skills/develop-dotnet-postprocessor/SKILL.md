---
name: develop-dotnet-postprocessor
description: Develop a C# postprocessor from the installed template — build it, run it through DotNet Posts or the batch runner, and inspect the NC output.
---

# Develop .NET postprocessors

## When to use

Work on a C# postprocessor: typed handlers, an SDK project, a compiled postprocessor assembly. Run `inspect-cldata` first and `verify-nc-program` afterwards.

There is no dedicated MCP server for .NET postprocessors. You work with the C# project through the ordinary file and build tools, and the postprocessor-specific parts through the DotNet Posts extension or the batch runner.

## Choose the starting point

Adapting an existing postprocessor is the normal case; creating one from a template is the exception. Decide explicitly, and say which you chose and why.

1. **Closest existing postprocessor — prefer this.** A distributed postprocessor supplied with the CAM system, or one from the user's own corpus, for a similar machine and control system. Copy it, then work from its actual code: it already builds and produces output, so the baseline is real. Never carry over machine-specific behaviour without checking it against this project's data.
2. **New from a template — only when nothing close exists.** The user creates postprocessors in the CLData Viewer UI, which copies and renames a template for them. When you are asked to do it instead, copy a template from `Supplement/Postprocessor/DotNet/Templates` (`EmptyPost` or `SimplePost`) yourself, and keep the SDK package reference, the target framework and the project settings exactly as the template has them. Never choose a version from memory — the installed release decides it. Do not ask the user to copy and rename files by hand.

**The renaming rule is hard: the folder name and the `.csproj` name must be identical.** The configuration that comes with the template derives both from the folder name: the build task in `.vscode\tasks.json` builds `${workspaceFolder}\${workspaceFolderBasename}.csproj`, and the launch configuration in `.vscode\launch.json` hands the runner `bin\Debug\${workspaceFolderBasename}.dll`. Name the `.csproj` differently and both the `F5` build and the debugger stop working, complaining about a file that does not exist rather than about a name. So rename the folder and the `.csproj` in one move, do not set `AssemblyName` by hand (the assembly name follows the project name), and leave the `.vscode` folder as it is. The same rule applies when you copy an existing postprocessor into a folder with a new name.

Then, whichever way you started:

3. Build the project unchanged and record framework, warnings and output assembly. If it does not build as it is, stop and report that — nothing after it is diagnosable.
4. Generate an NC program from the unchanged project and keep it as the baseline.

## Tools

DotNet Posts commands, available in VS Code and callable by an agent that can execute commands:

| Command | Purpose |
|---|---|
| `dotnetPosts.status` | Configurations, paths and post input parameters; read-only, does not open or change the panel |
| `dotnetPosts.setup` | Prepare a run configuration without starting it |
| `dotnetPosts.run` | Run the configured generation |
| `dotnetPosts.cancel` | Cancel a running generation |
| `dotnetPosts.symbols` / `dotnetPosts.goto` | List the postprocessor handlers; open one |
| `dotnetPosts.highlight` / `dotnetPosts.whereAmI` | Mark a range of code; report where the user's cursor is |
| `dotnetPosts.inspectCldata` | Open the configured CLData in the Inspector |
| `dotnetPosts.generateNC` / `dotnetPosts.generateNCFromDll` | Generate from the workspace project, or from an assembly you point at |

`dotnetPosts.autoBuild` builds the project before a run, which prevents testing an edit against a stale assembly. `dotnetPosts.installationFolder` must point at the CAM installation containing the batch runner.

The batch runner is `InpCore.exe`. It has two modes that matter here: writing the postprocessor's default settings out as a `Settings.xml` next to the input, which is what makes running an assembly without sources possible, and processing a CAM project in batch mode. It reports progress as a stream of events ending with a result code, and the process exit code repeats the outcome — a run counts as successful only when both agree. The settings format is not the SPPX one; use the file the runner produced. If the installed runner does not support extracting settings, report the version limitation instead of hand-writing a settings file.

## Workflow

1. Get the command and its real parameter values from `inspect-cldata`, in the `dotnet` path dialect.
2. `dotnetPosts.symbols` to list the handlers, `dotnetPosts.goto` to open the relevant one. Read the current implementation before changing it.
3. Make one small change and state the expected NC output. Prefer named typed properties from the SDK over raw indexes wherever the SDK provides them.
4. Build. Read the warnings that concern your change.
5. `dotnetPosts.status` to see the configuration, then `dotnetPosts.run` on the reduced project. Capture the report: output file, messages, result code. Use `dotnetPosts.generateNCFromDll` when there are no sources, and `dotnetPosts.cancel` to stop a long run.
6. If DotNet Posts is unavailable, run `InpCore.exe` directly in batch mode with the settings file produced by the runner, and report that you used the fallback.
7. Compare the generated program with the baseline, then hand over to `verify-nc-program`.

## Rules

- Do not hard-code framework or SDK versions, and do not replace template package references with guessed ones.
- Do not edit before the unchanged template builds.
- Keep your run configuration separate from the project sources: no agent wiring in the `.csproj`, no generated NC inside the source tree.
- Do not treat a zero exit code as verification, and do not report success without an NC file you compared.
- Do not change machine settings and do not transmit an NC program.

## Done means

The template copy builds unchanged with its SDK reference preserved, the typed change builds, a run through DotNet Posts or the batch runner produced an inspectable report and an NC file (or the limitation is recorded), the output was compared with the baseline, and the remaining verification is stated as still required.
