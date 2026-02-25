import time
import asyncio
async def async_function():
    print("Starting the async function.")
    await asyncio.sleep(2)  # wait for 2 seconds to simulate a time-consuming task
    print("This is an async function.")
    print("It executes asynchronously.")
asyncio.run(async_function())
print("program finished")