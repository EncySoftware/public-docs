# Publishing

Publishing lives in your DMC account: **My published** lists everything you own and takes single
components, **Bulk import** takes many at once. The **Publish** button in the DMC header opens
**My published**. Nothing goes to review until you submit it.

## From the form

1. In **My published**, click **Upload asset**. The **New Asset** form opens.
2. Choose the **Product** kind and attach the **Product File**.
3. Fill in the card (see [The card and links](the-card.md)).
4. Click **Save Draft** to come back to it later, or **Submit** to send it for review.

**Edit** in a component's **Actions** menu opens the same form on its latest saved state. If
someone else saves the component while you have it open, your save is refused: open it again and
repeat your change.

## From ZIP archives

1. Open **Bulk import** in your account.
2. Optionally, describe how your archive names are built in **Naming legend**, in up to 2000
   characters — for example `M3X = 3-axis mill, M5X = 5-axis mill, then brand-series-model` — and
   AI turns each name into a readable title. Left empty, the names stay as they are.
3. Set **Auto-fill**: **Generate cover image**, **Generate description** (with an optional hint) and
   **Generate metadata** — machine type, axes, controller, maker, series and model. Turn off what you
   would rather fill in yourself.
4. Drop the `.zip` archives on the page, or click **Select ZIP(s)**. Each can be up to 1 GB.
5. Click **Start import**.

Each top-level folder or zip inside an archive becomes one draft, and so does a loose `.sppx` (see
[Components and archives](components-and-archives.md#how-zip-import-tells-them-apart)). Imports are
listed under **Imports** and in the notifications bell; once an archive has uploaded, its import goes
on if you leave the page. One import of yours runs at a time, and the next waits as
**Queued — another import is running**. The result names every component created and, for every
failure, the reason.

Every draft from a ZIP import starts as **Generic**: set its price before you submit it — in the
form, or with **Edit fields** for many drafts at once (see
[Many components at once](#many-components-at-once)).

## From a spreadsheet

1. In **My published**, click **Upload CSV**.
2. **Download example CSV** gives a sheet with every column.
3. Click **Select CSV file** and check **Column mapping**.
4. Drop the product files and pictures into the dialog: they are matched to the rows by file name.
5. Look through the preview and click **Import**.

Only a missing **Product Name** or **Product** stops a row; anything else is a warning, and you
complete the draft in the form. **Price EUR** takes `0` for Generic, `-1` for With Maintenance, or
an amount for Paid. Travels have no column: they are read from the machine schema.

## From an AI assistant

dmc-mcp lets an AI assistant in Cursor, Claude Code or Codex publish for you: you say what to
publish, and it uploads the file, fills in the card and links it.

1. Install the .NET 8 SDK or newer, then the tool:
   `dotnet tool install -g EncySoftware.DmcMcp`
2. Run `dmc-mcp setup`. It signs you in with your ENCY account in the browser and registers the tool
   with your assistants.
3. Restart the editor. If something does not work, `dmc-mcp doctor` checks the sign-in, the
   Publisher role and the registration.

Then ask in your own words — *publish the post C:/posts/fanuc-0i.sppx, it is Fanuc 0i-MF for a Haas
VF-2*; *the control is Siemens 828D, not Fanuc*; *submit it for review*. The assistant can also
publish a whole folder, with an optional CSV manifest for exact names and fields, link a post to
machine schemas, set covers and replace a post's file.

Before uploading, the tool looks for similar components in DMC and stops if it finds any, so you do
not publish a duplicate. It never submits for review on its own: you check the card first. It cannot
set a price either: what it publishes starts as **Generic**, so set the price in the form before you
submit. Its tools,
settings and the hosted server for agents that cannot run a local program are described in the
[dmc-mcp README](https://github.com/EncySoftware/dmc-mcp).

## Many components at once

Tick rows in **My published**; a bar above the table offers:

- **Submit**, **Revoke**, **Disable**, **Unarchive**, **Archive** and **Delete**, wherever they fit
  (see [Review, updates and testing](review-and-updates.md#publication-states));
- **Edit fields** — the same machine, controller and pricing values on every selected component;
  fields you leave empty are not touched. As a publisher you change drafts this way; other statuses
  are skipped, with the reason;
- **Link…** and **Unlink…** — machine schemas with post processors or interpreters, up to 500
  components on each side and 2000 pairs at a time.

## Submitting

Click **Submit** in the form or in the **Actions** menu; a rejected component is submitted again
from **Actions**. A component that lacks a required field is not sent, and the message names the
fields (see
[The card and links](the-card.md#fields-needed-to-submit)).
