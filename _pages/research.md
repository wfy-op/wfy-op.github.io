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

<div class="workstream-panel" markdown="1">
**Recent workflow highlights**

- **Finite-array validation:** built a simplified HX1 5x5 PCSEL array model and compared it against periodic unit-cell references to separate finite-size trends from periodic-boundary artifacts.
- **QW etch-depth gate:** combined EC/HT and PDE/SRH proxy evidence to evaluate injection penalty, thermal behavior, and sidewall-recombination risk when etching approaches or exposes the quantum wells.
- **Backside DBR route:** used literature review and transfer-matrix modeling as a first-pass design screen before committing to expensive 3D COMSOL sweeps.
- **Optimization framing:** reviewed FDTD-driven device optimization as an expensive constrained multi-objective black-box problem, making Bayesian optimization, Pareto-front analysis, CMA-ES, and surrogate-assisted search natural complements to RL.
- **Literature infrastructure:** organized a local PCSEL literature workspace with searchable metadata, group/institution filters, PDFs, and notes to support device-design decisions.
</div>

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
