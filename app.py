from fastapi import FastAPI
from src.api.routes import router
import uvicorn

app = FastAPI(
    title="TikTok Automation API",
    description="API for automating TikTok tasks using uiautomator2",
    version="1.0.0"
)

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True) 