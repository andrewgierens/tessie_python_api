from ast import Dict
from typing import Any
from .tessie_wrapper import tessieRequest


async def schedule_software_update(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")


async def cancel_software_update(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")
