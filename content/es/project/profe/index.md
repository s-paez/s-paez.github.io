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
    url: https://arxiv.org/pdf/2603.09922
  - icon: external-link-alt
    name: Curvas de luz interactivas
    url: https://s-paez.github.io/opticam_lc/
---

**PROFE** (**P**ipeline de **R**educción de **O**pticam para **F**otometría de **E**xoplanetas) es una biblioteca de Python diseñada para optimizar, automatizar y estandarizar el proceso de reducción y análisis de datos temporales obtenidos con el instrumento multibanda **OPTICAM**, instalado en el telescopio de 2.1 m del Observatorio Astronómico Nacional en la Sierra de San Pedro Mártir (OAN-SPM).

### 🛠️ Características Principales

* **Filtro Mediano 3x3 Inteligente**: Implementa la corrección de píxeles tibios impredecibles generados en exposiciones largas (≥10s) por los detectores sCMOS del instrumento, mitigando el ruido rojo y la dispersión en las curvas de luz finales.
* **Procesamiento Paralelo**: Optimiza los tiempos de reducción distribuyendo el filtrado de imágenes (de más de 4 millones de píxeles cada una) a través de múltiples núcleos de CPU mediante el módulo `multiprocessing`.
* **Administración Automatizada de Datos**: Organiza los archivos FITS de calibración (darks, flats) y científicos por fecha, estrella y filtros de manera automática.
* **Correciones Temporales y de Masa de Aire**: Añade marcas de tiempo estandarizadas BJD y calcula automáticamente las masas de aire de cada observación.
* **Productos Científicos e Interactivos**: Tras realizar la fotometría en software complementario (como AstroImageJ), PROFE procesa los reportes fotométricos para generar gráficas de curvas de luz multibanda, masas de aire y trayectorias del objeto, listas para compartir con consorcios de seguimiento como el **TESS Follow-up Observing Program**.

### 📖 Publicación Asociada

Este software constituye el núcleo metodológico de mi trabajo de maestría, publicado en la revista científica internacional **RAS Techniques and Instruments (RASTI)** en marzo de 2026:
> *Páez et al. (2026). Data reduction method for OPTICAM multiband time series of transiting exoplanets. RAS Techniques and Instruments, Volume 5.*
