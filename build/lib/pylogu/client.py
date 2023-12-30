import asyncio
from threading import Thread
from .http import HTTPRequest
from .core.config import config

class Logu(HTTPRequest):
    def __init__(self, key, project, channel=None):
        self.project = project
        self.channel = channel
        base_url = config.LOGU_API_BASE_URL
        headers = {
            'Content-Type': 'application/json',
            'Authorization': key
        }
        super().__init__(base_url, headers)

    def _run_in_thread(self, loop, coro):
        """
        Run the given coroutine in a new thread and schedule it on the given loop.
        """
        asyncio.set_event_loop(loop)
        loop.run_until_complete(coro)
        loop.close()

    def run_async(self, coro):
        """
        Run the coroutine in a new background thread using a new event loop.
        """
        new_loop = asyncio.new_event_loop()
        t = Thread(target=self._run_in_thread, args=(new_loop, coro))
        t.start()
        t.join()

    def log(self, event, icon, project=None, channel=None):
        project = project if project else self.project
        channel = channel if channel else self.channel
        self.run_async(self._log(project, event, icon, channel))

    async def _log(self, project, event, icon, channel):
        payload = {"project": project, "event": event, "icon": icon, "channel": channel}
        return await self._send_request("POST", "log", payload)

    def identify(self, user_id, properties, project=None):
        project = project if project else self.project
        return self.run_async(self._identify(project, user_id, properties))

    async def _identify(self, project, user_id, properties):
        payload = {"project": project, "user_id": user_id, "properties": properties}
        return await self._send_request("POST", "identify", payload)

    def insight(self, insight, icon, value, project=None, channel=None):
        project = project if project else self.project
        channel = channel if channel else self.channel
        return self.run_async(self._insight(project, insight, icon, value, channel))

    async def _insight(self, project, insight, icon, value, channel):
        payload = {"project": project, "insight": insight, "icon": icon, "value": value, "channel": channel}
        return await self._send_request("POST", "insight", payload)
