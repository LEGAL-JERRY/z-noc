
from fastapi import FastAPI
from app.api.routes import devices, incidents, assignments, properties, dashboard

app = FastAPI(title="ZNOC Backend")

app.include_router(devices.router)
app.include_router(incidents.router)
app.include_router(assignments.router)
app.include_router(properties.router)
app.include_router(dashboard.router)

@app.get("/health")
async def health():
    return {"status": "healthy"}
