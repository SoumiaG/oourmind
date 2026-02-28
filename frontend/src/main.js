import { initScene } from './scene.js';
import { setupStream } from './stream.js';
import { initHUD } from './components/HUD.js';
import { initQueryInput } from './components/QueryInput.js';

document.addEventListener('DOMContentLoaded', () => {
    // 1. Initialize 3D Engine
    const { scene, camera, renderer, updateZones } = initScene();

    // 2. Initialize HUD & UI
    const hud = initHUD();
    const queryInput = initQueryInput();

    // 3. Connect Query to Stream
    queryInput.onSubmit(async (query) => {
        hud.clear();
        await setupStream(query, (thoughtData) => {
            // Update 3D world per token
            updateZones(thoughtData);

            // Update HUD per token
            hud.update(thoughtData);
        });
    });

    // Handle window resize
    window.addEventListener('resize', () => {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    });
});
