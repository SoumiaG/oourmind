# System Architecture

oourmind.io is built with a decoupled FastAPI backend and a Three.js-based frontend.

## Data Flow

1. **User Query**: The user enters a prompt via the frontend `QueryInput`.
2. **Backend Submission**: The frontend POSTs the query to the FastAPI backend.
3. **Mistral API Connection**: The backend `extractor.py` calls the Mistral AI streaming API.
4. **Token-Level Processing**: For each token:
   - Metadata (logprobs, entropy, etc.) is extracted.
   - `scorer.py` evaluates the token against three persona profiles (Architect, Oracle, Shadow).
   - A `ThoughtData` packet is constructed.
5. **SSE Stream**: The backend streams each `ThoughtData` packet via Server-Sent Events (SSE).
6. **3D Visualization**: The frontend `stream.js` client consumes the SSE stream.
7. **Spatial Mapping**: `scene.js` updates the Three.js zones (Blue Grid, Gold Nebula, Dark Core) based on the `intensity` values.
8. **Camera Control**: The camera shifts to the zone of the `dominant_persona`.
9. **HUD Update**: The HUD reflects live scores and token history.

## Components

### Backend
- `main.py`: App initialization and routing.
- `extractor.py`: Mistral API interface.
- `scorer.py`: Decision engine for persona scoring.
- `api/stream.py`: SSE implementation.

### Frontend
- `scene.js`: Three.js scene manager.
- `zones/`: Shader-based 3D visualizations for each persona.
- `stream.js`: SSE consumer.
- `components/`: UI/HUD elements.
