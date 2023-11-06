import os
from dotenv import load_dotenv
import aiohttp
import pytest

from tessie_api import get_state_of_all_vehicles

@pytest.mark.asyncio
async def test_can_get_vehicles():
    load_dotenv()  # take environment variables from .env.
    async with aiohttp.ClientSession() as session:  # ClientSession is created here and will be closed when exiting the block
        data = await get_state_of_all_vehicles(session=session, api_key=os.getenv("TESSIE_KEY"), only_active=True)
        vin_to_check = os.getenv("TESLA_VIN")
        assert any(result["vin"] == vin_to_check for result in data["results"])
