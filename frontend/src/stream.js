export async function setupStream(query, onToken) {
    const response = await fetch('/api/think/stream', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query }),
    });

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    let buffer = '';

    while (true) {
        const { value, done } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });

        // SSE messages are separated by double newlines
        const parts = buffer.split('\n\n');
        buffer = parts.pop();

        for (const part of parts) {
            if (part.startsWith('data: ')) {
                const data = part.slice(6);

                if (data === '[DONE]') {
                    console.log('Stream finished.');
                    return;
                }

                try {
                    const parsed = JSON.parse(data);
                    onToken(parsed);
                } catch (e) {
                    console.error('Failed to parse SSE data:', e, data);
                }
            }
        }
    }
}
