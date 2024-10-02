__version__ = "1.1.0"
__all__ = ("__version__", "concurrency_limiter")


import asyncio
import logging

logger = logging.getLogger("concurrency-limiter")
logger.addHandler(logging.NullHandler())


def concurrency_limiter(max_concurrent: int):
    """
    Limit the number of concurrent calls to the decorated function.

    This decorator uses an asyncio semaphore to restrict the number of
    concurrent executions of the decorated function to the specified
    maximum. It logs the function name and the current UTC timestamp
    each time the function is called.

    Args:
        max_concurrent (int): The maximum number of concurrent calls
        allowed for the decorated function.

    Returns:
        callable: A decorator that limits the concurrency of the
        decorated function.

    Example:
        @concurrency_limiter(max_concurrent=3)
        async def fetch_data(id):
            await asyncio.sleep(1)  # Simulate an I/O operation
            return f"Data for {id}"

        async def main():
            results = await asyncio.gather(*(fetch_data(i) for i in range(10)))
            print(results)

        # To run the example, you would typically call:
        # asyncio.run(main())
    """

    semaphore = asyncio.BoundedSemaphore(max_concurrent)

    def _concurrency_limiter(func):
        """
        The actual decorator that wraps the function with concurrency
        limiting logic.

        Args:
            func (callable): The function to be decorated.

        Returns:
            callable: The wrapped function with concurrency control.
        """

        async def wrapper(*args, **kwargs):
            if semaphore.locked():  # Check if the semaphore is activated
                logger.info(f"[WAITING] func: {func.__name__} - {semaphore}")
            async with semaphore:
                logger.debug(f"[RUNNING] func: {func.__name__} - {semaphore}")
                return await func(*args, **kwargs)

        return wrapper

    return _concurrency_limiter
