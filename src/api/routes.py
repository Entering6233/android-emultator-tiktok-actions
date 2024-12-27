from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from src.automation.tiktok_bot import TikTokBot

router = APIRouter()
bot = None

class DeviceConfig(BaseModel):
    device_id: str
    app_package: str = "com.zhiliaoapp.musically"

class TaskConfig(BaseModel):
    action: str
    parameters: Optional[dict] = None
    schedule_time: Optional[str] = None

@router.post("/connect")
async def connect_device(config: DeviceConfig):
    global bot
    try:
        bot = TikTokBot(config.device_id, config.app_package)
        return {"status": "success", "message": "Device connected successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/task")
async def schedule_task(task: TaskConfig):
    if not bot:
        raise HTTPException(status_code=400, detail="Device not connected")
    
    try:
        if task.schedule_time:
            # Schedule task for later execution
            bot.schedule_task(task.action, task.parameters, task.schedule_time)
            return {"status": "success", "message": f"Task scheduled for {task.schedule_time}"}
        else:
            # Execute task immediately
            result = bot.execute_task(task.action, task.parameters)
            return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/status")
async def get_status():
    if not bot:
        raise HTTPException(status_code=400, detail="Device not connected")
    
    try:
        status = bot.get_status()
        return {"status": "success", "device_status": status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 