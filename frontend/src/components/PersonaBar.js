export function createPersonaBar(name, color) {
    const container = document.createElement('div');
    container.style.marginBottom = '10px';

    const label = document.createElement('div');
    label.textContent = name;
    label.style.fontSize = '0.8rem';
    label.style.color = '#888';
    container.appendChild(label);

    const barContainer = document.createElement('div');
    barContainer.style.width = '100%';
    barContainer.style.height = '4px';
    barContainer.style.background = '#222';
    container.appendChild(barContainer);

    const fill = document.createElement('div');
    fill.style.width = '0%';
    fill.style.height = '100%';
    fill.style.background = color;
    fill.style.transition = 'width 0.2s';
    barContainer.appendChild(fill);

    return {
        element: container,
        update: (intensity) => {
            fill.style.width = `${intensity * 100}%`;
        }
    };
}
