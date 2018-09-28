import random

#empty list
a = []

#print list
print(a)

# adding to the list
a.append(5)
a.append(3)
a.append(8)

print(a)

#a += [1,2,3,4,5]

#print(a)

a = [1,2,3,4,5] + a

print(a)

#inserts values into the list
a.insert(0,[1,2,3,4,5])

print(a)
print(a[0]) #first position of the list
print(a[-1]) #first position counting from the end
#print(a[8]) out of range

#remvoes from the list
del a[0]
#a[n:] deletes everything after and including n
#a[:n] deletes everything before, excluding, n
#a[n:n2] deletes everything after, inlcuding, n and before, excluding, n2
print(a.pop(4)) #deletes value and returns it

print(a)

print(len(a))

#remove random values form list
x = random.randint(0,len(a)-1)
del a[x]
print(a)
print(a[-1])

# y = 5
# z = 10
# temp = y
# y = z
# z = temp

y,z = 5,10
y,z = z,y

a[0],a[-1] = a[-1],a[0]
print(a)

sevens = []
for i in range(7,701,7): #inclusive,exclusive,intervals
	sevens.append(i)

print(*sevens, len(sevens)) # *removes brackets

b = []
for i in range(1,5):
	b.append(i)

print(b)

#does the same thing as the top 3 lines
c = [x for x in range(0,2000,5)]
print(c)