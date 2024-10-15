---
title: "Computational Sensitivity Analysis Methods for Gradients and Hessians" 
image: "/files/images/"
---

<figure style="width: 300px; text-align: center;">    <img src="https://mathshistory.st-andrews.ac.uk/Biographies/Lanczos/Lanczos_4.jpeg" alt="C. Lanczos" style="width: 100%;"> 
<figcaption style="font-size: 1.0em;">... the idea of enlarging reality by including “tentative” possibilities and then selecting one of these by the condition that it minimizes a certain quantity, seems to bring purpose to the flow of natural events. <b>Cornelius Lanczos [1893–1974] </b></figcaption>
</figure>
My research along this trajectory is development of methods for calculating accurate gradients in a scalable manner -- to the number of design variables, as well as to the number of metrics of interest. 

![](/files/derivative-methods.png)

**The Adjoint Method**

My main interest is on the adjoint-based methods for sensitivity analysis. It offers scalability in terms of the number of design variables. I have focused on formulating and implementing time-dependent sensitivity analysis methods with several order agnostic multi-step and multi-stage time integrators in deterministic space time. This exercise has also been carried out in the probabilistic space time where without an explicit implementation of the stochastic adjoint, the adjoint fields are solved implicitly to assemble the adjoint gradient of statistics.

> Although the time-marching schemes come with various stencils, the overarching structure that is common to all methods is that the partial derivatives of the residuals and functions are combined using different weights to implement discrete adjoint methods. 

**Higher-Dimensional Numbers Based On Algebraic Structures and Differential Operators**

I also consider other possibilities to obtain design variable derivatives. I study the construction of higher-dimensional numbers that can provide first, second, and other higher-order derivatives, if necessary. This research is building upon the observations from complex-number arithmetics to four-dimensional numbers.
