# Package requirements

The store publishes a NuGet package (`.nupkg`). On the GitHub route the store packs it itself;
on the upload route you upload the package your build produces. Every route passes the same
checks.

## Layout

| Path in the package | Contents |
|---|---|
| `lib/<target framework>/` | The extension `.dll` with its `.pdb` and `.xml` |
| `build/` | The manifest `<Name>.settings.json`, `package.info.json`, `readme.md`, other files of the extension |
| `build/screenshots/` | Card pictures |
| `build/<packageId>.targets` | The list of files for the installer |

The `.nuspec` must contain the package id and version, and its id and version must match
`package.info.json`.

## Where the card comes from

Nothing on the card is entered on the website: the store reads it from the package. To change
the card, publish a new version.

| Card element | Source |
|---|---|
| Id, version, authors, link | `.nuspec` (`id`, `version`, `authors`, `projectUrl`) |
| Name and entry points | The manifest `<Name>.settings.json` |
| Description, tags, paid flag | `package.info.json` and `.nuspec` |
| README | `readme.md` |
| Icon and cover | The first picture in `screenshots/`; a file named `icon` or `logo` outside that folder is used as the icon instead |
| Category | `package.info.json`, the **Category** field on the upload form, or the moderator |

A package without pictures shows the entry point symbol instead of an icon, but the technical
requirements of the store expect an icon and card pictures.

## What else the package carries

| Item | When |
|---|---|
| Icon and card pictures | Always |
| Your end-user licence terms | Unless you adopt the standard extension EULA of the store |
| Privacy disclosure | When the extension processes personal data |
| Third-party licence notices | When the package includes open-source or third-party components |

## Marker tag

The package tags must include `ency-extension`. The store catalog indexes only packages with
this tag. The template and `ExtensionManagerCLI pack-library` add it (see
[Publishing](publishing.md#upload-a-package)).

## SDK version

The extension must be built against a released SDK (`EncySoftware.CAMAPI.SDK.Net`) that the
store can install:

- A prerelease SDK is refused.
- An SDK newer than the store ceiling is refused. The store reports the ceiling as
  `registrableSdk` at its `/api/sdk` address (see [External references](references.md#store));
  pin the SDK package to that version or lower.
- An SDK newer than any released version of the CAM system gives a warning: the extension
  needs a version of the CAM system that is not released yet.

## Versions

- Versions follow NuGet semantic versioning. Prerelease versions are allowed and marked.
- A published version cannot be replaced. To fix a package, increase the version.
- The card shows the highest stable version. An older version number can be published and does
  not change the card.

## Package id and ownership

- The first developer who publishes a package id becomes the owner of the extension. Only the
  owner publishes its new versions.
- Ids that differ only in punctuation share the same card address, so the store refuses an id
  that differs from an existing one only in punctuation.
- If an id is already taken or reserved, choose another one or ask a moderator.

## Limits

| Limit | Value |
|---|---|
| Package size | 200 MB |
| Package id | 100 characters |
| Version, name, each tag, authors, link | 255 characters |
| Description | 4000 characters |
| Picture file name | 150 characters |
| Publications per account | 20 per day |

## Safety checks

- The store scans each package with an antivirus; an infected package is refused.
- An archive that is damaged or contains paths leading outside the package is refused.
- The moderator sees hints about native code, process start, network and registry access in
  the package. These hints are not a verdict, but expect questions if your extension uses them.

Review also checks the rules that no automatic check covers: no code from outside the package,
disclosed network use, quality and machine-output requirements (see
[Store rules and your obligations](store-rules.md#technical-requirements)).
