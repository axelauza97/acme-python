from utilities import getHourTime
from workday import getWeekDays,getWeekendDays


class Company(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Company, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.weekDays=getWeekDays()
        self.weekendDays=getWeekendDays()
        
    def payEmployee(self,Person,schedule):
        for day, time in schedule.items():   
            lowerTime=time.split('-')[0]
            upperTime=time.split('-')[1]
            workTimeLower = getHourTime(lowerTime)
            workTimeUpper = getHourTime(upperTime)
            if day in ["MO","TU","WE","TH","FR"]:
                self.calculateWorkHours(Person,self.weekDays,workTimeLower,workTimeUpper)
            else:
                self.calculateWorkHours(Person,self.weekendDays,workTimeLower,workTimeUpper)
        return Person.getPayment()
                  
    def calculateWorkHours(self,Person,dictWeek,workTimeLower,workTimeUpper):
        for interval,workday in dictWeek.items():
            lower=workday.getHourTimeLower()
            upper=workday.getHourTimeUpper()
            hourPay=workday.getPayment()
            if(workTimeLower>=lower) and(workTimeUpper<=upper):
                payment=(workTimeUpper-workTimeLower).seconds//3600*hourPay
                Person.salary(payment)
                break
            elif (workTimeLower>lower) and (workTimeLower<upper) and (workTimeUpper>upper):
                payment=(upper-workTimeLower).seconds//3600*hourPay
                Person.salary(payment)
                break
            elif (workTimeLower<lower) and (lower>workTimeUpper) and (upper>workTimeUpper):
                payment=(workTimeUpper-lower).seconds//3600*hourPay
                Person.salary(payment)
                break