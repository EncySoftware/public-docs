# Uninstalling the Add-in

![Uninstalling the Add-in](../images/uninstall.svg)

1. The user opens the Add-ins Wizard in the CAM system. 
2. The Add-ins Wizard scans the standard folder and shows a list of the Add-ins found.
3. The user selects an installed Add-in. Installed Add-ins have the `Enable` checkbox checked.
4. The user clears the `Enable` checkbox and clicks the `Apply` button. 
5. The Add-ins Wizard calls `<Translator>.exe UnInstall`. 
6. The Translator removes the Toolbar from the CAD system. If the return code is not equal to `10` (False), an error message is shown to the user.
