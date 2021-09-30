# This script is designed to use the Github api to extract information about a series of repos,
# their contributors and their work. Data will be displayed graphically.
import github.GithubException
from github import Github
from collections import Counter
from time import time
import plotly.graph_objects as go
import datetime
import manager_group as mgr_group
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





if __name__ == '__main__':
    # project_start = "2020-09-13"
    # project_start_posix = posix2utc(project_start, '%Y-%m-%d')
    # project_time_now = time()

    print("Convert Markdown to HTML: https://dillinger.io/")
    for name in repo_names:
        repo_name = "http://github.com/" + name
        linkname = "[" + name + "]"
        linkurl = "(" + repo_name + ")"

        print("## " + linkname + linkurl)
        repo = g.get_repo(name)

        display_group_members(repo)
        display_summary_commits(repo)

        display_commits_all_branches(repo)
        # plotdata = display_member_commit_times(repo)
        # plot_frequency(name, plotdata[0], plotdata[1])
        print("END")
        print("---")


    # time_end = time()
    # print("Finished!")
    # project_elapsed_days = round((project_time_now - project_start) / 86400, 1)
    # print("Project has been running for " + project_elapsed_days + " days")





