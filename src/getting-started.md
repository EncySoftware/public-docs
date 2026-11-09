# Getting started

## What you need

- Windows 10 or newer.
- The CAM system with the **Extensions** tab on its Home page, to try your builds.
- The .NET 10 SDK. Extensions are built for `net10.0-windows`.
- An account of the CAM system. The store has no separate sign-up: **Sign in** on the store
  website takes the same account.
- A GitHub account — only for the GitHub route (see [Choose a route](#choose-a-route)).

## Become a developer

The store accepts publications only from developers who have accepted its terms. You do this
once, in your account, and it covers every route, GitHub included. The wizard saves each step,
so you can stop and come back later.

1. Sign in on the store website and open **Account settings** → **Developer**. The **Publish**
   button in the header leads there too.
2. Click **Become a developer**.
3. **Type.** Choose who publishes: **A company** or **Me, as an individual**. The agreement is
   made with the one you choose.
4. **Profile.** Choose **Free extensions only** or **Free and paid extensions**. You can enable
   paid extensions later (see [Selling and payouts](paid-extensions.md)).
5. **Your details.** Name, country and phone come from your account; check them. The email is
   the one of your account and changes only there. **Public developer name** is what users see on
   your extensions: 2 to 80 characters, each word in one alphabet, unique in the store. For a
   company this step is called **Company representative**: add your **Position** and confirm that
   you may enter into agreements on the company's behalf.
6. **Company.** Only for a company: the legal name as in the register, country of incorporation,
   registration number, registered address and country of control. VAT number and website are
   optional.
7. **Developer terms.** Read the documents, tick the box and click **I Agree**. What they ask of
   you is summarised in [Store rules and your obligations](store-rules.md).

The **Developer** section then shows your details and the terms you accepted, with the date and
versions; **Download record** saves this record. Your details are now part of the agreement: to
change them, write to the store team.

New versions of the terms are announced in advance, in the **Developer** section and on the
**Publish** page. A material change must be accepted before your next publication: until you click
**I Agree** again, publishing pauses, from GitHub too. A minor change asks nothing of you.

Read the rules before you start building: some capabilities may be published only with a licence
check, some not at all, and an extension may reach users only through the store (see
[Store rules and your obligations](store-rules.md)).

## Choose a route

All routes end in the same store checks and the same moderation (see
[Package requirements](package-requirements.md)).

| Route | Best for | Where it is described |
|---|---|---|
| **Publish from GitHub** | Most authors: every version is published by a workflow run | [Publishing](publishing.md#from-a-github-repository) |
| **AI assistant (MCP server)** | Creating, checking and publishing from Cursor, Claude Code and other MCP clients | [ency-extension-mcp](https://github.com/EncySoftware/ency-extension-mcp) |
| **Upload a .nupkg** | Code outside GitHub, a one-off release, a package your own build produces, publishing for an organization | [Publishing](publishing.md#upload-a-package) |

To write the code, start from the examples and the API documentation in
[External references](references.md). Before you publish, read the design rules: they describe
how an extension looks and behaves inside the CAM system and end with a pre-publish checklist.

## First publication checklist

1. You are a developer and have accepted the current terms.
2. The extension follows the store rules: no code from outside its package, disclosed network
   use and data processing, no misleading use of the product name (see
   [Store rules and your obligations](store-rules.md)).
3. It works in your local CAM system (see [Build and test locally](local-testing.md)).
4. The package passes the store checks: manifest, marker tag, released SDK, the SDK stamp of a
   paid extension, `reservedDomains`, a package id of your own (see
   [Package requirements](package-requirements.md)).
5. The card is ready: `readme.md` with what the extension does, how to reach you for support and
   how fast you answer, and a privacy disclosure if it processes personal data; an icon and at
   least one picture in `screenshots/`.
6. You know your answer to the reserved functionality question (see
   [Publishing](publishing.md#reserved-functionality)).
