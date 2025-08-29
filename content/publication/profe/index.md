---
title: "Data reduction method for OPTICAM multiband time series of transiting exoplanets"
authors:
- admin
- Y. Gómez Maqueo Chew
- L. H. Hebb
author_notes:
- "Equal contribution"
- "Equal contribution"
- "Equal contribution"
date: "2025-08-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2025-08-01T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*Montly Notices of Royal Astronomy Society*(Submitted)"
publication_short: "MNRAS(Submitted)"

abstract: We present a methodology for acquiring and reducing transiting exoplanet light curves obtained with San Pedro Mártir (SPM) 2.1m+OPTICAM, based on ~180h of observations acquired between 2023 and 2025. The OPTICAM sCMOS detectors generate significant hot pixels at exposures ≥ 10s, affecting both science and calibration frames. These hot pixels are not removed by standard dark subtraction because they vary unpredictably from frame to frame. We evaluate six pre-processing methods applied to science and calibration images using the transit of a TESS planet candidate observed in the g'r'i' filters. A median filter with a 3x3-pixel window minimizes the effect of hot pixels without affecting stellar signals. This proposed method best reduces dispersion and red noise in the light curves when stellar peak counts are close to the dark current level. The improvement is less significant when the stellar peak is several thousand counts above the dark current level. We fit a multiband transit model to the light curves, measuring photometric precision, correlated noise, and retrieved planetary parameters. Although we analyze the same dataset, we find that fitted parameters depend on the preprocessing method used. Posterior comparisons show that the median filter preprocessing best describes the data. We caution against combining light curves from different reductions, as it could introduce unquantifiable systematic errors; for example, the derived impact parameter varies by up to ~5.6σ. Finally, we introduce PROFE, a reduction pipeline that implements our proposed method, which incorporates AstroImageJ and Python scripts.

# Summary. An optional shortened abstract.
summary: We propose a preprocessing with a 3x3-pixel window median filter for the OPTICAM data of transiting exoplanet and introduce PROFE, a pipeline that implementa that preprocessing among other needed corrections and outputs.

tags:
- Article
- Transits

featured: false

# links:
# - name: ""
#   url: ""
url_pdf: 
url_code: 'https://github.com/s-paez/profe'
url_dataset: 'https://s-paez.github.io/opticam_lc/'
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Paez et al. (2025)'
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
