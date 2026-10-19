# Documentação ENCY CAM

Manual do usuário em português do Brasil, versão **3.1.13**.
Tradução automática.

- [Sumário](index.md)
- [Documentação HTML](https://docs.encycam.com/ENCY/3/pt-br/index.html)
- [Manual em PDF](https://docs.encycam.com/ENCY/pdf/ENCY3manual-pt-br.pdf)
- [Índice Markdown](llms.txt)
- [Versão e idioma](doc-profile.json)

A branch CAM/pt-br/v3 contém o estado atual da documentação.

## Gerar e visualizar localmente

O script `build.ps1` gera a documentação HTML com o DocFX
na pasta `_site` e inicia uma visualização local no endereço
<http://127.0.0.1:8000/index.html>. O navegador é aberto automaticamente;
para encerrar a visualização, pressione Ctrl+C.

Se o `docfx` não estiver no PATH, na primeira execução o script instala
o DocFX 2.78.2 com `dotnet tool install` na pasta `.tools/docfx`
do repositório. Não é necessária uma instalação global.

Requisitos:

- .NET SDK 8 ou posterior (<https://dotnet.microsoft.com/download>);
- acesso à internet ao nuget.org para a primeira instalação do DocFX;
- Windows PowerShell 5.1 ou PowerShell 7 (no Linux e no macOS: `pwsh`).

Execução a partir da pasta raiz do repositório:

```powershell
./build.ps1
./build.ps1 -Port 8080      # outra porta
./build.ps1 -NoBrowser      # não abrir o navegador
./build.ps1 -NoServe        # somente gerar, sem visualização
```

Se o Windows bloquear a execução de scripts:
`powershell -ExecutionPolicy Bypass -File build.ps1`.
