---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: true
---

<p class="research-intro">
  This page collects software-like research artifacts, technical notes, and workflow systems that support my photonics work. I separate public links from internal artifacts so visitors can see what is inspectable now and what is still being sanitized.
</p>

<section class="research-section" markdown="1">
## PCSEL Research Infrastructure

<div class="project-card-grid">
  <article class="project-card project-card--featured">
    <span class="project-card__status">Core workflow · internal artifacts being sanitized</span>
    <h2>pcsel-agent</h2>
    <p>A reproducible PCSEL research workflow that connects paper intake, target specifications, COMSOL/Lumerical execution, solver-syntax memory, geometry checks, metric provenance, and report generation.</p>
    <ul>
      <li><strong>Research role:</strong> make PCSEL simulation and optimization auditable.</li>
      <li><strong>Evidence tracked:</strong> eigenwavelength, Q-factor, mode identity, mesh/boundary checks, QW/process risk, and report artifacts.</li>
      <li><strong>Public status:</strong> concept, workflow map, and sanitized evidence table are public; raw run artifacts remain internal until cleaned.</li>
    </ul>
    <p><a class="btn btn--primary" href="{{ '/research/pcsel/' | relative_url }}">Open PCSEL research</a></p>
  </article>

  <article class="project-card">
    <span class="project-card__status">Public repository</span>
    <h2>PCSELBook</h2>
    <p>An AI-assisted ~300,000-character technical note on PCSEL theory, simulation methods, semiconductor device physics, quantum-well gain, and electro-thermal-optical coupling.</p>
    <p><a class="btn" href="https://github.com/wfy-op/PCSELbook">GitHub</a> <a class="btn" href="{{ '/posts/2026/04/pcselbook/' | relative_url }}">Project note</a></p>
  </article>

  <article class="project-card">
    <span class="project-card__status">Optimization sandbox · internal</span>
    <h2>RLcode</h2>
    <p>Reinforcement-learning and black-box optimization experiments for PCSEL structural search. The current public emphasis is metric provenance: separating solver-derived physical metrics from reward/proxy quantities.</p>
    <p><a class="btn" href="{{ '/research/pcsel/' | relative_url }}#companion-projects">Context</a></p>
  </article>

  <article class="project-card">
    <span class="project-card__status">Knowledge base · internal</span>
    <h2>PCSEL Paper Library</h2>
    <p>A structured PCSEL literature workspace with 101 wiki entries, multi-source paper intake, local PDF parsing, and topic/group metadata for design-review evidence.</p>
    <p><a class="btn" href="{{ '/research/pcsel/' | relative_url }}">Research context</a></p>
  </article>
</div>
</section>

<section class="research-section" markdown="1">
## Community and Study Notes

<div class="project-card-grid">
  <article class="project-card">
    <span class="project-card__status">Community / notes</span>
    <h2>Taishan Seminar and Study Notes</h2>
    <p>Long-running student-led learning and teaching activities, including electrodynamics and nonlinear-optics modules, plus public study-note sharing.</p>
    <p><a class="btn" href="https://space.bilibili.com/1601830564">Bilibili</a> <a class="btn" href="https://www.zhihu.com/people/fei-yu-33-8">Zhihu</a></p>
  </article>
</div>
</section>
