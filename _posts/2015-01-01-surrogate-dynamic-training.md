---
categories: journals
title: "Unified Framework for Training Point Selection and Error Estimation for Surrogate Models"
image: "/files/2015-surrogate-dynamic-cover.png"
---

[AIAA Journal](https://arc.aiaa.org/journal/aiaaj);  Volume 53; Number 1; 2015

[https://arc.aiaa.org/doi/10.2514/1.J053064](https://arc.aiaa.org/doi/10.2514/1.J053064)

A unified framework for surrogate model training point selection and error estimation is proposed. Building auxiliary local surrogate models over subdomains of the global surrogate model forms the basis of the proposed  framework. A discrepancy function, defined as the absolute difference between response predictions from local and global surrogate models for randomly chosen test candidates, drives the framework, thereby not requiring any additional exact function evaluations. The benefits of this new approach are demonstrated with analytical test functions and the construction of a two-dimensional aerodynamic database. The results show that the proposed training point selection approach improves the convergence monotonicity and produces more accurate surrogate models compared to random and quasi-random training point selection strategies. The introduced root-mean-square discrepancy and maximum absolute discrepancy exhibit close agreement with the actual root-mean-square error and maximum absolute error, respectively, and are therefore proposed as a measure for the approximation accuracy of surrogate models in applications of practical interest. Multivariate interpolation and regression is employed to build local surrogates, whereas kriging and polynomial chaos expansions serve as global surrogate models in demonstrating the applicability of the proposed framework. 

![](/files/2015-surrogate-dynamic-cover.png)
<p align="center"><b>Figure:</b> The Kriging surrogate model of lift coefficient built using the developed method for adaptive training point selection for high-fidelity training data and random selection for low-fidelity training data.</p>

<iframe src="/files/2015-surrogate-dynamic-preprint.pdf" width="100%" height="500"  frameborder="yes" border="10" marginwidth="10"  marginheight="10"></iframe>
