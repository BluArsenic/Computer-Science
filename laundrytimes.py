'''
When Mrs. Healey told us about the project, I first thought it would be fun to see how many hours I spend on my phone!
Then I thought, "Well, it won't be that useful because I can just look at my phone."
Next, I thought it would be a cool idea to track how much time it takes on average to do my homework.
I didn't think about that one for long because the next thought I had was the resulting code.
I decided to track, on average, the day that kids wash their clothes the most in Tenney.
I have a function that calculates the days that factors in the kids that use E&R, and one that doesn't.
I dont have the one with E&R activated because it heavily skews the results.
It prints multiple graphs of multiples weeks  of washing, and you can change the number of weeks in the weeks variable to procude more graphs and data.
Hopefully this can be helpful to me in the future!
'''

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
	dataThurs = [] # data of thursday washes
	dataFri = [] # data of friday washes
	dataSat = [] # data of saturday washes
	dataSun = [] # data of sunday washes
	dataWeeks = []
	weeks = 5
	colors = r.choice(['red','orange','yellow','green','blue','purple','magenta','cyan'])
	days = ["Mon.","Tues.","Wed.","Thurs.","Fri.","Sat.","Sun."]
	weekDays = [days for x in range(weeks)]
	daysResults = []
	students = 40 # students in the dorm; 40 for reference (Tenney population)
	for x in range(weeks): # if you want to implement weeks
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
		dataWeeks.append(daysResults)
		daysResults = []
	for x in range(weeks):
		plt.figure(x+1)
		plt.bar(weekDays[x], dataWeeks[x], .8, color = colors)
		plt.title("Days Students W/O E&R Wash Their Clothes in Tenney: Week "+str(x+1))
	plt.show()

print(calculateNoER())

# def calculateER(): # skews the results with the E&R results; if you want to add it back in, you can. That's why I'm leaving it commented.
# 	washed = 0
# 	dataMon = []
# 	dataTues = []
# 	dataWed = []
# 	dataThurs = []
# 	dataFri = []
# 	dataSat = []
# 	dataSun = []
# 	dataNONE = []
# 	colors = r.choice(['red','orange','yellow','green','blue','purple','magenta','cyan'])
# 	days = ["Mon.","Tues.","Wed.","Thurs.","Fri.","Sat.","Sun.","None"]
# 	daysResults = []
# 	# for x in range(weeks):
# 	students = 40
# 	for washed in range(students):
# 		whichDay()
# 		whichTime()
# 		ER()
# 		if er == 'Yes':
# 			dataNONE.append("None")
# 		elif day == 'Monday':
# 			dataMon.append(time)
# 		elif day == 'Tuesday':
# 			dataTues.append(time)
# 		elif day == 'Wednesday':
# 			dataWed.append(time)
# 		elif day == 'Thursday':
# 			dataThurs.append(time)
# 		elif day == 'Friday':
# 			dataFri.append(time)
# 		elif day == 'Saturday':
# 			dataSat.append(time)
# 		else:
# 			dataSun.append(time)
# 		washed += 1
# 	daysResults.append(len(dataMon))
# 	daysResults.append(len(dataTues))
# 	daysResults.append(len(dataWed))
# 	daysResults.append(len(dataThurs))
# 	daysResults.append(len(dataFri))
# 	daysResults.append(len(dataSat))
# 	daysResults.append(len(dataSun))
# 	daysResults.append(len(dataNONE))
# 	plt.bar(days, daysResults, .8, color = colors)
# 	plt.title("Days Students With E&R Wash Their Clothes in Tenney")
# 	plt.savefig("laundry2.png")
# 	plt.show()
# 	return