import asyncio
import pytest
from concurrency_limiter import concurrency_limiter
import random
import logging

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("concurrency-limiter").setLevel(logging.DEBUG)

# List of flowers for our examples
flowers = ["Rose", "Tulip", "Sunflower", "Daisy", "Lily"]


@concurrency_limiter(max_concurrent=3)
async def plant_flower():
    flower = random.choice(flowers)
    print(f"Attempting to plant a {flower}")
    await asyncio.sleep(0.1)  # Simulating planting time
    return f"{flower} planted successfully"


@pytest.mark.asyncio
async def test_plant_flower():
    results = await asyncio.gather(*(plant_flower() for _ in range(5)))
    assert len(results) <= 5  # Ensure we get at most 5 results
    for result in results:
        assert "planted successfully" in result
