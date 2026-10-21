# Geometry import into the CAM system

This chapter describes the **core of the Add-in** — transferring the model geometry from the CAD system to the CAM system. The geometry available through the CAD system API is converted into a file in the CAM system's internal format, which the CAM system then loads.

The base format for such a transfer is **SGF** (Structured Geometry File). It stores the topology (faces, edges, vertices) and the geometry (surfaces, curves, points) as a hierarchy of linked entities.

The file itself is built by the **STGeomFile.dll** library: it ships together with the CAM system and provides an API for building solids step by step — first the geometry primitives (surfaces, curves) are described, then the topology (faces and edges) is built on top of them, and finally the result is saved to a file.

The chapter is organized around the principle of "first *what* we import, then *how*". First, an abstract **[CAD model structure](cad-model.md)** is introduced — a hierarchy of objects (`CADDocument`, `CADPart`, `CADBody`, …) that in the subsequent examples we will transfer into SGF. Then come the two [import interfaces](import-interfaces.md) (`ISTGeomFiler` and `ISTGeomReceiver`), how to [connect the library](connecting-stgeomfile.md) in order to obtain them, how to [build the file itself](building-sgf.md), and the basic [SGF data structures](data-structures.md) — the types on which all the signatures are written. After that comes [working with assemblies](assembly.md): traversing the tree of components and their placement, and [working with a part](part.md): saving its solids. Then comes geometry import by type: [curves and points](curves-and-points.md), [faces](face.md), [surfaces](surfaces.md); [PMI annotations](pmi.md); [deprecated and unused methods](deprecated.md).

> **Example language.** All code examples in this chapter are given in C# — for consistency and clarity. The API itself is not tied to a language: it can be accessed from any language with COM support (`ISTGeomFiler` / `ISTGeomReceiver`).
