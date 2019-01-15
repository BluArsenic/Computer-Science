'''
If you go to ___ parties over winter break and 
eat ___ desserts, and each dessert has ___ calories
how many calories have you consumed?
'''

import random as r
import matplotlib.pyplot as plt

def winterBreak(breaks):
	global r, calData
	times = 0
	calData = []
	while times < breaks:
		parties = r.randint(1,10)
		calIntake = 0
		for attend in range(parties):
			desserts = r.randint(1,8)
			for eat in range(desserts):
				calories = r.randint(40,500)
				calIntake += calories
		calData.append(calIntake)
		times += 1
	return calData

breaks = 100
print(winterBreak(breaks))

# figure out how to switch axes
plt.plot(calData)
plt.show()
