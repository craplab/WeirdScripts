'''
TODO: https://www.devdungeon.com/content/working-git-repositories-python

run below command in a git directory
   python automate_commits.py
'''
from datetime import datetime
import git
import os
import sys

BRANCH = "master"
SLEEP_DURATION_MIN = 24 * 60
DIRECTORY_PATH = sys.argv[1] if sys.argv[1] != None else os.getcwd()
NUM_DAYS_IN_YEAR = 365
FILE_NAME = 'commits.txt'

# FIXME
# create repo object. setup remote
def setup_git_repo(path: str):
    pass

# TODO implement update_file()
# create file if not exists. append date at the end
def update_file(path: str):
    pass

# TODO
def git_add_commit_push():
    pass

# go to dir
repo = git.Repo(DIRECTORY_PATH)
repo.git.checkout(f'origin/{BRANCH}', b=BRANCH)
TIME = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open(f"{DIRECTORY_PATH}/{FILE_NAME}","a+") as f:
    f.write(TIME)


repo.git.add(FILE_NAME)

# git commit 
repo.git.commit( m=f"Automated Commit Time: {TIME}" )

# git push
# repo.git.


print(os.getcwd())