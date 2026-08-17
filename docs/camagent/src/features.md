# Features

- **CAM tools** — calculation, simulation, operation management, geometry, tools, NC code,
  coordinate systems, and more. Full list — [Agent tools](mcp-tools.md).
- **Semantic search** across the CAM system documentation — the agent finds relevant
  documentation sections by the meaning of a query, not just keywords.
- **Feature recognition** — a built-in 3D viewer that classifies STEP file faces into 48
  machining feature types (holes, pockets, slots, steps, chamfers, gears, grooves, and
  others). A CAD/CAM toggle in the legend switches between design and machining views; the
  CAM mode groups faces by machining type with parameters. Results are passed to the agent.
- **Task workflows** — 10 composable task-oriented workflows, each with a slash command, a
  quick action button, and a dedicated system prompt
  (see [Workflows and commands](workflows.md)).
- **MRR / tool life** — productivity vs tool life trade-off calculation.
- **Cycle time** — per-operation cycle time and machining cost estimation.
- **STL analysis** — geometric metrics and mesh quality checks.
- **Machining result comparison** — the simulation result against the target model: residual
  volume, maximum and average stock, gouges, surface coverage.
- **AI skills** — download and use ready-made skills from the server, or save your own.
- **Voice input** — real-time dictation with instant language switching from the toolbar.
- **Image attachments** — screen region screenshots, clipboard paste (Ctrl+V), file
  attachments.
- **3D scene analysis** — the agent autonomously takes viewport screenshots of the CAM system
  from different angles, analyzes geometry, checks toolpaths and simulation results.
- **Interactive tutorial** — step-by-step onboarding via the `/tutorial` command.
- **Multiple AI providers** — Claude (OAuth or API key), OpenAI, Qwen, Gemini, DeepSeek, and
  CAM GPT. Provider and model selection from the toolbar; API keys are validated before
  saving.
- **Conversation history** — long conversations are compressed automatically, and the archive
  is searchable by meaning.
- **Work modes** — Agent / Plan, with extended thinking support.
- **Effort level** — Low / Medium / High / Max from the toolbar, remembered per model.
- **CAM system status** — a connection indicator in the title bar; click it to set the path
  to the CAM system executable.
- **Auto-update** — the assistant checks for new versions and updates automatically.
