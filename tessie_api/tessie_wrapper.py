import aiohttp
from typing import Any, Dict

class TessieAPIWrapper:
    BASE_URL = 'https://api.tessie.com'

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session = aiohttp.ClientSession()

    async def close(self):
        await self.session.close()

    async def tessieRequest(self, method: str, path: str, **kwargs) -> Dict[str, Any]:
        url = f"{self.BASE_URL}{path}"
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
        }
        kwargs['headers'] = headers
        async with self.session.request(method, url, **kwargs) as response:
            response.raise_for_status()  # Will raise aiohttp.ClientResponseError on 4xx or 5xx
            return await response.json()