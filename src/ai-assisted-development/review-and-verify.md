# Checking and confirming the result

AI assistance changes how a draft is produced. It does not change how an interpreter is accepted. A successful build and a simulation without errors prove that the programs ran — and nothing more.

## State how far the check has gone

Use one of four states and keep the evidence for it. The point is that an unfinished check stays visible, not that everything is called "done".

| State | What it means |
|---|---|
| **Not verified** | There is a plan, changes or a build, but no NC programs have been run through the interpreter |
| **Technically verified** | The interpreter loaded, the programs ran, the log and the simulated commands are saved, but they have not been compared or analyzed |
| **Verified on reference programs** | All programs have been run before and after the change, every difference is explained, the log warnings have been read, all product versions the interpreter is intended for have been checked |
| **Accepted for the machine** | You or the customer confirmed the simulation for the particular machine |

Only a person assigns the last state. Never describe a result as finished on the strength of an exit code or a plausible tool path.

## Running the programs

Before any run, turn on the log as described in [advanced setup](advanced-setup.md#build-and-debugging-tools): without it there is nothing to compare the warnings with.

One program can be checked by hand: create a G-code based operation, select the interpreter, calculate the operation, then look at the simulation and the log. Doing this for the whole set after every change takes too long. The assistant can make a small run program that, without your clicks, opens the project, simulates each NC program with the interpreter and saves the simulated commands and the log of that run. It may be built only on the public programming interface of the CAM system for external applications, CAMIPC: it is described in the [CAM API documentation](https://docs.encycam.com/technical/CAMAPI/3/en/src/ExternalApplications/Main.html), and the library for connecting to the CAM system comes with its installation. Where the documentation does not show a step (for example, how to load the NC program text into an operation or select its interpreter), and in ENCY Tuner, which has no documented interface of this kind, the run is manual: you calculate the operations, and the assistant prepares the list of programs and steps, then collects and compares the results. Keep the run program in the interpreter repository and never give it to the customer.

Before trusting the run program, test it on a known error: give it an NC program with an error and with an unknown word and make sure it counted both. A counter that reads the wrong field of the log shows "0 errors" on anything.

Run the programs one at a time: runs in one process of the CAM system write to one log file, and parallel processes may fail to start the kernel at all.

## Comparison

1. Compare the summaries of all programs before and after. A changed number of warnings or commands in a program the change did not concern is the first thing to explain.
2. For each changed program, start with the first difference and trace it to the block and the word that caused it. An unintended difference matters more than an intended one.
3. Read the warnings themselves, not only their number: each one names a word, an axis or a cycle.
4. Check the edge cases that are not in the programs with a short program: the word in all spellings from the list, at the limits, omitted, repeated. Build it from the header of a real program of the same operation and replace only the blocks being checked — without the header the program may produce no movement at all.

A difference caused by the check itself rather than by the interpreter — a different coordinate system of the test operation, a different machine in the project — is not a result: name it and exclude it.

## Checking through the postprocessor

If you have the customer's postprocessor and the CAM project, close the loop: generate NC programs from the project's operations, run them through the interpreter and compare the simulation with the tool path of the operation itself. A discrepancy may turn out to be a postprocessor error. The interpreter simulates what the controller would do with the program, not what the operation intended: report such an error to the author of the postprocessor instead of hiding it in the interpreter.

## Safety check

Before hand-over, review every change for cases where the simulation looks safer than the machine: a missing retract, a guessed start point, a cycle that is not simulated but leaves the operation looking finished. Check each such case with a short program. After every round of edits based on review comments, run the whole set of programs again.

## Preparing for hand-over

The customer receives a folder for each product version: the `*.snci` file, the interpreter library and `InterpreterSettings.ini`, plus the `*.deps.json` file only if the interpreter does not load without it (this is checked on an unmodified installation). The assistant copies the required files by name rather than archiving the whole build folder: it contains debug files and service files of the SDK package. With them goes a README in the customer's language: what is supported, the limitations, the settings, which folder is for which product version, whether the product needs a license option to load a custom interpreter, and which simplifications were made on purpose, so that they are not taken for errors.

Before sending, check that:

- the files contain no traces of your computer: user names, home folders, internal servers. Build the delivered library without debug information or with path mapping: a normal build writes the path of the `*.pdb` file on your computer into it;
- the files contain no names that do not belong to this customer: names of other customers, of your computer and its users, of internal servers and package feeds — neither in file names, paths, settings, launch configurations or SDK package references, nor in the README. Search the content of every file, in UTF-8 and UTF-16 encodings, not only the file names; the same applies to everything sent together with the package;
- the project, if the customer asks for the sources, builds from a clean copy with the released SDK package;
- the interpreter works on an unmodified product installation.

Build the package from sources committed to the history, and record what was sent, when and to whom.

## What the assistant must not do

It must not assign the "Accepted for the machine" state to a result, change the reference programs, the machine or the project to make the comparison match, claim a check of a product version it did not run, or send the package without your permission.
