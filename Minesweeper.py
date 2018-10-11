#Dominic Thomas
#Oct 1, 2018
#Help from the Couch People from Squire (Jackson, Roshni)

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
	p[(y)-1][(x)-1] = m[(y)-1][(x)-1]
	p[(y)-1][(x)] = m[(y)-1][(x)]
	p[(y)-1][(x)+1] = m[(y)-1][(x)+1]
	p[(y)][(x)-1] = m[(y)][(x-1)]
	p[(y)][(x)] = m[(y)][(x)]
	p[(y)][(x)+1] = m[(y)][(x)+1]
	p[(y)+1][(x)-1] = m[(y)+1][(x)-1]
	p[(y)+1][(x)] = m[(y)+1][(x)]
	p[(y)+1][(x)+1] = m[(y)+1][(x)+1]

def hide():
	p[(y-1)-1][(x-1)-1] != m[(y-1)-1][(x-1)-1]
	p[(y-1)-1][(x-1)] != m[(y-1)-1][(x-1)]
	p[(y-1)-1][(x-1)+1] != m[(y-1)-1][(x-1)+1]
	p[(y-1)][(x-1)-1] != m[(y-1)][(x-1)-1]
	p[(y-1)][(x-1)] != m[(y-1)][(x-1)]
	p[(y-1)][(x-1)+1] != m[(y-1)][(x-1)+1]
	p[(y-1)+1][(x-1)-1] != m[(y-1)+1][(x-1)-1]
	p[(y-1)+1][(x-1)] != m[(y-1)+1][(x-1)]
	p[(y-1)+1][(x-1)+1] != m[(y-1)+1][(x-1)+1]

def newBoard():
	global p
	p = [["■"]*w for x in range(w)]
	p[0] = [*[1]*w]
	p[w-1] = [*[1]*w]
	for x in range(w-1):
		p[x][0] = 1
		p[x][w-1] = 1
	for x in p[1:-1]:
		print(*x[1:-1])
#Alt + 254 = ■

newBoard()

while t:
	x = int(input("X: "))
	y = int(input("Y: "))
	choice = input("Flag (f) or Reveal (r)? ")
	choice = choice.lower()
	if choice == "f":
		p[y-1][x-1] = "f"
		m[y-1][x-1] = "f"
		for i in p:
			print(*i)
		print("Remember, you have",bombs,"bombs in the board")
	elif choice == "r":
		p[y][x] = m[yy][xx]
		# if m[y-1][x-1] == 0:
		# 	check.append([x,y])
		# 	print(check)
		# while check:
		# 	check.pop(0)
		for i in range(-1,2):
			for j in range(-1,2):
				if m[(y)-i][(x)-j] >= 0:
					check.append([(x-i),(y-j)])
					p[(y)-i][(x)-j] = m[(y)-i][(x)-j]
				elif m[(y)-i][(x)-j] == "f":
					print("Please pick a new coordinate.")
					p[(y)-i][(x)-j] != m[(y)-i][(x)-j]
				elif m[(y)-i][(x)-j] == "b":
					p[(y)-i][(x)-j] != m[(y)-i][(x)-j]
				if m[((check[0][0]))-i][((check[0][1]))-j] == 0:
					# check.append([((check[0][0])-1)-i][((check[0][1])-1)-j])
					p[((check[0][0]))-i][((check[0][1]))-j] == m[((check[0][0])-1)-i][((check[0][1])-1)-j]
				elif m[(y)-i][(x)-j] == "b":
					print("Sorry. You lose! Better luck next time!")
					t = False
				print(m[check[0][0]][check[0][1]])
				print(check)
				# if m[check[0][0]][check[0][1]] == 0:
				# 	check.append([((check[0][0])-1)-i][((check[0][1])-1)-j])
				# 	p[((check[0][0])-1)-i][((check[0][1])-1)-j] == m[((check[0][0])-1)-i][((check[0][1])-1)-j]
				# elif m[y-i][x-j] != 0:
					# p[y-1][x-1] != m[y-1][x-1]
					# hide() 
		# 			c = (check[0][0])-1
		for x in p[1:-1]:
			print(*x[1:-1])
		print("Remember, you have",bombs,"bombs in the board")
	if p[yy][xx] == "b" and choice == "r":
		print("Sorry. You lose! Better luck next time!")
		t = False
	# for i in range(bombs):
	# 	if m[a][b] == "f":
	# 		print("You flagged all the bombs. You won!")
	# 		t = False