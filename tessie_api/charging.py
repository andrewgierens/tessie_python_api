import aiohttp
from typing import Any, Dict
from .tessie_wrapper import tessieRequest


async def start_charging(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    retry_duration: int = 40,
    wait_for_completion: bool = True,
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "GET",
        f"/{vin}/command/start_charging",
        api_key,
        params={
            "retry_duration": retry_duration,
            "wait_for_completion": str(wait_for_completion).lower(),
        },
    )


async def stop_charging(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    retry_duration: int = 40,
    wait_for_completion: bool = True,
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "GET",
        f"/{vin}/command/stop_charging",
        api_key,
        params={
            "retry_duration": retry_duration,
            "wait_for_completion": str(wait_for_completion).lower(),
        },
    )


async def set_charge_limit(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    percent: int,
    retry_duration: int = 40,
    wait_for_completion: bool = True,
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "GET",
        f"/{vin}/command/set_charge_limit",
        api_key,
        params={
            "percent": percent,
            "retry_duration": retry_duration,
            "wait_for_completion": str(wait_for_completion).lower(),
        },
    )


async def set_charging_amps(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    amps: int,
    retry_duration: int = 40,
    wait_for_completion: bool = True,
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "GET",
        f"/{vin}/command/set_charging_amps",
        api_key,
        params={
            "amps": amps,
            "retry_duration": retry_duration,
            "wait_for_completion": str(wait_for_completion).lower(),
        },
    )


async def open_unlock_charge_port(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    retry_duration: int = 40,
    wait_for_completion: bool = True,
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "GET",
        f"/{vin}/command/open_charge_port",
        api_key,
        params={
            "retry_duration": retry_duration,
            "wait_for_completion": str(wait_for_completion).lower(),
        },
    )


async def close_charge_port(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    retry_duration: int = 40,
    wait_for_completion: bool = True,
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "GET",
        f"/{vin}/command/close_charge_port",
        api_key,
        params={
            "retry_duration": retry_duration,
            "wait_for_completion": str(wait_for_completion).lower(),
        },
    )
