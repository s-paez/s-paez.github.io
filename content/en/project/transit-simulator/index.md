---
title: Exoplanet Transit Simulator
summary: A physically-inspired, interactive simulator that models stellar brightness drops as an exoplanet passes in front of its host star.
tags:
  - Outreach
  - Education
  - Interactive
date: '2025-10-12'

# Link to the simulator
links:
  - icon: external-link-alt
    name: View Simulator
    url: /simulators/transit/transit.html
  - icon: book-open
    name: Read Blog Post
    url: /blog/transitos/
---

The **Exoplanet Transit Simulator** is an interactive, web-based educational tool designed to model stellar brightness variations (light curves) when an exoplanet transits across the stellar disk from our perspective.

### 📐 Scientific Underpinnings

Unlike purely visual animations, this simulator is built on actual physical and astronomical equations that researchers use to model and fit real exoplanetary light curves:
* **3D Orbital Geometry**: Dynamically models the geometric projection of the planet's orbit using variables like inclination ($i$), semi-major axis ($a$), and the relative radii of the planet ($R_p$) and star ($R_\star$).
* **Quadratic Limb Darkening**: Incorporates the stellar coefficients $u_1$ and $u_2$ to simulate how the superficial brightness of a star fades from its center to its edges due to atmospheric depth and opacity.
* **Realistic Light Curves**: Generates real-time, high-fidelity light curves showing precisely modeled transit durations, entry/exit profiles, and depth signatures.

### 🏫 Educational Utility

This project serves as an active-learning tool for university astronomy courses and public science outreach. It allows users to experiment with core concepts by adjusting sliders:
1. Observing the scaling difference between a Earth-sized planet ($1 R_\oplus$) and a Jupiter-sized planet ($11 R_\oplus$) transit.
2. Exploring grazing transits (low inclination) that transform the classic "U-shaped" light curve into a distinct "V-shape".
3. Understanding how stellar atmospheric properties (limb darkening) affect the precise fitting and measurements of exoplanet sizes.
