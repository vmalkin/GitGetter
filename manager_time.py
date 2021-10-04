from datetime import datetime
import calendar

def utc2posix(utctime, timeformat):
    # Timestring is GMT
    # timeformat = '%a, %d %b %Y %H:%M:%S GMT'
    date_obj = datetime.strptime(utctime, timeformat)
    posixtime = round(calendar.timegm(date_obj.timetuple()), 0)
    return posixtime


def posix2utc(posixtime, timeformat):
    # '%Y-%m-%d %H:%M'
    utctime = datetime.utcfromtimestamp(int(posixtime)).strftime(timeformat)
    return utctime