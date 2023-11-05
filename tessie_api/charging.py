from ast import Dict
from typing import Any
from .tessie_wrapper import tessieRequest


async def start_charging(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")


async def stop_charging(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")


async def set_charge_limit(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")


async def set_charging_amps(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")


async def open_unlock_charge_port(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")


async def close_charge_port(self, vin: str) -> Dict[str, Any]:
    return await tessieRequest("GET", f"/PATH/{vin}")
