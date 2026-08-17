# Getting started

## Install

CAM Agent is installed from the **Extension Store** of the CAM system: open the store,
install **CAM Agent**, and it appears paired with your CAM instance. The store keeps it up
to date.

## First launch

1. **Run** `CamAgent.exe` — on the first launch its components are extracted to
   `%LOCALAPPDATA%\CamAgent3\bin\`; subsequent starts are instant.
2. **Sign in** — the authorization screen appears: OAuth via Claude.ai (a browser window
   opens) or manual API key entry for any supported provider. Keys are validated against the
   provider before they are saved.
3. **Select a project** — open an existing project file, create a new one, or connect to an
   already running CAM system instance. The connection indicator in the title bar turns green
   when the CAM system is reachable.
4. **Start working** — type a request in the chat, press a Quick Action button, or run a
   slash command (see [Workflows and commands](workflows.md)).

## Requirements

- Windows 10 or newer
- .NET 10 Desktop Runtime
- An installed CAM system

## Updates

No manual steps: CAM Agent checks for a new version, downloads it, and restarts itself.
