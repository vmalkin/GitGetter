def posix_to_nzst(timestring):
    # Timestring is GMT
    timeformat = '%a, %d %b %Y %H:%M:%S GMT'


def gmt_to_posix(timestring):
    # Timestring is GMT
    timeformat = '%a, %d %b %Y %H:%M:%S GMT'

def posix2utc(posixtime, timeformat):
    # '%Y-%m-%d %H:%M'
    utctime = datetime.datetime.utcfromtimestamp(int(posixtime)).strftime(timeformat)
    return utctime