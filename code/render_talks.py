from pathlib import Path
from datetime import datetime

import jinja2
import pytz
from ruamel.yaml import YAML

yaml = YAML(typ='safe')
with open('../speakers_corner_talks.yml') as f:
    talks = yaml.load(f)

for talk in talks:
    talk['time'] = talk['time'].replace(tzinfo=pytz.UTC)

template = jinja2.Template(Path('speakers_corner.md.j2').read_text())

Path('../speakers_corner.md').write_text(template.render(talks=talks, now=datetime.now(tz=pytz.UTC)))
