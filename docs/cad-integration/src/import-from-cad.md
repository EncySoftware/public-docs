# Import from a CAD system into a CAM system

![Import from a CAD system into a CAM system](images/export-to-cam.svg)

1. The user works in the CAD system, creating or opening a model.
2. The user clicks the Toolbar button (which was added when the Add-in was installed).
3. The Toolbar saves the file in the CAD system's native format (for a new file — the "Save As…" dialog; if it is cancelled, the process is aborted).
4. The Toolbar converts the geometry into one of the CAM system's internal formats (into SGF for direct import, or into any other supported format) as a temporary file.
5. The Toolbar launches the CAM system with command-line parameters (see [Toolbar](toolbar-plugin.md)).
6. The CAM system opens, imports the passed file, and deletes the temporary file.
