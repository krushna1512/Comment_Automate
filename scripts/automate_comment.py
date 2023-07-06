from datetime import datetime, timedelta
import os
from github import Github

def comment_on_inactive_issues():
    # Retrieve the GitHub token and repository from environment variables
    github_token = os.environ.get('GITHUB_TOKEN')
    repository = os.environ.get('GITHUB_REPOSITORY')
    
    # Split the repository string to get owner and repo names
    owner, repo = repository.split('/')

    # Create a GitHub instance using the token
    g = Github(github_token)
    
    # Get the repository object
    repo = g.get_repo(repository)
    
    # Get all open issues in the repository
    issues = repo.get_issues(state='open')

    # Calculate the date and time 4 minutes ago
    current_date = datetime.now() - timedelta(minutes=4)

    # Iterate over each issue
    for issue in issues:
        # Get all comments for the current issue
        comments = issue.get_comments()
        
        # Variable to store the last comment
        last_comment = None

        # Find the most recent comment
        for comment in comments:
            last_comment = comment

        # Check if the last comment is missing or older than 4 minutes
        if not last_comment or last_comment.created_at < current_date:
            # Create a comment mentioning the owner
            comment = "Hello @{owner}! It seems no activity has been recorded on this issue for the past 4 days. Is there anything I can assist you with?".format(owner=owner)
            
            # Post the comment on the issue
            issue.create_comment(comment)

# Call the function to execute the code
comment_on_inactive_issues()
