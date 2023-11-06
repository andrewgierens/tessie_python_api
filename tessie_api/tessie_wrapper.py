import aiohttp
from typing import Any, Dict, Optional


async def tessieRequest(
    session: aiohttp.ClientSession,
    method: str,
    path: str,
    api_key: str,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    url = f"https://api.tessie.com{path}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    async with session.request(method, url, headers=headers, params=params) as response:
        response.raise_for_status()  # Will raise aiohttp.ClientResponseError on 4xx or 5xx
        return await response.json()
