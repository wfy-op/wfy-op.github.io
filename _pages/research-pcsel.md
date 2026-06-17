---
layout: archive
title: "GaAs PCSEL Research"
permalink: /research/pcsel/
author_profile: true
---

<p class="research-intro">
  My PCSEL work is organized around <strong>pcsel-agent</strong>, an AI-assisted research system for GaAs photonic-crystal surface-emitting lasers. Instead of treating each simulation as an isolated file, I use pcsel-agent to connect literature intake, device specifications, COMSOL/Lumerical/FDTD execution, solver-syntax memory, metric provenance, and human-readable reports.
</p>

<p class="research-backlink"><a href="{{ '/research/' | relative_url }}">Back to all research directions</a></p>

<section class="research-section" markdown="1">
## Project Stack

<div class="pcsel-stack-grid">
  <article class="pcsel-stack-card pcsel-stack-card--primary">
    <span class="pcsel-stack-card__tag">Core system</span>
    <h3>pcsel-agent</h3>
    <p>A Python + agent workflow for PCSEL research. It routes papers, design briefs, solver jobs, repair memory, artifact checks, and reports into one reproducible research loop.</p>
    <ul>
      <li>COMSOL and Lumerical automation with verified syntax memory.</li>
      <li>HX1 940/980 nm model validation across GME, FEM, and FDTD routes.</li>
      <li>Process-aware gates for QW etch depth, DBR stacks, gain bands, and optimization results.</li>
    </ul>
  </article>

  <article class="pcsel-stack-card">
    <span class="pcsel-stack-card__tag">Theory backbone</span>
    <h3>PCSELBook</h3>
    <p>A roughly 300,000-character technical monograph covering PCSEL theory, simulation, semiconductor device physics, epitaxy, quantum-well gain, and electro-thermal-optical coupling.</p>
    <a href="{{ '/posts/2026/04/pcselbook/' | relative_url }}">Read the project note</a>
  </article>

  <article class="pcsel-stack-card">
    <span class="pcsel-stack-card__tag">Optimization code</span>
    <h3>RLcode</h3>
    <p>A reinforcement-learning and optimization codebase used to explore PCSEL structural search. My current emphasis is metric provenance: separating solver-derived physical results from bookkeeping, reward shaping, or proxy objectives.</p>
  </article>

  <article class="pcsel-stack-card">
    <span class="pcsel-stack-card__tag">Knowledge base</span>
    <h3>Paper Library</h3>
    <p>A local PCSEL paper library with <strong>101</strong> structured wiki entries. It ingests literature from arXiv, Semantic Scholar, Crossref, DOAJ, and local PDFs, then turns papers into searchable design evidence.</p>
  </article>
</div>
</section>

<section class="pcsel-agent-panel" markdown="1">
## pcsel-agent: Research Operating System

<div class="pcsel-agent-panel__lead" markdown="1">
The main output of this direction is not only a set of PCSEL simulation results. It is a workflow that makes those results auditable: every geometry convention, solver command, mesh setting, Q-factor, eigenwavelength, field identity, and process-risk claim should have a traceable source.
</div>

<div class="pcsel-agent-map">
  <div class="pcsel-agent-map__item">
    <span>1</span>
    <strong>Literature and priors</strong>
    <p>Paper feeds and local PDFs are parsed into a wiki-style knowledge layer for device concepts, reported bands, modeling assumptions, fabrication routes, and comparison targets.</p>
  </div>
  <div class="pcsel-agent-map__item">
    <span>2</span>
    <strong>Design and constraints</strong>
    <p>Device variables are defined with explicit geometry, material, QW-position, etch-depth, and fabrication constraints before any expensive sweep begins.</p>
  </div>
  <div class="pcsel-agent-map__item">
    <span>3</span>
    <strong>Solver execution</strong>
    <p>COMSOL, Lumerical FDTD/FDE, and Python-side analysis are connected through adapters, run manifests, and syntax memory that records commands only after local verification.</p>
  </div>
  <div class="pcsel-agent-map__item">
    <span>4</span>
    <strong>Evidence and report</strong>
    <p>Runs are checked for metric provenance, mode identity, mesh and boundary consistency, exported geometry, and public-facing reports with figures rather than loose screenshots.</p>
  </div>
</div>
</section>

<section class="workstream-showcase" aria-label="pcsel-agent research points">
  <div class="workstream-showcase__header">
    <span class="workstream-showcase__eyebrow">Concrete research points under pcsel-agent</span>
    <h3>From solver automation to device decisions</h3>
    <p>These are the main PCSEL research threads currently organized inside pcsel-agent. The figures are workflow schematics for public explanation; each thread is backed by run artifacts, scripts, or literature notes in the working system.</p>
  </div>

  <div class="workstream-detail-grid">
    <article class="workstream-card">
      <figure class="workstream-card__media">
        <img src="{{ '/images/research/pcsel_finite_array_workflow.svg' | relative_url }}" alt="Finite-array versus periodic-unit-cell PCSEL workflow schematic" loading="lazy">
      </figure>
      <div class="workstream-card__body">
        <span class="workstream-card__tag">HX1 model validation</span>
        <h4>940/980 nm full-wave validation across model scales</h4>
        <p>pcsel-agent organizes HX1 PCSEL simulations across periodic unit cells, simplified finite arrays, and full-wave references so that Q-factor and eigenwavelength trends can be compared without losing geometry identity.</p>
        <ul class="workstream-card__points">
          <li><strong>Question:</strong> which trends are device physics, and which are boundary, aperture, or mesh artifacts?</li>
          <li><strong>Method:</strong> compare GME-style references, COMSOL eigenfrequency studies, and FDTD checks with controlled lattice and hole parameters.</li>
          <li><strong>Evidence:</strong> mode identity, field localization, radiation channel, mesh statistics, and Q/wavelength consistency.</li>
        </ul>
      </div>
    </article>

    <article class="workstream-card">
      <figure class="workstream-card__media">
        <img src="{{ '/images/research/pcsel_qw_etch_risk_gate.svg' | relative_url }}" alt="Quantum-well etch-depth risk gate schematic" loading="lazy">
      </figure>
      <div class="workstream-card__body">
        <span class="workstream-card__tag">Process-aware design</span>
        <h4>QW etch-depth convention and risk gates</h4>
        <p>For top-etch PCSEL designs, I treat etch depth as a process variable that must be checked against the active region rather than a free geometric knob. The agent records the convention, exported geometry, and material assignment before accepting simulation results.</p>
        <ul class="workstream-card__points">
          <li><strong>Question:</strong> does a nominally good optical point create a QW exposure, carrier-transport, or sidewall-recombination risk?</li>
          <li><strong>Method:</strong> combine etch-front geometry audits with EC/HT reasoning and PDE/SRH-style recombination screens.</li>
          <li><strong>Evidence:</strong> hole depth, forbidden-region checks, injection penalty, thermal path, and non-radiative sidewall risk.</li>
        </ul>
      </div>
    </article>

    <article class="workstream-card">
      <figure class="workstream-card__media">
        <img src="{{ '/images/research/pcsel_backside_dbr_tmm_route.svg' | relative_url }}" alt="Backside DBR TMM-first simulation route schematic" loading="lazy">
      </figure>
      <div class="workstream-card__body">
        <span class="workstream-card__tag">Vertical stack</span>
        <h4>Backside DBR and gain-band route</h4>
        <p>pcsel-agent keeps fast transfer-matrix screens and gain-band estimates upstream of expensive 3D verification. This makes backside-DBR choices and QW gain assumptions easier to inspect before launching large solver jobs.</p>
        <ul class="workstream-card__points">
          <li><strong>Question:</strong> which DBR stacks and gain-band assumptions deserve full-wave verification?</li>
          <li><strong>Method:</strong> use TMM reflectivity and phase response, QW gain-spectrum calculations, and Lumerical MQW/gain workflow checks.</li>
          <li><strong>Evidence:</strong> flux balance, PML sanity, active-region coupling, and wavelength alignment.</li>
        </ul>
      </div>
    </article>

    <article class="workstream-card">
      <figure class="workstream-card__media">
        <img src="{{ '/images/research/pcsel_optimization_map.svg' | relative_url }}" alt="FDTD-driven black-box multi-objective optimization schematic" loading="lazy">
      </figure>
      <div class="workstream-card__body">
        <span class="workstream-card__tag">Optimization trust</span>
        <h4>From RLcode experiments to solver-backed optimization</h4>
        <p>RLcode is useful as an exploration framework, but pcsel-agent makes the optimization problem stricter: each candidate must be tied to solver-backed metrics, design constraints, and reproducible artifacts before it is treated as a physical result.</p>
        <ul class="workstream-card__points">
          <li><strong>Question:</strong> is an optimization number a real optical/device metric or only a reward/proxy signal?</li>
          <li><strong>Method:</strong> audit metric provenance, then frame expensive PCSEL search as constrained multi-objective black-box optimization.</li>
          <li><strong>Evidence:</strong> Pareto behavior, active-learning history, convergence traces, Q/wavelength outputs, and fabrication-tolerance checks.</li>
        </ul>
      </div>
    </article>

    <article class="workstream-card workstream-card--wide">
      <figure class="workstream-card__media">
        <img src="{{ '/images/research/pcsel_literature_workspace.svg' | relative_url }}" alt="PCSEL literature workspace schematic" loading="lazy">
      </figure>
      <div class="workstream-card__body">
        <span class="workstream-card__tag">Paper library</span>
        <h4>Literature as a design-review layer</h4>
        <p>The paper library is connected to pcsel-agent so that design decisions can be checked against prior reports, not just remembered informally. It supports paper scouting, abstract organization, source-linked claims, and reusable priors for reports or proposals.</p>
        <ul class="workstream-card__points">
          <li><strong>Question:</strong> what has already been reported for a band, material system, geometry, or fabrication route?</li>
          <li><strong>Method:</strong> combine multi-source search, local PDF parsing, wiki pages, and topic/group metadata.</li>
          <li><strong>Evidence:</strong> 101 structured paper entries with searchable methods, device claims, and source context.</li>
        </ul>
      </div>
    </article>
  </div>
</section>

<section class="research-section" markdown="1">
## Companion Projects

<div class="pcsel-companion-grid">
  <article class="pcsel-companion-card">
    <h3>PCSELBook</h3>
    <p><strong>Role:</strong> theory and method backbone. The book records the knowledge chain from Maxwell equations, Bloch modes, photonic bands, PWEM/RCWA/FDTD/FEM, epitaxy, and quantum-well gain to electro-thermal-optical device physics.</p>
    <p><strong>Why it matters:</strong> it turns scattered modeling decisions into a teachable reference, so pcsel-agent can use a stable vocabulary for design variables, solver assumptions, and device constraints.</p>
    <p><a href="https://github.com/wfy-op/PCSELbook">GitHub repository</a> | <a href="{{ '/posts/2026/04/pcselbook/' | relative_url }}">project note</a></p>
  </article>

  <article class="pcsel-companion-card">
    <h3>RLcode</h3>
    <p><strong>Role:</strong> optimization sandbox. RLcode captures the earlier reinforcement-learning direction for PCSEL structural search, including DQN-style action selection and solver-coupled optimization experiments.</p>
    <p><strong>Current lesson:</strong> the strongest value is no longer "RL for its own sake", but a reproducibility discipline: audit metric provenance, separate policy decisions from physical metrics, and compare RL with Bayesian/Pareto/black-box alternatives.</p>
  </article>

  <article class="pcsel-companion-card">
    <h3>Paper Library</h3>
    <p><strong>Role:</strong> evidence memory. The library keeps PCSEL papers, notes, metadata, and extracted design claims in a local wiki so that new device ideas can be checked against prior work quickly.</p>
    <p><strong>Current scope:</strong> 101 structured entries, multi-source ingestion, local PDF parsing, and a research workbench that links literature, run history, pipeline state, and agent memory.</p>
  </article>
</div>
</section>

<section class="research-section" markdown="1">
## Representative PCSEL Figures

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
</section>
