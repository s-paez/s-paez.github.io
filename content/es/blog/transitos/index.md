---
title: Exoplanetas en tránsito
summary: Qué son y qué podemos aprender a través de los tránsito de exoplanetas.
date: 2025-10-12
authors:
  - admin
tags:
  - Exoplanetas
  - Simulador
  - Transitos
image:
  filename: "simulator.png"
  caption: 
  focal_point: "Center"
  preview_only: True
---
> En esta entrada hablo sobre mi tema principal de estudio, los exoplanetas en tránsito. Explico en términos generales qué son los tránsitos y qué aprendemos a partir de analizar las curvas de luz de estrellas que albergan estos planetas .

<iframe src="/simuladores/transito/transito0.html"
        title="Animación de un planeta transitante"
        loading="lazy"
        style="width:150%;height:1200px;border:0;border-radius:16px;">
</iframe>

# ¿Qué es un planeta transitante?

Un planeta en tránsito es un planeta que en un punto de su orbita pasa enfrente de su estrella anfitriona y oculta temporalmente una parte de su brillo. Al medir constantemente el nivel de brillo de la estrella podemos detectar cuando el planeta pasa enfrente y así aprender de propiedades cómo su periodo orbital, su tamaño y la inclinación de su orbita. Esto se hace mediante el análisis de la curva de luz de la estrella.

# ¿Qué es una curva de luz?

Una curva de luz es el registro del brillo de una estrella a largo del tiempo. Se realizan mediciones secuenciales para medir como varía el brillo de la estrella a medida que pasa el tiempo. La animación del principio muestra una curva de luz simplificada de un planeta que pasa enfrente de su estrella. Podemos ver que cuando el planeta pasa enfrente, los puntos verdes que son las mediciones del brillo de la estrella, disminuyen y cuando el planeta ya no está frente observamos el brillo normal de la estrella, esto es lo que se conoce con un tránsito. En la animación también podemos ver que cuando el planeta pasa detrás de su estrella, también hay un caída de brillo pero mucho más pequeña, esto se conoce como el eclipse secundario y se da porque el planeta también aporta al brillo total del sistema estrella-planeta, por lo que cuando la estrella oculta al planeta, el brillo que medimos también disminuye un poco. 

# ¿Cómo se detectan los planetas transitantes?
Para detectar planetas transitantes, se necesita observar continuamente una estrella (o conjunto de estrellas al mismo tiempo) durante largos periodos de tiempo. Para observaciones desde la Tierra se puede observar como máximo lo que dura una noche, pero para observaciones con telescopios espaciales como TESS (Satélite de sondeo de planetas transitante, por sus siglas en inglés) o Kepler, las observaciones pueden ser de días, meses o incluso años, porque no son afectadas por el día y la noche. 

# ¿Qué información podemos obtener a partir de los tránsitos de exoplanetas?

A partir de analizar las curvas de luz de los planetas transitantes, podemos obtener información muy importante sobre el sistema planetario que estamos estudiando. Por ejemplo:

* Periodo orbital: Midiendo cada cuanto ocurre un tránsito, podemos saber cuanto tiempo le toma al planeta dar una vuelta alrededor de su estrella, esto se conoce como periodo orbital. El periodo orbital de la Tierra alrededor del Sol, es de 365 días. Es decir, un año. 

* Gracias a una relación matemática entre el periodo orbital y la distancia entre una estrella y un planeta, podemos tener una idea de que tan lejos está el planeta de su estrella. Esta relación matemática fue descubierta en el siglo XVII (17) para los planetas del sistema solar y se conoce como la Tercera Ley de Kepler. 

* Tamaño del planeta: La disminución del brillo que medimos depende directamente de que tan grande es un planeta respecto a su estrella. Un planeta grande va a bloquear más brillo que el que bloquea un planeta pequeño. Para poder saber el tamaño del planeta, debemos también conocer el tamaño de la estrella, de otra forma, solo tendremos que tan grande es el planeta respecto a su estrella. 

* Inclinación de la orbita: Como mencionamos al inicio, para que se de un tránsito, la orbita del planeta debe estar alineada con quien observa. La inclinación de la orbita del planeta, tiene un efecto directo en la forma del transito dependiendo de si pasa más cerca al centro de la estrella o si pasa más cerca al borde. 

* Oscurecimiento del borde estelar: La forma del tránsito también depende de cómo brilla la estrella en su superficie. Resulta que las estrellas no brillan uniformemente y desde nuestra perspectiva pareciera que son más brillantes en el centro que en el borde, eso se conoce como oscurecimiento del borde (Limb darkening) y tiene un efecto directo en la forma del tránsito. 

Algunos de estos conceptos como profundidad del transito, tamaño del planeta respecto a su estrella, inclinación de la orbita y oscurecimiento del borde pueden ser confusos a la hora de entender las curvas de luz generadas por planetas transitantes. Es por eso, que he preparado un simulador científicamente acertado que muestra como se ven la curva de luz de tránsitos de planetas de diferentes tamaños, con distintas inclinaciones orbitales, alrededor de estrellas con diferentes tamaños y diferentes tipos de oscurecimiento en el borde.

Aquí dejo algunas preguntas que pueden resultar útiles para responder con ayuda del simulador. 

1. Fija el radio de la estrella ($R_★$) a 2 radios solares ($R_\odot$) y determina la profundidad del tránsito de un planeta como la tierra (1 $R_\oplus$) y y de un planeta como Júpiter (~11$R_\oplus$)

2. Fija el radio de la estrella ($R_★$) a 0.7 radios solares ($R_\odot$) y el del planeta a 6 radios de la tierra ($R_\oplus$). Ahora mueve la inclinación de la orbita $i$ y analiza ¿qué pasa con la forma del transito?, ¿Que pasa cuando parte del planeta está fuera de la estrella?

3. Fija el radio de la estrella y el planeta a los valores que desees y la inclinación a 90° y varía el oscurecimiento del borde de la estrella con $u_1$ y $u_2$. ¿Qué cambia en la estrella?, ¿Qué cambia en la forma del tránsito?

4. Varía el tamaño de la estrella y analiza su cambio de color. A qué crees que se deba el cambio de color? No dudes en investigar más a fondo esta idea de por qué cambia el color de una estrella con su tamaño. 

# Simulador de exoplanetas transitantes

<iframe src="/simuladores/transito/transito.html"
        title="Simulador de tránsito planetario"
        loading="lazy"
        style="width:150%;height:1000px;border:0;border-radius:16px;">
</iframe>