from ast import Dict
from typing import Any
from .tessie_wrapper import tessieRequest


async def get_historical_states(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")


async def get_last_idle_state(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")


async def get_consumption_since_charge(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")
