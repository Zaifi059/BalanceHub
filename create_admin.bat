@echo off
echo ========================================
echo Accounts Management System
echo Super User Creation
echo ========================================
echo.

echo Choose an option:
echo 1. Quick Super User (digizone/digizone@00001)
echo 2. Interactive Super User Creation
echo 3. Full User Management
echo 4. Exit
echo.

set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    echo.
    echo Creating quick super user...
    python quick_superuser.py
    pause
) else if "%choice%"=="2" (
    echo.
    echo Starting interactive super user creation...
    python create_superuser.py
    pause
) else if "%choice%"=="3" (
    echo.
    echo Starting user management system...
    python user_management.py
    pause
) else if "%choice%"=="4" (
    echo Goodbye!
    exit
) else (
    echo Invalid choice! Please try again.
    pause
    goto :eof
)
