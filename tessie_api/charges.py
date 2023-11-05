from ast import Dict
from typing import Any
from .tessie_wrapper import tessieRequest


async def get_charges(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")


async def set_charge_cost(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")
