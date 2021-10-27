
def display_group_members(repo, repo_link):
    print("\n### GROUP MEMBERS")
    users = repo.get_contributors()
    print("| Github Login | Account Name | User Commits |")
    print("| --- | --- | --- |")
    for user in users:
        if user.name is None:
            username = "No name in github account"
        else:
            username = user.name

        commits_url = repo_link + "/commits?author=" + user.login

        peeps = "| " + str(user.login) + " | " + str(username) + " | " + "[Link](" + commits_url + ") |"
        print(peeps)

