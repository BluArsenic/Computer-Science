'''
1) FLip a coin (heads or tails)
2) Count the amount of times it lands on heads
3) Separate the amount of coin flips by how many times you land on heads
4) Put it in a graph
'''
import random
import collections as c
import matplotlib.pyplot as pyp

i = 0
j = 0
# with counter
while i<1000:
	data = []
	for x in range(10):
		coin = random.randint(1,2)
		if coin is 1:
			data.append(coin)
	print(c.Counter(data))
	i += 1

pyp.plot(data)
pyp.show()

# without counter
# while j<10:
# 	data = [] # data of coin flips
# 	dataHead = [] # data of "heads" amount
# 	dataNum = [] # data of of how many heads in numbers
# 	for x in range(10):
# 		coin = random.randint(1,2)
# 		if coin is 1:
# 			coin == "Heads"
# 			data.append(coin)
# 			dataHead.append(coin)
# 		elif coin is 2:
# 			coin == "Tails"
# 			data.append(coin)
# 	dataNum.append(len(dataHead))
# 	# print(data)
# 	print(dataNum)
# 	j += 1