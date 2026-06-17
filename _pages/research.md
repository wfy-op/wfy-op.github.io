---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

<p class="research-intro">
  My research sits at the intersection of photonic devices, full-wave electromagnetic simulation, and experiment-aware design workflows. The work is organized into three directions: GaAs PCSELs, thin-film LN/LT waveguides, and memristor-based reservoir computing, with a common method: define the physical question, build the numerical or data workflow, and close the loop with device evidence.
</p>

<section class="research-section" markdown="1">
## Method Transfer

<div class="highlight-grid">
  <article class="highlight-card">
    <h2>From numerical models to device variables</h2>
    <p>Early numerical-physics training and waveguide simulations taught me to identify the physical variables first, then choose the solver, mesh, parameter sweep, and metric extraction strategy.</p>
  </article>
  <article class="highlight-card">
    <h2>From device dynamics to task-level evidence</h2>
    <p>Memristor work connected nonlinear device behavior to image, audio, multimodal recognition, and spatio-temporal learning tasks, making metric provenance and data processing part of the research question.</p>
  </article>
  <article class="highlight-card">
    <h2>From PCSEL simulation to research automation</h2>
    <p>Current PCSEL work combines literature priors, COMSOL/Lumerical runs, process gates, optical/electrical tests, SEM feedback, and AI-assisted reporting into a reusable workflow.</p>
  </article>
</div>
</section>

<section class="research-section" markdown="1">
## Current Research Questions

<div class="highlight-grid">
  <article class="highlight-card">
    <h2>How can fabrication tolerance enter design directly?</h2>
    <p>I want PCSEL optimization to include etch-depth limits, SEM-observed deviations, mask/layout constraints, and QW clearance before a design is called promising.</p>
  </article>
  <article class="highlight-card">
    <h2>How can automated search stay physically trustworthy?</h2>
    <p>The goal is not just faster sweeps, but solver-backed optimization with clear metric provenance: wavelength, Q, mode identity, confinement, process risk, and convergence history.</p>
  </article>
  <article class="highlight-card">
    <h2>How can experiments close the simulation loop?</h2>
    <p>Optical/electrical pumping, L-I-V, spectra, beam profiles, SEM, ICP process tuning, and KLayout review should feed back into the next device model rather than remain separate records.</p>
  </article>
</div>
</section>

<section class="research-direction-grid" aria-label="Research directions">
  <article class="research-direction-card">
    <figure class="research-direction-card__media">
      <img src="{{ '/images/research/pcsel_device_concept.png' | relative_url }}" alt="PCSEL stack schematic connecting photonic-crystal feedback with vertical surface emission" loading="lazy" width="1024" height="448">
    </figure>
    <div class="research-direction-card__body">
      <span class="research-direction-card__tag">Current focus</span>
      <h2>GaAs Photonic Crystal Surface-Emitting Lasers</h2>
      <p>Design and simulation of 980 nm GaAs PCSELs, with full-wave modeling, process-aware risk screening, fabrication/characterization feedback, and pcsel-agent automation.</p>
      <ul>
        <li>COMSOL and Lumerical FDTD modeling</li>
        <li>Parameter sweeps for wavelength, Q, field profile, and confinement factor</li>
        <li>QW etch-depth, DBR, fabrication tolerance, and experimental feedback gates</li>
      </ul>
      <a class="btn btn--primary" href="{{ '/research/pcsel/' | relative_url }}">Open PCSEL research</a>
    </div>
  </article>

  <article class="research-direction-card">
    <figure class="research-direction-card__media">
      <img src="{{ '/images/research/waveguide_phase_matching_ln_lt.png' | relative_url }}" alt="LN/LT effective-index curves used to compare nonlinear phase-matching windows" loading="lazy" width="1357" height="695">
    </figure>
    <div class="research-direction-card__body">
      <span class="research-direction-card__tag">Integrated photonics</span>
      <h2>Thin-Film LN / LT Waveguide Mode Analysis</h2>
      <p>COMSOL FEM analysis of ridge waveguides in thin-film lithium niobate and lithium tantalate, focused on geometry-dependent effective-index dispersion, etch-depth sensitivity, and nonlinear phase-matching windows.</p>
      <ul>
        <li>Mode-profile and effective-index analysis</li>
        <li>LN/LT platform comparison</li>
        <li>Undergraduate thesis on broadband nonlinear frequency conversion</li>
      </ul>
      <a class="btn btn--primary" href="{{ '/research/waveguide/' | relative_url }}">Open waveguide research</a>
    </div>
  </article>

  <article class="research-direction-card">
    <figure class="research-direction-card__media">
      <img src="{{ '/images/research/memristor_reservoir_framework.png' | relative_url }}" alt="Reservoir-computing diagram linking input pulses, memristor internal state, and readout output" loading="lazy" width="406" height="343">
    </figure>
    <div class="research-direction-card__body">
      <span class="research-direction-card__tag">Neuromorphic devices</span>
      <h2>Memristor-Based Reservoir Computing</h2>
      <p>Work on dynamic SrTiO3-based memristors for neuromorphic computing, multimodal recognition, and spatio-temporal learning, connecting device dynamics, pulse encoding, and task-level performance.</p>
      <ul>
        <li>Pulse encoding for image and audio tasks</li>
        <li>MATLAB RC/ANN workflow implementation</li>
        <li>Co-authored Materials Futures 2023 and Advanced Materials 2025 papers</li>
      </ul>
      <a class="btn btn--primary" href="{{ '/research/memristor/' | relative_url }}">Open memristor research</a>
    </div>
  </article>
</section>
