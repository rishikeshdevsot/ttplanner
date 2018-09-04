from course import course
from timetable import Year
import const

#The days go from 1 to 7 instead of 0 to 6, for example const.MONDAY is 1 instead of 0

#first argument is the course code+ F/S/Y, (F- Fall, S-winter,  Y-year) 
#second argument is if it is available in both semesters or fall or winter or year

#Difference between both semesters and year is that for both semesters the course will have different timings
#and you can only choose the course either in fall or winter, it is just offered in both semesters
myYear = Year()

course1 = course("CSC100F", "Both", const.MONDAY, 9, 30, 10, 0)
course2 = course("MAT100S", "Both", const.TUESDAY, 9, 0, 10, 0)

myYear.addCourse(course1)
myYear.addCourse(course2)

myYear.Winter.printTT()








