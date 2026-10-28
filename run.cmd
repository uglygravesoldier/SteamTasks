@echo off
REM Start the worthlesstask dashboard with no console window.
REM The packaged build is preferred; without it the source tree is used.
setlocal
cd /d "%~dp0"

set "APP=%~dp0outputs\worthlesstask.exe"
if not exist "%APP%" set "APP=%~dp0dist\worthlesstask\worthlesstask.exe"
if exist "%APP%" (
  start "" "%APP%" %*
  exit /b 0
)

where pythonw >nul 2>nul
if errorlevel 1 (
  where python >nul 2>nul
  if errorlevel 1 (
    echo Neither the packaged build nor python was found.
    echo Expected the build at: %APP%
    exit /b 1
  )
  REM No windowless interpreter available: run minimized as a fallback.
  start /min "" python -m worthlesstask web --open %*
  exit /b 0
)

REM pythonw runs the panel with no console at all. Closing the browser tab
REM stops the program by itself, so there is nothing to keep open here.
start "" pythonw -m worthlesstask web --open %*
endlocal
