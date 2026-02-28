from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class HealthStatus(BaseModel):
    status: str
    version: str

@router.get("/health")
async def health():
    return HealthStatus(status="healthy", version="1.0.0")

@router.get("/schema")
async def schema():
    # Return schema metadata or link to shared schema
    return {"schema_uri": "/shared/schema.json"}
