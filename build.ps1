<#
.SYNOPSIS
Builds the HTML documentation with DocFX and serves it locally.
DocFX is installed into .tools/docfx when it is not available in PATH.
#>
param(
    [ValidateRange(1, 65535)][int]$Port = 8000,
    [switch]$NoBrowser,
    [switch]$NoServe
)
$ErrorActionPreference = 'Stop'
$docfxVersion = '2.78.2'

function Find-LocalDocfx([string]$Path) {
    Get-ChildItem -LiteralPath $Path -File -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -in @('docfx', 'docfx.exe') } | Select-Object -First 1 -ExpandProperty FullName
}

Push-Location $PSScriptRoot
try {
    $docfx = Get-Command docfx -ErrorAction SilentlyContinue | Select-Object -First 1 -ExpandProperty Source
    if (-not $docfx) {
        $toolPath = Join-Path $PSScriptRoot '.tools/docfx'
        $docfx = Find-LocalDocfx $toolPath
        if (-not $docfx) {
            if (-not (Get-Command dotnet -ErrorAction SilentlyContinue)) {
                throw '.NET SDK 8 or later is required to install DocFX: https://dotnet.microsoft.com/download'
            }
            Write-Host "Installing DocFX $docfxVersion into $toolPath"
            & dotnet tool install docfx --version $docfxVersion --tool-path $toolPath
            if ($LASTEXITCODE -ne 0) { throw 'DocFX installation failed' }
            $docfx = Find-LocalDocfx $toolPath
            if (-not $docfx) { throw "DocFX was not found in $toolPath" }
        }
    }
    $docProfile = Get-Content -LiteralPath doc-profile.json -Raw -Encoding UTF8 | ConvertFrom-Json
    $version = '{0}.{1}.{2}' -f $docProfile.version, $docProfile.minor, $docProfile.patch
    # DocFX does not remove stale pages from the output directory.
    if (Test-Path -LiteralPath _site) { Remove-Item -LiteralPath _site -Recurse -Force }
    & $docfx build docfx.json --output _site --metadata "_documentationVersion=$version"
    if ($LASTEXITCODE -ne 0) { throw 'Documentation build failed' }
    if ($NoServe) { return }
    $serveArgs = @('serve', '_site', '--hostname', '127.0.0.1', '--port', "$Port")
    if (-not $NoBrowser) { $serveArgs += @('--open-browser', '--open-file', 'index.html') }
    & $docfx @serveArgs
    if ($LASTEXITCODE -ne 0) { throw 'Preview failed' }
} finally { Pop-Location }
