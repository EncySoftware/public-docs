# Build and test locally

Try every build in a local CAM system before publishing: the store publishes the package
exactly as built.

Everything on this page is for your own development machines. Users may get the extension only
through the store: do not hand out builds, `.dext` files or feeds to them (see
[Store rules and your obligations](store-rules.md#the-store-is-the-only-channel)).

## Build

The build command and the output folder of a project made from the template are described in
the template README, section
[Local build & try-out](https://github.com/EncySoftware/ency-extension-template#local-build--try-out).
The examples in `cam-api-examples` are built by their own scripts and can also be packed into a
`.dext` file.

## Install your build

The **Extensions** tab of the CAM system opens from the Home page. Its **Manage** page lists the
installed extensions, enables and disables them, and installs extensions from files and feeds.

**Install from file….** Installs a `.nupkg` or `.dext` package, or registers a `.json` manifest
in place. You can also drag a file onto the tab.

**Register a manifest in place.** Select `<Name>.settings.json` in the build output folder.
The CAM system loads the library from that folder, so the next build is picked up without
reinstalling. This is the shortest loop while you develop.

**Add feed….** Adds a NuGet feed or a local folder with `.nupkg` and `.dext` files. Its
extensions appear on the **Store** page next to the store catalog — use it to check how your
package installs and updates.

A `.dext` file can also be installed by double-clicking it.

## Debug

1. Start the CAM system with the `/EXTENSION_DEBUG_FOLDER="<build output folder>"` argument.
   The CAM system loads the extensions from that folder in addition to the installed ones.
2. Attach the debugger to the CAM system process (**.NET Core Attach** in VS Code, **Attach to
   Process** in Visual Studio).
3. Call the extension from its place in the interface (see
   [Extension anatomy](extension-anatomy.md#entry-points)).

Debugging setups for .NET, Delphi and C++ are described in the API documentation, section
**Debugging** (see [External references](references.md)).

## Where installed extensions live

Each installed extension gets its own folder `extensions\<Name>\` in the user data folder of
the CAM system (under `%APPDATA%`). The list of registered libraries is `extensions.json` in the
same `extensions` folder.

## Restart and unloading

- An installed extension is registered, and the CAM system loads it on its own. If it does
  not appear, restart the CAM system.
- If the package has `"requiresRestart": true`, the tab asks for a restart after installation.
- A library that is still loaded cannot be replaced: the copy fails with an access error. With
  the default `unload_mode` (`umJustAfterExecution`) the library is unloaded after each run;
  with other modes, close the CAM system before installing the new build.
- If the extension does not appear where expected, check on the **Manage** page that the
  library and its entry point are enabled.
