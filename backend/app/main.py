from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import devices, incidents, assignments, properties, dashboard

app = FastAPI(title="ZNOC Backend")

# 1. CRITICAL: Allow your Vercel frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000", 
        "https://your-vercel-project-name.vercel.app" # REPLACE THIS with your actual Vercel domain
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

# 2. NEW FALLBACK ENDPOINT: Serves data to the frontend polling loop
@app.get("/api/ws-fallback")
async def ws_fallback():
    try:
        # Instead of duplicating DB connection code here, we call the exact 
        # same function your dashboard uses to gather state data.
        #
        # Open your 'app/api/routes/dashboard.py' or 'devices.py' to see 
        # what function compiles your dashboard metrics or node lists.
        
        # Example dummy structure matching what your frontend UI expects:
        mock_data = {
            "status": "active",
            "message": "Polling operational core state",
            "devices": [] 
        }
        
        return mock_data
        
    except Exception as e:
        return {"error": str(e)}, 500
