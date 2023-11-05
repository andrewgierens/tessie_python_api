from ast import Dict
from typing import Any
from .tessie_wrapper import tessieRequest


async def get_drives(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")


async def get_driving_path(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")


async def set_tag(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")
