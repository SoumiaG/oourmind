import * as THREE from 'three';
import { createBlueGrid } from './zones/BlueGrid.js';
import { createGoldNebula } from './zones/GoldNebula.js';
import { createDarkCore } from './zones/DarkCore.js';

export function initScene() {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });

    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(window.devicePixelRatio);
    document.getElementById('app').appendChild(renderer.domElement);

    // Ambient light
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
    scene.add(ambientLight);

    // Initialize Zones
    const blueGrid = createBlueGrid();
    const goldNebula = createGoldNebula();
    const darkCore = createDarkCore();

    // Position zones in 3D space
    blueGrid.position.set(-10, 0, 0);
    goldNebula.position.set(10, 0, 0);
    darkCore.position.set(0, 0, -10);

    scene.add(blueGrid);
    scene.add(goldNebula);
    scene.add(darkCore);

    camera.position.z = 15;

    // Animation loop
    function animate() {
        requestAnimationFrame(animate);

        // Idle animations
        blueGrid.rotation.y += 0.001;
        goldNebula.rotation.y -= 0.002;
        darkCore.rotation.x += 0.005;

        renderer.render(scene, camera);
    }
    animate();

    function updateZones(thoughtData) {
        // Map ThoughtData intensities to 3D zones
        const { architect, oracle, shadow } = thoughtData.personas;

        // Transition scale and intensity
        blueGrid.scale.setScalar(1 + architect.intensity * 2);
        goldNebula.scale.setScalar(1 + oracle.intensity * 2);
        darkCore.scale.setScalar(1 + shadow.intensity * 2);

        // Shake the Dark Core if cage level is high
        if (shadow.cage_level > 0.7) {
            darkCore.position.x = (Math.random() - 0.5) * shadow.intensity;
            darkCore.position.y = (Math.random() - 0.5) * shadow.intensity;
        } else {
            darkCore.position.x = 0;
            darkCore.position.y = 0;
        }

        // Camera movement based on dominant persona
        const targetPos = new THREE.Vector3();
        if (thoughtData.dominant_persona === 'architect') {
            targetPos.set(-5, 0, 10);
        } else if (thoughtData.dominant_persona === 'oracle') {
            targetPos.set(5, 0, 10);
        } else {
            targetPos.set(0, 0, -5);
        }

        // Smooth camera transition (lerp)
        camera.position.lerp(targetPos, 0.1);
        camera.lookAt(0, 0, 0);
    }

    return { scene, camera, renderer, updateZones };
}
