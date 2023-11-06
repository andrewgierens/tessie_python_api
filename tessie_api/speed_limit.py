import aiohttp
from typing import Any, Dict
from .tessie_wrapper import tessieRequest


async def set_speed_limit(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    mph: int,
    retry_duration: int = 40,
    wait_for_completion: bool = True,
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "GET",
        f"/{vin}/command/set_speed_limit",
        api_key,
        params={
            "mph": mph,
            "retry_duration": retry_duration,
            "wait_for_completion": str(wait_for_completion).lower(),
        },
    )


async def enable_speed_limit(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    pin: string,
    retry_duration: int = 40,
    wait_for_completion: bool = True,
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "GET",
        f"/{vin}/command/enable_speed_limit",
        api_key,
        params={
            "pin": pin,
            "retry_duration": retry_duration,
            "wait_for_completion": str(wait_for_completion).lower(),
        },
    )


async def disable_speed_limit(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    pin: str,
    retry_duration: int = 40,
    wait_for_completion: bool = True,
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "GET",
        f"/{vin}/command/disable_speed_limit",
        api_key,
        params={
            "pin": pin,
            "retry_duration": retry_duration,
            "wait_for_completion": str(wait_for_completion).lower(),
        },
    )


async def clear_speed_limit_pin(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    pin: str,
    retry_duration: int = 40,
    wait_for_completion: bool = True,
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "GET",
        f"/{vin}/command/clear_speed_limit_pin",
        api_key,
        params={
            "pin": pin,
            "retry_duration": retry_duration,
            "wait_for_completion": str(wait_for_completion).lower(),
        },
    )
