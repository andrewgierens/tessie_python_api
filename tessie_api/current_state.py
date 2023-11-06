import aiohttp
from typing import Any, Dict

from tessie_api.literals import MapStyle
from .tessie_wrapper import tessieRequest


async def get_state(
    session: aiohttp.ClientSession, vin: str, api_key: str, use_cache: bool = True
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "GET",
        f"/{vin}/state",
        api_key,
        params={"use_cache": str(use_cache).lower()},
    )


async def get_state_of_all_vehicles(
    session: aiohttp.ClientSession, api_key: str, only_active: bool = True
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "GET",
        f"/vehicles",
        api_key,
        params={"only_active": str(only_active).lower()},
    )


async def get_location(
    session: aiohttp.ClientSession, vin: str, api_key: str
) -> Dict[str, Any]:
    return await tessieRequest(session, "GET", f"/{vin}/location", api_key)


async def get_weather(
    session: aiohttp.ClientSession, vin: str, api_key: str
) -> Dict[str, Any]:
    return await tessieRequest(session, "GET", f"/{vin}/weather", api_key)


async def get_map(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    width: int = 300,
    height: int = 300,
    zoom: int = 13,
    marker_size: int = 75,
    style: MapStyle = "light",
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "GET",
        f"/{vin}/map",
        api_key,
        params={
            "width": width,
            "heigth": height,
            "zoom": zoom,
            "marker_size": marker_size,
            "style": style,
        },
    )
