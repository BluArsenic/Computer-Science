import random

w = 2 + int(input("Width: "))
# h = 2 + int(input("Height: "))
b = int(input("Bombs: "))
m = [[0]*w for x in range(w)]
for x in range(b):
	a = random.randrange(1,w-1)
	b = random.randrange(1,w-1)
	m[a][b] = "b"
	if m[a-1][b] is not "b":
		m[a-1][b] +=1
	else:
		m[a-1][b] == "b"
	if m[a-1][b-1] is not "b":
		m[a-1][b-1] +=1
	else:
		m[a-1][b-1] == "b"
	if m[a-1][b+1] is not "b":
		m[a-1][b+1] +=1
	else:
		m[a-1][b+1] == "b"
	if m[a][b+1] is not "b":
		m[a][b+1] +=1
	else:
		m[a][b-1] == "b"
	if m[a][b-1] is not "b":
		m[a][b-1] +=1
	else:
		m[a][b+1] == "b"
	if m[a+1][b] is not "b":
		m[a+1][b] +=1
	else:
		m[a+1][b] == "b"
	if m[a+1][b+1] is not "b":
		m[a+1][b+1] +=1
	else:
		m[a+1][b+1] == "b"
	if m[a+1][b-1] is not "b":
		m[a+1][b-1] +=1
	else:
		m[a+1][b-1] == "b"
	# if m[a][b] == "b":
	# 	m[a-1][b] +=1
	# 	m[a-1][b-1] +=1
	# 	m[a-1][b+1] +=1
	# 	m[a][b-1] +=1
	# 	m[a][b+1] +=1
	# 	m[a+1][b] +=1
	# 	m[a+1][b-1] +=1
	# 	m[a+1][b+1] +=1
del m[0]
del m[w-2]
for x in range(w-2):
	del m[x][0]
	del m[x][w-2]
for x in m:
	print(*x)