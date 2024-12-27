@echo off
setlocal EnableDelayedExpansion

echo TikTok Automation - Click Profile Button
echo ----------------------------------------
set /p DEVICE_ID="Enter your device ID: "

echo.
echo Connecting to device %DEVICE_ID%...
curl -X POST http://localhost:8000/api/connect -H "Content-Type: application/json" -d "{\"device_id\": \"%DEVICE_ID%\"}"

echo.
echo Clicking profile button at coordinates (972, 1868)...
curl -X POST http://localhost:8000/api/task -H "Content-Type: application/json" -d "{\"action\": \"tiktok_click_profile_button\", \"parameters\": {\"x\": 972, \"y\": 1868}}"

echo.
echo Done! Press any key to exit...
pause > nul 