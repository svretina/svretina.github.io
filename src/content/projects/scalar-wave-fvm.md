---
title: "ScalarWaveFVM.jl"
stack: ["Julia", "FVM"]
repoUrl: "https://github.com/svretina/ScalarWaveFVM.jl"
summary: "ScalarWaveFVM.jl is a numerical framework for computing the scalar self-force in general relativity with finite-volume methods. The project is designed around symmetry-reduced formulations of the wave equations, robust evolution near singular source structure, and numerically stable flux-based discretizations that can support precision self-force calculations on curved spacetimes. It serves as a research code for exploring both the physics and the numerics of self-force problems."
insights:
  - title: "Finite-volume structure is a robustness choice"
    body: "The code treats self-force evolution as a flux-based problem where local conservation and stable handling of sharp source structure matter more than relying on a purely formal high-order stencil. That makes the method a good fit for difficult curved-spacetime wave evolutions."
  - title: "Geometry and source treatment are designed together"
    body: "ScalarWaveFVM.jl is not positioned as a generic PDE sandbox. Its architecture is aimed at precision scalar-wave evolutions in general relativity, where coordinate choices, source regularization, and stable numerical fluxes have to work as one system."
links:
  - label: "arXiv"
    url: "https://arxiv.org/abs/2606.06487"
featured: true
order: 2
---
Numerical framework for scalar self force in general relativity using Finite Volume Method.
