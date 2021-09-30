
def display_group_members(repo):
    print("\n### GROUP MEMBERS")
    users = repo.get_contributors()
    for user in users:
        peeps = str(user) + " " + str(user.last_modified) + " " + str(user.name)
        print(peeps)

