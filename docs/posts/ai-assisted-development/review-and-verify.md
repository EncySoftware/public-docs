# Review and verify

AI assistance changes how drafts are produced, not how postprocessors are approved. Use an independent review path for every source change.

## Source review

- Confirm that the diff contains only the requested change.
- Check the command, parameter names, units, coordinate systems, and modal assumptions against CLData documentation.
- Compile or generate the postprocessor with the installed tools.
- Exercise normal, empty, repeated, maximum, and unsupported inputs.
- Check file encoding, line endings, output file names, and error handling.

Classify evidence instead of using a single pass label:

- **Verified**: reproduced with the recorded tool, fixture, and version.
- **Partially verified**: some checks passed, but a required input, runner, or
  edge case was unavailable.
- **Unverified**: inferred, mocked, or not run.
- **Blocked**: the result cannot be accepted because a required check failed or
  evidence is missing.

Compilation, a successful tool exit, and a matching text sample are source or
functional evidence only. They are not machine-safety verification.

## NC and machine review

Compare generated blocks with a known-good result. Inspect tool changes, spindle and coolant states, compensation, work offsets, retracts, rotary motion, subprogram calls, and program end. Run the result through the appropriate simulator and machine-specific verification. Mark each result with the classification above; missing simulation or machine verification is **Blocked**, not passed.

## Trust boundaries

Do not allow an assistant to approve code, change machine configuration, bypass a safety check, or transmit a program to a controller. Keep human approval between generated output and production use. Record the tool versions, source revision, test input, and reviewer when the change matters operationally.
