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

<section class="research-section" markdown="1">
## PCSEL Preprints

<div class="publication-card-grid">
  <article class="publication-card publication-card--preprint">
    <span class="publication-card__venue">arXiv:2607.23469 · July 2026</span>
    <h3>When Every Simulation Counts: Value-Based Reinforcement Learning for Accelerated Photonics Inverse Design</h3>
    <p class="publication-card__authors">Longying Wen*, <strong>Feiyang Wu*</strong>, Jinglin Yu*, Chongxian Yuan, Renjie Li, and Zhaoyu Zhang</p>
    <p><strong>Authorship:</strong> Co-first author; Longying Wen, Feiyang Wu, and Jinglin Yu contributed equally.</p>
    <p class="publication-card__summary">A matched study of seven value-based RL configurations for PCSEL inverse design under the same 83-call FDTD budget.</p>
    <figure class="publication-card__figure">
      <img src="{{ '/images/research/preprints/value_rl_matched_comparison.png' | relative_url }}" alt="Matched comparison table for seven value-based reinforcement-learning configurations under an 83-call FDTD budget" loading="lazy" width="1545" height="570">
      <figcaption>Matched multi-metric comparison from Table 1. Dueling DQN leads the endpoint, efficiency, cross-seed robustness, and mean-Q columns under the shared budget.</figcaption>
    </figure>
    <details class="publication-detail">
      <summary>Result and evidence boundary</summary>
      <p><strong>Result:</strong> Dueling DQN was the only tested variant to improve all four seeds. Relative to the first evaluated designs, its selected structures increased mean Q from 2.18 × 10<sup>5</sup> to 5.63 × 10<sup>6</sup>, reduced wavelength error by 64%, and increased upward power by 47%.</p>
      <p><strong>Evidence boundary:</strong> arXiv v1 preprint based on numerical FDTD experiments; the optimized PCSELs have not yet been fabricated or optically characterized.</p>
    </details>
    <p><a class="btn" href="https://arxiv.org/abs/2607.23469">arXiv</a> <a class="btn" href="https://arxiv.org/pdf/2607.23469">PDF</a> <a class="btn" href="https://github.com/Longying-Wen/PCSEL-RL">Code</a></p>
  </article>

  <article class="publication-card publication-card--preprint">
    <span class="publication-card__venue">arXiv:2607.21772 · July 2026</span>
    <h3>Reliability-Aware Bayesian Optimization of 1310 nm PCSELs with FDTD Verification</h3>
    <p class="publication-card__authors">Jinglin Yu*, <strong>Feiyang Wu*</strong>, Longying Wen*, Chongxian Yuan, Renjie Li, and Zhaoyu Zhang</p>
    <p><strong>Authorship:</strong> Co-first author; Jinglin Yu, Feiyang Wu, and Longying Wen contributed equally.</p>
    <p class="publication-card__summary">Reliability-aware Bayesian optimization using wavelength, beam quality, and Q-fit reliability to rank FDTD candidates.</p>
    <figure class="publication-card__figure">
      <img src="{{ '/images/research/preprints/bo_reliability_workflow.png' | relative_url }}" alt="Reliability-aware PCSEL candidate-selection workflow linking scripted offsets to resonance, Q-fit reliability, and far-field divergence" loading="lazy" width="1611" height="420">
      <figcaption>Physical map from Fig. 2. Candidate selection couples resonance placement, Q-fit reliability, and far-field width instead of maximizing raw Q alone.</figcaption>
    </figure>
    <details class="publication-detail">
      <summary>Result and evidence boundary</summary>
      <p><strong>Result:</strong> Three 80-evaluation runs each produced 5-15 joint-filter candidates. Fresh-model reconstructions retained Q<sub>eff</sub> = 4.33 × 10<sup>6</sup> to 7.76 × 10<sup>6</sup> at 1308.23-1310.90 nm with approximately 0.84° divergence.</p>
      <p><strong>Evidence boundary:</strong> arXiv v1 preprint reporting reconstructed full-wave simulations; the results are a verified numerical candidate pool, not measured laser performance.</p>
    </details>
    <p><a class="btn" href="https://arxiv.org/abs/2607.21772">arXiv</a> <a class="btn" href="https://arxiv.org/pdf/2607.21772">PDF</a></p>
  </article>
</div>
</section>

<section class="research-section" markdown="1">
## Journal Articles

<div class="publication-card-grid">
  <article class="publication-card">
    <span class="publication-card__venue">Materials Futures · 2023</span>
    <h3>Ultrathin SrTiO3-based oxide memristor with both drift and diffusive dynamics as versatile synaptic emulators for neuromorphic computing</h3>
    <p class="publication-card__authors">F. Nie, J. Wang, H. Fang, S. Ma, <strong>F. Wu</strong>, et al.</p>
    <p><strong>Citation:</strong> Materials Futures 2023, 2(3), 035302.</p>
    <p><strong>Contribution:</strong> Data processing, MATLAB readout-training support, debugging, and result visualization for memristor-based learning tasks.</p>
    <p><a class="btn" href="https://doi.org/10.1088/2752-5724/ace3dc">DOI</a></p>
  </article>

  <article class="publication-card">
    <span class="publication-card__venue">Advanced Materials · 2025</span>
    <h3>An Adaptive Solid-State Synapse with Bi-Directional Relaxation for Multimodal Recognition and Spatio-Temporal Learning</h3>
    <p class="publication-card__authors">F. Nie, H. Fang, J. Wang, L. Zhao, C. Jia, S. Ma, <strong>F. Wu</strong>, et al.</p>
    <p><strong>Citation:</strong> Advanced Materials 2025, 37(17), 2412006.</p>
    <p><strong>Contribution:</strong> Text/speech preprocessing, MATLAB training workflow, code debugging, and result visualization for multimodal reservoir-computing tasks.</p>
    <p><a class="btn" href="https://doi.org/10.1002/adma.202412006">DOI</a></p>
  </article>
</div>
</section>

<section class="research-section" markdown="1">
## Patent Applications

<div class="publication-card-grid">
  <article class="publication-card">
    <span class="publication-card__venue">CNIPA application accepted · 2026</span>
    <h3>Semiconductor Laser Automated Design Optimization Method and Storage Medium</h3>
    <p>半导体激光器自动化设计优化方法及存储介质</p>
    <p><strong>Application:</strong> CN 202610820592.4 · 2026-06-08 · The Chinese University of Hong Kong, Shenzhen</p>
    <p><strong>Inventors:</strong> Zhaoyu Zhang, Feiyang Wu, Sixuan Mao, and Kebo He. Accepted application; not a granted patent.</p>
  </article>
</div>
</section>

<section class="research-section" markdown="1">
## Technical Outputs

<div class="publication-card-grid">
  <article class="publication-card">
    <span class="publication-card__venue">Technical note · ongoing</span>
    <h3>PCSELBook: PCSEL Theory, Simulation, and Device Physics</h3>
    <p>A living technical monograph connecting PCSEL electromagnetic theory, numerical methods, epitaxy, quantum-well gain, coupled device physics, and practical validation cases.</p>
    <p><a class="btn" href="https://github.com/wfy-op/PCSELbook">GitHub</a> <a class="btn" href="{{ '/posts/2026/04/pcselbook/' | relative_url }}">Project note</a></p>
  </article>
</div>
  <p class="publication-support-link"><a href="{{ '/projects/' | relative_url }}">Browse research software and public artifacts</a></p>
</section>
