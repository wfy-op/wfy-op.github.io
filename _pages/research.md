---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

<p class="research-intro">
  My research sits at the intersection of photonic devices, full-wave electromagnetic simulation, and experiment-aware design workflows. The current center of gravity is GaAs PCSELs; earlier memristor reservoir-computing work provides a device-to-metric training ground for the same habit: separate physical response, data processing, and downstream performance claims.
</p>

<section class="research-direction-grid" aria-label="Research directions">
  <article class="research-direction-card">
    <figure class="research-direction-card__media">
      <img src="{{ '/images/research/pcsel_device_concept.png' | relative_url }}" alt="PCSEL stack schematic connecting photonic-crystal feedback with vertical surface emission" loading="lazy" width="1024" height="448">
      <figcaption>Current focus: photonic-crystal feedback, vertical emission, and process-aware design variables.</figcaption>
    </figure>
    <div class="research-direction-card__body">
      <span class="research-direction-card__tag">Current focus</span>
      <h2>GaAs Photonic Crystal Surface-Emitting Lasers</h2>
      <p>Design and simulation of 980 nm GaAs PCSELs, with full-wave modeling, process-aware risk screening, fabrication/characterization feedback, and pcsel-agent evidence tracking.</p>
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
      <img src="{{ '/images/research/memristor_reservoir_framework.png' | relative_url }}" alt="Reservoir-computing diagram linking input pulses, memristor internal state, and readout output" loading="lazy" width="406" height="343">
      <figcaption>Method transfer: pulse input, dynamic physical state, and task-level readout metrics.</figcaption>
    </figure>
    <div class="research-direction-card__body">
      <span class="research-direction-card__tag">Earlier device-to-metric training</span>
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

<section class="research-section" markdown="1">
## Current Research Questions

<div class="highlight-grid">
  <article class="highlight-card">
    <h2>How can fabrication tolerance enter design directly?</h2>
    <p>I want PCSEL optimization to include etch-depth limits, SEM-observed deviations, mask/layout constraints, and QW clearance before treating a design as a candidate for fabrication or experimental validation.</p>
  </article>
  <article class="highlight-card">
    <h2>How can automated search remain physically interpretable?</h2>
    <p>The goal is not just faster sweeps, but solver-backed optimization with clear metric provenance: wavelength, Q, mode identity, confinement, process risk, and convergence history.</p>
  </article>
  <article class="highlight-card">
    <h2>How can experiments close the simulation loop?</h2>
    <p>Optical/electrical pumping, L-I-V, spectra, beam profiles, SEM, ICP process tuning, and KLayout review should feed back into the next device model rather than remain separate records.</p>
  </article>
</div>
</section>

<section class="research-section" markdown="1">
## Method Transfer

<div class="highlight-grid">
  <article class="highlight-card">
    <h2>From numerical models to device variables</h2>
    <p>Early numerical-physics training taught me to identify the physical variables first, then choose the solver, mesh, parameter sweep, and metric extraction strategy.</p>
  </article>
  <article class="highlight-card">
    <h2>From device dynamics to task-level evidence</h2>
    <p>Memristor work connected nonlinear device behavior to image, audio, multimodal recognition, and spatio-temporal learning tasks, making metric provenance and data processing part of the research question.</p>
  </article>
  <article class="highlight-card">
    <h2>From PCSEL simulation to research automation</h2>
    <p>Current PCSEL work combines literature priors, COMSOL/Lumerical runs, process gates, optical/electrical tests, SEM feedback, and source-linked reporting into a documented workflow.</p>
  </article>
</div>
</section>
