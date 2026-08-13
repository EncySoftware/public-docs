# SPPX workflow

Use this workflow for mask-based postprocessors written in SPPX. SPPX reads the same CLData as .NET, but uses its own commands, masks, registers, and language syntax.

## Develop a change

1. Identify the CLData command and its parameters.
2. Find the existing SPPX program or mask that handles the command.
3. Ask the assistant to explain the current path before changing it.
4. Request a minimal mask or program change with an explicit example of expected NC output.
5. Discover the installed Postprocessors generator and its advertised SPPX operations; use the supported UI or local runner when no SPPX MCP operation is available.
6. Generate test NC code with that supported path.
7. Compare the result with the expected blocks, then test omitted, repeated, and boundary values.

Do not mix .NET property names with SPPX syntax. The shared CLData pages describe the command semantics; the SPPX pages describe the access form.

## AI-specific checks

Ask the assistant to preserve register formatting, modal behavior, subprogram handling, and existing mask conventions. Review every conditional branch and every direct output operation. If the SPPX service, selected instance, or runner is unavailable, fall back to the installed UI/documented local tool and record that path. A plausible-looking mask can still emit unsafe or incomplete machine code.

## Useful context

Provide the relevant mask, the command description, a short CLData listing, and a known-good output sample. Do not provide an entire customer project when a reduced example is sufficient.
