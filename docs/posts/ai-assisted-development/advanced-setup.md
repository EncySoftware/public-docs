# Advanced setup

This page is the full setup procedure and the reference for checking what was done. Hand it to the assistant as described in [Set up the tools](setup.md), follow it by hand when automatic setup is unavailable, or read it when a team needs repeatable results.

## What this is about

If you are an assistant reading this page to set the tools up, here is the ground you are standing on.

A CAM system calculates the toolpath and writes it out as **CLData** — a stream of commands and parameters that describes the machining independently of any particular machine. A **postprocessor** turns that stream into the **NC program** for one specific machine and control system: its codes, its formats, its conventions. Every machine on the shop floor needs its own, and adapting one is the daily work of the person you are helping.

There are two kinds of postprocessor, and they never mix:

- **SPPX** — a set of handlers, one per CLData command, written in a built-in Pascal-like language, executed by InP;
- **.NET** — a C# project built against the postprocessing SDK, executed by `InpCore.exe`.

Both read the same CLData. That is why reading the real project data always comes before changing code.

What you are being set up to do: read the input data through the CLData server, read and change a postprocessor through the InP server or the C# project, compile it, run it on a real test project, and compare the generated NC program with a known-good one. The VS Code extensions are the human's window into all of that — they show the data you found, the code you changed and the program you produced. The person you work with decides whether the result is correct; you produce the evidence they judge it by.

So the setup has four parts, in this order: the extensions, the folder each of them needs, the MCP servers, and the knowledge — this documentation plus the skills. After that, organise the workspace itself: see [Organize your workspace](workspace.md), and follow the `prepare-workspace` skill.

Record the versions when you report a problem: the CAM system, the extensions bundle, CAM Agent, the MCP servers and the AI client. Most "it worked yesterday" reports are version differences.

## Install the extensions

Visual Studio Code 1.85 or newer is required. In the unpacked bundle, `install.cmd` installs every `.vsix` next to it and replaces older versions; it needs the `code` command on `PATH`, which the VS Code installer adds by default. Without the script, install each file with `code --install-extension <file>.vsix`, or through **Extensions → Install from VSIX…** in VS Code. Then reload the window: `F1` (or `Ctrl+Shift+P`) opens the command palette, where **Developer: Reload Window** is run. Every command written in bold with a colon on this page is a VS Code command, run the same way.

The bundle holds four extensions: **SPPX Postprocessor Tools**, **CLData Inspector**, **DotNet Posts** and the updater.

## Point the extensions at the CAM installation

Each extension needs the folder where the CAM system is installed, because that is where the executables it drives live. This is the first setting on each extension's settings page:

| Setting | Needed by | Executable |
|---|---|---|
| `sppx.installationFolder` | SPPX Tools | `InP.exe` |
| `cldata.installationFolder` | CLData Inspector | `InpCoreMCP.exe` |
| `dotnetPosts.installationFolder` | DotNet Posts | `InpCore.exe` |

Both the product folder and its `Bin64` subfolder are accepted, and a path pasted with quotation marks is accepted as well. Instead of typing it, run the extension's command — for example **DotNet Posts: Select Installation Folder…** — and pick the folder in the dialog; the settings page offers the same picker as a link. SPPX Tools and CLData Inspector borrow each other's value while their own setting is empty, so in a normal installation the path is set once.

## Connect the MCP servers

MCP is what gives the assistant the ability to act. Any MCP-capable client works, and the configuration is the same everywhere except for the file it goes into.

**CLData MCP** — `InpCoreMCP.exe`, in the `Bin64` folder of the CAM installation. It works on its own: it opens a project (`*.stcp`, `*.stc`) or a single `*.inpcld` file and needs no running CAM system, and it never modifies the data.

**InP MCP** — `inp-mcp-server.exe`, shipped with CAM Agent; in a default installation `%LOCALAPPDATA%\CamAgent3\bin\inp-mcp-server.exe`. It drives the postprocessor IDE, and can either start an instance itself, windowed or headless, or attach to one you opened from the CAM system.

**CAM MCP** — `cam-mcp-server.exe`, next to the previous one. Optional, and not a postprocessor tool: it drives the running CAM system. Connect it when the answers you need are in the source project rather than in the CLData — the machine and its schema, the parameters of an operation, the tools and their properties, the coordinate systems and the workpiece setup. It can also produce the input you postprocess: recalculate the toolpaths, export the CLData of the active project, or create and open a test project. Useful when a test case has to be built or adjusted rather than merely read.

```json
{
  "mcpServers": {
    "inpcld": {
      "command": "C:\\Program Files\\<CAM installation>\\Bin64\\InpCoreMCP.exe",
      "args": []
    },
    "inp": {
      "command": "C:\\Users\\<user>\\AppData\\Local\\CamAgent3\\bin\\inp-mcp-server.exe",
      "args": []
    },
    "cam": {
      "command": "C:\\Users\\<user>\\AppData\\Local\\CamAgent3\\bin\\cam-mcp-server.exe",
      "args": []
    },
    "knowledge": {
      "command": "C:\\Users\\<user>\\AppData\\Local\\CamAgent3\\bin\\rag-mcp-server.exe",
      "args": []
    }
  }
}
```

The first two are what postprocessor work runs on; `cam` and `knowledge` are useful additions — leave out what you do not need.

Use absolute paths, and mind that JSON needs backslashes doubled. Where the configuration goes depends on the client:

| Client | Where the configuration goes |
|---|---|
| Kilo Code | `kilo.jsonc` in the project root or `.kilo/kilo.jsonc`; globally `~/.config/kilo/kilo.jsonc`. The UI writes it for you: settings icon → **Agent Behaviour** → **MCP Servers** |
| Roo Code | `.roo/mcp.json` in the project, or the global `mcp_settings.json` — **MCP Servers → Edit Project MCP** / **Edit Global MCP** |
| Cline | `cline_mcp_settings.json` — **MCP Servers → Configure** |
| Claude Code | `.mcp.json` in the project root, or `claude mcp add` |
| Copilot Chat in VS Code | `.vscode/mcp.json`, `servers` section |
| Codex CLI | `~/.codex/config.toml`, section `[mcp_servers.inpcld]` with `command = "…"` |

Where a client supports both levels, the project file takes precedence over the global one. The client has to be restarted after the file changes. Such a file contains local absolute paths, so keep it out of a shared repository.

These are plain executables on the same computer: the client starts one and talks to it directly over its standard input and output, so none of them needs a port, a service or an account of its own — the word "server" says nothing about the network here. That is why one configuration fits any client, and why a server that does not answer is a path or a permission problem. The knowledge server is the exception that proves it: documentation search goes out to an online service, while everything it has cached keeps working without one.

## Check the connection

Use a non-production project and a small read-only request for each server: the files of a CLData project, and a ping of InP with the structure of the open postprocessor. Compare the answers with the project you named. Never include a write, a source edit, an NC transmission or a machine connection in a connectivity test.

## Documentation and skills for the assistant

Besides the tools, the assistant needs the reference material.

Two sources, and they answer different questions.

- **The knowledge server** — `rag-mcp-server.exe`, in the CAM Agent folder next to the other servers. Add it to the MCP configuration the same way; it needs nothing else. It holds a snapshot of the published documentation — the product as a whole and postprocessing in particular — and searches it by keyword and by meaning, reads a page in full, and lists and searches the published skills. It can also index a CAM project so that its operations, tools and machine become searchable. This is what CAM Agent answers from, and the same server works for any MCP client. Being a snapshot, it is static by nature: it tells you what the product does, not what your team decided. It keeps a local cache, so ask the assistant to refresh it once — after that the skills are searchable offline.

  The published set can also grow from your side: a skill you wrote yourself can be submitted for review and, once accepted, becomes part of it for everyone. Submitting is done from the CAM Agent chat, and only for material you are willing to publish.
- **The workspace documentation** — your own, and it grows. Your projects, the techniques that work on your machines, the conventions your team has settled on, the cases you have already solved. This is the part the assistant cannot get anywhere else, and the part that makes its answers yours rather than generic. How to organise it is a topic of its own: [Organize your workspace](workspace.md).

  A checkout of the published documentation belongs in the workspace as well, next to your own: it is fixed at a revision you know, works with no network, and is what the assistant reads when it has to work through a whole section rather than look one thing up. The repository address is on the [External references and examples](xref:posts-external-references) page; clone it with `git clone --depth 1 <url>`, point the assistant at the `docs/posts` folder, and update it with `git pull`.

The skills published with this guide live in the `skills` folder of this documentation module — each one a folder with a `SKILL.md` file inside it. Take the whole set; it grows with the toolset, and an assistant only uses the skill that fits the task in front of it. In Kilo Code, copy the folders into `.kilo/skills/` in the project, or into `~/.kilo/skills/` (`%USERPROFILE%\.kilo\skills\` on Windows) to have them in every project; a new session picks them up, and `/reload` does it without restarting. In other clients it depends on the client — a workspace or user skills folder, an agent configuration entry, or manual inclusion. If your client has no skill mechanism, paste the relevant `SKILL.md` into the chat or reference it from the client's instruction file (`CLAUDE.md`, `AGENTS.md`, `.clinerules` and similar). CAM Agent manages its own set and keeps yours alongside it.

Whichever way they are provided, check that they are loaded: ask the assistant which skills and tools it currently sees.

## Updates on demand

The panels offer an update action when a new version is available. The same check runs from the palette: **Postprocessor Tools: Check for Updates**, then **Postprocessor Tools: Install Available Updates**, then **Developer: Reload Window**. Updates are configured by the bundle, so extensions installed by hand from separate `.vsix` files are never offered any.

## Several CAM installations on one computer

Each extension points at one installation folder, and the assistant runs whatever is in it. With a released version and a beta version side by side, decide which one the postprocessor is being developed against and set all three settings to it. When you switch, switch all of them — a mixed configuration where CLData is read by one version and the postprocessor is run by another produces results that cannot be reproduced.

One path is not covered by those settings. The `InpCoreDir` environment variable is written by the CLData Viewer when it starts, so it holds whichever installation's viewer ran last, and the debug configuration that comes with the .NET template launches `${env:InpCoreDir}/InpCore.exe` — debugging can therefore run a different version than the panels do, with no warning, because the run simply succeeds and gives different output. If you keep several versions, check that variable when results stop making sense. Changing it is not instant either: programs already running keep the old value, and in practice it takes signing out of Windows and back in for the new one to reach everything.

## Pin the documentation

For work that has to be reproducible, keep the documentation checkout at a known revision instead of pulling it constantly, and record that revision together with the postprocessor version. A retrieval service always answers from the current index, which is convenient for exploration and unhelpful when you need to explain why an answer changed.

## Give the assistant its own workspace

- Its own run configuration in the **Generate NC** panel, so your settings stay as you left them.
- Its own output folder for generated NC programs, outside the source tree.
- A branch or a copy of the postprocessor, never the production file.
- A reduced test project instead of the full customer project. Smaller data means a readable diff and a faster cycle.
- No credentials, tokens, customer archives or unrelated repositories in the workspace or in the instruction files.

## Automated checks

A headless run is suitable for a repeatable check: a fixed input project, a fixed postprocessor revision, captured logs and a stored NC program. Two rules keep it useful. Run it in a disposable working folder, so a failed run cannot leave a half-modified postprocessor behind. And review the diffs and the NC output outside the automation — an automated pipeline can tell you that output changed, never that the change is correct.

Do not connect an automated chain to a control system, and do not give it write access to production postprocessors.

## Rules worth writing into the instruction file

Put the requirements that always apply where the assistant always reads them — the workspace instruction file, or the skills. The ones that pay off in practice:

- read the actual project data before proposing a change, and cite the values used;
- read the current source of an item before editing it;
- compile, then run, then compare with the baseline — before reporting anything as done;
- keep the change minimal and explain what it does not cover;
- never send a program to a machine, and never change machine configuration.
