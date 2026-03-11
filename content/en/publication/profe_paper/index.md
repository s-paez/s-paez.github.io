---
title: "Data reduction method for OPTICAM multiband time series of transiting exoplanets"
authors:
- spaez
- Y. Gómez Maqueo Chew
- L. Hebb

author_notes:
- "Equal contribution"
- "Equal contribution"
- "Equal contribution"
date: "2026-03-07T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2026-03-10T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "Accepted for publication in *RAS Techniques and Instruments* on Mar. 2026"
publication_short: "Accepted for publication in RASTI"

abstract: We present a methodology for acquiring and reducing transiting exoplanet light curves obtained with the OPTICAM instrument in the Observatorio Astronómico Nacional en la Sierra de San Pedro Mártir (OAN-SPM). The OPTICAM sCMOS detectors generate significant warm pixels at exposures ≥10s, affecting both science and calibration frames. These warm pixels are not removed by standard dark subtraction because they vary unpredictably from frame to frame. We evaluate six pre-processing methods applied to science and calibration images using the transit of TOI-7149 b observed in g' r' i'. A median filter with a 3x3-pixel window minimizes the effect of warm pixels without affecting stellar signals. This median filter best reduces dispersion and red noise in the light curves when stellar peak counts are close to the dark current level. The improvement is less significant when the stellar peak is several thousand counts above the dark current level. We fit a multiband transit model to the light curves, measuring photometric precision, correlated noise, and retrieved planetary parameters. The transit model fitted to the light curves with pre-processing using a 3x3-median filter achieves the highest Bayesian evidence. Thus, it is our recommended method for correcting warm pixels. Finally, we present a reduction pipeline that combines Python modules (PROFE) and AstroImageJ to implement our proposed method for OAN-SPM 2.1m+OPTICAM transiting planet observations.

# Summary. An optional shortened abstract.
summary: We propose a preprocessing with a 3x3-pixel window median filter for the OPTICAM data of transiting exoplanet and introduce PROFE, a pipeline that implementa that preprocessing among other needed corrections and outputs.

tags:
- Article

featured: false

links:
- name: "Interactive light curves"
  url: 'https://s-paez.github.io/opticam_lc/'
url_pdf: 'https://arxiv.org/pdf/2603.09922'
url_code: 'https://github.com/s-paez/profe'
url_dataset: 
url_poster: 
url_project: 
url_slides: 
url_source: 
url_video: 

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Image subframes and distributions of counts for different median filters preprocessing including 3x3-pixel window.'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---
