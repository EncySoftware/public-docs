---
name: develop-sppx-postprocessor
description: Read, edit, compile and run an SPPX postprocessor through the InP MCP server — read-before-write, compile clean, run, compare with the baseline.
---

# Develop SPPX postprocessors

## When to use

Changes to an SPPX postprocessor: a command handler, a subroutine, an object, registers, masks, modal output, separators or subprogram behaviour. Run `inspect-cldata` first and `verify-nc-program` afterwards.

## Language foundation

Load `sppx-language-foundations` before interpreting or planning SPPX code. It provides compact language foundations for state, objects, runtime data, registers and output; it does not replace actual CLData, current postprocessor code, or versioned documentation.

Use the foundation for ordinary language forms. If the foundation, current code and actual CLData do not prove a required SPPX/InP semantic, follow the change-critical-unknowns workflow below: read the relevant documentation page before planning or editing.

## Tools and the order they go in

The InP MCP server (`inp-mcp-server.exe`) drives the postprocessor IDE. `pp_ping` first, always — it reports the server, the known instances and the default target.

| Call | Purpose |
|---|---|
| `pp_ping` | Health and instance list; call before anything else |
| `pp_launch` | Start an instance: `mode="windowed"` (default) or `"headless"`; `post_path` opens a postprocessor at once |
| `pp_instances` / `pp_select_instance` | List instances and pick a default; every call also takes `pid` |
| `pp_open_post` / `pp_create_post` | Open or create a postprocessor in the connected instance |
| `pp_get_structure` | Handlers, subroutines, objects, channels — item names come from here |
| `pp_get_code` / `pp_set_code` | Read an item; replace its full body |
| `pp_get_registers` / `pp_set_registers` | Register definitions |
| `pp_translate` | **Compile.** Run after every edit and fix every reported error before continuing |
| `pp_open_cld` + `pp_run` | Load a CLData project, then interpret it; `pp_run` returns the NC output |
| `pp_close` / `pp_kill` / `pp_delete` | Close an instance; force it down; delete an item — the last two are destructive |

Item kinds: `0` handler, `1` subroutine, `2` object. Handlers exist one per CLData command: they can be edited but not created or deleted. Only subroutines and objects can be created (`create=true`) or deleted.

If no instance is running, prefer `pp_launch` windowed when a person is watching, headless for batch work. If the server reports that the instance manager is unavailable, ask the user to open InP from the CAM system. If several instances are running, pass `pid` explicitly — an ambiguous call fails by design. Calls to one instance are serialized; `pp_translate` and `pp_run` can take minutes.

## Workflow

1. `pp_ping`. Get an instance, then `pp_open_post` if the postprocessor is not already open.
2. `pp_get_structure`. Find the handler for the CLData command from `inspect-cldata`. Remember that output may be emitted further down — in a subroutine, a mask or on the next modal change.
3. **Read before writing.** `pp_get_code` for every item you will change, `pp_get_registers` if registers are involved. Explain the current path from command to NC block before proposing an edit.
4. **Resolve change-critical unknowns.** Before planning an edit, make a short internal list of every fact the edit depends on but that is not yet evidenced: unclear request terms, unexplained code paths or side effects, unfamiliar SPPX constructs, CLData-to-output mapping, register/mask/format semantics, modal and reset lifecycle, version-sensitive InP behaviour, and conflicts between project data, code, notes or donor postprocessors. For each item, keep the unresolved fact, why it matters, required evidence, fact found and source, and status: `resolved`, `not applicable`, or `blocked`. Use actual CLData for input values, current code and a baseline run for current behaviour, authoritative documentation for SPPX/InP semantics, workspace notes for local conventions, and donor code only as a candidate example. Resolve every change-critical item before planning. For an unfamiliar SPPX construct, built-in object, method, syntax form or InP semantic, an item becomes `resolved` only after `cam_read_doc` has returned a documentation page and the agent has obtained a specific applicable fact from it. Use semantic documentation search for an unfamiliar concept and keyword search for an exact known term, then read the returned page in full. A search snippet, an intended lookup, general programming knowledge, the task description or a similar donor fragment does not resolve the item. Do not produce an implementation plan that names or relies on such a construct before this read succeeds. If the required documentation cannot be read, mark the item `blocked` and report the concrete limitation rather than proposing syntax. Do not plan or make an edit that depends on a `blocked` item. Keep this list internal unless it blocks safe completion.
5. Generate the baseline if there is none: `pp_open_cld` then `pp_run`, and keep the NC output separately from any reference NC program. Record the InP version, instance or `pid`, postprocessor path, CLData project path, baseline output location, and translation/run messages.
6. Plan the smallest edit and state the expected NC blocks. Cover omitted, repeated and boundary values plus every applicable state transition: first use, modal repeat/change, operation or tool boundary, subprogram boundary and reset.
7. `pp_set_code` with the full body — the code you read, with your change applied. It overwrites; a fragment destroys the rest of the item. Preserve register order and formatting, modal behaviour, separators, the state kept in `Common` and in local variables, and the existing subprogram conventions. Before borrowing code, verify its CLData input, register/mask meanings, modal-state assumptions and target control-system output against the current project.
8. `pp_translate`. Fix every error. Report errors in postprocessor terms — frame, register, handler, G/M code — not as software stack traces. If `pp_set_code` or `pp_translate` fails, reread the saved item before the next change and compare it with the body read before editing; do not assume a failed call left it unchanged.
9. `pp_open_cld` + `pp_run`. Record the changed output location and messages. Compare the new NC output with the baseline and with the reference program, and trace every difference, including unintended ones, to a command and a handler. Maintain the compact internal chain `CLData command and values -> changed SPPX item -> expected NC block -> observed NC difference -> evidence location`; reopen an assumption when generated NC contradicts its expected result.
10. Show the user what changed and hand over to `verify-nc-program`.

## Showing your work in VS Code

```text
vscode://postprocessor-tools.sppx-tools/goto?post=<path>&handler=<name>&line=<n>&beside=true
vscode://postprocessor-tools.sppx-tools/highlight?handler=<name>&line=3&endLine=7&message=<text>
vscode://postprocessor-tools.sppx-tools/run?post=<path>&config=Agent%20check&create=true&cldata=<path>&ncFilePath=<path>
```

Run links with `code --open-url "<link>"` and URL-encode the values. Address code by `handler` plus `line` or `find`, not by a raw file line. Highlights are cleared by any edit, so set them after the edit, not before. Inside VS Code the same actions are available as the `sppx.goto`, `sppx.highlight`, `sppx.symbols`, `sppx.whereAmI`, `sppx.status` and `sppx.run` commands, which return their result instead of just opening a view.

`pp_run` is your own silent check; the **Generate NC** panel is what the user watches. Create your own run configuration (`create=true`) rather than modifying the user's, and read `sppx.status` first to learn the post input parameter keys before setting values.

## Rules

- Never edit an item you have not read in this session.
- Never claim completion without `pp_run` output that you compared.
- Do not rewrite a whole postprocessor for a local fix, and do not silence a compile error by deleting code.
- `pp_delete` and `pp_kill` are irreversible: ask the user first, and prefer `pp_close`.
- Do not put .NET property syntax into SPPX code, and do not carry register defaults or CLD mappings over from another postprocessor unchecked.

## Done means

Read-before-write is evidenced, the diff is minimal, compilation is clean, `pp_run` produced NC output on the recorded project, the output was compared with the baseline and the reference, every difference is explained, and the remaining verification is stated as still required.
