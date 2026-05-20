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

**PROFE** (**P**ipeline de **R**educción de **O**pticam para **F**otometría de **E**xoplanetas) is a Python package designed to streamline, automate, and standardize the reduction and analysis of high-cadence time-series data obtained with the triple-band **OPTICAM** instrument. OPTICAM is mounted on the 2.1m Telescope at the Observatorio Astronómico Nacional in the Sierra de San Pedro Mártir (OAN-SPM), Mexico.

### 🛠️ Key Features

* **Smart 3x3 Median Filtering**: Corrects unpredictable warm pixels generated during long exposures (≥10s) by the instrument's sCMOS detectors, significantly minimizing red noise and dispersion in the final light curves.
* **Parallel Processing**: Speeds up reduction times by distributing the median filtering of massive images (4+ megapixels each) across multiple CPU cores via the Python `multiprocessing` library.
* **Automatic Data Management**: Automatically structures and groups calibration frames (darks, flats) and scientific images by date, target star, and filters.
* **Airmass and Time Corrections**: Standardizes time stamps to BJD (Barycentric Julian Date) and calculates airmass coordinates for every data point.
* **Scientific Diagnostics & Products**: After executing aperture photometry in complementary software (e.g., AstroImageJ), PROFE processes raw measurements to generate multiband light curves, airmass trends, and target sky-tracking plots. These are ready for sharing with international consortia such as the **TESS Follow-up Observing Program**.

### 📖 Associated Publication

This pipeline is the core contribution of my Master's thesis research, published in the international scientific journal **RAS Techniques and Instruments (RASTI)** in March 2026:
> *Páez et al. (2026). Data reduction method for OPTICAM multiband time series of transiting exoplanets. RAS Techniques and Instruments, Volume 5.*
