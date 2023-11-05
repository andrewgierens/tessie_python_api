from ast import Dict
from typing import Any
from .tessie_wrapper import tessieRequest


async def get_state(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")


async def get_state_of_all_vehicles(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")


async def get_location(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")


async def get_weather(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")


async def get_map(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")
