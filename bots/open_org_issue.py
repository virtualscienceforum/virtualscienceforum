from pathlib import Path
import os
from datetime import datetime, timedelta

import jinja2
from ruamel.yaml import YAML
from github import Github
import requests
import bs4

def new_hackmd_note(source):
    response = requests.get('https://hackmd.io')
    token = bs4.BeautifulSoup(response.content, 'html.parser').find("meta", attrs=dict(name="csrf-token"))["content"]
    result = requests.post(
        "https://hackmd.io/new", data={"content": source},
        headers={
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "X-XSRF-Token": token,
            "User-Agent": "HackMD Python client",
        },
        cookies=response.cookies,
    )
    return result.url

if __name__ == "__main__":
    yaml = YAML()
    g = Github(os.getenv("VSF_BOT_TOKEN"))
    with open("../.github/workflows/open_org_issue.yml") as f:
        data = yaml.load(f)
    minutes, hours_utc, *_ = data["on"]["schedule"][0]["cron"].split()
    meeting_time = datetime.now() + timedelta(days=7)
    meeting_time = meeting_time.replace(hour=int(hours_utc), minute=int(minutes))
    formatted_time = (
        f"{meeting_time + timedelta(hours=2):%-H:%M} European "
        f"/ {meeting_time - timedelta(hours=4):%-I:%M %p} Eastern"
    )
    template = jinja2.Template(Path('../templates/org_meeting.md').read_text())
    title = f"VSF Organizational Meeting {meeting_time:%-d %B} {formatted_time}"
    body=template.render(
        hackmd=new_hackmd_note(
            f"# {title}\n\n ## OPEN \n\n Present: \n Asynchronous contributors: \n\n## Next chair\n\nChair name\n"
        ),
        date=f"{meeting_time:%Y-%m-%d}",
        time=formatted_time
    )

    repo = g.get_repo("virtualscienceforum/virtualscienceforum")

    repo.create_issue(title=title, body=body)
