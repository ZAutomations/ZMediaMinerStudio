@echo off
title MediaMiner Studio
cd /d "%~dp0"

REM -- Force UTF-8 mode (fixes ASCII encoding on Windows) --
set PYTHONUTF8=1

REM -- Check venv exists, if not show setup instructions --
if not exist "%~dp0venv_light\Scripts\python.exe" (
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

"%~dp0venv_light\Scripts\python.exe" "%~dp0main.py"

if errorlevel 1 (
    echo.
    echo ============================================================
    echo   The app exited with an ERROR (code %errorlevel%).
    echo   Copy the messages above and send them for help.
    echo ============================================================
    pause
)
