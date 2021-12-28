import aiohttp
import asyncio
import pytest

from homework10.main import get_usd_rate_from_cbr


@pytest.mark.asyncio
async def test_get_usd_rate_from_cbr():
    """TESTS UNDER CONSTRUCTION"""
    async with aiohttp.ClientSession() as session:
        assert isinstance(await get_usd_rate_from_cbr(session), float)


loop = asyncio.get_event_loop()
loop.run_until_complete(test_get_usd_rate_from_cbr())
