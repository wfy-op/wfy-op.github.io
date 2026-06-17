---
layout: archive
title: "Thin-Film LN / LT Waveguide Research"
permalink: /research/waveguide/
author_profile: true
---

<p class="research-intro">
  This direction studies ridge waveguides in thin-film LiNbO3 and LiTaO3 using COMSOL FEM, with a focus on geometry-dependent mode dispersion, etch-depth sensitivity, and nonlinear phase matching. This work supported my undergraduate thesis on broadband nonlinear frequency conversion in thin-film lithium niobate.
</p>

<p class="research-backlink"><a href="{{ '/research/' | relative_url }}">Back to all research directions</a></p>

<section class="research-section" markdown="1">
## Mode Analysis and Phase Matching

<div class="research-section__summary" markdown="1">
During my undergraduate research at Shandong University, I studied ridge waveguides in thin-film LiNbO3 and LiTaO3 using **COMSOL FEM**. The focus was the coupling between waveguide geometry and effective-index dispersion, and how this determines phase-matching windows for nonlinear conversion.

Key outputs include:

- Geometry-aware mode and field analysis in 2D and 3D structures.
- Comparison of LN and LT platforms under unified parameter scans.
- Width and etch-depth sensitivity analysis for phase matching.
- Simulation support for an undergraduate thesis on broadband nonlinear frequency conversion in thin-film lithium niobate.
</div>
</section>

<section class="research-section" markdown="1">
## Representative Findings

<div class="highlight-grid">
  <article class="highlight-card">
    <h2>Etch depth changes the phase-matching window</h2>
    <p>Increasing etch depth shifts the fundamental-mode effective-index curve and makes higher-frequency modes more separated, so etch depth becomes a direct design variable rather than only a fabrication detail.</p>
  </article>
  <article class="highlight-card">
    <h2>LN and LT differ through birefringence</h2>
    <p>The comparison between LiNbO3 and LiTaO3 showed how ordinary and extraordinary refractive-index differences change mode curvature, crossing behavior, and nonlinear frequency-conversion opportunities.</p>
  </article>
  <article class="highlight-card">
    <h2>Width scans need physical interpretation</h2>
    <p>Waveguide-width sweeps did not always produce a simple monotonic design rule, which pushed the analysis toward mode identity, periodic poling, and phase-matching mechanisms rather than brute-force plotting.</p>
  </article>
</div>
</section>

<section class="research-section" markdown="1">
## Training Value for Current PCSEL Work

<div class="workstream-panel" markdown="1">
This project trained the workflow I now use in PCSEL research: build a stable simulation model, sweep parameters deliberately, interpret field profiles through device physics, and connect geometry changes to measurable performance. The same discipline carries over from effective-index and phase-matching analysis to PCSEL band/mode analysis, Q-factor interpretation, and fabrication-aware design.
</div>
</section>

<section class="research-section" markdown="1">
## Representative Figures

<div class="research-media-grid">
  <figure class="research-figure">
    <img src="{{ '/images/research/waveguide_geometry.png' | relative_url }}" alt="Waveguide geometry" loading="lazy">
    <figcaption>Ridge waveguide geometry used for simulation and analysis.</figcaption>
  </figure>
  <figure class="research-figure">
    <img src="{{ '/images/research/waveguide_comsol_field_map.png' | relative_url }}" alt="COMSOL field map" loading="lazy">
    <figcaption>Representative COMSOL field map in a ring-waveguide structure.</figcaption>
  </figure>
  <figure class="research-figure">
    <img src="{{ '/images/research/waveguide_phase_matching_ln_lt.png' | relative_url }}" alt="Phase matching comparison" loading="lazy">
    <figcaption>Phase-matching comparison between LN and LT material systems.</figcaption>
  </figure>
</div>
</section>
