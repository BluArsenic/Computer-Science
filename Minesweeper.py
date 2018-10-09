import random

t = True
g = 0
w = 2 + int(input("Length: "))
# h = 2 + int(input("Height: "))
bombs = int(input("Bombs: "))
m = [[0]*w for x in range(w)]
check = []
for x in range(bombs):
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
del m[0]
del m[w-2]
for x in range(w-2):
	del m[x][0]
	del m[x][w-2]

def reveal():
	p[(y-1)-1][(x-1)-1] = m[(y-1)-1][(x-1)-1]
	p[(y-1)-1][(x-1)] = m[(y-1)-1][(x-1)]
	p[(y-1)-1][(x-1)+1] = m[(y-1)-1][(x-1)+1]
	p[(y-1)][(x-1)-1] = m[(y-1)][(x-1)-1]
	p[(y-1)][(x-1)] = m[(y-1)][(x-1)]
	p[(y-1)][(x-1)+1] = m[(y-1)][(x-1)+1]
	p[(y-1)+1][(x-1)-1] = m[(y-1)+1][(x-1)-1]
	p[(y-1)+1][(x-1)] = m[(y-1)+1][(x-1)]
	p[(y-1)+1][(x-1)+1] = m[(y-1)+1][(x-1)+1]

def revealAdd():
	check.append(m[(y-1)-1][(x-1)-1])
	check.append(m[(y-1)-1][(x-1)])
	check.append(m[(y-1)-1][(x-1)+1])
	check.append(m[(y-1)][(x-1)-1])
	check.append(m[(y-1)][(x-1)])
	check.append(m[(y-1)][(x-1)+1])
	check.append(m[(y-1)+1][(x-1)-1])
	check.append(m[(y-1)+1][(x-1)])
	check.append(m[(y-1)+1][(x-1)+1])

#New Board
p = [["■"]*w for x in range(w)]
del p[0]
del p[w-2]
for x in range(w-2):
	del p[x][0]
	del p[x][w-2]
for x in p:
	print(*x)
#Alt + 254 = ■

while t:
	x = int(input("X: "))
	y = int(input("Y: "))
	choice = input("Flag (f) or Reveal (r)? ")
	choice = choice.lower()
	if choice == "f":
		p[y-1][x-1] = "f"
		for i in p:
			print(*i)
		print("Remember, you have",bombs,"bombs in the board")
	elif choice == "r":
		p[y-1][x-1] = m[y-1][x-1]
		check.append([x,y])
		print(check)
		while check:
			check.pop(0)
			for i in range(w-2):
				for j in range(w-2):
					if p[y-1][x-1] == m[y-1][x-1]:
						reveal()
		revealAdd()
		for i in p:
			print(*i)
		print("Remember, you have",bombs,"bombs in the board")
	if p[y-1][x-1] == "b" and choice == "r":
		print("Sorry. You lose! Better luck next time!")
		t = False
	for i in range(bombs):
		if m[a][b] == "f":
			print("You flagged all the bombs. You won!")
			t = False