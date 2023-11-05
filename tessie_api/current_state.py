import aiohttp
from typing import Any, Dict
from .tessie_wrapper import tessieRequest


async def get_state(session: aiohttp.ClientSession, vin: str, api_key: str) -> Dict[str, Any]:
    return await tessieRequest(session, "GET", f"/{vin}/state", api_key)


async def get_state_of_all_vehicles(session: aiohttp.ClientSession, vin: str, api_key: str) -> Dict[str, Any]:
    return await tessieRequest(session, "GET", f"/{vin}/PATH", api_key)


async def get_location(session: aiohttp.ClientSession, vin: str, api_key: str) -> Dict[str, Any]:
    return await tessieRequest(session, "GET", f"/{vin}/PATH", api_key)


async def get_weather(session: aiohttp.ClientSession, vin: str, api_key: str) -> Dict[str, Any]:
    return await tessieRequest(session, "GET", f"/{vin}/PATH", api_key)


async def get_map(session: aiohttp.ClientSession, vin: str, api_key: str) -> Dict[str, Any]:
    return await tessieRequest(session, "GET", f"/{vin}/PATH", api_key)
