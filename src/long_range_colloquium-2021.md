{% from 'registration.md' import registration_form %}
# Long Range Colloquium

The Long Range Colloquium is a bi-weekly seminar series covering the latest developments in condensed matter physics and quantum information. We alternate experimental and theory talks to keep the schedule exciting for a varied audience: have a look at our 2021 schedule below!
You can also find all the information and recordings for our 2020 talks [here](/#/long_range_colloquium-2020).

## Recordings

|     Speaker    | Title |
|:--------------:|:-----:|
{%- for talk in talks | sort(attribute="time") | reverse if talk.time.year == 2021 and talk.event_type == "lrc" %}
| {{ talk.speaker_name }} | [{{ talk.title }}](#{{ talk.title | a }}) |
{%- endfor %}


{% for talk in talks | sort(attribute="time") | reverse if talk.time.year == 2021 and talk.event_type == "lrc" %}

### {{ talk.title }}
**By {{ talk.speaker_name }} ({{ talk.speaker_affiliation }}), <time datetime="{{ talk.time.isoformat() }}">{{ talk.time.strftime("%B %-d %-H:%M %Z") }}</time>**

===! "Abstract"

{{ talk.abstract | indent(width=4, first=True) }}

{% if talk.youtube_id %}

=== "Video recording"

    <div data-youtubeId="{{ talk.youtube_id }}"></div>

{% endif %}

{% endfor %}
