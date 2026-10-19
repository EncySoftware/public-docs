# User defaults — overriding shipped defaults

Every property descriptor ships with a **default value** — the value a new object starts
with, declared as `DefaultValue` (and `InchDefaultValue`) in the XML
([§8](descriptor-syntax.md#8-attribute-catalog)). Those shipped values live under
`Supplement`, which you do **not** edit. Instead, the framework lets you set your **own**
default for any property — a *user default* — that takes precedence over the shipped one.
User defaults are stored in small `.usrdef` files, loaded at startup, and applied without
recompiling or editing `Supplement`.

This is the supported way to answer "I always want this parameter to start at *my*
value, not the factory value" — for a single seat, or rolled out across many.

## System default vs. user default

Two layers sit behind every property's default:

- the **system default** — the value shipped in the descriptor's `DefaultValue` /
  `InchDefaultValue`. It is read‑only and never changed by this mechanism; it is always
  there to fall back to.
- the **user default** — your override. When set, it becomes the property's *effective*
  default: new objects start from it, and "reset to default" returns to it.

Because the two are kept separately, you can always **reset to the system default** to
get the factory value back, or **remove** your user default entirely.

## Setting a user default from the inspector

You manage user defaults straight from the parameter inspector. Open a property row's
context menu (the same per‑row menu used to copy a property's full name — see
[Using XML properties from code](using-from-code.md)); it offers:

| Command | Effect |
|---|---|
| **Save as user default** | Make the property's current value your user default. |
| **Reset to user default** | Set the property back to your user default. |
| **Reset to system default** | Set the property back to the shipped (factory) value. |
| **Remove user default** | Forget your override; the system default applies again. |
| **Customize…** | Open the customization dialog for broader editing. |

Changes take effect **immediately** — there is no need to restart the application.

> **Metric vs. inch.** Just as descriptors carry both `DefaultValue` and
> `InchDefaultValue`, a user default is stored per measurement system: setting it while
> working in inches records an inch value that is independent of the metric one. Each is
> used when the project runs in the matching unit system.

> **Grouped inspector rows.** When several properties share one inspector row — a
> `Compact` complex type, or a unit‑switching radio‑edit row
> ([§9](descriptor-syntax.md#9-compact-and-radio-edit-rows)) — saving or resetting the
> row acts on **all** the properties visible in it together, not just the one you
> clicked.

## Where user defaults are stored

User defaults are kept in `.usrdef` files. They are pulled in at startup by the master
configuration with optional, wildcarded includes — for example, for the `Operations`
family:

```xml
<SCInclude Optional="True">$(SUPPLEMENT_FOLDER)\Defaults\*.usrdef</SCInclude>
<SCInclude Optional="True">$(LOCAL_OPERATIONS_FOLDER)\*.usrdef</SCInclude>
```

They are included **after** the system descriptors, which is why their values win over
the shipped defaults. The *Save as user default* command writes these files to your
user area automatically (the `$(LOCAL_OPERATIONS_FOLDER)` location, alongside your custom
operations — see [§7](framework-overview.md#7-where-your-custom-files-go)), so in
normal use you never edit them by hand. Other descriptor families are loaded the same
way by their own configuration.

## The `.usrdef` file format

For inspection, version control, or scripted roll‑out, a `.usrdef` file is plain
XMLProperties. It mirrors the path from a root type down to the overridden property, and
the leaf carries the override as a `UserDefaultValue` (or `UserInchDefaultValue`)
attribute:

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<SCCollection>
    <SCNameSpace ID="Operations">
        <TST2DContouringOp>
            <HelicalMachining>
                <Enabled UserDefaultValue="True"/>
            </HelicalMachining>
        </TST2DContouringOp>
    </SCNameSpace>
</SCCollection>
```

- One **`<SCNameSpace ID="…">`** per namespace (e.g. `Operations`, `Tools`, …); see
  [namespaces](framework-overview.md).
- The element nesting follows the **property path** from the root type
  (`TST2DContouringOp`) through any sub‑objects (`HelicalMachining`) to the property
  (`Enabled`).
- The leaf element carries **`UserDefaultValue`** for the metric default and/or
  **`UserInchDefaultValue`** for the inch default — never the system `DefaultValue`,
  which stays untouched.
- Conventionally there is **one file per root type**, named `<RootType>.usrdef` (e.g.
  `TST2DContouringOp.usrdef`).
- If a `.usrdef` refers to a type or property that the running system does not declare,
  that entry is simply **ignored** — a stale override does no harm.

## Deploying defaults across workstations

Because user defaults are just files, a standard configuration can be moved between
seats. Your custom operations together with their user defaults can be exported to, and
imported from, a single archive — letting an integrator prepare a house standard on one
machine and deploy it to others. The archive carries the operations configuration, the
custom operation files, optional icons, and the `Defaults\*.usrdef` files.

## Turning user defaults off

If you need the factory behaviour back wholesale, there is an escape hatch that disables
**all** user defaults at once: it moves every `*.usrdef` aside into a backup subfolder so
none are loaded. Since descriptors are read at startup, **restart the application** for
the change to take full effect.

---

Back to the **[XMLProperties framework](readme-xml-framework.md)** index.
