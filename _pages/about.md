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
    I work on GaAs PCSELs, integrated photonic devices, and AI-assisted simulation workflows, with a current focus on turning device physics, numerical design, fabrication tolerance, and experimental feedback into a reproducible research loop.
  </p>
  <div class="profile-hero__actions">
    <a class="btn btn--primary" href="{{ '/research/' | relative_url }}">Research</a>
    <a class="btn" href="{{ '/projects/' | relative_url }}">Projects</a>
    <a class="btn" href="{{ '/publications/' | relative_url }}">Publications</a>
    <a class="btn" href="{{ '/cv/' | relative_url }}">CV</a>
  </div>
</section>

<section class="quick-facts" aria-label="Profile highlights">
  <div class="quick-facts__item">
    <span class="quick-facts__label">Current Role</span>
    <strong>Research Assistant, CUHK-Shenzhen</strong>
    <p>School of Science and Engineering, advised by Prof. Zhaoyu Zhang.</p>
  </div>
  <div class="quick-facts__item">
    <span class="quick-facts__label">Main Direction</span>
    <strong>GaAs PCSEL research loop</strong>
    <p>Full-wave modeling, process-aware design, optical/electrical testing, and evidence tracking.</p>
  </div>
  <div class="quick-facts__item">
    <span class="quick-facts__label">Technical Thread</span>
    <strong>pcsel-agent and automation</strong>
    <p>Lumerical FDTD, COMSOL FEM, Java/Python APIs, paper intake, and reproducible reports.</p>
  </div>
</section>

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
    <p>Memristor reservoir-computing work introduced the link between device nonlinearity, short-term memory, pulse encoding, and algorithm-level recognition tasks.</p>
  </article>
  <article class="trajectory-card">
    <span>2024-2025</span>
    <h2>Integrated photonics modeling</h2>
    <p>LN/LT waveguide research trained me to connect geometry, effective-index dispersion, etch depth, and phase-matching windows through systematic COMSOL sweeps.</p>
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
    <p>Built an AI-assisted workflow that connects paper intake, target specifications, COMSOL/Lumerical execution, syntax memory, artifact checks, and research reports.</p>
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
    <span class="recent-work-card__tag">PhD fit</span>
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
    <h2>Thin-Film LN/LT Waveguides</h2>
    <p>COMSOL FEM mode analysis and phase-matching studies for thin-film lithium niobate and lithium tantalate ridge waveguides, supporting my undergraduate thesis on broadband nonlinear frequency conversion.</p>
  </article>
  <article class="highlight-card">
    <h2>Memristor Reservoir Computing</h2>
    <p>Dynamic SrTiO3-based memristors for reservoir computing, multimodal recognition, and spatio-temporal learning, with contributions to data preprocessing, MATLAB training workflows, and result visualization.</p>
  </article>
</div>

## Education

- 2021.09 -- 2025.06, B.S. in Physics, Taishan College, Shandong University
- 2025.08 -- Present, Research Assistant, School of Science and Engineering, The Chinese University of Hong Kong (Shenzhen), supervised by Prof. Zhaoyu Zhang

## Selected Publications

1. F. Nie, J. Wang, H. Fang, S. Ma, **F. Wu**, et al. *Ultrathin SrTiO₃-based oxide memristor with both drift and diffusive dynamics as versatile synaptic emulators for neuromorphic computing*. Materials Futures, 2023, 2(3): 035302. [DOI](https://doi.org/10.1088/2752-5724/ace3dc)

2. F. Nie, S. Yang, L. Zhao, C. Jia, S. Ma, **F. Wu**, et al. *An Adaptive Solid-state Synapse with Bi-directional Relaxation for Multimodal Recognition and Spatio-temporal Learning*. Advanced Materials, 2025, 37(17): 2412006. [DOI](https://doi.org/10.1002/adma.202412006)

## Useful Links

<div class="link-list">
  <a href="https://github.com/wfy-op/PCSELbook">PCSELBook - PCSEL Theory, Simulation & Device Physics</a>
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
