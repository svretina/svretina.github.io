---
title: "FastTanhSinhQuadrature.jl"
stack: ["Julia", "Numerical Analysis", "Performance Optimization"]
repoUrl: "https://github.com/svretina/FastTanhSinhQuadrature.jl"
summary: "FastTanhSinhQuadrature.jl implements high-performance tanh-sinh quadrature in Julia for difficult one-, two-, and three-dimensional integrals, especially near endpoint or boundary singularities. The library combines the robustness of double-exponential quadrature with careful vectorization and low-level performance work, delivering large speedups over baseline implementations while preserving stringent accuracy targets. It is intended for workloads where both numerical reliability and throughput matter."
insights:
  - title: "Convergence remains strong near singular endpoints"
    body: "The repository’s convergence figure reflects why tanh-sinh is the right method for this class of problems: double-exponential node clustering reaches high accuracy quickly even when the integrand has difficult endpoint behavior."
    imageUrl: "https://raw.githubusercontent.com/svretina/FastTanhSinhQuadrature.jl/master/docs/src/assets/convergence.png"
    imageAlt: "Convergence plot from FastTanhSinhQuadrature.jl"
  - title: "The speedups come from algorithm and implementation"
    body: "The benchmark summary highlights that the performance gains are not only mathematical. SIMD-specialized kernels and cache reuse are layered on top of the quadrature method, which is what makes the library competitive across repeated integration workloads."
    imageUrl: "https://raw.githubusercontent.com/svretina/FastTanhSinhQuadrature.jl/master/docs/src/assets/benchmark_summary.png"
    imageAlt: "Benchmark summary plot from FastTanhSinhQuadrature.jl"
links:
  - label: "JOSS"
    url: "https://joss.theoj.org/papers/10.21105/joss.10076"
featured: true
order: 4
---
An AVX-optimized Julia library for fast Tanh-Sinh quadrature. Achieved up to 62x speedup in 1D, 35,700x in 2D, and successful microsecond-scale convergence in 3D boundary-singular integrals where competing libraries failed to meet tolerance.
