import os
from github import Github
from dotenv import load_dotenv
import time

load_dotenv()
g = Github(os.getenv("GITHUB_ACCESS_TOKEN"))

repo = g.get_repo("MLH-Fellowship/prep-react-template")
issues = repo.get_issues(state="open", labels=["template"])

pod_repos = ["MLH-Fellowship/prep-project-23.MAR.PREP.1", "MLH-Fellowship/prep-project-23.MAR.PREP.2"]


for pod_repo in pod_repos:
    repo_obj = g.get_repo(pod_repo)
    for issue in issues:
        
        labels = list(issue.labels)
        for label in labels:
            if label.name == "template":
                labels.remove(label) 
    
        i = repo_obj.create_issue(
            title=issue.title,
            body=issue.body,
            labels=labels
        )
        print(f"Added {i}")
        time.sleep(15)
