---
name: verify-nc-program
description: Independently review generated NC code and its source change; require simulation and human approval before production use.
---

# Verify NC programs

## Trigger and when to use

Use this skill for every generated or changed NC program before acceptance, regardless of whether the source is SPPX or .NET and regardless of build success.

## Prerequisites and tool discovery

- Obtain the source diff, postprocessor/tool versions, actual CLData fixture, baseline NC, new NC, machine/controller context, and expected behavior.
- Discover the available generator/runner, CLData-to-output trace, simulator, machine-specific verification, and diff tools. Record their versions and do not claim unsupported checks.
- Ensure a qualified human reviewer can approve the result; simulation and review are not delegated to the agent.

## Safe workflow

1. Confirm the diff contains only the requested change and that source, encoding, line endings, output names, and error handling are appropriate.
2. Re-run or reproduce the postprocessor from the recorded fixture. Test normal, empty, omitted, repeated, maximum, unsupported, and boundary inputs as relevant.
3. Compare baseline and new NC, starting at the first differing block. Trace differences to CLData commands and handlers.
4. Review headers, tool changes, spindle, coolant, feeds, work offsets, units, coordinate transforms, compensation, retracts, rotary axes, limits, subprograms, synchronization, program end, and error behavior.
5. Run the complete result through the appropriate simulator and machine-specific verification. Investigate warnings rather than suppressing them.
6. Have a human inspect and approve the evidence before production use; record reviewer, date, fixture, source revision, and tool versions.

Classify each check as **Verified** (reproduced with recorded evidence),
**Partially verified** (some evidence exists but a required case or tool is
missing), **Unverified** (not run or inferred), or **Blocked** (a required
check failed or evidence is missing). Compilation, a successful runner exit,
and a text comparison are not machine-safety verification.

## Prohibited and unsafe actions

- Do not certify NC from compilation, a zero exit code, a text diff, or a visual plausibility check alone.
- Do not skip simulation, ignore warnings, bypass interlocks, change machine configuration to make output pass, transmit code to a controller, or authorize production autonomously.

## Completion criteria

Completion requires source and NC diffs, representative edge-case results, command-level investigation of differences, successful applicable simulation/machine verification, and explicit human approval. If any item is unavailable, mark the program not accepted.

## User-visible presentation

Present a pass/fail checklist, first differences and their causes, safety-relevant observations, simulator and machine-verification results, evidence locations, reviewer, and any blocked or unverified item. State plainly that passing this skill is not a substitute for site procedures.
