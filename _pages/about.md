---
permalink: /
title: "About me"
excerpt: "Wu Feiyang - photonics researcher"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<section class="profile-hero">
  <p class="profile-hero__eyebrow">Simulation-guided photonic devices · Semiconductor lasers · Research automation</p>
  <h1>Wu Feiyang (吴飞洋)</h1>
  <p class="profile-hero__lead">
    I develop evidence-gated workflows for semiconductor photonic devices. My current focus is GaAs PCSELs, where full-wave modeling, solver validation, process constraints, and characterization feedback are used to distinguish credible design trends from numerical false positives.
  </p>
  <div class="figure-explainer">
    <p><strong>Research thesis:</strong> automation is useful only when every result remains traceable to geometry, mode identity, solver settings, process limits, and the evidence needed for the next decision.</p>
  </div>
  <div class="profile-hero__actions">
    <a class="btn btn--primary" href="{{ '/research/pcsel/' | relative_url }}">PCSEL Research</a>
    <a class="btn" href="{{ '/cv/' | relative_url }}">CV</a>
  </div>
</section>

## At a Glance

<div class="home-facts" aria-label="Profile highlights">
  <article class="home-fact">
    <span>Current role</span>
    <strong>Research Assistant</strong>
    <p>CUHK-Shenzhen · Prof. Zhaoyu Zhang</p>
  </article>
  <article class="home-fact">
    <span>Primary program</span>
    <strong>940/980 nm GaAs PCSELs</strong>
    <p>Full-wave, process, and experiment loop</p>
  </article>
  <article class="home-fact">
    <span>Research outputs</span>
    <strong>2 journal papers + 2 preprints</strong>
    <p>Memristor devices · PCSEL inverse design</p>
  </article>
  <article class="home-fact">
    <span>Patent application</span>
    <strong>CN 202610820592.4</strong>
    <p>Accepted by CNIPA · 2026-06-08</p>
  </article>
</div>

<section id="research-programs" class="home-research" markdown="1">
## Research Programs

<div class="home-research-grid">
  <article class="home-research-card home-research-card--primary">
    <a class="home-research-card__media" href="{{ '/research/pcsel/' | relative_url }}">
      <img src="{{ '/images/research/pcsel_device_concept.png' | relative_url }}" alt="GaAs PCSEL stack connecting photonic-crystal feedback with vertical emission" loading="lazy" width="1024" height="448">
    </a>
    <div class="home-research-card__body">
      <span class="home-research-card__tag">Primary research program</span>
      <h2><a href="{{ '/research/pcsel/' | relative_url }}">GaAs photonic crystal surface-emitting lasers</a></h2>
      <p>Evidence-gated design for 940/980 nm devices, combining mode identity, boundary convergence, fabrication morphology, QW/DBR constraints, and characterization feedback.</p>
      <p class="home-research-card__meta">COMSOL · Lumerical · pcsel-agent · experiment-aware design</p>
    </div>
  </article>

  <article class="home-research-card">
    <a class="home-research-card__media" href="{{ '/research/memristor/' | relative_url }}">
      <img src="{{ '/images/research/memristor_reservoir_framework.png' | relative_url }}" alt="Memristor reservoir-computing framework linking pulse input, device state, and readout" loading="lazy" width="406" height="343">
    </a>
    <div class="home-research-card__body">
      <span class="home-research-card__tag">Published device research</span>
      <h2><a href="{{ '/research/memristor/' | relative_url }}">Memristor reservoir computing</a></h2>
      <p>Dynamic SrTiO3 devices, pulse encoding, multimodal recognition, and spatio-temporal learning.</p>
    </div>
  </article>

  <article class="home-research-card">
    <a class="home-research-card__media" href="{{ '/research/waveguide/' | relative_url }}">
      <img src="{{ '/images/research/waveguide_phase_matching_ln_lt.png' | relative_url }}" alt="LN and LT ridge-waveguide phase-matching comparison from COMSOL mode analysis" loading="lazy" width="1357" height="695">
    </a>
    <div class="home-research-card__body">
      <span class="home-research-card__tag">Integrated photonics</span>
      <h2><a href="{{ '/research/waveguide/' | relative_url }}">LN/LT waveguide mode analysis</a></h2>
      <p>Work with Prof. Lei Wang on effective-index sweeps, material dispersion, and phase-matching windows.</p>
    </div>
  </article>
</div>
</section>

## How I Work

<section class="home-feature">
  <figure class="home-feature__media">
    <img src="{{ '/images/research/pcsel_agent_architecture.svg' | relative_url }}" alt="pcsel-agent architecture connecting literature, device constraints, solvers, and evidence reports" loading="lazy" width="1360" height="760">
    <figcaption>pcsel-agent keeps literature priors, solver runs, process checks, and public claims connected to their source artifacts.</figcaption>
  </figure>
  <div class="home-feature__body">
    <span class="home-research-card__tag">Evidence before optimization</span>
    <h2>From a design variable to a defensible decision</h2>
    <p>I organize PCSEL research around three gates:</p>
    <ul class="home-feature__points">
      <li><strong>Physics:</strong> identify the mode and test mesh, boundary, and solver sensitivity.</li>
      <li><strong>Fabrication:</strong> check etch depth, QW clearance, morphology, mask, and material constraints.</li>
      <li><strong>Provenance:</strong> connect every wavelength, Q, field, or optimization score to a documented run and interpretation boundary.</li>
    </ul>
    <a class="btn btn--primary" href="{{ '/research/pcsel/' | relative_url }}#selected-validation">See validation cases</a>
  </div>
</section>

## Research Trajectory

<div class="trajectory-grid">
  <article class="trajectory-card">
    <span>2022</span>
    <h2>Numerical physics</h2>
    <p>ZEUS hydrodynamic simulations established a physics-first approach to variables, solvers, and numerical evidence.</p>
  </article>
  <article class="trajectory-card">
    <span>2022-2023</span>
    <h2>Dynamic devices</h2>
    <p>Memristor work connected device dynamics and data processing to task-level metrics.</p>
  </article>
  <article class="trajectory-card">
    <span>2024-2025</span>
    <h2>Integrated photonics</h2>
    <p>LN/LT waveguide studies developed a geometry-to-mode-to-phase-matching workflow.</p>
  </article>
  <article class="trajectory-card">
    <span>2025-Present</span>
    <h2>PCSEL research system</h2>
    <p>Current work integrates electromagnetic design, research automation, process support, and characterization.</p>
  </article>
</div>

## Education

- 2021.09 -- 2025.06, B.S. in Physics, Taishan College, Shandong University
- 2025.08 -- Present, Research Assistant, School of Science and Engineering, The Chinese University of Hong Kong (Shenzhen), supervised by Prof. Zhaoyu Zhang

## Selected Publications

1. L. Wen*, **F. Wu***, J. Yu*, C. Yuan, R. Li, and Z. Zhang. *When Every Simulation Counts: Value-Based Reinforcement Learning for Accelerated Photonics Inverse Design*. arXiv:2607.23469, 2026. Co-first author. [arXiv](https://arxiv.org/abs/2607.23469)

2. J. Yu*, **F. Wu***, L. Wen*, C. Yuan, R. Li, and Z. Zhang. *Reliability-Aware Bayesian Optimization of 1310 nm PCSELs with FDTD Verification*. arXiv:2607.21772, 2026. Co-first author. [arXiv](https://arxiv.org/abs/2607.21772)

3. F. Nie, H. Fang, J. Wang, L. Zhao, C. Jia, S. Ma, **F. Wu**, et al. *An Adaptive Solid-State Synapse with Bi-Directional Relaxation for Multimodal Recognition and Spatio-Temporal Learning*. Advanced Materials, 2025, 37(17): 2412006. [DOI](https://doi.org/10.1002/adma.202412006)

4. F. Nie, J. Wang, H. Fang, S. Ma, **F. Wu**, et al. *Ultrathin SrTiO₃-based oxide memristor with both drift and diffusive dynamics as versatile synaptic emulators for neuromorphic computing*. Materials Futures, 2023, 2(3): 035302. [DOI](https://doi.org/10.1088/2752-5724/ace3dc)

## Recognition & Community

<div class="recognition-grid">
  <article class="recognition-item">
    <span class="recognition-item__label">Selected awards</span>
    <h2>National physics competition recognition</h2>
    <p>National Second Prize in the 2023 China Undergraduate Physics Experiment Competition and the 2022 CUPT, plus a CUPT East China Regional Second Prize.</p>
  </article>
  <article class="recognition-item">
    <span class="recognition-item__label">Community building</span>
    <h2>Student-led academic exchange</h2>
    <p>Contributed lectures to the Taishan Seminar and co-founded the SDU Physics Innovation Alliance for cross-year exchange, competition training, and outreach.</p>
  </article>
  <article class="recognition-item">
    <span class="recognition-item__label">Public notes</span>
    <h2>Long-form science communication</h2>
    <p>Study notes and subject answers on Zhihu have accumulated 50,000+ views and 2,000+ likes/bookmarks.</p>
  </article>
</div>

## Useful Links

<div class="link-list">
  <a href="https://github.com/wfy-op/PCSELbook">PCSELBook - PCSEL Theory, Simulation & Device Physics</a>
  <a href="https://github.com/wfy-op/codex-for-comsol-lumerical">codex-for-comsol-lumerical - COMSOL / Lumerical solver skills</a>
  <a href="https://space.bilibili.com/1601830564">Taishan Seminar (Bilibili)</a>
  <a href="https://www.zhihu.com/people/fei-yu-33-8">Zhihu Profile</a>
</div>

## Contact

<div class="contact-panel">
  <p><strong>Name:</strong> Wu Feiyang 吴飞洋</p>
  <p><strong>Institution:</strong> School of Science and Engineering, The Chinese University of Hong Kong (Shenzhen)</p>
  <p><strong>E-mail:</strong> <a href="mailto:fywu2003@gmail.com">fywu2003@gmail.com</a> / <a href="mailto:wfy18350221083@163.com">wfy18350221083@163.com</a></p>
  <p class="contact-panel__updated">Updated: 2026.07</p>
</div>
