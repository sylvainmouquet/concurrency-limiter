import asyncio
import pytest
from concurrency_limiter import concurrency_limiter
from loguru import logger

import logging

logging.basicConfig()
logging.getLogger("concurrency-limiter").setLevel(logging.DEBUG)


@pytest.mark.asyncio
async def test_concurrency_limiter():
    @concurrency_limiter(max_concurrent=5)
    async def fetch_data(id):
        logger.info(f"Fetch data: {id}")
        fetch_data.calls += 1  # type:ignore
        await asyncio.sleep(1)

    fetch_data.calls = 0  # type:ignore
    await asyncio.gather(*(fetch_data(i) for i in range(10)))
    assert fetch_data.calls == 10  # type:ignore
