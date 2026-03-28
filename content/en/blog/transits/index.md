---
title: Transiting Exoplanets
summary: What they are and what we can learn from exoplanet transits.
date: 2025-10-12
authors:
  - admin
tags:
  - Exoplanets
  - Simulator
  - Transits
image:
  filename: "simulator.png"
  caption:
  focal_point: "Center"
  preview_only: True
---
> In this post I explain the transit method, why light curves are so valuable, and I share an interactive resource to experiment with different planetary scenarios.

<iframe src="/simulators/transit/transit0.html"
        title="Transiting planet animation"
        loading="lazy"
        style="width:100%;max-width:100%;height:1200px;border:0;border-radius:16px;margin:0 auto;display:block;">
</iframe>

## What is a transiting planet?

A planet is said to be in transit when its orbit takes it in front of its star from our line of sight. During that crossing it blocks a tiny fraction of the starlight, producing a brief and periodic dip in the observed brightness. The shape and repetition of that change form the signature that lets us infer the presence of the planet.

The way we study transiting exoplanet are light curves. A light curve records the brightness of a star over time. When we plot those consecutive measurements, the transits appear as U-shaped decreases. A much shallower drop can also be seen when the planet passes behind the star: that is the secondary eclipse, which reveals the small contribution of starlight reflected by the planet.

## How do we detect these planets?

The transit method demands continuous and precise observations. From the ground we depend on night time, weather, and the visibility of the target, so the light curves are often fragmented. Space missions such as [TESS](https://www.nasa.gov/tess/) and [Kepler](https://science.nasa.gov/mission/kepler/) overcame those limitations by monitoring thousands of stars without interruption, making it possible to detect brightness drops of just a few tenths of a percent and to gather fully continuous time series.

## What can we learn from a transit?

A detailed analysis of the light curve offers multiple clues about the star-planet system:

- **Orbital period**: the time between consecutive transits tells us how long the planet takes to complete one orbit.
- **Relative size**: the depth of the transit depends on the ratio between the planet’s radius and the star’s radius.
- **Orbital distance**: combining the period with Kepler’s laws allows us to estimate how far the planet is from its star.
- **Estimated temperature**: with the distance and the stellar brightness we can calculate how much energy the planet receives.
- **Orbital geometry**: the transit shape changes if the planet crosses the center of the stellar disk or just grazes the edge.
- **Stellar properties**: stars are not uniformly bright; limb darkening leaves traces in the ingress and egress of the transit.

## Guiding questions for the simulator

The following interactive simulator incorporates the same physical model we use to calculate the planetary and orbital parameters of a transiting exoplanet, it is physically inspired. It takes into account the stellar and planetary radii, the orbit inclination and the brightness profiles of the star using a quadratic law. 

The interactive simulator reproduces these effects and lets you explore different parameters. Here are a few prompts to get started:

1. Fix the stellar radius at 2 solar radii and compare the transit depth for a planet with 1 Earth radius and another with 11 Earth radii. How does the curve change and why?
2. Keep a planet of 6 Earth radii orbiting a star of 0.7 solar radii and modify the inclination. Watch how the duration and shape of the transit adjust when part of the planet no longer projects onto the star.
3. Set the inclination to 90° and experiment with the limb-darkening parameters ($u_1$ and $u_2$). What happens to the visibility of the transit edges, and what does that tell you about the stellar atmosphere?
4. Change the size of the star and pay attention to the color shift in the visualization. Investigate how stellar temperature relates to its hue.

# Transiting exoplanet simulator
Conventions:
* $R_\star$: Stellar radius
* $R_p$: Planet radius
* $R_\oplus$: Earth radii
* $R_\odot$: Solar radii

<iframe src="/simulators/transit/transit.html"
        title="Planetary transit simulator"
        loading="lazy"
        style="width:100%;max-width:100%;height:1100px;border:0;border-radius:16px;margin:0 auto;display:block;">
</iframe>

The transit method has confirmed thousands of exoplanets and will remain essential to identify potentially habitable worlds. Dive into the simulators, form hypotheses, and look for patterns that you can contrast with real observations.
