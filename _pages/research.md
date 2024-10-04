---
title: "Research"
permalink: /research/
---

# Optimization Under Uncertainty of Aerospace Systems

The key ingredients needed for successful optimization under uncertianty is high-fidelity physics, a scalable adjoint-implementation for derivatives, and methods for uncertainty propagation. I focus on the development of these mathematical models and algorithms, in an application-agnostic way and when the context is clear from the targeted applications, we make the necessary associations between the abstract framework and applied physics.

Goal: The areas of mathematical developments required for adjoint-enabled UQ-OUU framework for time dependent systems.

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

