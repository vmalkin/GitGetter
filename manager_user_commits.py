from collections import Counter

def display_main_commits(repo):
    main_commits = repo.get_commits("main")
    namelist = []
    commitlist = []
    for item in main_commits:
        j = repo.get_commit(item.sha)
        # if j.commit.committer.name != "GitHub":
        namelist.append(j.author.login)
        dp = [j.author.login, j.html_url, j.commit.message.strip("\n"), j.commit.committer.name, j.commit.last_modified]
        commitlist.append(dp)
    print(Counter(namelist))
    commitlist.sort()
    for item in commitlist:
        print(item)
