@echo off
cd /D %~dp0

echo.
echo Generate offline documentation script
echo Dotnet SDK should be installed to make it work

echo.
echo Trying to update docfx tool
CALL dotnet tool update -g docfx

echo.
echo Generating documentation
CALL docfx build docfx.json

echo.
echo Starting brouwser with documentation
start file://%~dp0_site/index.html

pause

EXIT /B 0
