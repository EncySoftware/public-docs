# Troubleshooting

## Store messages

The store refuses a package with a message that names the problem. The most common ones:

| Message begins with | What to do |
|---|---|
| The … Extension Store Developer Agreement (vX) has not been accepted | Register as a developer and click **I Agree** (see [Getting started](getting-started.md#register-as-a-developer)), then publish again. |
| The package has no 'ency-extension' tag | Add the marker tag to `tags` in `package.info.json`, or pack with the template or `ExtensionManagerCLI` (see [Package requirements](package-requirements.md#marker-tag)). |
| The .nupkg has no *.settings.json manifest or no .dll inside | Check the package layout (see [Package requirements](package-requirements.md#layout)). |
| The manifest has no "module_path" | Add `module_path` to the manifest (see [Extension anatomy](extension-anatomy.md#manifest)). |
| Manifest has no 'extensions' array / Manifest declares no extension points at all | Declare at least one entry point in `extensions`. |
| The package says two different things about itself | Make the id and version in `.nuspec` and `package.info.json` match, and rebuild. |
| Built against SDK x, which cannot be installed yet | Pin the SDK package to the version the message names, rebuild and publish again (see [Package requirements](package-requirements.md#sdk-version)). |
| Version X of Y is already on the feed / This version is already published | Increase the version and publish again. |
| You are not the owner of extension X | The package id belongs to another developer. Choose another id. |
| The name X would share its address with the existing extension Y | Choose an id that differs from Y in more than punctuation. |
| The name X is reserved by another publisher | Choose another id, or ask a moderator to release the name. |
| Your developer profile is Free, and a paid extension needs the Paid profile | Publish the extension as free, or apply for the paid profile (see [Paid extensions](paid-extensions.md)). |
| … is N characters long; the store keeps at most M | Shorten the field (see [Package requirements](package-requirements.md#limits)). |
| This store accepts 20 publishes a day from one account | Wait until the next day. |
| The package was refused by the virus scanner | Remove the flagged file from the package. If you believe the finding is false, contact the store team. |
| The virus scanner is not answering | Try again later; the package was not published. |

## In the CAM system

**The extension is installed but not visible.** Check on the **Manage** page of the
**Extensions** tab that the library and its entry point are enabled, and look for it where its
entry point type puts it (see [Extension anatomy](extension-anatomy.md#entry-points)). Restart
the CAM system if it still does not appear.

**Installing a new build fails with an access error.** The previous build is still loaded.
Close the CAM system and install again (see
[Build and test locally](local-testing.md#restart-and-unloading)).

**A published extension is not in the catalog.** A first publication appears in the catalog
after the moderator approves it; until then it opens by its direct link. A new version appears
after indexing, usually within a few minutes. Check its state in **My published** (see
[Review, updates and visibility](review-and-updates.md#publication-states)).

**The card has no icon.** Put PNG or JPG pictures into `screenshots/` of the package; the first
one becomes the icon.

## Not sure it is allowed

- **Whether a capability needs a licence check, or may be published at all** — ask the store team
  for a written determination before you build (see
  [Store rules and your obligations](store-rules.md#reserved-functionality)).
- **Whether a name is acceptable** — ask the store team before you publish.
- **How to give an extension to one customer or an internal team only** — ask for a private
  listing.

See [Contacts](references.md#contacts) for the address.
