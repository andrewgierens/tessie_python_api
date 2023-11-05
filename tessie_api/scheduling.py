import aiohttp
from typing import Any, Dict
from .tessie_wrapper import tessieRequest


async def set_scheduled_charging(session: aiohttp.ClientSession, vin: str, api_key: str) -> Dict[str, Any]:
    return await tessieRequest(session, "GET", f"/{vin}/PATH", api_key)


async def set_scheduled_departure(session: aiohttp.ClientSession, vin: str, api_key: str) -> Dict[str, Any]:
    return await tessieRequest(session, "GET", f"/{vin}/PATH", api_key)
