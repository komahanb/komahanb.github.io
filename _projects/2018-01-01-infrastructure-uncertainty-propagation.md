```
title: "Computational Methods for Uncertainty Propagation through PDE Models" 
image: "files/ouu-span.png"
```

## Propagation Methods through PDEs

An order-agnostic, systematic application of the spatial, temporal, and probabilistic domain discretization principles of applied mathematics can yield various frameworks for uncertainty propagation, with a few particular configurations depicted schematically as follows:

![](/files/2024-ssgm-ouu-canadarm-cover.png)

My preliminary studies applying probabilistic extensions to deterministic frameworks provided foundational intuitions that later helped me synthesize a novel method for uncertainty propagation—referred to as the Semi-Intrusive Stochastic Galerkin Projection Method—which is a *simplified* and *samplified* implementation of the Stochastic Galerkin method. The key to the identification of this mathematical configuration of principles lies in:

- Recognizing the freedom of order in which discretization and integration can be performed in the respective domains of PST.
- Constructing a mathematical connection between sampling and projection through stochastic inner products and exploiting their invariance to evaluation methods.

Even today, OUU frameworks and their aerospace applications rely on computational implementations of uncertainty propagation methods through deterministic physics simulation frameworks. My research philosophy emphasizes the careful application of concepts from sampling in the context of projection and the conjugate use of projection concepts in sampling. Through this dual approach, various uncertainty propagation methods (old and new) with distinct benefits and limitations can be derived and synthesized within a unified computational infrastructure to meet the simulation needs of aerospace design applications.

It is deeply satisfying to observe how two seemingly disparate concepts—sampling and projection—have harmonized to reduce the implementation intrusiveness associated with Galerkin projection, which has impeded its advance over the last two decades. The potential application of this idea to other configurations continues to excite and motivate my research within the OUU context.

<figure style="width: 300px; text-align: center;">   <img src="https://upload.wikimedia.org/wikipedia/commons/4/46/%D0%9B%D0%B0%D0%B3%D1%80%D0%B0%D0%BD%D0%B6.jpg" alt="J. L. Lagrange" style="width: 100%;">   <figcaption style="font-size: 1.0em;">As long as algebra and geometry have been separated, their progress **has** been slow and their uses limited; but when these two sciences have been united, they have lent **each other mutual** forces and marched together towards perfection. <b>J. L. Lagrange [1736 — 1813]</b></figcaption>   </figure>  



## Propagation Methods for Probabilistic and Non-Probabilistic Models of Uncertainties
