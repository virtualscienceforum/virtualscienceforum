---
title: ARQH workshop
description: Review of experimental progress and further directions in search of Andreev reflection in quantum Hall systems
hide:
  - navigation
---
{% from 'registration.md' import registration_form %}
# Andreev reflection in quantum Hall systems: 2021 state of the union 
**<time data-format="MMMM D YYYY H:mm" datetime="2021-12-09T14:30:00+00:00">December 9 2021 14:30</time>–<time data-format="H:mm" datetime="2021-12-09T17:00:00+00:00">17:00</time>** (all times are in <span id="timezone">UTC</span> timezone)

![Collage of Andreev quantum Hall systems](media/arqh_collage.svg){ width=80% }

A combination of superconductivity with quantum Hall effect allows perfectly nonlocal crossed Andreev reflection, which has made it a target of experimental search for more than a decade.

Due to progress in material physics and emergence of new hybrid platforms, this search has resulted in a series of
experiments observing a combined effect of chiral edge states and superconductivity.
At the same time, measurements of Andreev conductance in the quantum Hall regime demonstrate wildly different behaviors,
sometimes in disagreement with existing theoretical predictions.

In this workshop we aim to bring together experts working in the field, review observations and their interpretation, and identify the possible ways forward.

**To join the meeting, please [register](#registration).**

## Program

**<time data-format="MMMM D" datetime="2021-12-09T14:30:00+00:00">December 9</time>**

- <time data-format="H:mm" datetime="2021-12-09T14:30:00+00:00">14:30</time> Welcome
- <time data-format="H:mm" datetime="2021-12-09T14:35:00+00:00">14:35</time>    [**Carlo Beenakker**](https://www.lorentz.leidenuniv.nl/beenakker/), Leiden University  
    *The search for chiral Andreev edge states*  
- <time data-format="H:mm" datetime="2021-12-09T14:55:00+00:00">14:55</time>    [**Önder Gül**](https://kim.physics.harvard.edu/people/onder-gul), Harvard University  
    *Crossed Andreev reflection in fractional quantum Hall graphene devices*    
    Based on [arXiv:2009.07836](https://arxiv.org/abs/2009.07836) and [arXiv:1609.08104](https://arxiv.org/abs/1609.08104)   
- <time data-format="H:mm" datetime="2021-12-09T15:15:00+00:00">15:15</time>    [**Gleb Finkelstein**](http://webhome.phy.duke.edu/~gleb/), Duke University  
    *Supercurrent and Andreev edge states in the quantum Hall regime*    
    Based on [arXiv:1901.05928](https://arxiv.org/abs/1901.05928) and [arXiv:1907.01722](https://arxiv.org/abs/1907.01722)   
- <time data-format="H:mm" datetime="2021-12-09T15:35:00+00:00">15:35</time>    [**Javad Shabani**](https://wp.nyu.edu/shabanilab/), New York University  
    *Integer quantum Hall effect with a superconducting contact*    
    Based on [arXiv:2108.08899](https://arxiv.org/abs/2108.08899) and ongoing work
- <time data-format="H:mm" datetime="2021-12-09T15:55:00+00:00">15:55</time> Panel discussion with speakers and the participants
- <time data-format="H:mm" datetime="2021-12-09T17:00:00+00:00">17:00</time> Concluding Remarks

## Satellite talks

We invite the workshop participants to view the recordings of relevant talks below.

{% set talk1 = talks | selectattr("workflow_issue", "==", 462) | first %}
{% set talk2 = talks | selectattr("workflow_issue", "==", 471) | first %}

#### {{ talk1.title }}
**By {{ talk1.speaker_name }} ({{ talk1.speaker_affiliation }})**

===! "Video recording"

    <iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/{{ talk1.youtube_id }}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

=== "Details"

    **Authors:** {{ talk1.authors }}  
    **Preprint:** [arXiv:{{ talk1.preprint }}](https://arxiv.org/abs/{{ talk1.preprint }})


    {{ talk2.abstract | indent(width=4) }}

#### {{ talk2.title }}
**By {{ talk2.speaker_name }} ({{ talk2.speaker_affiliation }})**

===! "Video recording"

    <iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/{{ talk2.youtube_id }}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

=== "Details"

    **Authors:** {{ talk2.authors }}  
    **Preprint:** [arXiv:{{ talk2.preprint }}](https://arxiv.org/abs/{{ talk2.preprint }})


    {{ talk2.abstract | indent(width=4) }}


### Mesoscopic conductance along the proximitized quantum Hall edge
** by Vladislav D. Kurilovich (Department of Physics, Yale University)**

===! "Video recording"

    <iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/y0RkSdphwh4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

=== "Details"

    **Authors:** Vladislav D. Kurilovich, Leonid Glazman  
    **Preprint:** [arXiv:2201.00273](https://arxiv.org/abs/2201.00273)

### Induced Superconductivity in FQH Edges in Presence of Dissipation
** by Noam Schiller (Weizmann Institute) and Barak A. Katzir (Technion)**

===! "Video recording"

    <iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/h0rS7TyUUMI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

=== "Details"

    **Authors:** Noam Schiller, Barak A. Katzir, Ady Stern, Erez Berg, Netanel Lindner, Yuval Oreg

## Organizers

[Anton Akhmerov](https://antonakhmerov.org/), TU Delft  
[Valla Fatemi](https://fatemilab.aep.cornell.edu/), Yale University & Cornell University  
[Christian Schoenenberger](https://nanoelectronics.unibas.ch/), University of Basel

If you have any questions, you may reach us via arqh2021@virtualscienceforum.org
