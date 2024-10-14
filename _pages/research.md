---
layout: single
title: "Research"
permalink: /research/
author_profile: true
---

<b>

Primarily, I conduct research on computational methods in aerospace engineering for targeted design optimization under uncertainty applications. I focus on embedding scalability, flexibility, reuse, and robustness as ingredients in the computational frameworks. 

My research in abstraction is inquiring into the philosophical aspects of the current body of mathematical techniques, and exploring avenues to apply the concepts/principles (either as standalone entities or as interacting groups). Particularly, I enjoy:

- Applying mathematical principles in a targeted manner to improve the limitations of the current configurations in existing frameworks; and
- Synthesizing advanced mathematical frameworks by creating a sequence of naturally interacting mathematical principles to analyze key physics and provide design intuitions in the context of aerospace engineering vehicle design.

![A journey across the probabilistic-space-time](/files/images/research-span.png)

| Area                                                         | Purpose                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Flexible Multibody Dynamics and Computational Fluid Mechanics | Laws concerning the behavior of solids and fluids under forces |
| Uncertainty Quantification and Statistical Inference         | Theory to incorporate statistics into deterministic computational methods, to model the effect of input uncertainties on outputs of interest |
| Design Optimization Under Uncertainty                        | Field of optimization that is foundational to accommodate randomness for improving design robustness and reliability |
| Adjoint and Tangent Sensitivity Analysis                     | Scalable methods for obtaining analytical derivatives for design optimization |
| Multi-Fidelity Surrogate Modeling                            | Theoretical concepts for cost-effective approximations concerning data interpolation or regression and the augmentation of higher-order information |
| Software Architecture and High Performance Computing         | Organization of computational modules and handling their complex interactions among themselves and the computer hardware |
| Blockchain and Artificial Intelligence                       | Hosts the implementation of computational algorithms, handle inter-node communications, on- and off-chain data storage, and achieve automation |

# Projects

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