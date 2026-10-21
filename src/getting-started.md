# Getting started

## What you need

- Windows 10 or newer.
- The CAM system with the **Extensions** tab on the Home page — to try your build before
  publishing.
- The .NET 10 SDK. Extensions are built for `net10.0-windows`.
- An account of the CAM system. The store has no separate sign-up: **Sign in** on the store
  website uses the same account.
- A GitHub account — only for the GitHub route (see [Choose a route](#choose-a-route)).

## Register as a developer

The store accepts publications only from registered developers. Registration is done once, on
the **Publish** page of the store website, and applies to every publishing route, GitHub
included.

1. Open the store website and click **Sign in**.
2. Click **Publish** in the header, then **Become a developer**.
3. **Type.** Choose who publishes: **A company** or **Me, as an individual**.
4. **Profile.** Choose **Free extensions only** or **Free and paid extensions**. The paid
   profile is for companies and for individuals acting for their business; it requires tax and
   payout details, and its review takes up to five business days. You can switch to paid later
   (see [Paid extensions](paid-extensions.md)).
5. **Your details.** Name, phone and country; the email comes from your account. The
   **Public developer name** is shown on your extensions in the store: 2 to 80 characters,
   unique in the store.
6. **Company.** Only for a company: legal name, country of incorporation, registration
   number, registered address, country of control; VAT number and website are optional.
7. **Terms.** Read the Developer Agreement and the documents incorporated into it, select the
   checkbox and click **I Agree**. What they ask of you is summarised in
   [Store rules and your obligations](store-rules.md).

After you agree, your developer details become part of the agreement and can be changed only
through the store team. When a new version of the terms comes into force, the store shows a
banner, and publishing pauses until you accept it.

Read the rules before you start building: some capabilities may be published only with a licence
check, some not at all, and an extension may reach users only through the store (see
[Store rules and your obligations](store-rules.md)).

## Choose a route

All routes end in the same store checks and the same moderation (see
[Package requirements](package-requirements.md)).

| Route | Best for | Where it is described |
|---|---|---|
| **GitHub repository from the template** | Most authors; every version is published by a workflow run | [ency-extension-template](https://github.com/EncySoftware/ency-extension-template) |
| **AI assistant (MCP server)** | Creating, checking and publishing from Cursor, Claude Code and other MCP clients | [ency-extension-mcp](https://github.com/EncySoftware/ency-extension-mcp) |
| **Upload a .nupkg** | Code outside GitHub, a one-off release, a package produced by your own build | [Publishing](publishing.md#upload-a-package) |

To write the extension code, start from the examples and the API documentation listed in
[External references](references.md). Before you publish, read the design rules: they
describe how an extension looks and behaves inside the CAM system and end with a pre-publish
checklist.

## First publication checklist

1. You are registered as a developer and have accepted the terms.
2. The extension follows the store rules: no code from outside its package, disclosed network
   use and data processing, no misleading use of the product name (see
   [Store rules and your obligations](store-rules.md)).
3. The extension works in your local CAM system (see [Build and test locally](local-testing.md)).
4. The package passes the store checks (see [Package requirements](package-requirements.md)):
   manifest, marker tag, SDK version, unique package id.
5. The card is ready: `readme.md` with a privacy disclosure if the extension processes personal
   data, description and at least one picture in `screenshots/`.
6. The reserved functionality declaration is filled in (see
   [Publishing](publishing.md#reserved-functionality)).
