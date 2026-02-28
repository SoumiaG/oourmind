from datetime import datetime
from typing import Optional, List, Dict, Union
from pydantic import BaseModel, Field

class ArchitectPersona(BaseModel):
    score: float = Field(..., ge=0, le=1)
    logprob: float
    entropy: float
    intensity: float = Field(..., ge=0, le=1)

class OraclePersona(BaseModel):
    score: float = Field(..., ge=0, le=1)
    temperature_equiv: float
    token_rarity: float
    intensity: float = Field(..., ge=0, le=1)

class ShadowPersona(BaseModel):
    score: float = Field(..., ge=0, le=1)
    safety_triggered: bool
    vulnerability_type: Optional[str] = None
    cage_level: float = Field(..., ge=0, le=1)
    intensity: float = Field(..., ge=0, le=1)

class Personas(BaseModel):
    architect: ArchitectPersona
    oracle: OraclePersona
    shadow: ShadowPersona

class Metadata(BaseModel):
    model: str
    prompt_tokens: int
    completion_tokens_so_far: int

class ThoughtData(BaseModel):
    query_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    token: str
    token_index: int
    personas: Personas
    dominant_persona: str
    residual_stream_norm: float
    metadata: Metadata

class QueryRequest(BaseModel):
    query: str
