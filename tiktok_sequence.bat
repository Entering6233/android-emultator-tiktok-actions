@echo off
setlocal EnableDelayedExpansion

echo TikTok Draft Sequence
echo -------------------------
set /p DEVICE_ID="Enter your device ID: "

echo.
echo 1. Connecting to device %DEVICE_ID%...
curl -X POST http://localhost:8000/api/connect -H "Content-Type: application/json" -d "{\"device_id\": \"%DEVICE_ID%\"}"

echo.
echo 2. Opening TikTok app...
curl -X POST http://localhost:8000/api/task -H "Content-Type: application/json" -d "{\"action\": \"open_app\"}"

echo.
echo Waiting for app to load (13 seconds)...
timeout /t 13 /nobreak > nul

echo.
echo 3. Clicking profile button (972, 1868)...
curl -X POST http://localhost:8000/api/task -H "Content-Type: application/json" -d "{\"action\": \"click_location\", \"parameters\": {\"x\": 972, \"y\": 1868}}"

echo.
echo Waiting for profile to load (8 seconds)...
timeout /t 8 /nobreak > nul

echo.
echo 4. Clicking draft button (149, 1000)...
curl -X POST http://localhost:8000/api/task -H "Content-Type: application/json" -d "{\"action\": \"click_location\", \"parameters\": {\"x\": 149, \"y\": 1000}}"

echo.
echo Waiting for drafts to load (8 seconds)...
timeout /t 8 /nobreak > nul

echo.
echo 5. Clicking first draft (150, 404)...
curl -X POST http://localhost:8000/api/task -H "Content-Type: application/json" -d "{\"action\": \"click_location\", \"parameters\": {\"x\": 150, \"y\": 404}}"

echo.
echo Waiting for draft to load (8 seconds)...
timeout /t 8 /nobreak > nul

echo.
echo 6. Clicking next button (751, 1868)...
curl -X POST http://localhost:8000/api/task -H "Content-Type: application/json" -d "{\"action\": \"click_location\", \"parameters\": {\"x\": 751, \"y\": 1868}}"

echo.
echo Waiting for next screen to load (5 seconds)...
timeout /t 5 /nobreak > nul

echo.
echo 7. Clicking post button (751, 1868)...
curl -X POST http://localhost:8000/api/task -H "Content-Type: application/json" -d "{\"action\": \"click_location\", \"parameters\": {\"x\": 751, \"y\": 1868}}"

echo.
echo Sequence completed! Press any key to exit...
pause > nul 