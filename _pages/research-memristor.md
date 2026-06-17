---
layout: archive
title: "Memristor Reservoir Computing Research"
permalink: /research/memristor/
author_profile: true
---

<p class="research-intro">
  This direction connects dynamic SrTiO3-based memristor physics with reservoir computing, multimodal recognition, and spatio-temporal learning workflows.
</p>

<p class="research-backlink"><a href="{{ '/research/' | relative_url }}">Back to all research directions</a></p>

<section class="research-section" markdown="1">
## Device Dynamics and Computing Tasks

<div class="research-section__summary" markdown="1">
From 2022 to 2023, I worked on dynamic SrTiO3-based memristors for neuromorphic and reservoir-computing tasks (advisor: Prof. Limei Zheng, Shandong University). This work connected device-level nonlinear dynamics and short-term memory with algorithm-level behaviors in image, speech, multimodal recognition, and spatio-temporal learning pipelines.

Representative outcomes reported in the project include:

- **Linear and symmetric synaptic updates** in FTJ devices, supporting supervised recognition demonstrations.
- **Uniformity and temporal dynamics** in adaptive FTJ synapses, including cycle-to-cycle and device-to-device variation analysis reported in the paper.
- **Multimodal reservoir computing** with polarity-separated coding for image and speech inputs.
- **Spatio-temporal learning** via BCM-rule-based networks for orientation selectivity and motion-direction identification.

My contribution focused on text and speech data preprocessing, pulse-encoding pipelines, MATLAB-based RC/ANN implementation, debugging, robustness evaluation, and result visualization for reproducible analysis.
</div>
</section>

<section class="research-section" markdown="1">
## Training Value for Current PCSEL Work

<div class="workstream-panel" markdown="1">
This project trained a different but useful part of my current PCSEL workflow: separating device physics from task-level metrics. In the memristor work, I had to track how nonlinear device dynamics, pulse encoding, data preprocessing, MATLAB training code, and recognition metrics fit together. The same habit now helps me audit PCSEL optimization outputs, distinguish solver-derived physical metrics from proxy rewards, and document metric provenance before making device-design claims.
</div>
</section>

<section class="research-section" markdown="1">
## Task Pipelines

<div class="highlight-grid">
  <article class="highlight-card">
    <h2>Image recognition</h2>
    <p>Reservoir computing maps compact image matrices into pulse sequences and device-state responses, so only the readout layer needs to be trained for classification.</p>
  </article>
  <article class="highlight-card">
    <h2>Speech processing</h2>
    <p>Audio waveforms are trimmed, framed, filtered through auditory-inspired channels, masked, and converted into voltage sequences for dynamic device response.</p>
  </article>
  <article class="highlight-card">
    <h2>Multimodal recognition</h2>
    <p>Image and audio current sequences are combined to test how a dynamic physical reservoir can encode heterogeneous temporal information.</p>
  </article>
</div>
</section>

<section class="research-section" markdown="1">
## Representative Figures

<div class="research-media-grid">
  <figure class="research-figure">
    <img src="{{ '/images/research/memristor_synapse_device.png' | relative_url }}" alt="Memristor device sketch connecting physical synapse analogy to oxide device structure" loading="lazy" width="263" height="602">
    <figcaption>Physical-synapse analogy and oxide-device structure sketch.</figcaption>
  </figure>
  <figure class="research-figure">
    <img src="{{ '/images/research/memristor_reservoir_framework.png' | relative_url }}" alt="Reservoir-computing framework showing input pulses, dynamic internal state, and readout output" loading="lazy" width="406" height="343">
    <figcaption>Reservoir-computing framework: input, dynamic state, and readout.</figcaption>
  </figure>
  <figure class="research-figure">
    <img src="{{ '/images/research/memristor_audio_encoding.png' | relative_url }}" alt="Audio preprocessing and encoding workflow for memristor reservoir input sequences" loading="lazy" width="1053" height="375">
    <figcaption>Audio feature framing and encoding for memristor-driven processing.</figcaption>
  </figure>
</div>

Related papers: [**Materials Futures 2023**](https://doi.org/10.1088/2752-5724/ace3dc) and [**Advanced Materials 2025**](https://doi.org/10.1002/adma.202412006). Related publications are listed on the [Publications]({{ '/publications/' | relative_url }}) page.
</section>
