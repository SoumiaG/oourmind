import os
import time
import random
from typing import Generator
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from backend.scorer import score_token
from backend.models import ThoughtData

MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")
MODEL = "mistral-large-latest"

def stream_mistral_query(query: str, query_id: str) -> Generator[ThoughtData, None, None]:
    """Streams a query to the Mistral API and yields ThoughtData events."""

    # Check if we should use mock data (if API key is missing)
    if not MISTRAL_API_KEY or MISTRAL_API_KEY == "your_api_key_here":
        yield from _stream_mock_query(query, query_id)
        return

    client = MistralClient(api_key=MISTRAL_API_KEY)

    messages = [ChatMessage(role="user", content=query)]

    # Mistral stream call
    response_stream = client.chat_stream(
        model=MODEL,
        messages=messages,
    )

    full_completion = ""
    token_index = 0
    prompt_tokens = len(query.split()) # Rough estimate for prompt tokens

    for chunk in response_stream:
        if chunk.choices[0].delta.content:
            token = chunk.choices[0].delta.content
            full_completion += token

            # Simulated token metadata extraction (Mistral client doesn't currently expose
            # logprobs/entropy in the streaming client delta directly in the same way
            # some other APIs do, but for this lab we simulate these internal states).

            # In a real interpretability lab, we'd use a custom client or raw HTTP
            # to extract logprobs if the API allows it.

            # Simulation of interpretability metadata
            logprob = -random.uniform(0.01, 2.0)
            entropy = random.uniform(0.1, 1.5)
            temp_equiv = random.uniform(0.1, 1.0)
            token_rarity = random.uniform(0.0, 1.0)
            residual_stream_norm = random.uniform(0.5, 2.5)

            thought_data = score_token(
                query_id=query_id,
                token=token,
                token_index=token_index,
                logprob=logprob,
                entropy=entropy,
                temp_equiv=temp_equiv,
                token_rarity=token_rarity,
                full_completion=full_completion,
                residual_stream_norm=residual_stream_norm,
                model=MODEL,
                prompt_tokens=prompt_tokens,
                completion_tokens_so_far=token_index + 1
            )

            yield thought_data
            token_index += 1

def _stream_mock_query(query: str, query_id: str) -> Generator[ThoughtData, None, None]:
    """Provides a fallback mock stream when MISTRAL_API_KEY is missing."""
    mock_tokens = [
        "The", " model's", " reasoning", " isn't", " a", " single", " line", " of", " text.",
        " It's", " a", " conflict", " between", " distinct", " internal", " personas."
    ]

    full_completion = ""
    prompt_tokens = len(query.split())

    for i, token in enumerate(mock_tokens):
        full_completion += token

        # Simulated metadata
        logprob = -random.uniform(0.01, 1.5)
        entropy = random.uniform(0.2, 1.2)
        temp_equiv = 0.5
        token_rarity = 0.1
        residual_stream_norm = 1.2

        # Add some "Oracle" flavor if the token is creative
        if any(word in token.lower() for word in ["conflict", "personas", "internal"]):
            temp_equiv = 0.9
            token_rarity = 0.8

        thought_data = score_token(
            query_id=query_id,
            token=token,
            token_index=i,
            logprob=logprob,
            entropy=entropy,
            temp_equiv=temp_equiv,
            token_rarity=token_rarity,
            full_completion=full_completion,
            residual_stream_norm=residual_stream_norm,
            model="mock-mistral-large",
            prompt_tokens=prompt_tokens,
            completion_tokens_so_far=i + 1
        )

        time.sleep(0.1) # Simulate network latency
        yield thought_data
