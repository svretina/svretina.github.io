---
title: "PythiaBNS"
stack: ["Python", "Bayesian inference", "ML"]
repoUrl: "https://github.com/svretina/PythiaBNS"
summary: "PythiaBNS improves parameter estimation for gravitational-wave signals from binary neutron star merger remnants by combining empirical or physics-informed priors with machine-learning-assisted inference. The goal is to make post-merger analyses substantially faster without sacrificing the physical structure of the problem, enabling practical exploration of models that are otherwise too expensive for routine inference. The resulting workflow targets faster and more robust extraction of astrophysical information from gravitational-wave data."
insights:
  - title: "Empirical priors reshape the inference problem"
    body: "The important idea is not only to run a faster sampler, but to use physically informed priors so the posterior is easier to explore in the first place. That is what makes the advertised order-of-magnitude inference gains plausible rather than cosmetic."
  - title: "Posterior diagnostics are part of the workflow"
    body: "The repository includes automated plotting support, and the tutorial corner plot makes the posterior structure visible rather than opaque. That kind of diagnostic is important for checking how much the waveform model and priors are actually constraining the post-merger parameters."
    imageUrl: "https://raw.githubusercontent.com/svretina/PythiaBNS/main/docs/images/tutorial_corner_plot.png"
    imageAlt: "Tutorial corner plot from PythiaBNS"
links:
  - label: "arXiv"
    url: "https://arxiv.org/abs/2501.11518"
  - label: "PRD"
    url: "https://journals.aps.org/prd/abstract/10.1103/g1qs-j74x"
featured: true
order: 5
---
Improved parameter estimation for gravitational-wave models by ~10x using physics-informed priors and machine learning.
