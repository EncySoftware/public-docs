# Digital Machine Kits

A Digital Machine Kit sells a machine and its post processor as one component: one card, one
licence, both files. You build a kit yourself, or DMC makes one from a post processor and a machine
schema of yours that are linked to each other. DMC also works the other way round: it makes the post
processor and the machine schema of a kit you built into components of their own, for customers who
need only one of them.

Whatever DMC makes goes to review like any submission: the DMC team publishes it, never DMC itself.

## A kit you build

1. Put the machine schema's files and the post processor's file into one `.zip`, the post beside the
   schema's `.xml` (see [Components and archives](components-and-archives.md#digital-machine-kit)).
2. Upload it as a **Digital Machine Kit**, and fill in the card: the machine from the schema, the
   controller from the post.
3. Submit it.

**Kit contents** can name components already in the catalog that the kit holds.

## Kits DMC makes from your post and schema

When a post processor and a machine schema are both published, linked to each other (**Made for**,
or **Suitable post processors** on the schema), and published under the same company name — both by
you, or by two people of your dealer company — DMC makes a Digital Machine Kit of the two, in the
name of the schema's owner, and sends it for review.

- **Card** — named `<schema> + <post>`, with a short description naming both, the machine from the
  schema, the controller from the post, the schema's cover and the post's samples.
- **Price** — when either is paid, the sum of the paid prices; otherwise With Maintenance when
  either is With Maintenance; otherwise Generic.
- **Archive** — built by DMC: the schema's archive with the post beside its `.xml`.

While the pair holds, the kit follows it: its price, archive and contents always; its name,
description, machine and controller until you change them on the kit — a field you change stays as
you set it. The kit's price and archive are not yours to set, and its two contents links cannot be
removed.

- A post linked to several of your schemas makes a kit with each.
- No kit is made when you already have a kit holding both, for a link to someone else's component,
  or for an interpreter.
- When the post or the schema leaves the catalog, or the link between them is removed, a published
  kit goes back to Pending Review. Once the pair is published again, the DMC team accepts the kit
  again.
- A kit you delete is not made again. When the post or the schema is deleted, a published kit goes
  back to Pending Review, and the kit becomes an ordinary kit, its price and archive yours.

## Parts DMC makes from your kit

When a kit you built is published, DMC makes its post processor and its machine schema into two
components of their own, in your name, and sends them for review.

- **Which kits** — a kit you built (not one DMC made), whose archive is a `.zip` with exactly one
  post processor and one machine, and whose **Kit contents** do not already name a post processor or
  a machine schema.
- **Names** — the schema takes the kit's name without its controller
  (`DMG MORI DMU 80FD - Siemens Sinumerik 840D` gives `DMG MORI DMU 80FD`); the post takes the name
  of its file.
- **Price** — a paid kit's price is split: the post takes two thirds, rounded to the nearest ten
  euros when it is not a whole number, and the schema the rest — a kit at €499 gives €330 and €169.
  A With Maintenance kit gives two With Maintenance parts, a Generic kit two Generic ones.
- **Archives** — the post's file for the post, and a `.zip` of the machine's own files for the
  schema, both cut from the kit's archive.

The parts follow the kit: their prices, archives and the post's samples always; their names,
descriptions, machine and controller until you change them on a part. A part's price and archive are
not yours to set.

- When the kit leaves the catalog, its published parts go back to Pending Review.
- When the kit is deleted, its published parts go back to Pending Review, and the parts become
  ordinary components, their prices and archives yours.
- A part you delete, or one the DMC team rejects, is not made again.
- The parts never make a kit of their own.
