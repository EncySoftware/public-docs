# Troubleshooting

## The assistant does not see the postprocessor tools

Ask it which tools it currently has. If the CLData or InP tools are missing, the MCP configuration did not load: check that you edited the file your client actually reads, that the paths are absolute and exist, that backslashes are doubled in JSON, and restart the client. A client started before the configuration was saved keeps the old set.

## The assistant cannot reach InP

InP MCP drives a running instance of the postprocessor IDE. Let the assistant start one itself, or open InP from the CAM system with the postprocessor loaded and ask it to connect. If it reports that the instance manager is unavailable, the installed CAM system does not support starting instances — open InP by hand.

A headless instance that fails to compile or run with an error about focusing an invisible window is an older InP build. Use a windowed instance instead.

## Several InP instances are running

The assistant has to address one of them explicitly, and a request that does not is rejected rather than sent to an arbitrary instance. Close the instances you do not need, or tell it which one to work in — this is normal when you deliberately run several postprocessors in parallel.

## Command indexes no longer match the data

CLData indexes are valid for one revision of the data. When the project is regenerated, the server rereads it and asks for the call to be repeated; results captured earlier point at different commands. Always keep the project together with the indexes, and repeat the inspection after regenerating CLData.

## An extension says the installation folder is not set

Set it in the extension's settings, or run its **Select Installation Folder…** command from the command palette (`F1`) and pick the folder. Both the product folder and its `Bin64` subfolder are accepted, and quotation marks around a pasted path are tolerated. With several CAM versions installed, make sure it points at the one you actually want to test against — this is the most common cause of "it works differently than in the CAM system".

## The result does not match what the CAM system produces

With more than one CAM version installed, the run may have gone through a different one. Check that all three extension settings point at the version you are developing against, and for a .NET postprocessor check the `InpCoreDir` environment variable as well: the CLData Viewer writes it at startup, so it holds whichever installation's viewer ran last, and debugging from the editor follows it. Nothing warns you about this — the run succeeds and simply produces different output. If you change the variable, programs already running keep the old value; signing out of Windows and back in is what makes the new one take effect everywhere.

## Generate NC produces no file

Read the errors in **Problems** first: a postprocessor that failed to compile or stopped on a run-time error produces nothing. Then check that the output path is writable and that the configuration names the project you think it does. For .NET, check that the assembly was rebuilt after the last edit — `dotnetPosts.autoBuild` does that for you.

## Settings cannot be extracted from a .NET postprocessor

Extracting the default settings from the assembly requires a recent batch runner. If the installed one does not support it, use a project that has its settings file, or update the CAM system; do not hand-write a settings file to work around it.

## install.cmd closes before I can read it

It waits for a keypress, so a window that closed immediately means it was not the script that ran. Run it from a command prompt in the unpacked folder to keep the output visible.

If it reports that the `code` command was not found, the VS Code command-line launcher is not on `PATH`. The VS Code installer normally adds it; otherwise add the folder containing it to `PATH`, or install the `.vsix` files through **Extensions → Install from VSIX…**.

## The updater does not offer anything

Updates are configured by the bundle, so extensions installed by hand from separate `.vsix` files are never offered any. Reinstall with `install.cmd` from the unpacked archive, then run **Postprocessor Tools: Check for Updates**.

## The assistant answers from documentation instead of the project

This is what happens when the tools are unavailable, when the request named no project, or when the answer is not required to cite the data. Give it the project, ask which command and which parameter values it actually read, and let the skills do their job — they require inspection before editing.

## The assistant reports success without running anything

Compilation is not a result. Ask for the generated NC program and the comparison with the baseline; if there is none, the state is **Not verified** — see [Review and verify](review-and-verify.md).

## The documentation the assistant reads is outdated

A local checkout is a snapshot: update it with `git pull` and note the revision when it informs a release decision. Version-sensitive details — SDK versions, command names, panels — should be confirmed against the installed product rather than the checkout.
