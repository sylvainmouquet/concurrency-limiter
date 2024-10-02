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

DEBUG    concurrency-limiter:__init__.py:61 [RUNNING] func: fetch_data - <asyncio.locks.BoundedSemaphore object at 0x102778cd0 [unlocked, value:4]>
DEBUG    concurrency-limiter:__init__.py:61 [RUNNING] func: fetch_data - <asyncio.locks.BoundedSemaphore object at 0x102778cd0 [unlocked, value:3]>
DEBUG    concurrency-limiter:__init__.py:61 [RUNNING] func: fetch_data - <asyncio.locks.BoundedSemaphore object at 0x102778cd0 [unlocked, value:2]>
DEBUG    concurrency-limiter:__init__.py:61 [RUNNING] func: fetch_data - <asyncio.locks.BoundedSemaphore object at 0x102778cd0 [unlocked, value:1]>
DEBUG    concurrency-limiter:__init__.py:61 [RUNNING] func: fetch_data - <asyncio.locks.BoundedSemaphore object at 0x102778cd0 [locked]>
INFO     concurrency-limiter:__init__.py:59 [WAITING] func: fetch_data - <asyncio.locks.BoundedSemaphore object at 0x102778cd0 [locked]>
INFO     concurrency-limiter:__init__.py:59 [WAITING] func: fetch_data - <asyncio.locks.BoundedSemaphore object at 0x102778cd0 [locked, waiters:1]>
INFO     concurrency-limiter:__init__.py:59 [WAITING] func: fetch_data - <asyncio.locks.BoundedSemaphore object at 0x102778cd0 [locked, waiters:2]>
INFO     concurrency-limiter:__init__.py:59 [WAITING] func: fetch_data - <asyncio.locks.BoundedSemaphore object at 0x102778cd0 [locked, waiters:3]>
INFO     concurrency-limiter:__init__.py:59 [WAITING] func: fetch_data - <asyncio.locks.BoundedSemaphore object at 0x102778cd0 [locked, waiters:4]>
DEBUG    concurrency-limiter:__init__.py:61 [RUNNING] func: fetch_data - <asyncio.locks.BoundedSemaphore object at 0x102778cd0 [locked, waiters:4]>
DEBUG    concurrency-limiter:__init__.py:61 [RUNNING] func: fetch_data - <asyncio.locks.BoundedSemaphore object at 0x102778cd0 [locked, waiters:3]>
DEBUG    concurrency-limiter:__init__.py:61 [RUNNING] func: fetch_data - <asyncio.locks.BoundedSemaphore object at 0x102778cd0 [locked, waiters:2]>
DEBUG    concurrency-limiter:__init__.py:61 [RUNNING] func: fetch_data - <asyncio.locks.BoundedSemaphore object at 0x102778cd0 [locked, waiters:1]>
DEBUG    concurrency-limiter:__init__.py:61 [RUNNING] func: fetch_data - <asyncio.locks.BoundedSemaphore object at 0x102778cd0 [locked]>

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

