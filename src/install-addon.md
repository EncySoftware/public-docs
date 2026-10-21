# Installing the Add-in

![Installing the Add-in](images/install.svg)

1. The user opens the Add-in wizard in the CAM system. 
2. The Add-in wizard scans the standard folder and shows a list of the Add-ins found.
3. The user selects the desired Add-in. 
4. The Add-in wizard calls `<Translator>.exe IsInstalled`. If the return code is not `10` (False), the `Apply` button is disabled.
5. The user selects the `Enable` checkbox and clicks the `Apply` button. 
6. The Add-in wizard calls `<Translator>.exe Install`. 
7. The Translator installs the Toolbar into the CAD system. If the return code is not `10` (False), an error message is shown to the user.
