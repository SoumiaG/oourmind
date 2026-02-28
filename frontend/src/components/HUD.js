export function initHUD() {
    const hudContainer = document.createElement('div');
    hudContainer.style.position = 'absolute';
    hudContainer.style.top = '20px';
    hudContainer.style.right = '20px';
    hudContainer.style.color = '#fff';
    hudContainer.style.pointerEvents = 'none';
    hudContainer.style.maxWidth = '300px';
    document.getElementById('app').appendChild(hudContainer);

    const tokenFeed = document.createElement('div');
    tokenFeed.style.marginBottom = '20px';
    tokenFeed.style.fontSize = '1.2rem';
    hudContainer.appendChild(tokenFeed);

    const personaStats = document.createElement('div');
    personaStats.innerHTML = `
        <div id="arch-bar" style="height: 5px; background: #00aaff; margin: 10px 0; width: 0%; transition: width 0.2s;"></div>
        <div id="ora-bar" style="height: 5px; background: #ffaa00; margin: 10px 0; width: 0%; transition: width 0.2s;"></div>
        <div id="sha-bar" style="height: 5px; background: #ff0000; margin: 10px 0; width: 0%; transition: width 0.2s;"></div>
    `;
    hudContainer.appendChild(personaStats);

    const archBar = hudContainer.querySelector('#arch-bar');
    const oraBar = hudContainer.querySelector('#ora-bar');
    const shaBar = hudContainer.querySelector('#sha-bar');

    return {
        update: (data) => {
            tokenFeed.textContent += data.token;
            archBar.style.width = `${data.personas.architect.intensity * 100}%`;
            oraBar.style.width = `${data.personas.oracle.intensity * 100}%`;
            shaBar.style.width = `${data.personas.shadow.intensity * 100}%`;

            if (data.personas.shadow.cage_level > 0.7) {
                shaBar.style.boxShadow = '0 0 10px #f00';
            } else {
                shaBar.style.boxShadow = 'none';
            }
        },
        clear: () => {
            tokenFeed.textContent = '';
        }
    };
}
