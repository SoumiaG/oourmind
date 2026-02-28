import json
from uuid import uuid4
from fastapi import APIRouter, Header, Request
from fastapi.responses import StreamingResponse
from backend.extractor import stream_mistral_query
from backend.models import QueryRequest

router = APIRouter()

@router.post("/think/stream")
async def stream_thought(request_body: QueryRequest):
    """SSE Streaming Endpoint."""
    query_id = str(uuid4())
    query = request_body.query

    async def event_generator():
        # Using a blocking generator here with a simple loop to stream to client
        # In a fully production system, this could be async/await but MistralClient
        # is synchronous so we bridge it.
        for data in stream_mistral_query(query, query_id):
            # Format to SSE "data: <json>\n\n"
            json_data = data.model_dump_json()
            yield f"data: {json_data}\n\n"

        # End of stream indicator
        yield "data: [DONE]\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")
