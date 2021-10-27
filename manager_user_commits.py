from collections import Counter

def display_main_commits(repo):
    print("\n### Commits in Main")
    main_commits = repo.get_commits("main")
    namelist = []
    for item in main_commits:
        j = repo.get_commit(item.sha)
        # if j.commit.committer.name != "GitHub":
        namelist.append(j.author.login)
    j = Counter(namelist)
    for key, value in j.items():
        print(key, value)


def plot_commit_frequency(project_start_posix, project_time_now, repo):
    main_commits = repo.get_commits("main")
    commitlist = []
    for item in main_commits:
        j = repo.get_commit(item.sha)
        dp = [j.author.login, j.html_url, j.commit.message.strip("\n"), j.commit.committer.name, j.commit.last_modified]
        commitlist.append(dp)
    commitlist.sort()
    for item in commitlist:
        print(item)


def display_all_commits_all_branches(repo):
    branches = repo.get_branches()
    print("| Author | Commit Msg | Committer Name | Last Modified | Link to Commit |")
    for branch in branches:
        print("### " + branch.name)
        commits = repo.get_commits(branch.name)
        commitlist = []
        for item in commits:
            j = item.commit
            # dp = [j.author.name, j.message.strip("\n"), j.committer.name, j.last_modified, j.html_url]
            dp = "| " + j.author.name + " | " + j.message.strip("\n") + " | " + j.committer.name + " | " + j.last_modified + " | " +  "[Link](" + j.html_url + ") |"
            commitlist.append(dp)
        commitlist.sort()
        for item in commitlist:
            print(item)
