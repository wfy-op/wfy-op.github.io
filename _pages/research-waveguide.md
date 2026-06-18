---
layout: archive
title: "LN/LT Waveguide Research"
permalink: /research/waveguide/
author_profile: true
---

<p class="research-backlink"><a href="{{ '/research/' | relative_url }}">Back to all research directions</a></p>

<section class="research-section" markdown="1">
## Thin-Film LN/LT Waveguide Mode Analysis

<div class="research-section__summary" markdown="1">
From 2024.01 to 2025.06, I worked with Prof. Lei Wang at the School of Physics, Shandong University on mode analysis and phase-matching problems in thin-film lithium niobate and lithium tantalate waveguides on insulator. This project trained the simulation habits that later transferred into my PCSEL work: define geometry carefully, extract mode indices consistently, compare material platforms, and connect parameter sweeps back to physical phase-matching conditions.
</div>

<div class="highlight-grid">
  <article class="highlight-card">
    <h2>Mode and geometry sweep</h2>
    <p>Built COMSOL finite-element models for ridge waveguides and scanned width, etch depth, film thickness, and material platform to track effective refractive index and modal confinement.</p>
  </article>
  <article class="highlight-card">
    <h2>Phase-matching window</h2>
    <p>Compared lithium niobate and lithium tantalate waveguides under quasi-phase-matching assumptions, focusing on how geometry and material dispersion shift the accessible wavelength window.</p>
  </article>
  <article class="highlight-card">
    <h2>Transfer to PCSEL practice</h2>
    <p>The project strengthened my habit of treating parameter sweeps as physical arguments rather than image generation: every mode plot, effective index, and phase-matching curve needs a geometry convention and a solver setting.</p>
  </article>
</div>
</section>

<section class="research-section" markdown="1">
## Representative Figures

<div class="research-media-grid">
  <figure class="research-figure">
    <img src="{{ '/images/research/waveguide_geometry.png' | relative_url }}" alt="Thin-film LN/LT ridge waveguide geometry used for mode and phase-matching analysis" loading="lazy" width="762" height="564">
    <figcaption><span class="evidence-badge">Geometry schematic</span><strong>Waveguide geometry.</strong> The model defines the ridge width, etch depth, film thickness, cladding/substrate context, and material platform before comparing optical modes or phase-matching behavior.</figcaption>
  </figure>
  <figure class="research-figure">
    <img src="{{ '/images/research/waveguide_comsol_field_map.png' | relative_url }}" alt="COMSOL optical mode field map for a thin-film LN/LT waveguide" loading="lazy" width="1183" height="887">
    <figcaption><span class="evidence-badge evidence-badge--quant">Simulation output</span><strong>Mode-field analysis.</strong> COMSOL mode profiles were used to inspect confinement and effective-index behavior across geometry sweeps, not as standalone figures detached from the model parameters.</figcaption>
  </figure>
  <figure class="research-figure">
    <img src="{{ '/images/research/waveguide_phase_matching_ln_lt.png' | relative_url }}" alt="Phase-matching comparison plot for thin-film lithium niobate and lithium tantalate waveguides" loading="lazy" width="1357" height="695">
    <figcaption><span class="evidence-badge evidence-badge--quant">Simulation-derived comparison</span><strong>LN/LT phase matching.</strong> The comparison connects waveguide geometry and material dispersion to phase-matching trends, making this project a useful bridge between integrated photonics simulation and later PCSEL device modeling.</figcaption>
  </figure>
</div>
</section>
