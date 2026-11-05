---
name: verify-interpretation
description: Proves what an interpreter change does — runs every reference NC program before and after, compares the simulated commands and the CAM log, checks every product version — states how far the check went, and prepares a package the customer can use with their own product. Use before presenting any interpreter change and before handing an interpreter over.
---

# Verify interpretation

## When to use

Before an interpreter change is presented as a result, and before an interpreter is handed to a colleague or a customer
— regardless of how cleanly it built.

## What you need

The reference NC programs ("Inspect NC programs" (`inspect-nc-programs`)), the CAM project with the machine, the
interpreter built before and after the change, the products it must run in, and the expected behavior. If there is no
result of the unchanged interpreter yet, produce one first: without a baseline every difference is unexplained.

## State how far the check went

Report exactly one of these, and never upgrade it without the evidence:

| State | Requires |
|---|---|
| **Not verified** | only a plan, a diff or a build exists |
| **Technically verified** | the interpreter loaded and the programs ran; the log and the simulated commands are kept, but not compared or reviewed |
| **Verified on the reference programs** | all reference programs ran before and after, every difference is explained, the warnings of the CAM log are reviewed, every targeted product version was checked |
| **Accepted for the machine** | the user or the customer confirmed the simulation for a specific machine — you cannot assign this state |

## Workflow

1. Get or produce the baseline: the result of the unchanged interpreter on all reference programs.
2. Run all reference programs through the changed interpreter.
3. Compare the summaries, then the simulated commands, then the warnings (below).
4. Repeat for every product version the interpreter targets.
5. State the verification state with its evidence.
6. For a hand-over, prepare the package and run its checks.

## Run the programs

To run one program by hand: in the CAM system create an operation that works by an NC program, paste or load the
program, choose the interpreter in the operation's strategy, calculate the operation, then read the simulation and the
CAM log. Do this to look at one block; do not rely on it for the whole set.

Turn on **Use logs** and **Use log interaction with the interpreter** before any run (System setup → Additional → Logs,
the same in the CAM system and in Tuner). Without them the CAM log has none of the kernel's messages about the words it
reads and none of the lines the interpreter writes with `Kernel.Log`, and a comparison of warnings compares nothing.

Running a program by hand in the CAM system for every change does not scale. A runner can do it without the user
clicking: it opens the CAM project, creates an operation that simulates an NC program with the interpreter, calculates
it, writes the simulated commands to a text file and copies the CAM log of that run next to it. Build a runner only on
the public programming interface that the CAM system documents and installs: its interface for external applications
(CAMIPC), with which a program of your own starts the CAM system or connects to a running one. Find its description in
the documentation of the user's product (the section on the CAM API) and use only the calls, classes and operation
parameters described there — never guess one. Where the documentation does not show how to do a step (for example, how
to load the program of an NC operation or choose its interpreter), or for Tuner, which has no documented interface of
this kind, the run is manual: the user calculates the operations, and you prepare the list of programs and the steps,
then collect and compare the results. Keep a runner in the interpreter's repository, in a folder of its own with its own
README, and never ship it to a customer.

For every program keep: the simulated commands, the warnings and errors of the CAM log, and a one-line summary (errors,
warnings, exceptions, skipped words, number of commands). Run the programs one after another: runs in one process of the
CAM system write into one log file, and parallel processes can fail to start the kernel at all. A full set of programs
can take an hour: tell the user how long before you start.

What a good runner also does:

- runs every NC operation of a project in sequence, as the CAM system does, and reports every channel, not only the
  first;
- captures the interpreter's warnings and notifications, so their text is checked, not only their rules;
- stops a run that hangs after a timeout;
- judges a run by the result line it wrote, not by the exit code: the product may crash on unload after the result is
  complete;
- copies the CAM log right after each run and checks by its time or a marker line that it belongs to that run before
  reading it;
- runs from a copy of the build output, never from the folder you are building into, so a rebuild cannot replace the DLL
  in the middle of a set;
- never saves the reference project: record its hash and check it before each set. A project saved by a newer version
  of Tuner cannot be opened by older versions of Tuner or of the CAM system, so keep the reference project in the format
  of the oldest version you check;
- reads the log knowing how it is written: it is rotated in parts (older parts move to a `RotatedLogs` folder next to
  it), and with the interaction log on, a large project writes about a gigabyte. Search the rotated parts too, open the
  active file for reading with shared access, and do not judge freshness by the file's modification time — it lags
  behind.

**Prove the runner before trusting it.** Run a program with a deliberate error and a deliberate unknown word and check
that the runner counts both — a summary of "0 errors" from a counter that reads the wrong field of the log proves
nothing. Keep multi-line log events whole. The same applies to every automatic check, a linter or a name search: give
it a case it must catch first. Before blaming the interpreter for a crash or an exit code, repeat it with the unchanged
template interpreter and check the runner's own inputs.

## Compare

1. Compare the summaries of all programs before and after. A changed number of warnings or commands in a program the
   change was not meant for is the first thing to explain.
2. For every changed program, diff the simulated commands and start at the first difference. Trace it to the block and
   the word that produced it. An unintended difference matters more than an intended one.
3. Read the warnings, not only their count. Each warning names a word, an axis or a cycle; check that the ones left are
   expected (a word the machine schema does not have, a cycle that is not simulated) and written in the README.
4. Test the edges the programs do not cover with a short program of your own: the word with every spelling found by the
   census, at its limits, missing, repeated, in an unusual order. Build it from the header of a real program of the same
   operation (tool, spindle, coordinate system, plane) and replace only the blocks under test: without the header such a
   program may produce no motion at all. Keep these programs in the repository next to the runner, not in a temporary
   folder — they are the test set of the next change.
5. A difference that is caused by the test setup and not by the interpreter (another coordinate system of the test
   operation, a different machine in the project, an operation of another kind — turning instead of milling) is not a
   result: say what it is and leave it out. The runner must create the operation with the same kind and coordinate
   system as the real one.
6. Some differences between the CAM system and Tuner come from the product, not from the interpreter: Tuner does not run
   the CAM end template of an operation, so the spindle, coolant and compensation stay on until the program itself
   switches them off (`M5`, `M9`); a project setting of Tuner skips the first physical move (on by default and hidden
   for robots and multi-channel projects). Check these settings before reporting such a difference.

Some results vary between two runs of the same input — a warning that appears in one program in one run and in another
in the next. Run the program alone again before calling it a regression.

Say where the baseline comes from: the original interpreter, or a re-implementation of its logic. Only the first is a
baseline of the behavior the user had.

## Check through the postprocessor

When the customer's postprocessor and a CAM project are available, close the loop: postprocess the project's operations,
run the resulting programs through the interpreter and compare the simulation with the operation's own toolpath. If the
operations output cycles as plain moves, switch them to canned-cycle output first to get real cycle calls. A difference
may be a defect of the postprocessor — a missing jump over contour blocks, a cycle variant the manual does not allow.
The interpreter simulates what the control would do with the program, not what the CAM operation meant: report such a
defect to the postprocessor's author with the evidence instead of hiding it in the interpreter.

## Review for safety

Before a hand-over, review every change for cases where the simulation looks safer than the machine will be: a retract
that is skipped, a start point that was assumed, material that is not shown, a cycle that is not simulated but leaves
the operation looking complete. Test each case with a short program. After every round of review fixes run the whole set
of programs again: fixes made during a review are a common source of regressions.

## Check every product version

Build and run for every product version and architecture the interpreter targets, in the CAM system and in Tuner where
both are targeted. For native DLLs, build and load the Win64 binary (and a Win32 one only if a 32-bit product is
targeted) and verify the exports, `.snci` fields and `LibraryID`/`GetIdentifier` pair. For .NET, each product version
has its own .NET version and SDK package (see "The SDK package and the product versions" in "Develop .NET interpreters"
(`develop-dotnet-interpreter`)). Where a version cannot be run on this computer, say so instead of implying it was
checked.

## Native checks

For a native interpreter, keep a Win32 output, if there is one, apart from the Win64 one, test the matching `.snci` on
an unchanged installation, and verify `NCT_GetInterface`, `NCT_FreeMemory`, parent loading and protected
`.dat`/`INCT_Connect` behavior when applicable. Compilation without a loaded simulation is not verification.

## Prepare the package

What a customer gets is one folder per product version with the `.snci`, the interpreter DLL and
`InterpreterSettings.ini` kept together — and the `.deps.json` only if loading needs it, which you check on an unchanged
installation. The build output holds more than that: the SDK package copies
`STNCInterpreterSDKProject.stbuildresult.json` into it, which holds build metadata that does not belong to the customer,
and there are `.pdb` and SDK `.xml` files and, after `publish`, the SDK DLLs (the helper, `STNC*.dll`,
`Geometry.VecMatrLib.dll`, `InteropTypes.dll`, `STTypes.dll`), which the product ships itself. Copy the files you need
by name instead of zipping the output folder. Build the delivered DLL without debug information or with deterministic
path mapping: a normal build writes the path of the local `.pdb` into the DLL. Add a README in plain language and in the
customer's language — what is supported, the limits, the settings, how to debug, which folder fits which product
version, whether the product needs a license option to load a custom interpreter, what the simulation cannot know (where
the machine stands before the program, parameters set on the control), and which simplifications are deliberate, such as
skipped commands, so they are not taken for defects. The README describes only what is in the package. When the customer
asks for them, add the sources without `bin` and `obj`; check that they build from a clean copy with an empty package
cache and only the public package source.

Before it leaves:

- **No names that do not belong to this customer.** Search the content of every file in the package, inside the
  archive, for the names of other customers, of this computer and its users, and of internal servers and package feeds —
  in file names, paths, settings, launch configurations, package references, comments and the README. Search the bytes
  of each file in both encodings Windows programs use for text (UTF-8 and UTF-16), starting at every position, not the
  text an editor shows: strings inside a DLL are not aligned, and decoding a whole binary file loses some of them. Add a
  control word you know is present and check that the search finds it.
- **No traces of this computer.** No user names, home folders, internal servers or internal package feeds in any file;
  launch configurations point at the standard installation folders of the products, not at folders of this computer.
- **The customer can build it.** The SDK package version in the project is a released one, available on the public
  package feed of the product's vendor; your own test tools (the program runner, scripts, test programs of other
  customers) are not in the package.
- **It works on an unchanged installation.** The package must not depend on files you changed in the product or on a
  package version the customer cannot download.
- **The search covers everything sent**, not only the archive: a postprocessor or a document sent next to it too.
- **Archive entry names use `/`** as the separator, so the archive unpacks the same on every system.
- Build the package from sources saved in version control (a commit) — commit first, then build. Keep a delivery log
  (date, commit, archive hash, recipient), so the next list of changes is written against what the customer actually
  has.

## Rules

- A successful build, a zero exit code or a plausible-looking toolpath is not verification.
- Do not change the reference programs, the machine or the project to make a comparison pass.
- Do not describe a result as accepted for a machine, and do not send a package anywhere without the user's explicit
  permission.
- Do not claim a check on a product version, a machine or a simulation that was not run.
- Before reporting a task as done, go through the written list of the user's requests (see "The workspace" in
  "Interpreter development" (`interpreter-development`)) and give the evidence for each; an item without evidence is
  reported as not done or not verified.

## Done means

All reference programs were run before and after, every difference is explained at block level, the remaining warnings
are reviewed and documented, the runner and every automatic check were proven on a case they must catch, the change was
reviewed for cases where the simulation looks safer than the machine, every targeted product version was built and run
or its gap is stated, the verification state is stated with its evidence, and — for a hand-over — the package passed the
name, trace and unchanged-installation checks.
