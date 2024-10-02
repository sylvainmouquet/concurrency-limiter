# Concurrency-Limiter

Concurrency-Limiter is a python decorator to limit the number of concurrent executor in asyncio.gather

### Demonstration:

```python

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

concurrency_limiter is released under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For questions, suggestions, or issues related to concurrency_limiter, please open an issue on the GitHub repository.

