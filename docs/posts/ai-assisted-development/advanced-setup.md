# Advanced setup

This page is for the cases the basic setup does not cover: a team that needs repeatable results, an automated check, or a manual configuration when the automatic one is unavailable.

## Manual setup when there is no automatic one

The automatic setup offered by CAM Agent or by your client configures what it knows about. Everything else is done by hand, and everything can be done by hand: install the extensions from the bundle, set the installation folder of each extension, write the MCP configuration for your client, and point the assistant at the documentation. [Set up the tools](setup.md) covers each of those steps with the concrete file names and settings; nothing on this page replaces them.

When you report a problem, record the versions: the CAM system, the extensions bundle, CAM Agent, the MCP servers and the AI client. Most "it worked yesterday" reports are version differences.

## Several CAM installations on one computer

Each extension points at one installation folder, and the assistant runs whatever is in it. With a released version and a beta version side by side, decide which one the postprocessor is being developed against and set all three settings to it. When you switch, switch all of them — a mixed configuration where CLData is read by one version and the postprocessor is run by another produces results that cannot be reproduced.

## Pin the documentation

For work that has to be reproducible, keep the documentation checkout at a known revision instead of pulling it constantly, and record that revision together with the postprocessor version. A retrieval service always answers from the current index, which is convenient for exploration and unhelpful when you need to explain why an answer changed.

## Give the assistant its own workspace

- Its own run configuration in the **Generate NC** panel, so your settings stay as you left them.
- Its own output folder for generated NC programs, outside the source tree.
- A branch or a copy of the postprocessor, never the production file.
- A reduced test project instead of the full customer project. Smaller data means a readable diff and a faster cycle.
- No credentials, tokens, customer archives or unrelated repositories in the workspace or in the instruction files.

## Automated checks

A headless run is suitable for a repeatable check: a fixed input project, a fixed postprocessor revision, captured logs and a stored NC program. Two rules keep it useful. Run it in a disposable working folder, so a failed run cannot leave a half-modified postprocessor behind. And review the diffs and the NC output outside the automation — an automated pipeline can tell you that output changed, never that the change is correct.

Do not connect an automated chain to a control system, and do not give it write access to production postprocessors.

## Rules worth writing into the instruction file

Put the requirements that always apply where the assistant always reads them — the workspace instruction file, or the skills. The ones that pay off in practice:

- read the actual project data before proposing a change, and cite the values used;
- read the current source of an item before editing it;
- compile, then run, then compare with the baseline — before reporting anything as done;
- keep the change minimal and explain what it does not cover;
- never send a program to a machine, and never change machine configuration.
