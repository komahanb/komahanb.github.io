---
layout: single
title: "Research"
permalink: /research/
author_profile: true
---

<b>

I conduct research on **computational methods in aerospace engineering** for targeted design optimization under uncertainty applications.

<figure style="text-align: center; width: 600px; margin: auto;">
    <img src="/files/images/research-span2.png" alt="A journey across the probabilistic-space-time" style="width: 100%;">
</figure>

My research in abstraction is an inquiry into the philosophical aspects of the current body of mathematical techniques and exploring avenues to apply mathematical principles in a configuration that alleviates current limitations within the existing computational analysis frameworks, and create new such frameworks with advanced capabilities.

**<u>Computational Infrastructure:</u>** The first focus is on embedding accuracy, modularity, and scalability, robustness as characteristics of the computational frameworks. The key elements and their corresponding roles within the infrastructure are:

- high-fidelity physics simulations to predict the distribution of physical quantities on spatio-temporal manifolds  
- uncertainty quantification for obtaining statistics and confidence intervals  
- sensitivity analysis for higher-order derivative information to augment optimization algorithms and linear-nonlinear solution methods  

**<u>Infrastructure Applications:</u>** The second focus is on the aerospace applications of the computational infrastructure in design contexts such as:

- airplane wing shape design 
- structural sizing of wings
- helicopter blade design
- space systems robotic arm design

to demonstrate deterministic, robust or reliability optimizations.

<div class="publication-collage" id="collage">
  {% for post in site.posts %}
    <div class="publication-item">
        <a href="{{ post.url }}">
            <img src="{{ post.image | relative_url }}" alt="{{ post.title }}" class="gallery-image"/>
        </a>
    </div>
  {% endfor %}
</div>

<script>
// JavaScript to shuffle grid items every 5 seconds
function shuffleGrid() {
  const collage = document.getElementById('collage');
  const items = Array.from(collage.children);

  // Shuffle the array of items
  items.sort(() => Math.random() - 0.5);

  // Remove existing items and append them in the new shuffled order
  items.forEach(item => collage.appendChild(item));
}

// Set the shuffle to happen every 5 seconds
setInterval(shuffleGrid, 5000);
</script>