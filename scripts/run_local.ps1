# PowerShell script to run the AutoGen Planner application locally

# Stop on error
$ErrorActionPreference = "Stop"

# Display banner
Write-Host "====================================="
Write-Host "  AutoGen Planner - Local Launcher  "
Write-Host "====================================="
Write-Host ""

# Check if .env file exists
if (-not (Test-Path -Path ".\.env")) {
    Write-Host "Error: .env file not found. Please create one based on .env.example." -ForegroundColor Red
    exit 1
}

# Start backend in a new PowerShell window
Write-Host "Starting backend server..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd $PWD\backend; python -m src.autogen_planner.main"

# Wait for backend to start
Write-Host "Waiting for backend to start..." -ForegroundColor Yellow
Start-Sleep -Seconds 5

# Start frontend in a new PowerShell window
Write-Host "Starting frontend application..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd $PWD\frontend; python -m src.gradio_app.app"

# Display success message
Write-Host ""
Write-Host "AutoGen Planner is running!" -ForegroundColor Green
Write-Host "- Backend: http://localhost:8000"
Write-Host "- Frontend: http://localhost:7860"
Write-Host ""
Write-Host "Press Ctrl+C in the respective windows to stop the servers." 