---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<p class="research-intro">
  This page collects peer-reviewed papers and selected research outputs. For multi-author papers, I include a short contribution note so the publication list is useful as evidence rather than only a citation record.
</p>

<section class="research-section" markdown="1">
## Journal Articles

<div class="publication-card-grid">
  <article class="publication-card">
    <span class="publication-card__venue">Materials Futures · 2023</span>
    <h3>Ultrathin SrTiO3-based oxide memristor with both drift and diffusive dynamics as versatile synaptic emulators for neuromorphic computing</h3>
    <p class="publication-card__authors">F. Nie, J. Wang, H. Fang, S. Ma, <strong>F. Wu</strong>, et al.</p>
    <p><strong>Citation:</strong> Materials Futures 2023, 2(3), 035302.</p>
    <p><strong>Contribution note:</strong> Contributed to data processing, MATLAB readout-training support, debugging, and result visualization for memristor-based learning tasks. This work shaped my later PCSEL practice of separating physical device response from downstream performance metrics.</p>
    <p><a class="btn" href="https://doi.org/10.1088/2752-5724/ace3dc">DOI</a></p>
  </article>

  <article class="publication-card">
    <span class="publication-card__venue">Advanced Materials · 2025</span>
    <h3>An Adaptive Solid-state Synapse with Bi-directional Relaxation for Multimodal Recognition and Spatio-temporal Learning</h3>
    <p class="publication-card__authors">F. Nie, S. Yang, L. Zhao, C. Jia, S. Ma, <strong>F. Wu</strong>, et al.</p>
    <p><strong>Citation:</strong> Advanced Materials 2025, 37(17), 2412006.</p>
    <p><strong>Contribution note:</strong> Contributed to text/speech data preprocessing, MATLAB-based training workflow, code debugging, and result visualization for multimodal reservoir-computing tasks. This work shaped my later PCSEL practice of separating physical device response from downstream performance metrics.</p>
    <p><a class="btn" href="https://doi.org/10.1002/adma.202412006">DOI</a></p>
  </article>
</div>
</section>

<section class="research-section" markdown="1">
## Technical Outputs

<div class="publication-card-grid">
  <article class="publication-card">
    <span class="publication-card__venue">Technical note · ongoing</span>
    <h3>PCSELBook: PCSEL Theory, Simulation, and Device Physics</h3>
    <p>A ~300,000-character technical note on PCSEL electromagnetic theory, numerical methods, epitaxy, quantum-well gain, and electro-thermal-optical device modeling.</p>
    <p><a class="btn" href="https://github.com/wfy-op/PCSELbook">GitHub</a> <a class="btn" href="{{ '/posts/2026/04/pcselbook/' | relative_url }}">Project note</a></p>
  </article>
</div>
</section>

<section class="research-section" markdown="1">
## Software and Research Artifacts

<p>
  Public-ready artifacts are listed on the <a href="{{ '/projects/' | relative_url }}">Projects</a> page. Private solver runs, RLcode outputs, and PCSEL paper-library entries are not presented as public evidence until they are cleaned and documented.
</p>
</section>
