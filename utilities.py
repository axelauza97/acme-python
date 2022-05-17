import datetime

def getHourTime(time):
    return datetime.timedelta(hours=int(time.split(":")[0]), minutes=int(time.split(":")[1]))