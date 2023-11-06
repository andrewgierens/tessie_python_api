import aiohttp
from typing import Any, Dict

from tessie_api.literals import DistanceFormat, Format
from .tessie_wrapper import tessieRequest


async def get_charges(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    origin_latitude: int,
    origin_longitude: int,
    origin_radius: int,
    fromUnix: int,
    toUnix: int,
    minimum_energy_added: int,
    distance_format: DistanceFormat = "km",
    format: Format = "json",
    superchargers_only: bool = False,
    exclude_origin: bool = False,
    timezone: str = "UTC",
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "GET",
        f"/{vin}/charges",
        api_key,
        params={
            "distance_format": distance_format,
            "format": format,
            "superchargers_only": str(superchargers_only).lower(),
            "origin_latitude": origin_latitude,
            "origin_longitude": origin_longitude,
            "origin_radius": origin_radius,
            "exclude_origin": str(exclude_origin).lower(),
            "timezone": timezone,
            "from": fromUnix,
            "to": toUnix,
            "minimum_energy_added": minimum_energy_added,
        },
    )


async def set_charge_cost(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    charge_id: int,
    cost: int,
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "GET",
        f"/{vin}/charges/{charge_id}/set_cost",
        api_key,
        params={"cost": cost},
    )
