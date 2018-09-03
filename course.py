import datetime
import const

class Times:
    def __init__(self, selDay, startHour, startMinute, endHour, endMinute):
        self.startTime = datetime.datetime(const.YEAR, const.OCTOBER, selDay, startHour, startMinute)
        self.endTime = datetime.datetime(const.YEAR, const.OCTOBER, selDay, endHour, endMinute)
        




class course:
    def __init__(self, crcCode, bothSem, selDay, startHour, startMinute, endHour, endMinute):
        self.crcCode = crcCode
        self.bothSem = bothSem
        self.Times = []
        self.Times.append(Times(selDay, startHour, startMinute, endHour, endMinute))
    def addTime(self, selDay, startHour, startMinute, endHour, endMinute):
        self.Times.append(Times(selDay, startHour, startMinute, endHour, endMinute))
    def removeTime(self, selDay, startHour, startMinute, endHour, endMinute):
        temp = Times(selDay, startHour, startMinute, endHour, endMinute)
        self.Times.remove(temp)
    def printTimes(self):
        for i in self.Times:
            print(i.startTime, "  --  ", i.endTime)
    def getTimes(self):
        return self.Times

    
    

