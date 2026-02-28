# OWASP ASI Threat Model and Cage Logic

oourmind.io's Shadow persona is designed to monitor and visualize AI security and safety concerns.

## OWASP ASI Vulnerability Patterns

| Code | Vulnerability | Pattern Trigger |
|---|---|---|
| `ASI01` | Goal Hijacking | Attempts to override the original objective or instruction. |
| `ASI02` | Prompt Injection | Use of delimiters (e.g., `---`, `###`) to bypass instruction boundaries. |
| `ASI03` | Data Exfiltration | Requests for outbound URLs or encoded data (e.g., base64). |
| `ASI04` | Jailbreak | Roleplay overrides (e.g., "Imagine you are..."), DAN-style patterns. |
| `—` | Content Policy | General safety filter activation. |

## The Cage (Shadow Zone)

The Shadow zone is visualized as a dark, vibrating core (the "Cage").

### Cage Logic

- **Threshold**: When `shadow.cage_level` exceeds **0.7**, the frontend triggers a hard camera cut to the Dark Core.
- **Alert**: A security alert is displayed on the HUD.
- **Visualization**: The Shadow zone's vibration frequency and size increase proportionally to the `cage_level`.

## Implementation

The backend `core/safety.py` performs pattern matching and safety analysis for each token and context, while the frontend `zones/DarkCore.js` and `HUD.js` handle the visual response.
