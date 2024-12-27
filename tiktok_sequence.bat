@echo off
setlocal EnableDelayedExpansion

echo TikTok Automation Sequence
echo -------------------------
set /p DEVICE_ID="Enter your device ID: "

echo.
echo 1. Connecting to device %DEVICE_ID%...
curl -X POST http://localhost:8000/api/connect -H "Content-Type: application/json" -d "{\"device_id\": \"%DEVICE_ID%\"}"

echo.
echo 2. Opening TikTok app...
curl -X POST http://localhost:8000/api/task -H "Content-Type: application/json" -d "{\"action\": \"open_app\"}"

echo.
echo Waiting for app to load (5 seconds)...
timeout /t 5 /nobreak > nul

echo.
echo 3. Scrolling feed 2 times...
curl -X POST http://localhost:8000/api/task -H "Content-Type: application/json" -d "{\"action\": \"scroll_feed\", \"parameters\": {\"count\": 2}}"

echo.
echo 4. Clicking profile button location (972, 1868)...
curl -X POST http://localhost:8000/api/task -H "Content-Type: application/json" -d "{\"action\": \"click_location\", \"parameters\": {\"x\": 972, \"y\": 1868}}"

echo.
echo Sequence completed! Press any key to exit...
pause > nul 