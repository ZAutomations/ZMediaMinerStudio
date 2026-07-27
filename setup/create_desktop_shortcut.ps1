<#
    create_desktop_shortcut.ps1  —  MediaMiner Studio
    Creates a Desktop + Start-menu shortcut with the colourful app icon.
    Safe to re-run any time.
#>

$ErrorActionPreference = 'Stop'

$SetupDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoDir  = Split-Path -Parent $SetupDir
$Target   = Join-Path $RepoDir 'run.bat'
$IconPath = Join-Path $RepoDir 'assets\app_icon.ico'
$Name     = 'MediaMiner Studio'

if (-not (Test-Path $Target)) {
    Write-Host "  [ERROR] run.bat not found at $Target" -ForegroundColor Red
    exit 1
}
if (-not (Test-Path $IconPath)) {
    $py = Join-Path $RepoDir 'venv\Scripts\python.exe'
    $mk = Join-Path $SetupDir 'make_icon.py'
    if ((Test-Path $py) -and (Test-Path $mk)) {
        try { & $py $mk | Out-Null } catch {}
    }
}

function New-AppShortcut([string]$LinkPath) {
    $shell = New-Object -ComObject WScript.Shell
    $sc = $shell.CreateShortcut($LinkPath)
    $sc.TargetPath       = $Target
    $sc.WorkingDirectory = $RepoDir
    $sc.Description      = 'MediaMiner Studio - Download, OCR, Transcribe & AI Scripts'
    $sc.WindowStyle      = 1
    if (Test-Path $IconPath) { $sc.IconLocation = "$IconPath,0" }
    $sc.Save()
    Write-Host "  [OK] $LinkPath" -ForegroundColor Green
}

$Desktop  = [Environment]::GetFolderPath('Desktop')
New-AppShortcut (Join-Path $Desktop "$Name.lnk")

$Programs = [Environment]::GetFolderPath('Programs')
if ($Programs -and (Test-Path $Programs)) {
    New-AppShortcut (Join-Path $Programs "$Name.lnk")
}

Write-Host ""
Write-Host "  Desktop icon created. Look for '$Name' on your Desktop." -ForegroundColor Cyan
