---
title: "About"
permalink: /
author_profile: true
redirect_from: 
  - /about
  - /about.html
---

My passion lies in crafting simulation frameworks that model and analyze the equilibrium of aerospace vehicle components with the environmental surroundings, and provide means for design improvement through statistics of quantities of interest and their sensitivities to design variable perturbations. Thus, I undertake as well as take-part in the development of scalable, flexible and robust computational frameworks for scientific computing and targeted applications in aerospace vehicle design contexts such as fixed-wing aircrafts, rotorcrafts and space system robotic arms. 

| ![](../images/fixedwing.png) | ![](../images/rotorcraft.png) | ![](../images/spaceshuttle.png) |
| :--------------------------: | :---------------------------: | :-----------------------------: |
|       Aircraft Design        |       Rotorcraft Design       |      Space Systems Design       |



I work as a Senior Research Engineer at ANSYS, focused on the development activities of the Fluent GPU solver offering [orders of magnitude speed-up, and energy savings](https://www.ansys.com/blog/unleashing-the-full-power-of-gpus-for-ansys-fluent) over classical CPU-based HPC in the context of computational fluid dynamics (CFD) simulations. 

## Graduate Research

I hold a Ph.D. in Aerospace Engineering from the Georgia Institute of Technology, working as a research assistant in the [SMDO laboratory](https://gkennedy.gatech.edu/) led by [Prof. Graeme Kennedy](https://scholar.google.com/citations?user=LHqGhxkAAAAJ&hl=en). 

- I concentrated on the development of a computational [flexible multibody dynamics solver](https://github.com/smdogroup/tacs) with adjoint sensitivity analysis capabilities for the NASA Langley Research Center's [rotorcraft design applications](https://www.youtube.com/watch?v=-HM0KycBvnA), offering scalability benefits in the context of solving large-scale optimization problems.
- This deterministic computational framework was then naturally extended into an [adjoint-enabled stochastic finite-element, flexible multibody dynamics framework](https://github.com/komahanb/stacs). The stochastic framework is capable of providing statistical information on quantities of interest and adjoint gradient of statistics.

I also hold a Master's degree in Aerospace Engineering from the University of Dayton working as a research assistant in [Prof. Markus Rumpfkeil's](https://scholar.google.com/citations?user=zCRdVjYAAAAJ&hl=en) CFD laboratory.

-  I focused on the development of methods for aerodynamic optimization under uncertainty using surrogate models, as well as adaptive means for model error-estimation and training-point-selection. 

For more detailed information, the theses and associated presentations shall be accessed below:

| Degree | Program               | School                          | Year         | Thesis                                                       | Slides                                                       |
| ------ | --------------------- | ------------------------------- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Ph.D   | Aerospace Engineering | Georgia Institute of Technology | 2015 -- 2020 | [Adjoint Based Design Optimization of Systems with Time Dependent Physics and Probabilistically Modeled Uncertainties](http://hdl.handle.net/1853/63658) | <a href="../files/publications/komahan-boopathy-phd-defense.pdf"><img src="../files/phd-defense-slides-cover.png" alt="Slides Cover" style="width:100px;"></a> |
| M.S    | Aerospace Engineering | University of Dayton            | 2012 -- 2014 | [Uncertainty Quantification and Optimization Under Uncertainty Using Surrogate Models](http://rave.ohiolink.edu/etdc/view?acc_num=dayton1398302731) | <a href="../files/publications/komahan-boopathy-masters-defense.pdf"><img src="../files/masters-defense-slides-cover.png" alt="Slides Cover" style="width:100px;"></a> |
| B.Tech | Aerospace Engineering | SRM University                  | 2008 -- 2012 | --                                                           | --                                                           |

[Curriculum Vitae (PDF)](../files/KomahanBoopathyCV.pdf)

<iframe src="../files/KomahanBoopathyCV.pdf" width="100%" height="500"  frameborder="yes" border="10" marginwidth="10"  marginheight="10"></iframe>

### [Adjoint Based Design Optimization of Systems with Time Dependent Physics and Probabilistically Modeled Uncertainties](../files/2020-komahan-boopathy-gatech-phd-thesis.pdf) 

*Ph.D. Dissertation; School of Aerospace Engineering, Georgia Institute of Technology, Atlanta, Georgia, 2020*


![](../files/2020-komahan-boopathy-gatech-phd-cover-1.png)

<p align="center"><b>Figure:</b> Time dependent physics in aerospace and civil engineering applications. </p>

For aerospace structures, failure can occur not only because of static adversities like divergence, but also due to time dependent issues like flutter and large vibrations. Therefore, the consideration of time-domain physics becomes essential during design. The physics-based design of aerospace systems involves solving partial differential equations to obtain metrics of interest that guide the design process. These differential equations contain unknown parameters that are sometimes difficult to be characterized as a deterministic value. The uncertainties in input parameters have a direct impact on the output metrics of interest which guide the system design process. To this end, optimization under uncertainty has evolved as a field that accounts for the effect of uncertainties, by propagating the effect of uncertainties through physics simulations. 

![](../files/2020-komahan-boopathy-gatech-phd-cover-ouu.png)

<p align="center"><b>Figure:</b> The evolution of optimization under uncertainty from deterministic optimization. </p>

For numerical optimization, the algorithms that do not use gradient information become computationally intractable as the number of design variables increases. Moreover, the numerical approximations of the gradients through the finite-difference or the complex-step methods are inefficient, for their lack of scalability with respect to the number of design variables. Therefore, efficient gradient evaluation techniques such as the adjoint method are needed for solving large scale optimization problems with practical turnaround times. However, because of the inclusion of time dependent physics, the corresponding time dependent adjoint equations needs to be formulated and implemented. Furthermore, the uncertainties need to be propagated through the time dependent physics and the adjoint sensitivity analysis framework. Due to the inherent complexities in the development of time domain physics and adjoint sensitivities analysis capabilities, the sampling-based methods are widely used for the propagation of uncertainties while the projection-based methods are less used. 

![](../files/2020-komahan-boopathy-gatech-phd-cover-propagation.png)

<p align="center"><b>Figure:</b> The propagation of uncertainties through physics and adjoint frameworks.</p>

This work presents enhanced implicit time marching methods for flexible multibody dynamics, to analyze the time dependent behavior of aerospace structures, and formulates the corresponding time dependent adjoint sensitivity analysis equations, to efficiently optimize designs using gradient based methods. The adjoint-based design capabilities are demonstrated with the structural optimization of a rotorcraft hub system. 

![](../files/2020-komahan-boopathy-gatech-phd-cover-rotor-opt.png)

<p align="center"><b>Figure:</b> The rotocraft model subject to adjoint based optimization.</p>

A newly developed semi-intrusive approach for projection is shown to fully reuse the underlying time-domain analysis and adjoint sensitivity analysis capabilities, for the projection-based propagation of uncertainties. Using this method, the stochastic residuals and Jacobians are formed implicitly from the deterministic counterparts that have been implemented apriori. 

![](../files/2020-komahan-boopathy-gatech-phd-cover-sfem.png)

<p align="center"><b>Computational Framework for UQ-OUU :</b> Open Source Packages.</p>

The application of the semi-intrusive projection method is shown using a flexible robotic manipulator system modeled after the Canadarm. In the presence of uncertainties in the payloads, the Canadarm system experiences stresses that have a large variability. This work demonstrates the use of uncertainty quantification as a valuable tool for assessing the risk associated with such operating conditions.  

![](../files/2020-komahan-boopathy-gatech-phd-cover-canadarm.png)

<p align="center"><b>Figure:</b> The Canadarm system and its simplified finite element model used for optimization under uncertainty.</p>

---

### [Uncertainty Quantification and Optimization Under Uncertainty Using Surrogate Models](../files/2014-komahan-boopathy-masters-thesis.pdf)

*Masters Thesis; Department of Mechanical and Aerospace Engineering, University of Dayton, Dayton, Ohio, 2014*

Surrogate models are widely used as approximations to exact functions that are computationally expensive to evaluate. The choice of model training information and the estimation of the accuracy of surrogate models are major research avenues. In this work, a unified dynamic framework for surrogate model training point selection and error estimation is proposed. Building auxiliary local surrogate models over sub-domains of the global surrogate model forms the basis of the framework. A discrepancy function, defined as the absolute difference between response predictions from global and local surrogate models for randomly chosen test candidates, drives the framework.

The framework preferably evaluates the expensive exact function at locations, where the value of the discrepancy function is high and when a distance-constraint to previously existing training points are satisfied. As a result, the surrogate model is continually refined in regions of higher uncertainty in prediction, and a better spread of training points is also achieved. Unlike most training point selection approaches, the framework addresses surrogate training from two disparate contexts, as training in the presence and absence of derivative information. The local surrogate models use the derivative information when available and affect the framework via the discrepancy function, and helps determine the locations that require derivative information. The benefits of the dynamic training approach are demonstrated with analytical test functions and the construction of a two-dimensional aerodynamic database. The results show that the proposed method improves the convergence monotonicity and produces more accurate surrogate models, when compared to random and quasi-random training point selection strategies.

![](../files/drag-local-global-discrepancy)

<p align="center"><b>Figure:</b>The local surrogate model has orders of magnitude higher errors (left) in aerodynamic drag prediction than the main surrogate model error (middle), yet the difference between the two (right) effectively guides the training point selection process by systematically placing training points from the transonic regime of physics with higher nonlinearity in the parameter space.</p>

![](../files/drag-exact-global-contour.png)

<p align="center"><b>Figure:</b>The exact drag function (left) and the approximated drag function (right) contructed using a few training points selected dynamically.</p>

The newly introduced discrepancy function is proposed as an approximation to the actual error in the prediction of the surrogate model leading to the quantities: root mean square discrepancy (RMSD) and maximum absolute discrepancy (MAD). The results demonstrate a close agreement of RMSD and MAE with the actual root mean square error (RMSE) and maximum absolute error (MAE), respectively. Therefore, RMSD and MAD are proposed as measures for the accuracy of the surrogate models in applications of practical interest. The benefit of surrogate validation comes without warranting any additional exact function evaluations, which makes the framework computationally viable.

Multivariate interpolation and regression model is employed to build local surrogates, whereas the kriging and polynomial chaos expansions serve as global surrogate models. This demonstrates the applicability of the proposed framework to any surrogate model with an open choice of training data selection.

Finally, the dynamically trained surrogate models are applied to uncertainty quantifications and optimizations under mixed epistemic and aleatory uncertainties (OUU), for structural and aerodynamic test cases. In the OUUs epistemic uncertainties are propagated via box-constrained optimizations, whereas the aleatory uncertainties are propagated via inexpensive sampling of the surrogate models. The structural test cases include designing a three-bar truss and a cantilever beam, whereas the aerodynamic test case involves the robust optimization (lift-constrained drag minimization) of an airfoil under steady flow conditions.  

![](../files/2014-surrogate-robust-airfoil-shape-cover.png)

<p align="center"><b>Figure:</b> The optimized airfoil shapes produced using the developed optimization under uncertainty framework, shows improvement in lift distribution qualities in comparison to the deterministic design. </p>
