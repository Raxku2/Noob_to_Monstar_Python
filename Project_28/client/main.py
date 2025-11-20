import asyncio
import websockets
import os

SERVER_URL = "ws://13.235.2.136:8000/sender"

async def send_file(file_path):
    file_name = os.path.basename(file_path)

    async with websockets.connect(SERVER_URL, max_size=None) as conn:
        await conn.send(file_name)
        print(f"[+] Sending file: {file_name}")

        with open(file_path, "rb") as file:
            while chunk := file.read(4096):
                await conn.send(chunk)

        await conn.send(b"__end__")
        res = await conn.recv()
        print("[Server] =>", res)

if __name__ == "__main__":
    path = input("Enter file path: ").replace("'","").strip()
    if os.path.exists(path):
        asyncio.run(send_file(path))
    else:
        print("File not found.")
