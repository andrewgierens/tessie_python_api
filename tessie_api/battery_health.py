import aiohttp
from typing import Any, Dict

from .literals import DistanceFormat
from .tessie_wrapper import tessieRequest


async def get_battery_health(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    from_time: int = None,
    to_time: int = None,
    distance_format: DistanceFormat = "km",
) -> Dict[str, Any]:
    params = {
        k: v
        for k, v in {
            "from": from_time,
            "to": to_time,
            "distance_format": distance_format,
        }.items()
        if v is not None
    }
    return await tessieRequest(
        session, "GET", f"/{vin}/battery_health", api_key, params=params
    )
