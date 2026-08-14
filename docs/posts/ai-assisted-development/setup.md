# Set up the tools

The setup itself is the assistant's job. Your part is small: install the chat you are going to talk to, put two files on disk, and hand them over. Everything after that — installing the extensions, connecting the MCP servers, pointing them at the CAM installation, loading the skills — the assistant does and reports back.

## 1. Install the assistant

**In the CAM system.** CAM Agent is installed from the CAM system's own **Extension Store**: open the store, install **CAM Agent**, restart the CAM system if it asks. Nothing else is needed to start — see [Develop with CAM Agent](cam-agent.md).

**In Visual Studio Code.** The chat is an extension like any other: open the **Extensions** view (`Ctrl+Shift+X`), find the one you want by name in the Marketplace, and install it. Which one to take, and what makes a client suitable for this work, is in [Develop in Visual Studio Code](vscode.md#which-chat-extension-to-use); a client that lives in the terminal is installed its own way instead. You also need an account with an AI provider — see [What it costs](index.md#what-it-costs).

If you work only through CAM Agent, the rest of this page still applies to the knowledge and skills it uses; the tools bundle below is for the VS Code way of working.

## 2. Get the two files

Both addresses are on the [External references and examples](xref:posts-external-references) page.

- **The tools bundle** — an archive whose name starts with `posts-vscode-extensions-`. Download and unpack it; do not install anything yet.
- **This documentation as Markdown** — clone it with `git clone --depth 1 <url>`, or download it as an archive and unpack. The setup instruction the assistant needs is the page `docs/posts/ai-assisted-development/advanced-setup.md` inside it.

If your client is already connected to a documentation service, the second file is unnecessary: the assistant can find the page by name.

## 3. Hand both to the assistant

Open the chat, allow it to run commands in your workspace, and give it the task. Adjust the paths and paste:

```text
Set up the postprocessor tools for me, following the instruction in
<docs>\docs\posts\ai-assisted-development\advanced-setup.md

The unpacked extensions bundle is in <bundle>
The CAM system is installed in <cam>

Install the extensions, connect the CLData and InP servers to this client,
point the extensions at the CAM installation, and load the published skills.
Then tell me what you changed and which tools you can now see.
```

Two things the assistant cannot do for you: reload the editor window, and restart the chat client after the MCP configuration changes. It will tell you when either is needed.

## 4. Check that it worked

Two requests in the chat are enough. Both are safe: the assistant only reads, changes nothing and runs nothing on a machine.

**Reading the data.** Take any CAM project — a `*.stcp` file, preferably a small test one — and write in your own words, roughly:

> Read the CLData of the project `D:\Test\Sample.stcp` and tell me the machine, the units, and how many command files there are.

A good answer names the machine, the units, and lists the files with the number of commands in each — facts from your file. Compare them with the project: if the machine is not the one you expected, you gave the wrong path.

**Reading a postprocessor.** Take a `*.sppx` file and write:

> Read the postprocessor `D:\Posts\Sample.sppx` and list its handlers, subroutines and registers.

A good answer is a list of names taken from that file. For SPPX the assistant needs a working InP: it will either start one itself or ask you to open the postprocessor in it.

**How to spot a failure.** An assistant without tools does not go quiet — it reasons instead: it lists "typical" handlers such as `OnRapid` and `OnLine`, explains how CLData is usually arranged, or asks you to paste the file contents. All of that means the tool it needed is not connected — go back to step 3, or to [Advanced setup](advanced-setup.md).

## 5. Updates

When a new version is available, the postprocessor panels show an update action — that is the only thing you need to notice. Accept it, then reload the window.

## If something does not work

[Troubleshooting](troubleshooting.md) covers the usual symptoms. [Advanced setup](advanced-setup.md) holds the whole procedure in detail — the same page you handed to the assistant, so you can follow any step by hand and check what it did.
