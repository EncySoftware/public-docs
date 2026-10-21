# Introduction

This document describes the architecture and interaction protocols of CAM system Add-ins with CAD systems. Following these instructions, a developer can implement an Add-in for any CAD system that meets the minimum API requirements.

The document is not tied to a specific CAD system or a specific programming language. All examples of file formats and contracts are taken from real Add-ins (KOMPAS-3D, SolidWorks, etc.) and presented in a generalized form.

The main content of the document consists of two large chapters:

- **[Toolbar architecture](toolbar.md)** — which components make up the Add-in (the Translator, the Toolbar, and the accompanying files), how they are connected, and in which scenarios they interact: installing and removing the Add-in, as well as the two paths for transferring geometry to the CAM system.
- **[Importing geometry into CAM](geometry-import.md)** — the core of the Add-in: how to use the API of the `STGeomFile.dll` library to build a file in the CAM system's internal format (SGF), transferring the model's topology and geometry into it — bodies, faces, surfaces, curves, and PMI.

Although the source of geometry in the examples is a CAD system, **the geometry import itself is not tied to it**. The CAD system can be replaced with any other source — for example, a neutral exchange format (STEP, IGES, Parasolid, etc.): only the way the source geometry is obtained changes, while writing it to the SGF stays the same. For this reason, the chapter "[Importing geometry into CAM](geometry-import.md)" can also be used as a standalone guide to converting to SGF from an arbitrary source.
