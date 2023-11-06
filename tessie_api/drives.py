import aiohttp
from typing import Any, Dict, List

from tessie_api.literals import DistanceFormat, TemperatureFormat
from .tessie_wrapper import tessieRequest


async def get_drives(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    fromUnix: int,
    toUnix: int,
    origin_latitude: int,
    origin_lonitude: int,
    origin_radius: int,
    destination_latitude: int,
    destination_longitude: int,
    destination_radius: int,
    tag: str,
    driver_profile: str,
    minimum_distance: int,
    distance_format: DistanceFormat = "km",
    temperature_format: TemperatureFormat = "c",
    timezone: str = "UTC",
    exclude_origin: bool = False,
    exclude_destination: bool = False,
    exclude_tag: bool = False,
    exclude_driver_profile: bool = False,
    format: str = "Format",
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "GET",
        f"/{vin}/drives",
        api_key,
        params={
            "distance_format": distance_format,
            "temperature_format": temperature_format,
            "fromUnix": fromUnix,
            "toUnix": toUnix,
            "timezone": timezone,
            "origin_latitude": origin_latitude,
            "origin_lonitude": origin_lonitude,
            "origin_radius": origin_radius,
            "exclude_origin": str(exclude_origin).lower(),
            "destination_latitude": destination_latitude,
            "destination_longitude": destination_longitude,
            "destination_radius": destination_radius,
            "exclude_destination": str(exclude_destination).lower(),
            "tag": tag,
            "exclude_tag": str(exclude_tag).lower(),
            "driver_profile": driver_profile,
            "exclude_driver_profile": str(exclude_driver_profile).lower(),
            "format": format,
            "minimum_distance": minimum_distance,
        },
    )


async def get_driving_path(
    session: aiohttp.ClientSession, vin: str, api_key: str, fromUnix: int, toUnix: int
) -> Dict[str, Any]:
    return await tessieRequest(
        session, "GET", f"/{vin}/path", api_key, params={"from": fromUnix, "to": toUnix}
    )


async def set_tag(
    session: aiohttp.ClientSession, vin: str, api_key: str, drives: List[int], tag: str
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "POST",
        f"/{vin}/drives/set_tag",
        api_key,
        params={"drives": drives, "tag": tag},
    )
