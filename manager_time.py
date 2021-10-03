from datetime import datetime


def gmt_to_posix(timestring):
    # Timestring is GMT
    timeformat = '%a, %d %b %Y %H:%M:%S GMT'

def utc2posix():
    pass

def posix2utc(posixtime, timeformat):
    # '%Y-%m-%d %H:%M'
    utctime = datetime.utcfromtimestamp(int(posixtime)).strftime(timeformat)
    return utctime