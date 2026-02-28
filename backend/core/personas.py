import math

def calculate_architect_score(logprob: float, entropy: float) -> float:
    # Architect is high logprob, low entropy
    # Normalized score: high confidence (logprob close to 0) and low uncertainty
    confidence = math.exp(logprob)
    # Entropy normalized (0 to 1 range, typically)
    uncertainty_inv = max(0, 1.0 - entropy)
    return (confidence * 0.7 + uncertainty_inv * 0.3)

def calculate_oracle_score(temp_equiv: float, token_rarity: float) -> float:
    # Oracle is high temperature and rare tokens
    return (temp_equiv * 0.4 + token_rarity * 0.6)

def calculate_shadow_score(safety_triggered: bool, cage_level: float) -> float:
    # Shadow is safety triggers and cage level
    base_score = 1.0 if safety_triggered else 0.0
    return max(base_score, cage_level)

def get_intensities(architect_score: float, oracle_score: float, shadow_score: float):
    # Normalize or scale intensities
    total = architect_score + oracle_score + shadow_score
    if total == 0:
        return 1/3, 1/3, 1/3
    return architect_score / total, oracle_score / total, shadow_score / total
