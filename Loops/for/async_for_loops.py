"""
Using async for loops for asynchronous iteration.
Requires Python 3.6+ and understanding of asyncio basics.
"""

import asyncio

# An asynchronous iterable must implement __aiter__ (and optionally __anext__).
# Here we create a simple async range that yields numbers with a delay.

class AsyncRange:
    def __init__(self, start, end):
        self.data = range(start, end)

    # __aiter__ must return an asynchronous iterator.
    # We use 'async def' and 'yield' to create an asynchronous generator.
    async def __aiter__(self):
        for index in self.data:
            # Simulate some I/O-bound wait (e.g., network, file read)
            await asyncio.sleep(0.5)
            yield index

async def main():
    # The async for loop works like a regular for, but it awaits each iteration.
    # The iterable must be an asynchronous iterable.
    async for num in AsyncRange(0, 5):
        print(num)

# Run the async main function
asyncio.run(main())

# Output (with half-second pauses between numbers):
# 0
# 1
# 2
# 3
# 4

# Key points:
# - Use 'async for' only inside an async function (defined with 'async def').
# - The iterable must implement __aiter__ (and __anext__ if not a generator).
# - Asynchronous generators (like the one above) are the easiest way to create async iterables.
# - await asyncio.sleep() simulates non-blocking I/O – other tasks can run concurrently.