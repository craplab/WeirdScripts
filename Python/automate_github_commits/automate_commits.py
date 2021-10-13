from datetime import datetime
import git
import os
import sys
import time

BRANCH = "master"
REMOTE = "origin"
SLEEP_DURATION_SEC = 24 * 60 * 60
REPO_PATH = sys.argv[1] if sys.argv[1] != None else os.getcwd()
NUM_DAYS_IN_YEAR = 365
AUTO_UPDATE_FILENAME = 'commits.txt'
TIME = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def setup_git_repo(path: str):
    repo = git.Repo(path)
    repo.git.checkout(BRANCH)
    return repo

def update_file(path: str):
    with open(f"{REPO_PATH}/{AUTO_UPDATE_FILENAME}","a+") as f:
        f.write(f"{TIME}\n")

def git_add_commit_push(repo):
    repo.index.add([AUTO_UPDATE_FILENAME])
    repo.index.commit(f'Commit Time: {TIME}')

    repo.remotes.origin.pull()
    repo.remotes.origin.push()

if __name__ == "__main__":
    mrepo = setup_git_repo(REPO_PATH)
    for i in range(NUM_DAYS_IN_YEAR):
        TIME = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(TIME)
        update_file(REPO_PATH)
        git_add_commit_push(mrepo)
        time.sleep(SLEEP_DURATION_SEC)
