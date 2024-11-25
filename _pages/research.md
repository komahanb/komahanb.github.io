---
layout: single
title: "Research"
permalink: /research/
author_profile: true
---

<b>
## Computational Sciences for Aerospace Design Optimization Under Uncertainty

<figure style="text-align: center; width: 100%; max-width: 600px; margin: auto;">
    <img src="/files/images/research-span2.png" alt="A journey across the probabilistic-space-time" class="zoom-out-image" style="width: 100%;">
</figure>

My research in abstraction is the examination of philosophical aspects of existing mathematical techniques to alleviate the limitations of computational analysis methods and synthesize new methods with advance capabilities such as accuracy, adaptability, modularity, scalability, and robustness.

---

**[Computational Infrastructure]({{site.baseurl}}/computational-infrastructure)**: The first focus is on the creational aspects of optimization under uncertainty infrastructure for aerospace design composed of key elements such as:

- **High-fidelity physics** framework predicting the distribution of physical quantities on spatio-temporal manifolds.

- **Sensitivity analysis** framework providing higher-order derivative information to augment optimization and linear-nonlinear solution methods.

- **Uncertainty quantification** framework providing statistics and confidence intervals.

The mechanics of interactions among these infrastructure elements is a key challenge. It is a critical piece of technology required for **Multidisciplinary Optimization Under Uncertainty** efforts such as [NASA CFD Vision 2030](https://www.cfd2030.com/).

<div class="image-slider">
    <img id="slider" src="/files/images/cfd-vision-2030-roadmap.png" alt="https://www.cfd2030.com/report/CFD-Vision-2030-Roadmap-2020-wide.png" />
</div>


<script>
    const sliderImage = document.querySelector('.image-slider img');

    sliderImage.addEventListener('mousemove', (event) => {
        const rect = sliderImage.getBoundingClientRect();
        const x = ((event.clientX - rect.left) / rect.width) * 100; // Calculate x percentage
        const y = ((event.clientY - rect.top) / rect.height) * 100; // Calculate y percentage

        sliderImage.style.transformOrigin = `${x}% ${y}%`; // Set transform origin
    });

    sliderImage.addEventListener('mouseleave', () => {
        sliderImage.style.transformOrigin = 'center'; // Reset transform origin on mouse leave
    });
</script>

<script>
    const images = [
        "/files/images/cfd-vision-2030-roadmap.png",
        "/files/images/cfd-vision-2030-roadmap-annotated.png"
    ];
    let currentIndex = 0;

    function cycleImages() {
        const slider = document.getElementById("slider");
        currentIndex = (currentIndex + 1) % images.length;
        slider.src = images[currentIndex];
    }
    
    // Change image every 3 seconds
    setInterval(cycleImages, 3000);
</script>

<script>
    const sliderImage = document.querySelector('.image-slider img');

    sliderImage.addEventListener('mousemove', (event) => {
        const rect = sliderImage.getBoundingClientRect();
        const x = ((event.clientX - rect.left) / rect.width) * 100; // Calculate x percentage
        const y = ((event.clientY - rect.top) / rect.height) * 100; // Calculate y percentage

        sliderImage.style.transformOrigin = `${x}% ${y}%`; // Set transform origin
    });

    sliderImage.addEventListener('mouseleave', () => {
        sliderImage.style.transformOrigin = 'center'; // Reset transform origin on mouse leave
    });
</script>

---

**Infrastructure Applications**: The second focus is on targeted aerospace applications in design contexts such as:

- aerodynamic and structural optimization of wings
- helicopter rotor blade design in the presence of full kinematic chain of control
- robotic flexible manipulator arms of space systems

to demonstrate benefits from the use of computational infrastructure in contexts such as deterministic, robust, or reliability optimizations.

<div class="publication-collage" id="collage">
  {% for post in site.posts %}
    <div class="publication-item">
        <a href="{{ post.url }}">
            <img src="{{ post.image | relative_url }}" alt="{{ post.title }}" class="gallery-image"/>
        </a>
    </div>
  {% endfor %}
</div>