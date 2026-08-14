# Set up the tools

Three things have to be in place: the VS Code extensions that show you data and results, the MCP servers that let the assistant act, and the documentation the assistant reads. If you work only through the CAM Agent chat, you need the CAM Agent extension instead of the VS Code bundle — see [Develop with CAM Agent](cam-agent.md) — and the rest of this page still applies to knowledge and skills.

## Install the VS Code extensions

Visual Studio Code 1.85 or newer is required, with its command-line launcher `code` available on `PATH` — the installer uses it, and reports an error if it is missing.

1. Download the tools bundle archive — its name starts with `posts-vscode-extensions-`. The download location for your product edition is listed on the external references page of this documentation set.
2. Unpack the archive. Next to the `.vsix` files it contains `install.cmd`, a `readme.md` with the exact contents of that build, and the update manifest.
3. Run `install.cmd` — a double-click is enough. It installs every `.vsix` lying next to it and waits for a keypress so you can read the result. It does not use PowerShell, so the script execution policy does not affect it.
4. In VS Code, press `F1` and run **Developer: Reload Window**.

To install without the script, use `code --install-extension <file>.vsix` for each file, or **Extensions → Install from VSIX…** in VS Code.

The bundle contains four extensions:

| Extension | What you get |
|---|---|
| SPPX Postprocessor Tools | Syntax highlighting and outline for `*.sppx`, navigation, and the **Generate NC** panel |
| CLData Inspector | Files, commands grouped by structure sections, and command parameters |
| DotNet Posts | Setup, navigation, build and run for C# postprocessors, with its own **Generate NC** panel |
| Postprocessor Tools updater | Checks the release feed and installs new versions of the other three |

## Point the extensions at the CAM installation

Each extension needs to know where the CAM system is installed, because that is where the executables it drives live. This is the first setting in each extension's settings page:

| Setting | Needs | Executable |
|---|---|---|
| `sppx.installationFolder` | SPPX Tools | `InP.exe` |
| `cldata.installationFolder` | CLData Inspector | `InpCoreMCP.exe` |
| `dotnetPosts.installationFolder` | DotNet Posts | `InpCore.exe` |

Both the product folder and its `Bin64` subfolder are accepted, and a path pasted with quotation marks is accepted as well. Instead of typing the path, run the extension's **Select Installation Folder…** command — for example **DotNet Posts: Select Installation Folder…** — and pick the folder in the dialog. SPPX Tools and CLData Inspector borrow each other's value while their own setting is empty, so in a normal installation you set it once.

## Keep the extensions up to date

The updater reads the release feed configured in the bundle you installed from, so it always looks at the right edition. It checks on startup and when a postprocessor panel is activated; when a new version is available, the panels show an update action.

You can also run it yourself: **Postprocessor Tools: Check for Updates** and **Postprocessor Tools: Install Available Updates**. After an update, reload the window.

## Connect the MCP servers

MCP is how the assistant gets the ability to act. Both servers speak stdio, so any MCP-capable client can use them, and the configuration is the same everywhere except for the file it goes into.

**CLData MCP** — `InpCoreMCP.exe`, in the `Bin64` folder of the CAM installation. It works on its own: it opens a project (`*.stcp`, `*.stc`) or a single `*.inpcld` file, works on a temporary copy, and needs no running CAM system.

**InP MCP** — `inp-mcp-server.exe`, shipped with CAM Agent; in a default installation it is `%LOCALAPPDATA%\CamAgent3\bin\inp-mcp-server.exe`. It drives the postprocessor IDE. It can start an InP instance itself, windowed or headless, and it can also attach to an instance you opened from the CAM system.

A configuration with both servers looks like this:

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
    }
  }
}
```

Use absolute paths, and mind that JSON needs backslashes doubled. Where the configuration goes depends on the client:

| Client | File |
|---|---|
| Claude Code | `.mcp.json` in the project root, or `claude mcp add` |
| Cline, Roo Code, Kilo Code | `cline_mcp_settings.json` — **MCP Servers → Configure** |
| Copilot Chat in VS Code | `.vscode/mcp.json`, `servers` section |
| Codex CLI | `~/.codex/config.toml`, section `[mcp_servers.inpcld]` with `command = "…"` |

Such a configuration file contains local absolute paths, so keep it out of a shared repository.

## Check the connection

Do this once, on a test project, before you give the assistant real work. Both checks are read-only.

- CLData: ask for the files of a project. The assistant should call `cld_open_project` and come back with the machine, the units and the file list. Compare them with the project you named.
- InP: ask it to ping InP and show the structure of the open postprocessor. The assistant should call `pp_ping` first and then `pp_get_structure`, returning handlers, subroutines and objects.

If a server does not answer, it is a setup problem. An assistant that cannot reach a tool will fall back to guessing from documentation, which is exactly what you connected the tools to avoid.

## Give the assistant the documentation and skills

The assistant needs the reference material as well as the tools. Two ways to provide it:

- **Local Markdown.** This documentation is published as a Markdown repository; the location is on the external references page of this documentation set. Clone it with `git clone --depth 1 <url>` and point the assistant at the `docs/posts` folder — as a second workspace folder, or by naming the path in the client's instruction file. Update it with `git pull`.
- **A retrieval service.** CAM Agent answers from an indexed copy of the documentation and skills, with an offline cache. A separate retrieval server for VS Code clients is planned; until it ships, use the local checkout.

The five skills published with this guide live in the `skills` folder of this module: `postprocessor-development`, `inspect-cldata`, `develop-sppx-postprocessor`, `develop-dotnet-postprocessor` and `verify-nc-program`. Each is a folder with a `SKILL.md` file. How to enable them depends on the client — a workspace or user skills folder, an agent configuration entry, or manual inclusion. If your client has no skill mechanism, paste the relevant `SKILL.md` into the chat, or reference it from the client's instruction file (`CLAUDE.md`, `AGENTS.md`, `.clinerules` and similar). CAM Agent manages its own set of skills and keeps yours alongside them.

Whichever way you provide them, check that they are actually loaded: ask the assistant which skills and tools it currently sees.
