---
title: "SphericalSBPOperators.jl"
stack: ["Julia", "Numerical Analysis", "Performance Optimization"]
repoUrl: "https://github.com/svretina/SphericalSBPOperators.jl"
summary: "SphericalSBPOperators.jl develops stable high-order summation-by-parts finite-difference operators for spherical and general curvilinear coordinates, with special attention to coordinate singularities such as the origin. The project provides a framework for constructing discrete operators that preserve continuum energy estimates, reduce symmetry-reduced evolution problems to lower-dimensional domains, and retain high-order accuracy without giving up stability at singular points. In practice, that makes it possible to solve hyperbolic PDEs in geometries that would otherwise require a far more expensive full 3D Cartesian discretization."
insights:
  - title: "Symmetry reduction changes the computational regime"
    body: "The main payoff is dimensional reduction rather than a marginal constant-factor speedup. By building stable operators directly in spherical and curvilinear coordinates, the project targets problems where symmetry can be exploited without giving up rigorous stability arguments."
  - title: "The origin is handled through operator design"
    body: "A central numerical insight is that the r = 0 singularity should be treated as part of the discretization problem itself. The SBP construction is designed to retain discrete energy estimates and high-order accuracy even in the presence of singular coordinate structure."
links:
  - label: "arXiv"
    url: "https://arxiv.org/abs/2606.05155"
  - label: "Talk"
    url: "https://www.youtube.com/watch?v=Ji54w4Ks5PE"
featured: true
order: 1
---
High-order numerical operators for spherical and curvilinear coordinates, enabling symmetry-reduced simulations with theoretical O(N^2) speedups and memory reductions over full 3D Cartesian discretizations.
