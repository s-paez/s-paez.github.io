---
title: Reducción de datos para OPTICAM
summary: Mi principal trabajo de maestría fue desarrollar e implementar un método de reducción de datos.
date: 2025-10-12
authors:
  - admin
tags:
  - Exoplanetas
  - Artículo
  - Tránsitos
image:
  filename: "paper_title.jpeg"
  caption:
  focal_point: "Center"
  preview_only: True
---
> Aquí intento explicar de manera sencilla para personas fuera del campo de los exoplanetas y la astronomía en general, mi trabajo de maestría publicado en la revista RAS Techniques and Instruments.


## OPTICAM

OPTICAM es un instrumento que se instala en el Telescopio de 2.1m del Observatorio Astronómico Nacional en la Sierra de San Pedro Mártir. Tiene 3 cámaras que permiten tomar imágenes en tres "colores" diferentes esto es valioso porque las estrellas emiten diferentes cantidades de luz en diferentes colores. Esto depende de la temperatura a la que está la superficie de la estrella. 

En el caso del estudio de exoplanetas transitantes, observar en tres colores al mismo tiempo y con muy alta precisión permite descartar casos donde señales parecidas a las de planetas son en realidad originadas por otros fenómenos astrofísicos. 

Desde el principio de mi maestría, comencé a trabajar con datos de este instrumento y junto con mi tutora, nos dimos cuenta que las imágenes de cada cámara tenían gran cantidad de píxeles brillantes especialmente en tiempos de exposición de más de 10 segundos, por lo que nos propusimos evaluar el impacto que tenían estos píxeles brillantes en la calidad de nuestros datos de exoplanetas en tránsito. 

## Píxeles tibios

Cuando comenzamos a analizar estos píxeles brillantes en las imágenes de OPTICAM les llamamos píxeles calientes, sin embargo después encontramos que un mejor término para nombrarlos es píxeles tibios, hay diferencias técnicas importantes reflejadas en ambos nombres. 

El caso es que comenzamos a estudiar su comportamiento, analizamos como cambiaban entre cada imagen en una serie de imágenes consecutivas, era importante saber si eran constantes, si aumentaban o si disminuían entre imágenes y entre fechas de observación. Lo primero que encontramos es que eran alta e impredeciblemente variables. Cambian en número y posición entre imágenes consecutivas y principalmente, aumentan con el tiempo de exposición de lás imágenes. También encontramos que hay diferentes tipos de píxeles tibios que se comportan de manera diferente. En nuestro artículo, describimos las cuatro categorías que logramos identificar. 

## De imágenes a curvas de luz

Lo que tomamos con OPTICAM en el Telescopio de 2.1m son secuencias de imágenes durante el tiempo que dura un planeta pasando frente a su estrella anfitriona (en realidad intentamos observar antes y después de que el planeta pasa frente a la estrella) y el resultado son algunos cientos de imágenes que se tomaron al mismo tiempo en cada una de las cámaras. Para trasformar estas imágenes en una curva de luz (que son los datos de nivel de brillo de la estrella en función del tiempo) para poder analizar el planeta que pasó en frente, necesitamos realizar la reducción de datos y la fotometría. 

La reducción de datos consiste en quitar la contribución de ruidos conocidos introducidos especialmente por los detectores y por imperfecciones en el espejo del telescopio o los lentes del instrumento que pueden acumular polvo y/o generar otro tipo de aberraciones. Este proceso se hace adquiriendo imágenes de calibración y luego mediante un procesamiento con software se corrigen las imágenes. 

Una vez se ha hecho la reducción de datos, usamos una técnica que se conoce como fotometría diferencial para medir el brillo de la estrella a y convertir cada imagen en un punto en una curva de luz. La fotometría diferencial, en pocas palabras, consiste en medir el brillo de la estrella con el planeta y estrellas cercanas que sirven de comparación. La lógica es que sí la estrella con el planeta, tiene una variación que también se ve en la estrellas de comparación, entonces no es una variación propio de la estrella sino una variación externa, por ejemplo en la atmósfera. Por el contrario, si se ve una variación en el brillo de la estrella con el planeta y esa variación no se ve en las estrellas de comparación entonces es una variación propia de la estrella de interés. 

La precisión con la que se pueden medir las variaciones en el brillo de la estrella de interés depende de cuantas estrellas de comparación se usaron, el nivel de variación es estas, su nivel de brillo, entre otros factores relacionados al funcionamiento del telescopio, las cámaras y los detectores. Para dimensionar el reto, para estudiar exoplanetas necesitamos alcanzar precisiones que nos permitan medir variaciones alrededor del 0.01% en el brillo de la estrella. 