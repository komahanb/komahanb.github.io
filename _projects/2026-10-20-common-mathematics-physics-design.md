---
title: "Engineering a Lagrangian for Physics, Sensitivity, and Design"
permalink: /projects/common-mathematics-physics-design/
date: 2026-10-20
excerpt: "We construct a Lagrangian whose stationarity gives the motion, objective sensitivity, or design sought in a blade problem."
image: "/images/physics-design-illustration.png"
header:
  teaser: "physics-design-illustration.png"
comments: false
related: false
---

<link rel="stylesheet" href="{{ '/assets/css/lagrangian-note.css' | relative_url }}" />

Consider changing the thickness of a flexible rotor blade along its span. The change affects the blade's mass, its resistance to bending and twisting, and the stresses it experiences under load. To choose the thickness, we need to determine the resulting motion, assess whether the stresses are acceptable, and understand how both change when we alter the thickness.

These needs lead to three questions. Given a thickness distribution, how does the blade move? How does a measure of that motion or stress change with thickness? Which thickness distribution minimizes a chosen cost while meeting the motion and stress requirements?

We shall construct a *Lagrangian* to answer these questions. It is a scalar formed from the quantity we want to assess and the relations we require the blade to satisfy. We choose its terms so that requiring its first-order variation to vanish—its **stationarity**—gives the equations we need. The choice of what is prescribed, what is unknown, and what we want to improve determines the problem this scalar expresses.

<figure class="lagrangian-figure">
  <img src="{{ '/images/physics-design-illustration.png' | relative_url }}" alt="Conceptual illustration of oscillatory motion, a flexible blade, and swirling flow." width="1774" height="887" />
  <figcaption>An oscillator, a flexible blade, and a swirling flow give different physical meanings to the response fields and laws. We shall use their objectives and paired laws to construct each Lagrangian.</figcaption>
</figure>

## Describing the motion we need to determine

Let us first hold the blade's attachment fixed and consider small transverse bending. We begin by specifying the continuous domain on which we will describe this motion: its **manifold** $$\mathcal M$$. For a blade of length $$\ell$$ followed over a duration $$T$$, we take

<div class="math-display">
\[
\mathcal M=B\otimes I,
\qquad B=[0,\ell],\qquad I=[0,T].
\]
</div>

Here $$B$$ is the undeformed blade span, $$I$$ is the observation interval, and $$\otimes$$ denotes their product. This specifies the full span over the full interval of motion.

We choose coordinates on this manifold: $$x$$ measures position along the undeformed span, and $$t$$ measures time. We can then describe the motion by the transverse displacement $$w(x,t)$$, measured from the fixed, undeformed blade. This displacement is a **field** on $$\mathcal M$$.

The manifold's boundary faces tell us where to impose attachment and initial conditions. The root face, $$x=0$$, extends through the observation interval; the initial face, $$t=0$$, extends along the span. We impose the root attachment on the first and the starting displacement and velocity on the second.

More generally, a field assigns a physical quantity to each location on its manifold. For a quantity with $$m$$ real components, we write

<div class="math-display">
\[
u:\mathcal M\longrightarrow\mathbb R^m.
\]
</div>

The space $$\mathbb R^m$$ contains the possible component values. For the transverse displacement, $$u=w$$ and $$m=1$$.

Numerical nodes enter when we discretize the geometry. For this blade, we select span locations and time instants to obtain a discrete representation of $$\mathcal M$$. We then choose how to approximate the fields and their derivatives on that geometry. Specifying the manifold, discretizing its geometry, and choosing these approximations are separate decisions.

To determine inertia forces, we need the blade's acceleration. With the attachment fixed, differentiating $$w$$ with respect to time at a fixed span position gives transverse velocity and acceleration. To determine bending stresses, we need the curvature of the deformed blade. For small slopes, this is the second derivative of $$w$$ along the span.

We may keep these derivatives inside the equations, or give them separate names and require them to agree with derivatives of the displacement. Let $$v$$ denote transverse velocity, $$a$$ acceleration, $$\psi$$ slope, and $$\chi$$ curvature. Then

<div class="math-display">
\[
\begin{aligned}
\frac{\partial w}{\partial t}-v&=0,
&\frac{\partial v}{\partial t}-a&=0,\\
\frac{\partial w}{\partial x}-\psi&=0,
&\frac{\partial\psi}{\partial x}-\chi&=0.
\end{aligned}
\]
</div>

These equations make the five fields describe one consistent motion. Once we know the curvature, the cross-sectional geometry and material relations give the bending moment and bending stresses.

We shall use $$Q=(w,v,a,\psi,\chi)$$ as shorthand for these unknown fields together. Determining $$Q$$ means finding their values over the span and time interval.

## Writing the conditions that determine the response

The derivative relations do not yet determine the motion. We also need force balance, the applied load, the attachment conditions, and the starting displacement and velocity. For example, prescribing a starting deflection $$w_0(x)$$ requires

<div class="math-display">
\[
w(x,0)-w_0(x)=0
\qquad\text{along }B.
\]
</div>

The expression on the left measures departure from the requirement. We call such an expression a **residual**. Writing a condition as a vanishing residual lets us use the same construction for force balance, derivative relations, and prescribed data.

Suppose the thickness is described by design parameters $$s$$. We write the conditions determining the response in the common form

<div class="math-display">
\[
r_\alpha[Q,s](y)=0,\qquad y\in D_\alpha.
\]
</div>

The index $$\alpha$$ identifies a condition, and $$D_\alpha$$ tells us where it must hold. For a motion equation, $$D_\alpha$$ may be the whole space-time domain. For the starting displacement, it is the span at $$t=0$$. The notation $$r_\alpha[Q,s]$$ means that the residual depends on the response fields and thickness parameters, possibly through derivatives, boundary values, or integrals. The argument $$y$$ specifies where we evaluate it.

We use **law** for a required relation in this formulation, including the physical equations and the conditions selecting a particular response. A prescribed value in a law is its *datum*. Thus $$w_0(x)$$ is the datum in the starting-displacement law.

When a law holds a quantity to a prescribed value, we call it a **pin**. Prescribing thickness parameters as $$s_0$$ gives the pin $$s-s_0=0$$. Prescribing a field on a boundary face $$\Gamma$$ gives $$u\rvert_\Gamma-u_0=0$$, where $$u\rvert_\Gamma$$ means the value of $$u$$ on that face. We shall use the design pin later to ask how the response changes when we change the prescribed thickness.

## Constructing a scalar whose variations give these laws

Suppose we want the blade to follow a target motion. We can measure the squared difference between its displacement and the target, accumulated over the span and time interval. This gives one number, which we denote by $$J[Q,s]$$. Such a scalar quantity formed from fields is a *functional*. We use it as an objective when it expresses what we want to improve.

The objective alone does not require the blade to obey its motion equations. We need to include those equations in a way that makes stationarity return them. Consider the derivative law $$\partial w/\partial t-v=0$$. Introduce an unknown multiplier field $$\lambda_v(x,t)$$ and add the term

<div class="math-display">
\[
\int_0^T\!\int_B
\lambda_v(x,t)
\left(\frac{\partial w}{\partial t}-v\right)\,dx\,dt.
\]
</div>

Varying $$\lambda_v$$ whilst holding the other fields fixed makes the first variation equal to the integral of the residual times the multiplier variation. Requiring it to vanish for every admissible multiplier variation gives the derivative law. The multiplier therefore gives us a way to recover a required equation from a scalar.

For the starting-displacement law, we use a multiplier $$\lambda_0(x)$$ and add

<div class="math-display">
\[
\int_B\lambda_0(x)\bigl(w(x,0)-w_0(x)\bigr)\,dx.
\]
</div>

This integral is over the span because the initial condition applies at one time. Each law is paired with its multiplier where that law must hold.

We abbreviate such a contribution by $$\langle\lambda_\alpha,r_\alpha\rangle_{D_\alpha}$$. For scalar or vector residuals represented by ordinary functions,

<div class="math-display">
\[
\langle\lambda_\alpha,r_\alpha\rangle_{D_\alpha}
=\int_{D_\alpha}\lambda_\alpha(y)\cdot r_\alpha(y)\,d\mu_\alpha(y).
\]
</div>

The measure $$d\mu_\alpha$$ supplies the appropriate accumulation: along the span, through time, or over both. For a condition on finitely many parameters, the contribution is a dot product. More generally, the pairing means a linear action of the multiplier on the residual. Its units are chosen to make the contribution compatible with the objective.

Let $$\lambda$$ collect the law multipliers, and let the sum below contain the laws determining the response, including its initial and boundary conditions. With the design $$s$$ treated as prescribed for now, the Lagrangian is

<div class="math-display">
\[
\mathcal L[Q,s,\lambda]
=J[Q,s]
+\sum_\alpha\langle\lambda_\alpha,r_\alpha[Q,s]\rangle_{D_\alpha}.
\]
</div>

Variation in each multiplier gives its law. Variation in the response fields gives equations for the multipliers; we shall see that these equations allow us to differentiate the objective through the motion. Setting $$J=0$$ still recovers the response laws, and zero multipliers then satisfy the remaining stationarity equations once the response has been found.

## Finding how thickness changes the objective

We can now ask how the objective changes when we alter the thickness. Let $$Q(s)$$ denote the response satisfying the laws at design $$s$$. For example, its displacement component is $$w(x,t;s)$$. Changing $$t$$ follows one blade through its motion; changing $$s$$ compares the responses of different blade designs at the same position and time.

After determining the motion, the objective becomes a function of the design alone:

<div class="math-display">
\[
J(s)=J[Q(s),s].
\]
</div>

Here $$J(s)$$ means the objective evaluated after solving for the motion. Its total derivative $$dJ/ds$$ includes both the explicit effect of thickness and the effect caused by the changed motion. A partial derivative $$\partial J/\partial s$$ holds the response fields fixed. For several design parameters, $$dJ/ds$$ collects the total derivative with respect to each component.

Let $$R[Q,s]=0$$ collect the response laws, excluding the design pin. Assume the laws and objective are differentiable and that, near the response of interest, the linearized response equations determine a unique change in $$Q$$. A small design change $$\delta s$$ then gives

<div class="math-display">
\[
\begin{aligned}
\frac{\partial R}{\partial Q}\,\delta Q&=-\frac{\partial R}{\partial s}\,\delta s,\\
\delta J&=\frac{\partial J}{\partial Q}\,\delta Q+\frac{\partial J}{\partial s}\,\delta s.
\end{aligned}
\]
</div>

Here $$\partial R/\partial Q$$ is the linear operator that converts a small change in the response fields into the first-order change in the residuals. Each partial derivative holds the other arguments fixed. The first equation determines how the motion must change to continue satisfying the laws. Substituting that change into the second equation gives the objective sensitivity. This is the direct route.

If we need the derivative of one objective with respect to many thickness parameters, finding a separate response change for every parameter can be unnecessary. Instead, choose multipliers so that the terms involving $$\delta Q$$ cancel when we differentiate the Lagrangian. This gives

<div class="math-display">
\[
\begin{aligned}
\left(\frac{\partial R}{\partial Q}\right)^*\lambda&=-\frac{\partial J}{\partial Q},\\
\frac{dJ}{ds}&=\frac{\partial J}{\partial s}+\left(\frac{\partial R}{\partial s}\right)^*\lambda.
\end{aligned}
\]
</div>

The first equation is the **adjoint equation**. The star denotes the adjoint of the linear derivative under the chosen pairings: it transfers the derivative from a variation of the fields to the multiplier acting on that variation. This equation is exactly stationarity of $$\mathcal L$$ in $$Q$$. The second equation then gives the complete objective derivative without computing a response change for each design direction.

To read this derivative directly from a multiplier, now include the prescribed design as a law:

<div class="math-display">
\[
\mathcal L_{\mathrm{pin}}
=\mathcal L+\langle\lambda_s,s-s_0\rangle.
\]
</div>

We vary $$s$$ and $$\lambda_s$$ as well as the response fields and their multipliers. Variation in $$\lambda_s$$ enforces $$s=s_0$$. After the response and adjoint equations hold, variation in $$s$$ gives

<div class="math-display">
\[
\frac{dJ}{ds}+\lambda_s=0.
\]
</div>

The negative pin multiplier is therefore the derivative of the objective with respect to the prescribed thickness parameters. For a thickness field, the same statement gives a sensitivity distributed along the span, interpreted through its pairing with a thickness change.

The argument also tells us how to assess changes in prescribed loads or starting conditions. Replace a law $$r_\alpha=0$$ by $$r_\alpha-\varepsilon_\alpha=0$$, where $$\varepsilon_\alpha$$ is a change in its datum. If this datum enters only through that law and the stationary response varies differentiably with it, then

<div class="math-display">
\[
\delta J=-\langle\lambda_\alpha,\delta\varepsilon_\alpha\rangle_{D_\alpha}.
\]
</div>

For the initial-displacement law, this tells us how changing $$w_0(x)$$ changes the objective. The sign follows from writing the residual as the field value minus its datum. The multiplier's scale also depends on how we write the law: multiplying a residual by a nonzero constant divides its multiplier by that constant.

## Choosing thickness while respecting limits

Suppose we now want to determine the thickness instead of assessing a prescribed distribution. We remove the design pin and its multiplier, retain the response laws, and seek stationarity in $$s$$. The design equation becomes $$dJ/ds=0$$. For an unconstrained interior optimum, this is a necessary condition; stationarity alone does not establish a minimum.

<figure id="pinning-illustration" class="lagrangian-figure">
  <div class="lagrangian-panels lagrangian-panels--pinning">
    <a class="lagrangian-panel" href="{{ '/images/lagrangian-pinning.png' | relative_url }}"><img src="{{ '/images/lagrangian-pinning.png' | relative_url }}" alt="Pin imposed: a design is held away from the objective minimum to read its sensitivity." width="1774" height="887" loading="lazy" /></a>
    <a class="lagrangian-panel" href="{{ '/images/lagrangian-pinning.png' | relative_url }}"><img src="{{ '/images/lagrangian-pinning.png' | relative_url }}" alt="Pin removed: the same objective curve, with the design free to seek a stationary point." width="1774" height="887" loading="lazy" style="transform:translateX(-50%);" /></a>
  </div>
  <figcaption>We prescribe a design to obtain its objective sensitivity, or remove its pin to seek a stationary design. The curve shows J(s), evaluated after the motion has been determined.</figcaption>
</figure>

The objective must express what we want to achieve. For a light blade, it may be mass; for a blade following a prescribed motion, it may be the displacement error. The requirements specify which designs are acceptable.

Consider an upper limit on a specified stress measure. We write the constraint as that stress measure minus its allowable value, required to be nonpositive. If the stress is strictly below the limit, its inequality multiplier is zero. At the limit, the multiplier can contribute to the design equation. For finitely many differentiable constraints $$c_i(s)\leq0$$, evaluated after determining the motion, introduce a multiplier $$\eta_i$$ for each constraint. At a regular constrained minimum (for example, one with independent gradients of the active constraints), these quantities obey

<div class="math-display">
\[
\begin{gathered}
\nabla_s J+\sum_i\eta_i\nabla_s c_i=0,\\
c_i\leq0,\qquad\eta_i\geq0,\qquad\eta_i c_i=0.
\end{gathered}
\]
</div>

Here $$\nabla_s J$$ collects the objective derivatives with respect to the design parameters. The first equation balances them against the derivatives of the active limits. The remaining conditions require the limits to hold, the multipliers to be nonnegative, and each multiplier to vanish when its limit is inactive. A pointwise stress limit is imposed at each position and time where it must hold, with its multiplier on the same domain. Thickness bounds are imposed along the span.

We may also have a preferred thickness distribution without requiring it exactly. Let $$r=s-s_{\mathrm{preferred}}$$ measure departure from that preference. To penalize the departure, replace the exact pin term by

<div class="math-display">
\[
\langle\lambda,r\rangle
-\frac12\langle\lambda,W^{-1}\lambda\rangle.
\]
</div>

Here $$W$$ is a symmetric positive-definite, invertible weighting operator under the chosen pairing. Variation in $$\lambda$$ gives $$\lambda=Wr$$. Substituting this relation leaves the penalty $$\tfrac12\langle Wr,r\rangle$$. Increasing its weight makes departure from the preferred thickness more costly relative to the motion objective. This is a softened preference; an actual stress limit remains a separate requirement.

Thus the same thickness quantity can be prescribed, chosen subject to bounds, or guided by a preference. We specify the appropriate law or penalty for the question being asked. Removing any condition also requires checking that the remaining equations still determine the intended response.

## Checking whether a stationary design improves the objective

At a stationary design, the first derivative cannot tell us whether a small thickness change increases or decreases the objective. We need its second derivative. At an unconstrained stationary point, a positive-definite matrix of second derivatives (the Hessian) gives a strict local minimum. Constrained problems require the corresponding second-order test on admissible directions.

The pin multiplier gives a convenient way to obtain higher derivatives. For a scalar prescribed parameter $$s_0$$, the identity $$dJ/ds_0=-\lambda_s$$ implies

<div class="math-display">
\[
\frac{d^k J}{ds_0^k}
=-\frac{d^{k-1}\lambda_s}{ds_0^{k-1}},
\qquad k\geq1,
\]
</div>

provided the required derivatives exist. In particular, differentiating the pin multiplier once gives the objective's curvature. The derivatives come from differentiating the response and adjoint equations; they are not supplied by the value of the multiplier alone.

For several design parameters, we differentiate along chosen directions or form mixed derivatives. A separate question is how an *optimal design* changes with an allowable stress or another requirement. That requires differentiating the full optimality system. Smooth data, independent gradients of the active constraints, positive curvature on admissible directions, and positive multipliers on active inequalities provide a local setting in which this can be done. When the active constraints change, differentiability needs to be examined again.

## An oscillator: seeing the complete construction

Consider a displacement whose damping changes with the displacement itself. We want to know how the extent of its motion depends on the damping parameter. The nondimensional Van der Pol oscillator gives a compact example in which we can identify every field, law, and multiplier.

Let $$u(t)$$ be displacement, $$v(t)$$ velocity, $$a(t)$$ acceleration, and $$\nu$$ the damping parameter. Here the unknown response fields are $$Q=(u,v,a)$$ on $$I=[0,T]$$, and the design parameter is $$s=\nu$$. We label the motion residual $$r_\Omega$$ and collect the time-derivative residuals in $$r_t$$:

<div class="math-display">
\[
\begin{aligned}
r_\Omega&=a-\nu(1-u^2)v+u=0,\\
r_t&=\begin{pmatrix}
\partial u/\partial t-v\\
\partial v/\partial t-a
\end{pmatrix}=0.
\end{aligned}
\]
</div>

For positive $$\nu$$, the damping term feeds energy into small-amplitude motion and removes it when the displacement becomes sufficiently large. To select one trajectory, prescribe $$u(0)=u_0$$ and $$v(0)=v_0$$. We collect their residuals as $$r_{\mathrm{ic}}=(u(0)-u_0,v(0)-v_0)$$. To assess one damping value, add the design pin $$r_s=\nu-\nu_0=0$$.

Suppose we measure the motion by accumulating squared displacement and velocity:

<div class="math-display">
\[
J=\int_0^T\frac{u(t)^2+v(t)^2}{2}\,dt.
\]
</div>

We pair the motion law and derivative laws with multipliers over $$I$$. The initial conditions and the parameter pin contribute ordinary scalar products because each holds at a single point. Stationarity then gives the trajectory, the adjoint fields, and the objective sensitivity $$dJ/d\nu_0=-\lambda_s$$, where $$\lambda_s$$ is the multiplier of the pin $$s-s_0=\nu-\nu_0=0$$. The initial-condition multipliers give the sensitivities to $$u_0$$ and $$v_0$$ in the same way.

The figures below show which quantities each expression depends on. Following those dependencies explains how a variation of the same Lagrangian yields a response law, an adjoint equation, or a design equation.

<figure id="lagrangian-graph" class="lagrangian-figure">
  <a href="{{ '/images/lagrangian-figures/figure-1-lagrangian-graph.svg' | relative_url }}">
    <picture>
      <source media="(max-width: 640px)" srcset="{{ '/images/lagrangian-figures/figure-1-lagrangian-graph-mobile.svg' | relative_url }}" />
      <img src="{{ '/images/lagrangian-figures/figure-1-lagrangian-graph.svg' | relative_url }}" alt="Figure 1. The oscillator response fields and design feed the physical law, derivative relations, initial data, and objective. Each law has its own multiplier, and the terms form one Lagrangian." width="1000" height="610" loading="lazy" style="height:auto;" />
    </picture>
  </a>
  <figcaption><strong>Figure 1.</strong> The oscillator's response fields Q = (u, v, a) and design s = ν enter its laws and objective. Each residual is paired with a multiplier on the domain where the law holds. The dashed edge is used when J depends explicitly on s; it is absent for this objective.</figcaption>
</figure>

<figure id="stationarity-readings" class="lagrangian-figure">
  <div class="lagrangian-readings" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));gap:16px;">
    <a href="{{ '/images/lagrangian-figures/figure-2-response.svg' | relative_url }}"><img src="{{ '/images/lagrangian-figures/figure-2-response.svg' | relative_url }}" alt="Varying the response-law multipliers returns the laws that determine the response." width="480" height="440" loading="lazy" /></a>
    <a href="{{ '/images/lagrangian-figures/figure-2-adjoint.svg' | relative_url }}"><img src="{{ '/images/lagrangian-figures/figure-2-adjoint.svg' | relative_url }}" alt="Varying the response fields gives the adjoint equations for the response multipliers." width="480" height="440" loading="lazy" /></a>
    <a href="{{ '/images/lagrangian-figures/figure-2-sensitivity.svg' | relative_url }}"><img src="{{ '/images/lagrangian-figures/figure-2-sensitivity.svg' | relative_url }}" alt="Varying a pinned design determines the pin multiplier as the negative objective derivative." width="480" height="440" loading="lazy" /></a>
    <a href="{{ '/images/lagrangian-figures/figure-2-design.svg' | relative_url }}"><img src="{{ '/images/lagrangian-figures/figure-2-design.svg' | relative_url }}" alt="Releasing the pin sets its multiplier to zero; design stationarity then determines a candidate design." width="480" height="440" loading="lazy" /></a>
  </div>
  <figcaption><strong>Figure 2.</strong> Different variations of the same Lagrangian give the response laws, adjoint equations, and design equation. Here δℒ/δQ and δℒ/δλ denote variations in whole fields; ∂ℒ/∂s is the derivative with respect to the design parameter. The expressions using dJ/ds apply after the response and adjoint equations hold. The design pin is absent in the final panel.</figcaption>
</figure>

## A beam: using the construction along the span

Now consider a beam with fixed supports whose bending motion should follow a target displacement. Inertia depends on acceleration, while bending resistance depends on curvature. We use the fields $$Q=(w,v,a,\psi,\chi)$$ and the derivative relations introduced earlier, all on $$B\otimes I$$.

For small bending of an undamped Euler–Bernoulli beam, transverse force balance is

<div class="math-display">
\[
r_\Omega=\rho A\,a+
\frac{\partial^2(EI\chi)}{\partial x^2}-f=0.
\]
</div>

Here $$\rho A$$ is mass per unit length, $$EI$$ is bending stiffness, and $$f(x,t)$$ is the applied transverse load per unit length. We measure displacement in a fixed inertial frame. The bending moment $$EI\chi$$ supplies the spatial force term, and $$\rho A\,a$$ supplies inertia. Substituting the derivative relations gives the fourth-order spatial and second-order temporal equation for displacement.

We therefore prescribe starting displacement and velocity along the span, together with sufficient conditions at the ends. A stationary simply supported end has zero deflection and bending moment. A stationary clamped end has zero deflection and slope. These end conditions hold throughout the motion. Each enters the Lagrangian on the domain where it is required.

To isolate the effect of stiffness in this example, hold the mass per unit length and load fixed. Describe a family of stiffness distributions by

<div class="math-display">
\[
EI(x;s)=EI_0(1+s_1\xi+s_2\xi^2),
\qquad \xi=x/\ell,
\]
</div>

with a strictly positive stiffness requirement along the span. The two parameters control the linear and quadratic changes in stiffness. For a target displacement $$w_\star(x,t)$$, choose

<div class="math-display">
\[
J=\frac12\int_0^T\!\int_B
\bigl(w(x,t)-w_\star(x,t)\bigr)^2\,dx\,dt.
\]
</div>

Pinning $$s_1$$ and $$s_2$$ gives the sensitivity of this displacement error to each parameter. Removing their pins lets us seek a stiffness distribution that reduces the error whilst satisfying the response laws and stiffness requirement.

If the same beam must serve under two loads, give each load case its own response fields and laws. Retain one shared stiffness design and combine the two objective costs with chosen weights. The design equation then includes the contribution from both motions. For an actual thickness change, both area and stiffness generally change; the derivative must include both effects.

## Connected bodies: separating rigid motion from deformation

Return to the flexible blade attached to a rotating rigid hub. The hub can rotate without deforming, while the blade can bend relative to the hub. We must describe these motions separately before combining them.

For a hub rotating about a fixed axis, let $$\varphi(t)$$ be its angle. In a frame carried by the hub, let $$\mathbf r_0(x)$$ describe the undeformed blade and $$\mathbf u_e(x,t)$$ its elastic displacement. With a fixed hub centre $$\mathbf r_H$$, the absolute position of a blade point is

<div class="math-display">
\[
\mathbf r(x,t)=\mathbf r_H+
\mathbf C(\varphi(t))
\bigl(\mathbf r_0(x)+\mathbf u_e(x,t)\bigr).
\]
</div>

The rotation matrix $$\mathbf C(\varphi)$$ turns coordinates in the hub frame into coordinates in the fixed frame. For the transverse bending described earlier, $$w$$ is the transverse component of $$\mathbf u_e$$. Differentiating the complete position gives the velocity and acceleration used in inertia. Differentiating only the elastic displacement would omit contributions from the rigid rotation and its coupling with deformation.

For a blade clamped to the hub, elastic root displacement and rotation relative to the hub vanish. If the attachment is a hinge, any permitted relative rigid rotation has its own joint coordinate; the elastic displacement is then measured relative to the blade frame after that rotation. The attachment laws enforce the permitted connection and account for the reaction forces or moments.

To see how these reactions enter a variational description, consider several rigid bodies connected as a pendulum. Let $$q(t)$$ collect their positions and orientations, and let $$g_b(q,t,s)=0$$ express the joint conditions. For a conservative mechanical system, form the action

<div class="math-display">
\[
\mathcal A=\int_0^T\!
\left(K(q,\dot q,s)-V(q,s)
+\sum_b\eta_b\cdot g_b(q,t,s)\right)\,dt.
\]
</div>

The quantities $$K$$ and $$V$$ are kinetic and potential energy, and $$\dot q$$ is the time derivative of $$q$$. Each multiplier $$\eta_b(t)$$ acts on one joint condition. Variation in $$\eta_b$$ returns that condition; variation in $$q$$, with endpoint variations fixed, gives the equations of motion with joint reactions. Consistent initial positions and velocities select the trajectory.

Suppose we want the sensitivity of the last body's motion to the first body's inertia. We first obtain the mechanical equations from this action. We then use those equations, including the joint laws, as the response laws in a Lagrangian with the chosen motion objective. The joint multipliers are physical reactions among the unknowns of this response problem. The new multipliers give objective sensitivities to perturbations of its equations.

This returns us to blade design. For a specified material and cross-sectional form, thickness $$h(x)$$ determines the area and stiffness. To seek a light blade, we can use mass $$\int_B\rho A(h(x))\,dx$$ as the objective, impose the coupled motion and attachment laws, and require the stresses and thickness to satisfy their limits. A pin $$h-h_0=0$$ gives the objective sensitivity at one thickness distribution. Removing that pin permits thickness to be chosen subject to the remaining requirements.

If several operating conditions must be met, each has its own motion and stress fields. The thickness remains shared. Contributions from every operating condition therefore enter the same thickness equation.

## Using equations from one variational problem in the next

The connected-body example gives a reason to repeat the construction. Stationarity of a mechanical action gives equations for motion and reactions. A design question must preserve those equations while introducing an objective measuring that motion.

Let $$z$$ collect the unknowns at the first level, including any joint multipliers, and let $$\mathcal L_0[z;s]$$ be the scalar functional whose stationarity determines them. We collect its stationarity equations, together with the initial or boundary data needed to select a response, as $$F[z,s]=0$$. To assess that response with an objective $$J_1$$, form

<div class="math-display">
\[
\mathcal L_1[z,s,\mu]
=J_1[z,s]+\langle\mu,F[z,s]\rangle.
\]
</div>

The new multiplier collection $$\mu$$ has one member for each retained law. The pairing sums their contributions over the domains where those laws hold. Variation in $$\mu$$ enforces the first level's equations and data; variation in $$z$$ gives the adjoint equations for the new objective. We add a design pin or design constraints according to what is prescribed and what is sought.

The same step applies whenever the response to a new question is already defined by a stationary problem. Under the differentiability and invertibility assumptions used earlier, differentiating the response directly and reading the negative design-pin multiplier give the same objective derivative. That agreement is a mathematical check on the construction.

## Fluid motion: determining pressure as well as velocity

Consider an incompressible swirling flow, such as a Taylor–Green vortex. We want to know how viscosity affects the amount of motion that persists. The response now includes the velocity field $$\mathbf u(\mathbf x,t)$$ and the pressure divided by density, $$p(\mathbf x,t)$$, on a periodic spatial domain $$B$$ through time $$I$$.

For constant density and no body force, momentum balance and volume conservation require

<div class="math-display">
\[
\begin{gathered}
\partial_t\mathbf u
+(\mathbf u\cdot\nabla)\mathbf u
+\nabla p-\nu\Delta\mathbf u=0,\\
\nabla\cdot\mathbf u=0.
\end{gathered}
\]
</div>

Here $$\nu$$ is kinematic viscosity. The first equation balances acceleration against pressure and viscous effects; the second requires zero local volume expansion. We prescribe a divergence-free starting velocity and periodic conditions. We can retain velocity-gradient components as additional fields if useful, with equations requiring them to equal the corresponding derivatives.

These equations leave one quantity undetermined. Adding a spatially uniform value to pressure at any time leaves its gradient unchanged and therefore leaves the velocity equations unchanged. We select a unique pressure level by requiring

<div class="math-display">
\[
\int_B p(\mathbf x,t)\,d\mathbf x=0
\qquad\text{for each }t.
\]
</div>

This condition is essential before assuming a unique linearized response in the sensitivity argument. Its multiplier depends on time because there is one pressure-mean condition at each instant.

To measure the motion that persists, choose the accumulated squared speed

<div class="math-display">
\[
J=\frac12\int_0^T\!\int_B
\mathbf u\cdot\mathbf u\,d\mathbf x\,dt.
\]
</div>

The response laws now include momentum balance, volume conservation, initial data, periodicity, and the pressure-mean condition. Pairing them with multipliers and adding the viscosity pin $$\nu-\nu_0=0$$ gives the sensitivity of this objective to viscosity. The physical equations have changed; the multiplier construction answers the same kind of question.

## Changing controls, starting data, or geometry

Thickness is one quantity we can choose. If we instead seek an applied torque that produces a target motion, the torque becomes an unknown field of time. If we seek the starting displacement that best explains later observations, the initial displacement becomes unknown. The response laws remain, but the objective and the quantity being determined now express a control or inference question.

Changing the blade's span or the duration of observation requires another step. Different spans and durations give different domains, so we need to say which points we compare when taking a derivative. Introduce reference coordinates $$\xi,\tau\in[0,1]$$ and, for uniform scaling, write

<div class="math-display">
\[
x=\ell\xi,\qquad t=T\tau,\qquad
\widehat w(\xi,\tau)=w(\ell\xi,T\tau).
\]
</div>

The field $$\widehat w$$ describes the response on the same reference rectangle for every span and duration. At corresponding points, the chain rule gives

<div class="math-display">
\[
\frac{\partial w}{\partial x}
=\frac1\ell\frac{\partial\widehat w}{\partial\xi},
\qquad
\frac{\partial w}{\partial t}
=\frac1T\frac{\partial\widehat w}{\partial\tau},
\qquad
dx\,dt=\ell T\,d\xi\,d\tau.
\]
</div>

A span or duration change therefore affects both the derivatives in the motion laws and the integrals in the objective. These factors must be included when differentiating. For more general smooth, invertible maps $$x=x(\xi)$$ and $$t=t(\tau)$$ with positive derivatives, the same chain rule uses their local derivatives in place of $$\ell$$ and $$T$$.

The maps can themselves be treated as fields. Prescribing a map fixes the geometry or timing; allowing specified parts of it to vary asks for those features to be determined. The reference domain makes the comparison precise.

## Choosing one blade for uncertain loads

Suppose the load is uncertain. A thickness distribution that performs well for one load may perform poorly for another. We need to determine the response to the possible loads and choose how to combine those outcomes in the design objective.

Let $$\theta$$ identify a load realization, with possible values in $$\Theta$$ and prescribed probability density $$p_\Theta(\theta)$$. The displacement becomes $$w(\theta,x,t;s)$$. Its arguments identify the load, span position, and time, for the shared design $$s$$. The domain $$\Theta\otimes B\otimes I$$ is called **probabilistic space-time**.

<figure id="pst-illustration" class="lagrangian-figure">
  <div class="lagrangian-panels lagrangian-panels--pst">
    <a class="lagrangian-panel" href="{{ '/images/pst-field-dependence.png' | relative_url }}"><img src="{{ '/images/pst-field-dependence.png' | relative_url }}" alt="Along the blade: the response depends on position along its span." width="2172" height="724" loading="lazy" /></a>
    <a class="lagrangian-panel" href="{{ '/images/pst-field-dependence.png' | relative_url }}"><img src="{{ '/images/pst-field-dependence.png' | relative_url }}" alt="Through time: successive blade positions show its motion." width="2172" height="724" loading="lazy" style="transform:translateX(-33.333333%);" /></a>
    <a class="lagrangian-panel" href="{{ '/images/pst-field-dependence.png' | relative_url }}"><img src="{{ '/images/pst-field-dependence.png' | relative_url }}" alt="Across possible loads: one blade design has different responses under uncertain loads." width="2172" height="724" loading="lazy" style="transform:translateX(-66.666667%);" /></a>
  </div>
  <figcaption>The blade's displacement depends on span position, time, and the realized load. One thickness distribution is shared across all these responses.</figcaption>
</figure>

The thickness remains $$h(x)$$ for every realization. Allowing $$h(\theta,x)$$ would describe a design that changes after the load is known. For one manufactured blade, each load case has its own response fields and laws, but all cases use the same thickness.

Suppose we want to reduce both the average motion error and its variability. Let $$J(\theta;s)$$ be the objective after determining the response for load $$\theta$$. Its mean and variance are

<div class="math-display">
\[
\begin{aligned}
\overline J(s)
&=\int_\Theta J(\theta;s)p_\Theta(\theta)\,d\theta,\\
V_J(s)
&=\int_\Theta\bigl(J(\theta;s)-\overline J(s)\bigr)^2
p_\Theta(\theta)\,d\theta.
\end{aligned}
\]
</div>

The probability density supplies the weight in these integrals. We can choose $$\overline J+\beta V_J$$ as the objective, where $$\beta\geq0$$ sets the cost of variability and has units that make the two terms compatible. If stress limits must hold for every load in a specified set, we impose those limits separately; reducing a mean and variance does not enforce them.

To construct the Lagrangian before knowing the responses, let $$Q_\theta$$ collect the unknown fields for each realization and write $$J_\theta=J[Q_\theta,s]$$. Denote probability-weighted integration by $$\mathbb E_\theta$$. Then

<div class="math-display">
\[
\begin{aligned}
\mathcal L_U
&=\mathbb E_\theta[J_\theta]
+\beta\,\mathbb E_\theta
\bigl[(J_\theta-\mathbb E_\theta[J_\theta])^2\bigr]\\
&\quad+\mathbb E_\theta\!
\left[\sum_\alpha\langle\lambda_\alpha,r_\alpha\rangle_{D_\alpha}\right]
+\langle\lambda_s,s-s_0\rangle.
\end{aligned}
\]
</div>

Each residual and multiplier inside the expectation belongs to a particular load realization. The probability-weighted formulation enforces the response laws and their initial and boundary conditions except on sets of zero probability. Additional requirements over a specified load set are included on that set. The shared design pin appears once.

Stationarity gives the responses and adjoints across loads. The negative design-pin multiplier gives the derivative of the statistical objective. Removing that pin lets the shared thickness vary, with every load case contributing to the design equation.

If the probability density is independent of the design and differentiation under the integral is justified, the total derivatives are

<div class="math-display">
\[
\begin{aligned}
\frac{d\overline J}{ds}&=\mathbb E_\theta\!\left[\frac{dJ}{ds}\right],\\
\frac{dV_J}{ds}&=2\mathbb E_\theta\!\left[(J-\overline J)\frac{dJ}{ds}\right].
\end{aligned}
\]
</div>

The first averages the sensitivity from each load case. The second also weights each sensitivity by how far that case's cost lies from the mean. These are the two contributions needed to improve the statistical objective.

If we instead need the effect of changing a load parameter within one realization, we differentiate the response laws with respect to that parameter, holding position, time, and design fixed. Where this derivative exists, it can be retained as a field with its own derivative relation. The enlarged domain therefore supports both a description of possible responses and questions about their dependence on the load.

We began by choosing a blade's thickness. To assess one distribution, we prescribe it and determine the response and objective sensitivity. To choose a distribution, we state the objective and the limits it must meet. To accommodate uncertain loading, we keep one thickness and combine the consequences of many possible responses. In each case, constructing the Lagrangian makes these choices explicit: its terms state the question, and its stationarity gives the equations needed to answer it.
