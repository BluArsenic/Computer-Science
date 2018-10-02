import random

w = int(input("Width: "))
h = int(input("Height: "))
b = int(input("Bombs: "))
m = []
for x in range(w):
	m.append(0)
for x in range(h):
	m[random.randint(0,w-1)] = "B"
	print(*m)
