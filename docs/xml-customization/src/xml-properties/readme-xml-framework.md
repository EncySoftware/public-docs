# XMLProperties framework

The **XMLProperties** framework is how the CAM system describes its configurable
objects (operations, machines, tools, …) **declaratively**. Instead of hard‑coding the
parameters of a milling operation or a machine kinematic scheme, the system loads a tree
of **property descriptors** from XML. Each descriptor carries a name, a value type, a
default value, display metadata, and optional rules (visibility, enable/disable, computed
values). The running application turns this tree into the inspector UI, the data model
behind every project, and the values exposed through the CAM API. Because the model is
declarative, you can add a parameter, re‑group the inspector, change a default, or
describe a brand‑new machine — all by editing XML, without recompiling the application.

This area documents the framework itself — the part common to *every* kind of
descriptor. The operation‑ and machine‑specific guides build on it:
[Operations](../operations/readme-operations.md), [Machines](../machines/readme-machines.md).

Read top to bottom — each page builds on the previous one:

- **[Framework overview](framework-overview.md)** — the mental model: types vs.
  instances, namespaces, how files are loaded and combined, and where your own files
  go.
- **[Descriptor syntax](descriptor-syntax.md)** — the core reference: `SCType`,
  `SCProperty`, the type system, inheritance and overriding, and the full attribute
  catalog.
- **[Expression language](expression-language.md)** — computed values for
  `DefaultValue`, `Visible`, `Enabled` and friends: operators, functions, property
  references and accessors.
- **[Using XML properties from code](using-from-code.md)** — the one access pattern
  shared by the CAM API, native Delphi/C++, and postprocessors (.NET & `.sppx`).
- **[User defaults](user-defaults.md)** — overriding the shipped *default values* with
  your own preferred defaults, stored in `.usrdef` files and applied without editing
  `Supplement`.

(See the [documentation root](../index.md) for the intended audience.)

## The ground rules

These apply across *every* area — operations and machines included — so read them once
here.

> **You do not edit the `Supplement` folder.** The files under `Supplement` are the
> system's distribution files and are replaced on update. Your custom content goes into
> separate, dedicated folders that the system loads automatically. The `Supplement`
> files are still your best *reference* — read them to learn the patterns — but author
> your own files elsewhere. See
> [Where your custom files go](framework-overview.md#7-where-your-custom-files-go).

### Where the shipped files live

The shipped descriptor files live under the **program installation root**, for example:

```
C:\Program Files\<Vendor>\<Product>\Supplement\
```

These are read‑only system files — use them as a reference, but do not modify them.
Loading starts from a small set of root files under `Supplement`, each of which pulls
in the rest with `<SCInclude>` — including the optional, wildcarded extension folders
where your own files are picked up:

| Root file | Purpose |
|---|---|
| [`SCConfig.xml`](../../SCConfig.xml) | Master entry point — common types, operations, project schema, user defaults |
| [`Machines/MachinesConfig.xml`](../../Machines/MachinesConfig.xml) | Machine descriptors |
| [`STApplicationConfig.xml`](../../STApplicationConfig.xml) | Application‑level settings |
| [`Postprocessor/PostprocessorConfig.xml`](../../Postprocessor/PostprocessorConfig.xml) | Postprocessor descriptors |

### Conventions used in the examples

Short *synthetic* snippets (e.g. types named `TFoo`, `Bar`) illustrate pure syntax.
*Real* fragments quoted from the shipped `Supplement` files show how the rules are used
in production; these link back to the source file so you can see the full context.
File paths inside each guide are written relative to the `Supplement` folder.

### What this framework underlies

Operations and machines (documented in their own areas) are the main things you
customize with this framework. Other descriptor families — tools, the postprocessor
configuration and the application configuration — are built on the **same** framework,
but they are internal serialization data, maintained by the system's developers and not
intended for customization; they are therefore not documented in detail.
