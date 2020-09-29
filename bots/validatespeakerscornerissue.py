import os
import re
from copy import deepcopy
from pathlib import Path
from datetime import date, datetime, timedelta
import logging

from dateutil.parser import parse, ParserError
from github import Github
from ruamel.yaml import YAML
import arxiv
import jinja2
import pytz


yaml = YAML()

TEAM_CHECKLIST = jinja2.Template("""Your submission looks good!
{% if edits %}
{{ edits }}
{% endif %}
As the next step, a team member will check that:

- [ ] Everything is generally in order
- [ ] There are no scheduling conflicts
- [ ] The author's email is institutional or otherwise known

They will respond here and once everything looks good add the "approved" label.
""")

RESPONSE_TEMPLATE = jinja2.Template(
"""Hi! I checked your application, I found the following issues:

{% for fail in failed %}
- {{ fail }}
{% endfor %}

Please fix that by editing the issue description.
""")

ISSUE_TEMPLATE = jinja2.Template(
    Path("../templates/speakers_corner_application.md.j2").read_text()
)

with open("speakers_corner_questions.yml") as f:
    questions = yaml.load(f)


def check_name(name):
    if not name.strip():
        return "Please provide your name"


def check_date(timeslot):

    try:
        scheduled_date = parse(timeslot)
    except ParserError:
        return "I couldn't parse the date, please use YYYY-MM-DD HH:MM UTC."

    logging.debug(f"{scheduled_date=}")

    if scheduled_date - datetime.now(tz=pytz.UTC) < timedelta(days=14):
        return "Please schedule your talk at least two weeks into the future."


def check_arxiv(preprint):
    if not arxiv.query(id_list=[preprint]):
        return "Your arXiv preprint ID could not be found"


def check_confirmation(confirmation):
    if confirmation.replace("\r", "") != questions["confirmation"]["text"].strip():
        print(confirmation.strip())
        print(questions["confirmation"]["text"].strip())
        return "You have to confirm that you accept all rules"


def update_from_arxiv(submission):
    arxiv_result = arxiv.query(id_list=[submission['preprint']])[0]
    updated_entries = []
    if not submission["title"]:
        submission["title"] = arxiv_result.title.strip()
        updated_entries.append("title")
    if not submission["abstract"]:
        submission["abstract"] = arxiv_result.summary
        updated_entries.append("abstract")
    if not submission["authors"]:
        submission["authors"] = ', '.join(arxiv_result.authors)
        updated_entries.append("authors")

    if updated_entries:
        return "I updated " + ", ".join(updated_entries)


def parse_issue(issue_body):
    # Remove html comments.
    issue_body = re.sub(r'<!--.*?-->', '', issue_body)

    # Skip the first part because it is befor the first question
    parts = re.split(r'^## (.*?)$', issue_body, flags=re.MULTILINE)[1:]

    # We're using zip(iter, iter) idiom,
    # see "grouper" at https://docs.python.org/3/library/itertools.html
    parts = iter(parts)
    answers = {title.strip(): answer.strip() for title, answer in zip(parts, parts)}
    question_titles = set(question["name"] for question in questions.values())

    if missing := (question_titles - set(answers)):
        raise ValueError(
            f"Missing questions{'s' * (len(missing) > 1)}: "
            + ", ".join(missing)
        )
    if extra := (set(answers) - question_titles):
        raise ValueError(
            f"Extra section{'s' * (len(extra) > 1)}: "
            + ", ".join(extra)
        )

    submission = {
        next(
            question
            for question, data in questions.items()
            if data["name"] == title
        ): answer
        for title, answer in answers.items()
    }

    return submission


def validate_issue(issue_body):
    try:
        submission = parse_issue(issue_body)
    except ValueError as e:
        msg = e.args[0]
        if "Missing questions" in msg or "Extra sections" in msg:
            return issue_body, f"Sorry, couldn't parse issue;\n\n{msg}"
        raise e

    failed_checks = [
        message
        for check, value in
        zip(
            (check_name, check_arxiv, check_confirmation, check_date),
            ("name", "preprint", "confirmation", "time")
        )
        if (message := check(submission[value])) is not None
    ]

    if failed_checks:
        return issue_body, RESPONSE_TEMPLATE.render(failed=failed_checks)

    updates = update_from_arxiv(submission)

    answers = deepcopy(questions)

    for question, data in answers.items():
        data['text'] = submission[question]

    return (
        ISSUE_TEMPLATE.render(questions=answers),
        TEAM_CHECKLIST.render(edits=updates)
    )


def render_application_template():
    Path("../.github/ISSUE_TEMPLATE/speakers_corner_application.md").write_text(
        ISSUE_TEMPLATE.render(questions=questions, issue_template=True)
    )


if __name__ == "__main__":
    issue_number = int(os.getenv("ISSUE_NUMBER"))
    g = Github(os.getenv("VSF_BOT_TOKEN"))
    repo = g.get_repo("virtualscienceforum/virtualscienceforum")
    issue = repo.get_issue(number=issue_number)

    new_body, response = validate_issue(issue.body)

    if new_body != issue.body:
        issue.edit(body=new_body)

    issue.create_comment(response)
