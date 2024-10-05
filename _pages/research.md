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
