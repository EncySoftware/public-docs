# How AI-assisted development works

You talk to an AI client — a chat in a code editor or in a terminal. The client reads the skills and the files of your working folder, edits the interpreter sources, builds the interpreter and starts the CAM system or ENCY Tuner, in which the interpreter simulates the NC programs. No special servers are needed, and the only Visual Studio Code extensions you need are the chat itself and the C# extension for building and debugging: the assistant works with the same files and programs as you do.

```text
        you
         |
   AI client  (chat in Visual Studio Code or in a terminal)
         |
         +--> reads the skills                    skills folder
         +--> reads the NC programs, machine      working folder
         |    project, controller manual, notes
         +--> edits and builds the interpreter    sources, .NET SDK
         |
         v
   CAM system or ENCY Tuner  --->  NC program simulation  --->  log
                                            |
                                            v
                                    comparison and your check
```

## What it consists of

| Part | What it is | What it gives you |
|---|---|---|
| AI client | A chat extension of Visual Studio Code or a terminal program | A conversation with an assistant that is allowed to read files, edit them and run commands in the working folder |
| Skills | `SKILL.md` text files | A way of working written in words, so the cycle is the same every time: facts first, then the change, then the check. The work is led by the general `interpreter-development` skill, which brings in the others as needed |
| Working folder | An ordinary folder on your computer | NC programs, machine project, controller manual and your notes — everything the assistant knows about your task |
| Interpreter sources | A C# project from a template or a native project | What the assistant changes |
| .NET SDK and Visual Studio Code with the C# extension | Build and debugging tools | Building the interpreter and running it under the debugger with the `F5` key |
| CAM system or ENCY Tuner | The installed product | Loads the interpreter and simulates NC programs in a G-code based operation |
| Interpreter interaction log | The product's log file | What the kernel and the interpreter did with each block: words read, warnings, errors |

## How the CAM system reads a block

The work is driven by the CAM system kernel, not by the interpreter: the kernel reads the NC program text, splits a block into words using the interpreter's register table, queues them and calls the interpreter's code to execute each word. Which functions are called and in what order is described in [G-code based program interpretation](../g-code-interpretation/g-code-based-program-interpretation.md); the `nc-interpreter-foundations` skill retells this for the assistant together with the traps that cause the most mistakes: the first movement of an operation, coordinates in a rotated coordinate system, spindles, cycles.

The meaning of each word is defined by the interpreter, and the same word means different things on different controllers. That is why the assistant always starts from the actual programs and the controller manual, not from the name of a word. The interpreter simulates what the controller would do, not what the CAM operation intended.

## C# (.NET) by default

The assistant creates a new interpreter in C# from a template of the CAM system. Such an interpreter is built with one command, is debugged in Visual Studio Code and is easy to read for people who know the machine better than programming. A native interpreter in Delphi or C++ — only when you explicitly asked for one or when you are changing an interpreter that is already native. In detail — [.NET workflow](dotnet-workflow.md) and [Native interpreter workflow](native-workflow.md).

## What the assistant does well and what it cannot do

It is good at listing every word that occurs in your programs, finding the place in the interpreter where a word is read, explaining unfamiliar code, preparing a small change in the style of the surrounding code, running all NC programs before and after the change and comparing the results block by block.

It cannot know controller behavior that is neither in the manual nor in the programs, see the machine, judge whether movements are safe, or take responsibility for an interpreter delivered to a customer. Why a successful build and a simulation without errors are not enough, and how to check the result, is described in [Checking and confirming the result](review-and-verify.md).
