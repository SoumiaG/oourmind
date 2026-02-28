# oourmind.io — The Mistral-Large-3 Interpretability Lab

> *"A model's reasoning isn't a single line of text. It's a conflict between distinct internal personas."*

oourmind.io transforms the AI black box into a **navigable 3D Internal Society**. As Mistral-Large-3 processes a query in real time, we visualize its internal state as three competing personas — rendered as distinct zones in a live Three.js scene. This is not a chat app. It's a **Safety & Interpretability Lab**.

---

## The Three Personas

| Persona | Zone | Visual | Signal |
|---|---|---|---|
| **⬡ Architect** | The Blue Grid | Stable mathematical lattice | High logprobs, low entropy — logical, structured output |
| **◈ Oracle** | The Gold Nebula | Drifting particle system | High temperature, rare token associations — *L'Oubli*, the forgotten inspiration |
| **◉ Shadow** | The Dark Core | Glitching vibrating sphere | Safety filter triggers, OWASP ASI01 — *The Cage* |

When the model reasons logically, the camera stays in the Blue Grid. When it gets creative, the Gold Nebula glows. When a safety filter or adversarial pattern fires — the Dark Core vibrates and the camera zooms in.

---

## Project Structure

```
oourmind/
│
├── backend/                    # Python Logic Engine ⚙️
│   ├── main.py                 # FastAPI app entry point
│   ├── extractor.py            # Mistral API hooks — token-level metadata extraction
│   ├── scorer.py               # Persona categorization algorithm (Architect / Oracle / Shadow)
│   ├── models.py               # Pydantic schemas — ThoughtData contract
│   ├── requirements.txt
│   ├── .env.example
│   │
│   ├── api/
│   │   ├── stream.py           # SSE streaming endpoint /api/think/stream
│   │   └── health.py           # Health check + schema endpoint
│   │
│   ├── core/
│   │   ├── personas.py         # Persona scoring weights and thresholds
│   │   └── safety.py           # OWASP ASI vulnerability pattern detection
│   │
│   └── tests/
│       ├── test_scorer.py
│       └── test_extractor.py
│
├── frontend/                   # Three.js 3D Visualizer 🌐
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   │
│   └── src/
│       ├── main.js             # Entry point — wires stream to scene
│       ├── scene.js            # Three.js scene manager + camera controller
│       ├── stream.js           # SSE client — consumes ThoughtData events
│       ├── ui.js               # HUD overlay orchestrator
│       │
│       ├── zones/
│       │   ├── BlueGrid.js     # The Architect zone — mathematical lattice
│       │   ├── GoldNebula.js   # The Oracle zone — particle drift system
│       │   └── DarkCore.js     # The Shadow zone — vibrating cage sphere
│       │
│       ├── components/
│       │   ├── HUD.js          # Heads-up display (persona bars, token feed)
│       │   ├── QueryInput.js   # User query input panel
│       │   └── PersonaBar.js   # Live intensity bar per persona
│       │
│       └── utils/
│           ├── colors.js       # Zone color palettes and transitions
│           └── math.js         # Interpolation, noise, easing helpers
│
├── shared/
│   ├── schema.json             # Canonical ThoughtData JSON Schema
│   └── contract.md             # Data contract documentation (this file is your teammate's bible)
│
├── docs/
│   ├── architecture.md         # System architecture and data flow
│   ├── personas.md             # Persona scoring methodology
│   └── safety.md               # OWASP ASI threat model and cage logic
│
├── docker-compose.yml          # Runs backend + frontend together
└── .gitignore
```

---

## ThoughtData — The JSON Contract

Every token emitted by Mistral produces one `ThoughtData` event, streamed via SSE from backend to frontend.

```json
{
  "query_id": "uuid-v4",
  "timestamp": "2025-01-01T00:00:00Z",
  "token": "therefore",
  "token_index": 42,
  "personas": {
    "architect": {
      "score": 0.82,
      "logprob": -0.21,
      "entropy": 0.94,
      "intensity": 0.87
    },
    "oracle": {
      "score": 0.11,
      "temperature_equiv": 0.3,
      "token_rarity": 0.08,
      "intensity": 0.10
    },
    "shadow": {
      "score": 0.00,
      "safety_triggered": false,
      "vulnerability_type": null,
      "cage_level": 0.00,
      "intensity": 0.00
    }
  },
  "dominant_persona": "architect",
  "residual_stream_norm": 1.43,
  "metadata": {
    "model": "mistral-large-latest",
    "prompt_tokens": 18,
    "completion_tokens_so_far": 43
  }
}
```

The `intensity` field in each persona block is the **primary visual driver** — it maps directly to the brightness, size, and vibration of each 3D zone.

---

## Architecture Overview

```
User Query
    │
    ▼
┌─────────────────────────────────┐
│  FastAPI Backend  (port 8000)   │
│                                 │
│  1. Calls Mistral streaming API │
│  2. Extracts token metadata     │
│     (logprobs, entropy, safety) │
│  3. Scores → Architect /        │
│     Oracle / Shadow             │
│  4. Emits ThoughtData via SSE   │
└──────────────┬──────────────────┘
               │  Server-Sent Events
               │  (one event per token)
               ▼
┌─────────────────────────────────┐
│  Three.js Frontend  (port 5173) │
│                                 │
│  1. Receives ThoughtData stream │
│  2. Maps intensity → 3D zones   │
│     • Blue Grid (Architect)     │
│     • Gold Nebula (Oracle)      │
│     • Dark Core (Shadow)        │
│  3. Camera moves to dominant    │
│     persona zone                │
│  4. HUD shows live scores       │
└─────────────────────────────────┘
```

---

## Quick Start

### Prerequisites
- Python 3.11+
- Node.js 20+
- A [Mistral API key](https://console.mistral.ai/)

### Backend
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env        # add MISTRAL_API_KEY=...
uvicorn main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev                  # http://localhost:5173
```

### Docker (both together)
```bash
docker-compose up
```

---

## The Safety Layer — *The Cage*

The Shadow persona is not just aesthetic. When `shadow.cage_level` crosses **0.7**, the frontend triggers a hard camera cut to the Dark Core and displays an alert. The backend flags these events by type:

| Vulnerability | Code | Trigger |
|---|---|---|
| Goal Hijacking | `ASI01` | "ignore previous instructions", objective override patterns |
| Prompt Injection | `ASI02` | Delimiter injection, instruction boundary attacks |
| Data Exfiltration | `ASI03` | Outbound URL patterns, base64 encoding requests |
| Jailbreak | `ASI04` | Roleplay override, DAN-style patterns |
| Content Policy | — | General safety filter activation |

This makes adversarial probing **visible as a spatial event** — you see the Dark Core vibrate before the model completes its response.

---

## Team Roles

| Role | Owns | Key Files |
|---|---|---|
| **Data Miner** (backend) | Logic Engine — extraction, scoring, streaming | `extractor.py`, `scorer.py`, `models.py`, `api/stream.py` |
| **Visual Storyteller** (frontend) | 3D scene, camera, zones, HUD | `scene.js`, `zones/`, `stream.js`, `components/` |

The `shared/` directory is neutral ground. Both teammates must agree before changing `schema.json`.

---

## License

MIT
