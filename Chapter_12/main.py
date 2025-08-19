import asyncio

async def greet():
    print("Start")
    await asyncio.sleep(2)
    print("End")

asyncio.run(greet())
