@echo off
setlocal EnableDelayedExpansion

echo TikTok Automation - Open App
echo -------------------------
set /p DEVICE_ID="Enter your device ID: "

echo.
echo Connecting to device %DEVICE_ID%...
curl -X POST http://localhost:8000/api/connect -H "Content-Type: application/json" -d "{\"device_id\": \"%DEVICE_ID%\"}"

echo.
echo Opening TikTok...
curl -X POST http://localhost:8000/api/task -H "Content-Type: application/json" -d "{\"action\": \"open_app\"}"

echo.
echo Done! Press any key to exit...
pause > nul 