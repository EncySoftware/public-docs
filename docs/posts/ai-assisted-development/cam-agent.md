# CAM Agent

CAM Agent is the assisted-development entry point for CAM postprocessor work. It connects an AI client to supported CAM context and tools. It is not the same component as InP MCP or InP itself. Install it from the CAM Agent Extension Store in the supported host application. Use the Store entry and its release notes for current installation steps; do not copy extension files from an unknown location.

## Windowed and headless roles

The windowed role runs with the host application's user interface. Use it when you need to select a project, inspect a CLData view, open a postprocessor, or confirm an operation visually.

The headless role runs without the user interface. Use it for repeatable inspection, batch checks, and automation in a controlled workspace. Headless execution does not imply that the result is safe: it cannot replace machine simulation or human review.

The two roles may share documentation and source context, but they have different capabilities. A request that depends on a visible selection, dialog, or interactive preview belongs in the windowed role. A deterministic file operation or validation script may belong in the headless role.

## CAM Agent, InP MCP, and InP

- **CAM Agent** is the host integration and setup point.
- **InP MCP** is a service interface used by an AI client to request advertised InP operations.
- **Windowed InP** runs with the host UI and can use visible project context.
- **Headless InP** runs without the UI for controlled, repeatable operations.

InP MCP may use an available InP role, but it does not turn headless InP into a windowed session or make a UI-only operation available. Check the installed service capabilities rather than assuming a command exists.

## Postprocessor Tools

Postprocessor Tools 0.9.27 can assist with current postprocessor development tasks such as inspecting CLData-related data, working with postprocessor sources, and running supported checks. Exact commands and availability depend on the installed tool and host role. Ask the tool for its available commands instead of assuming that every example is implemented.

## Installation and first use

1. Open the CAM Agent Extension Store in the host application.
2. Install the CAM Agent Extension and restart the host if the Store requests it.
3. Run the automatic setup or health check offered by the installed agent. Treat a reported success as a connectivity indication, not as a functional or safety test.
4. If automatic setup is unavailable or incomplete, follow the documented manual setup for the installed AI client and services; do not invent settings or labels.
5. Open a non-production project and select the windowed or headless role appropriate for the task.
6. Run a safe, read-only smoke test: ask for a small project/file or CLData summary and confirm that the returned identity and counts match the selected test input. Do not write, generate production NC, alter settings, or transmit output during this test.

Keep the extension, Postprocessor Tools, CAM system, and documentation versions compatible. Record versions when reporting a problem.
