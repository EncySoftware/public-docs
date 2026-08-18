# Workflows and commands

## Task workflows

Ten composable, task-oriented workflows. Each has a slash command, a quick action button in
the chat area, and a dedicated system prompt that focuses the agent on the task.

| Command | Workflow |
|---------|----------|
| `/tutorial` | Interactive tutorial — learn CAM Agent basics step by step |
| `/setup` | Setup helper — machine, material, geometry |
| `/feature` | Feature recognition — part analysis in the built-in 3D viewer |
| `/yolo` | Full automatic pipeline from model to NC program |
| `/scan` | Review the current project |
| `/wizard` | Technology wizard — operations, simulation, NC program |
| `/check` | Troubleshooting |
| `/feeds` | Feeds and speeds — cutting parameters |
| `/tools` | Tool picker — tool library |
| `/cost` | Cycle time and cost estimate |

## System commands

| Command | Action |
|---------|--------|
| `/open` | Open a 3D model or project file |
| `/camdir` | Select the CAM system executable |
| `/index` | Scan the project structure |
| `/explain` | Describe the current configuration |
| `/clear` | Start a new conversation |

Commands are filtered by the project state: some appear only when a project is loaded or
ready.

## Keyboard shortcuts

- `Ctrl+O` — open a model
- `Ctrl+V` — paste an image from the clipboard
- `Enter` — send the message; `Shift+Enter` — new line
