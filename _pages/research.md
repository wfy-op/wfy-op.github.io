---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

<section class="research-direction-grid" aria-label="Research directions">
  <article class="research-direction-card">
    <figure class="research-direction-card__media">
      <img src="{{ '/images/research/pcsel_device_concept.png' | relative_url }}" alt="PCSEL stack schematic connecting photonic-crystal feedback with vertical surface emission" loading="lazy" width="1024" height="448">
      <figcaption>Current focus: photonic-crystal feedback, vertical emission, and process-aware design variables.</figcaption>
    </figure>
    <div class="research-direction-card__body">
      <span class="research-direction-card__tag">Primary research program</span>
      <h2>GaAs Photonic Crystal Surface-Emitting Lasers</h2>
      <p>Design and simulation of 940/980 nm GaAs PCSELs, integrating full-wave validation, process-aware screening, inverse design, and pcsel-agent evidence tracking.</p>
      <p class="research-direction-card__meta">Mode identity · COMSOL/FDTD · QW/DBR · fabrication feedback</p>
      <a class="btn btn--primary" href="{{ '/research/pcsel/' | relative_url }}">Open PCSEL research</a>
    </div>
  </article>

  <article class="research-direction-card">
    <figure class="research-direction-card__media">
      <img src="{{ '/images/research/memristor_reservoir_framework.png' | relative_url }}" alt="Reservoir-computing diagram linking input pulses, memristor internal state, and readout output" loading="lazy" width="406" height="343">
      <figcaption>Method transfer: pulse input, dynamic physical state, and task-level readout metrics.</figcaption>
    </figure>
    <div class="research-direction-card__body">
      <span class="research-direction-card__tag">Earlier device-to-metric training</span>
      <h2>Memristor-Based Reservoir Computing</h2>
      <p>Dynamic SrTiO3-based memristors for neuromorphic computing, connecting pulse encoding and device relaxation to multimodal and spatio-temporal learning.</p>
      <p class="research-direction-card__meta">Materials Futures 2023 · Advanced Materials 2025</p>
      <a class="btn btn--primary" href="{{ '/research/memristor/' | relative_url }}">Open memristor research</a>
    </div>
  </article>

  <article class="research-direction-card">
    <figure class="research-direction-card__media">
      <img src="{{ '/images/research/waveguide_phase_matching_ln_lt.png' | relative_url }}" alt="LN and LT waveguide phase-matching comparison from COMSOL-based mode analysis" loading="lazy" width="1357" height="695">
      <figcaption>Integrated-photonics training: mode indices, geometry sweeps, and phase-matching windows.</figcaption>
    </figure>
    <div class="research-direction-card__body">
      <span class="research-direction-card__tag">Integrated photonics training</span>
      <h2>LN/LT Waveguide Mode Analysis</h2>
      <p>COMSOL-based thin-film lithium niobate and lithium tantalate ridge-waveguide studies, comparing geometry-dependent effective indices and phase-matching windows.</p>
      <p class="research-direction-card__meta">Mode analysis · geometry sweeps · material dispersion</p>
      <a class="btn btn--primary" href="{{ '/research/waveguide/' | relative_url }}">Open waveguide research</a>
    </div>
  </article>
</section>

<section class="research-section" markdown="1">
## Research Throughline

<div class="research-throughline">
  <article><span>01</span><h2>Establish model credibility</h2><p>Identify the physical variable and mode first, then test solver, mesh, boundary, and metric sensitivity.</p></article>
  <article><span>02</span><h2>Bring constraints into the model</h2><p>Translate material dispersion, device dynamics, etch windows, morphology, and mask limits into measurable design gates.</p></article>
  <article><span>03</span><h2>Close the evidence loop</h2><p>Connect simulation outputs to task metrics, fabrication observations, and characterization data without losing provenance.</p></article>
</div>
</section>
