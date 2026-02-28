export function lerp(a, b, t) {
    return a + (b - a) * t;
}

export function clamp(val, min, max) {
    return Math.max(min, Math.min(max, val));
}

export function generateNoise(t) {
    // Simple pseudo-random sine-based noise for vibration
    return Math.sin(t * 10) * Math.sin(t * 1.5) * 0.5;
}

export function normalize(val, min, max) {
    return clamp((val - min) / (max - min), 0, 1);
}
