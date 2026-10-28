@echo off
REM Start worthlesstask inside the trimmed Electron window.
REM First run installs Electron into the shell folder (needs internet once).
setlocal
cd /d "%~dp0electron"

if not exist "node_modules\electron" (
  echo Installing the shell runtime, one-time...
  call npm install --no-audit --no-fund || (echo npm install failed & exit /b 1)
)

start "" /b cmd /c "npm start"
endlocal
