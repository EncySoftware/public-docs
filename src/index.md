---
uid: main_page
---

# Postprocessor development

Postprocessors convert the CAM system's neutral **CLData** stream into the machine specific files required by a CNC control. This documentation covers the two postprocessing systems and the shared data they process.

## Main sections

- **[SPPX postprocessors](sppx/src/index.md)** - create postprocessors in the built in Pascal like language with the Postprocessors generator.
- **[.NET postprocessors](dotnet/src/index.md)** - build postprocessors as .NET assemblies using the DotnetPostprocessing SDK. The [API reference](dotnet/src/references.md) is part of this section.
- **[CLData](cldata/cldata.md)** - reference for the shared toolpath and technology command stream.
- **[AI assisted development](ai-assisted-development/index.md)** - configure tools and workflows for developing postprocessors with an assistant.

Choose a section above to start. The SPPX and .NET systems are independent authoring paths and use the same CLData input.
