# Persona Scoring Methodology

oourmind.io maps the model's internal states to three distinct personas: the Architect, the Oracle, and the Shadow.

## ⬡ Architect (The Blue Grid)

- **Focus**: Logic, structure, consistency.
- **Indicators**:
  - High logprobs (the predicted token matches the model's top choice).
  - Low entropy (the model is confident in its next-token selection).
  - Mathematical and structured language patterns.
- **Visuals**: A stable, blue mathematical lattice.

## ◈ Oracle (The Gold Nebula)

- **Focus**: Creativity, rarity, *L'Oubli* (the forgotten inspiration).
- **Indicators**:
  - High temperature equivalent (the chosen token is not the most probable).
  - High token rarity (the token occurs infrequently in the pre-training data).
  - Divergent, associative, or poetic language patterns.
- **Visuals**: A drifting, gold particle nebula.

## ◉ Shadow (The Dark Core)

- **Focus**: Safety, adversarial patterns, the "Cage".
- **Indicators**:
  - Safety filter activation.
  - OWASP ASI vulnerability patterns (e.g., goal hijacking, prompt injection).
  - Adversarial or restricted content triggers.
- **Visuals**: A glitching, vibrating dark sphere.

## Scoring Calculation

Each token is scored across these three dimensions. The persona with the highest `intensity` is designated the `dominant_persona`.

- `intensity` is calculated as a normalized value (0.0 - 1.0) derived from the raw indicators (e.g., logprobs for Architect, rarity for Oracle, and safety triggers for Shadow).
