$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Runtime.WindowsRuntime
[Windows.Storage.StorageFile, Windows.Storage, ContentType = WindowsRuntime] | Out-Null
[Windows.Storage.Streams.IRandomAccessStream, Windows.Storage.Streams, ContentType = WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics.Imaging, ContentType = WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.SoftwareBitmap, Windows.Graphics.Imaging, ContentType = WindowsRuntime] | Out-Null
[Windows.Media.Ocr.OcrEngine, Windows.Foundation, ContentType = WindowsRuntime] | Out-Null
[Windows.Media.Ocr.OcrResult, Windows.Foundation, ContentType = WindowsRuntime] | Out-Null
[Windows.Globalization.Language, Windows.Globalization, ContentType = WindowsRuntime] | Out-Null
$asTask = [System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object { $_.Name -eq 'AsTask' -and $_.IsGenericMethod -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' } | Select-Object -First 1
function Await-WinRT($operation, [Type]$resultType) {
    $task = $asTask.MakeGenericMethod($resultType).Invoke($null, @($operation))
    $task.Wait()
    $task.Result
}
$language = New-Object Windows.Globalization.Language('en-US')
$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage($language)
$report = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'text-report.json') -Encoding UTF8 -Raw | ConvertFrom-Json
$results = [System.Collections.Generic.List[object]]::new()
$errors = [System.Collections.Generic.List[object]]::new()
$count = 0
foreach ($item in $report.ocr_inputs) {
    try {
        $file = Await-WinRT ([Windows.Storage.StorageFile]::GetFileFromPathAsync($item.input)) ([Windows.Storage.StorageFile])
        $stream = Await-WinRT ($file.OpenAsync([Windows.Storage.FileAccessMode]::Read)) ([Windows.Storage.Streams.IRandomAccessStream])
        try {
            $decoder = Await-WinRT ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
            $bitmap = Await-WinRT ($decoder.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
            try {
                $ocr = Await-WinRT ($engine.RecognizeAsync($bitmap)) ([Windows.Media.Ocr.OcrResult])
                $results.Add([PSCustomObject]@{ image = $item.image; frame = $item.frame; articles = $item.articles; text = $ocr.Text; brand_match = [bool]($ocr.Text -match 'sprut[\s_-]*cam|\u0441\u043f\u0440\u0443\u0442[\s_-]*\u043a\u0430\u043c'); sprut_match = [bool]($ocr.Text -match 'sprut|\u0441\u043f\u0440\u0443\u0442') })
            } finally { $bitmap.Dispose() }
        } finally { $stream.Dispose() }
    } catch {
        $errors.Add([PSCustomObject]@{ image = $item.image; frame = $item.frame; error = $_.Exception.Message })
    }
    $count++
    if ($count % 50 -eq 0) { Write-Output "OCR $count / $($report.ocr_inputs.Count)" }
}
$output = [PSCustomObject]@{ checked_frames = $results.Count; errors = @($errors.ToArray()); findings = @($results.ToArray() | Where-Object { $_.brand_match -or $_.sprut_match }); results = $results.ToArray() }
$output | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $PSScriptRoot 'ocr-report.json') -Encoding UTF8
[PSCustomObject]@{ checked_frames = $results.Count; errors = $errors.Count; findings = $output.findings.Count } | ConvertTo-Json
