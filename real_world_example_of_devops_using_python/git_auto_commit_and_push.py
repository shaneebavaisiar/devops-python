# Git Auto Commit and Push Script
import subprocess  # For running git commands from Python


def git_commit_push(message):
    # Add all changed files to staging
    subprocess.run(["git", "add", "."], check=True)

    # Commit the changes with the provided message
    subprocess.run(["git", "commit", "-m", message], check=True)

    # Push the commit to the remote repository
    subprocess.run(["git", "push","origin","feature"], check=True)

    print("Changes pushed to remote repository.")


git_commit_push("Auto commit from Python script")  # Customize commit message