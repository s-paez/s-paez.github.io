---
title: PROFE
summary: Pipeline de Reducción de OPTICAM para Fotometría de Exoplanetas. Un paquete de Python de código abierto para el preprocesamiento, calibración y fotometría diferencial de tránsitos.
tags:
  - Software
  - Exoplanetas
  - Python
date: '2026-03-11'

# Enlaces externos del proyecto
links:
  - icon: brands/github
    icon_pack: fab
    name: Código en GitHub
    url: https://github.com/s-paez/profe
  - icon: file-pdf
    name: Artículo Científico
    url: https://academic.oup.com/rasti/article/doi/10.1093/rasti/rzag021/8516487
  - icon: external-link-alt
    name: Curvas de luz interactivas
    url: https://s-paez.github.io/opticam_lc/
---

**PROFE** es una biblioteca de Python para preparar y reducir imágenes del instrumento OPTICAM, instalado en el telescopio de 2.1 m del OAN-SPM. La desarrollé durante mi maestría para trabajar con series de tiempo de exoplanetas en tránsito.

Sus herramientas permiten aplicar un filtro por la mediana de 3×3 píxeles, organizar archivos de calibración y científicos, y calcular marcas de tiempo y masas de aire. El flujo de trabajo combina PROFE con AstroImageJ para obtener y analizar curvas de luz multibanda.

Los enlaces de esta página llevan al código, al artículo que describe el método y a las curvas de luz interactivas. La explicación del preprocesamiento está en el [blog](/es/blog/opticam_dr/).
