---
name: inspect-cldata
description: Inspect actual CLData files, commands, structure, and named parameters without guessing from documentation or raw indexes.
---

# Inspect CLData

## Trigger and when to use

Use this skill whenever a task depends on a CLData file, command, section, parameter, machine, operation, or project setting. Use it before changing an SPPX mask or .NET handler.

## Prerequisites and tool discovery

- Obtain a representative `.stcp` project or CLData file and confirm the CAM version, units, machine, enabled files, and data sensitivity.
- Discover the available CLData MCP/Inspector commands and their current schemas. Prefer named/typed access supplied by the tool over guessed indexes.
- If no inspector is available, use documented local tools or a reduced exported listing; state the limitation.

## Safe workflow

1. Open the project with the available CLData tool and record its project identity and machine information.
2. List files and command counts. Do not begin by dumping a large file.
3. Read the file skeleton/structure first. Use the skeleton to locate sections and command families.
4. List a small, relevant command range with indentation; exclude high-volume motion points when they are not relevant.
5. Fetch specific commands and named parameters, using the syntax dialect required by the target postprocessor. Inspect project parameters separately when needed.
6. Record actual values, units, coordinate systems, presence/absence, ordering, repetition, and boundary cases. Correlate them with the official CLData command page.
7. Reduce the fixture to only the commands needed to reproduce the behavior and retain a known-good output sample.
8. Give the development skill a factual map: command, handler, parameters, values, structure, and unknowns.

## Prohibited and unsafe actions

- Do not skip skeleton-first inspection on a large file or infer structure from a random command sample.
- Do not treat raw CLD positions as universal mappings, substitute .NET properties for SPPX names, or claim a parameter exists because documentation lists it.
- Do not modify source, project settings, machine configuration, or CLData while inspecting.
- Do not disclose full customer projects when a reduced fixture is sufficient.

## Completion criteria

Inspection is complete when the relevant real file and machine are identified, the skeleton and command range were examined, required values were obtained through verified paths, and all missing or ambiguous data is explicitly listed.

## User-visible presentation

Present a compact evidence table or equivalent containing file/section, command, parameter path, actual value, units, and source/tool used. Include the exact next handler or postprocessor path only when verified, plus fixture limits and unresolved questions.
