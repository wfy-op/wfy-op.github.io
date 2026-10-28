---
permalink: /
title: "About me"
excerpt: "Wu Feiyang — Ph.D. student at CUHK-Shenzhen; photonics research, computational tools, and project notes"
author_profile: false
redirect_from:
  - /about/
  - /about.html
---

<section class="profile-hero" aria-labelledby="profile-name">
  <div class="profile-hero__text">
    <p class="profile-hero__eyebrow">Semiconductor photonics · PCSEL modeling · research software</p>
    <h1 id="profile-name">Wu Feiyang <span lang="zh">吴飞洋</span></h1>
    <p class="profile-hero__role">Ph.D. Student · CUHK-Shenzhen</p>
    <p class="profile-hero__lead">
      I work on semiconductor photonics, with a current focus on GaAs photonic crystal surface-emitting lasers (PCSELs). I build computational models and research tools to connect device design, simulation, and experimental data. This site collects my research, projects, and learning notes.
    </p>
    <div class="profile-hero__actions">
      <a class="btn btn--primary" href="{{ '/research/pcsel/' | relative_url }}">PCSEL Research</a>
      <a class="btn" href="{{ '/cv/' | relative_url }}">CV</a>
    </div>
    <ul class="profile-hero__contact" aria-label="Contact">
      <li><a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a></li>
      <li><a href="https://github.com/wfy-op">GitHub</a></li>
      <li><a href="https://www.zhihu.com/people/fei-yu-33-8">Zhihu</a></li>
    </ul>
  </div>
  <figure class="profile-hero__portrait">
    <img src="{{ '/images/profile.jpg' | relative_url }}" alt="Portrait of Wu Feiyang" width="1279" height="2275" fetchpriority="high">
    <figcaption>Shenzhen · School of Science and Engineering, CUHK-Shenzhen</figcaption>
  </figure>
</section>

## At a Glance

<div class="home-facts" aria-label="Profile highlights">
  <article class="home-fact">
    <span>Current role</span>
    <strong>Ph.D. Student</strong>
    <p>CUHK-Shenzhen · Prof. Zhaoyu Zhang</p>
  </article>
  <article class="home-fact">
    <span>Primary program</span>
    <strong>940/980 nm GaAs PCSELs</strong>
    <p>Modeling, fabrication, and characterization</p>
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
      <p>940/980 nm device studies connecting electromagnetic models, fabrication constraints, and characterization, with CWT and full-wave calculations used to examine mode behavior.</p>
      <p class="home-research-card__meta">COMSOL · Lumerical · Python · Coupled-wave theory</p>
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

## Selected Outputs

<div class="home-output-list">
  <article class="home-output">
    <span>2026 · arXiv preprint · Co-first author</span>
    <h2><a href="https://arxiv.org/abs/2607.23469">When Every Simulation Counts</a></h2>
    <p>Matched evaluation of value-based RL methods under an 83-call FDTD budget.</p>
  </article>
  <article class="home-output">
    <span>2026 · arXiv preprint · Co-first author</span>
    <h2><a href="https://arxiv.org/abs/2607.21772">Reliability-Aware Bayesian Optimization of 1310 nm PCSELs</a></h2>
    <p>Candidate selection combines wavelength, beam quality, and Q-fit reliability.</p>
  </article>
  <article class="home-output">
    <span>2025 · Advanced Materials</span>
    <h2><a href="https://doi.org/10.1002/adma.202412006">Adaptive solid-state synapse for multimodal learning</a></h2>
    <p>Device dynamics connected to multimodal recognition and spatio-temporal tasks.</p>
  </article>
  <article class="home-output">
    <span>2023 · Materials Futures</span>
    <h2><a href="https://doi.org/10.1088/2752-5724/ace3dc">Ultrathin SrTiO3 memristor as a synaptic emulator</a></h2>
    <p>Drift and diffusive dynamics used for neuromorphic computing.</p>
  </article>
</div>

<p class="home-section-link"><a href="{{ '/publications/' | relative_url }}">View publications and evidence notes</a></p>

## Projects & Tools

<p class="home-section-intro">Interfaces from my research and teaching projects. Open a project to see its homepage and key screens; sensitive laboratory data are masked.</p>

{% include software-list.html compact=true %}

<p class="home-section-link"><a href="{{ '/projects/' | relative_url }}">Browse all projects and tools</a></p>

## Research Approach

<div class="home-approach" aria-label="Research approach">
  <article><strong>Model credibility</strong><p>Check mode identity, mesh, boundaries, and cross-solver consistency.</p></article>
  <article><strong>Process relevance</strong><p>Bring etch, morphology, mask, material, and QW constraints into design decisions.</p></article>
  <article><strong>Traceable evidence</strong><p>Keep figures, metrics, limitations, and source artifacts connected.</p></article>
</div>

## Recognition & Community

<div class="home-community-strip">
  <p><strong>National Second Prize</strong><span>Physics competitions · 2022/2023</span></p>
  <p><strong>Taishan Seminar</strong><span>Student-led academic exchange</span></p>
  <p><strong>Physics Innovation Alliance</strong><span>Co-founder · Shandong University</span></p>
  <p><strong>50,000+ views</strong><span>Long-form study notes on Zhihu</span></p>
</div>

## Contact

<p class="home-contact-line">School of Science and Engineering, The Chinese University of Hong Kong, Shenzhen · <a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a> · <a href="https://github.com/wfy-op">GitHub</a> · <a href="https://www.zhihu.com/people/fei-yu-33-8">Zhihu</a></p>
