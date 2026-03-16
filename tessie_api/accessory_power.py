import aiohttp
from typing import Any, Dict
from .tessie_wrapper import tessieRequest


async def enable_keep_accessory_power_mode(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    max_attempts: int = 3,
    wait_for_completion: bool = True,
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "POST",
        f"/{vin}/command/enable_keep_accessory_power_mode",
        api_key,
        params={
            "max_attempts": max_attempts,
            "wait_for_completion": str(wait_for_completion).lower(),
        },
    )


async def disable_keep_accessory_power_mode(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    max_attempts: int = 3,
    wait_for_completion: bool = True,
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "POST",
        f"/{vin}/command/disable_keep_accessory_power_mode",
        api_key,
        params={
            "max_attempts": max_attempts,
            "wait_for_completion": str(wait_for_completion).lower(),
        },
    )
