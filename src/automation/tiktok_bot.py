import uiautomator2 as u2
import schedule
import time
from typing import Optional, Dict
import threading
from datetime import datetime

class TikTokBot:
    def __init__(self, device_id: str, app_package: str):
        """Initialize TikTok bot with device connection."""
        self.device = u2.connect(device_id)
        self.app_package = app_package
        self.scheduler_thread = None
        self.is_running = False
        self._start_scheduler()

    def _start_scheduler(self):
        """Start the scheduler in a separate thread."""
        def run_scheduler():
            self.is_running = True
            while self.is_running:
                schedule.run_pending()
                time.sleep(1)

        self.scheduler_thread = threading.Thread(target=run_scheduler)
        self.scheduler_thread.daemon = True
        self.scheduler_thread.start()

    def execute_task(self, action: str, parameters: Optional[Dict] = None) -> Dict:
        """Execute a TikTok task immediately."""
        if not self.device.info.get('screenOn'):
            self.device.screen_on()

        try:
            if action == "open_app":
                return self._open_app()
            elif action == "like_video":
                return self._like_video()
            elif action == "follow_user":
                return self._follow_user()
            elif action == "comment":
                return self._add_comment(parameters.get("text", ""))
            elif action == "scroll_feed":
                return self._scroll_feed(parameters.get("count", 1))
            elif action == "click_location":
                return self._click_location(
                    parameters.get("x", 0),  # Exact X coordinate
                    parameters.get("y", 0)   # Exact Y coordinate
                )
            else:
                raise ValueError(f"Unknown action: {action}")
        except Exception as e:
            return {"error": str(e)}

    def schedule_task(self, action: str, parameters: Optional[Dict], schedule_time: str):
        """Schedule a TikTok task for later execution."""
        try:
            schedule_datetime = datetime.strptime(schedule_time, "%Y-%m-%d %H:%M:%S")
            schedule.every().day.at(schedule_datetime.strftime("%H:%M")).do(
                self.execute_task, action, parameters
            )
        except Exception as e:
            raise Exception(f"Failed to schedule task: {str(e)}")

    def get_status(self) -> Dict:
        """Get the current status of the device and app."""
        try:
            return {
                "device_info": self.device.info,
                "app_running": self.app_package in self.device.app_list_running(),
                "screen_on": self.device.info.get('screenOn'),
                "battery": self.device.battery_info
            }
        except Exception as e:
            return {"error": str(e)}

    def _open_app(self) -> Dict:
        """Open TikTok app."""
        try:
            self.device.app_start(self.app_package)
            return {"status": "success", "message": "App opened successfully"}
        except Exception as e:
            return {"error": str(e)}

    def _like_video(self) -> Dict:
        """Like the current video."""
        try:
            like_btn = self.device(resourceId=f"{self.app_package}:id/like_button")
            if like_btn.exists:
                like_btn.click()
                return {"status": "success", "message": "Video liked"}
            return {"status": "error", "message": "Like button not found"}
        except Exception as e:
            return {"error": str(e)}

    def _follow_user(self) -> Dict:
        """Follow the current user."""
        try:
            follow_btn = self.device(resourceId=f"{self.app_package}:id/follow_button")
            if follow_btn.exists:
                follow_btn.click()
                return {"status": "success", "message": "User followed"}
            return {"status": "error", "message": "Follow button not found"}
        except Exception as e:
            return {"error": str(e)}

    def _add_comment(self, text: str) -> Dict:
        """Add a comment to the current video."""
        try:
            comment_btn = self.device(resourceId=f"{self.app_package}:id/comment_button")
            if comment_btn.exists:
                comment_btn.click()
                comment_input = self.device(resourceId=f"{self.app_package}:id/comment_input")
                if comment_input.exists:
                    comment_input.set_text(text)
                    self.device(resourceId=f"{self.app_package}:id/send_button").click()
                    return {"status": "success", "message": "Comment added"}
            return {"status": "error", "message": "Comment functionality not available"}
        except Exception as e:
            return {"error": str(e)}

    def _scroll_feed(self, count: int = 1) -> Dict:
        """Scroll through the feed."""
        try:
            for _ in range(count):
                self.device.swipe(0.5, 0.8, 0.5, 0.2)
                time.sleep(1)
            return {"status": "success", "message": f"Scrolled {count} times"}
        except Exception as e:
            return {"error": str(e)}

    def _click_location(self, x: int, y: int) -> Dict:
        """Click at exact coordinates provided."""
        try:
            # Perform the click at exact coordinates
            self.device.click(x, y)
            return {
                "status": "success", 
                "message": f"Clicked at coordinates ({x}, {y})"
            }
        except Exception as e:
            return {"error": str(e)}

    def __del__(self):
        """Cleanup when the bot is destroyed."""
        self.is_running = False
        if self.scheduler_thread:
            self.scheduler_thread.join(timeout=1) 