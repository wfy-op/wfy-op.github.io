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

Representative outcomes from this project include:

- **Linear and symmetric synaptic updates** in FTJ devices, supporting high MNIST recognition accuracy in supervised learning.
- **Strong uniformity and temporal dynamics** in adaptive FTJ synapses, including cycle-to-cycle and device-to-device variation analysis.
- **Multimodal reservoir computing** with polarity-separated coding for image and speech inputs.
- **Spatio-temporal learning** via BCM-rule-based networks for orientation selectivity and motion-direction identification.

My contribution focused on text and speech data preprocessing, pulse-encoding pipelines, MATLAB-based RC/ANN implementation, debugging, robustness evaluation, and result visualization for reproducible analysis.
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
    <img src="{{ '/images/research/memristor_synapse_device.png' | relative_url }}" alt="Memristor synapse schematic" loading="lazy">
    <figcaption>Physical-synapse analogy and device structure sketch.</figcaption>
  </figure>
  <figure class="research-figure">
    <img src="{{ '/images/research/memristor_reservoir_framework.png' | relative_url }}" alt="Reservoir framework" loading="lazy">
    <figcaption>Reservoir-computing framework: input, dynamic state, and readout.</figcaption>
  </figure>
  <figure class="research-figure">
    <img src="{{ '/images/research/memristor_audio_encoding.png' | relative_url }}" alt="Audio encoding for reservoir input" loading="lazy">
    <figcaption>Audio feature framing and encoding for memristor-driven processing.</figcaption>
  </figure>
</div>

Related papers: [**Materials Futures 2023**](https://doi.org/10.1088/2752-5724/ace3dc) and [**Advanced Materials 2025**](https://doi.org/10.1002/adma.202412006). Related publications are listed on the [Publications]({{ '/publications/' | relative_url }}) page.
</section>
