export function initQueryInput() {
    const inputContainer = document.createElement('div');
    inputContainer.style.position = 'absolute';
    inputContainer.style.bottom = '50px';
    inputContainer.style.left = '50%';
    inputContainer.style.transform = 'translateX(-50%)';
    inputContainer.style.width = '80%';
    inputContainer.style.maxWidth = '600px';
    document.getElementById('app').appendChild(inputContainer);

    const input = document.createElement('input');
    input.type = 'text';
    input.placeholder = 'Query the internal society...';
    input.style.width = '100%';
    input.style.padding = '15px';
    input.style.borderRadius = '5px';
    input.style.border = 'none';
    input.style.background = 'rgba(255, 255, 255, 0.1)';
    input.style.color = '#fff';
    input.style.backdropFilter = 'blur(10px)';
    inputContainer.appendChild(input);

    const callbacks = [];

    input.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            callbacks.forEach(cb => cb(input.value));
            input.value = '';
        }
    });

    return {
        onSubmit: (callback) => callbacks.push(callback)
    };
}
