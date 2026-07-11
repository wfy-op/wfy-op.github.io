---
layout: archive
title: "GaAs PCSEL Research"
permalink: /research/pcsel/
author_profile: true
---

<p class="research-backlink"><a href="{{ '/research/' | relative_url }}">Back to all research directions</a> · <a href="#pcsel-portal">Open evidence &amp; progress</a></p>

<nav class="section-index" aria-label="PCSEL page sections">
  <a href="#pcsel-question">Question</a>
  <a href="#selected-validation">Validation cases</a>
  <a href="#pcsel-portal">Evidence &amp; progress</a>
  <a href="#public-evidence">Evidence map</a>
  <a href="#pcsel-projects">Project stack</a>
  <a href="#pcsel-agent">pcsel-agent</a>
  <a href="#device-loop">Device loop</a>
  <a href="#next-questions">Next questions</a>
  <a href="#research-threads">Research threads</a>
  <a href="#representative-figures">Figures</a>
</nav>

<section id="pcsel-question" class="research-section" markdown="1">
## Scientific Question

<div class="workstream-panel" markdown="1">
Can a GaAs PCSEL design loop jointly evaluate optical mode quality, fabrication tolerance, and electro-thermal device limits without losing metric provenance? My current answer is to keep each design decision attached to its geometry convention, solver settings, process gate, and experimental or report artifact.
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

  <article class="validation-case">
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
        <div><dt>Boundary</dt><dd><code>screen-reject</code> means “send to process-map review or a full-wave checkpoint”; it never means fab reject.</dd></div>
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

{% include research-portal-dashboard.html %}

<section id="public-evidence" class="research-section" markdown="1">
## Public Evidence Map

<div class="evidence-table-wrap" markdown="1">

| Research thread | Publicly inspectable artifact | Current limitation / risk | Decision value |
| --- | --- | --- | --- |
| HX1 940/980 nm validation | Public workflow figure and narrative; representative mode-profile figure below. | Raw run folders, exact mesh settings, and full Q/wavelength tables remain private until sanitized. | Separates genuine PCSEL trends from finite-aperture, side-boundary, and mesh artifacts. |
| QW etch-depth risk gate | Public process-risk schematic and exported-geometry audit logic. | The current public page explains the gate; it does not yet expose a numeric etch-depth/QW-clearance table. | Prevents optically attractive designs from violating active-region or process constraints. |
| Backside DBR and gain-band route | Public TMM-first route and literature-backed modeling plan. | Full stack parameters and 3D verification artifacts remain private until documentation is cleaned. | Keeps expensive 3D verification focused on physically plausible vertical stacks. |
| RLcode and optimization audit | Public description of metric-provenance discipline and project context. | Code/results are private; reward traces are not presented as physical evidence. | Makes optimization claims auditable before they are interpreted as device results. |
| RLcomsol optimization validation | Public-safe portal panel with three-seed 20-step COMSOL smoke curves and action trajectory figures. | Raw COMSOL models, local run folders, and training internals remain private. | Connects search policy, geometry audit, mode selection, score guards, and repeatability checks. |
| Agent report corpus | Short public summaries and representative figures from local single-file HTML/PDF design-review reports. | Raw reports, NAS paths, solver models, and private tables are not published. | Shows how pcsel-agent turns solver runs into bounded design decisions instead of loose screenshots. |
| Automated design-optimization method | CNIPA patent application accepted: CN 202610820592.4, application date 2026-06-08, titled 半导体激光器自动化设计优化方法及存储介质. | This is an accepted application, not a granted patent; technical details are not exposed on the public page. | Records the formal IP path for the semiconductor-laser automation workflow while keeping public research claims evidence-limited. |

</div>
</section>

<section id="pcsel-projects" class="research-section" markdown="1">
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
      <li>Single-file design-review reports summarized as an agent report corpus with bounded public claims.</li>
      <li>Related CN patent application accepted for semiconductor-laser automated design optimization.</li>
    </ul>
  </article>

  <article class="pcsel-stack-card">
    <span class="pcsel-stack-card__tag">Theory backbone</span>
    <h3>PCSELBook</h3>
    <p>A living technical monograph that connects Maxwell and Bloch-mode foundations, CWT/PWEM/RCWA/FDTD/FEM methods, epitaxy, quantum-well gain, electro-thermal-optical coupling, and practical simulation failure modes.</p>
    <a href="{{ '/posts/2026/04/pcselbook/' | relative_url }}">Read the project note</a>
  </article>

  <article class="pcsel-stack-card">
    <span class="pcsel-stack-card__tag">Solver connection</span>
    <h3>codex-for-comsol-lumerical</h3>
    <p>A public Codex skill repository that keeps COMSOL and Lumerical FDTD connection probes, API/CLI fallback paths, and solver-syntax memory separate from device-specific PCSEL assumptions.</p>
    <a href="https://github.com/wfy-op/codex-for-comsol-lumerical">Open GitHub repository</a>
  </article>

  <article class="pcsel-stack-card">
    <span class="pcsel-stack-card__tag">Optimization code</span>
    <h3>RLcode</h3>
    <p>A reinforcement-learning and optimization codebase used to explore PCSEL structural search. My current emphasis is metric provenance: separating solver-derived physical results from bookkeeping, reward shaping, or proxy objectives.</p>
  </article>

  <article class="pcsel-stack-card">
    <span class="pcsel-stack-card__tag">COMSOL-backed optimization</span>
    <h3>RLcomsol</h3>
    <p>A COMSOL-backed optimization bridge that tests whether search policies remain physically auditable when connected to geometry checks, mode-selection policy, accepted-score guards, multi-seed smoke panels, and reportable run provenance.</p>
    <a href="#rlcomsol">Open evidence panel</a>
  </article>

  <article class="pcsel-stack-card">
    <span class="pcsel-stack-card__tag">Knowledge base</span>
    <h3>Paper Library</h3>
    <p>A local PCSEL literature workspace with <strong>{{ site.data.research_portal.paper_library.records }}</strong> indexed records and <strong>{{ site.data.research_portal.paper_library.standardized_analyses }}</strong> standardized analyses. No design prior is promoted automatically; claims remain linked to review status and source context.</p>
  </article>
</div>
</section>

<section id="pcsel-agent" class="pcsel-agent-panel" markdown="1">
## pcsel-agent: Reproducible PCSEL Workflow

<div class="pcsel-agent-panel__lead" markdown="1">
In addition to simulation results, this direction produces an auditable workflow in which geometry conventions, solver commands, mesh settings, Q-factors, eigenwavelengths, mode identities, and process-risk checks are linked to their source artifacts.
</div>

<figure class="research-wide-figure">
  <img src="{{ '/images/research/pcsel_agent_architecture.svg' | relative_url }}" alt="Architecture diagram of pcsel-agent connecting paper library, PCSELBook, RLcode, experiment feedback, solver adapters, evidence store, and public reports" loading="lazy" width="1360" height="760">
  <figcaption><strong>pcsel-agent architecture.</strong> The diagram shows how literature priors, PCSELBook theory notes, RLcode optimization experiments, and experimental feedback enter a single orchestration layer. COMSOL, Lumerical, Python/TMM tools, KLayout, and SEM checks are treated as evidence-producing adapters rather than isolated software islands.</figcaption>
</figure>

<div class="figure-explainer">
  <p><strong>How to read the diagram:</strong> inputs on the left define the research question, pcsel-agent in the center records specifications and run manifests, solver/process adapters on the right produce auditable artifacts, and the report/design-review layer helps distinguish private artifacts from results that are sufficiently documented for public reporting.</p>
  <p><strong>Why it matters:</strong> this structure prevents a PCSEL result from being described only by a screenshot or a reward value; each wavelength, Q-factor, mode identity, DBR conclusion, or QW etch-risk statement needs a traceable source. The public <a href="https://github.com/wfy-op/codex-for-comsol-lumerical">codex-for-comsol-lumerical</a> repository documents the generic solver-connection layer behind this practice.</p>
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

<div class="agent-report-corpus" id="agent-report-corpus">
  <div class="agent-report-corpus__header">
    <span class="workstream-showcase__eyebrow">Agent subproject: report corpus</span>
    <h3>Short public summaries from solver-facing agent reports</h3>
    <p>The local report store contains single-file HTML/PDF reports generated during PCSEL design reviews. I summarize them here as evidence-status cards: each card keeps the decision value and one representative figure, while raw reports, local paths, solver models, and private tables remain outside the public site.</p>
  </div>

  <div class="agent-report-grid">
    <article class="agent-report-card">
      <figure class="agent-report-card__media">
        <img src="{{ '/images/research/agent-reports/agent_report_650_model.png' | relative_url }}" alt="COMSOL model check from the 650 nm PCSEL engineering screen" loading="lazy">
      </figure>
      <div class="agent-report-card__body">
        <span class="agent-report-card__tag">Engineering screen</span>
        <h4>650 nm PCSEL baseline review</h4>
        <p>The report treats a single-round-hole square lattice as a baseline rather than a final 650 nm PCSEL design. Its value is the negative screen: overlap, loss, and out-coupling did not close simultaneously into a convincing device route.</p>
        <p class="agent-report-card__meta">Evidence: computed COMSOL/FDTD report. Claim: baseline screening, not device sign-off.</p>
      </div>
    </article>

    <article class="agent-report-card">
      <figure class="agent-report-card__media">
        <img src="{{ '/images/research/agent-reports/agent_report_source_sweep_q.png' | relative_url }}" alt="FDTD source sweep Q-factor comparison for 980 nm PCSEL probes" loading="lazy">
      </figure>
      <div class="agent-report-card__body">
        <span class="agent-report-card__tag">Gain and source rules</span>
        <h4>980 nm gain window and FDTD source selection</h4>
        <p>Threshold-gain, QW gain-spectrum, and FDTD source-setting reports are grouped as screening rules. They separate realistic QW electric-dipole probes from high-Q search probes that are useful for finding modes but should not be interpreted as direct emission likelihood.</p>
        <p class="agent-report-card__meta">Evidence: screening-level gain/source reports. Claim: source and gain-window guidance.</p>
      </div>
    </article>

    <article class="agent-report-card">
      <figure class="agent-report-card__media">
        <img src="{{ '/images/research/agent-reports/agent_report_fdtd_comsol.png' | relative_url }}" alt="HX1-940 FDTD and COMSOL Q-factor comparison by hole depth" loading="lazy">
      </figure>
      <div class="agent-report-card__body">
        <span class="agent-report-card__tag">Solver cross-check</span>
        <h4>HX1-940 sweep and FDTD-vs-COMSOL comparison</h4>
        <p>HX1-940 sweep reports connect hole depth, wavelength, Q, and model identity across COMSOL and FDTD. The comparison is useful for debugging mode tracking and boundary/model differences, not for claiming final laser performance.</p>
        <p class="agent-report-card__meta">Evidence: solver cross-check. Claim: model-consistency audit with explicit limits.</p>
      </div>
    </article>

    <article class="agent-report-card">
      <figure class="agent-report-card__media">
        <img src="{{ '/images/research/agent-reports/agent_report_ito_intrusion.png' | relative_url }}" alt="HX1 ITO intrusion eigenwavelength and Q-factor comparison" loading="lazy">
      </figure>
      <div class="agent-report-card__body">
        <span class="agent-report-card__tag">Process sensitivity</span>
        <h4>ITO intrusion, bottom grass, and hole-shape defects</h4>
        <p>These reports turn SEM/process observations into simplified COMSOL perturbations: ITO filling/top film, bottom grass residues, and InP hole or sidewall defects. The goal is to rank sensitivity and expose geometry assumptions before a design is treated as fabrication-ready.</p>
        <p class="agent-report-card__meta">Evidence: computed sensitivity screens. Claim: process-risk ranking, not optimized geometry.</p>
      </div>
    </article>

    <article class="agent-report-card">
      <figure class="agent-report-card__media">
        <img src="{{ '/images/research/agent-reports/agent_report_bottom_fillet.svg' | relative_url }}" alt="HX1-940 bottom fillet radius tradeoff report figure" loading="lazy">
      </figure>
      <div class="agent-report-card__body">
        <span class="agent-report-card__tag">Geometry perturbation</span>
        <h4>Bottom fillet rerun for HX1-940</h4>
        <p>The bottom-fillet report is a fresh 20-mode COMSOL rerun that keeps the straight-bottom reference separate from the rounded-bottom cases. In the 940 +/- 1 nm target window, nonzero bottom radius reduces the selected-mode Q, with the 5 nm case retaining the strongest nonzero-radius candidate in this screen.</p>
        <p class="agent-report-card__meta">Evidence: fresh 20-mode COMSOL rerun. Claim: fillet sensitivity under the current approximation.</p>
      </div>
    </article>

    <article class="agent-report-card">
      <figure class="agent-report-card__media">
        <img src="{{ '/images/research/agent-reports/agent_report_dbr_reflectance.png' | relative_url }}" alt="GaAs AlAs DBR reflectance versus pair count from the HX1-940 DBR workflow" loading="lazy">
      </figure>
      <div class="agent-report-card__body">
        <span class="agent-report-card__tag">Vertical boundary</span>
        <h4>Backside DBR TMM-first workflow</h4>
        <p>The DBR report runs a two-stage workflow: fast 1D GaAs/AlAs TMM screening, then a small COMSOL smoke check with a backside DBR. It keeps reflectance, phase, Q, eigenwavelength, and field localization in one review path.</p>
        <p class="agent-report-card__meta">Evidence: TMM screen plus COMSOL smoke check. Claim: workflow validation, not final DBR sign-off.</p>
      </div>
    </article>
  </div>
</div>
</section>

<section id="device-loop" class="research-section" markdown="1">
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
    <p><strong>Device target:</strong> single-mode operation, narrow-linewidth behavior, low-divergence surface output, and interpretable links between spectra, far-field behavior, and SEM-verified structure. These are target criteria; quantitative spectra and far-field evidence should be linked when a documented dataset/report is ready.</p>
  </article>
</div>
</section>

<section id="next-questions" class="research-section" markdown="1">
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

<section id="research-threads" class="workstream-showcase" aria-label="pcsel-agent research points">
  <div class="workstream-showcase__header">
    <span class="workstream-showcase__eyebrow">Concrete research points under pcsel-agent</span>
    <h3>From solver automation to device decisions</h3>
    <p>These are the main PCSEL research threads currently organized inside pcsel-agent. The figures are workflow schematics for public explanation; the evidence map above separates public-facing support from private run artifacts that still need documentation before release.</p>
  </div>

  <div class="workstream-detail-grid">
    <article class="workstream-card">
      <figure class="workstream-card__media">
        <img src="{{ '/images/research/pcsel_finite_array_workflow.svg' | relative_url }}" alt="Finite-array versus periodic-unit-cell PCSEL workflow schematic" loading="lazy">
        <figcaption>Validation path for comparing periodic-cell assumptions with finite-array and full-wave checks.</figcaption>
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
        <figcaption>Process gate that keeps QW clearance, etch-front convention, and sidewall risk attached to every optical design point.</figcaption>
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
        <figcaption>TMM-first route for filtering vertical DBR/gain-band choices before expensive 3D simulation.</figcaption>
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
        <figcaption>Optimization audit path separating solver-derived metrics from reward shaping and proxy objectives.</figcaption>
      </figure>
      <div class="workstream-card__body">
        <span class="workstream-card__tag">Optimization trust</span>
        <h4>From RLcode experiments to RLcomsol validation</h4>
        <p>RLcode serves as the exploration sandbox, while RLcomsol connects search policies to COMSOL-backed PCSEL metrics and pcsel-agent adds provenance checks. Candidate designs are linked to solver-derived metrics, design constraints, accepted-score guards, and reproducible artifacts before being interpreted as physical results.</p>
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
        <figcaption>Literature workspace used to turn paper intake into searchable design priors and source-linked claims.</figcaption>
      </figure>
      <div class="workstream-card__body">
        <span class="workstream-card__tag">Paper library</span>
        <h4>Literature as a design-review layer</h4>
        <p>The paper library is connected to pcsel-agent so that design decisions can be checked against prior reports, not just remembered informally. It supports paper scouting, abstract organization, source-linked claims, and reusable priors for reports or proposals.</p>
        <ul class="workstream-card__points">
          <li><strong>Question:</strong> what has already been reported for a band, material system, geometry, or fabrication route?</li>
          <li><strong>Method:</strong> combine multi-source search, local PDF parsing, wiki pages, and topic/group metadata.</li>
          <li><strong>Evidence:</strong> {{ site.data.research_portal.paper_library.records }} indexed records, {{ site.data.research_portal.paper_library.standardized_analyses }} standardized analyses, and {{ site.data.research_portal.paper_library.design_priors_auto_promoted }} auto-promoted design priors.</li>
        </ul>
      </div>
    </article>
  </div>
</section>

<section id="related-project-artifacts" class="research-section" markdown="1">
## Related Project Artifacts

<div class="workstream-panel" markdown="1">
The PCSEL work is supported by companion artifacts: **PCSELBook** for theory and method vocabulary, public **codex-for-comsol-lumerical** skills for solver connection, **RLcode** for optimization experiments, **RLcomsol** for COMSOL-backed search validation, and a **{{ site.data.research_portal.paper_library.records }}-record indexed literature workspace** for source-linked review. The [research software page]({{ '/projects/' | relative_url }}) keeps public links and release boundaries together, while [Evidence & Progress](#pcsel-portal) reports reproducible aggregate status.
</div>
</section>

<section id="representative-figures" class="research-section" markdown="1">
## Representative PCSEL Figures

<div class="research-media-grid">
  <figure class="research-figure">
    <img src="{{ '/images/research/pcsel_device_concept.png' | relative_url }}" alt="PCSEL layer schematic showing photonic-crystal feedback and vertical surface emission from a GaAs laser stack" loading="lazy" width="1024" height="448">
    <figcaption><span class="evidence-badge">Concept schematic</span><strong>Device concept.</strong> This figure frames the target device class: a GaAs PCSEL stack where the photonic-crystal layer supplies in-plane feedback and couples the resonant mode toward vertical surface emission.</figcaption>
  </figure>
  <figure class="research-figure">
    <img src="{{ '/images/research/pcsel_mode_profile.png' | relative_url }}" alt="PCSEL mode-profile plot used to connect optical confinement and refractive-index context" loading="lazy" width="1124" height="660">
    <figcaption><span class="evidence-badge evidence-badge--quant">Quantitative simulation evidence</span><strong>Mode-profile evidence.</strong> The plot is used to inspect field localization, vertical confinement, and active-region overlap before interpreting a wavelength/Q result as a device-relevant candidate. It supports confinement reasoning, not by itself a device-performance claim.</figcaption>
  </figure>
  <figure class="research-figure">
    <img src="{{ '/images/research/pcsel_iv_recombination_curve.jpeg' | relative_url }}" alt="Preliminary PCSEL electrical-bias simulation with Chinese axis labels pending relabeling" loading="lazy" width="1227" height="813">
    <figcaption><span class="evidence-badge evidence-badge--prelim">Preliminary simulation</span><strong>Electrical-bias context.</strong> This output is kept as process/device context for current injection and recombination behavior. It is not public quantitative evidence yet; model conditions, structure parameters, and English axis labels should be added before using it as a result figure.</figcaption>
  </figure>
  <figure class="research-figure">
    <img src="{{ '/images/research/pcsel_optical_setup_optimized.jpg' | relative_url }}" alt="Optical characterization setup used for PCSEL photoluminescence and beam-profile measurements" loading="lazy" width="900" height="1200">
    <figcaption><span class="evidence-badge evidence-badge--setup">Experimental setup only</span><strong>Characterization setup.</strong> The optical bench documents measurement capability for photoluminescence, spectra, and beam-profile work. Spectra, calibration, beam profiles, and sample identity are required before using the setup as experimental performance evidence.</figcaption>
  </figure>
</div>
</section>
