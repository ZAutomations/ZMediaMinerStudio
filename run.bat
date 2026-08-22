@echo off
title MediaMiner Studio
cd /d "%~dp0"

REM -- Force UTF-8 mode (fixes ASCII encoding on Windows) --
set PYTHONUTF8=1

REM -- Pick the venv: prefer venv_light (dev PC), fall back to venv (this PC) --
set "PY_EXE=%~dp0venv_light\Scripts\python.exe"
if not exist "%PY_EXE%" set "PY_EXE=%~dp0venv\Scripts\python.exe"
if not exist "%PY_EXE%" (
    echo ============================================================
    echo   First-time setup required!
    echo   Double-click:  setup\install_dependencies.bat
    echo ============================================================
    pause
    exit /b 1
)

echo Starting MediaMiner Studio...
echo (Keep this window open. If the app fails, the error appears below.)
echo.

REM -- Run the app -- errors print to this console --
"%PY_EXE%" "%~dp0main.py"

if errorlevel 1 (
    echo.
    echo ============================================================
    echo   The app exited with an ERROR (code %errorlevel%).
    echo   Copy the messages above and send them for help.
    echo ============================================================
    pause
)
