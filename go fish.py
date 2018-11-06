import random

class Deck:
	def __init__(self):
		self.deck = []
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
		playerDeck = []
		for x in range(8):
			playerDeck.append(self.deck[x])
			status += "\n"+str(playerDeck[x][0])+" of "+str(playerDeck[x][1])
		status = "\nYour Cards:"+status
		return status

	def opponent(self):
		status = ""
		enemyDeck = []
		for x in range(8,16):
			enemyDeck.append(self.deck[x])
		status += "\nYour oppenent has "+str(len(enemyDeck))+" cards."
		return status

playerDeck = Deck()
enemyDeck = Deck()
print(playerDeck.player())
print(enemyDeck.opponent())