import aiohttp
from typing import Any, Dict
from .tessie_wrapper import tessieRequest


async def flash_lights(session: aiohttp.ClientSession, vin: str, api_key: str) -> Dict[str, Any]:
    return await tessieRequest(session, "GET", f"/{vin}/PATH", api_key)
