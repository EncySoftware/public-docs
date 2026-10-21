# Review and verify

AI assistance changes how a draft is produced. It does not change how a postprocessor is accepted. A successful build and a clean run prove that the tools worked — nothing more.

## Say how far the check went

Use one of four states, and keep the evidence for it. The point is to make an unfinished check visible instead of calling everything "done".

| State | What it means |
|---|---|
| **Not verified** | There is a plan, a diff or a build, but the postprocessor was not run on a recorded project |
| **Technically verified** | The run completed as expected and the log, result code and generated file are kept; the content of the NC program has not been reviewed |
| **Verified on a test project** | The baseline and the new NC program were compared on the normal test operations and applicable boundary cases — such as program start and end, operation or tool transitions, repeated modal commands, and minimum or maximum parameter values — and the machine parameters were checked |
| **Approved for production** | A qualified engineer confirmed the program for a specific machine, control system and application |

Only the last state allows production use, and only a person can grant it. Never describe a result as ready or safe on the strength of a process exit code.

## Review the source change

- The diff contains the requested change and nothing else — no reformatting, no unrelated rewrites.
- Command names, parameters, units, coordinate systems and modal assumptions match the CLData reference and the actual project data.
- The postprocessor compiles, and the compile messages were read rather than skipped.
- Normal, omitted, repeated, maximum and unsupported inputs were exercised, not only the one case in the fixture.
- Output file name, encoding, line endings and error handling are as the machine expects.

## Review the NC program

Compare against a known-good program and start at the first differing block; a difference early in the program often explains everything after it. Trace each difference back to the CLData command and the handler that produced it.

Check the program as a whole:

- the selected machine, control system, units and work coordinate system;
- program start and end, including the final positioning and program stop;
- tool changes, spindle, feeds, coolant and safe positions;
- signs, axis order, compensation, work offsets and retracts;
- cycles, subprograms, rotary motion, limits and synchronization;
- no unexpected motion, no missing commands, no leftover blocks;
- the program still corresponds to the original toolpath, on the test section and on the boundary cases.

Then run it through the simulator and through the machine-specific verification you normally use. Investigate warnings instead of suppressing them.

## Keep the evidence

Store the source diff, the input project, the postprocessor version, the run report and the generated program together, and record who reviewed it and when. When a problem surfaces later, this is what makes it possible to tell a postprocessor change from a data change.

## What the assistant must not do

It must not approve code, change machine configuration to make output pass, bypass a check, or transmit a program to a control system. Human approval stays between the generated output and production use.
