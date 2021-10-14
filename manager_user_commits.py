from collections import Counter
from plotly import graph_objects as go
import github

def display_user_commits_summary(repo):
    # First get all branches for the repo
    branches = repo.get_branches()
    tally = []
    for branch in branches:
        print("### Commits detail for ", branch.name )
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

    commit_summary = Counter(tally)
    print("| Group Member | TOTAL Commits |")
    print("| --- | --- |")
    for keys, values in commit_summary.items():
        print("| " + keys + " | " + str(values) + " |")


def display_branch_commits_summary(repo):
    # First get all branches for the repo
    branches = repo.get_branches()

    for branch in branches:
        tally = []
        print("### Summary of branch: " + branch.name)
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

        commit_summary = Counter(tally)
        print("| Group Member | No of Commits |")
        print("| --- | --- |")
        for keys, values in commit_summary.items():
            print("| " + keys + " | " + str(values) + " |")


def display_all_commits_all_branches(repo):
    branches = repo.get_branches()
    for branch in branches:
        print("\n### BRANCH: " + branch.name)
        commits = repo.get_commits(branch.name)
        print("| Author | Date (UTC) | Link to commit |" )
        print("| --- | --- | --- |")
        for c in commits:
            header_keys = c.raw_headers
            if c.author is None:
                author = "INVALID CONTRIBUTOR"
            else:
                author = c.author.login
            # print(c.raw_data["commit"])
            commit_message = c.raw_data["commit"]["message"]
            commit_url = c.html_url
            commit_date = c.raw_data["commit"]["author"]["date"]
            link = "[" + commit_message + "](" + commit_url + ")"
            print("| " + author + " | " + commit_date +" | " + link + " |")



def plot_commit_frequency(team_name, times, names):
    n = Counter(names).keys()
    coders = []
    for item in names:
        coders.append(item)

    times.reverse()
    names.reverse()

    fig = go.Figure(go.Bar(x=times, y=names))
    fig.update_layout(barmode='group')
    fig.show()