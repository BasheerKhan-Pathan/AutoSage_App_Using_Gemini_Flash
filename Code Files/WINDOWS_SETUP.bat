@echo off
echo ================================================================================
echo                    AutoSage - Windows Quick Setup
echo ================================================================================
echo.

echo Step 1: Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)
echo Python found!
echo.

echo Step 2: Installing required packages...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install packages
    echo Try running as Administrator or check your internet connection
    pause
    exit /b 1
)
echo Packages installed successfully!
echo.

echo Step 3: Checking for .env file...
if not exist .env (
    echo Creating .env file from template...
    copy .env.example .env
    echo.
    echo IMPORTANT: Please edit .env file and add your Google API Key!
    echo Opening .env file in notepad...
    timeout /t 2 >nul
    notepad .env
    echo.
    echo After adding your API key, save and close notepad, then press any key...
    pause >nul
) else (
    echo .env file already exists
)
echo.

echo ================================================================================
echo                    Setup Complete!
echo ================================================================================
echo.
echo To start AutoSage, run: streamlit run app.py
echo Or simply double-click START_AUTOSAGE.bat
echo.
pause
