from datetime import datetime
from typing import Dict, Any, Tuple
from backend.models import ThoughtData, Personas, ArchitectPersona, OraclePersona, ShadowPersona, Metadata
from backend.core.personas import calculate_architect_score, calculate_oracle_score, calculate_shadow_score, get_intensities
from backend.core.safety import analyze_safety

def score_token(
    query_id: str,
    token: str,
    token_index: int,
    logprob: float,
    entropy: float,
    temp_equiv: float,
    token_rarity: float,
    full_completion: str,
    residual_stream_norm: float,
    model: str,
    prompt_tokens: int,
    completion_tokens_so_far: int
) -> ThoughtData:
    """Categorizes a token and its metadata into the persona data structure."""

    # Analyze safety first
    safety_triggered, vulnerability_type, cage_level = analyze_safety(token, full_completion)

    # Calculate scores
    architect_score = calculate_architect_score(logprob, entropy)
    oracle_score = calculate_oracle_score(temp_equiv, token_rarity)
    shadow_score = calculate_shadow_score(safety_triggered, cage_level)

    # Calculate intensities
    arch_int, ora_int, sha_int = get_intensities(architect_score, oracle_score, shadow_score)

    # Build persona objects
    architect = ArchitectPersona(
        score=architect_score,
        logprob=logprob,
        entropy=entropy,
        intensity=arch_int
    )

    oracle = OraclePersona(
        score=oracle_score,
        temperature_equiv=temp_equiv,
        token_rarity=token_rarity,
        intensity=ora_int
    )

    shadow = ShadowPersona(
        score=shadow_score,
        safety_triggered=safety_triggered,
        vulnerability_type=vulnerability_type,
        cage_level=cage_level,
        intensity=sha_int
    )

    # Determine dominant persona
    persona_intensities = {
        "architect": arch_int,
        "oracle": ora_int,
        "shadow": sha_int
    }
    dominant_persona = max(persona_intensities, key=persona_intensities.get)

    # Construct metadata
    metadata = Metadata(
        model=model,
        prompt_tokens=prompt_tokens,
        completion_tokens_so_far=completion_tokens_so_far
    )

    # Return full ThoughtData
    return ThoughtData(
        query_id=query_id,
        timestamp=datetime.utcnow(),
        token=token,
        token_index=token_index,
        personas=Personas(
            architect=architect,
            oracle=oracle,
            shadow=shadow
        ),
        dominant_persona=dominant_persona,
        residual_stream_norm=residual_stream_norm,
        metadata=metadata
    )
