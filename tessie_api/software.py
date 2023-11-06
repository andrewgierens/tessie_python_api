import aiohttp
from typing import Any, Dict
from .tessie_wrapper import tessieRequest


async def schedule_software_update(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    in_seconds: int,
    retry_duration: int = 40,
    wait_for_completion: bool = True,
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "GET",
        f"/{vin}/command/schedule_software_update",
        api_key,
        params={
            "in_seconds": in_seconds,
            "retry_duration": retry_duration,
            "wait_for_completion": str(wait_for_completion).lower(),
        },
    )


async def cancel_software_update(
    session: aiohttp.ClientSession,
    vin: str,
    api_key: str,
    retry_duration: int = 40,
    wait_for_completion: bool = True,
) -> Dict[str, Any]:
    return await tessieRequest(
        session,
        "GET",
        f"/{vin}/command/cancel_software_update",
        api_key,
        params={
            "retry_duration": retry_duration,
            "wait_for_completion": str(wait_for_completion).lower(),
        },
    )
