---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

<p class="research-intro">
  My research sits at the intersection of photonic devices, full-wave electromagnetic simulation, and experiment-aware design workflows. The work is organized into three directions: GaAs PCSELs, thin-film LN/LT waveguides, and memristor-based reservoir computing.
</p>

<section class="research-direction-grid" aria-label="Research directions">
  <article class="research-direction-card">
    <figure class="research-direction-card__media">
      <img src="{{ '/images/research/pcsel_device_concept.png' | relative_url }}" alt="PCSEL device concept" loading="lazy">
    </figure>
    <div class="research-direction-card__body">
      <span class="research-direction-card__tag">Current focus</span>
      <h2>GaAs Photonic Crystal Surface-Emitting Lasers</h2>
      <p>Design and simulation of 980 nm GaAs PCSELs, with full-wave modeling, process-aware risk screening, finite-array validation, DBR route planning, and AI-assisted optimization workflows.</p>
      <ul>
        <li>COMSOL and Lumerical FDTD modeling</li>
        <li>Finite-array vs. periodic-cell comparison</li>
        <li>QW etch-depth and DBR design gates</li>
      </ul>
      <a class="btn btn--primary" href="{{ '/research/pcsel/' | relative_url }}">Open PCSEL research</a>
    </div>
  </article>

  <article class="research-direction-card">
    <figure class="research-direction-card__media">
      <img src="{{ '/images/research/waveguide_phase_matching_ln_lt.png' | relative_url }}" alt="LN and LT phase matching comparison" loading="lazy">
    </figure>
    <div class="research-direction-card__body">
      <span class="research-direction-card__tag">Integrated photonics</span>
      <h2>Thin-Film LN / LT Waveguide Mode Analysis</h2>
      <p>COMSOL FEM analysis of ridge waveguides in thin-film lithium niobate and lithium tantalate, focused on geometry-dependent effective-index dispersion and nonlinear phase-matching windows.</p>
      <ul>
        <li>Mode-profile and effective-index analysis</li>
        <li>LN/LT platform comparison</li>
        <li>Phase-matching sensitivity to geometry</li>
      </ul>
      <a class="btn btn--primary" href="{{ '/research/waveguide/' | relative_url }}">Open waveguide research</a>
    </div>
  </article>

  <article class="research-direction-card">
    <figure class="research-direction-card__media">
      <img src="{{ '/images/research/memristor_reservoir_framework.png' | relative_url }}" alt="Memristor reservoir computing framework" loading="lazy">
    </figure>
    <div class="research-direction-card__body">
      <span class="research-direction-card__tag">Neuromorphic devices</span>
      <h2>Memristor-Based Reservoir Computing</h2>
      <p>Work on dynamic SrTiO3-based memristors for neuromorphic computing, multimodal recognition, and spatio-temporal learning, connecting device dynamics to algorithm-level task performance.</p>
      <ul>
        <li>Pulse encoding for image and audio tasks</li>
        <li>MATLAB RC/ANN workflow implementation</li>
        <li>Co-authored published memristor papers</li>
      </ul>
      <a class="btn btn--primary" href="{{ '/research/memristor/' | relative_url }}">Open memristor research</a>
    </div>
  </article>
</section>
