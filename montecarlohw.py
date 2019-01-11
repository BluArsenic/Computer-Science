'''
The longest walk you can take where you will be
withing walking distance of home at least 50% of
the time is 22 blocks
'''
'''
A Monte Carlo simulation is a mathematical technique
used to calculate the risk of an event. It lets
you see all the possible outcomes of your decisions
allowing for better decision making.
'''

#distance formula = math.sqrt(((x2-x1)**2))+((y2-y1)**2))

import random as r
import math

def dartboard(throws):
	global r
	times = 0 #amount of times ran
	success = 0 # in the circle
	while times < throws:
		x , xC = 0 , 0
		y , yC = 0 , 0
		center = (xC,yC)
		dart = (x,y)
		radius = 1
		throwDart = (r.uniform(-1,1),r.uniform(-1,1))
		(x,y) = throwDart
		dartRad = math.sqrt(((x-xC)**2)+((y-yC)**2))
		if dartRad < radius:
			success += 1
		times += 1
	return (success*4)/throws

print(dartboard(100000))

# 100 times, the number was always around 3
# 1000 times, the number is still around 3
# Same for 10000
# Same for 100000
