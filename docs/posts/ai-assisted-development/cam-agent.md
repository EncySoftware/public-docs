# Develop with CAM Agent

CAM Agent is the chat inside the CAM system. It is the shortest path from a task to a checked result: you describe what the NC program should look like, and the agent investigates the project, changes the postprocessor, compiles it, runs it and reports back. You do not have to open the code — although for SPPX you can watch every step in the postprocessor IDE if you want to.

## Install it

CAM Agent is a regular CAM system extension: open the **Extension Store** in the CAM system, install **CAM Agent**, and restart the CAM system if the store asks for it. There is no separate installer to download any more. Its own documentation, available from the store entry, covers the chat itself; this page covers only postprocessor work.

CAM Agent brings `inp-mcp-server.exe` with it, which is also the InP MCP server used by VS Code clients — see [Set up the tools](setup.md#connect-the-mcp-servers).

## The working cycle

1. Open a project that contains a short, representative piece of the toolpath. A small test project makes every following step faster and the comparison readable.
2. Open the postprocessor you want to change, or tell the agent which file to use.
3. State the task in terms of the NC program: which block is wrong, what it should look like, on which machine. "Add M08 after the tool change" is a workable task; "make the coolant right" is not.
4. Ask for a plan first, and for the data it is based on. The agent should name the CLData command it found and the handler that processes it before it proposes an edit.
5. Approve the change. The agent edits the handler, compiles the postprocessor, runs it on the same project and returns the generated NC program.
6. Read the report: the changed code, the compile messages, and the NC blocks that differ from the previous run.
7. Verify the result as described in [Review and verify](review-and-verify.md). Then either accept it or refine the task.

Steps 4 and 5 are where the time is saved or lost. An agent that has read the actual data produces a small, explainable edit; an agent that was not given a project guesses from the command name.

## What you see while it works

For SPPX the agent drives the postprocessor IDE. Started **windowed**, the IDE is on screen: the handler it edited, the compile messages, the generated NC program. This is the mode to use when you want to follow along, and it is also the mode to use when the agent gets stuck — you can take over in the same instance.

Started **headless**, InP runs without a window. It is faster and it can process several runs in parallel, but there is nothing on screen, so the report and the generated file are all you get.

For .NET postprocessors the agent works with the project and the batch runner, so there is no IDE to watch; you see the build result, the run report and the NC file.

## Knowledge

CAM Agent answers from an indexed copy of the product documentation and of the official skills, with an offline cache, and it keeps your own skills alongside them. It does not clone the documentation repository into your project; if you want the agent to read a specific local copy of the documentation, say so explicitly and give the path.

## Limits

The agent does not replace a postprocessing engineer. Two rules are worth stating plainly: do not let it change a production postprocessor without your review, and do not let it send an NC program to a machine. A run that ended with code 0 means the tools worked, not that the program is safe.
