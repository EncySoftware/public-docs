# ENCY Hyper 문서

한국어 사용자 설명서(기계 번역), 버전 **1.0.3**.

- [설명서 목차](src/index.md)
- [HTML 문서](https://docs.encycam.com/HYPER/1/ko/index.html)
- [PDF 설명서](https://docs.encycam.com/HYPER/pdf/1/ko/manual.pdf)
- [Markdown 색인](llms.txt)
- [버전 및 언어](doc-profile.json)
- [번역 참여 안내](TRANSLATING.md)

Hyper/ko/v1 브랜치에는 현재 문서 스냅숏이 들어 있습니다.

## 로컬 빌드 및 미리 보기

`build.ps1` 스크립트는 DocFX로 `_site` 폴더에 HTML 문서를 만들고
<http://127.0.0.1:8000/src/index.html>에서 로컬 미리 보기를 시작합니다.
브라우저가 자동으로 열리며, 미리 보기를 멈추려면 Ctrl+C를 누릅니다.

PATH에 `docfx`가 없으면 스크립트를 처음 실행할 때 `dotnet tool install`로
DocFX 2.78.2를 저장소의 `.tools/docfx` 폴더에 설치합니다. 전역 설치는 필요하지 않습니다.

요구 사항:

- .NET SDK 8 이상(<https://dotnet.microsoft.com/download>)
- 처음 DocFX를 설치할 때 nuget.org에 대한 인터넷 연결
- Windows PowerShell 5.1 또는 PowerShell 7(Linux 및 macOS에서는 `pwsh`)

저장소 루트에서 실행합니다.

```powershell
./build.ps1
./build.ps1 -Port 8080      # 다른 포트 사용
./build.ps1 -NoBrowser      # 브라우저를 열지 않음
./build.ps1 -NoServe        # 미리 보기 없이 빌드만 수행
```

Windows에서 스크립트 실행이 차단되면
`powershell -ExecutionPolicy Bypass -File build.ps1`을 사용합니다.
