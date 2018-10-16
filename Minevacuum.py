#Dominic Thomas
#0ct 11, 2018
#Reredition of original Minesweeper code
#Help from the Couch People from Squire (Jackson,Roshni)

import random
true = True

#Solution Board
length = 2 + int(input("Length: "))
bombs = int(input("Bombs: "))
mine = [[0]*length for x in range(length)]
mine[0] = [*[1]*length]
mine[length-1] = [*[1]*length]
for x in range(bombs):
	wR = random.randrange(1,length-1)
	hR = random.randrange(1,length-1)
	mine[wR][hR] = "B"
	for i in range(-1,2):
		for j in range(-1,2):
			if i is 0 and j is 0:
				mine[wR-i][hR-j] = "B"
			elif mine[wR-i][hR-j] is not "B":
				mine[wR-i][hR-j] += 1
for x in range(length-1):
	mine[x][0] = 1
	mine[x][length-1] = 1

#Game Board
game = [["■"]*length for x in range(length)]
game[0] = [*[1]*length]
game[length-1] = [*[1]*length]
for x in range(length-1):
	game[x][0] = 1
	game[x][length-1] = 1
for x in game[1:-1]:
	print(*x[1:-1])

#Game Mechanics
while true:
	xcoord = int(input("X: "))
	ycoord = int(input("Y: "))
	choice = input("Flag (f) or Reveal (r)? ")
	choice = choice.lower()
	if choice == "r" and mine[ycoord][xcoord] == "B":
		print("You revealed a bomb. You lost!")
		true = False
	if choice == "r" and mine[ycoord][xcoord] == 0:
		game[ycoord][xcoord] = mine[ycoord][xcoord]
		check = [(xcoord,ycoord)]
		while len(check) > 0:
			temp = check.pop(0)
			xcoord = temp[0]
			ycoord = temp[1]
			for i in range(-1,2):
				for j in range(-1,2):
					if mine[ycoord-i][xcoord-j] == 0 and game[ycoord-i][xcoord-j] == '■':
						check.append((xcoord-j,ycoord-i))
					game[ycoord-i][xcoord-j] = mine[ycoord-i][xcoord-j]
	if choice == "r" and mine[ycoord][xcoord] > 0:
		game[ycoord][xcoord] = mine[ycoord][xcoord]
	if choice == "r" and game[ycoord][xcoord] != "B" and game[ycoord][xcoord] == mine[ycoord][xcoord]:
		print("You won!")
		true = False
	for x in game[1:-1]:
		print(*x[1:-1])