# This script is designed to use the Github api to extract information about a series of repos,
# their contributors and their work. Data will be displayed graphically.
import github.GithubException
from github import Github
from collections import Counter
from time import time
import plotly.graph_objects as go
import datetime


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

def display_group_members(repo):
    print("\n### GROUP MEMBERS")
    users = repo.get_contributors()
    for user in users:
        peeps = str(user) + " " + str(user.last_modified) + " " + str(user.name)
        print(peeps)


def display_summary_commits(repo):
    tally = []
    # First get all branches for the repo
    branches = repo.get_branches()
    for branch in branches:
        commits = repo.get_commits(branch.name)
        try:
            for commit in commits:
                if commit.author is None:
                    author = "INVALID CONTRIBUTOR"
                else:
                    author = commit.author.login

                tally.append(author)
        except github.GithubException:
            print("Error: no commits")

    print("### TOTAL COMMITS BY CONTRIBUTORS ACROSS ALL BRANCHES")

    commit_summary = Counter(tally)
    print("| Group Member | No of Commits |")
    print("| --- | --- |")
    for keys, values in commit_summary.items():
        print("| " + keys + " | " + str(values) + " |")


def display_commits_all_branches(repo):
    print("\n### COMMITS ALL BRANCHES")
    tally = []

    # First get all branches for the repo
    branches = repo.get_branches()
    for branch in branches:
        print("\n### BRANCH: " + branch.name)
        commits = repo.get_commits(branch.name)
        c = []
        try:
            for commit in commits:
                header_keys = commit.raw_headers
                # print(headerkeys)
                if commit.author is None:
                    author = "INVALID CONTRIBUTOR"
                else:
                    author = commit.author.login

                linkname = "[" + author + "]"
                linkurl = "(" + commit.html_url + ")"
                url = linkname + linkurl
                comms = [str(header_keys['last-modified']), url, str(commit.author)]
                c.append(comms)
        except github.GithubException:
            print("Error: no commits")

        sorted_commits = sorted(c, key=lambda c: (c[2], c[0]))
        for cm in sorted_commits:
            print(cm)


def display_member_commit_times(repo):
    print("\n### COMMIT FREQUENCY")
    times = []
    coder = []

    # First get all branches for the repo
    branches = repo.get_branches()
    for branch in branches:
        print("\n### BRANCH: " + branch.name)
        commits = repo.get_commits(branch.name)
        try:
            for commit in commits:
                header_keys = commit.raw_headers
                # print(headerkeys)
                if commit.author is None:
                    author = "INVALID CONTRIBUTOR"
                else:
                    author = commit.author.login
                times.append(str(header_keys['last-modified']))
                coder.append(author)
        except github.GithubException:
            print("Error: no commits")
    return [times, coder]


def posix_to_nzst(timestring):
    # Timestring is GMT
    timeformat = '%a, %d %b %Y %H:%M:%S GMT'


def gmt_to_posix(timestring):
    # Timestring is GMT
    timeformat = '%a, %d %b %Y %H:%M:%S GMT'

def posix2utc(posixtime, timeformat):
    # '%Y-%m-%d %H:%M'
    utctime = datetime.datetime.utcfromtimestamp(int(posixtime)).strftime(timeformat)
    return utctime


def plot_frequency(team_name, times, names):
    n = Counter(names).keys()
    coders = []
    for item in names:
        coders.append(item)

    times.reverse()
    names.reverse()

    fig = go.Figure(go.Bar(x=times, y=names))
    fig.update_layout(barmode='group')
    fig.show()


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





