# Documentazione ENCY CAM

Manuale utente in italiano, versione **3.1.13**.
Tradotto automaticamente.

- [Indice](index.md)
- [Documentazione HTML](https://docs.encycam.com/ENCY/3/it/index.html)
- [Manuale PDF](https://docs.encycam.com/ENCY/pdf/ENCY3manual-it.pdf)
- [Indice Markdown](llms.txt)
- [Versione e lingua](doc-profile.json)

Il branch CAM/it/v3 contiene lo stato attuale della documentazione.

## Generare e visualizzare in locale

Lo script `build.ps1` genera la documentazione HTML con DocFX
nella cartella `_site` e avvia un'anteprima locale all'indirizzo
<http://127.0.0.1:8000/index.html>. Il browser si apre automaticamente;
per terminare l'anteprima premere Ctrl+C.

Se `docfx` non è presente nel PATH, al primo avvio lo script installa
DocFX 2.78.2 con `dotnet tool install` nella cartella `.tools/docfx`
del repository. Non è necessaria un'installazione globale.

Requisiti:

- .NET SDK 8 o successivo (<https://dotnet.microsoft.com/download>);
- accesso a Internet a nuget.org per la prima installazione di DocFX;
- Windows PowerShell 5.1 o PowerShell 7 (su Linux e macOS: `pwsh`).

Esecuzione dalla cartella principale del repository:

```powershell
./build.ps1
./build.ps1 -Port 8080      # porta diversa
./build.ps1 -NoBrowser      # non aprire il browser
./build.ps1 -NoServe        # solo generazione, senza anteprima
```

Se Windows blocca l'esecuzione degli script:
`powershell -ExecutionPolicy Bypass -File build.ps1`.
