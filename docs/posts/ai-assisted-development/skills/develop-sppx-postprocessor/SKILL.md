---
name: develop-sppx-postprocessor
description: Read, edit, compile and run an SPPX postprocessor through the InP MCP server — read-before-write, compile clean, run, compare with the baseline.
---

# Develop SPPX postprocessors

## When to use

Changes to an SPPX postprocessor: a command handler, a subroutine, an object, registers, masks, modal output, separators or subprogram behaviour. Run `inspect-cldata` first and `verify-nc-program` afterwards.

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
4. Generate the baseline if there is none: `pp_open_cld` then `pp_run`, and keep the NC output for comparison.
5. Plan the smallest edit and state the expected NC blocks, including the omitted, repeated and boundary cases.
6. `pp_set_code` with the full body — the code you read, with your change applied. It overwrites; a fragment destroys the rest of the item. Preserve register order and formatting, modal behaviour, separators, the state kept in `Common` and in local variables, and the existing subprogram conventions. Donor code from another postprocessor must be adapted to this project's actual data.
7. `pp_translate`. Fix every error. Report errors in postprocessor terms — frame, register, handler, G/M code — not as software stack traces.
8. `pp_open_cld` + `pp_run`. Compare the new NC output with the baseline and with the reference program, and trace every difference, including unintended ones, to a command and a handler.
9. Show the user what changed and hand over to `verify-nc-program`.

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
