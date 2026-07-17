# Postprocessing

A **postprocessor** converts the toolpath the CAM system produces — a neutral,
machine‑independent **CLData** stream (tool loads, moves, spindle/coolant switches, …) —
into the input files a specific CNC control expects (typically a G‑code program). Each
control family can require its own format, so the postprocessor is the adjustable part
that turns the universal commands into the exact output a given machine needs.

The CAM system has **two independent postprocessing subsystems**. They share the same job
and the same input (CLData), but differ in language, implementation and authoring style —
pick one per postprocessor; they are documented separately:

- **[Postprocessors generator (sppx postprocessors)](sppx/readme-sppx.md)** — postprocessors
  written in the built‑in **Pascal‑like language**, with the `.sppx` extension, authored in the
  dedicated **Postprocessors generator** application. Mature and self‑contained, with its own
  editor and masks/registers model.
- **[Postprocessors — .NET](dotnet/readme-dotnet.md)** — postprocessors built as **.NET
  assemblies** (`.dll`) against the postprocessing SDK, authored in a general‑purpose IDE
  (e.g. Visual Studio Code). The runner (`InpCore.exe`) reads the CLData and calls the
  postprocessor's command handlers.

Both subsystems read the **same CLData**; that shared input model is documented once under
[CLData](cldata/cldata.md) and referenced from each subsystem.
