import json
import os
import re

# Output directory
output_dir = "src/content/projects"
os.makedirs(output_dir, exist_ok=True)

try:
    with open('repos.json', 'r') as f:
        data = json.load(f)

    if isinstance(data, dict) and 'message' in data:
        print(f"Error from GitHub API: {data['message']}")
        exit(1)

    targets = ['Julia', 'Python', 'C', 'Fortran']
    projects = []

    for repo in data:
        name = repo.get('name', '')
        language = repo.get('language', '')
        description = repo.get('description', '')
        is_fork = repo.get('fork', False)
        html_url = repo.get('html_url', f"https://github.com/svretina/{name}")

        if language not in targets:
            continue
        if is_fork:
            continue
        if name.startswith('.'):
            continue
        if 'github.io' in name:
            continue
        if not description:
            continue

        projects.append({
            "name": name,
            "language": language,
            "description": description,
            "url": html_url
        })

    # Keep top 8
    if len(projects) > 8:
        projects = projects[:8]

    # Add manual entries
    # 1. SphericalSummationByPartsOperators.jl
    projects.append({
        "name": "SphericalSummationByPartsOperators.jl",
        "language": "Julia",
        "description": "Developing stable, high-order **Summation-By-Parts (SBP)** operators for spherical coordinates, with a focus on resolving the coordinate singularity at r=0.",
        "url": "https://github.com/svretina/SphericalSummationByPartsOperators.jl"
    })
    
    # 2. ScalarWaveFVM.jl
    projects.append({
        "name": "ScalarWaveFVM.jl",
        "language": "Julia",
        "description": "Scalar Wave Finite Volume Method implementation in Julia.",
        "url": "https://github.com/svretina/ScalarWaveFVM.jl"
    })

    # Generate files
    filename_map = {
        "SphericalSummationByPartsOperators.jl": "spherical-sbp.md",
        "ScalarWaveFVM.jl": "scalar-wave-fvm.md",
        "TOV.jl": "tov.md",
        "FastTanhSinhQuadrature.jl": "tanhsinh.md"
    }

    for i, project in enumerate(projects):
        order = i + 1
        name = project['name']
        
        if name in filename_map:
            filename = f"{output_dir}/{filename_map[name]}"
        else:
            # Create kebab-case filename
            safe_name = re.sub(r'[^a-zA-Z0-9]', '-', name.lower()).strip('-')
            filename = f"{output_dir}/{safe_name}.md"
        
        content = f"""---
title: "{name}"
stack: ["{project['language']}"]
repoUrl: "{project['url']}"
featured: true
order: {order}
---
{project['description']}
"""
        with open(filename, "w") as out:
            out.write(content)
        print(f"Generated {filename}")

except Exception as e:
    print(f"Error: {e}")
