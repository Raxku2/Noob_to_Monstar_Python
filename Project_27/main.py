from fastapi import  FastAPI, WebSocket,WebSocketDisconnect
# from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True,
)


@app.get('/')
def home():
    # return RedirectResponse('/docs')
    return 0
        

connections = []

@app.websocket('/msg')
async def message(websck : WebSocket):
    await websck.accept() 
    # conn = websck #<== conn 
    connections.append(websck)

    try:
        while True:
            data = await websck.receive_text()
    except WebSocketDisconnect:
        connections.remove(websck) 

@app.get('/send') 
async def send(msg: str):
    for conn in connections:
        await conn.send_text(msg)
    return {"status":"ok",'message':msg}
