@echo off
REM Build the PDF for this documentation unit -> out\pdf\CAM-postprocessing-dotnet.pdf
REM Requires: .NET SDK, docfx (dotnet tool install -g docfx), Node.js and Python 3.
cd /D "%~dp0.."
CALL dotnet tool update -g docfx
python "%~dp0..\..\..\_common\build.py" "%~dp0.." pdf --name CAM-postprocessing-dotnet.pdf
pause
