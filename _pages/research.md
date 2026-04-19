---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

Figures below are selected from my 2026 research presentation and represent my recent workstreams.

## GaAs Photonic Crystal Surface-Emitting Laser (PCSEL)

My current research focuses on **GaAs-based Photonic Crystal Surface-Emitting Lasers (PCSELs)** targeting the 980 nm band. PCSELs use a 2D photonic crystal resonator in the active region to realize single-mode, narrow-linewidth lasing with low-divergence surface emission.

Using **Lumerical FDTD** and **COMSOL Multiphysics**, I build full-wave models and perform:

- **Band-structure and mode analysis** for in-plane feedback and slow-light behavior.
- **Parameter sweeps** of lattice constant, hole radius, slab thickness, and cavity period.
- **Electro-optical co-analysis** for carrier transport, recombination behavior, and lasing-relevant constraints.

I also participate in fabrication and characterization, including ICP etching optimization, mask/layout checking, SEM inspection, and L-I-V plus spectral measurements.

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;align-items:start;">
  <figure style="margin:0;">
    <img src="{{ '/images/research/pcsel_device_concept.png' | relative_url }}" alt="PCSEL device concept" style="width:100%;height:auto;">
    <figcaption><small>PCSEL device-level concept.</small></figcaption>
  </figure>
  <figure style="margin:0;">
    <img src="{{ '/images/research/pcsel_mode_profile.png' | relative_url }}" alt="PCSEL mode profile" style="width:100%;height:auto;">
    <figcaption><small>Mode profile with refractive-index and confinement context.</small></figcaption>
  </figure>
  <figure style="margin:0;">
    <img src="{{ '/images/research/pcsel_iv_recombination_curve.jpeg' | relative_url }}" alt="PCSEL current and recombination curve" style="width:100%;height:auto;">
    <figcaption><small>Current-recombination behavior under electrical bias sweep.</small></figcaption>
  </figure>
  <figure style="margin:0;">
    <img src="{{ '/images/research/pcsel_optical_setup.jpg' | relative_url }}" alt="Optical characterization setup" style="width:100%;height:auto;">
    <figcaption><small>Optical measurement setup used in characterization.</small></figcaption>
  </figure>
</div>

The theoretical foundations for this direction are documented in [**PCSELBook**](https://github.com/wfy-op/PCSELbook).

---

## Thin-Film LiNbO3 / LiTaO3 Waveguide Mode Analysis

During my undergraduate research at Shandong University, I studied ridge waveguides in thin-film LiNbO3 and LiTaO3 using **COMSOL FEM**. The focus was the coupling between geometry and effective-index dispersion, and how this determines phase-matching windows for nonlinear conversion.

Key outputs include:

- Geometry-aware mode and field analysis in 2D and 3D structures.
- Comparison of LN and LT platforms under unified parameter scans.
- Width and etch-depth sensitivity analysis for phase matching.

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;align-items:start;">
  <figure style="margin:0;">
    <img src="{{ '/images/research/waveguide_geometry.png' | relative_url }}" alt="Waveguide geometry" style="width:100%;height:auto;">
    <figcaption><small>Ridge waveguide geometry used for simulation and analysis.</small></figcaption>
  </figure>
  <figure style="margin:0;">
    <img src="{{ '/images/research/waveguide_comsol_field_map.png' | relative_url }}" alt="COMSOL field map" style="width:100%;height:auto;">
    <figcaption><small>Representative COMSOL field map in a ring-waveguide structure.</small></figcaption>
  </figure>
  <figure style="margin:0;">
    <img src="{{ '/images/research/waveguide_phase_matching_ln_lt.png' | relative_url }}" alt="Phase matching comparison" style="width:100%;height:auto;">
    <figcaption><small>Phase-matching comparison between LN and LT material systems.</small></figcaption>
  </figure>
</div>

This work informed my undergraduate thesis on broadband nonlinear frequency conversion in thin-film lithium niobate.

---

## Memristor-based Reservoir Computing

From 2022 to 2023, I worked on dynamic SrTiO3-based memristors for reservoir-computing tasks (advisor: Prof. Limei Zheng, Shandong University). The project connected device nonlinearity and short-term memory with multimodal recognition pipelines.

My contribution focused on data processing, task pipeline implementation, and model/debug workflows for image and audio recognition tasks.

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;align-items:start;">
  <figure style="margin:0;">
    <img src="{{ '/images/research/memristor_synapse_device.png' | relative_url }}" alt="Memristor synapse schematic" style="width:100%;height:auto;">
    <figcaption><small>Physical-synapse analogy and device structure sketch.</small></figcaption>
  </figure>
  <figure style="margin:0;">
    <img src="{{ '/images/research/memristor_reservoir_framework.png' | relative_url }}" alt="Reservoir framework" style="width:100%;height:auto;">
    <figcaption><small>Reservoir-computing framework: input, dynamic state, and readout.</small></figcaption>
  </figure>
  <figure style="margin:0;">
    <img src="{{ '/images/research/memristor_audio_encoding.png' | relative_url }}" alt="Audio encoding for reservoir input" style="width:100%;height:auto;">
    <figcaption><small>Audio feature framing and encoding for memristor-driven processing.</small></figcaption>
  </figure>
</div>

Related publications are listed on the [Publications]({{ '/publications/' | relative_url }}) page.
