import os
from datetime import date, timedelta
from github import Github
import arxiv

VSF_BOT_TOKEN = os.getenv("VSF_BOT_TOKEN")
ISSUENUMBER = os.getenv("ISSUENUMBER")

g = Github(VSF_BOT_TOKEN)
repo = g.get_repo("virtualscienceforum/virtualscienceforum")
issue = repo.get_issue(number=ISSUENUMBER)

def check_date(date_str, time_str):
    scheduled_date = date.fromisoformat(dateStr)
    if scheduled - datetime.now() < timedelta(days=14):
        return False, "Please schedule your talk at least two weeks into the future"

    return True, "Ok"

def check_arxiv(preprint_ID):
    # 1) Check if preprint exists
    arxiv_result = arxiv.query(id_list=[preprint_ID])

    if not arxiv_result:
        return False, {}

    # Extract the paper
    return True, dict(
        title=arxiv_result[0].title.replace('\n ', ''),
        abstract=arxiv_result[0].summary,
        authors=arxiv_result[0].authors,
    )

def update_issue(current_body, preprint):
    b = current_body

    # Extract the current title and abstract
    title = b.split("Title")[1].split()[0]
    abstract = b.split("Abstract")[1].split()[0]

    # If the title has been left empty, update it
    if (title == "<!--"):
        before, after = b.split("Title")
        b = before + "Title\n\n" + preprint["title"] + after

    # If the abstract has been left empty, update it
    if (abstract == "<!--"):
        before, after = b.split("Abstract")
        b = before + "Abstract\n\n" + preprint["abstract"] + after

    # Add the authors
    current_notes = b.split("Notes")[1].split()[0]
    current_notes = "Authors: " + ", ".join(preprint["authors"])
    before, after = b.split("Notes")
    b = before + "Notes\n\n" + current_notes + after

    issue.edit(body=b)

def add_comments(comments):
    comment_body = "I am sorry, I was unable to successfully process your data.\n"
    comment_body += "Please amend the following issues: \n"

    for c in range(len(comments)-1):
        comment_body += "* " + comments[c] + "\n"
    comment_body += "* " + comments[-1]

    issue.create_comment(comment_body)

def add_team_checklist():
    checklist_body = "Your submission looks good! \n"
    checklist_body += "A member of our team will now verify that: \n"
    checklist_body += "[ ] There are no scheduling conflicts"
    checklist_body += "[ ] Everything is in order"
    issue.create_comment(checklist_body)

def parse_issue():
    b = issue.body

    #with open("exampleissue.txt", "r") as f:
    #   b = f.read()

    # Validate the date: must be sufficiently far into the future
    date = b.split("Time slot (at least 14 days ahead)")[1].split()
    day = date[0]
    time = date[1]
    date_valid, date_msg = check_date(day, time)

    # Grab title, abstract and authors, edit the description
    arxiv_ID = b.split("Preprint ID")[1].split()[0]
    arxiv_valid, preprint = check_arxiv(arxiv_ID)

    # If we have a valid preprint, we can amend the issue if required
    if( arxiv_valid ):
        update_issue(b, preprint)

    comments = []
    if not date_valid:
        comments.append(dateMsg)
    if not arxiv_valid:
        comments.append("Your arXiv preprint ID could not be found.")

    # If there were any problems, comment and return
    if( len(comments) != 0 ):
        add_comments(comments)
        return
    else:
        # Add a checklist for team member to confirm if not already there
        add_team_checklist()

        # Check for Zoom link in corresponding YAML
        # add_user_checklist

if __name__ == "__main__":
    parse_issue()
