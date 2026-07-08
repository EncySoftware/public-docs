# Requirements

Before you begin developing an Add-in for the CAM system, make sure that the finished product will meet the following requirements:

1. **CAD system licensing.** The CAD-SDK files used by the Add-in must be permitted for distribution as part of the CAM system's distributive.
2. **External install/uninstall.** The Add-in must support installation and uninstallation without user interaction in the CAD system's UI — this is required for the Add-ins Wizard to work correctly.
3. **Geometry export.** The Add-in must be able to export geometry into one of the CAM system's internal formats.

**Additionally** — if the Add-in supports importing CAD files on request from the CAM system, one more requirement applies to it:

- **Programmatic import of CAD files.** The CAD system's API must allow a project file of that CAD system to be opened programmatically and converted — without interactive user involvement.

---
