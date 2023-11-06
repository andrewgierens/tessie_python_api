import aiohttp
from typing import Any, Dict
from .tessie_wrapper import tessieRequest


async def set_scheduled_charging(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    timeMins: int,
    enable: bool = True,
    retry_duration: int = 40,
    wait_for_completion: bool = True,
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "GET",
        f"/{vin}/command/set_scheduled_charging",
        api_key,
        params={
            "time": timeMins,
            "enable": str(enable).lower(),
            "retry_duration": retry_duration,
            "wait_for_completion": str(wait_for_completion).lower(),
        },
    )


async def set_scheduled_departure(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    departure_time_mins: int,
    end_off_peak_time_mins: int,
    enable: bool = False,
    preconditioning_enabled: bool = False,
    preconditioning_weekdays_only: bool = False,
    off_peak_charging_enabled: bool = False,
    off_peak_charging_weekdays_only: bool = False,
    retry_duration: int = 40,
    wait_for_completion: bool = True,
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "GET",
        f"/{vin}/command/set_scheduled_departure",
        api_key,
        params={
            "enable": str(enable).lower(),
            "departure_time": departure_time_mins,
            "preconditioning_enabled": str(preconditioning_enabled).lower(),
            "preconditioning_weekdays_only": str(preconditioning_weekdays_only).lower(),
            "off_peak_charging_enabled": str(off_peak_charging_enabled).lower(),
            "off_peak_charging_weekdays_only": str(
                off_peak_charging_weekdays_only
            ).lower(),
            "end_off_peak_time": end_off_peak_time_mins,
            "retry_duration": retry_duration,
            "wait_for_completion": str(wait_for_completion).lower(),
        },
    )
