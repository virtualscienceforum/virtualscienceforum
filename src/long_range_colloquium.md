{% from 'registration.md' import registration_form %}
# Long Range Colloquium

The Long Range Colloquium is a bi-weekly seminar series covering the latest developments in condensed matter physics and quantum information. We alternate experimental and theory talks to keep the schedule exciting for a varied audience: have a look at our 2021 schedule below!
You can also find all the information and recordings for our 2020 talks [here](/#/long_range_colloquium-2020).

The colloquium runs every other Wednesday at 1:30 PM ET / 19:30 CEST.
Attendance is open to everyone, but please register to attend! If you would like to hear about upcoming talks, you can subscribe to the colloquim mailing list [here](https://virtualscienceforum.org/#/mailinglist).

## Program

|   Date   |     Speaker    | Title |
|:---------:|:--------------:|:-----:|
{%- for talk in talks | sort(attribute="time") if talk.time > now() and talk.event_type == "lrc" %}
| {{ talk.time.strftime("%B %-d") }} | {{ talk.speaker_name }} | [{{ talk.title }}](#{{ talk.title | a }}) |
{%- endfor %}

## Upcoming talks

{% for talk in talks | sort(attribute="time") if talk.time > now() and talk.event_type == "lrc" %}
### {{ talk.speaker_name }} ({{ talk.speaker_affiliation }})
#### {{ talk.title }}

{% for line in talk.abstract.split("\n") -%}
> {{ line }}
{%- endfor %}

{% if talk.registration_url %}
If the form below doesn't work, [register directly]({{ talk.registration_url }})

{{ registration_form(talk) }}
{% endif %}
{% endfor %}

## Recordings

|     Speaker    | Title |
|:--------------:|:-----:|
{%- for talk in talks | sort(attribute="time") | reverse if talk.time < now() and talk.event_type == "lrc" %}
| {{ talk.speaker_name }} | [{{ talk.title }}](#{{ talk.title | a }}) |
{%- endfor %}


{% for talk in talks | sort(attribute="time") | reverse if talk.time < now() and talk.event_type == "lrc" %}

### {{ talk.title }}
**By {{ talk.speaker_name }} ({{ talk.speaker_affiliation }})**

===! "Abstract"

{{ talk.abstract | indent(width=4, first=True) }}

{% if talk.youtube_id %}

=== "Video recording"

    <div data-youtubeId="{{ talk.youtube_id }}"></div>

{% endif %}

{% endfor %}
