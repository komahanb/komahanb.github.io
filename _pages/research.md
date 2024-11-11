---
layout: single
title: "Research"
permalink: /research/
author_profile: true
---
<b>
## Computational Sciences for Aerospace Design Optimization Under Uncertainty

<figure style="text-align: center; width: 100%; max-width: 600px; margin: auto;">
<img src="/files/images/research-span2.png" alt="A journey across the probabilistic-space-time" style="width: 100%;">
</figure>
My research in abstraction is the examination of philosophical aspects of existing mathematical techniques to alleviate the limitations of computational analysis methods and synthesize new methods with advance capabilities such as accuracy, adaptability, modularity, scalability, and robustness.

**[Computational Infrastructure]({{site.baseurl}}/computational-infrastructure)**: The first focus is on the creational aspects of optimization under uncertainty infrastructure for aerospace design composed of key elements such as:

- High-fidelity physics framework predicting the distribution of physical quantities on spatio-temporal manifolds.

- Sensitivity analysis framework providing higher-order derivative information to augment optimization and linear-nonlinear solution methods.

- Uncertainty quantification framework providing statistics and confidence intervals.

The mechanics of interactions among these infrastructure elements is a key challenge. 

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