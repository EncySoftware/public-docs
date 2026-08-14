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

Ask for two read-only things on a test project:

- the files of a CLData project — the answer should name the machine, the units and the files;
- a ping of InP with the structure of the open postprocessor — handlers, subroutines and objects.

Compare them with the project you named. If a tool does not answer, the setup is incomplete: an assistant without tools falls back to guessing from documentation, which is exactly what the tools are there to prevent.

## 5. Updates

When a new version is available, the postprocessor panels show an update action — that is the only thing you need to notice. Accept it, then reload the window.

## If something does not work

[Troubleshooting](troubleshooting.md) covers the usual symptoms. [Advanced setup](advanced-setup.md) holds the whole procedure in detail — the same page you handed to the assistant, so you can follow any step by hand and check what it did.
