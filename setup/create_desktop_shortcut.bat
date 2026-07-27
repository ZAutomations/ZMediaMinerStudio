@echo off
REM ===================================================================
REM  create_desktop_shortcut.bat  —  MediaMiner Studio
REM  Creates a desktop + Start-menu shortcut with the app icon.
REM ===================================================================
echo.
echo Creating "MediaMiner Studio" desktop shortcut ...
echo.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0create_desktop_shortcut.ps1"
if errorlevel 1 (
    echo.
    echo [WARN] Could not create the shortcut automatically.
    echo        You can right-click run.bat -^> Send to -^> Desktop instead.
)
echo.
pause
