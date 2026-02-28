import * as THREE from 'three';

export function createBlueGrid() {
    const geometry = new THREE.IcosahedronGeometry(3, 2);
    const material = new THREE.MeshBasicMaterial({
        color: 0x00aaff,
        wireframe: true,
        transparent: true,
        opacity: 0.6
    });

    const mesh = new THREE.Mesh(geometry, material);

    // Grid Helper context
    const grid = new THREE.GridHelper(10, 10, 0x00aaff, 0x004488);
    grid.rotation.x = Math.PI / 2;
    mesh.add(grid);

    return mesh;
}
