import os
from github import Github
from dotenv import load_dotenv

load_dotenv()
g = Github(os.getenv("GITHUB_ACCESS_TOKEN"))

repo = g.get_repo("MLH-Fellowship/portfolio-template")
issues = repo.get_issues(state="open", labels=["template"])

pod_repos = ["MLH-Fellowship/pod-4.1.0-portfolio", "MLH-Fellowship/pod-4.1.1-portfolio", "MLH-Fellowship/pod-4.1.2-portfolio"]


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
