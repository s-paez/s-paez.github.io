---
title: Exoplanetas en tránsito
summary: Qué son y qué podemos aprender a través de los tránsitos de exoplanetas.
date: 2025-10-12
authors:
  - admin
tags:
  - Exoplanetas
  - Simulador
  - Tránsitos
image:
  filename: "simulator.png"
  caption:
  focal_point: "Center"
  preview_only: True
---
> En esta entrada cuento sobre el método del tránsito, por qué las curvas de luz son tan valiosas y dejo un recurso interactivo para experimentar con distintos escenarios planetarios.

<iframe src="/simuladores/transito/transito0.html"
        title="Animación de un planeta transitante"
        loading="lazy"
        style="width:150%;height:1200px;border:0;border-radius:16px;margin:0 auto;display:block;">
</iframe>

# ¿Qué es un planeta en tránsito?

Un planeta está en tránsito cuando su órbita lo lleva a pasar por delante de su estrella desde nuestro punto de vista. Durante ese cruce bloquea una fracción diminuta de la luz estelar, lo que produce un descenso breve y periódico en el brillo observado. La forma y la repetición de ese cambio son la firma que nos permite inferir la presencia del planeta.

# ¿Qué es una curva de luz?

La curva de luz es el registro del brillo de una estrella a lo largo del tiempo. Si graficamos esas mediciones consecutivas, los tránsitos aparecen como disminuciones en forma de “U”. También puede verse una caída mucho más tenue cuando el planeta pasa detrás de la estrella: es el eclipse secundario, que revela la pequeña contribución del planeta que refleja la luz de su estrella.

# ¿Cómo detectamos estos planetas?

El método del tránsito requiere observaciones continuas y precisas. Desde la Tierra dependemos de la noche, del clima y de la visibilidad del objeto, por lo que los registros suelen estar fragmentados. Las misiones espaciales como [TESS](https://www.nasa.gov/tess/) y [Kepler](https://www.nasa.gov/mission_pages/kepler/overview/index.html) superaron esas limitaciones al monitorear miles de estrellas desde el espacio sin interrupciones, lo que permitió detectar descensos de brillo de apenas unas décimas de un 1% y datos temporales continuos.

# ¿Qué podemos aprender de un tránsito?

El análisis detallado de la curva de luz ofrece múltiples pistas sobre el sistema estrella-planeta:

- **Periodo orbital**: la distancia temporal entre tránsitos consecutivos indica cuánto tarda el planeta en completar una órbita.
- **Tamaño relativo**: la profundidad del tránsito depende de la proporción entre el radio del planeta y el de la estrella.
- **Distancia orbital**: combinando el periodo con las leyes de Kepler estimamos cuán lejos se encuentra el planeta de su estrella.
- **Temperatura estimada**: con la distancia y el brillo estelar podemos calcular la energía que recibe el planeta.
- **Geometría de la órbita**: la forma del tránsito varía si el planeta cruza el centro del disco estelar o sólo roza el borde.
- **Propiedades de la estrella**: las estrellas no brillan uniformemente; el oscurecimiento del borde (limb darkening) deja huellas en los perfiles de entrada y salida del tránsito.

# Preguntas guía para el simulador

El simulador interactivo permite reproducir estos efectos y explorar distintos parámetros. Algunas propuestas de análisis:

1. Fija el radio estelar en 2 radios solares y compara la profundidad del tránsito para un planeta de 1 radio terrestre y otro de 11 radios terrestres. ¿Cómo cambia la curva y por qué?
2. Mantén un planeta de 6 radios terrestres orbitando una estrella de 0.7 radios solares y modifica la inclinación. Observa cómo se alteran la duración y la forma del tránsito cuando parte del planeta deja de proyectarse sobre la estrella.
3. Ajusta la inclinación a 90° y experimenta con los parámetros de oscurecimiento de borde ($u_1$ y $u_2$). ¿Qué ocurre con la visibilidad de los bordes del tránsito y qué dice eso sobre la atmósfera de la estrella?
4. Cambia el tamaño de la estrella y presta atención al cambio de color en la visualización. Investiga cómo se relacionan temperatura y tonalidad estelar.

# Simulador de exoplanetas transitantes
Convenciones:
* $R_\star$: Radio de la estrella
* $R_p$: Radio del planeta
* $R_\oplus$: Radios de la Tierra
* $R_\odot$: Radios del Sol

<iframe src="/simuladores/transito/transito.html"
        title="Simulador de tránsito planetario"
        loading="lazy"
        style="width:150%; height:1100px;border:0;border-radius:16px;margin:0 auto;display:block;">
</iframe>

El método del tránsito ha permitido confirmar miles de exoplanetas y seguirá siendo clave para identificar mundos potencialmente habitables. Te invito a experimentar con los simuladores, formular hipótesis y buscar resultados con observaciones reales.
