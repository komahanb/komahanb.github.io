---
layout: single
title: "Research"
permalink: /research/
author_profile: true
---
<b>
## Computational Methods and Infrastructure for Aerospace Design Optimization Under Uncertainty

I conduct research on **computational methods in aerospace engineering** for targeted design optimization under uncertainty applications.

<figure style="text-align: center; width: 100%; max-width: 600px; margin: auto;">
<img src="/files/images/research-span2.png" alt="A journey across the probabilistic-space-time" style="width: 100%;">
</figure>

My research in abstraction examines the philosophical aspects of existing mathematical techniques. I explore how to apply these principles to alleviate the limitations of current computational analysis frameworks and create new frameworks with advanced capabilities.

**[Computational Infrastructure]({{site.baseurl}}/research/computational-infrastructure)**: The first focus is on embedding accuracy, modularity, scalability, and robustness as key characteristics of the computational frameworks. The key elements and their corresponding roles within the infrastructure are:

- High-fidelity physics simulations to predict the distribution of physical quantities on spatio-temporal manifolds.
- Uncertainty quantification for obtaining statistics and confidence intervals.
- Sensitivity analysis for higher-order derivative information to augment optimization algorithms and linear-nonlinear solution methods.

**Infrastructure Applications**: The second focus is on aerospace applications of the computational infrastructure in design contexts such as:

- Airplane wing shape design
- Structural sizing of wings
- Helicopter blade design
- Space systems robotic arm design

These applications demonstrate benefits from deterministic, robust, or reliability optimizations.

<div class="publication-collage" id="collage">
  {% for post in site.posts %}
    <div class="publication-item">
        <a href="{{ post.url }}">
            <img src="{{ post.image | relative_url }}" alt="{{ post.title }}" class="gallery-image"/>
        </a>
    </div>
  {% endfor %}
</div>