
from fastapi import FastAPI, WebSocket
from routers import devices, incidents, properties

app = FastAPI(title="ZNOC API")

app.include_router(properties.router, prefix="/api/properties")
app.include_router(devices.router, prefix="/api/devices")
app.include_router(incidents.router, prefix="/api/incidents")

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    await ws.send_json({
        "event": "SYSTEM_CONNECTED",
        "message": "ZNOC realtime channel active"
    })

    while True:
        await ws.receive_text()
