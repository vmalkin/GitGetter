def get_index(starttime, finishtime, value):
    t = None
    binsize = 60 * 60
    if value <= finishtime:
        t = value - starttime
        t = int(t / binsize)
    return t

print(get_index(0, 1000000, 1000000))