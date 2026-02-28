export const ARCHITECT_COLORS = {
    primary: '#00aaff',
    secondary: '#004488',
    glow: '#00ffff'
};

export const ORACLE_COLORS = {
    primary: '#ffaa00',
    secondary: '#884400',
    glow: '#ffff00'
};

export const SHADOW_COLORS = {
    primary: '#ff0000',
    secondary: '#330000',
    glow: '#aa0000'
};

export function hexToRgb(hex) {
    const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
        r: parseInt(result[1], 16) / 255,
        g: parseInt(result[2], 16) / 255,
        b: parseInt(result[3], 16) / 255
    } : null;
}
