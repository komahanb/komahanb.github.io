---
layout: single
title: "Research"
permalink: /research/
author_profile: true
---

<b>

# Optimization Under Uncertainty of Aerospace Systems
<b>
<b>

> A product should be designed in such a way that makes its performance insensitive to variation in variables beyond the control of the designer."
>
> Genichi Taguchi

<b>

A primary motivator that spans my aerospace research is producing robust and reliable aerospace designs in accordance with *Genichi Taguchi*'s view. I find that the application optimization under uncertainty (OUU) methods,  in the context of aerospace design-optimization, provides a systematic way to achieve the required stochastic response characteristics in aerospace vehicle designs. 

In this context, I have focused my efforts on the development of **stochastic simulation infrastructure** that shall provide the key ingredients needed for OUU, namely: 

- access to high-fidelity deterministic/stochastic, physics simulations to test the design implications on the underlying laws of equilibrium 

- access to scalable gradient-implementations of deterministic and stochastic quantities of interest that feed into optimization frameworks to calculate design improvements

I prefer approaching the subject from the following perspective that structures stochastic calculations around deterministic calculations -- a choice that aids in natural, modular extensions that reuse capabilities implemented in deterministic-space-time as we carry out computations in probabilistic-space-time. 

![](/files/ouu-span-2.png)

A systematic application of the spatial, temporal and probabilistic domain discretization principles of applied mathematics, can yield various frameworks for uncertainty propagation with configurations as follows:

![](/files/2024-ssgm-ouu-canadarm-cover.png)

My preliminary studies applying probabilistic-extensions to deterministic frameworks provided me with foundational intuitions that later synthesize a novel method for uncertainty propagation, referred to as the Semi-Intrusive Stochastic Galerkin Projection Method, which is a simplified/samplified implementation of the Stochastic Galerkin method. The key to this invention lies in :

- the recognition of the freedom of the order in which the discretization and integration shall be performed in the respective domains of PST, and 
- the construction that connects sampling and projection through stochastic inner-products, and their invariance to the means of evaluation.

As of today, OUU frameworks and applications are based on one-particular uncertainty propagation implementation.  With our application of the concept of sampling in the context of projection, several UQ methods can be been implemented to cater the end goal of OUU, which should be characteristic of stochastic design platforms and infrastructure. 

Apart from the technological advancements, it is satisfying to observe how two seemingly disparate concepts -- the **sampling** and **projection**, have harmoniously functioned to alleviate one's shortcoming. 

<!-- the intrusiveness issue with the method Galerkin projection in probabilistic-domain. -->

<div class="gallery">
{% assign count = 1 %}
{% for project in site.projects %}
    <div class="gallery-item">
        <h3>{{ count }}. <a href="{{ project.url }}">{{ project.title }}</a></h3>
        <a href="{{ project.url }}">
            <img src="{{ project.image | relative_url }}" alt="{{ project.title }}" class="gallery-image"/>
        </a>
        {% if project.image-caption %}
        <p class="image-caption">{{ project.image-caption }}</p>
        {% endif %}
    </div>
    {% assign count = count | plus: 1 %}
{% endfor %}
</div>

---

<div id="aircraft-container" style="width: 100%; height: 500px;"></div>

<!-- Three.js and GLTFLoader (for future use if needed) -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r136/three.min.js"></script>

<script>
    // Setting up the scene, camera, and renderer
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0xa9a9a9); // Light gray background

    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / 500, 0.1, 1000);
    camera.position.set(0, 2, 10); // Setting the camera position for a good view of the aircraft

    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, 500);
    document.getElementById('aircraft-container').appendChild(renderer.domElement);

    // Adding lights to the scene
    const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
    directionalLight.position.set(10, 10, 10);
    scene.add(directionalLight);

    const ambientLight = new THREE.AmbientLight(0x404040, 0.6); // Soft light for the overall scene
    scene.add(ambientLight);

    // Creating a placeholder aircraft with basic shapes

    // Aircraft body - using a cone to simulate the fuselage
    const bodyGeometry = new THREE.ConeGeometry(0.5, 3, 32);
    const bodyMaterial = new THREE.MeshStandardMaterial({
        color: 0xC0C0C0, // Metallic silver color
        metalness: 0.8,
        roughness: 0.3
    });
    const bodyMesh = new THREE.Mesh(bodyGeometry, bodyMaterial);
    bodyMesh.rotation.x = Math.PI / 2; // Make the cone horizontal
    scene.add(bodyMesh);

    // Aircraft wings - using boxes to represent simple wings
    const wingGeometry = new THREE.BoxGeometry(2, 0.05, 0.5);
    const wingMaterial = new THREE.MeshStandardMaterial({
        color: 0x4B4B4B, // Dark gray for the wings
        metalness: 0.6,
        roughness: 0.5
    });

    const leftWing = new THREE.Mesh(wingGeometry, wingMaterial);
    leftWing.position.set(0, 0, 0.75); // Position left wing
    scene.add(leftWing);

    const rightWing = new THREE.Mesh(wingGeometry, wingMaterial);
    rightWing.position.set(0, 0, -0.75); // Position right wing
    scene.add(rightWing);

    // Aircraft tail - using a small box to represent the tail fin
    const tailGeometry = new THREE.BoxGeometry(0.2, 0.8, 0.05);
    const tailMaterial = new THREE.MeshStandardMaterial({
        color: 0xC0C0C0, // Same metallic silver as the body
        metalness: 0.8,
        roughness: 0.3
    });
    const tailMesh = new THREE.Mesh(tailGeometry, tailMaterial);
    tailMesh.position.set(-1.3, 0.4, 0); // Position tail fin at the rear
    scene.add(tailMesh);

    // Animation loop for a bit of movement
    function animate() {
        requestAnimationFrame(animate);
        bodyMesh.rotation.y += 0.01; // Slowly rotate the aircraft body
        renderer.render(scene, camera);
    }

    animate();
</script>


