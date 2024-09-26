---
categories: "thesis"
title: "Adjoint Based Design Optimization of Systems with Time Dependent Physics and Probabilistically Modeled Uncertainties"
image: "/files/2020-komahan-boopathy-gatech-phd-cover-rotor-opt.png"
---

Ph.D. Dissertation; School of Aerospace Engineering, Georgia Institute of Technology, Atlanta, Georgia, 2020

---

### Presentation

<iframe src="/files/2020-komahan-boopathy-gatech-phd-thesis-talk.pdf#view=FitH" width="100%" height="750" frameborder="0"></iframe> 

### Dissertation

<iframe src="/files/2020-komahan-boopathy-gatech-phd-thesis.pdf#view=FitH" width="100%" height="750" frameborder="0"></iframe> 

### Summary 

![](/files/2020-komahan-boopathy-gatech-phd-cover-1.png)

<p align="center"><b>Figure:</b> Time dependent physics in aerospace and civil engineering applications. </p>

For aerospace structures, failure can occur not only because of static adversities like divergence, but also due to time dependent issues like flutter and large vibrations. Therefore, the consideration of time-domain physics becomes essential during design. The physics-based design of aerospace systems involves solving partial differential equations to obtain metrics of interest that guide the design process. These differential equations contain unknown parameters that are sometimes difficult to be characterized as a deterministic value. The uncertainties in input parameters have a direct impact on the output metrics of interest which guide the system design process. To this end, optimization under uncertainty has evolved as a field that accounts for the effect of uncertainties, by propagating the effect of uncertainties through physics simulations. 

![](/files/2020-komahan-boopathy-gatech-phd-cover-ouu.png)

<p align="center"><b>Figure:</b> The evolution of optimization under uncertainty from deterministic optimization. </p>

For numerical optimization, the algorithms that do not use gradient information become computationally intractable as the number of design variables increases. Moreover, the numerical approximations of the gradients through the finite-difference or the complex-step methods are inefficient, for their lack of scalability with respect to the number of design variables. Therefore, efficient gradient evaluation techniques such as the adjoint method are needed for solving large scale optimization problems with practical turnaround times. However, because of the inclusion of time dependent physics, the corresponding time dependent adjoint equations needs to be formulated and implemented. Furthermore, the uncertainties need to be propagated through the time dependent physics and the adjoint sensitivity analysis framework. Due to the inherent complexities in the development of time domain physics and adjoint sensitivities analysis capabilities, the sampling-based methods are widely used for the propagation of uncertainties while the projection-based methods are less used. 

![](/files/2020-komahan-boopathy-gatech-phd-cover-propagation.png)

<p align="center"><b>Figure:</b> The propagation of uncertainties through physics and adjoint frameworks.</p>

This work presents enhanced implicit time marching methods for flexible multibody dynamics, to analyze the time dependent behavior of aerospace structures, and formulates the corresponding time dependent adjoint sensitivity analysis equations, to efficiently optimize designs using gradient based methods. The adjoint-based design capabilities are demonstrated with the structural optimization of a rotorcraft hub system. 

![](/files/2020-komahan-boopathy-gatech-phd-cover-rotor-opt.png)

<p align="center"><b>Figure:</b> The rotocraft model subject to adjoint based optimization.</p>

A newly developed semi-intrusive approach for projection is shown to fully reuse the underlying time-domain analysis and adjoint sensitivity analysis capabilities, for the projection-based propagation of uncertainties. Using this method, the stochastic residuals and Jacobians are formed implicitly from the deterministic counterparts that have been implemented apriori. 

![](/files/2020-komahan-boopathy-gatech-phd-cover-sfem.png)

<p align="center"><b>Computational Framework for UQ-OUU :</b> Open Source Packages.</p>

The application of the semi-intrusive projection method is shown using a flexible robotic manipulator system modeled after the Canadarm. In the presence of uncertainties in the payloads, the Canadarm system experiences stresses that have a large variability. This work demonstrates the use of uncertainty quantification as a valuable tool for assessing the risk associated with such operating conditions.  

![](/files/2020-komahan-boopathy-gatech-phd-cover-canadarm.png)

<p align="center"><b>Figure:</b> The Canadarm system and its simplified finite element model used for optimization under uncertainty.</p>
