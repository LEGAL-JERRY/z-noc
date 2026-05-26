from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import devices, incidents, assignments, properties, dashboard

app = FastAPI(title="ZNOC Backend")

# 1. CRITICAL: Allow your Vercel frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000", 
        "https://your-vercel-project-name.vercel.app" # Make sure to replace this with your real Vercel URL!
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
