---
layout: single
title: "Research"
permalink: /research/
author_profile: true
---

<b>

# Aerospace Design and Optimization Under Uncertainty


<figure style="width: 300px; text-align: center;">    <img src="https://www.toolshero.com/wp-content/uploads/2022/08/genichi-taguchi-toolshero.jpg" alt="G. Taguchi" style="width: 100%;"> 
<figcaption style="font-size: 1.0em;">A product should be designed in such a way that makes its performance insensitive to variation in variables beyond the control of the designer. <b>Genichi Taguchi [1924 — 2012] </b></figcaption>
</figure>

A primary motivator that spans and generates my aerospace research is producing robust and reliable aerospace designs in resonance with *Genichi Taguchi*'s view. I find that the application optimization under uncertainty (OUU) methods,  in the context of aerospace design-optimization, provides a systematic way to achieve the required stochastic response characteristics in aerospace vehicle designs. 

With this motivation, I have focused my efforts on the development of **stochastic simulation infrastructure** that shall provide the key ingredients needed for OUU, namely: 

- access to high-fidelity deterministic and stochastic, physics simulation outputs to analyze the effect of design changes on the underlying laws of physical equilibrium 

- access to gradient-implementations of the deterministic and stochastic quantities of interest that feed into optimization frameworks to calculate further design improvements or changes

I take the standpoint of is approaching this computational and mathematical aeroscience and technology from the following perspective of structuring stochastic calculations around deterministic calculations -- a choice that aids in natural, modular extensions that reuse capabilities implemented in deterministic-space-time (DST) as we carry out computations in probabilistic-space-time (PST). 

![](/files/ouu-span-2.png)

An order-agnostic and systematic application of the spatial, temporal and probabilistic domain discretization principles of applied mathematics, can yield various frameworks for uncertainty propagation with a few particular configurations depicted schematically as follows:

![](/files/2024-ssgm-ouu-canadarm-cover.png)

My preliminary studies applying probabilistic-extensions to deterministic frameworks provided me with foundational intuitions that later helped synthesize a novel method for uncertainty propagation, referred to as the Semi-Intrusive Stochastic Galerkin Projection Method, which is a *simplified* and *samplified* implementation of the Stochastic Galerkin method. The key to this invention lies in :

- the recognition of the freedom of the order in which the discretization and integration shall be performed in the respective domains of PST, and 
- the mathematical construction that connects sampling and projection through stochastic inner-products, and their invariance to the means of evaluation.

As of today, the OUU frameworks and their aerospace applications are based on the computational implementations of a particular method of uncertainty propagation through deterministic physics simulation frameworks. My research philosophy in this context are careful applications of the concepts from sampling in the context of projection, and the *conjugate* applications of the concepts from projection in the context of sampling, through which several uncertainty propagation methods (old and new) with varied benefits and limitations shall be derived/synthesized in a generalized fashion under a unified computational infrastructure to facilitate the simulation needs emerging from aerospace design applications.

Apart from seeing the technology advance as above in accordance with the unified perspectives of sampling and projection, it is deeply satisfying to observe how two seemingly disparate concepts -- the **sampling** and **projection**, have harmoniously synchronized to alleviate the issue of implementation intrusiveness in the context of Galerkin projection, which has been impeding its advance and maturity over the last two decades. The potential application of this idea in other configurations excites and motivates my research in the context of OUU.

<figure style="width: 300px; text-align: center;">    <img src="https://upload.wikimedia.org/wikipedia/commons/4/46/%D0%9B%D0%B0%D0%B3%D1%80%D0%B0%D0%BD%D0%B6.jpg" alt="J. L. Lagrange" style="width: 100%;"> 
<figcaption style="font-size: 1.0em;">As long as algebra and geometry have been  separated, their progress have been slow and their uses limited; but when these two sciences have been united, they have lent each mutual forces, and have marched together towards perfection. <b> J. L. Lagrange [1736 — 1813] </b> </figcaption>
</figure>

<!--

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

-->