# Concurrency-Limiter

Concurrency-Limiter is a python decorator to limit the number of concurrent executor in asyncio.gather

### Demonstration:

```python

```

## Table of Contents

- [ReAttempt](#ReAttempt)
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
from reattempt import reattempt
import asyncio
import random

# List of flowers for our examples
flowers = ["Rose", "Tulip", "Sunflower", "Daisy", "Lily"]

# Synchronous function example
@reattempt
def plant_flower():
    flower = random.choice(flowers)
    print(f"Attempting to plant a {flower}")
    if random.random() < 0.8:  # 80% chance of failure
        raise Exception(f"The {flower} didn't take root")
    return f"{flower} planted successfully"

# Synchronous generator example
@reattempt
def grow_flowers():
    for _ in range(3):
        flower = random.choice(flowers)
        print(f"Growing {flower}")
        yield flower
    if random.random() < 0.5:  # 50% chance of failure at the end
        raise Exception("The garden needs more fertilizer")

# Asynchronous function example
@reattempt
async def water_flower():
    flower = random.choice(flowers)
    print(f"Watering the {flower}")
    await asyncio.sleep(0.1)  # Simulating watering time
    if random.random() < 0.6:  # 60% chance of failure
        raise Exception(f"The {flower} needs more water")
    return f"{flower} is well-watered"

# Asynchronous generator function example
@reattempt
async def harvest_flowers():
    for _ in range(3):
        flower = random.choice(flowers)
        print(f"Harvesting {flower}")
        yield flower
        await asyncio.sleep(0.1)  # Time between harvests
    if random.random() < 0.4:  # 40% chance of failure at the end
        raise Exception("The garden needs more care")

async def tend_garden():
    # Plant a flower (sync function)
    try:
        result = plant_flower()
        print(result)
    except Exception as e:
        print(f"Planting error: {e}")

    # Grow flowers (sync generator)
    try:
        for flower in grow_flowers():
            print(f"Grown: {flower}")
    except Exception as e:
        print(f"Growing error: {e}")

    # Water a flower (async function)
    try:
        result = await water_flower()
        print(result)
    except Exception as e:
        print(f"Watering error: {e}")

    # Harvest flowers (async generator function)
    try:
        async for flower in harvest_flowers():
            print(f"Harvested: {flower}")
    except Exception as e:
        print(f"Harvesting error: {e}")

if __name__ == "__main__":
    asyncio.run(tend_garden())
```


## License

ReAttempt is released under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For questions, suggestions, or issues related to ReAttempt, please open an issue on the GitHub repository.

