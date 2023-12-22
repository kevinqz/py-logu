import httpx

class HTTPRequest:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    async def _send_request(self, method, endpoint, payload=None):
        async with httpx.AsyncClient() as client:
            url = f"{self.base_url}/{endpoint}/"
            response = await client.request(method, url, headers=self.headers, json=payload)
            response.raise_for_status()
            return response.json()
