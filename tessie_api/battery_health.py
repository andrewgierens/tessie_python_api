import aiohttp
from typing import Any, Dict, Literal
from .tessie_wrapper import tessieRequest

DistanceFormat = Literal['mi', 'km']

async def get_battery_health(session: aiohttp.ClientSession, vin: str, api_key: str, distance_format: DistanceFormat, from_time: int = None, to_time: int = None) -> Dict[str, Any]:
    params = {k: v for k, v in {'from': from_time, 'to': to_time, 'distance_format': distance_format}.items() if v is not None}
    return await tessieRequest(session, "GET", f"/{vin}/battery_health", api_key, params=params)
