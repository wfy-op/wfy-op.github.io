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
From 2022 to 2023, I worked on dynamic SrTiO3-based memristors for neuromorphic and reservoir-computing tasks (advisor: Prof. Limei Zheng, Shandong University). This work connected device-level physics, including ferroelectric switching and ionic dynamics, with algorithm-level behaviors in supervised, unsupervised, and multimodal recognition pipelines.

Representative outcomes from this project include:

- **Linear and symmetric synaptic updates** in FTJ devices, supporting high MNIST recognition accuracy in supervised learning.
- **Strong uniformity and temporal dynamics** in adaptive FTJ synapses, including cycle-to-cycle and device-to-device variation analysis.
- **Multimodal reservoir computing** with polarity-separated coding for image and speech inputs.
- **Spatio-temporal learning** via BCM-rule-based networks for orientation selectivity and motion-direction identification.

My contribution focused on data preprocessing and pulse-encoding pipelines, MATLAB-based RC/ANN implementation, debugging, robustness evaluation, and result visualization for reproducible analysis.
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

Related papers: [**Adv. Funct. Mater. 2022**](https://doi.org/10.1002/adfm.202202366) and [**Adv. Mater. 2025**](https://doi.org/10.1002/adma.202412006). Related publications are listed on the [Publications]({{ '/publications/' | relative_url }}) page.
</section>
