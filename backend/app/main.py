from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import devices, incidents, assignments, properties, dashboard

app = FastAPI(title="ZNOC Backend")

# CORS middleware configured specifically for your project URLs
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000", 
        "https://z-noc.vercel.app"  # Your exact Vercel production domain
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Existing routers
app.include_router(devices.router)
app.include_router(incidents.router)
app.include_router(assignments.router)
app.include_router(properties.router)
app.include_router(dashboard.router)

@app.get("/health")
async def health():
    return {"status": "healthy"}
