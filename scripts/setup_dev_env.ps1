# PowerShell script to set up the development environment for AutoGen Planner

# Stop on error
$ErrorActionPreference = "Stop"

# Display banner
Write-Host "============================================"
Write-Host "  AutoGen Planner - Development Setup  "
Write-Host "============================================"
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version
    Write-Host "Found Python: $pythonVersion" -ForegroundColor Green
}
catch {
    Write-Host "Error: Python not found. Please install Python 3.8 or higher." -ForegroundColor Red
    exit 1
}

# Create .env file if it doesn't exist
if (-not (Test-Path -Path ".\.env")) {
    Write-Host "Creating .env file from template..." -ForegroundColor Yellow
    Copy-Item -Path ".\.env.example" -Destination ".\.env"
    Write-Host "Please edit the .env file to add your API keys." -ForegroundColor Yellow
}

# Create virtual environments
Write-Host "Setting up backend environment..." -ForegroundColor Cyan
if (-not (Test-Path -Path ".\backend\venv")) {
    python -m venv backend\venv
}
& .\backend\venv\Scripts\Activate.ps1
pip install -e .\backend
deactivate

Write-Host "Setting up frontend environment..." -ForegroundColor Cyan
if (-not (Test-Path -Path ".\frontend\venv")) {
    python -m venv frontend\venv
}
& .\frontend\venv\Scripts\Activate.ps1
pip install -r .\frontend\requirements.txt
deactivate

# Display success message
Write-Host ""
Write-Host "Development environment setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "To activate the environments:"
Write-Host "- Backend: .\backend\venv\Scripts\Activate.ps1"
Write-Host "- Frontend: .\frontend\venv\Scripts\Activate.ps1"
Write-Host ""
Write-Host "To run the application:"
Write-Host "- Use: .\scripts\run_local.ps1" 