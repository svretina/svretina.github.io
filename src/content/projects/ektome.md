---
title: "Ektome"
stack: ["Python", "HTCondor", "Bash/Linux", "Git (CI/CD)"]
repoUrl: "https://github.com/svretina/Ektome"
summary: "Ektome is an HPC automation system for large Einstein Toolkit simulation campaigns on HTCondor infrastructure. It coordinates preprocessing, submission, monitoring, restart handling, data movement, and post-processing across very large job sets, with an emphasis on reliability under real cluster conditions. The pipeline was built to scale to more than one hundred thousand simulations while keeping the operational workflow reproducible and manageable."
insights:
  - title: "The result is operational scale, not just scripting convenience"
    body: "Ektome was built for simulation campaigns large enough that ad hoc shell scripting stops being viable. Submission, monitoring, restart logic, and post-processing are treated as one automation layer so six-figure job counts remain manageable."
  - title: "Reliability dominates at HTCondor scale"
    body: "For large campaigns, the engineering bottleneck is often workflow fragility rather than raw compute. The project’s value is in making simulation studies reproducible, restartable, and inspectable so cluster failures do not dominate the human cost of the work."
featured: true
order: 3
---
Python-based automation pipeline that processed 100,000+ simulations on HPC systems (HTCondor), with robust job orchestration and post-processing.
