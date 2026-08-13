# .NET workflow

Use this workflow for C# postprocessors based on the .NET postprocessing API. The workflow is object-oriented and typed, but it still consumes the same CLData hierarchy as SPPX.

## Start from the SDK template

Copy the .NET postprocessor template supplied with the installed CAM system or SDK into a new working folder. Treat the untouched copy as the baseline. Do not assume a fixed .NET SDK version: use the version and project settings required by the installed template and product release. Preserve the template's project files, package references, generated files, and build instructions unless the documentation for that release says otherwise.

1. Copy the template to a new folder and place it under version control.
2. Open the copied folder in Visual Studio Code.
3. Build the unmodified template first and retain its output as the baseline.
4. Locate the handler for the CLData command to change.
5. Ask for a small typed change and include the expected output.
6. Build, debug with representative CLData, and inspect the generated NC program.

## API boundaries

Use .NET property and method names from the installed SDK reference. Do not infer a typed property from a raw CLD index when the SDK provides a named value. Keep compatibility decisions tied to the copied template and installed SDK rather than hard-coding a version in this guide.

## Beta runner requirements

For the current beta, the InpCore fallback must support `-settingsdump` and
produce the required JSONL settings output. Check the installed executable by
running its documented help or settings-dump procedure before a workflow that
depends on it. A missing switch or non-JSONL result is an unsupported runner;
record the limitation instead of guessing an alternative.

DotNet Posts 0.2.0 API operations must be used in the order advertised by the
installed integration: discover/status, setup when needed, then inspection,
build/run, and diagnostics. Keep the agent/client configuration separate from
the postprocessor project's `.csproj` and source files. Do not add tool wiring
to the template unless the installed integration explicitly requires it.

## AI-specific checks

Review null and boundary handling, file encoding, culture-sensitive formatting, modal state, tool compensation, coordinate transformations, and exception paths. Generated C# must be compiled and exercised with representative operations before it is trusted.
