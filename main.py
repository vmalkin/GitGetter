# This script is designed to use the Github api to extract information about a series of repos,
# their contributors and their work. Data will be displayed graphically.
from pprint import pprint

import github.GithubException
from github import Github
from collections import Counter
import time
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
    "BIT-Studio-2/project-21s2-buddy-on-the-beach",
    "BIT-Studio-2/project-21s2-ark-tech",
    "BIT-Studio-2/project-21s2-beach-boys",
    "BIT-Studio-2/project-21s2-beach-buddy",
    "BIT-Studio-2/project-21s2-jackal",
    "BIT-Studio-2/project-21s2-paw-patrol",
    "BIT-Studio-2/project-21s2-sea-dogs",
    "BIT-Studio-2/project-21s2-walkeez"
    ]

def get_index(start_posix, value_posix):
    # returns an integer value for an index, in one hour blocks
    index = int((value_posix - start_posix) / 3600)
    return index


if __name__ == '__main__':
    project_start = "2021-09-13"
    project_start_posix = mgr_time.utc2posix(project_start, '%Y-%m-%d')
    project_time_now = int(time.time())



    print("Convert Markdown to HTML: https://dillinger.io/")

    print("## Quick link to repos:")
    for name in repo_names:
        repo_name = "http://github.com/" + name
        linkname = "[" + name + "]"
        linkurl = "(" + repo_name + ")"
        print("## " + linkname + linkurl)
        repo = g.get_repo(name)

        # rate_limit = Github.get_rate_limit(repo)
        # rl_search = rate_limit.search
        # print(mgr_time.posix2utc(rl_search, '%Y-%m-%d %H:%M'))

        mgr_group.display_group_members(repo, repo_name)
        mgr_commits.display_main_commits(repo)

        print("## Detailed Repo Stats")
        # mgr_commits.plot_commit_frequency(project_start_posix, project_time_now, repo)
        print(" --- ")
        mgr_commits.display_all_commits_all_branches(repo)
        print("---")


print("END")



    # time_end = time()
    # print("Finished!")
    # project_elapsed_days = round((project_time_now - project_start) / 86400, 1)
    # print("Project has been running for " + project_elapsed_days + " days")





