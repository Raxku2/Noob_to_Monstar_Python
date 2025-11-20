from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

app = FastAPI()

clients: List[WebSocket] = []

@app.websocket("/receiver")
async def receiver_socket(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    print(f"[+] Receiver connected ({len(clients)} total)")

    try:
        while True:
            await websocket.receive_text()  # keep-alive or dummy wait
    except WebSocketDisconnect:
        clients.remove(websocket)
        print(f"[-] Receiver disconnected ({len(clients)} total)")


@app.websocket("/sender")
async def sender_socket(websocket: WebSocket):
    await websocket.accept()
    file_name = await websocket.receive_text()
    print(f"[Sender] Incoming file: {file_name}")

    # Notify receivers
    for client in clients:
        await client.send_text(f"START:{file_name}")

    while True:
        message = await websocket.receive()
        data = message.get("bytes")
        if data:
            if data == b"__end__":
                for client in clients:
                    await client.send_text("END")
                print(f"[Sender] File transfer completed: {file_name}")
                await websocket.send_text("File transfer successful")
                break
            for client in clients:
                await client.send_bytes(data)
