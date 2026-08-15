---
name: verify-nc-program
description: Review a generated NC program and the change behind it, state how far the check went, and leave production approval to a qualified person.
---

# Verify NC programs

## When to use

Before any generated or changed NC program is presented as a result — SPPX or .NET, regardless of how cleanly it built.

## What you need

The source diff, the postprocessor and tool versions, the project the program was generated from, the baseline NC program, the new NC program, the machine and control system, and the expected behaviour. If the baseline is missing, generate one from the unchanged postprocessor before comparing.

## State how far the check went

Report exactly one of these, and never upgrade it without the evidence:

| State | Requires |
|---|---|
| **Not verified** | Only a plan, a diff or a build exists |
| **Technically verified** | The run completed, and the log, result code and generated file are kept; the NC content has not been reviewed |
| **Verified on a test project** | Baseline and new program compared on the test and boundary sections, machine parameters checked |
| **Approved for production** | A qualified person confirmed it for a specific machine and control system — you cannot assign this state |

## Workflow

1. Check that the diff contains the requested change and nothing else, and that output file name, encoding, line endings and error handling are as expected.
2. Reproduce the run from the recorded project. Exercise the cases the fixture does not cover as far as the data allows: omitted, repeated, maximum and unsupported values.
3. Diff the programs and start at the first differing block. Trace each difference to a CLData command and the code that produced it. Unintended differences matter more than intended ones.
4. Review the program as a whole: machine, control system, units and work coordinate system; program start and end; tool changes, spindle, feeds, coolant, safe positions; signs, axis order, compensation, work offsets, retracts; cycles, subprograms, rotary motion, limits, synchronization; and whether the program still corresponds to the original toolpath.
5. Name what only a person or a simulator can settle, and say so plainly instead of implying it was covered.
6. Report the state from the table, with the evidence and its location.

## Rules

- Compilation, a zero exit code, a plausible-looking listing and a matching text diff are not verification.
- Do not suppress warnings to make output pass, and do not change machine configuration or postprocessor settings to make a comparison succeed.
- Do not transmit a program to a control system, and do not describe a result as safe or production-ready.
- Do not claim simulation or machine checks that were not run.

## Done means

The source and NC diffs were reviewed, differences are explained at command level, the reachable edge cases were exercised, the verification state is stated with its evidence, and the checks left to the user — simulation, machine verification, approval — are named explicitly.
