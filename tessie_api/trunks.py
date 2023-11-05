from ast import Dict
from typing import Any
from .tessie_wrapper import tessieRequest


async def open_front_trunk(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")


async def open_close_rear_trunk(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")
