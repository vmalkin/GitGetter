# This script is designed to use the Github api to extract information about a series of repos,
# their contributors and their work. Data will be displayed graphically.
import github.GithubException
from github import Github
from pprint import pprint



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

def displayGroupMembers(repo):
    print("\n###GROUP MEMBERS")
    users = repo.get_contributors()
    for user in users:
        peeps = str(user) + " " + str(user.last_modified) + " " + str(user.name) + "\n"
        print(peeps)


def displayMemberCommitsAllBranches(repo):

    print("\n###COMMITS ALL BRANCHES")

    # First get all branches for the repo
    branches = repo.get_branches()
    for branch in branches:
        print("\n###BRANCH: " + branch.name)
        commits = repo.get_commits(branch.name)
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
                print(comms)
        except github.GithubException:
            print("Error: no commits")


def convertGMTtoNZ(timestring):
    # Timestring is GMT
    timeformat = '%a, %d %b %Y %H:%M:%S GMT'


if __name__ == '__main__':
    # with open("Studio_2.txt", "w") as s:
    print("Convert Markdown to HTML: https://dillinger.io/")
    for name in repo_names:
        repo_name = "http://github.com/" + name
        linkname = "[" + name + "]"
        linkurl = "(" + repo_name + ")"

        print("##" + linkname + linkurl)
        repo = g.get_repo(name)

        displayGroupMembers(repo)
        displayMemberCommitsAllBranches(repo)


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

    print("Finished!")





