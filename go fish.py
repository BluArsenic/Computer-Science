import random

class Deck:
	def __init__(self):
		self.deck = []
		self.playerDeck = []
		self.enemyDeck = []
		for i in range(1,14):
			for j in range(1,5):
				if i is 1:
					i = "Ace"
				elif i is 11:
					i = "Jack"
				elif i is 12:
					i = "Queen"
				elif i is 13:
					i = "King"
				if j is 1:
					j = "Clubs"
				elif j is 2:
					j = "Diamonds"
				elif j is 3:
					j = "Hearts"
				elif j is 4:
					j = "Spades"
				self.deck.append((i,j))
		self.shuffle()

	def shuffle(self):
		random.shuffle(self.deck)

	def player(self):
		status = ""
		for x in range(7):
			self.playerDeck.append(self.deck[x])
			status += "\n"+str(self.playerDeck[x][0])+" of "+str(self.playerDeck[x][1])
		status = "\nYour Cards:"+status
		return status

	def opponent(self):
		status = ""
		for x in range(8,15):
			self.enemyDeck.append(self.deck[x])
		status += "\nYour oppenent has "+str(len(self.enemyDeck))+" cards."
		return status

	def match(self, x, y):
		status = ""
		playerMatch = []
		if self.playerDeck[x][0] == self.playerDeck[y][0]:
			playerMatch += self.playerDeck.pop(x)
			playerMatch += self.playerDeck.pop(y)
		for x in range(len(playerDeck)):
			status = "\nYour Cards:\n"+str(self.playerDeck[x][0])+" of "+str(self.playerDeck[x][1])
		for x in range(len(playerMatch)):
			matches = "\nYou have "+(len(playerMatch)/2)+" matches."
		print(matches)
		return status

playerDeck = Deck()
enemyDeck = Deck()
print(playerDeck.player())
print(enemyDeck.opponent())
askMatch = input("Are there any matching cards? Y or N: ")
askMatch = askMatch.lower()
if askMatch == "y":
	inputOne = int(input("Enter the position of the first matching card: "))-1
	inputTwo = int(input("Enter the position of the second matching card: "))-1
	print(playerDeck.match(inputOne, inputTwo))
else:
	print(playerDeck.player())
	print(enemyDeck.opponent())