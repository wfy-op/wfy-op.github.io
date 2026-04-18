---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

## GaAs Photonic Crystal Surface-Emitting Laser (PCSEL)

My current research focuses on **GaAs-based Photonic Crystal Surface-Emitting Lasers (PCSELs)** targeting the 980 nm band. PCSELs exploit a 2D photonic crystal resonator in the active region to achieve simultaneous single-mode, narrow-linewidth lasing and near-zero-divergence surface emission — key advantages over conventional edge-emitting and VCSEL architectures.

Using **Lumerical FDTD** and **COMSOL Multiphysics**, I built full 3D electromagnetic simulation models and performed:

- **Band structure analysis** to identify Γ-point slow-light modes responsible for in-plane feedback
- **Systematic parameter sweeps** of lattice constant, air-hole radius, and slab thickness
- **Double quantum-well epitaxial structure design** achieving stable single-mode lasing with FWHM < 0.2 nm and far-field divergence < 1°

Beyond simulation, I participate in the full device lifecycle:

- **Fabrication**: ICP etching recipe tuning, KLayout mask layout, and SEM inspection of etch profiles and overlay accuracy
- **Characterization**: Photoluminescence setup, L-I-V curves, spectral and beam-profile measurements
- **Project management**: Assisting with national/provincial grant applications and final reporting

I also developed an **automated simulation workflow** driven by a Claude Code agent system, linking Lumerical and COMSOL via Java/Python APIs for hands-free parameter sweeps and data extraction, with a reinforcement-learning optimization loop for device structure convergence.

The theoretical foundations underlying this work are documented in [**PCSELBook**](https://github.com/wfy-op/PCSELbook) — a ~300,000-character monograph I co-wrote covering Maxwell equations, Bloch modes, band analysis, PWEM/RCWA/FDTD/FEM numerical methods, semiconductor epitaxy, quantum-well gain, carrier transport, and electro-thermal-optical coupling.

---

## Thin-Film LiNbO₃ / LiTaO₃ Waveguide Mode Analysis

For my undergraduate research at Shandong University (advised by Prof. Lei Wang), I used **COMSOL FEM** to study the relationship between ridge waveguide geometry and effective mode index / phase-matching wavelength for thin-film LiNbO₃ and LiTaO₃. Fundamental-mode phase matching was achieved via **periodic poling**.

I also:
- Learned the grinding and polishing of thin-film micro-nano devices
- Built and operated optical measurement setups for ring-resonator frequency response

This work informed my undergraduate thesis: *Broadband Nonlinear Frequency Conversion in Thin-Film Lithium Niobate*, which systematically reviews the key mechanisms for wideband nonlinear frequency conversion and their implementations in waveguides, resonators, and optical frequency combs.

---

## Memristor-based Reservoir Computing

During 2022–2023 (advised by Prof. Limei Zheng, Shandong University), I contributed to an empirical study on dynamic SrTiO₃-based memristors for **reservoir computing**. The work demonstrated multimodal signal processing — text and speech recognition plus spatio-temporal learning — highlighting the potential of such synaptic devices for neuromorphic computing. Two co-authored papers were published in *Materials Futures* (2023) and *Advanced Materials* (2025).
