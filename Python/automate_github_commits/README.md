# Github Commits Automation with Python 3 🐍

The python script [automate_commits.py](automate_commits.py) will automatically make commits to a git repository.

<br>

The script will create a file called **commits.txt** if doesn't exists; adds the current time to that file when change is made and pushes to the remote repository. The script will then sleeps for 24 hours and tries again 365 times.

### Setup and Usage: 
- Install [GitPython](https://gitpython.readthedocs.io/en/stable/intro.html#installing-gitpython)
    * `pip install GitPython`
- Run script
```bash
# without commandline argument, current working directory will be used
python3 automate_commits.py

# pass in absolute path for git directory
python3 automate_commits.py /PATH/TO/DIRECTORY
```



### Resources: 
Other resources and git clients to interact with a git repository
- [GitPython Tutorial](https://www.devdungeon.com/content/working-git-repositories-python)
- [Gittle git client](https://github.com/FriendCode/gittle)
- [pygit2 git client](https://www.pygit2.org/)