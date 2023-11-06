import aiohttp
from typing import Any, Dict

import pytz

from tessie_api.literals import DistanceFormat, Format, TemperatureFormat
from .tessie_wrapper import tessieRequest


async def get_historical_states(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    fromUnix: int,
    toUnix: int,
    interval: int,
    condensed: bool = False,
    timezone: str = "UTC",
    distance_format: DistanceFormat = "km",
    temperature_format: TemperatureFormat = "c",
    format: Format = "json",
) -> Dict[str, Any]:
    if timezone not in pytz.all_timezones:
        raise ValueError(
            "Invalid timezone. Please sure the passed value is a valid IANA timezone."
        )

    return await tessieRequest(
        session,
        "GET",
        f"/{vin}/states",
        api_key,
        params={
            "from": fromUnix,
            "to": toUnix,
            "interval": interval,
            "condense": str(condensed).lower(),
            "timezone": timezone,
            "distance_format": distance_format,
            "temperature_format": temperature_format,
            "format": format,
        },
    )


async def get_last_idle_state(
    session: aiohttp.ClientSession, vin: str, api_key: str
) -> Dict[str, Any]:
    return await tessieRequest(session, "GET", f"/{vin}/last_idle_state", api_key)


async def get_consumption_since_charge(
    session: aiohttp.ClientSession, vin: str, api_key: str
) -> Dict[str, Any]:
    return await tessieRequest(
        session, "GET", f"/{vin}/consumption_since_charge", api_key
    )
