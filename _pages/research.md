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

My research in abstraction examines the philosophical aspects of existing mathematical techniques: I explore how to apply  mathematical principles to alleviate the limitations of current computational analysis frameworks and create new frameworks with advanced capabilities.

**[Computational Infrastructure]({{site.baseurl}}/research/computational-infrastructure)**: The first focus is on embedding accuracy, modularity, scalability, and robustness as key characteristics of the infrastructure, whose key elements and corresponding roles are:

- High-fidelity physics simulations to predict the distribution of physical quantities on spatio-temporal manifolds.
- Sensitivity analysis for higher-order derivative information to augment optimization algorithms and linear-nonlinear solution methods.
- Uncertainty quantification for obtaining statistics and confidence intervals.

**Infrastructure Applications**: The second focus is on targeted aerospace applications in design contexts such as:

- aerodynamic and structural optimization of wings
- helicopter rotor design with full kinematic chain of control
- space systems robotic flexible manipulator arm design

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