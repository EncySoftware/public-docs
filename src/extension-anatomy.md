# Extension anatomy

An extension is a .NET library that the CAM system loads through a manifest. The template
already contains every file listed here; this page explains what the store and the CAM system
read from them.

## Files

| File | Purpose |
|---|---|
| `<Name>.dll` | The extension code. The CAM system creates its objects through the `CAMAPI.ExtensionFactory` class. |
| `<Name>.settings.json` | The manifest: the library and its entry points. Without it the CAM system does not register the extension and the store refuses the package. |
| `package.info.json` | Store metadata: package id, version, author, description, category, tags, SDK version, flags. |
| `readme.md` | The README on the store card: what the extension does and how to call it. |
| `screenshots/` | PNG, JPG, GIF or WebP pictures for the card. The first one becomes the icon and the cover. |

## Manifest

The manifest is a JSON file next to the library.

**name.** The library name. Required.

**description.** The library description. Required.

**module_path.** The path to the library. Required; the store refuses a manifest without it.

**unload_mode.** When the CAM system unloads the library: `umJustAfterExecution` (default),
`umBeforeProgramFinalization` or `umManuallyFromUI`. Optional.

**extensions.** An array of entry points. Each element is an object with exactly one key — the
entry point type — whose value describes the entry point: `id`, `name`, and the fields of that
type, for example `caption`, `hint_text` and `icon_path` for a utility.

The ids in the manifest must match the ids the factory creates. A minimal manifest is in the
template (`src/<Name>.settings.json`).

## Entry points

The entry point type decides where the extension appears in the CAM system. The store copies
the files and registers the extension, but does not run it.

| Type | Manifest key | Where it appears |
|---|---|---|
| Utility | `utility` | The **Utilities** palette, opened by the **Utilities** button on the top toolbar or Ctrl+Shift+E |
| Operation popup | `operation_popup` | The context menu of an operation in the technology tree |
| Geometry node popup | `geom_model_node_popup` | The context menu of a node in the geometry model tree |
| Operation solver | `OperationSolver` | An operation in the project; the extension calculates the operation and its toolpath |
| Global | `global` | No visible place; runs when the CAM system starts and finishes |
| CLData converter | `geom_cldata_converter` | No visible place; processes CLData after toolpath calculation |
| Utility runner | `utility_runner` | No visible place; runs or wraps other utilities |

Code skeletons of every type, and further types with their examples, are in the
`cam-api-examples` repository (see [External references](references.md)).

## package.info.json

The store builds the card from this file together with the package metadata.

**packageId.** The package id. It identifies the extension in the store; the first publisher
of an id becomes its owner (see [Package requirements](package-requirements.md#package-id-and-ownership)).

**version.** The extension version, in NuGet format.

**description**, **author.** The card description and author.

**category.** What the extension does. The category list is on the **Publish** page of the
store website; a moderator sets the category if you leave it empty.

**tags.** Card tags. The list must keep the store marker tag (see
[Package requirements](package-requirements.md#marker-tag)).

**sdkVersion.** The SDK version the extension is built with. The card shows the minimum
version of the CAM system from it.

**requiresRestart.** `true` if the CAM system must be restarted after installation.

**licensed.** `true` for a paid extension (see [Paid extensions](paid-extensions.md)).

**reservedDomains.** The reserved functionality declaration (see
[Publishing](publishing.md#reserved-functionality)).
