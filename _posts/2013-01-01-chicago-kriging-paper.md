---
categories: conferences
title: "Building Aerodynamic Databases Using Enhanced Kriging Surrogate Models"
image: "/files/2013-chicago-kriging-cover.png"
---

AIAA Region III Student Conference, Chicago, Illinois, April 2013

Recently, we developed a variable-fidelity hybrid Kriging surrogate model1 that is enhanced by Multivariate Interpolation and Regression (MIR) and adaptive training point selection. We use MIR as a local surrogate model that guides the construction of the global Kriging surrogate. The adaptive training point strategy that we use adds training points at locations where the difference between local (MIR) and global (Kriging) surrogate predictions differ by a given threshold. The model is iteratively updated at these locations of greater uncertainty until convergence or a maximum number of evaluations has been reached. This approach helps us to monitor the progress of the surrogate model construction as well as eliminates unnecessary function evaluations in regions where the surrogate is already doing a good job approximating the exact function. In this paper, we demonstrate the use of our hybrid Kriging model for the construction of a two-dimensional aerodynamic database for a NACA 0012 airfoil in steady and inviscid transonic flow. We study the variations of its lift and drag coefficients for changes in Mach number (0.5 < M < 1.5) and angle of attack (0 ◦ < α < 5 ◦ ). For the purpose of validation of our hybrid surrogate, an “exact” database is obtained through Euler flow solves on a Cartesian mesh of 51×51 = 2601 equispaced nodes. The root mean square error (RMSE) between the exact and surrogate approximated coefficient values over the entire domain are calculated and used to compare the performances of ordinary Kriging approaches and our enhanced Kriging approach. We also investigate the use of variable-fidelity training points to build the surrogate even more efficiently.

![](/files/2013-chicago-kriging-cover.png)

<p align="center"><b>Figure:</b> The Kriging surrogate model of the lift coefficient is built using high and low fidelity training points. </p>

<iframe src="/files/2013-chicago-kriging-paper.pdf" width="100%" height="500"  frameborder="yes" border="10" marginwidth="10"  marginheight="10"></iframe>