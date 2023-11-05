from ast import Dict
from typing import Any
from .tessie_wrapper import tessieRequest


async def honk(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")
