# Publishing

Publishing starts with the **Publish** button in the header of the store website. The page
offers two routes as tiles — **Publish from GitHub** and **Upload a .nupkg** — and remembers your
choice; the AI assistant reaches the same store from your editor. Until you have become a developer
the page sends you to do that first (see
[Getting started](getting-started.md#become-a-developer)).

## From a GitHub repository

The template repository contains the workflow that builds the extension; the store packs and
publishes it.

1. Create a repository from the template (**Use the template** on the **Publish** page). Write
   your code in `src/`; the card text lives in `src/readme.md` and `src/package.info.json`.
2. Link your GitHub account once: **Account settings** → **Profile** → **Publishing from
   GitHub** → **Sign in with GitHub**. After that every repository of yours publishes without
   tokens. GitHub links whoever is signed in there, so check the account first.
3. In your repository open **Actions** → **publish-to-ency-store** → **Run workflow** and leave
   the fields empty: the workflow picks the next version by itself. From a terminal:
   `gh workflow run publish-to-ency-store`.

The result of each run, failures included, appears in **My published** (see
[Review, updates and visibility](review-and-updates.md#my-published)). Bringing an existing
project over is described in the template README, section
[Quick start](https://github.com/EncySoftware/ency-extension-template#quick-start).

The GitHub route publishes in your own name. To publish for an organization, upload the package
(see [Organizations and collaborators](organizations.md)).

## From an AI assistant

The `ency-extension-mcp` server lets an AI assistant create, check and publish an extension from
Cursor, Claude Code or another MCP client, with or without a GitHub repository. Its installation,
tools and commands are described in the
[ency-extension-mcp README](https://github.com/EncySoftware/ency-extension-mcp).

## Upload a package

Use this route for code outside GitHub, a one-off release, a package your own build already
produces, or a publication for an organization. Every version is uploaded the same way, by hand.

1. Build the package. The packing tool of the CAM system does it in one command:

   ```powershell
   ExtensionManagerCLI.exe pack-library --folder <build output folder> --output <folder for the package>
   ```

   `ExtensionManagerCLI.exe` is in the `Bin64` folder of the CAM system installation. The folder
   must contain `package.info.json`; `ExtensionManagerCLI.exe inspect --folder <build output folder>`
   writes a draft of it. The tool adds the marker tag and leaves out the files that already ship
   with the CAM system. If you pack with your own tooling, follow
   [Package requirements](package-requirements.md).
2. On the **Publish** page choose **Upload a .nupkg** and drop the file onto the upload area, or
   click it to pick the file.
3. The form opens with the package id, version and authors, the store's warnings and a preview of
   the card. Fill it in (see [The publication form](#the-publication-form)).
4. Click **Submit for review**. The page shows **Published** with a link to the card. If the store
   refuses the package, the form says why; the refusal is also kept in **My published** (see
   [Review, updates and visibility](review-and-updates.md#my-published)).

Nothing is sent until you submit: **Choose another package** takes you back.

## The publication form

The left column is the store card.

**Pricing.** **Free** — anyone installs it. **Paid** — the extension runs only with a licence
from the store; a package with `"licensed": true` arrives with **Paid** already chosen. **Paid**
cannot be undone in later versions. While the extension has no price, **Paid** also asks for the
plans and the trial: they go on the card once the version is approved and reaches the feed. If
your paid profile or payouts are not ready, the form shows the step that is left with its button
(see [Selling and payouts](paid-extensions.md)). A paid package must carry the SDK stamp (see
[Package requirements](package-requirements.md#sdk-version)).

**Publish as.** Shown only if you belong to an organization: **Myself** or the organization. A
member without a developer registration of their own publishes only for the organization. A new
extension belongs to whom you choose; a new version of an existing one goes to its owner (see
[Organizations and collaborators](organizations.md)).

**Category.** What the extension does, or **Let a moderator sort it**.

**Tags.** The package tags stay as they are. Add up to 10 of your own: the store suggests tags it
already knows, so that users find your extension under the same words. Your tags stay on later
versions until you remove them here.

**Icon.** Click or drop a PNG or JPEG picture: it is cut to a square and shown round on the card.
The uploaded icon stays on later versions; **Use the package's picture instead** brings back the
picture from the package.

**Card preview** and **README** show the card approximately as users will see it. The live card
changes once a moderator approves the version.

The right column is the reserved functionality declaration, and below both columns are the
**Declarations** (see [Reserved functionality](#reserved-functionality)). **Submit for review**
stays inactive until both are complete.

## Reserved functionality

Some capabilities of the CAM system are licensed separately; Schedule A of the Publishing Policy
lists them as Domains. In the Domains open to third parties, an extension may provide such a
capability only behind a check that the user holds the licence for that Domain; some Domains are
closed altogether (see
[Store rules and your obligations](store-rules.md#reserved-functionality)).

Every submission declares its position, and a submission without the declaration is refused:

- **In the package** — `reservedDomains` in `package.info.json`, `[]` if the extension provides
  nothing from Schedule A. The format is described in the template README, section
  [What the store asks you to declare](https://github.com/EncySoftware/ency-extension-template#what-the-store-asks-you-to-declare).
- **On the form** — **Does your extension do any of the following?** Answer **No**, or **Yes**
  and tick the areas; the table shows the licence each area requires. A new version starts with
  the previous answer. The form tells you at once if the answer disagrees with the package.
- **Declarations** — three statements to tick: the extension gives no reserved capability to a
  user without the matching licence; nobody distributes add-ons or unlocks for it outside the
  store; the submission is complete and accurate.

The first publication with a given answer is confirmed in the browser. Later versions with the
same answer carry it forward, until the answer, Schedule A or the wording of the confirmation
changes.

The declaration must match what the extension does: review checks the output, not only the answer,
and a materially wrong declaration counts as inaccurate information. A version that adds, removes
or moves a capability between Domains needs a new declaration. If you are not sure which Domains
apply, ask the store team for a written determination before you build.
