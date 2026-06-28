---
layout: archive
title: "Research Portal"
permalink: /research/portal/
author_profile: true
---

{% assign portal = site.data.research_portal %}

<section class="portal-hero">
  <p class="profile-hero__eyebrow">Research outcome portal</p>
  <h1>Evidence dashboard for PCSEL design, reproduction, and academic radar</h1>
  <p class="portal-hero__lead">A public-facing snapshot of the research artifacts that matter for group meetings, proposal reviews, applications, and defense-style presentations: literature coverage, solver sweeps, reproduction status, solver-comparison evidence, RL/COMSOL optimization validation, and daily academic monitoring.</p>
  <div class="portal-hero__meta">
    <span>Updated {{ portal.snapshot.updated }}</span>
    <span>{{ portal.snapshot.scope }}</span>
  </div>
</section>

<section class="portal-kpi-grid" aria-label="Research portal key metrics">
  {% for item in portal.kpis %}
  <article class="portal-kpi-card">
    <span>{{ item.label }}</span>
    <strong>{{ item.value }}</strong>
    <p>{{ item.note }}</p>
  </article>
  {% endfor %}
</section>

<section class="portal-module" id="pcsel-library">
  <div class="portal-module__header">
    <span class="portal-module__eyebrow">PCSEL knowledge base</span>
    <h2>PCSEL literature library statistics</h2>
    <p>The private literature index is exposed here as aggregate evidence only: counts, year coverage, DOI coverage, source-group coverage, and refresh status. PDFs and private metadata stay outside the public site.</p>
  </div>
  <div class="portal-split">
    <figure class="research-figure">
      <img src="{{ portal.paper_library.year_chart | relative_url }}" alt="PCSEL literature library year distribution chart" loading="lazy">
      <figcaption>{{ portal.paper_library.records }} indexed records, {{ portal.paper_library.doi_count }} DOI-linked entries, year range {{ portal.paper_library.year_range }}. Snapshot: {{ portal.paper_library.exported_at }}.</figcaption>
    </figure>
    <div class="portal-fact-panel">
      <h3>Coverage signals</h3>
      <ul class="portal-list">
        <li>{{ portal.paper_library.recent_2020_plus }} records are from 2020 or later.</li>
        <li>PDF redistribution is {% if portal.paper_library.redistribution_allowed %}enabled{% else %}disabled{% endif %}; public pages show statistics, not PDFs.</li>
        <li>Top source groups:</li>
      </ul>
      <div class="portal-pill-row">
        {% for group in portal.paper_library.top_groups limit:6 %}
        <span>{{ group.label }} · {{ group.count }}</span>
        {% endfor %}
      </div>
    </div>
  </div>
</section>

<section class="portal-module" id="hx1-sweep">
  <div class="portal-module__header">
    <span class="portal-module__eyebrow">HX1-940 sweep</span>
    <h2>Hole-depth sweep figures and solver-derived metrics</h2>
    <p>HX1-940 is presented as a credibility and comparison panel: FDTD mesh3/mesh5 runs are checked against COMSOL target-window rows, with quantum-well clearance and detuning kept visible as risk gates.</p>
  </div>
  <div class="portal-metric-strip">
    <span>Depths: {{ portal.hx1.depths_nm | join: ", " }} nm</span>
    <span>FDTD rows: {{ portal.hx1.fdtd_rows }}</span>
    <span>COMSOL rows: {{ portal.hx1.comsol_rows }}</span>
    <span>FDTD Q range: {{ portal.hx1.fdtd_q_minmax }}</span>
    <span>FDTD detuning: {{ portal.hx1.fdtd_detuning_minmax_nm }} nm</span>
  </div>
  <div class="portal-media-grid">
    {% for figure in portal.hx1.figures %}
    <figure class="research-figure">
      <img src="{{ figure.src | relative_url }}" alt="{{ figure.alt }}" loading="lazy">
      <figcaption>{{ figure.caption }}</figcaption>
    </figure>
    {% endfor %}
  </div>
</section>

<section class="portal-module" id="comsol-fdtd">
  <div class="portal-module__header">
    <span class="portal-module__eyebrow">COMSOL / FDTD comparison</span>
    <h2>Comparison report status</h2>
    <p>The portal separates solver agreement from device claims. COMSOL rows currently provide the high-Q target-window reference; Lumerical FDTD provides a periodic-cell trend model whose wavelength detuning and Q spread still need interpretation before being used as a design conclusion.</p>
  </div>
  <div class="portal-card-grid">
    <article class="highlight-card">
      <h2>COMSOL reference</h2>
      <p>{{ portal.hx1.comsol_rows }} depth rows across 100-600 nm, with target-window Q range {{ portal.hx1.comsol_q_minmax }}.</p>
    </article>
    <article class="highlight-card">
      <h2>FDTD trend model</h2>
      <p>{{ portal.hx1.fdtd_rows }} mesh-comparison rows, mesh labels {{ portal.hx1.mesh_labels | join: " / " }}, generated {{ portal.hx1.created_at }}.</p>
    </article>
    <article class="highlight-card">
      <h2>Interpretation boundary</h2>
      <p>Use this panel to discuss solver-model differences, mode tracking, and process gates; do not present it as a final laser-performance claim.</p>
    </article>
  </div>
</section>

<section class="portal-module" id="rlcomsol">
  <div class="portal-module__header">
    <span class="portal-module__eyebrow">RLcomsol</span>
    <h2>COMSOL-backed optimization validation</h2>
    <p>RLcomsol is the bridge between the earlier RLcode optimization sandbox and solver-backed PCSEL evidence. It tests whether candidate-search policies can stay tied to COMSOL geometry audits, mode-selection policy, accepted-score guards, and reportable run provenance.</p>
  </div>
  <div class="portal-metric-strip">
    <span>Reports: {{ portal.rlcomsol.reports_count }}</span>
    <span>Scripts: {{ portal.rlcomsol.scripts_count }}</span>
    <span>Tests: {{ portal.rlcomsol.tests_count }}</span>
    <span>Completed runs: {{ portal.rlcomsol.completed_runs }}</span>
    <span>Verdict: {{ portal.rlcomsol.verdict }}</span>
    <span>Best accepted score: {{ portal.rlcomsol.best_score }}</span>
  </div>
  <div class="portal-card-grid">
    <article class="highlight-card">
      <h2>Best smoke-panel point</h2>
      <p>{{ portal.rlcomsol.best_seed }} step {{ portal.rlcomsol.best_step }} reached accepted score {{ portal.rlcomsol.best_score }} with Q {{ portal.rlcomsol.best_q }} under the fixed radius-guard protocol.</p>
    </article>
    <article class="highlight-card">
      <h2>Interpretation boundary</h2>
      <p>The three-seed 20-step panel is a repeatability and guard-provenance smoke check. It supports discussion of optimization stability, not a claim of global optimum discovery.</p>
    </article>
    <article class="highlight-card">
      <h2>Public boundary</h2>
      <p>{{ portal.rlcomsol.public_boundary }}</p>
    </article>
  </div>
  <div class="portal-media-grid">
    {% for figure in portal.rlcomsol.figures %}
    <figure class="research-figure">
      <img src="{{ figure.src | relative_url }}" alt="{{ figure.alt }}" loading="lazy">
      <figcaption>{{ figure.caption }}</figcaption>
    </figure>
    {% endfor %}
  </div>
</section>

<section class="portal-module" id="cwt-reproduction">
  <div class="portal-module__header">
    <span class="portal-module__eyebrow">CWT reproduction</span>
    <h2>Reproduction progress and provenance</h2>
    <p>The CWT work is shown as computed reproduction progress: report figures, per-result provenance, and scripts. This keeps the discussion anchored in real generated outputs rather than hand-drawn lookalikes.</p>
  </div>
  <div class="portal-metric-strip">
    <span>Provenance files: {{ portal.cwt.provenance_count }}</span>
    <span>Report figures: {{ portal.cwt.report_figures }}</span>
    <span>Scripts: {{ portal.cwt.scripts_count }}</span>
    <span>HTML report: {{ portal.cwt.report_exists }}</span>
  </div>
  <div class="portal-media-grid">
    {% for figure in portal.cwt.figures %}
    <figure class="research-figure">
      <img src="{{ figure.src | relative_url }}" alt="{{ figure.alt }}" loading="lazy">
      <figcaption>{{ figure.caption }}</figcaption>
    </figure>
    {% endfor %}
  </div>
  <div class="portal-pill-row">
    {% for item in portal.cwt.focus %}
    <span>{{ item }}</span>
    {% endfor %}
  </div>
</section>

<section class="portal-module" id="dailybrief-radar">
  <div class="portal-module__header">
    <span class="portal-module__eyebrow">DailyBrief academic radar</span>
    <h2>Daily academic monitoring snapshot</h2>
    <p>DailyBrief turns morning monitoring into a reviewable research signal. The public portal reports only the local output count, latest report date, link count, and academic keyword distribution.</p>
  </div>
  <div class="portal-split">
    <figure class="research-figure">
      <img src="{{ portal.dailybrief.radar_chart | relative_url }}" alt="DailyBrief academic radar keyword chart" loading="lazy">
      <figcaption>{{ portal.dailybrief.html_count }} local DailyBrief HTML reports from {{ portal.dailybrief.date_range }}; latest report {{ portal.dailybrief.latest }} with {{ portal.dailybrief.href_count }} links.</figcaption>
    </figure>
    <div class="portal-fact-panel">
      <h3>Latest academic topics</h3>
      <ul class="portal-list">
        {% if portal.dailybrief.latest_topics.size == 0 %}
        <li>No academic keyword topic was extracted from the latest local brief.</li>
        {% endif %}
        {% for topic in portal.dailybrief.latest_topics %}
        <li>{{ topic }}</li>
        {% endfor %}
      </ul>
    </div>
  </div>
</section>

<section class="portal-boundary">
  <h2>Public boundary and refresh path</h2>
  <p>{{ portal.snapshot.boundary }}</p>
  <p>Refresh command source: <code>{{ portal.snapshot.refresh_script }}</code>. The generated site keeps the research claims inspectable while preserving private raw artifacts.</p>
</section>
