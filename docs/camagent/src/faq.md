# FAQ

**Something went wrong.**
Click **Report a bug** in the CAM Agent menu — a bug report with logs is sent automatically.

**Where are the logs?**
`%TEMP%\CamAgent3Logs\` — the current session log plus a `_history` folder with previous
sessions.

**How do I update?**
No manual steps — CAM Agent checks for a new version, downloads it, and restarts itself.

**How do I switch the provider or model?**
Use the provider and model selectors in the toolbar. API keys are entered once per provider
and validated before saving.

**How do I reset the chat?**
Type `/clear` or restart CAM Agent.

**How do I recognize part features?**
Type `/feature` or click the Feature recognition button — it appears when a STEP file is
selected.

**How do I machine a part automatically?**
Type `/yolo` — from model to NC program with minimal interaction. For a step-by-step guided
workflow, type `/wizard`.

**Can the assistant reorder or delete an operation?**
Yes — ask it to move an operation after another one, make it the first, or delete it. Before
deleting, the assistant names the operation and waits for your confirmation: a deletion cannot
be undone from the chat, and once the project is saved the only way back is building the
operation again. Reordering does not recalculate toolpaths — ask for a recalculation when the
new order changes what a later operation machines.
