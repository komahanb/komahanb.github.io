---
title: ""
permalink: /research/computational-infrastructure
author_profile: true
---

# Computational Infrastructure for Aerospace Optimization Under Uncertainty

<figure style="width: 300px; text-align: center;">    
<!-- <img src="https://www.toolshero.com/wp-content/uploads/2022/08/genichi-taguchi-toolshero.jpg" alt="G. Taguchi" style="width: 100%;"> -->
<figcaption style="font-size: 1.0em;">A product should be designed in such a way that makes its performance insensitive to variation in variables beyond the control of the designer. <b>Genichi Taguchi [1924 — 2012] </b></figcaption>
</figure>
The primary motivation is to produce robust and reliable aerospace designs aligned with Genichi Taguchi's view. I find that the application of optimization under uncertainty (OUU) methods, in the context of aerospace design-optimization, provides a systematic way to achieve the required stochastic response characteristics in aerospace vehicle designs. I focus my efforts on the development of stochastic simulation infrastructure to provide the key ingredients needed for OUU, namely:

- Access to high-fidelity deterministic and stochastic physics simulations to analyze the effect of design changes on the underlying laws of physical equilibrium.  
- Access to design variable gradients of the quantities of interest that feed into optimization frameworks to calculate further design improvements or changes.  
- Access to mean, variance, and standard deviation of the spatio-temporal quantities and their corresponding design variable gradients through the application of the adjoint method. 

<table style="width: 100%; border-collapse: collapse;">
  <tr>
    <td style="text-align: center;">
      <img src="/files/ouu-span.png" alt="OUU Span" style="width: 100%;">
    </td>
    <td style="text-align: center;">
      <img src="/files/ouu-do-schematic.png" alt="Deterministic Optimization Span" style="width: 100%;">
    </td>
  </tr>
  <tr>
    <td style="text-align: center;">
      OUU is in the span of (1), (2) and (3)
    </td>
    <td style="text-align: center;">
      Deterministic Optimization is in the span of (1) and (3)
    </td>
  </tr>
</table>

For the creation of simulation infrastructure, I apply the philosophical perspective of structuring stochastic calculations around deterministic calculations -- a choice that aids in natural, modular extensions that reuse capabilities implemented in deterministic space-time (DST) when computations are carried out in probabilistic space-time (PST).

![](/files/ouu-span-2.png)

---

## (I) Computational Methods for High Fidelity Spatio-Temporal Physics







---

## (II) Computational Sensitivity Analysis Methods for Higher Order Derivatives

<figure style="width: 300px; text-align: center;">    <img src="https://mathshistory.st-andrews.ac.uk/Biographies/Lanczos/Lanczos_4.jpeg" alt="C. Lanczos" style="width: 100%;"> 
<figcaption style="font-size: 1.0em;">... the idea of enlarging reality by including “tentative” possibilities and then selecting one of these by the condition that it minimizes a certain quantity, seems to bring purpose to the flow of natural events. <b>Cornelius Lanczos [1893–1974] </b></figcaption>
</figure>

My research along this trajectory is development of methods for calculating accurate gradients in a scalable manner -- to the number of design variables, as well as to the number of metrics of interest. 

![](/files/derivative-methods.png)

**The Adjoint Method**

My main interest is on the adjoint-based methods for sensitivity analysis. It offers scalability in terms of the number of design variables. I have focused on formulating and implementing time-dependent sensitivity analysis methods with several order agnostic multi-step and multi-stage time integrators in deterministic space time. This exercise has also been carried out in the probabilistic space time where without an explicit implementation of the stochastic adjoint, the adjoint fields are solved implicitly to assemble the adjoint gradient of statistics.

> Although the time-marching schemes come with various stencils, the overarching structure that is common to all methods is that the partial derivatives of the residuals and functions are combined using different weights to implement discrete adjoint methods. 

**Higher-Dimensional Numbers Based On Algebraic Structures and Differential Operators**

I also consider other possibilities to obtain design variable derivatives. I study the construction of higher-dimensional numbers that can provide first, second, and other higher-order derivatives, if necessary. This research is building upon the observations from complex-number arithmetics to four-, and eight-dimensional numbers.

---

## (III) Uncertainty Propagation Methods through PDE Models

My research explores the application of **probabilistic extensions** to deterministic frameworks for new perspective on uncertainty propagation through PDEs. One of the key results is the development of the **Semi-Intrusive Stochastic Galerkin Projection Method**, a *simplified* and *samplified* version of the Stochastic Galerkin method. In this [demonstration](https://komahanb.github.io/journals/ssgm-ouu-canadarm/), the probabilistic domain integration is performed around spatial integration that uses the finite-element method, followed by time-domain integration. This method draws from:

- The **flexibility in the order** of discretization and integration across the probabilistic space-time (PST) domain.
- A **mathematical construction** that connects *sampling* and *projection* through *stochastic inner products*, exploiting their invariance to the method of evaluation, whether analytical, numerical, or experimental.

The following diagram outlines various **uncertainty propagation methods** in PDE models, detailing how **input probability distributions** influence stochastic solutions that yield **output statistics** like **expectation** and **variance**.

<figure style="text-align: center; width: 100%;">
  <img src="/files/2024-ssgm-ouu-canadarm-cover.png" alt="Uncertainty Propagation Methods" style="max-width: 100%;">
  <figcaption style="font-size: 1.0em;">Figure: Key methods for uncertainty propagation using probabilistic and deterministic frameworks</figcaption>
</figure>

An **discretization-order agnostic** and **physics independent** application of spatial, temporal, and probabilistic discretization principles can yield diverse frameworks for uncertainty propagation. Some of the key methods include:

1. **Stochastic Sampling & Surrogate Models**
   This method uses **sampling nodes** to generate **surrogate models**, approximating PDE outputs with lower computational costs.
2. **Stochastic Galerkin Projection**
   Introduces **spectral expansions** and solves SPDEs, generating **output spectral modes** directly from the assembly of the SPDE.
3. **Stochastic Spectral Projection**
   Combines **spectral expansions** with **sampling nodes** for deterministic PDE solutions, producing **output spectral modes** through post-processing.
4. **Semi-Intrusive Stochastic Galerkin Projection**
   Integrates **spectral expansions** and **sampling nodes** to assemble and solve **sampled matrices and vectors** for SPDEs.

It is deeply satisfying from a philosophical perspective to witness how two seemingly disparate concepts—**sampling** and **projection**—harmonize to reduce the implementation intrusiveness of Galerkin projection. This long-standing challenge, which has slowed the method's advancement for decades, is resolved by the integration of these ideas. The potential to extend this synthesis to other configurations drives my ongoing research within **OUU**. This vision aligns with the philosophical framework outlined by pioneers like **Lagrange**, whose unification of algebra and geometry mirrors the synthesis of **sampling** and **projection** in modern computational methods. The merging of these two fields not only accelerates the progress of uncertainty quantification but also highlights the beauty of their interconnectedness—a guiding principle in my research.

<figure style="text-align: center; width: 300px; margin: auto;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/4/46/%D0%9B%D0%B0%D0%B3%D1%80%D0%B0%D0%BD%D0%B6.jpg" alt="J. L. Lagrange" style="width: 100%;">
  <figcaption style="font-size: 1.0em;">As long as algebra and geometry have been separated, their progress **has** been slow and their uses limited; but when these two sciences have been united, they have lent **each other mutual** forces and marched together towards perfection. <b>J. L. Lagrange [1736 — 1813]</b></figcaption>
</figure>







## 
