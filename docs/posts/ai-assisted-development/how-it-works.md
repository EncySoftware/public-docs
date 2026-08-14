# How the system works

Four kinds of components take part. Knowing which is which saves most of the confusion when something does not work.

```text
        you
         |
   AI chat client                        knowledge
   (CAM Agent, or an     <-------------  skills + this documentation
    extension in VS Code)                (as local Markdown, or from a RAG service)
         |
         |  MCP tools                    what the assistant can do
         +--> CLData MCP  (InpCoreMCP.exe)      read the input data
         +--> InP MCP     (inp-mcp-server.exe)  read, edit, compile and run an SPPX postprocessor
         |
         |  VS Code commands and links    what you see
         +--> CLData Inspector                  the actual commands and parameters
         +--> SPPX Tools                        the postprocessor code, Generate NC
         +--> DotNet Posts                      the C# project, Generate NC
         |
         v
   InP / InpCore.exe  ------------------> the generated NC program
                                                |
                                                v
                                          simulation and your review
```

## The components

| Component | What it is | What it is not |
|---|---|---|
| AI chat client | Where you state the task and see the answer: the CAM Agent chat, or a chat extension in VS Code | Not a postprocessor tool by itself; without MCP servers it can only talk |
| Skills | Markdown procedures that tell the assistant which tools to call and what to check | Not a replacement for the language and CLData reference |
| CLData MCP (`InpCoreMCP.exe`) | Read-only access to the input data: files, sections, commands, named parameters, machine information | It never changes CLData and never runs a postprocessor |
| InP MCP (`inp-mcp-server.exe`) | Drives the postprocessor IDE: structure, source code, registers, compile, interpret | Not the IDE itself, and not a .NET postprocessor tool |
| CLData Inspector | The VS Code panel that shows you what the assistant found in the data | Not a data editor |
| SPPX Tools | The VS Code extension for `*.sppx`: highlighting, outline, navigation, Generate NC | Not the compiler; it drives the installed generator |
| DotNet Posts | The VS Code extension for C# postprocessors: setup, navigation, build and run | Not a C# language service; that is the C# extension |
| InP | The postprocessor IDE and runtime for SPPX; runs windowed or headless | Not a CAM system and not a simulator |
| `InpCore.exe` | The batch runner for .NET postprocessors: extracts settings, processes a project | Unrelated to SPPX postprocessors |

Two mistakes are worth naming, because they cost the most time. **InP MCP is not InP**: the server is an adapter that drives an InP instance, and it fails with a clear error when no instance is available. **`InpCore.exe` is not headless InP**: `InP.exe` runs SPPX postprocessors, `InpCore.exe` runs .NET postprocessors, and each has its own batch mode.

## Windowed and headless

An SPPX postprocessor is executed by InP, which the assistant can start in either of two modes.

**Windowed** opens the IDE you can watch. Use it whenever you want to see what the assistant is doing: the code it changed, the compile messages, the NC program it produced. This is the default and the right choice when you are at the computer.

**Headless** starts a worker without a window. Use it for batch checks and for several parallel runs. There is nothing to look at, and nothing to approve — a headless run is exactly as trustworthy as the review you do afterwards.

Both modes need a CAM installation new enough to ship the instance manager. If the assistant reports that the manager is unavailable, open InP from the CAM system yourself and let the assistant connect to it.

## CLData is the contract

Both postprocessing subsystems consume the same commands and parameters. The difference is only in how the code addresses them: the SPPX language and the .NET SDK use different syntax and different index bases for the same values. This is why the assistant should always read the actual project through CLData MCP rather than reason from a command name: the documentation explains what a command means, and the project says what it actually contains.

## What the assistant does well, and what it cannot do

It is good at finding the command that produced a given NC block, explaining an unfamiliar handler, drafting a small change with the conventions of the surrounding code, listing the cases a handler forgets, and comparing two NC programs block by block.

It cannot know machine behaviour that is not in the data or the documentation, guarantee that generated code compiles, judge whether a motion is safe, or take responsibility for a postprocessor released to production. Compilation and a successful run prove that the software worked, not that the program is correct.
