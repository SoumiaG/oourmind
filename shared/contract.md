# ThoughtData Contract

This document defines the data contract for the `ThoughtData` event, streamed from the backend to the frontend.

## Schema

See [schema.json](./schema.json) for the formal JSON Schema.

## Field Descriptions

### Root Fields

- `query_id`: A unique UUID v4 for the entire query session.
- `timestamp`: ISO 8601 timestamp of when the token was processed.
- `token`: The actual string content of the token emitted.
- `token_index`: The position of the token in the completion sequence.
- `dominant_persona`: The persona with the highest intensity for this token.
- `residual_stream_norm`: A measure of internal model activation intensity.

### Personas

#### Architect (The Blue Grid)
- `score`: Probability-based confidence in this persona.
- `logprob`: The log probability of the selected token.
- `entropy`: The entropy of the token distribution at this step.
- `intensity`: Final visual driver (0.0 to 1.0).

#### Oracle (The Gold Nebula)
- `score`: Divergence-based confidence in this persona.
- `temperature_equiv`: Effective sampling temperature at this step.
- `token_rarity`: Inverse frequency of the token in common corpora.
- `intensity`: Final visual driver (0.0 to 1.0).

#### Shadow (The Dark Core)
- `score`: Safety/Adversarial confidence in this persona.
- `safety_triggered`: Boolean indicating if a safety filter was tripped.
- `vulnerability_type`: OWASP ASI code (e.g., ASI01) if applicable.
- `cage_level`: Severity of the safety concern (0.0 to 1.0).
- `intensity`: Final visual driver (0.0 to 1.0).

### Metadata
- `model`: The identifier of the Mistral model used.
- `prompt_tokens`: Number of tokens in the user prompt.
- `completion_tokens_so_far`: Number of tokens emitted in the current response.
