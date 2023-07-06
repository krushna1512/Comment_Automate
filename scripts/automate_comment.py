from datetime import datetime, timedelta
import os
from github import Github

def comment_on_inactive_issues():
    github_token = os.environ.get('GITHUB_TOKEN')
    repository = os.environ.get('GITHUB_REPOSITORY')
    owner, repo = repository.split('/')

    g = Github(github_token)
    repo = g.get_repo(repository)
    issues = repo.get_issues(state=['open', 'inprocess'])

    current_date = datetime.now() - timedelta(minutes=4)

    for issue in issues:
        comments = issue.get_comments()
        last_comment = None

        for comment in comments:
            last_comment = comment

        if not last_comment or last_comment.created_at < current_date:
            comment = "Hello! It seems no activity has been recorded on this issue for the past 4 days. "
            issue.create_comment(comment)

comment_on_inactive_issues()
