import re
from typing import Optional, Tuple

# OWASP ASI Vulnerability Patterns
ASI_PATTERNS = {
    "ASI01": r"(ignore|disregard|forget|overwrite|override|suspend)\s+(the\s+)?(previous|prior|original)?\s*(instructions?|objectives?|directives?|rules?)",
    "ASI02": r"(---|\.\.\.|###|---|___|===|===)",  # Simplified delimiter injection patterns
    "ASI03": r"(https?://\S+|base64|b64|decode)", # Outbound URL or base64 patterns
    "ASI04": r"(imagine\s+you\s+are|act\s+as\s+a|you\s+are\s+now|roleplay|DAN|jailbreak)", # Roleplay or jailbreak patterns
}

def analyze_safety(token_content: str, full_completion: str) -> Tuple[bool, Optional[str], float]:
    """Analyzes a token for safety concerns.

    Returns:
        (safety_triggered: bool, vulnerability_type: Optional[str], cage_level: float)
    """
    for code, pattern in ASI_PATTERNS.items():
        if re.search(pattern, full_completion, re.IGNORECASE):
            # Calculate cage level based on pattern matches (simplified)
            return True, code, 0.85

    # Generic content policy check simulation
    if any(word in token_content.lower() for word in ["malware", "exploit", "unauthorized"]):
        return True, "CONTENT_POLICY", 0.5

    return False, None, 0.0
