import aiohttp
from typing import Any, Dict
from .tessie_wrapper import tessieRequest


async def vent_windows(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    retry_duration: int = 40,
    wait_for_completion: bool = True,
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "GET",
        f"/{vin}/command/vent_windows",
        api_key,
        params={
            "retry_duration": retry_duration,
            "wait_for_completion": str(wait_for_completion).lower(),
        },
    )


async def close_windows(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    retry_duration: int = 40,
    wait_for_completion: bool = True,
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "GET",
        f"/{vin}/command/close_windows",
        api_key,
        params={
            "retry_duration": retry_duration,
            "wait_for_completion": str(wait_for_completion).lower(),
        },
    )
