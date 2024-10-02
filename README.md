# Concurrency-Limiter

Concurrency-Limiter is a python decorator to limit the number of concurrent executor in asyncio.gather

### Demonstration:

```python
@pytest.mark.asyncio
async def test_concurrency_limiter():
    @concurrency_limiter(max_concurrent=5)
    async def fetch_data(id):
        logger.info(f"Fetch data: {id}")
        await asyncio.sleep(1)

    await asyncio.gather(*(fetch_data(i) for i in range(10)))

INFO     concurrency-limiter:__init__.py:61 run function: fetch_data timestamp: 2024-10-02 09:36:42.246222+00:00 <asyncio.locks.BoundedSemaphore object at 0x1026c8a50 [unlocked, value:4]>
INFO     concurrency-limiter:__init__.py:61 run function: fetch_data timestamp: 2024-10-02 09:36:42.246624+00:00 <asyncio.locks.BoundedSemaphore object at 0x1026c8a50 [unlocked, value:3]>
INFO     concurrency-limiter:__init__.py:61 run function: fetch_data timestamp: 2024-10-02 09:36:42.246735+00:00 <asyncio.locks.BoundedSemaphore object at 0x1026c8a50 [unlocked, value:2]>
INFO     concurrency-limiter:__init__.py:61 run function: fetch_data timestamp: 2024-10-02 09:36:42.246819+00:00 <asyncio.locks.BoundedSemaphore object at 0x1026c8a50 [unlocked, value:1]>
INFO     concurrency-limiter:__init__.py:61 run function: fetch_data timestamp: 2024-10-02 09:36:42.246895+00:00 <asyncio.locks.BoundedSemaphore object at 0x1026c8a50 [locked]>
INFO     concurrency-limiter:__init__.py:57 waiting function: fetch_data timestamp: 2024-10-02 09:36:42.246964+00:00 <asyncio.locks.BoundedSemaphore object at 0x1026c8a50 [locked]>
INFO     concurrency-limiter:__init__.py:57 waiting function: fetch_data timestamp: 2024-10-02 09:36:42.246996+00:00 <asyncio.locks.BoundedSemaphore object at 0x1026c8a50 [locked, waiters:1]>
INFO     concurrency-limiter:__init__.py:57 waiting function: fetch_data timestamp: 2024-10-02 09:36:42.247022+00:00 <asyncio.locks.BoundedSemaphore object at 0x1026c8a50 [locked, waiters:2]>
INFO     concurrency-limiter:__init__.py:57 waiting function: fetch_data timestamp: 2024-10-02 09:36:42.247049+00:00 <asyncio.locks.BoundedSemaphore object at 0x1026c8a50 [locked, waiters:3]>
INFO     concurrency-limiter:__init__.py:57 waiting function: fetch_data timestamp: 2024-10-02 09:36:42.247073+00:00 <asyncio.locks.BoundedSemaphore object at 0x1026c8a50 [locked, waiters:4]>
INFO     concurrency-limiter:__init__.py:61 run function: fetch_data timestamp: 2024-10-02 09:36:43.248582+00:00 <asyncio.locks.BoundedSemaphore object at 0x1026c8a50 [locked, waiters:4]>
INFO     concurrency-limiter:__init__.py:61 run function: fetch_data timestamp: 2024-10-02 09:36:43.250872+00:00 <asyncio.locks.BoundedSemaphore object at 0x1026c8a50 [locked, waiters:3]>
INFO     concurrency-limiter:__init__.py:61 run function: fetch_data timestamp: 2024-10-02 09:36:43.251272+00:00 <asyncio.locks.BoundedSemaphore object at 0x1026c8a50 [locked, waiters:2]>
INFO     concurrency-limiter:__init__.py:61 run function: fetch_data timestamp: 2024-10-02 09:36:43.251523+00:00 <asyncio.locks.BoundedSemaphore object at 0x1026c8a50 [locked, waiters:1]>
INFO     concurrency-limiter:__init__.py:61 run function: fetch_data timestamp: 2024-10-02 09:36:43.251759+00:00 <asyncio.locks.BoundedSemaphore object at 0x1026c8a50 [locked]>
PASSED  

```

## Table of Contents

- [concurrency_limiter](#concurrency_limiter)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Installation](#installation)
  - [Usage](#usage)
  - [License](#license)
  - [Contact](#contact)

## Description

Concurrency-Limiter is a Python library that provides a decorator to limit the number of concurrent executions in asyncio.gather. This ensures that your asynchronous tasks do not overwhelm system resources, allowing for better control over concurrency and improved performance in applications that rely on asynchronous operations.

## Installation

```bash
# Install the dependency
pip install concurrency-limiter
uv add concurrency-limiter
poetry add concurrency-limiter
```

## Usage

```python
from concurrency_limiter import concurrency_limiter
import asyncio
import random

# List of flowers for our examples
flowers = ["Rose", "Tulip", "Sunflower", "Daisy", "Lily"]

# Asynchronous function example to plant a flower
@concurrency_limiter(max_concurrent=3)
async def plant_flower():
    flower = random.choice(flowers)
    print(f"Attempting to plant a {flower}")
    await asyncio.sleep(0.1)  # Simulating planting time
    if random.random() < 0.8:  # 80% chance of failure
        raise Exception(f"The {flower} didn't take root")
    return f"{flower} planted successfully"

# Start of Selection
if __name__ == "__main__":
    asyncio.run(asyncio.gather(*(plant_flower() for i in range(5))))
# End of Selection
```


## License

Concurrency-Limiter is released under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For questions, suggestions, or issues related to Concurrency-Limiter, please open an issue on the GitHub repository.

