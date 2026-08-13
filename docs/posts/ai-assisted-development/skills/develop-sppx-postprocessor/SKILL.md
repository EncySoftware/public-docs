---
name: develop-sppx-postprocessor
description: Safely adapt, compile, run, and compare an SPPX postprocessor using verified CLData and current SPPX tools.
---

# Develop SPPX postprocessors

## Trigger and when to use

Use this skill for SPPX masks, processing programs, registers, separators, modal logic, or subprogram behavior. Use it after CLData inspection and before NC verification.

## Prerequisites and tool discovery

- Identify the current SPPX source, installed CAM/Postprocessor generator, target machine/controller, reduced CLData fixture, and expected NC blocks.
- Discover current SPPX MCP/tool capabilities. The names and signatures below describe a safe pattern, not a promise of exact arguments. If the service is unavailable, use the installed UI or documented local runner and record the fallback.
- Confirm that the tool can perform the relevant operations before invoking them; if a capability is absent, use the installed UI or documented runner and report it.

## Safe workflow

1. Read the existing mask/program and relevant documentation before writing anything. Explain the current command-to-handler path.
2. Use the available `pp_ping` capability to confirm the SPPX service, then query available `instances` and select the intended installation explicitly.
3. Open or select the postprocessor and inspect its `structure` before editing. Read relevant source, registers, masks, and programs.
4. Inspect the real CLData fixture using `get`/inspection access; use `translate` only as a controlled baseline or comparison operation. Do not assume a fixed signature.
5. Define expected output for normal, omitted, repeated, and boundary values. Make the smallest source change and preserve register order, formatting, modal state, separators, local/Common/register state, and subprogram conventions.
6. Write only after the read-before-write review. Use the available `set`/edit operation or the supported local editor; retain a diff and do not overwrite unrelated content.
7. Compile with the installed SPPX tool, then use the available `open_cld` and `run` pattern (or the documented equivalent) on the reduced fixture. Capture diagnostics and generated files.
8. Compare output blocks to the baseline and expected result, trace every difference to a command/handler, and hand the result to NC verification.

## Prohibited and unsafe actions

- Never write before reading the target source and structure. Never invent exact MCP signatures, old HTTP endpoints, CLD mappings, or universal register defaults.
- Do not mix .NET property syntax into SPPX, rewrite a whole post for a local change, deploy automatically, bypass compile/runtime errors, or infer machine safety from output text.

## Completion criteria

The source diff is minimal, read-before-write is evidenced, the selected instance and actual CLData are known, compile/run results are captured, expected and actual NC are compared, and remaining verification risk is explicit.

## User-visible presentation

Show the selected instance/tool versions, changed mask/program and rationale, concise diff, compile and run diagnostics, baseline-versus-new NC blocks, and any unavailable operation or required human review.
