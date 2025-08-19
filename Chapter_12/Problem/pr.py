import asyncio

async def hello():
    await asyncio.sleep(1)
    print("Hello")

async def done():
    await asyncio.sleep(2)
    print("Done")

async def tasks():
    await asyncio.gather(hello(),done())

async def wait_demo():
    print("Before"); await asyncio.sleep(1); print("After")

async def ret():
    await asyncio.sleep(1); return 42

async def many():
    tasks=[hello(),done()]
    await asyncio.gather(*tasks)

async def numbers():
    for i in range(1,6):
        print(i); await asyncio.sleep(1)

async def download():
    print("Downloading..."); await asyncio.sleep(2); print("Complete")

# asyncio.run(...) to run above
