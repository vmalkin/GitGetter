# This script is designed to use the Github api to extract information about a series of repos,
# their contributors and their work. Data will be displayed graphically.
from pprint import pprint

import github.GithubException
from github import Github
from collections import Counter
from time import time
import plotly.graph_objects as go
import datetime
import manager_group as mgr_group
import manager_time
import manager_time as mgr_time
import manager_user_commits as mgr_commits




with open("../git.token") as g:
    for line in g:
        git_token = line.strip()

g = Github(git_token)

repo_names = [
    # "BIT-Studio-2/project-21s2-buddy-on-the-beach",
    # "BIT-Studio-2/project-21s2-ark-tech",
    # "BIT-Studio-2/project-21s2-beach-boys",
    # "BIT-Studio-2/project-21s2-beach-buddy",
    # "BIT-Studio-2/project-21s2-jackal",
    # "BIT-Studio-2/project-21s2-paw-patrol",
    "BIT-Studio-2/project-21s2-sea-dogs",
    # "BIT-Studio-2/project-21s2-walkeez"
    ]

def get_index(start_posix, value_posix):
    # returns an integer value for an index, in one hour blocks
    index = int((value_posix - start_posix) / 3600)
    return index




if __name__ == '__main__':
    project_start = "2021-09-13"
    project_start_posix = mgr_time.utc2posix(project_start, '%Y-%m-%d')
    project_time_now = int(time())

    print("Convert Markdown to HTML: https://dillinger.io/")
    for name in repo_names:
        repo_name = "http://github.com/" + name
        linkname = "[" + name + "]"
        linkurl = "(" + repo_name + ")"

        print("## " + linkname + linkurl)
        repo = g.get_repo(name)
        #
        # mgr_group.display_group_members(repo, repo_name)
        # mgr_commits.display_main_commits(repo)
        # print(" --- ")
        #
        # mgr_commits.display_all_commits_all_branches(repo)
        # print("---")
        date_time_range = []
        for i in range(project_start_posix, project_time_now, 3600):
            utc_time = mgr_time.posix2utc(i, '%Y-%m-%d %H:%M')
            commit = False
            dp = [utc_time, commit]
            date_time_range.append(dp)

        main_commits = repo.get_commits("main")
        users = repo.get_contributors()
        for user in users:
            if user.name is None:
                username = "No name in github account"
                break
            else:
                username = user.name




print("END")



    # time_end = time()
    # print("Finished!")
    # project_elapsed_days = round((project_time_now - project_start) / 86400, 1)
    # print("Project has been running for " + project_elapsed_days + " days")





