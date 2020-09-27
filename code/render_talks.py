from pathlib import Path
from datetime import datetime

import jinja2
import pytz
from ruamel.yaml import YAML

yaml = YAML(typ='safe')
with open('../talks.yml') as f:
    talks = yaml.load(f)

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('../templates')
)

for talk in talks:
    talk['time'] = talk['time'].replace(tzinfo=pytz.UTC)

Path('../speakers_corner.md').write_text(
    env.get_template('speakers_corner.md.j2').render(
        talks=[talk for talk in talks if talk['event_type'] == 'speakers_corner'],
        now=datetime.now(tz=pytz.UTC)
    )
)
