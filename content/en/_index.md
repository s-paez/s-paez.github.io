---
# Leave the homepage title empty to use the site title
title: ""
date: 2025-08-29
type: landing

design:
  # Default section spacing
  spacing: "6rem"

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
      text: ""
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download my CV
        url: uploads/resume_en.pdf
      #   text: Descargar CV-ES
      #   url: uploads/resume_es.pdf  
    design:
      css_class: dark
      background:
        color: black
        image:
          # Add your image background to `assets/media/`.
          filename: stacked-peaks.webp
          filters:
            brightness: 1.0
          size: cover
          position: center
          parallax: false
  # - block: cta-button-list
  #   content:
  #     buttons:
  #       - text: "Download my CV in English "
  #         url: "uploads/resume_en.pdf"
  #         icon:
  #       - text: "Descarga mi CV en Español"
  #         url: "uploads/resume_es.pdf"
  #         icon: 
  - block: markdown
    content:
      title: 'My work'
      subtitle: ''
      text: |-
        My work focuses on ground-based transit multiband photometry. For my Master's degree, I worked on data acquired with [OPTICAM](https://www.astrossp.unam.mx/es/usuarios/instrumentos/imagendirecta/opticam), a triple-band imaging system designed for use with the [2.1m Telescope](https://www.astrossp.unam.mx/es/usuarios/telescopios/tel2m) at the Observatorio Astronómico Nacional en la Sierra de San Pedro Mártir (OAN-SPM). My research involved developing a data reduction method to enable follow-up observations of planet candidates and multiband studies of transiting exoplanet systems.
        
    design:
      columns: '1'
  - block: collection
    id: papers
    content:
      title: Featured Publications
      filters:
        folders:
          - publication
        featured_only: true
    design:
      view: article-grid
      columns: 2
  # - block: collection
  #   content:
  #     title: Recent Publications
  #     text: ""
  #     filters:
  #       folders:
  #         - publication
  #       exclude_featured: false
  #   design:
  #     view: citation
  # - block: collection
  #   id: talks
  #   content:
  #     title: Recent & Upcoming Talks
  #     filters:
  #       folders:
  #         - event
  #   design:
  #     view: article-grid
  #     columns: 1
  # - block: collection
  #   id: news
  #   content:
  #     title: Recent News
  #     subtitle: ''
  #     text: ''
  #     # Page type to display. E.g. post, talk, publication...
  #     page_type: post
  #     # Choose how many pages you would like to display (0 = all pages)
  #     count: 5
  #     # Filter on criteria
  #     filters:
  #       author: ""
  #       category: ""
  #       tag: ""
  #       exclude_featured: false
  #       exclude_future: false
  #       exclude_past: false
  #       publication_type: ""
  #     # Choose how many pages you would like to offset by
  #     offset: 0
  #     # Page order: descending (desc) or ascending (asc) date.
  #     order: desc
  #   design:
  #     # Choose a layout view
  #     view: date-title-summary
  #     # Reduce spacing
  #     spacing:
  #       padding: [0, 0, 0, 0]
---
