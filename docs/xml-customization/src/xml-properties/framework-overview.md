# Framework overview

This chapter gives you the mental model behind the XMLProperties framework. Once
you understand the four core ideas below, the rest of the syntax is detail.

## 1 What the framework is for

Every configurable object in the CAM system — a technological operation, a machine,
a tool, a project — is described by a tree of **properties**. A property has a
name, a value, a type, a default, and metadata that tells the UI how to present
it and tells the engine how to behave.

These property trees are not written in code. They are declared in XML
descriptor files and loaded at startup. This means you can:

- add or remove parameters on an operation or machine,
- change default values (including separate metric / inch defaults),
- reorganize how parameters are grouped and shown in the inspector,
- make a parameter appear, disappear, enable or disable depending on other
  parameters,
- define an entirely new operation or machine,

all by editing XML.

## 2 Types vs. instances

This is the single most important distinction in the framework.

- A **descriptor (type)** is a *template*. It says "a `RoughPasses` block has a
  boolean `Enabled` defaulting to `true` and a `Step` of `1 mm`." Descriptors are
  declared with `<SCType>` (and, at the top level, `<SCProperty>`). They form an
  inheritance chain: a type can be based on another type and extend or override
  it.

- An **instance (property pointer)** is an *actual value* attached to a concrete
  object — for example, the `RoughPasses.Step` of one particular facing
  operation in your project. Instances are created from descriptors when an
  object is created, and they hold the real, editable data.

You author **descriptors**. The application creates **instances** from them. When
you read or write values through the CAM API
(see [Using XML properties from code](using-from-code.md)), you work with instances.

A key consequence: a property instance whose value still equals its descriptor's
default is *not* stored verbatim — it is computed from the descriptor on demand.
Changing a default in XML therefore affects every existing instance that hasn't
been explicitly edited.

## 3 The shape of a descriptor tree

Descriptors nest. A `ComplexType` descriptor contains child descriptors; those
children may themselves be complex; arrays contain a single child that acts as
the element template; enumerations contain their items as children. So a single
operation descriptor is a deep tree whose leaves are simple values (numbers,
strings, booleans, enum selections).

```xml
<SCType ID="TFinishPasses" type="ComplexType">
    <SCType ID="Enabled" type="Boolean" DefaultValue="true"/>
    <SCType ID="Step"    type="Double"  DefaultValue="1" DimensionKind="Linear"/>
    <SCType ID="Count"   type="Integer" DefaultValue="1"/>
</SCType>
```

Navigation through the tree later (in expressions and in the API) uses dotted
paths like `FinishPasses.Step`.

## 4 Namespaces

Descriptors are grouped into **namespaces**. A namespace is a self‑contained
dictionary of type names: the `TSTFaceMillingOp` operation type lives in the
`Operations` namespace, a machine type lives in the `Machines` namespace, and so
on. Two namespaces may contain types with the same name without clashing.

Namespaces are declared with `<SCNameSpace ID="...">`. The same physical type
file is often included into more than one namespace (for example, the shared
[`CommonTypes.xml`](../../CommonTypes.xml) is included almost everywhere), so the
common building blocks are available wherever they are needed.

The main namespaces you will encounter:

| Namespace | Contents |
|---|---|
| `Operations` | Technological operation types |
| `Machines` | Machine types and their kinematic building blocks |
| `Project` | Project / setup schema |
| `Application` | Application‑level settings |
| `Postprocessor` | Postprocessor descriptors |
| `OperationRegistrator` | Small "registration" records that announce which types are real operations (see [Operation descriptors](../operations/operation-xml-descriptors.md)) |

## 5 How files are loaded and combined

Loading begins at a root file (such as [`SCConfig.xml`](../../SCConfig.xml)) and
follows `<SCInclude>` directives to assemble the whole model. Three rules matter:

1. **Order is significant.** Files are processed top to bottom. A type must be
   declared before it is used as a base type, and later declarations can override
   earlier ones. This is why the root files include abstract/base types before
   the concrete types that derive from them.

2. **Includes can be optional and wildcarded.** `Optional="True"` means "load
   this if it exists, otherwise skip silently"; wildcards like `*_ExtOp.xml`
   let you drop extension files into a folder without editing the root config.
   Several of these optional, wildcarded includes point at folders **outside**
   `Supplement` — that is exactly how your custom content is loaded without
   touching the system files. See [§7](#7-where-your-custom-files-go).

3. **Paths use folder variables.** Instead of absolute paths, includes (and file
   references such as icons) use `$(VARIABLE)` placeholders that resolve to real
   folders at runtime. See [§7](descriptor-syntax.md#7-path-variables) for
   the list.

```xml
<!-- from SCConfig.xml -->
<SCInclude>$(SUPPLEMENT_FOLDER)\CommonTypes.xml</SCInclude>
<SCInclude>$(SUPPLEMENT_FOLDER)\Operations.xml</SCInclude>
<!-- optional, wildcarded, loaded only if present -->
<SCInclude Optional="True">$(LOCAL_OPERATIONS_FOLDER)\*.usrdef</SCInclude>
```

> **Not every namespace has a root file on disk.** Assembling a namespace is just
> "open the namespace, load a sequence of files into it, close it." That sequence
> is usually declared in XML (`<SCNameSpace>` + `<SCInclude>`), but the
> application can also build a namespace **in memory at startup** by loading the
> same building‑block files in order. The `Project` namespace is built this way —
> there is no single project root config file; the system loads
> [`CommonTypes.xml`](../../CommonTypes.xml),
> [`ProjectSchema/CommonProjectSchema.xml`](../../ProjectSchema/CommonProjectSchema.xml),
> [`ProjectSchema/ProjectSchema.xml`](../../ProjectSchema/ProjectSchema.xml) and a
> few others into a fresh `Project` namespace. The result is identical to the
> declarative form — so if you can't find a root file for a namespace, that is why.

## 6 What the framework drives

A single descriptor tree feeds several subsystems at once. Understanding this
explains why a descriptor carries so many different attributes:

- **The data model** — the actual values stored in a project.
- **The inspector UI** — labels, grouping, ordering, icons, which rows are
  visible/enabled, and special editors. Most "presentation" attributes
  (`Caption`, `Visible`, `Compact`, `Category`, `ImageFile`, …) exist for this.
- **The processing engine** — solvers and the toolpath/NC pipeline read property
  values by name.
- **The CAM API** — external code reads and writes the same properties.

The next chapter is the reference for the syntax that all of this is built on.

## 7 Where your custom files go

The `Supplement` folder is **read‑only system content** — it is overwritten on
every update, so any change you make there is lost. Instead, the root configs
include a number of *optional, wildcarded* locations **outside** `Supplement`,
reserved for your content. Put your files there and they are loaded automatically
alongside the system descriptors, in the right order.

The locations are addressed through [path variables](descriptor-syntax.md#7-path-variables)
so they resolve correctly per installation and per user:

| You want to add… | How | Loaded by |
|---|---|---|
| A new / extended **operation type** (automatic by name) | drop an `*_ExtOp.xml` file in `$(COMMON_CONTAINERS_FOLDER)` | [`Operations.xml`](../../Operations.xml) |
| A new **operation type** (registered via wizard) | register your operation XML file with the *Operations Manager* (see below) → it is added to `$(OPERATIONS_FOLDER)\UserOperationsList.xml` | [`Operations.xml`](../../Operations.xml) |
| **User default overrides** | place `*.usrdef` files in `$(LOCAL_OPERATIONS_FOLDER)` | [`SCConfig.xml`](../../SCConfig.xml) |
| A **custom machine** | build it with the machine‑building tools; stored in `$(SCHEMAS_FOLDER)` / `$(CUSTOM_SCHEMAS_FOLDER)` | the machine‑building subsystem |

Guidelines:

- **Operations — two ways.** There are two independent mechanisms for adding a
  custom operation, and both load *after* the system operations, so either can
  declare new operation types or override existing ones:
  - **By naming convention.** Drop an `*_ExtOp.xml` file into
    `$(COMMON_CONTAINERS_FOLDER)`. Any file matching the mask is picked up
    automatically — nothing else to configure.
  - **Via the Operations Manager wizard** (menu **Utilities → Operations
    Manager**). You point the wizard at your operation's XML file (kept wherever
    you like); it registers that file by adding an entry to
    `$(OPERATIONS_FOLDER)\UserOperationsList.xml`. That list file is *maintained
    by the wizard* — you don't hand‑edit it.

  In both cases the operation file itself is an ordinary descriptor file (an
  `<SCCollection>` in the `Operations` namespace); only how it gets registered
  differs.
- **Machines.** Custom machines are normally created interactively with the
  **MachineMaker** application, which writes their kinematic schemes to the machine
  schema folders — not to `Supplement`. Hand‑written XML is only for special cases;
  the machine descriptor syntax in the [Machine descriptors](../machines/machine-descriptors.md) guide is what those schemes
  are built from.
- **Read, don't edit, `Supplement`.** Treat the shipped files purely as a
  reference for the patterns and base types you build on.

The mechanics are identical wherever the file lives: same `<SCCollection>` root,
same namespaces, same syntax. Only the *folder* differs.

---

Next: **[Descriptor syntax](descriptor-syntax.md)**
