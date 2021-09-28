# This script is designed to use the Github api to extract information about a series of repos,
# their contributors and their work. Data will be displayed graphically.
import github.GithubException
from github import Github
from collections import Counter
from time import time
from plotly import graph_objects as go



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


def display_commits_all_branches(repo):
    print("---")
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

                tally.append(author)

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

    print("### TOTAL COMMITS BY CONTRIBUTORS")
    print(Counter(tally))


def display_member_commit_times(repo):
    print("---")
    print("\n### COMMIT FREQUENCY")
    tally = []

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

                tally.append(author)

                linkname = "[" + author + "]"
                linkurl = "(" + commit.html_url + ")"
                url = linkname + linkurl
                comms = [str(header_keys['last-modified']), url, str(commit.author)]
        except github.GithubException:
            print("Error: no commits")




def convertGMTtoNZ(timestring):
    # Timestring is GMT
    timeformat = '%a, %d %b %Y %H:%M:%S GMT'


if __name__ == '__main__':
    time_start = time()
    # with open("Studio_2.txt", "w") as s:
    print("Convert Markdown to HTML: https://dillinger.io/")
    for name in repo_names:
        repo_name = "http://github.com/" + name
        linkname = "[" + name + "]"
        linkurl = "(" + repo_name + ")"

        print("## " + linkname + linkurl)
        repo = g.get_repo(name)

        display_group_members(repo)
        display_commits_all_branches(repo)
        # display_member_commit_times(repo)


        # print("OPEN ISSUES\n")
        # open_issues = repo.get_issues(state="open")
        # for issue in open_issues:
        #     issues = str(issue.id) + " " + str(issue.state) + " " + str(issue.assignees)
        #     print(issues + "\n")




        # print("PULL REQUESTS\n")
        # pulls = repo.get_pulls()
        # for p in pulls:
        #     print(p.state)
        #     for c in p.get_review_comments():
        #         print(c + "\n")


        print("==================" + "END" + "==================\n\n")
    # s.close()
    time_end = time()
    print("Finished!")
    time_elapsed = round((time_end - time_start) / 60, 2)
    print("Elapsed time: " + str(time_elapsed) + " minutes")





