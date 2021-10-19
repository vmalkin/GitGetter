import manager_time as mgr_time


class DataPoint():
    def __init__(self, datetime):
        self.datetime = datetime
        self.commit = False

class Student():
    def __init__(self, name, binlist):
        self.name = name
        self.commit_list = binlist

    def plot_commits(self):
        for i in self.commit_list:
            print(i.datetime, i.commit)


def get_index(starttime, finishtime, value):
    t = None
    binsize = 60 * 60
    if value <= finishtime:
        t = value - starttime
        t = int(t / binsize)
    return t


def wrapper(project_start_posix, project_time_now, repo):
    binlist = []
    for i in range(project_start_posix, project_time_now, (60 * 60)):
        binlist.append(DataPoint(i))

    studentlist = []
    users = repo.get_contributors()
    for user in users:
        if user.login is None:
            username = "No name in github account"
        else:
            studentlist.append(Student(user.login, binlist))

    branches = repo.get_branches()
    for branch in branches:
        commits = repo.get_commits(branch.name)
        for c in commits:
            header_keys = c.raw_headers
            if c.author is None:
                author = "INVALID CONTRIBUTOR"
            else:
                author = c.author.login
                commit_date = c.raw_data["commit"]["author"]["date"]
                posix_date = mgr_time.utc2posix(commit_date, "%Y-%m-%dT%H:%M:%SZ")

                for s in studentlist:
                    if s.name == author:
                        index = get_index(project_start_posix, project_time_now, posix_date)
                        s.commit_list[index].commit = True

    for s in studentlist:
        for data in s.commit_list:
            for item in data:
                print(item)
