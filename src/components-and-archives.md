# Components and archives

## Kinds of component

| Kind | What it is | Product File |
|---|---|---|
| **Post Processor** | Turns ENCY's toolpaths into NC code for a control. | `.sppx`, `.dll` or `.zip` |
| **Machine Schema** | The machine itself: its kinematics, geometry, travels and equipment, for simulation in ENCY. | `.zip` with the machine's `.xml` and its `.osd` files |
| **Interpreter** | Reads a control's NC code into ENCY. | `.zip` with the interpreter's files |
| **Digital Machine Kit** | Two or more of the above in one archive, licensed together — usually a machine schema with its post processor. | `.zip` holding them |

A file can be up to 1 GB, but one over 300 MB cannot be licensed: keep components smaller. The
catalog's tab for kits reads **Kit**.

## Post processor

Upload the post processor's own file — the `.sppx` written in the Postprocessor Generator, or the
`.dll` of a .NET post processor — or a `.zip` that holds it. Whatever the `.zip` holds reaches every
licence holder's ENCY with the post.

The post's samples belong on the card, in **G&M Codes File** and **NC File** (see
[The card and links](the-card.md#samples)). DMC takes them from files named after the post:

- `<name>_g-and-m.zip` — the G and M codes the post supports;
- `<name>_NCcode.nc` — an example NC program the post wrote.

In a ZIP import, put the `.sppx` at the top of the archive, not in a folder, with these files
beside it: they go on the card, and the post goes to licence holders alone. In a folder or a `.zip`
they are packed with the post. A new post that comes with an NC sample starts as
**Tested in simulation** (see [The card and links](the-card.md#experience-and-tested-in-ency)).

## Machine schema

Pack the machine's folder as ENCY keeps it into a `.zip`: the machine's `.xml`, the `.osd` geometry
files it refers to, and the preview picture ENCY saves beside them. DMC reads from it:

- **Travels** — X, Y and Z, in mm.
- **Equipment** — the schema's choices of what the machine comes with or without, such as a pallet
  or a chuck, shown as tags on the card.
- **The preview picture** — for the cover (see [Covers](the-card.md#covers)).
- **The 3D model** — built from the `.osd` files; the card then shows the machine in 3D.

A new archive is read again: what the schema declares replaces what the card had, the 3D model is
built anew, and the machine is tried in ENCY again (see
[Review, updates and testing](review-and-updates.md#tested-in-ency)).

## Interpreter

Pack the interpreter's files into a `.zip` as ENCY installs them: its descriptor (`.snci`, with an
`.sncix` beside it for a configurable interpreter), its native library (`<name>_Win64.dll`) and its
settings (`<name>.ini`), if it has them.

## Digital Machine Kit

Put the machine schema's files and the post processor's file into one `.zip`, the post beside the
schema's `.xml`; add an interpreter's files the same way if the kit has one. How kits work, and the
kits DMC builds by itself, is in [Digital Machine Kits](kits.md).

## How ZIP import tells them apart

In **Bulk import**, every top-level folder or zip inside an archive becomes one component, by the
files it holds, and so does a post processor's `.sppx` lying loose beside them:

| Files inside | Becomes |
|---|---|
| `.xml` and `.osd` | Machine Schema |
| `.sppx`, or a `.dll` that is not an interpreter's | Post Processor |
| `.snci` or `.sncix` | Interpreter |
| Two or more of the above | Digital Machine Kit |
| None of these | Ignored |

A loose file is named after itself. A folder or zip that holds a single post processor or
interpreter is named after its file — a kit with one post too; any other, such as a machine schema,
after the folder or the zip. An underscore between two digits becomes a slash, so `HAAS VF-10_50` is
named `HAAS VF-10/50`.
**Naming legend** turns coded names into readable ones (see
[Publishing](publishing.md#from-zip-archives)).
