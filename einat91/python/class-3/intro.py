#import my_module as mm
from my_module import find_index, test
import Lib.random as random
import math
import Lib.datetime as datetime
import Lib.calendar as calendar
import Lib.os as os

courses = ['History', 'Math', 'Physics', 'CompSci']


#index = mm.find_index(courses, 'Math')
index = find_index(courses, 'Math')
#print(index) 
#print(test)
random_course = random.choice(courses)
rads = math.radians(90)

print(random_course)
print(rads)

today = datetime.date.today()
print(today)
print(calendar.isleap(2017))

#print (os.getcwd()) # Current working directory
#print(os.__file__) # Location of file in file system

import Lib.antigravity


