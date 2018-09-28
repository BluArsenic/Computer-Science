#2nd question
import random
from random import shuffle

l = [x for x in range(1,101)]

shuffle(l)
print(l)

#3rd question i have no idea
d = [x for x in range(0,101,2)]
e = [x for x in range(0,101,3)]
for i in d:
	if i not in e:
		e.append(i)

print(e)

#5th question
y = [x for x in range(0,101,2)]

print(y)