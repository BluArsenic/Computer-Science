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

def whichDay(): # determines which day of the week it is
	global day
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

def whichTime(): # determines which time of day it is
	global time
	time = r.randint(1,4) # 1 is morning, 2 afternoon, 3 evening, 4 night
	if time is 1:
		time = 'Morning'
	elif time is 2:
		time = 'Afternoon'
	elif time is 3:
		time = 'Evening'
	else:
		time = 'Night/Early Morning'

def ER(): # determines if they use E&R Laundry Service
	global er
	er = r.randint(0,2) # 0 is no, 1 is sometimes, 2 is yes
	if er is 0:
		er = 'No'
	elif er is 1:
		er = 'Sometimes'
	else:
		er = 'Yes'

def calculateNoER(dorms):
	students = 40 # students in the dorm; 40 for reference (Tenney population)
	washed = 0 # how many students have washed their clothes
	dataNoER = [] # data of original wash days and times
	dataDYUER = [] # data Do YOU USE ER; data that holds whether you use E&R or not
	dataWithER = [] # data with day and times as well as if you use E&R
	while washed < students:
		whichDay() # gets value for day
		whichTime() # gets vaule for time of day
		ER() # gets value of E&R use
		if er == 'No' or er == 'Sometimes':
			dataNoER.append("\n"+day+" "+time)
			dataDYUER.append("\n"+er)
			dataWithER.append("\n"+er+" "+day+" "+time)
		washed += 1
	print(len(dataNoER), c.Counter(dataDYUER))
	return dataWithER
	
def calculateER(dorms):
	students = 40
	washed = 0
	dataER = [] # data of all students; who doesn't use, who does use, and who sometimes uses E&R
	dataDYUER = []
	dataWithER = []
	while washed < students:
		whichDay()
		whichTime()
		ER()
		if er == 'Yes':
			dataER.append("\nNONE")
			dataDYUER.append("\n"+er)
			dataWithER.append("\n"+er)
		else:
			dataER.append("\n"+day+" "+time)
			dataDYUER.append("\n"+er)
			dataWithER.append("\n"+er+" "+day+" "+time)
		washed += 1
	print(len(dataER), c.Counter(dataDYUER))
	return dataER

dorm = 10
# print(*calculateNoER(dorm))
print(*calculateER(dorm))

# 1) Figure out how to implement dorms
# 2) Figure out how to graph
# 3) if you remember later write it down