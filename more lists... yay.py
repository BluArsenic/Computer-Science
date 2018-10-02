#3x3 list; three values in each list, three lists
i = [[1,2,3],[4,5,6],[7,8,9]]
print(*i[0])
print(i[0][0])

j = []
for x in range(10):
	j.append(0)
print(j)

j = [0]*10
print(j)
#equivalent of lines 6, 7, and 8

j = [[0]*10 for x in range(10)]
print(j)

j = []
for x in range(10):
	k = [0]*10
	j.append(*k)
print(*j)
#equivalent to line 15

print(len(j))

for x in range(len(j)):
	print(j[x])
for x in j:
	print(*x)