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

# class DataPoint():
#     def __init__(self, datetime):
#         self.datetime = datetime
#         self.commit = False
#
# class Student():
#     def __init__(self, name, binlist):
#         self.name = name
#         self.commit_frequency = binlist
#
#     def plot_commits(self):
#         pass

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
    "BIT-Studio-2/project-21s2-paw-patrol",
    # "BIT-Studio-2/project-21s2-sea-dogs",
    # "BIT-Studio-2/project-21s2-walkeez"
    ]

def get_index(starttime, finishtime, value):
    t = None
    binsize = 60 * 60
    if value <= finishtime:
        t = value - starttime
        t = int(t / binsize)
    return t

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

        # mgr_group.display_group_members(repo, repo_name)
        # mgr_commits.display_user_commits_summary(repo)
        # print(" --- ")

        # mgr_commits.display_branch_commits_summary(repo)
        # mgr_commits.display_all_commits_all_branches(repo)
        # print("---")

    

    branches = repo.get_branches()
    for branch in branches:
        commits = repo.get_commits(branch.name)
        for c in commits:
            header_keys = c.raw_headers
            if c.author is None:
                author = "INVALID CONTRIBUTOR"
            else:
                author = c.author.login

            commit_date = c.raw_data["commit"]["author"]["date"]
            posix_date = mgr_time.utc2posix(commit_date, "%Y-%m-%dT%H:%M:%SZ")
            print(author + "," + str(posix_date))



    print("END")



    # time_end = time()
    # print("Finished!")
    # project_elapsed_days = round((project_time_now - project_start) / 86400, 1)
    # print("Project has been running for " + project_elapsed_days + " days")





