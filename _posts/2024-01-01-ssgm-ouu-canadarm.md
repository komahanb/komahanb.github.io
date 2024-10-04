---
title: "Semi-Intrusive Stochastic Galerkin Finite Element Method for Adjoint-Based Optimization Under Uncertainty"
categories: journals
image: "/files/2024-ssgm-ouu-canadarm-cover.svg"
---

[Journal of Aerospace Information Systems](https://arc.aiaa.org/journal/jais); Volume 21; Number 9; Year 2024

[https://doi.org/10.2514/1.I011254](https://doi.org/10.2514/1.I011254)

The stochastic Galerkin method for the propagation of probabilistically modeled uncertainties can be difficult to apply in practice due to its formulation and the challenge of creating a computational infrastructure to support it. To address these challenges, this work proposes a sampling-based stochastic Galerkin method that leverages existing deterministic analysis and adjoint-based derivative implementations. The proposed formulation is semi-intrusive, since it is implemented using an existing deterministic framework, requiring only the numerical sampling of the deterministic residuals, Jacobians, boundary conditions, and adjoint implementations at nodes in the probabilistic domain. The software architectures to support stochastic generalizations of the deterministic finite element frameworks are presented. This proposed approach is demonstrated on a finite-element framework for flexible multibody dynamics problems. Finally, the semi-intrusive implementation of the stochastic Galerkin method is used to demonstrate adjoint gradient-based optimizations of flexible multibody dynamics systems in the presence of probabilistically modeled uncertainties.

![](/files/2024-ssgm-ouu-canadarm-cover.png)
<p align="center"><b>Figure:</b> (1), (3), (4) are the easy to implement sampling-based methods for the propagation of uncertainties through computational physics frameworks.</p>

<iframe src="/files/2024-ssgm-ouu-canadarm-preprint.pdf" width="100%" height="500"  frameborder="yes" border="10" marginwidth="10"  marginheight="10"></iframe>