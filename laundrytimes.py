'''
What days of the week can you wash your laundry?
	-All days
What times can you wash them?
	-Morning (6 AM-12 PM)
	-Afternoon (12 PM-6 PM)
	-Evening (6 PM-9 PM)
	-Night/Early Morning (9 PM-6 AM)
Do you have the E&R Laundry Service?
	-Yes
	-No
	-Yes, but I also wash my own clothes
'''

import random as r
import collections as c

def whichDay():
    day = r.randint(1,7) # 1 being Sunday, 7 being Saturday
    if day is 1:
        day = 'Sunday'
    elif day is 2:
        day = 'Monday'
    elif day is 3:
        day = 'Tuesday'
    elif day is 4:
        day = 'Wednesday'
    elif day is 5:
        day = 'Thursday'
    elif day is 6:
        day = 'Friday'
    else:
        day = 'Saturday'

def whichTime():
    time = r.randint(1,4) # 1 is morning, 2 afternoon, 3 evening, 4 night
    if time is 1:
        time = 'Morning'
    elif time is 2:
        time = 'Afternoon'
    elif time is 3:
        time = 'Evening'
    else:
        time = 'Night/Early Morning'

def ER():
    global er
    er = r.randint(0,1) # 0 is no, 1 is yes
    if er is 0:
        er = 'No'
    else:
        er = 'Yes'

def calculate():
    students = 100
    times = 0
    data = []
    while times < students:
        whichDay()
        whichTime()
        ER()
        if er == 'Yes':
            pass
        elif er == 'No':
            data.append(day+time)
        times+1
    return data
    return c.Couner(data)

print(calculate())