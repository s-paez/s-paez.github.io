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
date: "2025-09-10T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2025-09-10T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "Aceptado para publicación en *RAS Techniques and Instruments* en Marzo de 2026"
publication_short: "Aceptado en RASTI en Marzo 2026"

abstract: Presentamos una metodología para adquirir y reducir las curvas de luz de exoplanetas en tránsito obtenidas con el instrumento OPTICAM en el Observatorio Astronómico Nacional en la Sierra de San Pedro Mártir (OAN-SPM). Los detectores sCMOS de OPTICAM generan píxeles cálidos significativos en exposiciones ≥10 s, lo que afecta tanto a los fotogramas científicos como a los de calibración. Estos píxeles cálidos no se eliminan mediante la sustracción oscura estándar, ya que varían de forma impredecible de un fotograma a otro. Evaluamos seis métodos de preprocesamiento aplicados a imágenes científicas y de calibración utilizando el tránsito de TOI-7149 b observado en g' r' i'. Un filtro mediano con una ventana de 3x3 píxeles minimiza el efecto de los píxeles cálidos sin afectar a las señales estelares. Este filtro mediano reduce mejor la dispersión y el ruido rojo en las curvas de luz cuando los recuentos máximos estelares se acercan al nivel de corriente oscura. La mejora es menos significativa cuando el pico estelar está varios miles de recuentos por encima del nivel de corriente oscura. Ajustamos un modelo de tránsito multibanda a las curvas de luz, midiendo la precisión fotométrica, el ruido correlacionado y los parámetros planetarios recuperados. El modelo de tránsito ajustado a las curvas de luz con preprocesamiento utilizando un filtro mediano 3x3 alcanza la mayor evidencia Bayesiana. Por lo tanto, es nuestro método recomendado para corregir los píxeles cálidos. Por último, presentamos un proceso de reducción que combina módulos Python (PROFE) y AstroImageJ para implementar nuestro método propuesto para las observaciones de planetas en tránsito con OAN-SPM 2,1 m + OPTICAM.

# Summary. An optional shortened abstract.
summary: Proponemos un procesamiento con un filtro por la mediana con una ventana de 3x3 pixeles antes de la reducción estándar para los datos de OPTICAM para fotometría de exoplanetas en tránsito. Presentamos PROFE, una código en Python que implementa ese preprocesamiento entre otras corecciones necesarias a los archivos FITS de OPTICAM.

tags:
- Artículo

featured: false

links:
- name: "Curvas de luz interactivas"
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
  caption: 'Recortes de imagen para diferentes preprocesamientos antes y después de la calibración'
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
