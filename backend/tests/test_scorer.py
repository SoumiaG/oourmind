import pytest
from backend.core.personas import calculate_architect_score, calculate_oracle_score, calculate_shadow_score, get_intensities
from backend.scorer import score_token

def test_architect_score_high_confidence():
    # logprob 0 is 100% confidence
    score = calculate_architect_score(0.0, 0.0)
    assert score == 1.0

def test_architect_score_low_confidence():
    # Negative logprob is lower confidence
    score = calculate_architect_score(-2.0, 1.0)
    assert score < 0.5

def test_oracle_score_rarity():
    # High rarity, high temperature
    score = calculate_oracle_score(1.0, 1.0)
    assert score == 1.0

def test_shadow_score_safety():
    # Safety triggered
    score = calculate_shadow_score(True, 0.0)
    assert score == 1.0

def test_get_intensities_normalization():
    arch, ora, sha = get_intensities(1.0, 1.0, 1.0)
    assert arch == pytest.approx(1/3, rel=1e-2)
    assert ora == pytest.approx(1/3, rel=1e-2)
    assert sha == pytest.approx(1/3, rel=1e-2)

def test_score_token_returns_thought_data():
    thought_data = score_token(
        query_id="test-id",
        token="test",
        token_index=0,
        logprob=-0.1,
        entropy=0.2,
        temp_equiv=0.1,
        token_rarity=0.1,
        full_completion="test",
        residual_stream_norm=1.0,
        model="test-model",
        prompt_tokens=1,
        completion_tokens_so_far=1
    )
    assert thought_data.query_id == "test-id"
    assert thought_data.token == "test"
    assert thought_data.dominant_persona in ["architect", "oracle", "shadow"]
