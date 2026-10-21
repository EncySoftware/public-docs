# Getting started

## Install

CAM Agent is installed from the **Extension Store** of the CAM system: open the store and
install **CAM Agent** — a **CAM Agent** button appears among the utilities of the CAM
system. Restart the CAM system after installing: a running instance does not pick up a
newly installed extension.

## First launch

1. **Press the CAM Agent button** among the utilities of the CAM system. If the assistant
   is not on the machine yet, the button offers to download it (about 480 MB) and starts it;
   on the first start its components are extracted to `%LOCALAPPDATA%\CamAgent3\bin\`,
   subsequent starts are instant. If it is already installed, the button simply opens it,
   connected to the CAM instance it was pressed from.
2. **Sign in** — the authorization screen appears: OAuth via Claude.ai (a browser window
   opens) or manual API key entry for any supported provider. Keys are validated against the
   provider before they are saved.
3. **Select a project** — when started from the button, the assistant is already connected
   to that CAM instance and the connection indicator in the title bar is green. Open an
   existing project file or create a new one.
4. **Start working** — type a request in the chat, press a Quick Action button, or run a
   slash command (see [Workflows and commands](workflows.md)).

## Requirements

- Windows 10 or newer
- .NET 10 Desktop Runtime
- An installed CAM system

## Updates

No manual steps: CAM Agent checks for a new version, downloads it, and restarts itself.
