---
name: prepare-workspace
description: Set up and maintain the developer's workspace — the folder, the standing brief, the local documentation, their own notes, and version history — because that folder is the only memory you have between sessions.
---

# Prepare the workspace

## When to use

At the start of work with a user whose workspace has no `AGENTS.md` and no notes folder, whenever they ask how to organise their files, and at the end of any task — the distilling step below is part of finishing, not an extra.

Assume the user is a postprocessor developer, not a programmer: they may never have used version control, and nothing here may require them to learn it.

## What you are building and why

You have no memory between sessions. The workspace is it. Everything the user explained yesterday is gone unless it is written in a file you will read again. Say this plainly when you propose the layout — not as an apology, as the reason.

```text
work\
├── AGENTS.md      the standing brief, read every session - keep it short
├── posts\         the postprocessors
├── projects\      test CAM projects and reference NC programs
├── docs\          a copy of the postprocessing documentation
└── notes\         the user's own practices and solved cases
    └── skills\    their own skills, in the same format as the published ones
```

Adapt the names to what already exists; never reorganise a folder the user is working in without asking first.

## Workflow

1. Look before proposing. List what is already there: postprocessors, test projects, reference NC programs, an existing instruction file, whether the folder is already a git repository (`git rev-parse --git-dir`).
2. Propose the layout as a short plan, in the user's terms, and say what each part is for. Create only what they agree to, and move nothing without permission.
3. For .NET postprocessors the editor is opened on the postprocessor folder itself, so what lies above it falls out of view: the standing brief is read from the folder you were opened on, not from the ones above it. Put the repository at the top of the whole workspace rather than inside one postprocessor. Then, if the client can be told where the brief is — Kilo Code takes a list of instruction files in the `instructions` key of its global `kilo.jsonc` — add the full path of the main `AGENTS.md` there once. Otherwise leave a two-line `AGENTS.md` in each postprocessor folder pointing at the main brief and at the notes. Install the skills for the user rather than for one project, so they do not depend on which folder is open.
3. Draft `AGENTS.md` from what you can already see and what they tell you: machines and control systems, which postprocessor serves which, conventions that always apply, where test projects and reference programs live, the rules of engagement (read the actual CLData before editing, run and compare before reporting done, never touch a production postprocessor unasked). Keep it to about a page: it is read in full every session. Details belong in `notes\`.
4. Record standing constraints **in the user's own words**, quoted. A rejected option with the reason for rejecting it is worth more than a description of the chosen one.
5. Give yourself the documentation: connect the knowledge server if it is available, and clone the documentation repository into the workspace as well — the checkout is what pins a revision and works offline. Note the revision you cloned. If a knowledge cache has never been refreshed on this machine, refresh it once.
6. Offer version history — see below — and accept a refusal without arguing.
7. When the task itself is done, distil it: one short file in `notes\`, one topic per file, saying what was wrong, how it was found, what fixed it and why that way. If a way of working repeated, write it down as a skill in `notes\skills\` instead. Then tell the user what you wrote, in one line.
8. If what you wrote applies beyond this shop — a technique, a check, a way of reading the data, with nothing specific to their machines or customers in it — say so, and offer to prepare it for sharing: a self-contained file, cleaned of customer names, part numbers, machine particulars and internal paths, with what you removed reported to the user. Submitting it to the shared knowledge base is done from the CAM Agent chat, so leave the submission to the user unless you are working there yourself. Never publish anything on your own initiative.

## Version history

Ask once, plainly: keep history in git, or keep working with folders and copies? Both are legitimate. If the user is uneasy about letting you edit their files, say the useful part rather than reassuring them: under version control nothing you do is irreversible, and any state can be brought back. If they decline, help them the other way — a copy of the postprocessor before a substantial change, reference NC programs kept next to the test projects — and do not raise it again in that session.

If they accept, do all of it yourself:

- check for git (`git --version`); if it is missing, install it — `winget install --id Git.Git` on Windows, or point them at <https://git-scm.com/downloads> if winget is unavailable;
- `git init`, then a `.gitignore` that excludes generated NC output, build artefacts and temporary files, and a `.gitattributes` that fixes line endings for the text files in the repository;
- verify there are no credentials, licence files or customer archives in the first commit, then commit the current state as the starting point;
- explain in two sentences what they got, without git vocabulary: every state can be brought back, and every change can be explained.

Then serve the plain-language requests without making them learn commands:

| They ask | You do |
|---|---|
| "commit this" | Commit with a message that says **why**, not what changed |
| "compare with Friday" / "with the previous version" | Diff the working tree or two revisions, and report differences in NC terms |
| "when did this break?" | Search the history for the change that introduced the behaviour; bisect with the test project if the history is long |
| "why is this line here?" | Find the change that added it and quote its message |
| "put it back as it was" | Restore the file from history — never retype it from memory |

## Rules

- Never commit passwords, tokens, licence files or customer data. Check before the first commit, not after.
- Never force version control on a user who declined it, and never make a routine task depend on it.
- Keep `AGENTS.md` short. Everything you add to it is paid for in every future session; if it is not needed every time, it belongs in `notes\`.
- One fact in one place, and always the current state. No "it used to be" asides in notes — that is what history is for.
- Do not describe a task as finished while its outcome exists only in the chat.
- Do not restructure or rename the user's existing folders on your own initiative.

## Done means

The workspace has a layout the user agreed to, `AGENTS.md` exists and is short and accurate, the documentation is reachable, `notes\` contains at least the outcome of the current task, and history is either under git with a clean first commit or explicitly declined by the user.
