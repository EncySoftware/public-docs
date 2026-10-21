---
name: inspect-cldata
description: Read the actual CLData of a project — files, sections, commands and named parameters — instead of guessing from documentation. Use before changing any postprocessor code.
---

# Inspect CLData

## When to use

Whenever the task depends on the input data: a CLData command, a section, a parameter, the machine, the units, or the reason a block appears in the NC program. Always before editing an SPPX handler or a .NET handler.

## Tools

The CLData MCP server (`InpCoreMCP.exe`) is read-only and works without a running CAM system. The calls used below:

| Call | Purpose |
|---|---|
| `cld_open_project` | Open a `*.stcp` / `*.stc` project or a `*.inpcld` file; returns the project id, the machine, the units and the file list |
| `cld_list_files` | Files of the project with their command counts |
| `cld_get_skeleton` | Section tree of one file plus a histogram of command types inside each section |
| `cld_list_commands` | A range of commands as a listing, with `include_names` / `exclude_names` filters |
| `cld_get_command` | One command in full: raw array, named parameters, typed projection |
| `cld_find_command` | Find a command by name, optionally filtered by values |
| `cld_get_unique_command_names` | Which commands the project contains at all — that is, which handlers the postprocessor needs |
| `cld_find_parameter` / `cld_get_parameter` | Locate a parameter by name, then read it by exact path |
| `cld_get_machine_info` / `cld_get_project_parameter` | Machine description and project-level settings |

If no CLData tools are available, say so and ask for a reduced export; do not reconstruct the data from documentation.

When the answer is not in the CLData at all — how the machine is configured, what an operation was set to, which tool is mounted — and CAM tools are available, read it from the source project instead of inferring it. The same tools can prepare the input when the fixture you need does not exist yet: recalculate the toolpaths, export the CLData of the active project, create or open a test project. Say when you did this: regenerated data invalidates every command index you reported earlier.

## Workflow

1. `cld_open_project` on the project you were given. Record the project id, machine, units and file list, and report them — a mismatch here means you are inspecting the wrong data.
2. `cld_list_files` and check `command_count`. Never start by dumping a large file.
3. `cld_get_skeleton` for the file of interest. The skeleton shows the section tree and, in NC-subroutine files, the subroutine boundaries, with a per-section histogram. Note that it is order-free: read a range for order. On files with hundreds of thousands of commands this call is heavy but worth it — it also makes later indented listings cheap.
4. `cld_list_commands` over a bounded range to see order and context. Exclude the high-volume motion commands when they are not the subject (`exclude_names: ["GOTO"]`), or include only what you are looking for.
5. `cld_get_command` for the command itself. For a large parameter tree, use `cld_find_parameter` to locate the path and `cld_get_parameter` to read it, extending the path level by level instead of dumping the whole tree.
6. Choose the path dialect for the code you are going to write: `sppx` for the postprocessor language, `dotnet` for the .NET SDK. The same value has different index bases in the two dialects — 1-based in the SPPX form, 0-based in the typed .NET form. Returned paths are paste-ready in the dialect you asked for; do not translate them by hand.
7. Record what you found: file, section, command index, parameter paths, actual values, units, and what is absent. Absence in one fixture is not proof that a command never carries the parameter.
8. Show it to the user when it matters. The CLData Inspector opens the exact command:

   ```text
   vscode://postprocessor-tools.cldata-inspector/reveal?project=<path>&file=<index|name>&command=<index>&parameter=<name>&where=both
   ```

   Run it with `code --open-url "<link>"` and URL-encode the values. Inside VS Code the `cldata.reveal` command does the same and returns what was selected.

## Rules

- No full-file scans without a skeleton and a bounded range.
- Do not guess a subtype, an array index, a parameter name or a collection position — read it.
- Command indexes belong to one revision of the data. After the project is regenerated the server rereads it and asks you to repeat the call; results captured earlier are stale. Always report indexes together with the project.
- Never modify the project, its settings or the CLData while inspecting.
- Do not disclose unrelated customer data; ask for a reduced fixture instead.

## Done means

The project, file, section and command are identified; the required values were read through verified calls and reported with their paths and dialect; units and machine are known; and everything still unknown is listed as unknown, not filled in from documentation.
