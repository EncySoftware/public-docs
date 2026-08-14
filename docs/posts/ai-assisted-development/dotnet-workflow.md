# .NET workflow

A .NET postprocessor is a C# project built against the postprocessing SDK: typed handlers, a `.csproj`, and a compiled assembly that the batch runner executes. The assistant works here as it does in any C# project — with the C# extension providing the language service and `dotnet` doing the build — and the postprocessor-specific parts are the template, the settings file and the runner.

For the API, see the .NET postprocessors documentation; for the input data, see the [CLData reference](../cldata/cldata.md).

## Where to start

Most of the time, not from scratch. Take the closest postprocessor that already exists — one supplied with the CAM system, or one written earlier for a similar machine or control system — copy it, and adapt it. You start from code that already works, and the differences you have to reason about are the ones that actually matter.

If a new postprocessor really is needed, create it in the CLData Viewer: **CLData viewer → Create new postprocessor → Simple postprocessor…**, then pick an empty folder — its name becomes the name of the postprocessor. The project is created for you, and its context menu opens it in VS Code. The .NET postprocessors documentation describes this in "How to prepare the computer to start writing the postprocessors". Ask the assistant only if you want it done from the templates instead — that is its job, not yours.

Work on it with VS Code opened on the postprocessor's own folder — the C# language service, the build and the debugger expect that. Keeping your standing brief and your notes reachable from there takes one arrangement, described in [Organize your workspace](workspace.md#when-the-open-folder-has-to-be-the-postprocessor).

Either way, start from a known state:

1. Put the postprocessor under version control before changing anything.
2. Build it unchanged. If it does not build as it is, no later diagnosis is worth anything.
3. Generate an NC program from it and keep that as the baseline for comparison.

## The cycle

1. Inspect the test project's CLData and find the command you need. The Inspector shows every command in the typed .NET projection as well — the interface, the handler name and the property values — and can copy a parameter name in the form you paste into C# code.
2. Locate the typed handler for that command. Ask the assistant to list the handlers of the project and open the relevant one.
3. Make one small change, with the expected NC output stated in advance. Use the named typed properties from the SDK rather than raw indexes when the SDK provides them.
4. Build. Treat warnings as information about your change, not as noise to be silenced.
5. Run on the test project and read the run report: the NC file it produced, the messages, the result code.
6. Compare the generated program with the baseline and continue with [Review and verify](review-and-verify.md).

## Running from VS Code

DotNet Posts drives the run and reports it back in the **Generate NC** panel, the same way SPPX Tools does. Two entry points cover both situations: **Generate NC Program** works with the postprocessor project open in the workspace and finds the built assembly itself, and **Generate NC Program from DLL…** takes a compiled postprocessor you point at, without any sources — which also means you can keep several postprocessors in separate **Generate NC** tabs and compare their output on the same project.

`dotnetPosts.autoBuild` makes the extension build the project before a run, so an edit is never tested against a stale assembly. The panel also has the commands the assistant uses to work with you: listing and opening handlers, highlighting a range of code, reporting where your cursor is, and opening the current CLData in the Inspector.

## Running a postprocessor you have no sources for

A postprocessor carries its default settings inside the assembly, and the runner can write them out as a `Settings.xml` next to the input — which is what makes **Generate NC Program from DLL…** possible. Use the file the runner produced; the format is not the same as the SPPX one, so a hand-written file will not do. If settings cannot be extracted, the installed CAM system is older than this workflow needs — check its version before suspecting the postprocessor.

A run counts as finished only when the report and the process result agree. A run that ended silently produced nothing worth comparing.

## What to check in the code

Review null handling and boundary values, units, culture-sensitive number formatting, the encoding and line endings of the output file, modal state kept between commands, tool compensation, coordinate transformations, and the exception paths. Generated C# has to be built and exercised on representative data before it is trusted — for a typed API the compiler catches a smaller share of the real mistakes than it appears to.
