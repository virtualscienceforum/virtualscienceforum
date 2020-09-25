import os
from datetime import date, timedelta
from github import Github
import arxiv

VSF_BOT_TOKEN = os.getenv("VSF_BOT_TOKEN")
ISSUENUMBER = os.getenv("ISSUENUMBER")

g = Github(VSF_BOT_TOKEN)
repo = g.get_repo("virtualscienceforum/virtualscienceforum")
issue = repo.get_issue(number=ISSUENUMBER)

def CheckDate(dateStr, timeStr):
    scheduledDate = date.fromisoformat(dateStr)
    if scheduled - datetime.now() < timedelta(days=14):
        return False, "Please schedule your talk at least two weeks into the future"

    return True, "Ok"

def CheckArxiv(preprintID):
    # 1) Check if preprint exists
    arxivResult = arxiv.query(id_list=[preprintID])

    if not arxivResult:
        return False, {}

    # Extract the paper
    return True, dict(
        title=arxivResult[0].title.replace('\n ', ''),
        abstract=arxivResult[0].summary,
        authors=arxivResult[0].authors,
    )

def UpdateIssue(currentBody, preprint):
    b = currentBody

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
    currentNotes = b.split("Notes")[1].split()[0]
    currentNotes = "Authors: " + ", ".join(preprint["authors"])
    before, after = b.split("Notes")
    b = before + "Notes\n\n" + currentNotes + after

    with open("updatesissue.txt", "w") as f:
        f.write(b)

    issue.edit(body=b)

def AddComments(comments):
    commentBody = "I am sorry, I was unable to successfully process your data.\n"
    commentBody += "Please amend the following issues: \n"

    for c in range(len(comments)-1):
        commentBody += "* " + comments[c] + "\n"
    commentBody += "* " + comments[-1]

    issue.create_comment(commentBody)

def AddTeamChecklist():
    checklistBody = "Your submission looks good! \n"
    checklistBody += "A member of our team will now verify that: \n"
    checklistBody += "[ ] There are no scheduling conflicts"
    checklistBody += "[ ] Everything is in order"
    issue.create_comment(checklistBody)

def ParseIssue():
    b = issue.body

    #with open("exampleissue.txt", "r") as f:
    #   b = f.read()

    # Validate the date: must be sufficiently far into the future
    date = b.split("Time slot (at least 14 days ahead)")[1].split()
    day = date[0]
    time = date[1]
    dateValid, dateMsg = CheckDate(day, time)

    # Grab title, abstract and authors, edit the description
    arXivID = b.split("Preprint ID")[1].split()[0]
    arXivValid, preprint = CheckArxiv(arXivID)

    # If we have a valid preprint, we can amend the issue if required
    if( arXivValid ):
        UpdateIssue(b, preprint)

    comments = []
    if not dateValid:
        comments.append(dateMsg)
    if not arXivValid:
        comments.append("Your arXiv preprint ID could not be found.")

    # If there were any problems, comment and return
    if( len(comments) != 0 ):
        AddComments(comments)
        return
    else:
        # Add a checklist for team member to confirm if not already there
        AddTeamChecklist()

        # Check for Zoom link in corresponding YAML
        # AddUserChecklist

if __name__ == "__main__":
    ParseIssue()
