import asyncio
import aiohttp


async def async_timer(name, delay):
    await asyncio.sleep(delay)
    print(f'timer {name} is ended after {delay} sec')


async def main():
    task1 = asyncio.create_task(async_timer('one', 2))
    task2 = asyncio.create_task(async_timer('two', 1))
    task3 = asyncio.create_task(async_timer('three', 4))
    await asyncio.gather(task1, task2, task3)

asyncio.run(main())

