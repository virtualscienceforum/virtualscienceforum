from pathlib import Path
from datetime import datetime
import re
import string

import jinja2
import pytz
from ruamel.yaml import YAML

yaml = YAML(typ='safe')
with open('../talks.yml') as f:
    talks = yaml.load(f)

def format_title(s):
    punctuation = string.punctuation.replace('-','')
    s = s.translate(str.maketrans('', '', punctuation))
    return s.replace(' ', '-')
    
env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('../templates')
)
env.filters['format_title'] = format_title

header = Path("../speakers-corner-header.md").read_text()

for talk in talks:
    talk['time'] = talk['time'].replace(tzinfo=pytz.UTC)
    if re.fullmatch(r"\d{4}\.\d{5}", talk.get("preprint", "")) is None:
        talk.pop("preprint", "")

Path('../speakers-corner.md').write_text(
    env.get_template('speakers_corner.md.j2').render(
        header=header,
        talks=[talk for talk in talks if talk['event_type'] == 'speakers_corner'],
        now=datetime.now(tz=pytz.UTC)
    )
)

Path('../long_range_colloquium.md').write_text(
    env.get_template('long_range_colloquium.md.j2').render(
        header=header,
        talks=[talk for talk in talks if talk['event_type'] == 'lrc'],
        now=datetime.now(tz=pytz.UTC)
    )
)
