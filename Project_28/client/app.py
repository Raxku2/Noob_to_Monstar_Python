import asyncio
import websockets
import os
import time

SERVER_URL = "ws://13.235.2.136:8000/receiver"

async def handle_connection():
    """Connect to the server and handle incoming file transfers."""
    async with websockets.connect(SERVER_URL, max_size=None) as conn:
        print(f"[+] Connected to {SERVER_URL}")
        current_file = None
        file_handle = None

        try:
            while True:
                msg = await conn.recv()

                if isinstance(msg, str):
                    if msg.startswith("START:"):
                        file_name = msg.split("START:")[1]
                        safe_name = os.path.basename(file_name)
                        save_path = f"rcv_{safe_name}"
                        file_handle = open(save_path, "wb")
                        current_file = save_path
                        print(f"[↓] Receiving file: {safe_name}")

                    elif msg == "END":
                        if file_handle:
                            file_handle.close()
                            print(f"[✓] File saved as {current_file}")
                            file_handle = None
                            current_file = None

                elif isinstance(msg, bytes):
                    if file_handle:
                        file_handle.write(msg)

        except websockets.ConnectionClosed:
            print("[!] Connection lost — will retry in 5 seconds.")
            raise  # re-raise so outer loop restarts

        finally:
            if file_handle:
                file_handle.close()

async def keep_alive_receiver():
    """Automatically reconnect if disconnected."""
    while True:
        try:
            await handle_connection()
        except Exception as e:
            print(f"[x] Disconnected ({e}). Retrying...")
            await asyncio.sleep(5)  # wait before reconnecting

if __name__ == "__main__":
    print("[*] Receiver started — waiting for files...")
    try:
        asyncio.run(keep_alive_receiver())
    except KeyboardInterrupt:
        print("\n[✗] Receiver stopped manually.")
