from utilities import getHourTime


class WorkDay():
    def __init__(self, payment,lowertime,uppertime):
        self.payment=payment
        self.lowertime=lowertime
        self.uppertime=uppertime

    def _str_(self):
        return (str(self.payment) +" USD from "+ self.lowertime +" to "+ self.uppertime)
    
    def getPayment(self):
        return self.payment

    def getHourTimeLower(self):
        return getHourTime(self.lowertime)
        
    def getHourTimeUpper(self):
        return getHourTime(self.uppertime)

def getWeekDays():
	"""The factory method"""
	days = dict(i1=WorkDay(25,"00:01","09:00"),i2=WorkDay(15,"09:01","18:00"),i3=WorkDay(30,"00:01","09:00"))
	return days

def getWeekendDays():
	"""The factory method"""
	days = dict(i1=WorkDay(30,"00:01","09:00"),i2=WorkDay(20,"09:01","18:00"),i3=WorkDay(25,"18:01","24:00"))
	return days