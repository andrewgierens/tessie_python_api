import aiohttp
from typing import Any, Dict

from tessie_api.literals import DistanceFormat, Format
from .tessie_wrapper import tessieRequest


async def get_idles(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    fromUnix: str,
    toUnix: str,
    origin_latitude: str,
    origin_longitude: str,
    origin_radius: str,
    distance_format: DistanceFormat = "km",
    format: Format = "json",
    timezone: str = "UTC",
    exclude_origin: str = False,
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "GET",
        f"/{vin}/idles",
        api_key,
        params={
            "distance_format": distance_format,
            "format": format,
            "timezone": timezone,
            "from": fromUnix,
            "to": toUnix,
            "origin_latitude": origin_latitude,
            "origin_longitude": origin_longitude,
            "origin_radius": origin_radius,
            "exclude_origin": exclude_origin,
        },
    )
