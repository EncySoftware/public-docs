# ENCY Hyper documentation

English user manual, version **1.0.1**.

- [Manual contents](src/index.md)
- [HTML documentation](https://docs.encycam.com/HYPER/1/en/index.html)
- [PDF manual](https://docs.encycam.com/HYPER/pdf/1/en/manual.pdf)
- [Markdown index](llms.txt)
- [Version and language](doc-profile.json)
- [Translation contribution guide](TRANSLATING.md)

The Hyper/en/v1 branch contains the current documentation snapshot.

## Build and preview locally

The `build.ps1` script builds the HTML documentation with DocFX
in the `_site` folder and starts a local preview at
<http://127.0.0.1:8000/src/index.html>. The browser opens automatically;
press Ctrl+C to stop the preview.

If `docfx` is not in PATH, the script installs DocFX 2.78.2
on its first run using `dotnet tool install` into the repository's
`.tools/docfx` folder. A global installation is not required.

Requirements:

- .NET SDK 8 or later (<https://dotnet.microsoft.com/download>);
- Internet access to nuget.org for the first DocFX installation;
- Windows PowerShell 5.1 or PowerShell 7 (on Linux and macOS: `pwsh`).

Run from the repository root:

```powershell
./build.ps1
./build.ps1 -Port 8080      # use a different port
./build.ps1 -NoBrowser      # do not open the browser
./build.ps1 -NoServe        # build without starting the preview
```

If Windows blocks script execution:
`powershell -ExecutionPolicy Bypass -File build.ps1`.
