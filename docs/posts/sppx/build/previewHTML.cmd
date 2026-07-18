@echo off
REM Preview the HTML site over HTTP so full-text search works
REM (browsers block search when pages are opened as local file:// files).
REM Requires: .NET SDK, docfx (dotnet tool install -g docfx) and Python 3.
cd /D "%~dp0.."
CALL dotnet tool update -g docfx
python "%~dp0../../../_common/build.py" "%~dp0.." serve
pause
