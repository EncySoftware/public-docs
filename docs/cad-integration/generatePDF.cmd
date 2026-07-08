@echo off
cd /D %~dp0

echo.
echo Generate offline PDF documentation script
echo Dotnet SDK and Node.js should be installed to make it work

echo.
echo Trying to update docfx tool
CALL dotnet tool update -g docfx

echo.
echo Generating documentation
CALL docfx build pdf_docfx.json

echo.
echo Generating PDF
CALL docfx pdf pdf_docfx.json

echo.
echo Copying result to section root
COPY /Y _pdf\pdf\toc.pdf "CAM-CAD-integration.pdf" >nul
echo Done. Review file: CAM-CAD-integration.pdf

pause

EXIT /B 0
