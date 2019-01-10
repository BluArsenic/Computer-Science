'''
In terms of actually playing the game, I think it depends whether or not you should stick with
the box you chose initially or switch because it's a 50/50
chance, but also you could have different feelings each
round about switching
'''
from random import shuffle
import random as r
import collections as c

#Trials where you switch the box
def switch(runs):
	global r # To be able to use the random module
	times = 0 # Starts of zero rounds completed
	chosen = [] # Chosen boxes go in this list
	# Adds pennies and keys to boxes
	while times < runs:
		box = []
		for x in range(3):
			if x is 0 or x is 1:
				x == "Penny"
			if x is 2:
				x == "KEYS!!"
			box.append(x)
		# Shuffles boxes
		shuffle(box)
		# "Chooses" box
		chosen.append(box.pop(r.randrange(3)))
		variable = r.randrange(len(box))
		# "Reveals" one of the penny boxes; deletes that penny box from the box list
		if box[variable] is 0 or box[variable] is 1: #2 is current length of box list
			del box[variable]
		# "Switches" chosen box
		box.append(chosen.pop(-1))
		chosen.append(box.pop(0))
		# Resets boxes for next round
		box = []
		# Oe trial completed
		times += 1
		# Prints how many times you chose keys (2) or pennies (0 or 1)
	print(c.Counter(chosen))

switch(1000)

#Trials where you don't switch the box
def stickWith(runs):
	global r
	times = 0
	chosen = []
	while times < runs:
		box = []
		for x in range(3):
			if x is 0 or x is 1:
				x == "Penny"
			if x is 2:
				x == "KEYS!!"
			box.append(x)
		shuffle(box)
		#"Chooses" box 
		chosen.append(box.pop(r.randrange(3)))
		#Resets box for the next round
		box = []
		#"Moves to the next trial"
		times += 1
	print(c.Counter(chosen))

stickWith(1000)

'''
I was surprised that your twice as likely to win
when switching, but I wasn't surprised seeing the results of
keeping your box since the every trial is basically a 33/33/33 chance.
'''