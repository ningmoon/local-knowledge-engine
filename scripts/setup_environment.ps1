<#
.SYNOPSIS
Creates a project-local virtual environment and installs pinned Python dependencies.

.DESCRIPTION
This script does not install Python, FFmpeg, GPU drivers, or change system PATH.
Install those prerequisites first as documented in docs/Environment_Setup.md.
#>
[CmdletBinding()]
param(
    [string]$PythonExecutable = "python",
    [string]$VenvPath = ".venv",
    [ValidateSet("cpu", "cuda")]
    [string]$Runtime = "cpu"
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$VenvFullPath = Join-Path $ProjectRoot $VenvPath
$VenvPython = Join-Path $VenvFullPath "Scripts\python.exe"

if (-not (Test-Path $VenvPython)) {
    Write-Host "Creating virtual environment: $VenvFullPath"
    & $PythonExecutable -m venv $VenvFullPath
}

Write-Host "Installing Local Knowledge Engine ($Runtime runtime)..."
& $VenvPython -m pip install --upgrade pip
$RequirementsFile = Join-Path $ProjectRoot "requirements-$Runtime.txt"
& $VenvPython -m pip install -r $RequirementsFile
& $VenvPython -m pip install -e $ProjectRoot

Write-Host "Verifying environment..."
& $VenvPython -m local_knowledge_engine.cli check
if ($LASTEXITCODE -ne 0) {
    throw "Environment verification failed with exit code $LASTEXITCODE"
}
