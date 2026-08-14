# What the extensions give you

Three extensions do the work you see: one for editing and running SPPX postprocessors, one for looking at the input data, one for C# postprocessors. The assistant drives the same commands, but they are ordinary VS Code features — this page is what to expect from them and where to find it.

Commands are run from the command palette: `F1` (or `Ctrl+Shift+P`), then start typing the name. Commands whose title ends with **(agent API)** exist for the assistant; you never need them by hand.

## SPPX Postprocessor Tools

### Editing

Open a `*.sppx` file and you get the XML structure and the handler code highlighted as two different languages. The XML wrapper is folded away, so the file reads as a list of handlers with their code. The **Outline** view lists handlers, subroutines and registers and navigates to them, `F12` jumps to a definition, completion and signature help cover the built-in language, and syntax errors are underlined as you type.

If VS Code restores an old folding layout and the file looks wrong, run **SPPX: Unfold Code (reset folding to default layout)**.

### Generating an NC program

The **Generate NC** panel is the main working surface. With a `*.sppx` file open, it opens from the triangular play button in the editor title bar — hover it and the tooltip reads **SPPX: Generate NC Program** — or from the command of the same name in the palette.

In the panel:

- named run configurations — the CAM project to process, the output file, and the postprocessor's own input parameters, shown with their captions rather than internal names;
- **Run**, with progress while the generation goes on;
- errors and warnings in the **Problems** view, each linking to the line in the handler that produced it;
- the generated program, with diffs against the previous run and against a reference program you point at.

Buttons next to **Run** open the CLData of the current configuration in the Inspector — the project name opens it in the sidebar, the arrow in a panel below the editor. The same is available as **SPPX: Inspect CLData of the Current Run Configuration**.

Two more commands are worth knowing: **SPPX: Open in Postprocessors Generator IDE** opens the same postprocessor in InP, and **SPPX: Clean Stored Run Data** discards the stored run state if a configuration gets into a bad shape.

## CLData Inspector

This is where you see what actually arrives at the postprocessor. Its icon in the activity bar opens three views:

- **Files** — the files of the opened project with their command counts. The view's buttons open a CAM project (`*.stcp`, `*.stc`) or a single `*.inpcld` file, reopen a recent one, reload the project after it was regenerated, and open the wide inspector tab in the editor area.
- **Commands** — the commands of the selected file, grouped by structure sections; in NC-subroutine files, by subroutine boundaries. `Ctrl+F` in the view, or **CLData: Find Command…**, searches on the server side, so it stays usable on files with hundreds of thousands of commands.
- **Parameters** — `Key = Value` for the selected command: the raw array, the named parameters, and the typed .NET view. **CLData: Toggle .NET Parameter View** switches the last one on and off.

Right-click a parameter to copy what you need for code: **Copy Name (sppx)** and **Copy Name (.NET)** give the exact form to paste into a handler, and **Copy Value** the value itself. On a command, **Copy Caption** copies its human-readable name.

The assistant can open a specific file, command or parameter here when it wants to show you something — see [Develop in Visual Studio Code](vscode.md).

## DotNet Posts

For C# postprocessors, with the same **Generate NC** panel as SPPX Tools — configurations, input parameters, progress, results and diffs.

Two ways to start a generation:

- **DotNet Posts: Generate NC Program**, or the triangular play button in the editor title bar of a C# file (its tooltip carries the same name) — works with the postprocessor project open in the workspace and finds the built assembly itself;
- **DotNet Posts: Generate NC Program from DLL…**, or a right-click on a `.dll` in the **Explorer** — runs a compiled postprocessor without any sources. Several postprocessors can be kept in separate panel tabs and compared on the same project.

**DotNet Posts: Reveal Postprocessor Handler** opens the handler that processes a given command. The `dotnetPosts.autoBuild` setting builds the project before each run, so a change is never tested against a stale assembly.

## Postprocessor Tools updater

The updater has no interface of its own. When a new version is available, the postprocessor panels show an update action; accept it and reload the window. The same check is available from the palette — see [Advanced setup](advanced-setup.md#updates-on-demand).

## Settings

Each extension's settings page starts with the folder where the CAM system is installed — that is the one setting that has to be right for anything to work. [Advanced setup](advanced-setup.md#point-the-extensions-at-the-cam-installation) lists all three and the picker that fills them in.
