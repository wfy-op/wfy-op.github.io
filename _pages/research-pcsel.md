---
layout: archive
title: "GaAs PCSEL Research"
permalink: /research/pcsel/
author_profile: true
---

<p class="research-intro">
  My PCSEL work is organized around <strong>pcsel-agent</strong>, a reproducible research workflow for GaAs photonic-crystal surface-emitting lasers. The current device target is the 980 nm band, while the 940/980 nm HX1 work is used as a validation and reference track. Instead of treating each simulation as an isolated file, I use pcsel-agent to connect literature intake, device specifications, COMSOL/Lumerical/FDTD execution, solver-syntax memory, metric provenance, and human-readable reports.
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
      <li>HX1 940/980 nm reference validation across GME, FEM, and FDTD routes.</li>
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
## pcsel-agent: Reproducible PCSEL Workflow

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

<section class="research-section" markdown="1">
## Public Evidence Map

<div class="evidence-table-wrap" markdown="1">

| Research thread | Public evidence status | Metrics tracked | Why it matters |
| --- | --- | --- | --- |
| HX1 940/980 nm validation | Sanitized workflow figures and public narrative; detailed run files remain internal while reports are prepared. | Eigenwavelength, Q-factor, mode identity, mesh/boundary checks, field localization. | Separates genuine PCSEL trends from finite-aperture, side-boundary, and mesh artifacts. |
| QW etch-depth risk gate | Public process-risk schematic and exported-geometry audit logic. | Hole depth convention, QW clearance, carrier/thermal risk, sidewall recombination proxy. | Prevents optically attractive designs from violating active-region or process constraints. |
| Backside DBR and gain-band route | Public TMM-first route and literature-backed modeling plan. | Reflectivity, phase response, flux balance, wavelength alignment, active-region coupling. | Keeps expensive 3D verification focused on physically plausible vertical stacks. |
| RLcode and optimization audit | Public description of metric-provenance discipline; code/results are being sanitized before release. | Solver-derived Q/wavelength versus proxy reward, Pareto behavior, convergence trace, fabrication tolerance. | Makes optimization claims auditable before they are presented as physical device results. |

</div>
</section>

<section class="research-section" markdown="1">
## Device Evidence and Experimental Loop

<div class="pcsel-companion-grid">
  <article class="pcsel-companion-card">
    <h3>Simulation evidence</h3>
    <p><strong>Role:</strong> connect geometry to device metrics. My PCSEL sweeps track resonance wavelength, Q-factor, field profile, optical confinement, and sensitivity rather than treating field plots as standalone outputs.</p>
    <p><strong>Typical variables:</strong> lattice constant, air-hole radius, slab thickness, active-region position, and fabrication-feasible etch depth.</p>
  </article>

  <article class="pcsel-companion-card">
    <h3>Device and process context</h3>
    <p><strong>Role:</strong> keep optical designs compatible with epitaxy and process constraints. The current GaAs PCSEL work targets the 980 nm band and connects photonic-crystal design with double-quantum-well active-region assumptions.</p>
    <p><strong>Checks:</strong> ICP etch windows, KLayout mask review, SEM-based deviation analysis, overlay accuracy, and design-to-process correspondence tables.</p>
  </article>

  <article class="pcsel-companion-card">
    <h3>Characterization feedback</h3>
    <p><strong>Role:</strong> close the loop after fabrication. The workflow records optical/electrical pumping, photoluminescence setup, L-I-V curves, spectra, beam profiles, and structural observations.</p>
    <p><strong>Device target:</strong> stable single-mode emission, narrow linewidth, low-divergence surface output, and interpretable links between spectra, far-field behavior, and SEM-verified structure. Public pages describe the target and workflow; quantitative spectra and far-field evidence should be linked when a sanitized dataset/report is ready.</p>
  </article>
</div>
</section>

<section class="research-section" markdown="1">
## Next Research Questions

<div class="highlight-grid">
  <article class="highlight-card">
    <h2>Fabrication-aware inverse design</h2>
    <p>Use SEM-informed etch deviation, overlay tolerance, QW clearance, and mask constraints as explicit optimization variables instead of post-hoc fabrication comments.</p>
  </article>
  <article class="highlight-card">
    <h2>Surrogate-assisted automated search</h2>
    <p>Use solver-backed metrics from COMSOL/Lumerical runs to train interpretable surrogate models that accelerate PCSEL and nanocavity candidate selection.</p>
  </article>
  <article class="highlight-card">
    <h2>Electro-thermal-optical coupling</h2>
    <p>Extend optical mode analysis toward carrier transport, heat flow, gain-region overlap, and device-level performance limits.</p>
  </article>
</div>
</section>

<section class="workstream-showcase" aria-label="pcsel-agent research points">
  <div class="workstream-showcase__header">
    <span class="workstream-showcase__eyebrow">Concrete research points under pcsel-agent</span>
    <h3>From solver automation to device decisions</h3>
    <p>These are the main PCSEL research threads currently organized inside pcsel-agent. The figures are workflow schematics for public explanation; the evidence map above separates public-facing support from internal run artifacts that are still being sanitized.</p>
  </div>

  <div class="workstream-detail-grid">
    <article class="workstream-card">
      <figure class="workstream-card__media">
        <img src="{{ '/images/research/pcsel_finite_array_workflow.svg' | relative_url }}" alt="Finite-array versus periodic-unit-cell PCSEL workflow schematic" loading="lazy">
      </figure>
      <div class="workstream-card__body">
        <span class="workstream-card__tag">HX1 reference validation</span>
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
## Related Project Artifacts

<div class="workstream-panel" markdown="1">
The PCSEL work is supported by three companion artifacts: **PCSELBook** for theory and method vocabulary, **RLcode** for optimization experiments and metric-provenance audits, and a **101-entry PCSEL paper library** for literature-backed design review. I keep their public status and links on the [Projects]({{ '/projects/' | relative_url }}) page so this research page can stay focused on the device evidence chain.
</div>
</section>

<section class="research-section" markdown="1">
## Representative PCSEL Figures

<div class="research-media-grid">
  <figure class="research-figure">
    <img src="{{ '/images/research/pcsel_device_concept.png' | relative_url }}" alt="PCSEL layer schematic showing photonic-crystal feedback and vertical surface emission from a GaAs laser stack" loading="lazy" width="1024" height="448">
    <figcaption>Device-level PCSEL concept linking the photonic-crystal layer to surface emission.</figcaption>
  </figure>
  <figure class="research-figure">
    <img src="{{ '/images/research/pcsel_mode_profile.png' | relative_url }}" alt="PCSEL mode-profile plot used to connect optical confinement and refractive-index context" loading="lazy" width="1124" height="660">
    <figcaption>Mode-profile evidence used to connect field localization, effective-index context, and active-region overlap.</figcaption>
  </figure>
  <figure class="research-figure">
    <img src="{{ '/images/research/pcsel_iv_recombination_curve.jpeg' | relative_url }}" alt="PCSEL electrical-bias simulation plot comparing current and recombination behavior" loading="lazy" width="1227" height="813">
    <figcaption>Electrical-bias simulation output used to reason about current and recombination behavior; a public report should add model condition and English axis labels.</figcaption>
  </figure>
  <figure class="research-figure">
    <img src="{{ '/images/research/pcsel_optical_setup_optimized.jpg' | relative_url }}" alt="Optical characterization setup used for PCSEL photoluminescence and beam-profile measurements" loading="lazy" width="900" height="1200">
    <figcaption>Optical characterization setup for photoluminescence and beam-profile measurements.</figcaption>
  </figure>
</div>
</section>
