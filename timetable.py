import const


class TimeTable:
    def __init__(self):
        #The elements are the days from Monday to Sunday (indexed as (const.{day}-1)
        #The elements contain half an hour intervals of the entire day 
        self.TimeTable = [[], [], [], [], [], [], []]
        for day in self.TimeTable:
            for interval in range(0, 48):
                day.append(" ")

    #adds courses assuming that the course ends on the same day
    #conflict management not done yet
    def addCourse(self, selCourse):
        day = (selCourse.getTimes())[0].startTime.day
        for index in self.getTTindices(selCourse):
            (self.TimeTable[day-1])[index] = selCourse.crcCode
            
    #returns the range of indices(half an hour intervals) in which the course take place
    def getTTindices(self, selCourse):
        hourStart = (selCourse.getTimes())[0].startTime.hour
        minutesStart = (selCourse.getTimes())[0].startTime.minute
        indexStart = (hourStart*2)+ (1 if (minutesStart==30) else 0)
        hourStop = (selCourse.getTimes())[0].endTime.hour
        minutesStop = (selCourse.getTimes())[0].endTime.minute
        indexStop = (hourStop*2)+ (1 if (minutesStop==30) else 0)
        return range(indexStart, indexStop)
    def printTT(self):
        print(self.TimeTable)
            

class Year:
    def __init__(self):
        self.Fall = TimeTable()
        self.Winter = TimeTable()
    def addCourse(self, selCourse):
        if(selCourse.bothSem == "Fall"):
            self.Fall.addCourse(selCourse)
        elif(selCourse.bothSem == "Winter"):
            self.Winter.addCourse(selCourse)
        else:
            if(selCourse.crcCode[-1:] == "F"):
                self.Fall.addCourse(selCourse)
            elif(selCourse.crcCode[-1:] == "S"):
                self.Winter.addCourse(selCourse)
            elif(selCourse.crcCode[-1:] == "Y"):
                self.Winter.addCourse(selCourse)
                self.Fall.addCourse(selCourse)
            else:
                return -1

                
