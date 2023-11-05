from ast import Dict
from typing import Any
from .tessie_wrapper import tessieRequest


async def vent_sunroof(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")


async def close_sunroof(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")
