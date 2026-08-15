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

## Command lines

There is no MCP server for .NET postprocessors, so when DotNet Posts is unavailable you drive the same programs yourself. `InpCore.exe` lives in the CAM installation — the folder in `dotnetPosts.installationFolder`, or its `Bin64`. Quote any path that contains spaces.

Take that path from the setting or from what the user tells you, and name the executable you used in your report. There is also an `InpCoreDir` environment variable, but treat it as a hint, not as the answer: the CLData Viewer writes it when it starts, so on a computer with several CAM versions installed it holds whichever installation's viewer ran last — which may not be the one the user is working with. The trap is quiet, because a run against the wrong version usually succeeds and merely produces different output.

Debugging from the editor is covered: the template's `F5` configuration is written in terms of `${env:InpCoreDir}`, but the DotNet Posts extension substitutes the path from `dotnetPosts.installationFolder` when the session starts, and warns once if the two disagree. The variable remains the fallback when the setting is empty. Remember that changing it does not reach programs that are already running — in practice it takes signing out of Windows and back in.

**Build.**

```text
dotnet build "<folder>\<Name>.csproj"
```

The template's own build task adds `/property:GenerateFullPaths=true /consoleloggerparameters:NoSummary`, which makes the compiler report full paths and stops duplicate error summaries — use the same flags when you intend to parse the output.

**Extract `Settings.xml` from a compiled postprocessor.** Needed when you have the DLL but no sources; a project of your own already carries its settings file.

```text
InpCore.exe -settingsdump -postfile:"<folder>\bin\Debug\<Name>.dll" -settingsfile:"<folder>\Settings.xml"
```

A non-zero exit code, or a settings file that is not there afterwards, means the extraction failed — report the version limitation instead of writing a settings file by hand.

**Generate an NC program.**

```text
InpCore.exe -batchmode -postfile:"<...>\<Name>.dll" -cldfile:"<project>.stcp" -settingsfile:"<...>\Settings.xml"
```

Progress and results are written as JSONL next to the settings file, as `<settings file>.events.jsonl`: one JSON object per line, with `event`, and depending on it `percent`, `severity`, `text`, `path`, `success`, `resultCode` and `durationMs`. The `file` event carries the path of what was written; the closing `done` event carries `success` and `resultCode`. Read that file rather than the console output.

Two rules about the result. A run counts as successful only when `done.success` is true **and** the process exit code is 0; if events appeared but no `done` did, the runner stopped early and the NC file, if any, is not to be trusted. And the output path is not a command-line argument: the NC file name and directory are parameters of the settings file, so set them there before the run.

Where the human is meant to watch instead, the template's `F5` configuration runs `InpCore.exe -cldviewermode -sharedfile:STInpCoreOfDebugger -postfile:...` with the build task in front of it. That is the debugging path, not a batch run — do not mix the two.

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
