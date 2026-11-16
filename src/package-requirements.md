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
| `build/docs/` | Documentation: Markdown pages and their pictures (see [Documentation and video](#documentation-and-video)) |
| `build/translations/<language>/readme.md` | Translations of the README, next to `readme.md` (see [README translations](#readme-translations)) |
| `build/<packageId>.targets` | The list of files for the installer |

The `.nuspec` must contain the package id and version, and its id and version must match
`package.info.json`.

## Where the card comes from

Most of the card is read from the package and changes only with a new version. The short
description, tags, the icon, the video and the category can also be set on the publication form;
what you set there stays on later versions.

| Card element | Source |
|---|---|
| Id, version, authors, link | `.nuspec` (`id`, `version`, `authors`, `projectUrl`) |
| Name and entry points | The manifest `<Name>.settings.json` |
| Short description, under the name in the catalog | The **Short description** field of the form or `summary` of the GitHub workflow, kept on later versions; otherwise the description in `package.info.json` and `.nuspec`, cut at a word to 160 characters |
| README | `readme.md` and its translations |
| Tags | `package.info.json`, plus up to 10 of your own from the form |
| Icon | The icon uploaded on the form; otherwise `<icon>` in `.nuspec`; otherwise the picture named by `iconPath` in `package.info.json`, relative to that file; otherwise a file named `icon` or `logo` in the package; otherwise the first picture in `screenshots/` |
| Cover and screenshots | The pictures in `screenshots/` |
| Documentation | The `docs` folder of the highest stable version |
| Video | The **Video** field of the form; otherwise `videoUrl` in `package.info.json` |
| Category | `package.info.json`, the form, **Change the category** in **My published**, or the moderator |
| Licence check | `licensed` in `package.info.json` or **Paid** on the form |

Without an icon the card shows the symbol of the entry point, but an icon and card pictures are
required by the technical requirements of the store.

## README translations

`readme.md` is the original. Put its translations next to it, in `translations/<language>/readme.md`,
for example `translations/de/readme.md` or `translations/pt-BR/readme.md`. The language is a
two-letter ISO 639-1 code, optionally with a region. The language of the original is `<language>`
in `.nuspec`.

The card offers a **README language** switch, and the store opens the README in the language the
user chose in its header, or in the language of the browser; without a matching translation it
shows the original. The **Extensions** tab of the CAM system shows the original.

The GitHub route does not carry `translations/` into the package yet: to publish translations,
upload the package.

## Documentation and video

**Documentation.** Put the pages in a `docs` folder of the package: `.md` pages and their `.png` or
`.jpg` pictures. The template copies `src/docs/` into the build, and the GitHub route carries the
folder as it is.

- `index.md` (or `readme.md`) at the root of the folder opens first; the other pages follow by
  path. A page's first heading is its title, or else its file name.
- Link pages and pictures relatively: `[Setup](setup.md#machine)`, `![Dialog](img/dialog.png)`.
  A link starting with `/` or leading out of the folder goes nowhere.
- Raw HTML in a page is not shown, and links to other sites open in a new tab.
- The card shows the documentation of its highest stable version on its own page, `/extension/<id>/docs`,
  and in the **Extensions** tab of the CAM system. A new version replaces it; a version without a
  `docs` folder removes it.

The publication is refused if the folder exceeds the limits below. Files of other types in the
folder and links to pages that are not there are warnings.

**Video.** A link to a YouTube or Vimeo video: `videoUrl` in `package.info.json`, or the **Video**
field of the publication form, which wins over the package. The card shows it as the first frame
of its gallery and the video plays on its own site; the store keeps no videos. Links to other
sites are refused.

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
- A paid extension must carry the `EncySdk` stamp: the CAM system neither installs nor loads a
  paid extension without it. SDK 3.0.19 and newer put the stamp into the build. The store looks
  for it in the `.dll` named after the manifest: `<Name>.settings.json` → `<Name>.dll`. The
  publication form reports a missing stamp as soon as the package is uploaded.

## Reserved functionality

`package.info.json` must contain `reservedDomains`: the Domains of Schedule A the extension works
in, or `[]` if none. A package without it is refused on every route (see
[Publishing](publishing.md#reserved-functionality)).

## Versions

- Versions follow NuGet semantic versioning. Prerelease versions are allowed and marked.
- A published version cannot be replaced. To fix a package, increase the version.
- The card shows the highest stable version. An older version number can be published and does
  not change the card.

## Package id and ownership

- The first developer who publishes a package id becomes the owner of the extension. New
  versions come from the owner, the members of the owning organization or the collaborators (see
  [Organizations and collaborators](organizations.md)).
- Ids that differ only in punctuation share the same card address, so the store refuses an id
  that differs from an existing one only in punctuation.
- If an id is already taken or reserved, choose another one or ask a moderator.

## Limits

| Limit | Value |
|---|---|
| Package size | 200 MB |
| Unpacked size | Four times the package size, at least 32 MB and at most 128 MB; up to 20 000 files |
| Package id | 100 characters |
| Version, name, each package tag, authors, link | 255 characters |
| Description | 4000 characters |
| Short description | 40 to 160 characters, at least 5 words |
| README | 65 536 characters |
| README translations | 20, each 65 536 characters |
| Documentation | 50 pages, 5 MB with the pictures, each page 65 536 characters |
| Video link | 255 characters |
| Picture file name | 150 characters |
| Your own tags on the form | 10 tags, 32 characters each |
| Icon uploaded on the form | PNG or JPEG, at least 32 px on each side |
| Publications per account | 50 per day, 20 attempts per hour |

## Safety checks

- The store scans each package with an antivirus; an infected package is refused.
- An archive that is damaged, contains paths leading outside the package, or whose table of
  contents disagrees with its entries is refused.
- The moderator sees hints about native code, process start, network and registry access in
  the package. These hints are not a verdict, but expect questions if your extension uses them.

Review also checks the rules that no automatic check covers: no code from outside the package,
disclosed network use, quality and machine-output requirements (see
[Store rules and your obligations](store-rules.md#technical-requirements)).
