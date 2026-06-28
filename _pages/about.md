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
    I build documented simulation-to-experiment workflows for semiconductor photonic devices. My current focus is GaAs PCSELs: using full-wave modeling, process constraints, and characterization feedback to decide which designs deserve further fabrication or experimental validation.
  </p>
  <div class="figure-explainer">
    <p><strong>Research thesis:</strong> my through-line is metric provenance: turning complex device outputs into claims traceable to physical variables, solver settings, process limits, and experiments.</p>
  </div>
  <div class="profile-hero__actions">
    <a class="btn btn--primary" href="{{ '/research/portal/' | relative_url }}">Research Portal</a>
    <a class="btn" href="{{ '/research/' | relative_url }}">Research</a>
    <a class="btn" href="{{ '/projects/' | relative_url }}">Projects</a>
    <a class="btn" href="{{ '/publications/' | relative_url }}">Publications</a>
    <a class="btn" href="{{ '/cv/' | relative_url }}">CV</a>
  </div>
</section>

## Evidence Snapshot

<div class="evidence-snapshot">
  <article class="evidence-snapshot__item">
    <span class="evidence-snapshot__label">Research portal</span>
    <strong><a href="{{ '/research/portal/' | relative_url }}">Live evidence dashboard</a></strong>
    <p>PCSEL library statistics, HX1-940 sweep figures, CWT reproduction progress, COMSOL/FDTD comparison status, RLcomsol optimization validation, and DailyBrief academic radar.</p>
  </article>
  <article class="evidence-snapshot__item">
    <span class="evidence-snapshot__label">Current role</span>
    <strong>Research Assistant at CUHK-Shenzhen</strong>
    <p>PCSEL research in the School of Science and Engineering, advised by Prof. Zhaoyu Zhang.</p>
  </article>
  <article class="evidence-snapshot__item">
    <span class="evidence-snapshot__label">Peer-reviewed papers</span>
    <strong>2 memristor papers</strong>
    <p>Co-authored Materials Futures 2023 and Advanced Materials 2025 work on neuromorphic devices.</p>
  </article>
  <article class="evidence-snapshot__item">
    <span class="evidence-snapshot__label">Patent application</span>
    <strong>CN 202610820592.4 accepted</strong>
    <p>Semiconductor-laser automated design-optimization method; CNIPA application accepted on 2026-06-08, not a granted patent.</p>
  </article>
  <article class="evidence-snapshot__item">
    <span class="evidence-snapshot__label">Public artifact</span>
    <strong><a href="https://github.com/wfy-op/PCSELbook">PCSELBook</a></strong>
    <p>A ~300,000-character technical note on PCSEL theory, simulation, and device physics.</p>
  </article>
  <article class="evidence-snapshot__item">
    <span class="evidence-snapshot__label">Device workflow</span>
    <strong>COMSOL / Lumerical / experiment loop</strong>
    <p>Modeling, process gates, optical/electrical setup, SEM feedback, and evidence tracking.</p>
  </article>
</div>

## Research Trajectory

<div class="trajectory-grid">
  <article class="trajectory-card">
    <span>2022</span>
    <h2>Numerical physics training</h2>
    <p>Early work with ZEUS hydrodynamic simulations and open-ended physics problems shaped my habit of understanding the physical variables before organizing the code workflow.</p>
  </article>
  <article class="trajectory-card">
    <span>2022-2023</span>
    <h2>Dynamic devices and data pipelines</h2>
    <p>Memristor reservoir-computing work trained my device-to-metric discipline: separating device nonlinearity, pulse encoding, preprocessing, and task-level metrics.</p>
  </article>
  <article class="trajectory-card">
    <span>2024-2025</span>
    <h2>Integrated photonics waveguides</h2>
    <p>LN/LT waveguide work with Prof. Lei Wang trained my COMSOL-based mode-analysis workflow: connect geometry sweeps, effective indices, and phase-matching conditions.</p>
  </article>
  <article class="trajectory-card">
    <span>2025-Present</span>
    <h2>PCSEL device loop</h2>
    <p>Current work combines electromagnetic design, solver automation, fabrication support, optical/electrical characterization, and literature-backed decision making.</p>
  </article>
</div>

## Current PCSEL Workflow

<section class="home-feature">
  <figure class="home-feature__media">
    <img src="{{ '/images/research/pcsel_device_concept.png' | relative_url }}" alt="Schematic PCSEL stack showing how the photonic-crystal layer couples in-plane feedback to surface emission." loading="lazy" width="1024" height="448">
    <figcaption>PCSEL concept figure: the photonic-crystal layer couples in-plane feedback to surface emission, anchoring the current device-design loop.</figcaption>
  </figure>
  <div class="home-feature__body">
    <span class="recent-work-card__tag">Current focus</span>
    <h2>From PCSEL design variables to verified device evidence</h2>
    <p>My current work treats PCSEL research as a loop: literature priors define device questions, COMSOL/Lumerical runs extract wavelength/Q/field metrics, process checks constrain feasible structures, and optical/electrical characterization feeds back into the next design step.</p>
  </div>
</section>

<div class="recent-work-grid">
  <article class="recent-work-card">
    <span class="recent-work-card__tag">pcsel-agent</span>
    <h2>Literature, solver, and report pipeline</h2>
    <p>Built a Python-based workflow that connects paper intake, target specifications, COMSOL/Lumerical execution, syntax memory, artifact checks, and research reports.</p>
  </article>
  <article class="recent-work-card">
    <span class="recent-work-card__tag">Simulation evidence</span>
    <h2>Parameter sweeps with physical questions</h2>
    <p>PCSEL sweeps are organized around wavelength, Q, field profile, confinement factor, sensitivity, and process feasibility rather than isolated images.</p>
  </article>
  <article class="recent-work-card">
    <span class="recent-work-card__tag">Experiment loop</span>
    <h2>Fabrication and characterization feedback</h2>
    <p>Optical/electrical pumping, L-I-V, spectra, beam profiles, SEM observations, ICP etch tuning, and KLayout mask checks are fed back into design decisions.</p>
  </article>
  <article class="recent-work-card">
    <span class="recent-work-card__tag">Future research direction</span>
    <h2>Next research questions</h2>
    <p>I want to extend this workflow toward fabrication-aware inverse design, surrogate-assisted automated search, and electro-thermal-optical coupling for semiconductor photonic devices.</p>
  </article>
</div>

## Research Highlights

<div class="highlight-grid">
  <article class="highlight-card">
    <h2>GaAs Photonic Crystal Surface-Emitting Laser</h2>
    <p>Current core direction: 980 nm GaAs PCSEL modeling and experiment-aware design, including band/mode analysis, Q-factor and wavelength extraction, process gates, optical/electrical testing, SEM-informed feedback, and pcsel-agent automation.</p>
  </article>
  <article class="highlight-card">
    <h2>Memristor Reservoir Computing</h2>
    <p>Dynamic SrTiO3-based memristors for reservoir computing, multimodal recognition, and spatio-temporal learning, with contributions to data preprocessing, MATLAB training workflows, and result visualization.</p>
  </article>
  <article class="highlight-card">
    <h2>LN/LT Waveguide Mode Analysis</h2>
    <p>Thin-film lithium niobate and lithium tantalate ridge-waveguide simulations with COMSOL, focused on geometry-dependent mode indices and phase-matching behavior.</p>
  </article>
</div>

## Education

- 2021.09 -- 2025.06, B.S. in Physics, Taishan College, Shandong University
- 2025.08 -- Present, Research Assistant, School of Science and Engineering, The Chinese University of Hong Kong (Shenzhen), supervised by Prof. Zhaoyu Zhang

## Selected Publications

1. F. Nie, J. Wang, H. Fang, S. Ma, **F. Wu**, et al. *Ultrathin SrTiO₃-based oxide memristor with both drift and diffusive dynamics as versatile synaptic emulators for neuromorphic computing*. Materials Futures, 2023, 2(3): 035302. [DOI](https://doi.org/10.1088/2752-5724/ace3dc)

2. F. Nie, H. Fang, J. Wang, L. Zhao, C. Jia, S. Ma, **F. Wu**, et al. *An Adaptive Solid-State Synapse with Bi-Directional Relaxation for Multimodal Recognition and Spatio-Temporal Learning*. Advanced Materials, 2025, 37(17): 2412006. [DOI](https://doi.org/10.1002/adma.202412006)

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
  <p><strong>E-mail:</strong> <a href="mailto:fywu2003@gmail.com">fywu2003@gmail.com</a> / <a href="mailto:wfy18350221083@outlook.com">wfy18350221083@outlook.com</a></p>
  <p class="contact-panel__updated">Updated: 2026.06</p>
</div>
