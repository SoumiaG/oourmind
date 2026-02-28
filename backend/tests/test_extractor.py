import pytest
from backend.extractor import _stream_mock_query
from backend.models import ThoughtData

def test_mock_query_returns_tokens():
    generator = _stream_mock_query("test query", "test-uuid")
    tokens = list(generator)

    assert len(tokens) > 0
    assert isinstance(tokens[0], ThoughtData)
    assert tokens[0].query_id == "test-uuid"
    assert tokens[0].token == "The" # Match first mock token
    assert tokens[0].token_index == 0

def test_mock_query_completeness():
    generator = _stream_mock_query("test query", "test-uuid")
    tokens = list(generator)

    # Confirm it reaches the end of mock tokens
    assert tokens[-1].token_index == len(tokens) - 1
    assert "personas." in tokens[-1].token
