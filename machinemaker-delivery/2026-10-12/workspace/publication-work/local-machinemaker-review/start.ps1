param([switch]$Restart)
$ErrorActionPreference = 'Stop'
$taskRoot = $PSScriptRoot
$pidFile = Join-Path $taskRoot 'server.pid'
$listener = Get-NetTCPConnection -LocalPort 8765 -State Listen -ErrorAction SilentlyContinue
if ($listener) {
    $knownPid = if (Test-Path -LiteralPath $pidFile) { [int](Get-Content -LiteralPath $pidFile) } else { 0 }
    $knownProcess = Get-CimInstance Win32_Process -Filter "ProcessId = $knownPid"
    if ($knownProcess.CommandLine -notmatch 'serve\.py.*--port.*8765' -or $listener.OwningProcess -ne $knownPid) {
        throw 'Port 8765 belongs to another process; it will not be stopped.'
    }
    if (-not $Restart) { Write-Output 'MachineMaker review is available at http://127.0.0.1:8765/'; exit 0 }
    Stop-Process -Id $knownPid
}
$pythonPath = (Get-Command python).Source
$process = Start-Process -FilePath $pythonPath -ArgumentList @('serve.py','--port','8765') -WorkingDirectory $taskRoot -WindowStyle Hidden -RedirectStandardOutput (Join-Path $taskRoot 'server.stdout.log') -RedirectStandardError (Join-Path $taskRoot 'server.stderr.log') -PassThru
Set-Content -Encoding ASCII -LiteralPath $pidFile -Value $process.Id
Write-Output ('MachineMaker review started, PID ' + $process.Id + ', http://127.0.0.1:8765/')
