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