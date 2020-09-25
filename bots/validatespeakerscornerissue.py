import os
from datetime import date, datetime, timedelta
from dateutil.parser import parse
from dateutil.utils import today
from github import Github
import re
import arxiv

test_mode = True

VSF_BOT_TOKEN = os.getenv("VSF_BOT_TOKEN")
ISSUENUMBER = os.getenv("ISSUENUMBER")

TEAM_CHECKLIST = "[ ] There are no scheduling conflicts \n" \
                 "[ ] Everything is generally in order \n"

def check_date(timeslot):

    scheduled_date = parse(timeslot[:-4])
    print("Scheduled date")
    print(scheduled_date)

    #if scheduled_date - today() < timedelta(days=14):
    #    return False, "Please schedule your talk at least two weeks into the future"

    return True, "Ok"

def check_arxiv(submission):
    # 1) Check if preprint exists
    arxiv_result = arxiv.query(id_list=[submission['preprint_ID']])

    if not arxiv_result:
        return False, "Your arXiv preprint ID could not be found"

    # Extract the paper
    if( submission.get("title", "") == ""):
        submission["title"] = arxiv_result[0].title.replace('\n ', '')
    if( submission.get("abstract", "") == ""):
        submission["abstract"] = arxiv_result[0].summary
    submission["authors"] = arxiv_result[0].authors

    return True, "arxiv ok"

def update_issue_body(issue_body, submission):
    b = issue_body

    # Update the title
    before, after = b.split("Title")
    b = before + "Title\n\n" + submission["title"] + after

    # Update the abstract
    before, after = b.split("Abstract")
    b = before + "Abstract\n\n" + submission["abstract"] + after

    # Add the authors
    current_notes = b.split("Notes")[1].split()[0]
    current_notes = "Authors: " + ", ".join(submission.get("authors", "Uknown"))
    before, after = b.split("Notes")
    b = before + "Notes\n\n" + current_notes + after

    return b

def format_issue_comments(comments):
    comment_body = "I am sorry, I was unable to successfully process your data.\n"
    comment_body += "Please amend the following issues: \n"

    for c in range(len(comments)-1):
        comment_body += "* " + comments[c] + "\n"
    comment_body += "* " + comments[-1]

    return comment_body

def format_team_checklist(TEAM_CHECKLIST):
    checklist_body = "Your submission looks good! \n"
    checklist_body += "A member of our team will now verify that: \n"
    checklist_body += TEAM_CHECKLIST
    return checklist_body

def parse_issue(issue_body):
    b = str(issue_body)

    # Replace all <!-- * --> lines
    b = re.sub(r'<!--.*?-->', '', b)
    b = re.split(r'\n## (.*)\n', b)

    submission = dict(
        name = b[2].lstrip('\n').rstrip('\n'),
        email = b[4].lstrip('\n').rstrip('\n'),
        preprint_ID = b[6].lstrip('\n').rstrip('\n\n'),
        title = b[8].lstrip('\n').rstrip('\n'),
        abstract = b[10].lstrip('\n').rstrip('\n'),
        timeslot = b[12].lstrip('\n').rstrip('\n'),
        notes = b[14].lstrip('\n').rstrip('\n'),
    )

    return submission

def validate_issue(issue_body):
    # Create a copy of the body
    submission = parse_issue(issue_body)
    date_valid, date_msg = check_date(submission['timeslot'])
    arxiv_valid, arxiv_msg = check_arxiv(submission)

    # If we have a valid preprint, we can amend the issue if required
    new_body = update_issue_body(issue_body, submission)

    comments = []
    if not date_valid:
        comments.append(date_msg)
    if not arxiv_valid:
        comments.append("Your arXiv preprint ID could not be found.")

    return comments, new_body

if __name__ == "__main__":
    g = Github(VSF_BOT_TOKEN)
    repo = g.get_repo("virtualscienceforum/virtualscienceforum")
    issue = repo.get_issue(number=ISSUENUMBER)

    #with open("exampleissue.txt", "r") as f:
    #        body = f.read()

    comments, new_body = validate_issue(body)

    if( (new_body != issue.body) and not test_mode):
        issue.edit(body=new_body)

    # If there were any problems, comment and return
    if( len(comments) != 0 ):
        issue_comments = format_issue_comments(comments)

        if test_mode:
            print("--- Issue Comments ---")
            print(issue_comments)
        else:
            issue.create_comment(issue_comments)

    else:
        # Add a checklist for team member to confirm if not already there
        checklist = format_team_checklist(TEAM_CHECKLIST)

        if test_mode:
            print("--- Team Checklist ---")
            print(checklist)
            print("--- New Body ---")
            print(new_body)
        else:
            issue.create_comment(checklist)

        # Check for Zoom link in corresponding YAML
        # AddUserChecklist
