# Interaction scenarios

The Add-in components are involved in four scenarios, which fall into two groups:

- **Add-in life cycle** — [installation](install-addon.md) and [uninstallation](uninstall-addon.md); these are managed by the Add-in Manager (`AddinManager.dll`), which calls the Translator.
- **Transferring geometry to the CAM system** — [by pressing the Toolbar button](import-from-cad.md) in an open CAD model, and [importing a CAD file on request from the CAM system](import-cad-file.md).

Each scenario involves its own set of components and connections (shown in the diagrams below). The CAD system does not directly "know" about the CAM system — the connection is provided by the Toolbar and the Translator (`<Translator>.exe`).

- **[Installing the Add-in](install-addon.md)** — the Add-in Manager calls the Translator to embed the Toolbar into the CAD system.
- **[Uninstalling the Add-in](uninstall-addon.md)** — the Add-in Manager calls the Translator to remove the Toolbar from the CAD system.
- **[Import from the CAD system into the CAM system](import-from-cad.md)** — the user exports the open model by pressing the Toolbar button.
- **[Import of a CAD file into the CAM system](import-cad-file.md)** — the CAM system imports a CAD file by calling the Translator on an already loaded model.
