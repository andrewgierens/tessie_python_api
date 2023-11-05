from ast import Dict
from typing import Any
from .tessie_wrapper import tessieRequest


async def set_scheduled_charging(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")


async def set_scheduled_departure(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")
