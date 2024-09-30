---
title: "About Me"
permalink: /
author_profile: true
redirect_from: 
  - /about
  - /about.html
---

My passion lies in crafting simulation frameworks that model and analyze the equilibrium of aerospace vehicle components with the environmental surroundings --  thereby, to provide means for design improvement through statistics of quantities of interest and their sensitivities to design variable perturbations. Thus, I undertake as well as take-part in the development of scalable, flexible and robust computational frameworks -- for scientific computing and targeted applications in aerospace vehicle design contexts such as fixed-wing aircrafts, rotorcrafts and space system robotic arms. 

| ![](../images/fixedwing.png) | ![](../images/rotorcraft.png) | ![](../images/spaceshuttle.png) |
| :--------------------------: | :---------------------------: | :-----------------------------: |
|       Aircraft Design        |       Rotorcraft Design       |      Space Systems Design       |

Currently, I work as a Senior Research Engineer at ANSYS, focused on the development activities of the Fluent GPU solver offering [orders of magnitude speed-up, and energy savings](https://www.ansys.com/blog/unleashing-the-full-power-of-gpus-for-ansys-fluent) over classical CPU-based HPC in the context of computational fluid dynamics (CFD) simulations. 

## Graduate Research

I hold a Ph.D. in Aerospace Engineering from the Georgia Institute of Technology, working as a research assistant in the [SMDO laboratory](https://gkennedy.gatech.edu/) led by [Prof. Graeme Kennedy](https://scholar.google.com/citations?user=LHqGhxkAAAAJ&hl=en). 

- I concentrated on the development of a computational [flexible multibody dynamics solver](https://github.com/smdogroup/tacs) with adjoint sensitivity analysis capabilities for the NASA Langley Research Center's [rotorcraft design applications](https://www.youtube.com/watch?v=-HM0KycBvnA), offering scalability benefits in the context of solving large-scale optimization problems.
- This deterministic computational framework was then naturally generalized into an [adjoint-enabled stochastic finite-element, flexible multibody dynamics framework](https://github.com/komahanb/stacs). The stochastic framework is capable of providing statistical information on quantities of interest and adjoint gradient of statistics.

I also hold a Master's degree in Aerospace Engineering from the University of Dayton working as a research assistant in [Prof. Markus Rumpfkeil's](https://scholar.google.com/citations?user=zCRdVjYAAAAJ&hl=en) CFD laboratory.

-  I focused on the development of methods for aerodynamic optimization under uncertainty using surrogate models, as well as adaptive means for model error-estimation and training-point-selection. 

For more detailed information, the theses and associated presentations shall be accessed below:

| Degree | Program               | School                          | Year         | Thesis                                                       | Slides                                                       |
| ------ | --------------------- | ------------------------------- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Ph.D   | Aerospace Engineering | Georgia Institute of Technology | 2015 -- 2020 | [Adjoint Based Design Optimization of Systems with Time Dependent Physics and Probabilistically Modeled Uncertainties](http://hdl.handle.net/1853/63658) | <a href="../files/publications/komahan-boopathy-phd-defense.pdf"><img src="../files/phd-defense-slides-cover.png" alt="Slides Cover" style="width:100px;"></a> |
| M.S    | Aerospace Engineering | University of Dayton            | 2012 -- 2014 | [Uncertainty Quantification and Optimization Under Uncertainty Using Surrogate Models](http://rave.ohiolink.edu/etdc/view?acc_num=dayton1398302731) | <a href="../files/publications/komahan-boopathy-masters-defense.pdf"><img src="../files/masters-defense-slides-cover.png" alt="Slides Cover" style="width:100px;"></a> |


<div class="gallery">
{% assign count = 1 %}
{% for post in site.posts %}
    {% if post.categories contains "thesis" %}
    <div class="gallery-item">
        <h3>{{ count }}. <a href="{{ post.url }}">{{ post.title }}</a></h3>
        <a href="{{ post.url }}">
            <img src="{{ post.image | relative_url }}" alt="{{ post.title }}" class="gallery-image"/>
        </a>
        {% if post.image-caption %}
        <p class="image-caption">{{ post.image-caption }}</p>
        {% endif %}
    </div>
    {% assign count = count | plus: 1 %}
    {% endif %}
{% endfor %}
</div>

# Curriculum Vitae

<iframe src="../files/KomahanBoopathyCV.pdf" width="100%" height="500"  frameborder="yes" border="10" marginwidth="10"  marginheight="10"></iframe>