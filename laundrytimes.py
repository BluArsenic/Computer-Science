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
import matplotlib.pyplot as plt

def whichDay(): # determines which day of the week it is
	global day
	day = r.randint(0,6) # 1 being Sunday, 7 being Saturday
	if day is 0:
		day = 'Sunday'
	elif day is 1:
		day = 'Monday'
	elif day is 2:
		day = 'Tuesday'
	elif day is 3:
		day = 'Wednesday'
	elif day is 4:
		day = 'Thursday'
	elif day is 5:
		day = 'Friday'
	else:
		day = 'Saturday'

def whichTime(): # determines which time of day it is
	global time
	time = r.randint(0,3) # 1 is morning, 2 afternoon, 3 evening, 4 night
	if time is 0:
		time = 'Morning'
	elif time is 1:
		time = 'Afternoon'
	elif time is 2:
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

def calculateNoER():
	washed = 0 # how many students have washed their clothes
	dataMon = [] # data of monday washes
	dataTues = [] # data of tuesday washes
	dataWed = [] # data of wednesday washes
	dataThurs = [] # thursday
	dataFri = [] # friday
	dataSat = [] # saturday
	dataSun = [] # sunday
	colors = r.choice(['red','orange','yellow','green','blue','purple','magenta','cyan'])
	days = ["Mon.","Tues.","Wed.","Thurs.","Fri.","Sat.","Sun."]
	daysResults = []
	# for x in range(weeks): # if you want to implement weeks
	students = 40 # students in the dorm; 40 for reference (Tenney population)
	for washed in range(students):
		whichDay() # gets value for day
		whichTime() # gets vaule for time of day
		ER() # gets value of E&R use
		if er == 'No' or er == 'Sometimes':
			if day == 'Monday':
				dataMon.append(time)
			elif day == 'Tuesday':
				dataTues.append(time)
			elif day == 'Wednesday':
				dataWed.append(time)
			elif day == 'Thursday':
				dataThurs.append(time)
			elif day == 'Friday':
				dataFri.append(time)
			elif day == 'Saturday':
				dataSat.append(time)
			else:
				dataSun.append(time)
		washed += 1
	daysResults.append(len(dataMon))
	daysResults.append(len(dataTues))
	daysResults.append(len(dataWed))
	daysResults.append(len(dataThurs))
	daysResults.append(len(dataFri))
	daysResults.append(len(dataSat))
	daysResults.append(len(dataSun))
	plt.bar(days, daysResults, .8, color = colors)
	plt.title("Days Students W/O E&R Wash Their Clothes in Tenney")
	plt.savefig("laundry1.png")
	plt.show()
	return daysResults,len(dataMon),len(dataTues),len(dataWed),len(dataThurs),len(dataFri),len(dataSat),len(dataSun)
	
def calculateER():
	washed = 0
	dataMon = []
	dataTues = []
	dataWed = []
	dataThurs = []
	dataFri = []
	dataSat = []
	dataSun = []
	dataNONE = []
	colors = r.choice(['red','orange','yellow','green','blue','purple','magenta','cyan'])
	days = ["Mon.","Tues.","Wed.","Thurs.","Fri.","Sat.","Sun.","None"]
	daysResults = []
	# for x in range(weeks):
	students = 40
	for washed in range(students):
		whichDay()
		whichTime()
		ER()
		if er == 'Yes':
			dataNONE.append("None")
		elif day == 'Monday':
			dataMon.append(time)
		elif day == 'Tuesday':
			dataTues.append(time)
		elif day == 'Wednesday':
			dataWed.append(time)
		elif day == 'Thursday':
			dataThurs.append(time)
		elif day == 'Friday':
			dataFri.append(time)
		elif day == 'Saturday':
			dataSat.append(time)
		else:
			dataSun.append(time)
		washed += 1
	daysResults.append(len(dataMon))
	daysResults.append(len(dataTues))
	daysResults.append(len(dataWed))
	daysResults.append(len(dataThurs))
	daysResults.append(len(dataFri))
	daysResults.append(len(dataSat))
	daysResults.append(len(dataSun))
	daysResults.append(len(dataNONE))
	plt.bar(days, daysResults, .8, color = colors)
	plt.title("Days Students With E&R Wash Their Clothes in Tenney")
	plt.savefig("laundry2.png")
	plt.show()
	return daysResults

# weeks = 10
print(calculateNoER())
print(calculateER())

# 1) Go to Squire for extra help
#	 - Figure out how to implement dorms √
#	 - Figure out how to graph (kinda) √
#	 - Work on making every dorm a different number of students... but after you're done with the assignment √