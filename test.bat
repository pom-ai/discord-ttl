REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    pause
    exit /b 1
)

REM Requreiments installation
pip install -r requirements.txt

REM Continue with the rest of the script
python index.py