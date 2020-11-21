from pathlib import Path
import os
from datetime import date

import jinja2
from dateutil import relativedelta
from github import Github
import requests
import bs4

def new_hackmd_note(source):
    response = requests.get('https://hackmd.io')
    token = bs4.BeautifulSoup(response.content).find("meta", attrs=dict(name="csrf-token"))["content"]
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
    g = Github(os.getenv("VSF_BOT_TOKEN"))
    template = jinja2.Template(Path('../templates/org_meeting.md').read_text())
    meeting_date = date.today() + relativedelta.relativedelta(relativedelta.TU)
    title = f"VSF Organizational Meeting {meeting_date} 7pm CEST / 1pm EST"

    repo = g.get_repo("virtualscienceforum/virtualscienceforum")

    repo.create_issue(
        title=title,
        body=template.render(
            hackmd=new_hackmd_note(
                f"# {title}\n\n## Present: \n\n* \n\n## Next chair\n\nChair name\n"
            )
        )
    )
