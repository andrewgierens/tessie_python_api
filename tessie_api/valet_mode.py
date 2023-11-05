from ast import Dict
from typing import Any
from .tessie_wrapper import tessieRequest


async def enable_valet_mode(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")


async def disable_valet_mode(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")
