---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

<p class="research-intro">
  My recent work centers on photonic devices, full-wave electromagnetic simulation, and experiment-aware design workflows. The selected figures below come from my 2026 research presentation and represent the main technical threads I am building.
</p>

<section class="research-section" markdown="1">
## GaAs Photonic Crystal Surface-Emitting Laser (PCSEL)

<div class="research-section__summary" markdown="1">
My current research focuses on **GaAs-based Photonic Crystal Surface-Emitting Lasers (PCSELs)** targeting the 980 nm band. PCSELs use a 2D photonic crystal resonator in the active region to realize single-mode, narrow-linewidth lasing with low-divergence surface emission.

Using **Lumerical FDTD** and **COMSOL Multiphysics**, I build full-wave models and perform:

- **Band-structure and mode analysis** for in-plane feedback and slow-light behavior.
- **Parameter sweeps** of lattice constant, hole radius, slab thickness, and cavity period.
- **Electro-optical co-analysis** for carrier transport, recombination behavior, and lasing-relevant constraints.

I also participate in fabrication and characterization, including ICP etching optimization, mask/layout checking, SEM inspection, and L-I-V plus spectral measurements.
</div>

<section class="workstream-showcase" aria-label="Recent PCSEL workstreams">
  <div class="workstream-showcase__header">
    <span class="workstream-showcase__eyebrow">Recent AI-assisted PCSEL workstreams</span>
    <h3>From isolated simulations to evidence-driven device decisions</h3>
    <p>These workstreams came from recent research sessions and are written here as public-facing technical directions. The schematics are workflow figures, not standalone experimental claims.</p>
  </div>

  <div class="workstream-detail-grid">
    <article class="workstream-card">
      <figure class="workstream-card__media">
        <img src="{{ '/images/research/pcsel_finite_array_workflow.svg' | relative_url }}" alt="Finite-array versus periodic-unit-cell PCSEL workflow schematic" loading="lazy">
      </figure>
      <div class="workstream-card__body">
        <span class="workstream-card__tag">COMSOL validation</span>
        <h4>Finite-array vs. periodic-unit-cell modeling</h4>
        <p>I built a simplified HX1 5x5 PCSEL finite-array model and compared it against periodic unit-cell references. The goal was to understand which Q-factor and mode-shape trends are intrinsic to the design, and which come from aperture size, side boundaries, or mesh choices.</p>
        <ul class="workstream-card__points">
          <li><strong>Method:</strong> finite aperture model, periodic reference cell, controlled geometry and mesh comparisons.</li>
          <li><strong>Evidence:</strong> mode identity, field localization, radiation channel, and Q-trend consistency.</li>
          <li><strong>Output:</strong> a validation route for deciding when expensive finite-array simulations are worth running.</li>
        </ul>
      </div>
    </article>

    <article class="workstream-card">
      <figure class="workstream-card__media">
        <img src="{{ '/images/research/pcsel_qw_etch_risk_gate.svg' | relative_url }}" alt="Quantum-well etch-depth risk gate schematic" loading="lazy">
      </figure>
      <div class="workstream-card__body">
        <span class="workstream-card__tag">Process risk gate</span>
        <h4>Quantum-well etch-depth EC/HT + PDE/SRH screen</h4>
        <p>For PCSEL top-etch decisions, I separated a practical etch-depth candidate from high-risk quantum-well exposure cases. The screen combines electrical-current and heat-transport reasoning with PDE/SRH sidewall-recombination proxies.</p>
        <ul class="workstream-card__points">
          <li><strong>Method:</strong> compare etch-front position against active-region geometry and carrier-transport constraints.</li>
          <li><strong>Evidence:</strong> injection penalty, thermal path, sidewall proximity, and non-radiative recombination risk.</li>
          <li><strong>Output:</strong> a process-window gate before committing to detailed device sweeps or fabrication recipes.</li>
        </ul>
      </div>
    </article>

    <article class="workstream-card">
      <figure class="workstream-card__media">
        <img src="{{ '/images/research/pcsel_backside_dbr_tmm_route.svg' | relative_url }}" alt="Backside DBR TMM-first simulation route schematic" loading="lazy">
      </figure>
      <div class="workstream-card__body">
        <span class="workstream-card__tag">DBR simulation route</span>
        <h4>Backside DBR design with TMM-first screening</h4>
        <p>Before launching large 3D COMSOL sweeps, I used literature review and transfer-matrix modeling as a fast screen for backside-DBR design. This keeps the first-pass search interpretable and reduces the chance of spending 3D simulation time on poor layer stacks.</p>
        <ul class="workstream-card__points">
          <li><strong>Method:</strong> start with TMM reflectivity and phase response, then shortlist stacks for full-wave checks.</li>
          <li><strong>Evidence:</strong> flux balance, PML sanity, mode-index consistency, and active-region coupling.</li>
          <li><strong>Output:</strong> a staged route from literature-backed stack choices to 3D verification.</li>
        </ul>
      </div>
    </article>

    <article class="workstream-card">
      <figure class="workstream-card__media">
        <img src="{{ '/images/research/pcsel_literature_workspace.svg' | relative_url }}" alt="PCSEL literature workspace schematic" loading="lazy">
      </figure>
      <div class="workstream-card__body">
        <span class="workstream-card__tag">Research infrastructure</span>
        <h4>Searchable PCSEL literature workspace</h4>
        <p>I organized a local PCSEL literature workspace that links PDFs, notes, group/institution metadata, topics, and design claims. The purpose is not just paper storage, but evidence retrieval for device-design decisions.</p>
        <ul class="workstream-card__points">
          <li><strong>Method:</strong> curate papers by device type, emission band, modeling method, and reported fabrication route.</li>
          <li><strong>Evidence:</strong> connect claims to source PDFs, figures, and simulation assumptions.</li>
          <li><strong>Output:</strong> a reusable knowledge layer for PCSEL design reviews, grant writing, and experiment planning.</li>
        </ul>
      </div>
    </article>

    <article class="workstream-card workstream-card--wide">
      <figure class="workstream-card__media">
        <img src="{{ '/images/research/pcsel_optimization_map.svg' | relative_url }}" alt="FDTD-driven black-box multi-objective optimization schematic" loading="lazy">
      </figure>
      <div class="workstream-card__body">
        <span class="workstream-card__tag">Optimization strategy</span>
        <h4>FDTD-driven structure optimization beyond a direct RL framing</h4>
        <p>I reframed PCSEL structural search as an expensive constrained multi-objective black-box problem. This makes Bayesian optimization, Pareto-front analysis, CMA-ES, and surrogate-assisted search natural complements to reinforcement learning when each FDTD or COMSOL evaluation is costly.</p>
        <ul class="workstream-card__points">
          <li><strong>Method:</strong> define design variables and constraints before choosing the search algorithm.</li>
          <li><strong>Evidence:</strong> evaluate Q, radiation behavior, beam quality, fabrication tolerance, and QW/process risk together.</li>
          <li><strong>Output:</strong> a clearer optimization roadmap that connects simulation cost, device objectives, and candidate ranking.</li>
        </ul>
      </div>
    </article>
  </div>
</section>

<h3 class="research-subtitle">Representative PCSEL figures</h3>

<div class="research-media-grid">
  <figure class="research-figure">
    <img src="{{ '/images/research/pcsel_device_concept.png' | relative_url }}" alt="PCSEL device concept" loading="lazy">
    <figcaption>PCSEL device-level concept.</figcaption>
  </figure>
  <figure class="research-figure">
    <img src="{{ '/images/research/pcsel_mode_profile.png' | relative_url }}" alt="PCSEL mode profile" loading="lazy">
    <figcaption>Mode profile with refractive-index and confinement context.</figcaption>
  </figure>
  <figure class="research-figure">
    <img src="{{ '/images/research/pcsel_iv_recombination_curve.jpeg' | relative_url }}" alt="PCSEL current and recombination curve" loading="lazy">
    <figcaption>Current-recombination behavior under electrical bias sweep.</figcaption>
  </figure>
  <figure class="research-figure">
    <img src="{{ '/images/research/pcsel_optical_setup.jpg' | relative_url }}" alt="Optical characterization setup" loading="lazy">
    <figcaption>Optical measurement setup used in characterization.</figcaption>
  </figure>
</div>

The theoretical foundations for this direction are documented in [**PCSELBook**](https://github.com/wfy-op/PCSELbook).
</section>

<section class="research-section" markdown="1">
## Thin-Film LiNbO₃ / LiTaO₃ Waveguide Mode Analysis

<div class="research-section__summary" markdown="1">
During my undergraduate research at Shandong University, I studied ridge waveguides in thin-film LiNbO₃ and LiTaO₃ using **COMSOL FEM**. The focus was the coupling between geometry and effective-index dispersion, and how this determines phase-matching windows for nonlinear conversion.

Key outputs include:

- Geometry-aware mode and field analysis in 2D and 3D structures.
- Comparison of LN and LT platforms under unified parameter scans.
- Width and etch-depth sensitivity analysis for phase matching.
</div>

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

This work informed my undergraduate thesis on broadband nonlinear frequency conversion in thin-film lithium niobate.
</section>

<section class="research-section" markdown="1">
## Memristor-based Reservoir Computing

<div class="research-section__summary" markdown="1">
From 2022 to 2023, I worked on dynamic SrTiO₃-based memristors for neuromorphic and reservoir-computing tasks (advisor: Prof. Limei Zheng, Shandong University). This work connected device-level physics (ferroelectric switching + ionic dynamics) with algorithm-level behaviors in supervised, unsupervised, and multimodal recognition pipelines.

Representative outcomes from this project include:

- **Linear and symmetric synaptic updates** in FTJ devices (NL = 0.13-0.17, mean single-pulse conductance update about +0.32/-0.36 uS), enabling **96.7%** MNIST accuracy in supervised learning (and **92.1%** when device variations are included).
- **Strong uniformity and temporal dynamics** in adaptive FTJ synapses, including cycle-to-cycle/device-to-device variation below **1.21%/1.93%**, and PPF/PPD time constants of **69/240 ms** and **66/380 ms**.
- **Multimodal reservoir computing** with polarity-separated coding (positive pulses for image, negative pulses for speech): when single-modal inputs were heavily corrupted, accuracy dropped to **64.0%** (image) or **62.7%** (audio), while multimodal fusion recovered accuracy to **95.4%**.
- **Spatio-temporal learning** via BCM-rule-based networks (81 input neurons, 324 synapses), supporting orientation selectivity and motion-direction identification.

My contribution focused on data preprocessing and pulse-encoding pipelines, MATLAB-based RC/ANN implementation, debugging, robustness evaluation, and result visualization for reproducible analysis.
</div>

<div class="research-media-grid">
  <figure class="research-figure">
    <img src="{{ '/images/research/memristor_synapse_device.png' | relative_url }}" alt="Memristor synapse schematic" loading="lazy">
    <figcaption>Physical-synapse analogy and device structure sketch.</figcaption>
  </figure>
  <figure class="research-figure">
    <img src="{{ '/images/research/memristor_reservoir_framework.png' | relative_url }}" alt="Reservoir framework" loading="lazy">
    <figcaption>Reservoir-computing framework: input, dynamic state, and readout.</figcaption>
  </figure>
  <figure class="research-figure">
    <img src="{{ '/images/research/memristor_audio_encoding.png' | relative_url }}" alt="Audio encoding for reservoir input" loading="lazy">
    <figcaption>Audio feature framing and encoding for memristor-driven processing.</figcaption>
  </figure>
</div>

Related papers: [**Adv. Funct. Mater. 2022**](https://doi.org/10.1002/adfm.202202366) and [**Adv. Mater. 2025**](https://doi.org/10.1002/adma.202412006). Related publications are listed on the [Publications]({{ '/publications/' | relative_url }}) page.
</section>
