# Troubleshooting

## Store messages

The store refuses a package with a message that names the problem. The most common ones:

| Message begins with | What to do |
|---|---|
| The … Extension Store Developer Agreement (vX) has not been accepted | Become a developer and click **I Agree** (see [Getting started](getting-started.md#become-a-developer)), then publish again. |
| The … Extension Store terms changed for the account … | Open **Account settings** → **Developer**, accept the new versions with **I Agree**, then publish again. |
| The store requires a declaration | Add `reservedDomains` to `package.info.json`, `[]` if the extension provides nothing from Schedule A (see [Publishing](publishing.md#reserved-functionality)). |
| The package's manifest has no "reservedDomains" | The form answer needs the key in the package too: add `"reservedDomains": []` to `package.info.json`. |
| The package has no 'ency-extension' tag | Add the marker tag to `tags` in `package.info.json`, or pack with the template or `ExtensionManagerCLI` (see [Package requirements](package-requirements.md#marker-tag)). |
| The .nupkg has no *.settings.json manifest or no .dll inside | Check the package layout (see [Package requirements](package-requirements.md#layout)). |
| The manifest has no "module_path" | Add `module_path` to the manifest (see [Extension anatomy](extension-anatomy.md#manifest)). |
| Manifest has no 'extensions' array / Manifest declares no extension points at all | Declare at least one entry point in `extensions`. |
| The package says two different things about itself | Make the id and version in `.nuspec` and `package.info.json` match, and rebuild. |
| Built against SDK x, which cannot be installed yet | Pin the SDK package to the version the message names, rebuild and publish again (see [Package requirements](package-requirements.md#sdk-version)). |
| Version X of Y is already on the feed / This version is already published | Increase the version and publish again. |
| You are not the owner of extension X | The package id belongs to another developer. Choose another id, or ask its owner to add you as a collaborator. |
| The name X would share its address with the existing extension Y | Choose an id that differs from Y in more than punctuation. |
| The name X is reserved by another publisher | Choose another id, or ask a moderator to release the name. |
| X is in the store as an organization | Ask the owner of the organization to invite you, and publish on its behalf (see [Organizations and collaborators](organizations.md)). |
| X has not accepted the Developer Agreement yet | The owner of the organization accepts the terms under **Account settings** → **Organizations**. |
| Your developer profile is Free, and a paid extension needs the Paid profile / Your developer profile is for free extensions only | Publish without **Paid**, or click **Enable paid extensions** (see [Selling and payouts](paid-extensions.md#get-ready-to-sell)). |
| A paid extension needs your payout account with Stripe | Click **Set up payouts** on the form or in **Earnings**, finish the Stripe form and submit again. |
| … carries no EncySdk stamp / A paid extension needs its dll named after the manifest | Rebuild against SDK 3.0.19 or newer, with the `.dll` named after the manifest (see [Package requirements](package-requirements.md#sdk-version)). |
| The card takes up to 10 tags of yours / The tag … is N characters long | Keep at most 10 tags of your own, 32 characters each. |
| The card icon … | Upload a PNG or JPEG picture of at least 32 px on each side. |
| … is N characters long; the store keeps at most M | Shorten the field (see [Package requirements](package-requirements.md#limits)). |
| This store accepts N publishes a day from one account / Too many publish attempts | Wait and try again later. |
| The package was refused by the virus scanner | Remove the flagged file from the package. If you believe the finding is false, contact the store team. |
| The virus scanner is not answering / The licensing service did not answer | Try again in a few minutes; the package was not published. |
| Payouts cannot be set up right now: Stripe is waiting for a confirmation from the store | The store team has been told; try again later. |
| … has prices or sales: a paid extension cannot change hands | An extension with prices or sales stays with its owner and cannot be moved into an organization. |

Refused packages stay listed under **Refused at submission** in **My published** (see
[Review, updates and visibility](review-and-updates.md#my-published)).

## In the CAM system

**The extension is installed but not visible.** Check on the **Manage** page of the
**Extensions** tab that the library and its entry point are enabled, and look for it where its
entry point type puts it (see [Extension anatomy](extension-anatomy.md#entry-points)). Restart
the CAM system if it still does not appear.

**Installing a new build fails with an access error.** The previous build is still loaded.
Close the CAM system and install again (see
[Build and test locally](local-testing.md#restart-and-unloading)).

**A published extension is not in the catalog.** Each version appears after the moderator
approves it. Check its state under **Versions on their way** in **My published** (see
[Review, updates and visibility](review-and-updates.md#my-published)).

**The card has no icon.** Upload one on the publication form, or put PNG or JPG pictures into
`screenshots/` of the package; the first one becomes the icon.

**Users cannot take a trial of a paid extension.** The extension has no price yet: the card says
**Price not set**. Set the price (see [Selling and payouts](paid-extensions.md#set-a-price)).

## Not sure it is allowed

- **Whether a capability needs a licence check, or may be published at all** — ask the store team
  for a written determination before you build (see
  [Store rules and your obligations](store-rules.md#reserved-functionality)).
- **Whether a name is acceptable** — ask the store team before you publish.
- **How to give an extension to one customer or an internal team only** — ask for a private
  listing.

See [Contacts](references.md#contacts) for the address.
