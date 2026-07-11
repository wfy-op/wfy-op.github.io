---
layout: archive
title: "GaAs PCSEL Research"
permalink: /research/pcsel/
author_profile: true
---

<p class="research-backlink"><a href="{{ '/research/' | relative_url }}">Back to all research directions</a> · <a href="#pcsel-portal">Open evidence &amp; progress</a></p>

<nav class="section-index" aria-label="PCSEL page sections">
  <a href="#pcsel-overview">Overview</a>
  <a href="#selected-validation">Validation</a>
  <a href="#research-threads">Research threads</a>
  <a href="#pcsel-portal">Evidence &amp; progress</a>
  <a href="#pcsel-system">Research system</a>
  <a href="#next-questions">Next questions</a>
</nav>

<section id="pcsel-overview" class="research-section" markdown="1">
## Program Overview

<div class="pcsel-program-overview">
  <figure class="pcsel-program-overview__media">
    <img src="{{ '/images/research/pcsel_device_concept.png' | relative_url }}" alt="GaAs PCSEL layer stack linking photonic-crystal feedback with vertical surface emission" width="1024" height="448">
    <figcaption>The photonic-crystal layer couples in-plane feedback to vertical emission; the research problem is to preserve that optical function under numerical and fabrication constraints.</figcaption>
  </figure>
  <div class="pcsel-program-overview__body">
    <span class="home-research-card__tag">Primary research program · 940/980 nm GaAs</span>
    <h2>Evidence-gated design, not isolated high-Q points</h2>
    <p class="pcsel-program-overview__lead">I use pcsel-agent to connect literature, full-wave modeling, process constraints, and characterization feedback into one traceable PCSEL design loop.</p>
    <dl class="pcsel-program-overview__facts">
      <div><dt>Question</dt><dd>Can optical mode quality, fabrication tolerance, and electro-thermal limits be evaluated without losing metric provenance?</dd></div>
      <div><dt>Method</dt><dd>Cross-check COMSOL, Lumerical, reduced models, geometry audits, and experiment-facing process evidence.</dd></div>
      <div><dt>Decision rule</dt><dd>A candidate advances only when mode identity, convergence, process feasibility, and claim boundaries are explicit.</dd></div>
    </dl>
  </div>
</div>
</section>

<section id="selected-validation" class="research-section" markdown="1">
## Selected Validation Cases

<div class="validation-case-grid">
  <article class="validation-case validation-case--wide">
    <figure class="validation-case__media">
      <img src="{{ '/images/research/validation/apl2018_mode_localization_progression.png' | relative_url }}" alt="APL 2018 diagnostic progression showing recovery of a localized branch as the active-core model is revised" loading="lazy" width="2048" height="1024">
    </figure>
    <div class="validation-case__body">
      <div class="validation-case__meta">
        <span class="evidence-status evidence-status--diagnostic">Diagnostic only</span>
        <span>Mode identity · July 2026</span>
      </div>
      <h3>Mode-localization gate</h3>
      <p class="validation-case__finding">A localization filter overturned a misleading high-Q depth sweep.</p>
      <dl class="validation-case__facts">
        <div><dt>Finding</dt><dd>The original highest-Q modes were concentrated in the substrate and lower buffer, with nearly zero PC/QW overlap. An active390 diagnostic surrogate recovered a localized branch near 926-927 nm.</dd></div>
        <div><dt>Boundary</dt><dd>The surrogate diagnoses the root cause but is not a strict reproduction of the reported 928.6 nm device and is not a device sign-off.</dd></div>
      </dl>
    </div>
  </article>

  <article class="validation-case">
    <figure class="validation-case__media">
      <img src="{{ '/images/research/validation/hx1_buffer_convergence.svg' | relative_url }}" alt="HX1-940 COMSOL Q-factor sensitivity to GaAs buffer thickness" loading="lazy" width="920" height="460">
    </figure>
    <div class="validation-case__body">
      <div class="validation-case__meta">
        <span class="evidence-status evidence-status--fullwave">Full-wave result</span>
        <span>COMSOL eigenfrequency</span>
      </div>
      <h3>Boundary and convergence audit</h3>
      <p class="validation-case__finding">Substrate-buffer and PML choices materially changed the Q ranking.</p>
      <dl class="validation-case__facts">
        <div><dt>Finding</dt><dd>Near-target modes remained sensitive to vertical-domain choices, so high Q was treated as boundary-conditioned evidence rather than an intrinsic device number.</dd></div>
        <div><dt>Boundary</dt><dd>Cold-cavity unit-cell screening under the documented model; it does not predict threshold, far field, or fabricated-device performance.</dd></div>
      </dl>
    </div>
  </article>

  <article class="validation-case">
    <figure class="validation-case__media">
      <img src="{{ '/images/research/validation/sch400_failure_modes.png' | relative_url }}" alt="SCH400 optimizer feasibility and failure-mode counts across five search seeds" loading="lazy" width="1586" height="768">
    </figure>
    <div class="validation-case__body">
      <div class="validation-case__meta">
        <span class="evidence-status evidence-status--nogo">No-go</span>
        <span>Five seeds · 512-point holdout</span>
      </div>
      <h3>SCH400 candidate rejection</h3>
      <p class="validation-case__finding">No candidate passed the pre-registered process-recommendation gates.</p>
      <dl class="validation-case__facts">
        <div><dt>Finding</dt><dd>The closest diagnostic candidate improved paired overlap metrics, but failed the PC P10, absolute Wilson-LCB, discovery-eligibility, and local-rank gates.</dd></div>
        <div><dt>Boundary</dt><dd>This is a 1D vertical-overlap screen. It has no 3D Bloch-mode identity, eigenwavelength, or cavity-Q sign-off.</dd></div>
      </dl>
    </div>
  </article>

  <article class="validation-case validation-case--wide">
    <figure class="validation-case__media">
      <img src="{{ '/images/research/validation/hx1_uniformity_morphology_screen.png' | relative_url }}" alt="HX1-940 two-dimensional surrogate comparison of critical disorder morphologies" loading="lazy" width="2048" height="724">
    </figure>
    <div class="validation-case__body">
      <div class="validation-case__meta">
        <span class="evidence-status evidence-status--surrogate">Surrogate screening</span>
        <span>2D effective-index model</span>
      </div>
      <h3>Fabrication-morphology screen</h3>
      <p class="validation-case__finding">Spatial structure was more informative than RMS error alone.</p>
      <dl class="validation-case__facts">
        <div><dt>Finding</dt><dd>Slow, low-frequency, connected, and clustered perturbations were more damaging than independent single-hole white noise at comparable RMS detuning.</dd></div>
        <div><dt>Boundary</dt><dd><code>screen-reject</code> means "send to process-map review or a full-wave checkpoint"; it never means fab reject.</dd></div>
      </dl>
    </div>
  </article>

  <article class="validation-case validation-case--wide">
    <figure class="validation-case__media">
      <img src="{{ '/images/research/validation/sch_mode_fde_profile.png' | relative_url }}" alt="Lumerical MODE FDE vertical mode profile used in the APL 2018 SCH reproduction ladder" loading="lazy" width="2048" height="1135">
    </figure>
    <div class="validation-case__body">
      <div class="validation-case__meta">
        <span class="evidence-status evidence-status--crosssolver">Cross-solver check</span>
        <span>Python 1D · Lumerical MODE/FDE</span>
      </div>
      <h3>Literature reproduction ladder</h3>
      <p class="validation-case__finding">The APL 2018 SCH trend survived a staged 1D-to-FDE validation path.</p>
      <dl class="validation-case__facts">
        <div><dt>Finding</dt><dd>The tuned 3QW MODE/FDE sweep accepted 219 of 225 guided-active points; the paper's 30/70 nm point reached 96.99% of the accepted peak.</dd></div>
        <div><dt>Boundary</dt><dd>This supports a semi-quantitative trend and mode-selection workflow, not a complete reproduction of the paper's full PCSEL device.</dd></div>
      </dl>
    </div>
  </article>
</div>
</section>

<section id="research-threads" class="workstream-showcase" aria-label="pcsel-agent research points">
  <div class="workstream-showcase__header">
    <span class="workstream-showcase__eyebrow">Research points under pcsel-agent</span>
    <h2>From solver output to device decisions</h2>
    <p>Five connected workstreams organize the current program. Each figure shows the model or review route; the evidence labels above and progress modules below state what has actually closed.</p>
  </div>

  <div class="workstream-detail-grid">
    <article class="workstream-card">
      <figure class="workstream-card__media">
        <img src="{{ '/images/research/pcsel_finite_array_workflow.svg' | relative_url }}" alt="Finite-array versus periodic-unit-cell PCSEL workflow schematic" loading="lazy">
        <figcaption>Periodic-cell trends are checked against finite-array and full-wave references.</figcaption>
      </figure>
      <div class="workstream-card__body">
        <span class="workstream-card__tag">Model credibility</span>
        <h3>HX1 940/980 nm validation across model scales</h3>
        <p>GME-style references, COMSOL eigenfrequency studies, and FDTD checks are compared with controlled lattice, hole, boundary, and mesh conventions.</p>
        <p><strong>Decision evidence:</strong> mode identity, field localization, radiation channel, convergence, and Q/wavelength consistency.</p>
      </div>
    </article>

    <article class="workstream-card">
      <figure class="workstream-card__media">
        <img src="{{ '/images/research/pcsel_qw_etch_risk_gate.svg' | relative_url }}" alt="Quantum-well etch-depth risk gate schematic" loading="lazy">
        <figcaption>QW clearance and etch-front convention stay attached to each optical design point.</figcaption>
      </figure>
      <div class="workstream-card__body">
        <span class="workstream-card__tag">Process-aware design</span>
        <h3>Etch depth, morphology, and sidewall-risk gates</h3>
        <p>Optically attractive points are checked against QW exposure, ITO intrusion, bottom grass, bottom fillet, hole shape, sidewall defects, and mask/layout constraints.</p>
        <p><strong>Decision evidence:</strong> exported geometry, forbidden-region checks, sensitivity ranking, and process-map review.</p>
      </div>
    </article>

    <article class="workstream-card">
      <figure class="workstream-card__media">
        <img src="{{ '/images/research/pcsel_backside_dbr_tmm_route.svg' | relative_url }}" alt="Backside DBR TMM-first simulation route schematic" loading="lazy">
        <figcaption>TMM and gain-band screens filter vertical-stack choices before 3D verification.</figcaption>
      </figure>
      <div class="workstream-card__body">
        <span class="workstream-card__tag">Vertical stack and gain</span>
        <h3>Backside DBR and quantum-well gain route</h3>
        <p>Fast transfer-matrix and gain-spectrum calculations narrow the stack and wavelength space before expensive full-wave solver runs.</p>
        <p><strong>Decision evidence:</strong> reflectance and phase, active-region coupling, wavelength alignment, flux balance, and PML sanity.</p>
      </div>
    </article>

    <article class="workstream-card">
      <figure class="workstream-card__media">
        <img src="{{ '/images/research/pcsel_optimization_map.svg' | relative_url }}" alt="FDTD-driven black-box multi-objective optimization schematic" loading="lazy">
        <figcaption>Optimization metrics remain separate from reward shaping and proxy objectives.</figcaption>
      </figure>
      <div class="workstream-card__body">
        <span class="workstream-card__tag">Optimization trust</span>
        <h3>From RLcode experiments to RLcomsol validation</h3>
        <p>RLcode is the exploration sandbox; RLcomsol connects candidate search to geometry checks, mode-selection policy, accepted-score guards, and multi-seed COMSOL smoke panels.</p>
        <p><strong>Decision evidence:</strong> solver-derived metrics, action history, repeatability, constraint status, and bounded optimization claims.</p>
      </div>
    </article>

    <article class="workstream-card workstream-card--wide">
      <figure class="workstream-card__media">
        <img src="{{ '/images/research/pcsel_literature_workspace.svg' | relative_url }}" alt="PCSEL literature workspace schematic" loading="lazy">
        <figcaption>Paper intake becomes searchable, source-linked design context rather than an informal reading list.</figcaption>
      </figure>
      <div class="workstream-card__body">
        <span class="workstream-card__tag">Theory and literature</span>
        <h3>PCSELBook and the paper library as review layers</h3>
        <p>PCSELBook provides the theory and method vocabulary; the indexed paper library supports source-linked checks across bands, material systems, geometries, fabrication routes, and reported evidence.</p>
        <p><strong>Current snapshot:</strong> {{ site.data.research_portal.paper_library.records }} indexed records, {{ site.data.research_portal.paper_library.standardized_analyses }} standardized analyses, and {{ site.data.research_portal.paper_library.design_priors_auto_promoted }} auto-promoted design priors.</p>
      </div>
    </article>
  </div>
</section>

{% include research-portal-dashboard.html %}

<section id="pcsel-system" class="pcsel-agent-panel" markdown="1">
## Research System and Public Artifacts

<figure class="research-wide-figure">
  <img src="{{ '/images/research/pcsel_agent_architecture.svg' | relative_url }}" alt="Architecture diagram of pcsel-agent connecting paper library, PCSELBook, optimization, experiment feedback, solvers, evidence, and reports" loading="lazy" width="1360" height="760">
  <figcaption><strong>pcsel-agent architecture.</strong> Literature and theory define questions; orchestration records specifications and run manifests; solver and process adapters produce auditable artifacts; reports expose only evidence that has a clear public boundary.</figcaption>
</figure>

<div class="pcsel-agent-map">
  <div class="pcsel-agent-map__item"><span>1</span><strong>Define</strong><p>Literature priors, device targets, geometry conventions, and process constraints.</p></div>
  <div class="pcsel-agent-map__item"><span>2</span><strong>Execute</strong><p>COMSOL, Lumerical, Python/TMM, KLayout, and SEM-facing review workflows.</p></div>
  <div class="pcsel-agent-map__item"><span>3</span><strong>Verify</strong><p>Mode identity, mesh and boundary checks, geometry audits, and accepted-score guards.</p></div>
  <div class="pcsel-agent-map__item"><span>4</span><strong>Report</strong><p>Source-linked figures, decision status, limitations, and public/private release boundaries.</p></div>
</div>

<div class="pcsel-stack-grid">
  <article class="pcsel-stack-card pcsel-stack-card--primary">
    <span class="pcsel-stack-card__tag">Core system</span>
    <h3>pcsel-agent</h3>
    <p>A Python and agent workflow connecting paper intake, design briefs, COMSOL/Lumerical execution, verified syntax memory, artifact checks, and design-review reports.</p>
  </article>
  <article class="pcsel-stack-card">
    <span class="pcsel-stack-card__tag">Theory backbone</span>
    <h3>PCSELBook</h3>
    <p>A living technical monograph spanning Maxwell/Bloch foundations, CWT and full-wave methods, epitaxy, gain, and coupled device physics.</p>
    <a href="{{ '/posts/2026/04/pcselbook/' | relative_url }}">Read the project note</a>
  </article>
  <article class="pcsel-stack-card">
    <span class="pcsel-stack-card__tag">Knowledge base</span>
    <h3>PCSEL Paper Library</h3>
    <p>{{ site.data.research_portal.paper_library.records }} indexed records and {{ site.data.research_portal.paper_library.standardized_analyses }} standardized analyses, with no automatic promotion into design priors.</p>
  </article>
  <article class="pcsel-stack-card">
    <span class="pcsel-stack-card__tag">Public solver layer</span>
    <h3>codex-for-comsol-lumerical</h3>
    <p>Reusable connection probes, API/CLI fallbacks, and verified solver-syntax memory kept separate from device-specific assumptions.</p>
    <a href="https://github.com/wfy-op/codex-for-comsol-lumerical">Open GitHub repository</a>
  </article>
  <article class="pcsel-stack-card">
    <span class="pcsel-stack-card__tag">Optimization layer</span>
    <h3>RLcode and RLcomsol</h3>
    <p>Exploration code and a COMSOL-backed bridge for testing whether candidate search remains tied to geometry, mode, score, and repeatability checks.</p>
    <a href="#rlcomsol">Open the RLcomsol evidence module</a>
  </article>
  <article class="pcsel-stack-card">
    <span class="pcsel-stack-card__tag">Intellectual property</span>
    <h3>Automated semiconductor-laser design</h3>
    <p>CNIPA application CN 202610820592.4, accepted 2026-06-08. This is an accepted patent application, not a granted patent.</p>
  </article>
</div>

<details class="agent-report-disclosure">
  <summary>
    <span><strong>Agent report corpus</strong><small>Six solver-facing report groups with representative computed figures</small></span>
    <span class="disclosure-state" aria-hidden="true"></span>
  </summary>
  <div class="agent-report-disclosure__body">
    <p>The local report store contains single-file HTML/PDF design reviews. The public cards retain the decision value and one figure while raw reports, private paths, solver models, and internal tables remain unpublished.</p>
    <div class="agent-report-grid">
      <article class="agent-report-card">
        <figure class="agent-report-card__media"><img src="{{ '/images/research/agent-reports/agent_report_650_model.png' | relative_url }}" alt="COMSOL model check from the 650 nm PCSEL engineering screen" loading="lazy"></figure>
        <div class="agent-report-card__body"><span class="agent-report-card__tag">Engineering screen</span><h3>650 nm baseline review</h3><p>A round-hole square lattice was rejected as a final route because overlap, loss, and out-coupling did not close simultaneously.</p><p class="agent-report-card__meta">Computed COMSOL/FDTD report · baseline screen, not device sign-off.</p></div>
      </article>
      <article class="agent-report-card">
        <figure class="agent-report-card__media"><img src="{{ '/images/research/agent-reports/agent_report_source_sweep_q.png' | relative_url }}" alt="FDTD source sweep Q-factor comparison for 980 nm PCSEL probes" loading="lazy"></figure>
        <div class="agent-report-card__body"><span class="agent-report-card__tag">Gain and source rules</span><h3>980 nm gain window and source selection</h3><p>Threshold-gain, QW gain-spectrum, and source-setting reports separate realistic dipole probes from high-Q mode-search probes.</p><p class="agent-report-card__meta">Screening guidance · not direct emission-likelihood evidence.</p></div>
      </article>
      <article class="agent-report-card">
        <figure class="agent-report-card__media"><img src="{{ '/images/research/agent-reports/agent_report_fdtd_comsol.png' | relative_url }}" alt="HX1-940 FDTD and COMSOL Q-factor comparison by hole depth" loading="lazy"></figure>
        <div class="agent-report-card__body"><span class="agent-report-card__tag">Solver cross-check</span><h3>HX1-940 FDTD versus COMSOL</h3><p>Hole depth, wavelength, Q, and model identity are compared to expose mode-tracking and boundary differences.</p><p class="agent-report-card__meta">Model-consistency audit · not final laser performance.</p></div>
      </article>
      <article class="agent-report-card">
        <figure class="agent-report-card__media"><img src="{{ '/images/research/agent-reports/agent_report_ito_intrusion.png' | relative_url }}" alt="HX1 ITO intrusion eigenwavelength and Q-factor comparison" loading="lazy"></figure>
        <div class="agent-report-card__body"><span class="agent-report-card__tag">Process sensitivity</span><h3>ITO, bottom grass, and hole defects</h3><p>SEM/process observations are translated into simplified perturbations to rank sensitivity and expose geometry assumptions.</p><p class="agent-report-card__meta">Computed sensitivity screen · not optimized geometry.</p></div>
      </article>
      <article class="agent-report-card">
        <figure class="agent-report-card__media"><img src="{{ '/images/research/agent-reports/agent_report_bottom_fillet.svg' | relative_url }}" alt="HX1-940 bottom fillet radius tradeoff report figure" loading="lazy"></figure>
        <div class="agent-report-card__body"><span class="agent-report-card__tag">Geometry perturbation</span><h3>Bottom fillet rerun</h3><p>A fresh 20-mode COMSOL rerun keeps the straight-bottom reference separate and shows lower selected-mode Q for nonzero radii in the current approximation.</p><p class="agent-report-card__meta">Fresh COMSOL rerun · fillet sensitivity only.</p></div>
      </article>
      <article class="agent-report-card">
        <figure class="agent-report-card__media"><img src="{{ '/images/research/agent-reports/agent_report_dbr_reflectance.png' | relative_url }}" alt="GaAs AlAs DBR reflectance versus pair count from the HX1-940 workflow" loading="lazy"></figure>
        <div class="agent-report-card__body"><span class="agent-report-card__tag">Vertical boundary</span><h3>Backside DBR TMM-first workflow</h3><p>Fast GaAs/AlAs TMM screening is followed by a small COMSOL smoke check linking reflectance, phase, Q, wavelength, and localization.</p><p class="agent-report-card__meta">Workflow validation · not final DBR sign-off.</p></div>
      </article>
    </div>
  </div>
</details>

<div class="pcsel-device-loop">
  <figure class="pcsel-device-loop__media">
    <img src="{{ '/images/research/pcsel_optical_setup_optimized.jpg' | relative_url }}" alt="Optical characterization setup used for PCSEL photoluminescence and beam-profile measurements" loading="lazy" width="900" height="1200">
    <figcaption>Characterization capability for photoluminescence, spectra, and beam-profile work; quantitative device claims require linked sample data and calibration.</figcaption>
  </figure>
  <div class="pcsel-device-loop__body">
    <span class="home-research-card__tag">Device and experiment loop</span>
    <h3>Simulation, process, and measurement stay connected</h3>
    <ul>
      <li><strong>Simulation:</strong> wavelength, Q, mode profile, confinement, and sensitivity.</li>
      <li><strong>Process:</strong> ICP etch windows, KLayout mask review, SEM deviations, overlay, and design-to-process correspondence.</li>
      <li><strong>Characterization:</strong> optical/electrical pumping, L-I-V, spectra, beam profiles, and structural feedback.</li>
    </ul>
  </div>
</div>

<details class="system-disclosure">
  <summary>
    <span><strong>Public claim boundaries</strong><small>What each workstream can and cannot currently support</small></span>
    <span class="disclosure-state" aria-hidden="true"></span>
  </summary>
  <div class="evidence-table-wrap">
    <table>
      <thead><tr><th>Research thread</th><th>Current public evidence</th><th>Interpretation boundary</th></tr></thead>
      <tbody>
        <tr><td>HX1 validation</td><td>Mode-localization, convergence, sweep, and solver-comparison figures.</td><td>Raw models and full run tables remain private; no fabricated-device performance claim.</td></tr>
        <tr><td>QW and process gates</td><td>Etch-risk and morphology screens plus summarized agent reports.</td><td>Surrogates rank risk; they do not issue fabrication rejection.</td></tr>
        <tr><td>DBR and gain route</td><td>TMM-first workflow and COMSOL smoke-check summaries.</td><td>Full stack parameters and final 3D sign-off remain private.</td></tr>
        <tr><td>RLcode / RLcomsol</td><td>Three-seed smoke-panel curves and aggregate provenance status.</td><td>No global-optimum claim; raw COMSOL and training artifacts remain private.</td></tr>
        <tr><td>Patent application</td><td>CN 202610820592.4 acceptance information.</td><td>Accepted application, not a granted patent; technical details are not disclosed here.</td></tr>
      </tbody>
    </table>
  </div>
</details>
</section>

<section id="next-questions" class="research-section" markdown="1">
## Next Research Questions

<div class="highlight-grid">
  <article class="highlight-card">
    <h2>Fabrication-aware inverse design</h2>
    <p>Make SEM-informed etch deviation, overlay tolerance, QW clearance, and mask constraints part of the optimization problem rather than post-hoc comments.</p>
  </article>
  <article class="highlight-card">
    <h2>Interpretable surrogate search</h2>
    <p>Use solver-backed COMSOL/Lumerical metrics to accelerate candidate selection while preserving mode identity, uncertainty, and decision provenance.</p>
  </article>
  <article class="highlight-card">
    <h2>Electro-thermal-optical closure</h2>
    <p>Extend cold-cavity analysis toward carrier transport, heat flow, gain-region overlap, and measured device-level limits.</p>
  </article>
</div>
</section>
