@echo off
REM Build the HTML site for this documentation unit -> out\html\index.html
REM Requires: .NET SDK, docfx (dotnet tool install -g docfx) and Python 3.
cd /D "%~dp0.."
CALL dotnet tool update -g docfx
python "%~dp0..\..\_common\build.py" "%~dp0.." html --open
pause
