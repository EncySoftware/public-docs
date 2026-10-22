# ENCY documentation

[Open the ENCY documentation center](https://docs.encycam.com/portal/)

The documentation covers the main ENCY products and development tools:

- **ENCY CAM** — CAD/CAM programming, machining and production planning.
- **ENCY Robot** — robot programming and manufacturing workflows.
- **ENCY Hyper** — hybrid manufacturing workflows.
- **MachineMaker** — configuration of machines, robots and turn-milling equipment.
- **Technical guides** — CAM API, CAM Agent, postprocessor development, CAD integration,
  Extension Store and XML customization.

## Translating the documentation

1. Open the branch for the guide and version you want to translate. Start from the English source,
   or improve an existing translation when one is already available. The branch contains the
   Markdown source and its attachments.
2. Create a fork of this repository and a translation branch in your fork. Do not edit `main`.
3. Translate the Markdown text while preserving file names, page IDs, headings, links, anchors,
   examples, tables, conditions, numbers, units and attachments. Save files as UTF-8.
4. Keep API names, namespaces, code, commands and other technical identifiers unchanged. Keep
   programming and machining terms in English when they are used as technical terms.
5. Check links and images, commit the translation, and push the branch to your fork.
6. Open a pull request against the original documentation branch. Describe the translated pages,
   remaining work and terminology questions. Do not target `main`.

The maintainers review the translation and publish approved changes. If the source branch has
changed meanwhile, update your translation from its current version before submitting it.
