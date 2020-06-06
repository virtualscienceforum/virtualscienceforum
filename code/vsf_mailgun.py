# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import zipfile
import json
from pathlib import Path
from getpass import getpass
import ics

import requests
from requests import get, post, put
import pandas
from IPython.display import HTML

import icalendar
from icalendar import vCalAddress, vText
from datetime import datetime, timedelta
import pytz
from pathlib import Path
# -

key = getpass()

# +
mailgun_base_url = "https://api.eu.mailgun.net/v3/"
domain = "mail.virtualscienceforum.org/"

def decode(response):
    if response.status_code != 200:
        raise RuntimeError(response.content.decode())
    return json.loads(response.content.decode())

def api_query(method, endpoint, **params):
    return decode(method(
        mailgun_base_url + endpoint,
        auth=("api", key),
        **params
    ))


# -

template = """Dear %recipient_name%,

Thank you for registering for today's Long Range Colloquium! It will begin in three hours (19:30 CEST / 1:30 PM ET).
You should have received the meeting link right after your registration.
If you cannot find the link anymore, please fill out the registration form again at https://virtualscienceforum.org/#/long_range_colloquium?id=nicola-spaldin-eth-z%c3%bcrich

Today's speaker is {speaker_name} ({speaker_affiliation}). See the title and the abstract of her talk below.

Title: {title}

Abstract: {abstract}

See you soon,
The Virtual Science Forum team"""

html = HTML(
    '<p><html>'
    + (template.format(**event_data)
       .replace('\n\n', '</p><p>')
       .replace('\n', '<br>')
       .replace('Title:', '<b>Title:</b>')
       .replace('Abstract:', '<b>Abstract:</b>')
       .replace("at https://virtualscienceforum.org/#/long_range_colloquium?id=nicola-spaldin-eth-z%c3%bcrich",
                '<a href="https://virtualscienceforum.org/#/long_range_colloquium?id=nicola-spaldin-eth-z%c3%bcrich">here</a>.'))
    + '</p></html>'
)

# +
# TODO: get zoom meeting id from zoom

requests.post(
    "https://api.eu.mailgun.net/v3/mail.virtualscienceforum.org/messages",
    auth=("api", key),
    data={
        "from": "Long Range Colloquium <no-reply@mail.virtualscienceforum.org>",
        "to": list({f"{i._1} {i._2} <{i.Email}>" for i in data.itertuples()}),
        "subject": "Long Range Colloquium starting soon!",
        "text": template,
        "html": html.data,
        "recipient-variables": json.dumps({i.Email: {'zoom_meeting_id': i.meeting_id} for i in data.itertuples()}),
    }
)
# -

r.text

# ## Update the mailing list

# +
## This mailing list is read-only (can only be used from API), and therefore not a secret

announce_list = 'vsf-announce@mail.virtualscienceforum.org'
# -

api_query(get, f'lists/{announce_list}/members')['total_count']

failures = requests.get(
    mailgun_base_url + 'events',
    auth=("api", key),
    params=dict(event='failed'),
)

data = pandas.read_csv('RegistrationReport.csv')

to_subscribe = {
    i.Email: f"{i._1} {i._2}"
    for i in data[data["May we contact you about future Virtual Science Forum events?"] == 'Yes'].itertuples()
}

api_query(
    post, f'lists/{announce_list}/members.json',
    data=dict(members=json.dumps([
        dict(address=email, name=name)
        for email, name in to_subscribe.items()
    ]))
)

# ## Announce

event_data = dict(
    speaker_name="Klaus Mølmer",
    speaker_affiliation="Aarhus University",
    date=datetime(2020, 6, 10, tzinfo=pytz.timezone('Europe/Copenhagen')),
    speaker_pronoun="he",
    title="Quantum interactions with pulses of radiation",
    abstract='How does a quantum system interact with a travelling pulse of quantum radiation, prepared for example in a number state or a coherent state of light? While crucial for multiple effects in quantum optics and for the entire concept of flying and stationary qubits, quantum optics textbooks do not provide a formal description of this foundational and elementary interaction process. In this lecture, I shall introduce a new (and simple) master equation that describes the joint quantum state of travelling pulses of quantized radiation and local quantum systems. Applications of the theory will be presented for recent experiments with qubits and non-linear resonators interacting with pulses of optical, microwave and acoustic radiation.'
)

# +
announcement_template = """Dear %recipient_name%,

We would like to invite you to the upcoming VSF Long Range Colloquium that is going to take place Wednesday {date:%B %d} at 1:30 PM ET (19:30 PM CEST).

The speaker is {speaker_name} ({speaker_affiliation}), and {speaker_pronoun} is going to talk about "{title}".

To see the talk abstract and register, please go to https://virtualscienceforum.org/#/long_range_colloquium

Best regards,
The Virtual Science Forum team

---

You are receiving this email because you indicated that you are interested in updates from the Virtual Science Forum.
To unsubscribe visit %mailing_list_unsubscribe_url%
"""

html = ('<html><p>'
    + (announcement_template
       .replace('\n\n', '</p><p>')
       .replace('\n', '<br>')
       .replace('---', '<hr>')
       .replace('https://virtualscienceforum.org/#/long_range_colloquium', '<a href="https://virtualscienceforum.org/#/long_range_colloquium">the colloquium website</a>.')
       .replace('visit %mailing_list_unsubscribe_url%', '<a href="%mailing_list_unsubscribe_url%">click here</a>.')
    )
    + '</p></html>'
)

# +
duration = timedelta(hours=1, minutes=30)
start = event_data['date'] + timedelta(hours=19, minutes=30)

cal = icalendar.Calendar()
cal.add('prodid', '-//VSF announcements//virtualscienceforum.org//')
cal.add('version', '2.0')


event = icalendar.Event()
event.add('summary', f"Long Range Colloquium by {event_data['speaker_name']}")
event.add('description', f"Title: {event_data['title']}\n\nAbstract:{event_data['abstract']}")
event.add('dtstart', start)
event.add('dtend', start + duration)
event.add('dtstamp', datetime.now(tz=pytz.timezone('Europe/Amsterdam')))
event['uid'] = event['dtstart'].to_ical().decode() + '@virtualscienceforum.org'

organizer = vCalAddress('MAILTO:vsf@virtualscienceforum.org')
organizer.params['cn'] = vText('Virtual Science Forum')
event['organizer'] = organizer

cal.add_component(event)
# -

api_query(
    post, f'{domain}messages',
    data={
        "from": "Long Range Colloquium <no-reply@mail.virtualscienceforum.org>",
        "to": announce_list,
        "subject": f"Long Range Colloquium by {event_data['speaker_name']}",
        "text": announcement_template.format(**event_data),
        "html": html.format(**event_data),
    },
    files=[
        ("attachment", ("long_range_colloquium.ics", cal.to_ical()))
    ],
)
