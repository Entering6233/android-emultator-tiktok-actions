# TikTok Automation API Documentation

A FastAPI-based automation system for TikTok using uiautomator2.

## Getting Started

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start the server:
```bash
python app.py
```

The API will be available at `http://localhost:8000`

## API Endpoints

### 1. Connect Device
Establishes connection with an Android device/emulator.

```http
POST /api/connect
```

Request body:
```json
{
    "device_id": "your_device_id",
    "app_package": "com.zhiliaoapp.musically"  // optional, defaults to TikTok
}
```

### 2. Execute/Schedule Tasks
Execute tasks immediately or schedule them for later.

```http
POST /api/task
```

Request body:
```json
{
    "action": "action_name",
    "parameters": {},  // optional, depends on action
    "schedule_time": "YYYY-MM-DD HH:MM:SS"  // optional, for scheduling
}
```

Available Actions:

#### a) Open TikTok App
```json
{
    "action": "open_app"
}
```

#### b) Like Current Video
```json
{
    "action": "like_video"
}
```

#### c) Follow User
```json
{
    "action": "follow_user"
}
```

#### d) Add Comment
```json
{
    "action": "comment",
    "parameters": {
        "text": "Your comment text"
    }
}
```

#### e) Scroll Feed
```json
{
    "action": "scroll_feed",
    "parameters": {
        "count": 5  // number of times to scroll
    }
}
```

#### f) Click at Location
```json
{
    "action": "click_location",
    "parameters": {
        "x": 972,  // x coordinate
        "y": 1868  // y coordinate
    }
}
```

Example curl command for clicking at specific location:
```bash
curl -X POST http://localhost:8000/api/task -H "Content-Type: application/json" -d "{\"action\": \"click_location\", \"parameters\": {\"x\": 972, \"y\": 1868}}"
```

### 3. Get Device Status
Returns current device and app status.

```http
GET /api/status
```

Response example:
```json
{
    "status": "success",
    "device_status": {
        "device_info": {},
        "app_running": true,
        "screen_on": true,
        "battery": {}
    }
}
```

## Scheduling Tasks

You can schedule tasks by including the `schedule_time` parameter:

```json
{
    "action": "like_video",
    "schedule_time": "2024-12-27 15:30:00"
}
```

## Batch Files

### tiktok_sequence.bat
Performs a sequence of actions:
1. Opens TikTok app
2. Scrolls feed
3. Clicks at specific location (e.g., profile button at 972, 1868)

```bash
tiktok_sequence.bat
```

## Error Handling

All endpoints return error responses in the format:
```json
{
    "detail": "Error message"
}
```

Common HTTP status codes:
- 200: Success
- 400: Bad Request (e.g., device not connected)
- 500: Internal Server Error

## Example Usage

1. Connect to device:
```bash
curl -X POST http://localhost:8000/api/connect -H "Content-Type: application/json" -d "{\"device_id\": \"your_device_id\"}"
```

2. Open TikTok and scroll 3 times:
```bash
curl -X POST http://localhost:8000/api/task -H "Content-Type: application/json" -d "{\"action\": \"open_app\"}"
curl -X POST http://localhost:8000/api/task -H "Content-Type: application/json" -d "{\"action\": \"scroll_feed\", \"parameters\": {\"count\": 3}}"
```

3. Schedule a like action:
```bash
curl -X POST http://localhost:8000/api/task -H "Content-Type: application/json" -d "{\"action\": \"like_video\", \"schedule_time\": \"2024-12-27 15:30:00\"}"
```

4. Click at specific coordinates:
```bash
curl -X POST http://localhost:8000/api/task -H "Content-Type: application/json" -d "{\"action\": \"click_location\", \"parameters\": {\"x\": 972, \"y\": 1868}}"
``` 