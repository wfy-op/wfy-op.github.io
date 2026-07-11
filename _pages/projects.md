---
layout: archive
title: "Research Software"
permalink: /projects/
author_profile: true
---

<section class="research-section" markdown="1">
## PCSEL Research Infrastructure

<div class="project-card-grid">
  <article class="project-card project-card--featured">
    <span class="project-card__status">Workflow index · public overview</span>
    <h2>pcsel-agent</h2>
    <p>A reproducible PCSEL research workflow that connects paper intake, target specifications, COMSOL/Lumerical execution, solver-syntax memory, geometry checks, metric provenance, and report generation.</p>
    <ul>
      <li><strong>Research role:</strong> make PCSEL simulation and optimization auditable.</li>
      <li><strong>Evidence tracked:</strong> eigenwavelength, Q-factor, mode identity, mesh/boundary checks, QW/process risk, and report artifacts.</li>
      <li><strong>Report corpus:</strong> summarized single-file design-review reports for 650 nm screening, 980 nm gain/source rules, HX1-940 sweeps, process sensitivity, bottom fillet sensitivity, and DBR workflow.</li>
      <li><strong>Public status:</strong> concept, workflow map, and evidence-status table are public; raw run artifacts remain private until they are cleaned and documented.</li>
      <li><strong>IP status:</strong> related semiconductor-laser automated design-optimization method filed as CN patent application 202610820592.4; application accepted by CNIPA on 2026-06-08, not a granted patent.</li>
    </ul>
    <p><a class="btn btn--primary" href="{{ '/research/pcsel/' | relative_url }}">Open PCSEL research</a></p>
  </article>

  <article class="project-card">
    <span class="project-card__status">Public repository</span>
    <h2>PCSELBook</h2>
    <p>A living technical monograph spanning Maxwell/Bloch foundations, CWT/PWEM/RCWA/FDTD/FEM methods, epitaxy, quantum-well gain, electro-thermal-optical coupling, and practical validation checklists.</p>
    <p><a class="btn" href="https://github.com/wfy-op/PCSELbook">GitHub</a> <a class="btn" href="{{ '/posts/2026/04/pcselbook/' | relative_url }}">Project note</a></p>
  </article>

  <article class="project-card">
    <span class="project-card__status">Public solver-connection skills</span>
    <h2>codex-for-comsol-lumerical</h2>
    <p>A Codex skill repository for connecting commercial simulation solvers to local research workflows. It separates COMSOL Multiphysics and Ansys Lumerical FDTD into reusable skills for path discovery, minimal probes, API/CLI fallback checks, and solver-syntax memory.</p>
    <ul>
      <li><strong>COMSOL:</strong> command-line tools, Java API, Python <code>mph</code> sessions, and local manual lookup.</li>
      <li><strong>Lumerical FDTD:</strong> <code>lumapi</code> probing, CLI sentinel scripts, Qanalysis, far-field, monitor, and material syntax checks.</li>
      <li><strong>Boundary:</strong> general solver-connection infrastructure, not a PCSEL device-template or reproduction package.</li>
    </ul>
    <p><a class="btn" href="https://github.com/wfy-op/codex-for-comsol-lumerical">GitHub</a></p>
  </article>

  <article class="project-card">
    <span class="project-card__status">Optimization sandbox · private</span>
    <h2>RLcode</h2>
    <p>Reinforcement-learning and black-box optimization experiments for PCSEL structural search. The current public emphasis is metric provenance: separating solver-derived physical metrics from reward/proxy quantities.</p>
    <p><a class="btn" href="{{ '/research/pcsel/' | relative_url }}#related-project-artifacts">Context</a></p>
  </article>

  <article class="project-card">
    <span class="project-card__status">COMSOL-backed optimization · private</span>
    <h2>RLcomsol</h2>
    <p>A COMSOL-backed continuation of the PCSEL optimization work. It connects RL/search policies to COMSOL geometry audits, mode-selection rules, accepted-score guards, multi-seed smoke panels, and reportable run provenance.</p>
    <ul>
      <li><strong>Current evidence:</strong> {{ site.data.research_portal.rlcomsol.reports_count }} local reports supporting geometry, mode-selection, guard, and repeatability audits.</li>
      <li><strong>Latest public-safe panel:</strong> three-seed, 20-step radius-guard smoke check with completed runs 3/3 and best accepted score 97.14.</li>
      <li><strong>Boundary:</strong> private code and raw solver artifacts; public page shows aggregate status and sanitized figures only.</li>
    </ul>
    <p><a class="btn" href="{{ '/research/pcsel/' | relative_url }}#rlcomsol">Evidence panel</a> <a class="btn" href="{{ '/research/pcsel/' | relative_url }}#related-project-artifacts">PCSEL context</a></p>
  </article>

  <article class="project-card">
    <span class="project-card__status">Knowledge base · private</span>
    <h2>PCSEL Paper Library</h2>
    <p>A private PCSEL literature workspace containing {{ site.data.research_portal.paper_library.records }} indexed records, {{ site.data.research_portal.paper_library.doi_count }} DOI-linked entries, and {{ site.data.research_portal.paper_library.standardized_analyses }} standardized analyses. Indexed, analyzed, and promoted states remain distinct.</p>
    <p><a class="btn" href="{{ '/research/pcsel/' | relative_url }}">Research context</a> <a class="btn" href="{{ '/research/pcsel/' | relative_url }}#pcsel-library">Evidence status</a></p>
  </article>
</div>
</section>
