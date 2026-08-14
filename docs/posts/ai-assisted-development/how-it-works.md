# How the system works

You talk to a chat. Behind it, three kinds of things do the work: servers that let the assistant read the data and drive the postprocessor, extensions that show you what it found and produced, and the postprocessor runtime that turns CLData into an NC program.

The servers are reached over MCP — the Model Context Protocol, the standard way a chat client is given access to tools. That is why the same servers work in CAM Agent and in any chat extension you connect them to.

Do not read too much into the word *server* here. These are ordinary programs on your own computer, started by the chat client when it needs them; they exist so that the tools can talk to it, and nothing of yours is published or listens on the network. The one that does reach outside is the knowledge server, which queries the documentation service — and even that keeps a local cache.

```text
        you
         |
   AI chat  (CAM Agent, or a chat extension in VS Code)
         |
         +--> reads the input data          CLData MCP      (InpCoreMCP.exe)
         +--> reads and edits an SPPX post  InP MCP         (inp-mcp-server.exe)
         +--> drives the CAM system         CAM MCP         (cam-mcp-server.exe, optional)
         +--> searches the documentation    knowledge MCP   (rag-mcp-server.exe, optional)
         +--> shows you the data            CLData Inspector
         +--> shows you the code and runs   SPPX Tools, DotNet Posts
         |
         v
   InP (SPPX posts) / InpCore.exe (.NET posts)  --->  NC program
                                                        |
                                                        v
                                              simulation and your review
```

## The parts

| Part | What it gives you |
|---|---|
| CAM Agent | The chat inside the CAM system, with access to the project and the postprocessor |
| Skills | Instructions in plain language that the assistant follows, so the cycle is the same every time |
| CLData MCP | Lets the assistant read the input data: files, sections, commands, parameters, machine. It never changes anything |
| InP MCP | Lets the assistant work with an SPPX postprocessor: structure, code, registers, compile, run |
| CAM MCP | Optional. Lets the assistant look into the source project — machine, operations, tools — and prepare the input: recalculate toolpaths, export CLData, create a test project |
| Knowledge MCP | Optional. Searches a snapshot of the published documentation and of the skills — what the product does. What your team decided lives in your own notes instead |
| CLData Inspector | Shows you the commands and parameters the assistant is talking about |
| SPPX Tools | Editing support for `*.sppx` and the **Generate NC** panel |
| DotNet Posts | The same for C# postprocessors: navigation, build, run |
| InP | Runs SPPX postprocessors; also the IDE you can watch |
| `InpCore.exe` | Runs .NET postprocessors |

Two names are worth keeping apart when you read a message: `InP.exe` executes SPPX postprocessors, `InpCore.exe` executes .NET ones. And InP MCP is not InP itself — it drives an InP instance, so it reports a clear error when no instance is available.

## Windowed and headless

An SPPX postprocessor is executed by InP, and the assistant can start it two ways.

**Windowed** opens the IDE you can watch: the code it changed, the compile messages, the NC program. Use it whenever you want to follow along, and when the assistant gets stuck — you can take over in the same instance.

**Headless** runs without a window. It is faster and allows several parallel runs, but there is nothing on screen, so the report and the generated file are all you get.

If the assistant reports that it cannot start an instance, open InP from the CAM system yourself and let it connect.

## CLData is the same for both subsystems

Both postprocessing subsystems consume the same commands and parameters; only the syntax for reading them differs. This is why the assistant should always read the actual project instead of reasoning from a command name: the documentation explains what a command means, the project says what it actually contains.

## What the assistant is good at, and what it cannot do

It is good at finding the command that produced a given NC block, explaining an unfamiliar handler, drafting a small change in the style of the surrounding code, listing the cases a handler forgets, and comparing two NC programs block by block.

It cannot know machine behaviour that is absent from the data and the documentation, guarantee that generated code compiles, judge whether a motion is safe, or take responsibility for a postprocessor released to production. Compilation and a successful run prove that the software worked, not that the program is correct.
