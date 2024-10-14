---
title: "Computational Infrastructure for Optimization Under Uncertainty" 
image: "files/ouu-span.png" 
---



<figure style="width: 300px; text-align: center;">    <img src="https://www.toolshero.com/wp-content/uploads/2022/08/genichi-taguchi-toolshero.jpg" alt="G. Taguchi" style="width: 100%;"> 
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

Even within the realm of aerospace engineering, I believe optimization under uncertainty represents a truly vast context: 

>  The simplest route to conceive this complexity is to view the subject matter as mathematically segmented domains of space (3-dimensional), time (1-dimensional), probability (N-dimensional), and an overarching engineering design domain (M-dimensional), with interactions among these domains.
