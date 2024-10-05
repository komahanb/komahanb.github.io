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
> Genichi Taguchi

<b>

A primary motivator that spans my aerospace research is producing robust and reliable aerospace designs in accordance with *Genichi Taguchi*'s view. I find that the application optimization under uncertainty (OUU) methods,  in the context of aerospace design-optimization, provides a systematic way to achieve the required stochastic response characteristics in aerospace vehicle designs. 

In this context, I focus my efforts on the development of **stochastic simulation infrastructure** that shall provide the key ingredients needed for OUU, namely: 

- access to high-fidelity deterministic/stochastic, physics simulations to test the design implications on the underlying laws of equilibrium 

- access to scalable gradient-implementations of deterministic and stochastic quantities of interest that feed into optimization frameworks to calculate design improvements

I approach the subject, from the following perspective that structures stochastic calculations around deterministic calculations, which helps in modular extensions that reuse capabilities implemented in deterministic-space-time as we carry out computations in probabilistic-space-time.

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
