---
title: PROFE
summary: OPTICAM Reduction Pipeline for Exoplanet Photometry. An open-source Python package for preprocessing, calibrating, and performing differential photometry on transiting exoplanets.
tags:
  - Software
  - Exoplanets
  - Python
date: '2026-03-11'

# External links for the project
links:
  - icon: brands/github
    icon_pack: fab
    name: GitHub Code
    url: https://github.com/s-paez/profe
  - icon: file-pdf
    name: Research Paper
    url: https://academic.oup.com/rasti/article/doi/10.1093/rasti/rzag021/8516487
  - icon: external-link-alt
    name: Interactive Light Curves
    url: https://s-paez.github.io/opticam_lc/
---

**PROFE** is a Python library for preparing and reducing images from OPTICAM, installed on the OAN-SPM 2.1 m telescope. I developed it during my master's degree to work with photometric time series of transiting exoplanets.

Its tools apply a 3×3 median filter, organize calibration and science files, and calculate timestamps and airmass. The workflow combines PROFE with AstroImageJ to obtain and analyze multiband light curves.

The links on this page lead to the code, the paper describing the method, and the interactive light curves. The preprocessing method is explained in the [blog](/blog/opticam_dr/).
