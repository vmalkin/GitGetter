# This script is designed to use the Github api to extract information about a series of repos,
# their contributors and their work. Data will be displayed graphically.
import github.GithubException
from github import Github
from time import sleep


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
    # with open("Studio_2.txt", "w") as s:
    for name in repo_names:
        repo_name = "http://github.com/" + name
        linkname = "[" + name + "]"
        linkurl = "(" + repo_name + ")"

        print("##" + linkname + linkurl + "\n")
        repo = g.get_repo(name)

        # print("OPEN ISSUES\n")
        # open_issues = repo.get_issues(state="open")
        # for issue in open_issues:
        #     issues = str(issue.id) + " " + str(issue.state) + " " + str(issue.assignees)
        #     print(issues + "\n")
        print("###GROUP MEMBERS\n")
        users = repo.get_contributors()
        for user in users:
            peeps = str(user) + " " +  str(user.last_modified) + " " +  str(user.name)
            print(peeps)

        c = []
        print("###COMMITS\n")
        try:
            commits = repo.get_commits()
            for commit in commits:
                header_keys = commit.raw_headers
                # print(headerkeys)
                linkname = "[" + str(commit.author) + "]"
                linkurl = "(" + commit.html_url + ")"
                url = linkname + linkurl
                comms = [str(header_keys['last-modified']),  url, str(commit.author)]
                c.append(comms)
        except github.GithubException:
            print("Error: no commits")

        # sort on student login
        c.sort(key=lambda c: c[2])
        for item in c:
            print(item[0], item[1], item[2])

        # print("PULL REQUESTS\n")
        # pulls = repo.get_pulls()
        # for p in pulls:
        #     print(p.state)
        #     for c in p.get_review_comments():
        #         print(c + "\n")


        print("==================" + "END" + "==================\n\n")
    # s.close()
    sleep(2)

    print("Finished!")





