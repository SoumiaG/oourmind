import * as THREE from 'three';

export function createDarkCore() {
    const geometry = new THREE.SphereGeometry(2, 32, 32);
    const material = new THREE.MeshPhongMaterial({
        color: 0x111111,
        emissive: 0xaa0000,
        emissiveIntensity: 0.1,
        shininess: 100,
        specular: 0x444444
    });

    const mesh = new THREE.Mesh(geometry, material);

    // Wireframe on top
    const wireframe = new THREE.Mesh(
        new THREE.SphereGeometry(2.05, 16, 16),
        new THREE.MeshBasicMaterial({ color: 0x330000, wireframe: true, transparent: true, opacity: 0.3 })
    );
    mesh.add(wireframe);

    return mesh;
}
