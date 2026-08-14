# Organize your workspace

The assistant starts every session with no memory of the previous one. It does not remember what you agreed yesterday, which machine gave you trouble last month, or why a particular block is formatted the way it is. Whatever is written down in your working folder is what it knows; whatever stayed in the chat is gone.

So the working folder is not housekeeping — it is the assistant's memory. A few hours spent on it once saves the same explanations in every later session.

## What to keep in it

One folder, opened as the workspace in VS Code:

```text
work\
├── AGENTS.md      what the assistant must know every time
├── posts\         the postprocessors you work on
├── projects\      test CAM projects and reference NC programs
├── docs\          a copy of this documentation
└── notes\         your own practices and solved cases
    └── skills\    your own procedures for the assistant
```

The names do not matter; the separation does. Sources apart from test data, your own knowledge apart from the official documentation.

## AGENTS.md — the short standing brief

This file is read at the start of every session, so keep it short — a page at most — and put the details in `notes\`. What earns its place:

- the machines and control systems you work with, and which postprocessor serves which;
- conventions that always apply: block numbering, decimal format, comments, file naming;
- where things are: test projects, reference NC programs, your notes;
- the rules of engagement — read the actual CLData before changing code, run the postprocessor and compare with the reference before reporting anything as done, never change a production postprocessor without asking;
- constraints you have already stated once, written as you said them. An assistant reads them as instructions; otherwise it will propose the same rejected idea again next month.

Ask the assistant to draft it and then correct it — it is faster than starting from an empty file.

## notes — where your experience accumulates

After every solved case, one short file: what was wrong, how it was found, what fixed it, **and why that way**. The "why" is what saves time later: without it the assistant cheerfully proposes the option you rejected for a good reason.

Two habits keep this useful:

- **one topic per file**, not one growing file — you want to find things, and a small file is cheap to read;
- **describe the current state**. Historical asides ("it used to be like this") rot; if you keep the folder in git, the history is already there.

When a procedure repeats — the same check, the same sequence for a family of machines — write it as your own skill in `notes\skills\` and point the assistant at it. The published skills are ordinary Markdown files; yours look the same.

A task is not finished when the postprocessor works. It is finished when what you learned is in `notes\`.

## Documentation next to the sources

Two kinds of knowledge live side by side here, and it is worth keeping them apart.

The **published documentation** is a snapshot: the assistant can search it through the knowledge server, and a copy in the workspace serves the same purpose offline and at a revision you know — see [Advanced setup](advanced-setup.md#documentation-and-skills-for-the-assistant). It answers what the product does, and it changes only when a new version is released.

Your **own documentation** — `notes\` above — is the living half, and the only one that knows your machines, your projects and the decisions your team has made. It grows every time you solve something. The published snapshot cannot contain it, and neither can the assistant: nobody but you writes this part.

When a documented detail contradicts the installed product, the product wins — and the note about it goes into `notes\`, which is exactly the kind of thing the living half is for.

## Two ways to keep history

**Folders and copies.** Perfectly workable, and nothing here forces you to change it. Copy the postprocessor before a substantial change, keep the reference NC programs, and let dated folders be your history. The cost is that "what exactly changed since Friday" and "when did this break" become questions nobody can answer precisely.

**Git.** The same folder, with every state recoverable and every change explained. What it gives you in this work:

- an exact answer to *what changed* between two states, down to the block;
- an exact answer to *when* a behaviour broke, and *what else* changed in that step;
- the *reason* a line exists — the message of the change that introduced it;
- a safe way to try something risky and drop it without traces;
- a way to hand a colleague the postprocessor together with its history.

You do not have to learn git for this. Ask in plain words and let the assistant do it:

- "commit this, the offset fix works" — it commits, with a message that says why;
- "compare with what we had on Friday" — it shows what changed;
- "find when the coolant block disappeared" — it searches the history;
- "why is this line here?" — it finds the change that added it and reads its message;
- "put it back the way it was before the last change" — it restores from history instead of retyping.

If git is not installed, ask the assistant to install it — the official download is at <https://git-scm.com/downloads>. Ask it to set the workspace up as well: one folder under version control, with the generated NC output and temporary files excluded.

## What must not go in

Passwords, tokens, licence files, customer archives that have nothing to do with the postprocessor, and unrelated repositories. Everything in the workspace is material the assistant may read and, if you keep history, material that stays in it.
