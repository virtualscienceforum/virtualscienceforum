import os
import re
from copy import deepcopy
from pathlib import Path
from io import StringIO
import datetime

from dateutil.parser import parse, ParserError
import github
from ruamel.yaml import YAML
import jinja2

import validatespeakerscornerissue

yaml = YAML()
TALKS_FILE = "talks.yml"
EVENT_TYPES = ["speakers_corner", "lrc"]

def add_talk(gh, issue_number):
    repo = gh.get_repo("virtualscienceforum/virtualscienceforum")
    issue = repo.get_issue(number=issue_number)

    # Only one of the talk type labels must be present.
    event_type, = (
        name for name in EVENT_TYPES
        if any(l.name == name for l in issue.labels)
    )

    talks_data = repo.get_contents(TALKS_FILE, ref="master")
    talks = yaml.load(StringIO(talks_data.decoded_content.decode()))

    if event_type == "speakers_corner":
        if any(talk.get('workflow_issue') == issue_number for talk in talks):
            issue.create_comment("The talk is already scheduled, cannot update.")
            return

        try:
            submission = validatespeakerscornerissue.parse_issue(issue.body, questions)
        except ValueError:
            issue.create_comment("Could not process issue, data is invalid.")
            return

        try:
            submission['time'] = parse(submission['time'])
        except ParserError:
            issue.create_comment("Could not determine the talk date")
            return

        submission.pop('notes')
        submission.pop('confirmation')

        response = Path("../templates/talk_registered.md").read_text()

    elif event_type == "lrc":
        with open('lrc_questions.yml') as f:
            questions = yaml.load(f)

        try:
            submission = validatespeakerscornerissue.parse_issue(issue.body, questions)
        except ValueError:
            issue.create_comment("Could not process issue, data is invalid.")
            return

        submission['time'] = (
            parse(submission['time'])
            .replace(hour=18, minute=30, tzinfo=datetime.timezone.utc)
        )
        submission.pop("checlist")

        response = "I added/updated the talk!"

    talks.append(dict(
        workflow_issue=issue_number,
        event_type=event_type,
        **submission,
    ))
    serialized = StringIO()
    yaml.dump(talks, serialized)

    if talks_data is not None:
        repo.update_file(
            TALKS_FILE, f"Add a talk from #{issue_number}",
            serialized.getvalue(),
            sha=talks_data.sha,
            branch='master'
        )
    else:
        repo.create_file(
            TALKS_FILE, f"Add a talk from #{issue_number}",
            serialized.getvalue(),
            branch='master'
        )
    # Respond with instructions
    issue.create_comment(response)

if __name__ == "__main__":
    issue_number = int(os.getenv("ISSUE_NUMBER"))
    gh = github.Github(os.getenv("VSF_BOT_TOKEN"))
    add_talk(gh, issue_number)
