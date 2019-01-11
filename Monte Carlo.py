import random as r

location = []
x = 0
y = 0
for x in range(10):
    addX = r.randrange(-1,2,2)
    addY = r.randrange(-1,2,2)
    location = ((x+addX),(y+addY))
print(*location)