from course import course
from timetable import Year
import const

#The days go from 1 to 7 instead of 0 to 6, for example const.MONDAY is 1 instead of 0

#first argument is the course code+ L/P/T, (L - lecture, P -practical, T - tutorial) 
#second argument is if it is available in both semesters(or fall or winter)
myYear = Year()

course1 = course("CSC100L", "Both", const.MONDAY, 9, 30, 10, 0)
course2 = course("MAT100L", "Both", const.TUESDAY, 9, 0, 10, 0)

myYear.addCourse(course1)
myYear.addCourse(course2)

myYear.Fall.printTT()







