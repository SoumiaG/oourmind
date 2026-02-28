import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from backend.api.stream import router as stream_router
from backend.api.health import router as health_router

load_dotenv()

app = FastAPI(
    title="oourmind.io — The Mistral-Large-3 Interpretability Lab",
    description="Transforms the AI black box into a navigable 3D Internal Society.",
    version="1.0.0"
)

# CORS middleware for frontend to interact with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict this.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(stream_router, prefix="/api")
app.include_router(health_router, prefix="/api")

@app.get("/")
async def root():
    return {
        "message": "Welcome to oourmind.io. The backend engine is running.",
        "api_docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
