@echo off
cd /D %~dp0

echo.
echo Generate offline PDF for the .NET postprocessors documentation
echo Dotnet SDK should be installed to make it work

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
echo Renaming output
COPY /Y _pdf\pdf\toc.pdf "_pdf\Postprocessing-dotnet.pdf" >nul

echo.
echo Done. Review file: _pdf\Postprocessing-dotnet.pdf
pause

EXIT /B 0
