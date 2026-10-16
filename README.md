# ENCY CAM-Dokumentation

Deutsches Benutzerhandbuch, Version **3.1.13**.
Maschinell übersetzt.

- [Inhaltsverzeichnis](index.md)
- [HTML-Dokumentation](https://docs.encycam.com/ENCY/3/de/index.html)
- [PDF-Handbuch](https://docs.encycam.com/ENCY/pdf/ENCY3manual-de.pdf)
- [Markdown-Verzeichnis](llms.txt)
- [Version und Sprache](doc-profile.json)

Die Branch CAM/de/v3 enthält den aktuellen Dokumentationsstand.

## Lokal erstellen und ansehen

Das Skript `build.ps1` erstellt die HTML-Dokumentation mit DocFX
im Ordner `_site` und startet eine lokale Vorschau unter
<http://127.0.0.1:8000/index.html>. Der Browser wird automatisch geöffnet;
die Vorschau wird mit Strg+C beendet.

Ist `docfx` nicht im PATH vorhanden, installiert das Skript DocFX 2.78.2
beim ersten Aufruf mit `dotnet tool install` in den Ordner `.tools/docfx`
des Repositorys. Eine globale Installation ist nicht erforderlich.

Voraussetzungen:

- .NET SDK 8 oder neuer (<https://dotnet.microsoft.com/download>);
- Internetzugang zu nuget.org für die erste Installation von DocFX;
- Windows PowerShell 5.1 oder PowerShell 7 (unter Linux und macOS: `pwsh`).

Aufruf im Stammordner des Repositorys:

```powershell
./build.ps1
./build.ps1 -Port 8080      # anderer Port
./build.ps1 -NoBrowser      # Browser nicht öffnen
./build.ps1 -NoServe        # nur erstellen, ohne Vorschau
```

Falls Windows die Ausführung von Skripten blockiert:
`powershell -ExecutionPolicy Bypass -File build.ps1`.
