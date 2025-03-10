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

# Create backend .env file if it doesn't exist
if (-not (Test-Path -Path ".\backend\.env")) {
    Write-Host "Creating backend/.env file from template..." -ForegroundColor Yellow
    
    # Create a basic template for the backend .env file
    @"
# AutoGen Planner Backend Environment Variables

# Application settings
AUTOGEN_APP_NAME=AutoGen Planner
AUTOGEN_API_PREFIX=/api/v1
AUTOGEN_DEBUG=False

# API keys
AUTOGEN_GEMINI_API_KEY=your_gemini_api_key_here
"@ | Out-File -FilePath ".\backend\.env" -Encoding utf8
    
    Write-Host "Please edit the backend/.env file to add your API keys." -ForegroundColor Yellow
}

# Create frontend .env file if it doesn't exist
if (-not (Test-Path -Path ".\frontend\.env")) {
    Write-Host "Creating frontend/.env file from template..." -ForegroundColor Yellow
    
    # Create a basic template for the frontend .env file
    @"
# AutoGen Planner Frontend Environment Variables

# API settings
AUTOGEN_API_URL=http://localhost:8000/api/v1

# UI settings
AUTOGEN_PORT=7860
AUTOGEN_SHARE=False
"@ | Out-File -FilePath ".\frontend\.env" -Encoding utf8
    
    Write-Host "Please edit the frontend/.env file if needed." -ForegroundColor Yellow
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