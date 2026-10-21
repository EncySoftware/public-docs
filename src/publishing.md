# Publishing

Publishing starts on the **Publish** page of the store website (the **Publish** button in the
header). The page offers the GitHub route and the package upload; the AI assistant uses the same
store from your editor. Before the first publication, register as a developer (see
[Getting started](getting-started.md#register-as-a-developer)).

## From a GitHub repository

The template repository contains the workflow that builds the extension, and the store packs
and publishes it. Connect your GitHub account once on your profile page of the store website
(**Publishing from GitHub**, **Sign in with GitHub**); after that every repository of yours
publishes without tokens.

The steps — creating the repository, connecting it, running the workflow, bringing an existing
project over — are described in the template README, section
[Quick start](https://github.com/EncySoftware/ency-extension-template#quick-start).

The result of each run, failures included, is shown under **My published** (see
[Review, updates and visibility](review-and-updates.md#publication-states)).

## From an AI assistant

The `ency-extension-mcp` server lets an AI assistant create, check and publish an extension
from Cursor, Claude Code or another MCP client — with or without a GitHub repository. Its
installation, tools and console commands are described in the
[ency-extension-mcp README](https://github.com/EncySoftware/ency-extension-mcp).

## Upload a package

Use this route for code outside GitHub, a one-off release, or a package your own build already
produces. Every new version is uploaded the same way, by hand.

1. Build the package. Pack the build output with the packing tool of the CAM system:

   ```powershell
   ExtensionManagerCLI.exe pack-library --folder <build output folder> --output <folder for the package>
   ```

   `ExtensionManagerCLI.exe` is in the `Bin64` folder of the CAM system installation. The folder
   must contain `package.info.json`; `ExtensionManagerCLI.exe inspect --folder <build output folder>`
   writes a draft of it. The tool adds the marker tag and leaves out the files that already ship
   with the CAM system. If you pack with your own tooling, follow
   [Package requirements](package-requirements.md).
2. On the **Publish** page, find **Upload a .nupkg** and click **Choose package...** (or **Sign in
   to upload** if you are not signed in).
3. Select the `.nupkg` file. The page shows the package id, version and authors, the warnings,
   and a preview of the card.
4. **Paid extension (requires a license).** Select it for a paid extension (see
   [Paid extensions](paid-extensions.md)).
5. **Category.** Choose what the extension does, or leave it to the moderator.
6. **Reserved functionality.** Answer the declaration (see
   [Reserved functionality](#reserved-functionality)).
7. Click **Submit for review**. The page shows **Published** with a link to the card.

The card preview is approximate: the live card appears after the catalog indexes the package,
usually within a few minutes.

## Reserved functionality

Some capabilities of the CAM system are licensed separately; they are listed in Schedule A of
the Publishing Policy. An extension may provide them, but each such function must check that the
user holds the licence for that area. A licence for one area does not unlock functions in
another.

Every submission declares whether the extension provides such capabilities:

- On the upload form — the **Reserved functionality** block: **No — it does not provide any
  capability listed in Schedule A**, or **Yes — it provides capabilities in these areas:** with
  the list of areas, followed by three confirmations.
- In the package — `reservedDomains` in `package.info.json`. The format is described in the
  template README, section
  [What the store asks you to declare](https://github.com/EncySoftware/ency-extension-template#what-the-store-asks-you-to-declare).

The first release with a given answer asks you to confirm it in the browser. Releases with the
same answer then publish without a question until the answer, Schedule A or the confirmation
wording changes.

The declaration must match what the extension actually does: review checks the output, not only
the answer, and a materially wrong declaration is treated as inaccurate information. A new
version that adds, removes or moves a capability between areas needs a new declaration. What
gated and complementary extensions are, and which areas are closed, is described in
[Store rules and your obligations](store-rules.md#reserved-functionality).

From 1 November 2026 a submission without the declaration is refused; until then it gives a
warning. If you are not sure which areas apply, ask the store team for a written determination
before you build.
