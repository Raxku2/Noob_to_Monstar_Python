# Chapter 12: Async & Await

- async defines coroutine
- await pauses until result

```python
import asyncio
async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")
asyncio.run(main())
```
